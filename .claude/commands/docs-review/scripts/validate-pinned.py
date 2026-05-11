#!/usr/bin/env python3
"""validate-pinned.py — validate a rendered pinned-review body.

Runs 21 deterministic structural and computational invariants on the rendered
review body BEFORE pinned-comment.sh upsert publishes it. On violations, writes
a structured fix-me marker (JSON + rendered markdown) and exits 1; the caller
re-renders and re-runs.

Subcommands:
  check  --body-file <path> --pr <N> [--repo <owner/repo>]
         [--output-json <path>] [--output-markdown <path>]
                       Run all 21 checks. On violations, write fix-me marker
                       and exit 1; otherwise exit 0.
  show-rules           Print the rule registry (id, description, hint).
  schema-version       Print the validator's schema version.

Exit codes:
  0  no violations
  1  violations (fix-me marker written)
  2  usage / config error

Schema version: 6
"""

from __future__ import annotations

import argparse
import json
import re
import statistics
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

SCHEMA_VERSION = 7

DEFAULT_OUTPUT_JSON = "/tmp/validate-pinned.fix-me.json"
DEFAULT_OUTPUT_MARKDOWN = "/tmp/validate-pinned.fix-me.md"

# Mandatory H3 sections in the order they must appear in any review body. Mirror
# of `references/output-format.md` L81 — keep these synchronized; the schema-
# version bump catches drift.
MANDATORY_H3_SECTIONS = [
    "🔍 Verification trail",
    "🚨 Outstanding",
    "⚠️ Low-confidence",
    "📜 Review history",
]
# Conditional sections. Editorial balance is mandatory only on content/blog/**.
# Its conditional presence is checked via dedicated rules, not the order check.

# 8 mandatory investigation-log bullets, in order (output-format.md §Investigation log).
INVESTIGATION_LOG_BULLETS = [
    "Cross-sibling reads",
    "External claim verification",
    "Cited-claim spot-checks",
    "Frontmatter sweep",
    "Temporal-trigger sweep",
    "Code execution",
    "Code-examples checks",
    "Editorial-balance pass",
]

# Recognized investigation-log line shapes. Each bullet must match exactly one.
INVESTIGATION_STATE_PATTERNS = [
    re.compile(r"^\d+ of \d+\b"),                # "X of Y..."
    re.compile(r"^ran\b"),                        # "ran ..."
    re.compile(r"^not run\b"),                    # "not run (...)"
]

# Temporal-trigger word list (output-format.md / fact-check.md temporal sweep).
TEMPORAL_TRIGGERS = {
    "recently", "now supports", "now available", "new", "just launched",
    "latest", "introduced", "as of", "starting", "going forward",
}

# Dispatch-metadata format on the External claim verification line
# (output-format.md L122). Two segments are required, matched independently:
# the extraction-side specialists tail and the routed-verification tail.
# Schema v3: routed-metadata replaces the v2 PASS_METADATA_RE (pass-1/pass-2
# breakdown). With the routing change in S33 Change 4, claims now dispatch
# by `source_class` to one of three lanes -- inline, Pass 1, Pass 2.
# Schema v5: Pass 2 (URL fetch) is now subdivided from Pass 3 (search-then-
# fetch). Pass 3 segment is optional in the regex for backward compat with
# v4 captures (which carry no `, S Pass 3` segment); v5 captures render the
# four-lane form per `docs-review:references:output-format`.
DISPATCH_METADATA_RE = re.compile(
    r"\d+ specialists \([^)]+\); \d+ cross-specialist corroborations"
)
ROUTED_METADATA_RE = re.compile(
    r"routed: \d+ inline, \d+ Pass 1, \d+ Pass 2"
)
# Schema v4: when Pass 2 count F > 0, the routed-metadata segment carries an
# attribution parenthetical breaking F into verified / contradicted /
# unverifiable. Inline + Pass 1 verdicts are already aggregated in the leading
# `(N unverifiable, M contradicted)` parenthetical; Pass 2 is the lane where
# verdict drift across runs is observable, so per-lane attribution there is
# the load-bearing observability for cost-variance analysis. Schema v5
# extends the same attribution to Pass 3 via parallel ROUTED_PASS3_RE /
# PASS3_OUTCOME_RE patterns.
ROUTED_PASS2_RE = re.compile(
    r"routed: \d+ inline, \d+ Pass 1, (\d+) Pass 2"
)
PASS2_OUTCOME_RE = re.compile(
    r"\d+ Pass 2 \(verified (\d+), contradicted (\d+), unverifiable (\d+)\)"
)
ROUTED_INLINE_PASS1_RE = re.compile(
    r"routed: (\d+) inline, (\d+) Pass 1"
)
ROUTED_PASS3_RE = re.compile(
    r", (\d+) Pass 3\b"
)
PASS3_OUTCOME_RE = re.compile(
    r"\d+ Pass 3 \(verified (\d+), contradicted (\d+), unverifiable (\d+)\)"
)
LEADING_STATE_RE = re.compile(
    r"(\d+)\s+of\s+(\d+)\s+claims\s+verified\b"
)


@dataclass
class Violation:
    rule_id: str
    line_ref: str  # e.g., "L42-L58", "table", "<section>"
    expected: str
    actual: str
    hint: str

    def to_dict(self) -> dict:
        return {
            "rule_id": self.rule_id,
            "line_ref": self.line_ref,
            "expected": self.expected,
            "actual": self.actual,
            "hint": self.hint,
        }


@dataclass
class Context:
    body: str
    body_lines: list[str]
    pr: int | None
    repo: str | None
    diff_files: list[str]
    diff_files_added: set[str]
    diff_text: str
    repo_root: Path
    is_blog: bool
    # Schema v5: workflow pre-step `extract-urls-and-fetch.py` writes the
    # fetched URLs here. None means the file wasn't present (e.g., local
    # invocation with no PR diff context); empty list means the workflow
    # ran but the diff had no external URLs in content/(docs|blog)/**/*.md.
    fetched_urls: list[dict] | None = None
    # Schema v5: workflow pre-step `editorial-balance-detect.py` writes
    # Tier 1 stats here (trigger, sections, mean/median/std, outliers).
    # None means the file wasn't present; otherwise a dict with keys
    # `trigger`, `files`. Used by `editorial-balance-counts-faithful`.
    editorial_balance: dict | None = None
    # Schema v7: the merged claim-extraction artifact `.candidate-claims.json`
    # (regex floor ∪ two Sonnet passes). None means the file wasn't present
    # (local mode or workflow didn't run the pre-step); otherwise the parsed
    # `claims` list (possibly empty — the pre-step ran but found nothing).
    # Used by `candidate-claims-coverage` and by the 0-claim relaxation in
    # `trail-bucket-consistency`.
    candidate_claims: list[dict] | None = None


# ---- Body parsing helpers --------------------------------------------------


def find_section(body: str, heading_substring: str) -> tuple[int, int] | None:
    """Return (start_line, end_line) of the H3 section whose heading contains `heading_substring`.

    end_line is exclusive (the line of the next H3 or end-of-body).
    Returns None if not found.
    """
    lines = body.splitlines()
    start = None
    for i, line in enumerate(lines):
        if line.startswith("### ") and heading_substring in line:
            start = i
            break
    if start is None:
        return None
    end = len(lines)
    for j in range(start + 1, len(lines)):
        if lines[j].startswith("### "):
            end = j
            break
    return (start, end)


def extract_bucket_bullets(body: str, heading_substring: str) -> list[str]:
    """Return the lines that look like top-level bucket findings in a given H3 section.

    A bucket finding is a column-0 line that starts with `**` (any of: spec
    `- **[L<a>-<b>]**`, legacy `- **content/foo.md L40-50**`, numbered
    `**1. L40 ...`, or bare-bold `**L40 ...`). The trail-record prefix mandate
    is enforced separately by check_trail_bucket_consistency; this function
    counts every top-level finding paragraph so the count-table check stays
    accurate across format variants.

    Sub-bullets (indented), continuation paragraphs (no leading `**`), and
    style-finding bullets (`- **line N:**`) are still counted as findings —
    style findings belong in the ⚠️ count per the S32 mandate.
    """
    span = find_section(body, heading_substring)
    if span is None:
        return []
    start, end = span
    bullets = []
    # Match any column-0 line starting with `**` (with optional `- ` prefix).
    finding_re = re.compile(r"^(?:- )?\*\*\S")
    for line in body.splitlines()[start:end]:
        if finding_re.match(line):
            bullets.append(line)
    return bullets


def section_text(body: str, heading_substring: str) -> str:
    """Return the full text of an H3 section (excluding heading)."""
    span = find_section(body, heading_substring)
    if span is None:
        return ""
    start, end = span
    return "\n".join(body.splitlines()[start + 1:end])


def extract_count_table_row(body: str) -> dict[str, int] | None:
    """Parse the `| **N** | **N** | **N** | **N** |` row.

    Returns {outstanding, low_confidence, pre_existing, resolved} or None.
    """
    # The row sits between the header (with 🚨 / ⚠️ / 💡 / ✅) and the next blank
    # line. We find the header line, then the data row two lines down (after
    # the separator).
    lines = body.splitlines()
    for i, line in enumerate(lines):
        if "🚨 Outstanding" in line and "⚠️ Low-confidence" in line and "|" in line:
            # Data row is i+2 (i is header, i+1 is separator)
            if i + 2 < len(lines):
                row = lines[i + 2]
                cells = [c.strip().strip("*") for c in row.split("|") if c.strip()]
                if len(cells) >= 4:
                    try:
                        return {
                            "outstanding": int(cells[0]),
                            "low_confidence": int(cells[1]),
                            "pre_existing": int(cells[2]),
                            "resolved": int(cells[3]),
                        }
                    except ValueError:
                        return None
    return None


def extract_trail_records(body: str) -> list[dict]:
    """Pull line-anchored verdicts out of 🔍 Verification trail.

    Returns list of {line_ref, line_refs, verdict, raw} dicts where line_ref is
    the *first* L<n> or L<a>-<b> anchor on the line and line_refs is *all* of
    them (collapsed frontmatter-sweep entries cite several locations on one
    line — e.g. `- L12 "..." (also L88, L91) → ✅ matches`). verdict is one of
    ✅ / ⚠️ / 🚨.
    """
    span = find_section(body, "🔍 Verification trail")
    if span is None:
        return []
    start, end = span
    records = []
    for raw in body.splitlines()[start:end]:
        m = re.search(r"L(\d+(?:-\d+)?)\b.*?→\s*(✅|⚠️|🚨)\s+(\S[^\n]*)", raw)
        if m:
            # Pull every L<a>[-<b>] token on the line — the verdict applies to
            # all of them (frontmatter-sweep collapse).
            all_refs = re.findall(r"L\d+(?:-\d+)?", raw)
            records.append({
                "line_ref": f"L{m.group(1)}",
                "line_refs": all_refs or [f"L{m.group(1)}"],
                "verdict_emoji": m.group(2),
                "verdict_text": m.group(3),
                "raw": raw,
            })
    return records


def extract_bullet_prefix(line: str) -> str | None:
    """Return the `[L<a>-<b>]` or `[L<n>]` prefix of a bucket bullet, if any."""
    m = re.match(r"^\s*-\s+\*\*\[(L\d+(?:-\d+)?)\]\*\*", line)
    return m.group(1) if m else None


# ---- Check functions -------------------------------------------------------


def check_count_table_matches_bullets(ctx: Context) -> list[Violation]:
    counts = extract_count_table_row(ctx.body)
    if counts is None:
        return [Violation(
            rule_id="count-table-present",
            line_ref="<bucket count table>",
            expected="A `| **N** | **N** | **N** | **N** |` row under the 🚨/⚠️/💡/✅ header",
            actual="missing or unparseable",
            hint="Render the bucket count table as 4 bold integers in a markdown table row, in order Outstanding/Low-confidence/Pre-existing/Resolved.",
        )]

    actual_outstanding = len(extract_bucket_bullets(ctx.body, "🚨 Outstanding"))
    actual_low = len(extract_bucket_bullets(ctx.body, "⚠️ Low-confidence"))
    actual_pre = len(extract_bucket_bullets(ctx.body, "💡 Pre-existing"))
    actual_resolved = len(extract_bucket_bullets(ctx.body, "✅ Resolved"))

    violations = []
    for label, table_val, actual_val in [
        ("outstanding", counts["outstanding"], actual_outstanding),
        ("low_confidence", counts["low_confidence"], actual_low),
        ("pre_existing", counts["pre_existing"], actual_pre),
        ("resolved", counts["resolved"], actual_resolved),
    ]:
        if table_val != actual_val:
            violations.append(Violation(
                rule_id="count-table-matches-bullets",
                line_ref=f"<bucket count table — {label}>",
                expected=f"{label} count = {actual_val} (number of bullets in the section)",
                actual=f"table shows {table_val}",
                hint=f"Recount the bullets in the {label} section (including any style findings under #### Style findings for ⚠️) and update the table cell.",
            ))
    return violations


def check_investigation_log_bullets(ctx: Context) -> list[Violation]:
    """8 mandatory bullets present, in order, each in a recognized format."""
    # Find the Investigation log <details> block.
    body_lines = ctx.body.splitlines()
    log_start = None
    log_end = None
    for i, line in enumerate(body_lines):
        if "<summary>Investigation log</summary>" in line:
            log_start = i + 1
        elif log_start is not None and line.strip() == "</details>":
            log_end = i
            break
    if log_start is None or log_end is None:
        return [Violation(
            rule_id="investigation-log-block-present",
            line_ref="<investigation log>",
            expected="A `<details><summary>Investigation log</summary>...</details>` block",
            actual="missing",
            hint="Render the Investigation log as a collapsed <details> block under the Review confidence table.",
        )]

    log_lines = body_lines[log_start:log_end]

    # Each bullet should appear in order. Track positions.
    found_positions: dict[str, int] = {}
    line_states: dict[str, str] = {}
    for i, raw in enumerate(log_lines):
        stripped = raw.lstrip()
        if not stripped.startswith("- **"):
            continue
        for bullet_name in INVESTIGATION_LOG_BULLETS:
            if f"- **{bullet_name}" in stripped:
                found_positions[bullet_name] = i
                # Pull the state portion (after "**: " or "** — ").
                m = re.match(r"^\s*-\s+\*\*[^*]+\*\*[:\s—\-]+(.+?)\s*$", raw)
                line_states[bullet_name] = m.group(1) if m else ""
                break

    violations: list[Violation] = []
    # Missing bullets.
    for name in INVESTIGATION_LOG_BULLETS:
        if name not in found_positions:
            violations.append(Violation(
                rule_id="investigation-log-bullets-present",
                line_ref="<investigation log>",
                expected=f"a bullet starting with `- **{name}**`",
                actual="missing",
                hint=f"Add the `- **{name}**` bullet with one of the recognized states (`X of Y`, `ran ...`, or `not run (...)`).",
            ))

    # Order check.
    expected_order = [n for n in INVESTIGATION_LOG_BULLETS if n in found_positions]
    actual_order = sorted(found_positions, key=lambda n: found_positions[n])
    if expected_order != actual_order:
        violations.append(Violation(
            rule_id="investigation-log-bullets-order",
            line_ref="<investigation log>",
            expected=" → ".join(INVESTIGATION_LOG_BULLETS),
            actual=" → ".join(actual_order),
            hint="Re-order the investigation-log bullets to match the spec (Cross-sibling reads → External claim verification → Cited-claim spot-checks → Frontmatter sweep → Temporal-trigger sweep → Code execution → Code-examples checks → Editorial-balance pass).",
        ))

    # State-format check.
    for name, state in line_states.items():
        if not any(p.match(state) for p in INVESTIGATION_STATE_PATTERNS):
            violations.append(Violation(
                rule_id="investigation-log-bullet-state",
                line_ref=f"<investigation log: {name}>",
                expected="state begins with `X of Y`, `ran`, or `not run`",
                actual=state[:80],
                hint=f"Rewrite the `{name}` bullet's state as one of `X of Y ...`, `ran ...`, or `not run (<reason>)`.",
            ))
    return violations


def check_cross_sibling_math(ctx: Context) -> list[Violation]:
    """Cross-sibling reads line: `X of Y siblings (a, b, ...; skipped d, e)`.

    count(named-read) == X; count(read) + count(skipped) == Y. Only runs when
    the parenthetical contains a `;` separator (the explicit `read; skipped`
    form). Free-form parentheticals like "(5 SAML guides, 3 SCIM guides)" are
    group labels, not enumerated reads — skip the math check there.
    """
    for line in ctx.body_lines:
        if "Cross-sibling reads" not in line:
            continue
        m = re.search(
            r"(\d+) of (\d+) siblings\s*\(([^;)]+);\s*skipped\s+([^)]*)\)",
            line,
        )
        if not m:
            return []  # no `;skipped` form — not subject to math check

        x, y = int(m.group(1)), int(m.group(2))
        read_list = [s.strip() for s in m.group(3).split(",") if s.strip()]
        skipped_list = [s.strip() for s in m.group(4).split(",") if s.strip()]

        violations: list[Violation] = []
        if len(read_list) != x:
            violations.append(Violation(
                rule_id="cross-sibling-read-count",
                line_ref="<investigation log: Cross-sibling reads>",
                expected=f"X={x} matches the number of named-read siblings ({len(read_list)})",
                actual=f"X={x} but parenthetical names {len(read_list)} read siblings: {read_list}",
                hint=f"Either change the leading X to {len(read_list)} or list all {x} siblings actually read.",
            ))
        if len(read_list) + len(skipped_list) != y:
            violations.append(Violation(
                rule_id="cross-sibling-total-count",
                line_ref="<investigation log: Cross-sibling reads>",
                expected=f"Y={y} matches read + skipped ({len(read_list) + len(skipped_list)})",
                actual=f"Y={y} but read={len(read_list)}, skipped={len(skipped_list)}",
                hint=f"Either change Y to {len(read_list) + len(skipped_list)} or list all skipped siblings explicitly.",
            ))
        return violations
    return []


def check_style_render_mode(ctx: Context) -> list[Violation]:
    """Style-findings render mode matches the relaxed rule from output-format.md L252-258."""
    span = find_section(ctx.body, "⚠️ Low-confidence")
    if span is None:
        return []
    start, end = span
    section_lines = ctx.body_lines[start:end]
    section_text = "\n".join(section_lines)

    # Locate #### Style findings sub-section.
    style_idx = None
    for i, line in enumerate(section_lines):
        if line.strip() == "#### Style findings":
            style_idx = i
            break
    if style_idx is None:
        return []  # no style findings — render-mode N/A

    style_lines = section_lines[style_idx:]
    # Count bullets and detect <details> blocks.
    bullet_count = sum(1 for ln in style_lines if ln.lstrip().startswith("- **line "))
    file_count = sum(1 for ln in style_lines if ln.lstrip().startswith("<summary>"))
    has_details = any("<details>" in ln for ln in style_lines)

    # Determine actual mode.
    actual_mode = "collapse-all" if has_details else "inline-all"

    # Determine expected mode per the relaxed rule:
    # inline-all when (a) total ≤5 OR (b) concentrate in one file AND total ≤30
    # collapse-all when files >1 AND total >5, OR total >30
    if bullet_count <= 5:
        expected_mode = "inline-all"
    elif file_count <= 1 and bullet_count <= 30:
        expected_mode = "inline-all"
    elif file_count > 1 and bullet_count > 5:
        expected_mode = "collapse-all"
    elif bullet_count > 30:
        expected_mode = "collapse-all"
    else:
        expected_mode = actual_mode  # ambiguous — don't flag

    if actual_mode != expected_mode:
        return [Violation(
            rule_id="style-render-mode",
            line_ref="<#### Style findings>",
            expected=f"{expected_mode} mode (bullets={bullet_count}, files={file_count})",
            actual=f"{actual_mode} mode rendered",
            hint=(
                "Re-render style findings inline (no <details>) — total ≤5 or concentrated in one file."
                if expected_mode == "inline-all"
                else "Re-render style findings inside per-file <details> blocks with the per-file roll-up summary."
            ),
        )]
    return []


def check_mandatory_h3_order(ctx: Context) -> list[Violation]:
    """Mandatory H3 sections present, in order. Editorial balance is conditional on blog."""
    expected = list(MANDATORY_H3_SECTIONS)
    if ctx.is_blog:
        # 📊 Editorial balance sits between Verification trail and 🚨 Outstanding.
        idx = expected.index("🚨 Outstanding")
        expected.insert(idx, "📊 Editorial balance")

    actual_h3s = [
        line[4:].strip()
        for line in ctx.body_lines
        if line.startswith("### ")
    ]

    violations: list[Violation] = []
    # Presence + order: walk expected, advance through actual, fail on missing.
    cursor = 0
    for need in expected:
        found = False
        while cursor < len(actual_h3s):
            if need in actual_h3s[cursor]:
                cursor += 1
                found = True
                break
            cursor += 1
        if not found:
            violations.append(Violation(
                rule_id="mandatory-h3-order",
                line_ref=f"<### {need}>",
                expected=f"`### {need}` present after the previously-rendered mandatory section",
                actual="missing or out-of-order",
                hint=f"Render `### {need}` in the spec order. Use the explicit-empty form if the section has no content (per output-format.md §Verification trail empty form, etc.).",
            ))
            cursor = 0  # restart so we still check later sections

    return violations


def _external_claim_line(ctx: Context) -> str | None:
    """Find the External claim verification investigation-log line, or None if not applicable.

    Returns None when the bullet is absent, `not run`, malformed (no canonical
    `X of Y claims verified` state — `external-claim-state-format` carries that
    violation), or `0 of 0` (no claims extracted — dispatch metadata not applicable).
    Strict word-boundary on `claims\\b` to reject near-canonical drift like
    "N of M verifiable claims verified".
    """
    for line in ctx.body_lines:
        stripped = line.lstrip()
        if not stripped.startswith("- **External claim verification"):
            continue
        if "not run" in line:
            return None
        m = re.search(r"\d+\s+of\s+(\d+)\s+claims\s+verified\b", line)
        if not m:
            return None
        if int(m.group(1)) == 0:
            return None
        return line
    return None


def check_external_claim_state_format(ctx: Context) -> list[Violation]:
    """External claim verification bullet uses the canonical 'X of Y claims verified' state form.

    The dispatch-metadata and pass-metadata checks can only attach to a canonically
    shaped line; if the state form drifts (e.g., model writes 'ran (N claims, ...)'
    or 'N of M verifiable claims verified'), they silently no-op. This check is the
    fail-loud gate that surfaces the drift before the silent-skip.
    """
    for line in ctx.body_lines:
        stripped = line.lstrip()
        if not stripped.startswith("- **External claim verification"):
            continue
        if "not run" in line:
            return []
        if re.search(r"\d+\s+of\s+\d+\s+claims\s+verified\b", line):
            return []
        return [Violation(
            rule_id="external-claim-state-format",
            line_ref="<investigation log: External claim verification>",
            expected="line uses canonical `X of Y claims verified (N unverifiable, M contradicted)` state form",
            actual=line.strip()[:160],
            hint="Render the bullet as `X of Y claims verified (N unverifiable, M contradicted) · 4 specialists (...); K cross-specialist corroborations · Pass 1: A verified, B deferred; Pass 2: C verified, D unverifiable.` or as `not run (<reason>)`. Compaction (e.g., `single-pass`, `ran (N claims, ...)`, `N of M verifiable claims verified`) is not permitted.",
        )]
    return []


def check_external_claim_dispatch_metadata(ctx: Context) -> list[Violation]:
    """Investigation-log External claim verification line includes the extraction-specialists tail.

    Required segment: `N specialists (numerical, cross-reference, capability, framing); K cross-specialist corroborations`.
    """
    line = _external_claim_line(ctx)
    if line is None or DISPATCH_METADATA_RE.search(line):
        return []
    return [Violation(
        rule_id="external-claim-dispatch-metadata",
        line_ref="<investigation log: External claim verification>",
        expected="line includes `N specialists (numerical, cross-reference, capability, framing); K cross-specialist corroborations`",
        actual=line.strip()[:160],
        hint="Append the extraction dispatch metadata to the External claim verification bullet: e.g., `· 4 specialists (numerical, cross-reference, capability, framing); 2 cross-specialist corroborations`.",
    )]


def check_external_claim_routed_metadata(ctx: Context) -> list[Violation]:
    """Investigation-log External claim verification line includes the routed-verification tail.

    Required segment: `routed: I inline, P Pass 1, F Pass 2`. Counts how many claims
    took each verification lane (inline / Pass 1 / Pass 2 fan-out); I + P + F must
    equal Y from the leading `X of Y claims verified` -- but that sum check belongs
    to a separate rule, not this regex.
    """
    line = _external_claim_line(ctx)
    if line is None or ROUTED_METADATA_RE.search(line):
        return []
    return [Violation(
        rule_id="external-claim-routed-metadata",
        line_ref="<investigation log: External claim verification>",
        expected="line includes `routed: I inline, P Pass 1, F Pass 2`",
        actual=line.strip()[:160],
        hint="Append the routed-verification metadata to the External claim verification bullet: e.g., `· routed: 5 inline, 1 Pass 1, 4 Pass 2`. Counts must sum to Y (the total claims extracted).",
    )]


def check_external_claim_pass2_outcome(ctx: Context) -> list[Violation]:
    """Investigation-log Pass 2 segment carries V/C/U attribution when F > 0.

    Schema v4. When the Pass 2 lane has any traffic (F > 0), the routed-metadata
    segment must include `(verified V, contradicted C, unverifiable U)` immediately
    after `Pass 2`, and V + C + U must equal F. When F = 0, the parenthetical is
    omitted -- nothing to attribute.

    Why: Pass 2 is the lane where verdict drift across runs is observable
    (web sources change, retries flake). Inline + Pass 1 outcomes are visible
    in the leading `(N unverifiable, M contradicted)` parenthetical at the
    aggregate level. Per-lane attribution at Pass 2 is what closes the
    observability gap for cost-variance analysis.
    """
    line = _external_claim_line(ctx)
    if line is None:
        return []
    m = ROUTED_PASS2_RE.search(line)
    if not m:
        # Routed metadata isn't present at all; the routed-metadata check
        # already flags that. Don't double-flag here.
        return []
    pass2_count = int(m.group(1))
    if pass2_count == 0:
        # No Pass 2 traffic; V/C/U parenthetical is omitted by design. Reject
        # if the model added one anyway (an empty parenthetical is noise).
        if PASS2_OUTCOME_RE.search(line):
            return [Violation(
                rule_id="external-claim-pass2-outcome",
                line_ref="<investigation log: External claim verification>",
                expected="omit `(verified V, contradicted C, unverifiable U)` when Pass 2 count is 0",
                actual=line.strip()[:200],
                hint="Drop the V/C/U parenthetical from `0 Pass 2`. The breakdown only appears when at least one claim routed to Pass 2.",
            )]
        return []

    outcome_match = PASS2_OUTCOME_RE.search(line)
    if not outcome_match:
        return [Violation(
            rule_id="external-claim-pass2-outcome",
            line_ref="<investigation log: External claim verification>",
            expected=f"`Pass 2` segment carries `(verified V, contradicted C, unverifiable U)` parenthetical when F > 0 (here F = {pass2_count})",
            actual=line.strip()[:200],
            hint=f"Append the Pass 2 outcome attribution: e.g., `{pass2_count} Pass 2 (verified V, contradicted C, unverifiable U)` where V + C + U = {pass2_count}.",
        )]

    v, c, u = (int(outcome_match.group(i)) for i in (1, 2, 3))
    if v + c + u != pass2_count:
        return [Violation(
            rule_id="external-claim-pass2-outcome",
            line_ref="<investigation log: External claim verification>",
            expected=f"V + C + U == Pass 2 count ({pass2_count}); got V + C + U = {v + c + u}",
            actual=f"V={v}, C={c}, U={u}, Pass 2={pass2_count}",
            hint=f"Pass 2 verdicts must sum to the lane count. Either fix the V/C/U numbers (totals: verified={v}, contradicted={c}, unverifiable={u}) or fix the `{pass2_count} Pass 2` count to match.",
        )]
    return []


def check_external_claim_pass3_outcome(ctx: Context) -> list[Violation]:
    """Investigation-log Pass 3 segment carries V/C/U attribution when S > 0.

    Schema v5 mirror of `external-claim-pass2-outcome` for the Pass 3 (search-
    then-fetch) lane. Pass 3 segment is optional in the routed-metadata regex
    (back-compat with v4 captures); when the segment is present and S > 0,
    the V/C/U parenthetical is required. When S = 0 or the segment is absent,
    the parenthetical is omitted.

    Why split Pass 2 / Pass 3: Pass 3 dispatches WebSearch + WebFetch; Pass 2
    consults the workflow's pre-fetched URLs. Per-lane verdict attribution
    keeps cost-variance analysis honest -- a verdict drift in the search
    lane should not be confused with one in the URL-fetch lane.
    """
    line = _external_claim_line(ctx)
    if line is None:
        return []
    m = ROUTED_PASS3_RE.search(line)
    if not m:
        return []  # Pass 3 segment absent (v4-shape capture or omitted)
    pass3_count = int(m.group(1))
    if pass3_count == 0:
        if PASS3_OUTCOME_RE.search(line):
            return [Violation(
                rule_id="external-claim-pass3-outcome",
                line_ref="<investigation log: External claim verification>",
                expected="omit `(verified V, contradicted C, unverifiable U)` when Pass 3 count is 0",
                actual=line.strip()[:200],
                hint="Drop the V/C/U parenthetical from `0 Pass 3`. The breakdown only appears when at least one claim routed to Pass 3.",
            )]
        return []

    outcome_match = PASS3_OUTCOME_RE.search(line)
    if not outcome_match:
        return [Violation(
            rule_id="external-claim-pass3-outcome",
            line_ref="<investigation log: External claim verification>",
            expected=f"`Pass 3` segment carries `(verified V, contradicted C, unverifiable U)` parenthetical when S > 0 (here S = {pass3_count})",
            actual=line.strip()[:200],
            hint=f"Append the Pass 3 outcome attribution: e.g., `{pass3_count} Pass 3 (verified V, contradicted C, unverifiable U)` where V + C + U = {pass3_count}.",
        )]

    v, c, u = (int(outcome_match.group(i)) for i in (1, 2, 3))
    if v + c + u != pass3_count:
        return [Violation(
            rule_id="external-claim-pass3-outcome",
            line_ref="<investigation log: External claim verification>",
            expected=f"V + C + U == Pass 3 count ({pass3_count}); got V + C + U = {v + c + u}",
            actual=f"V={v}, C={c}, U={u}, Pass 3={pass3_count}",
            hint=f"Pass 3 verdicts must sum to the lane count. Either fix the V/C/U numbers (totals: verified={v}, contradicted={c}, unverifiable={u}) or fix the `{pass3_count} Pass 3` count to match.",
        )]
    return []


def check_pass2_fetch_faithfulness(ctx: Context) -> list[Violation]:
    """Strict-zero faithfulness floor for Pass 2: F > 0 requires non-empty `.fetched-urls.json`.

    Schema v5. Catches the actual S35 unfaithful pattern observed in the
    stream-JSON audit: docs reviews rendered routed-metadata claiming Pass 2
    dispatch but had ZERO Agent / WebFetch / WebSearch tool calls. The S33
    validator caught format drift; v4 caught V/C/U arithmetic drift; v5
    catches the dispatch lie -- if the workflow fetched no URLs, the model
    cannot honestly report Pass 2 traffic.

    Rule: trip iff `.fetched-urls.json` exists AND is empty AND the routed
    metadata reports F > 0. Pass when the file is missing (local mode), or
    when the file is non-empty (any URL count is consistent with model-side
    bouncing arithmetic), or when F = 0.
    """
    if ctx.fetched_urls is None:
        return []  # local mode / file not present
    if len(ctx.fetched_urls) > 0:
        return []  # workflow fetched URLs; F > 0 is plausibly faithful
    line = _external_claim_line(ctx)
    if line is None:
        return []
    m = ROUTED_PASS2_RE.search(line)
    if not m:
        return []  # routed-metadata regex check carries this case
    pass2_count = int(m.group(1))
    if pass2_count == 0:
        return []
    return [Violation(
        rule_id="pass-2-fetch-faithfulness",
        line_ref="<investigation log: External claim verification>",
        expected=f"Pass 2 count = 0 when `.fetched-urls.json` is empty (no URLs in PR diff); got Pass 2 = {pass2_count}",
        actual=line.strip()[:200],
        hint=f"The workflow fetched 0 URLs but the routed-metadata claims {pass2_count} Pass 2 dispatch(es). Either re-route the unrouted external-public claims to Pass 3 (search-then-fetch) and update `Pass 2` to 0, or fix the count to reflect actual URL-fetch verifications. See `docs-review:references:fact-check` §Routed verification.",
    )]


def check_pass3_dispatch_mandate(ctx: Context) -> list[Violation]:
    """Pass 3 must dispatch when external-public claims exist with no URL.

    Schema v5. When `.fetched-urls.json` is empty (no URLs in the PR diff)
    AND the routed-metadata accounting leaves claims unrouted (Y > I + P + F),
    those leftover claims must have routed to Pass 3 (S > 0). The model can
    no longer silently roll external-public claims into the inline lane to
    skip the search dispatch.

    Skipped when:
      - `.fetched-urls.json` is missing or non-empty (Pass 2 has actual fetches).
      - Pass 2 count > 0 with empty fetched-urls (faithfulness rule trips first;
        no need to double-flag with dispatch-mandate).
      - Y == I + P + F (every claim is routed; nothing left to mandate).
    """
    if ctx.fetched_urls is None or len(ctx.fetched_urls) > 0:
        return []
    line = _external_claim_line(ctx)
    if line is None:
        return []
    leading = LEADING_STATE_RE.search(line)
    routed_ip = ROUTED_INLINE_PASS1_RE.search(line)
    routed_p2 = ROUTED_PASS2_RE.search(line)
    if not (leading and routed_ip and routed_p2):
        return []  # other rules cover the missing segments
    y = int(leading.group(2))
    i = int(routed_ip.group(1))
    p = int(routed_ip.group(2))
    f = int(routed_p2.group(1))
    if f > 0:
        return []  # faithfulness rule trips; don't double-flag

    routed_p3 = ROUTED_PASS3_RE.search(line)
    s = int(routed_p3.group(1)) if routed_p3 else 0
    unrouted = y - i - p - f - s
    if unrouted <= 0 and s > 0:
        return []
    if unrouted == 0 and s == 0:
        return []  # all claims absorbed inline / Pass 1; no external claims
    return [Violation(
        rule_id="pass-3-dispatch-mandate",
        line_ref="<investigation log: External claim verification>",
        expected=f"Pass 3 dispatch required: {unrouted} external-public claim(s) unrouted to Pass 2 (no URLs fetched) must route to Pass 3",
        actual=f"Y={y}, I={i}, P={p}, F={f}, S={s}; unrouted={unrouted}",
        hint=f"Add `, {unrouted if unrouted > 0 else 1} Pass 3` to the routed-metadata segment with WebSearch + WebFetch dispatches per claim. Pass 3 is mandatory for external-public claims that lack URLs in the diff -- ⚠️ unverifiable verdicts on these claims must include a search-was-run negative-evidence pointer in the trail.",
    )]


def check_pass3_unverifiable_evidence(ctx: Context) -> list[Violation]:
    """Pass 3 ⚠️ unverifiable verdicts must carry search-was-run evidence in the trail.

    Schema v5. Per `docs-review:references:fact-check` §Routed verification:
    a Pass 3 ⚠️ unverifiable verdict requires a negative-evidence pointer
    naming the search that was run (`WebSearch ran query X; top N results
    didn't address the claim`). The model can't shortcut to ⚠️ unverifiable
    in Pass 3 without trying.

    Implementation: when Pass 3 outcome shows U > 0, the verification trail
    must include at least U trail entries that name a search/fetch attempt
    (regex `WebSearch|search ran|searched|query`).
    """
    line = _external_claim_line(ctx)
    if line is None:
        return []
    m = PASS3_OUTCOME_RE.search(line)
    if not m:
        return []
    u_pass3 = int(m.group(3))
    if u_pass3 == 0:
        return []

    span = find_section(ctx.body, "🔍 Verification trail")
    if span is None:
        return []
    start, end = span
    evidence_re = re.compile(r"WebSearch|search ran|searched|query", re.IGNORECASE)
    evidence_count = 0
    for raw in ctx.body_lines[start:end]:
        if "⚠️" in raw and "unverifiable" in raw.lower() and evidence_re.search(raw):
            evidence_count += 1
    if evidence_count >= u_pass3:
        return []
    return [Violation(
        rule_id="pass-3-unverifiable-evidence",
        line_ref="<🔍 Verification trail>",
        expected=f"at least {u_pass3} ⚠️ unverifiable trail entries naming a search dispatch (`WebSearch|search ran|searched|query`)",
        actual=f"only {evidence_count} of {u_pass3} ⚠️ unverifiable Pass 3 entries cite search evidence",
        hint=f"For each Pass 3 ⚠️ unverifiable verdict, append a negative-evidence pointer to the trail entry: e.g., `WebSearch ran query \"<phrase>\"; top 5 results didn't address the claim`. Pass 3 cannot shortcut to unverifiable without trying.",
    )]


# Schema v6: exploration patterns that don't read canonical source. The trail
# provenance rule flags trail-entry evidence text containing these substrings.
EXPLORATION_PATH_RE = re.compile(
    r"repos/[\w.-]+/[\w.-]+/(?:issues|pulls)(?:[?/]|\b)",
    re.IGNORECASE,
)
# Recursive tree-walks: `git/trees/<sha>?recursive=1`. Anchor on `trees/...?recursive`
# rather than the bare `?recursive=` query param so we don't over-match unrelated calls.
TREE_RECURSIVE_RE = re.compile(
    r"git/trees/[^\s`?]*\?recursive",
    re.IGNORECASE,
)


def check_pulumi_internal_trail_provenance(ctx: Context) -> list[Violation]:
    """Schema v6: trail entries must cite canonical-source paths, not exploration.

    Per `docs-review:references:fact-check` §Inline lane → "Canonical sources
    for pulumi-internal verification": pulumi-internal claims have known
    canonical sources (`data/docs_menu_sections.yml` for menu, sibling pages
    under `content/docs/<closest>/`, `static/programs/<name>-<lang>/` for
    example programs, `pulumi/pulumi-<provider>` for schema, etc.).

    `gh api repos/<owner>/<repo>/issues|pulls` and recursive tree-walks
    (`tree?recursive=...`) are exploration patterns — they don't read
    canonical source. The S37 pr18568 r1 rabbit-hole captured 75 gh calls
    iterating these instead of reading the canonical paths directly. This
    rule walks every line in 🔍 Verification trail and flags any that
    reference these patterns.

    Scope: applies trail-wide. Pass 1 / Pass 2 / Pass 3 entries also rarely
    have a legitimate use of these patterns; if one trips, audit it the
    same way.
    """
    span = find_section(ctx.body, "🔍 Verification trail")
    if span is None:
        return []
    start, end = span
    violations = []
    for i, raw in enumerate(ctx.body_lines[start:end], start=start):
        matched = None
        m = EXPLORATION_PATH_RE.search(raw)
        if m:
            matched = m.group(0)
        else:
            tm = TREE_RECURSIVE_RE.search(raw)
            if tm:
                matched = tm.group(0)
        if matched is None:
            continue
        line_ref_match = re.search(r"\bL\d+(?:-\d+)?\b", raw)
        line_ref = line_ref_match.group(0) if line_ref_match else f"<🔍 Verification trail line {i + 1}>"
        violations.append(Violation(
            rule_id="pulumi-internal-trail-provenance",
            line_ref=line_ref,
            expected="trail evidence cites a canonical-source path under `content/`, `data/`, `layouts/`, `static/programs/`, or `pulumi/pulumi-<provider>`",
            actual=raw.strip()[:200],
            hint=f"Replace exploration call (`{matched}`) with a targeted canonical-source read per the playbook in `docs-review:references:fact-check` §Inline lane → \"Canonical sources for pulumi-internal verification\". `gh api repos/.../issues|pulls` and recursive `tree?recursive=...` are exploration, not verification — if the canonical-source table doesn't close the claim in 3 reads, mark it `ambiguous` and route to Pass 1 (the shrug rule).",
        ))
    return violations


def check_frontmatter_locations_in_diff(ctx: Context) -> list[Violation]:
    """If the Frontmatter sweep line names locations, those files must exist in the PR diff."""
    for line in ctx.body_lines:
        stripped = line.lstrip()
        if not stripped.startswith("- **Frontmatter sweep"):
            continue
        if "not run" in line:
            return []
        m = re.search(r"ran on\s+([^)\n]+)", line)
        if not m:
            return []
        # Locations may include "body", "social.linkedin", "meta_desc", etc., or
        # explicit file paths. We check only entries that look like file paths
        # (contain `/` and end in `.md` or are within content/).
        listed = [tok.strip().strip(".,;") for tok in re.split(r"[,\s]+", m.group(1)) if tok.strip()]
        path_like = [t for t in listed if "/" in t]
        if not path_like or not ctx.diff_files:
            return []
        diff_set = set(ctx.diff_files)
        missing = [p for p in path_like if p not in diff_set]
        if missing:
            return [Violation(
                rule_id="frontmatter-sweep-locations-in-diff",
                line_ref="<investigation log: Frontmatter sweep>",
                expected="every listed file path appears in the PR's `gh pr diff --name-only`",
                actual=f"not in PR diff: {missing}",
                hint="Either remove the file paths from the Frontmatter sweep line or restrict the sweep to files actually changed in this PR.",
            )]
        return []
    return []


def _bullet_mentions_anchor(bullet: str, anchor: str) -> bool:
    """Fuzzy match: anchor (e.g., 'L83-87' or 'L42') appears anywhere in the bullet text.

    Used as a fallback when the [L<a>-<b>] prefix is missing — the bullet may
    still surface the right finding via in-text line references.
    """
    # Normalize: 'L83-87' should match both 'L83-87' and 'L83-88' loosely?
    # No — only exact match, since the trail anchor is the source of truth.
    return re.search(rf"\b{re.escape(anchor)}\b", bullet) is not None


def check_trail_bucket_consistency(ctx: Context) -> list[Violation]:
    """Every bucket bullet's [L...] prefix matches a trail record. Every 🚨 trail verdict surfaces in 🚨 Outstanding.

    Relaxation (S42): when the 🔍 Verification trail has no parsed records
    (the explicit-empty form, `_No verifiable claims extracted from this
    diff._` — the pure-layout / 0-claim case like #18857), the
    `bucket-bullet-trail-match` half is skipped: there is nothing in the trail
    for a bullet's prefix to match, and ⚠️/💡 code-behavior observations on a
    layout PR legitimately have no fact-check claim behind them. The prefix
    mandate (`bucket-bullet-line-range-prefix`) still applies, and the
    `candidate-claims-coverage` rule independently catches a content PR whose
    review failed to populate the trail.
    """
    trail_records = extract_trail_records(ctx.body)
    trail_refs = {r["line_ref"] for r in trail_records}
    trail_is_empty = len(trail_records) == 0

    violations: list[Violation] = []

    # Every bucket bullet must have a [L...] prefix; when the trail is non-empty
    # it must also match a trail record. When the prefix is missing, emit only
    # the prefix-mandate violation; the trail-match violation requires the
    # prefix to check.
    for section_label in ("🚨 Outstanding", "⚠️ Low-confidence", "💡 Pre-existing"):
        for bullet in extract_bucket_bullets(ctx.body, section_label):
            # Skip style findings (line N: prefix instead of [L...]).
            if bullet.lstrip().startswith("- **line "):
                continue
            prefix = extract_bullet_prefix(bullet)
            if prefix is None:
                violations.append(Violation(
                    rule_id="bucket-bullet-line-range-prefix",
                    line_ref=f"<{section_label} bullet>",
                    expected="bullet starts with `- **[L<start>-<end>]**`",
                    actual=bullet.strip()[:100],
                    hint="Add the `**[L<start>-<end>]**` prefix matching the corresponding 🔍 Verification trail record. The prefix is the exact key the validator uses to verify trail/bucket consistency.",
                ))
                continue
            if trail_is_empty:
                continue  # 0-claim / pure-layout PR — nothing in the trail to match against
            if prefix not in trail_refs:
                violations.append(Violation(
                    rule_id="bucket-bullet-trail-match",
                    line_ref=f"<{section_label} {prefix}>",
                    expected=f"a 🔍 Verification trail record with anchor {prefix}",
                    actual="no matching trail record",
                    hint=f"Either add the trail record for {prefix} (a `- L... → ...` line under 🔍 Verification trail) or remove this bucket bullet.",
                ))

    # Every 🚨 trail verdict (contradicted, mismatch) surfaces in 🚨 Outstanding.
    # Match by either: (a) bullet's [L...] prefix, OR (b) fuzzy mention of the
    # anchor anywhere in the Outstanding section text. The text-level fallback
    # tolerates legacy bullet formats and missing-prefix bullets — those are
    # flagged separately above so the model still gets a fix instruction.
    outstanding_text = section_text(ctx.body, "🚨 Outstanding")
    outstanding_bullets = extract_bucket_bullets(ctx.body, "🚨 Outstanding")
    seen_trail_refs = set()
    for r in trail_records:
        if r["verdict_emoji"] != "🚨":
            continue
        ref = r["line_ref"]
        if ref in seen_trail_refs:
            continue  # duplicate trail records — flag once
        seen_trail_refs.add(ref)
        # Match by prefix.
        prefix_match = any(extract_bullet_prefix(b) == ref for b in outstanding_bullets)
        # Fallback: anchor mentioned anywhere in the Outstanding section.
        text_match = re.search(rf"\b{re.escape(ref)}\b", outstanding_text) is not None
        if prefix_match or text_match:
            continue
        violations.append(Violation(
            rule_id="trail-verdict-bucket-promotion",
            line_ref=ref,
            expected=f"🚨 trail verdict at {ref} surfaces in 🚨 Outstanding via a bucket bullet with `**[{ref}]**` prefix",
            actual="not in 🚨 Outstanding",
            hint=f"Render a bullet under 🚨 Outstanding starting with `**[{ref}]**` that quotes the contradicted/mismatch finding. Trail verdict drives bucket placement — do not relitigate via the two-question test.",
        ))

    return violations


def _parse_line_token(tok: str) -> tuple[int, int] | None:
    """Parse 'L42' / 'L42-47' → (42, 42) / (42, 47). Returns None if unparseable."""
    m = re.fullmatch(r"L(\d+)(?:-(\d+))?", tok.strip())
    if not m:
        return None
    a = int(m.group(1))
    b = int(m.group(2)) if m.group(2) else a
    return (min(a, b), max(a, b))


def _parse_line_ranges(line_range: str) -> list[tuple[int, int]]:
    """Parse a claim's `line_range` ('L42', 'L42-47', or 'L12, L88, L91') into ranges."""
    out: list[tuple[int, int]] = []
    for m in re.finditer(r"L\d+(?:-\d+)?", line_range or ""):
        r = _parse_line_token(m.group(0))
        if r:
            out.append(r)
    return out


def _ranges_overlap(ra: list[tuple[int, int]], rb: list[tuple[int, int]], window: int = 2) -> bool:
    for a1, b1 in ra:
        for a2, b2 in rb:
            if a1 <= b2 + window and a2 <= b1 + window:
                return True
    return False


def check_candidate_claims_coverage(ctx: Context) -> list[Violation]:
    """Schema v7: every entry in `.candidate-claims.json` has a 🔍 Verification
    trail record whose line reference overlaps the claim's line range (± a
    small window). The claim list is the *floor* — the review must verify (or
    account for) every entry; it may add more. A dropped candidate claim is
    the #18771-R2 failure mode, and a missing trail entry can't be honestly
    synthesized by the surgical fixer — so this is non-surgical and soft-floors
    loudly, surfacing the gap to the maintainer.
    """
    claims = ctx.candidate_claims
    if claims is None:
        return []  # pre-step didn't run (local mode) — skip the rule
    if not claims:
        return []  # pre-step ran, found no claims — nothing to cover

    trail_records = extract_trail_records(ctx.body)
    # Flatten every trail record's line refs into (record, [parsed ranges]).
    trail_ranges: list[list[tuple[int, int]]] = []
    for r in trail_records:
        rngs = []
        for tok in r.get("line_refs", [r.get("line_ref", "")]):
            pr = _parse_line_token(tok)
            if pr:
                rngs.append(pr)
        if rngs:
            trail_ranges.append(rngs)

    violations: list[Violation] = []
    for c in claims:
        lr = c.get("line_range", "")
        claim_ranges = _parse_line_ranges(lr)
        if not claim_ranges:
            continue  # malformed line_range in the artifact — not the review's fault
        covered = any(_ranges_overlap(claim_ranges, tr) for tr in trail_ranges)
        if covered:
            continue
        text = (c.get("text", "") or "").strip()
        ctype = c.get("type", "claim")
        fb = "+".join(c.get("found_by", [])) or "?"
        violations.append(Violation(
            rule_id="candidate-claims-coverage",
            line_ref=lr or "<candidate claim>",
            expected=f"a 🔍 Verification trail record whose line ref overlaps {lr}",
            actual=f"no trail entry covers candidate claim [{ctype}, found_by={fb}]: \"{text[:120]}\"",
            hint=(
                f"`.candidate-claims.json` is the claim floor — add a 🔍 Verification trail line for {lr} "
                "(`- L… \"<claim>\" → <emoji> <verdict>`). Verdict is `verified`/`unverifiable`/`contradicted`/"
                "`matches`/`mismatch` per `docs-review:references:output-format`; if the candidate is a "
                "regex-layer false positive (git metadata, a Dockerfile-comment tag, a faithful description of "
                "the author's own design — see `docs-review:references:claim-extraction` §\"What is NOT a claim\"), "
                "record `✅ not-a-claim — <one-line reason>` so the demotion is traced. You MAY also add claims "
                "the artifact missed; you may NOT silently drop one."
            ),
        ))
    return violations


def check_editorial_balance_counts(ctx: Context) -> list[Violation]:
    """Editorial balance numbers (mean/median/std/outliers) match what's actually in the diff.

    Computed from the PR diff's blog markdown. Compares model-rendered numbers
    against re-computation. Only runs on blog PRs with the section present.
    """
    if not ctx.is_blog:
        return []
    span = find_section(ctx.body, "📊 Editorial balance")
    if span is None:
        return []
    start, end = span
    section = "\n".join(ctx.body_lines[start:end])
    # If the section is the explicit-empty form, skip.
    if "Single-subject post" in section or "balance check N/A" in section:
        return []

    # Pull the model's claimed `<N> H2 sections (mean <X> lines, median <Y>, std <Z>)`.
    m = re.search(
        r"(\d+)\s+H2\s+sections\s*\(mean\s+([\d.]+)\s+lines,\s*median\s+([\d.]+),\s*std\s+([\d.]+)\)",
        section,
    )
    if not m:
        return []  # different format — covered by other rules

    claimed_n = int(m.group(1))
    claimed_mean = float(m.group(2))
    claimed_median = float(m.group(3))
    claimed_std = float(m.group(4))

    # Recompute from the PR's blog markdown files.
    blog_files = [f for f in ctx.diff_files if f.startswith("content/blog/") and f.endswith(".md")]
    if not blog_files:
        return []

    section_lengths: list[int] = []
    for rel in blog_files:
        path = ctx.repo_root / rel
        if not path.exists():
            continue
        text = path.read_text(errors="replace")
        # Split on H2 headings.
        chunks = re.split(r"^##\s+", text, flags=re.MULTILINE)
        # First chunk is preamble, skip.
        for chunk in chunks[1:]:
            section_lengths.append(len(chunk.splitlines()))

    if not section_lengths:
        return []

    actual_n = len(section_lengths)
    actual_mean = round(statistics.mean(section_lengths), 1)
    actual_median = round(statistics.median(section_lengths), 1)
    actual_std = round(statistics.pstdev(section_lengths), 1) if len(section_lengths) > 1 else 0.0

    violations: list[Violation] = []
    # Allow ±10% tolerance on continuous stats (the model rounds differently).
    def diverges(a: float, b: float, tol: float = 0.10) -> bool:
        if a == b:
            return False
        return abs(a - b) > max(tol * max(abs(a), abs(b)), 0.5)

    if claimed_n != actual_n:
        violations.append(Violation(
            rule_id="editorial-balance-section-count",
            line_ref="<### 📊 Editorial balance>",
            expected=f"{actual_n} H2 sections (computed from PR diff)",
            actual=f"{claimed_n} H2 sections claimed",
            hint=f"Recount the H2 sections in the blog post(s) — actual is {actual_n}.",
        ))
    if diverges(claimed_mean, actual_mean):
        violations.append(Violation(
            rule_id="editorial-balance-mean",
            line_ref="<### 📊 Editorial balance>",
            expected=f"mean = {actual_mean}",
            actual=f"mean = {claimed_mean}",
            hint=f"Recompute the mean section length from the PR's blog markdown — actual is {actual_mean} lines.",
        ))
    if diverges(claimed_median, actual_median):
        violations.append(Violation(
            rule_id="editorial-balance-median",
            line_ref="<### 📊 Editorial balance>",
            expected=f"median = {actual_median}",
            actual=f"median = {claimed_median}",
            hint=f"Recompute the median section length — actual is {actual_median} lines.",
        ))
    if diverges(claimed_std, actual_std):
        violations.append(Violation(
            rule_id="editorial-balance-std",
            line_ref="<### 📊 Editorial balance>",
            expected=f"std = {actual_std}",
            actual=f"std = {claimed_std}",
            hint=f"Recompute the section-length standard deviation — actual is {actual_std}.",
        ))
    return violations


def check_editorial_balance_counts_faithful(ctx: Context) -> list[Violation]:
    """Tier 1 faithful counts: rendered section-depth stats match the JSON pre-step.

    Schema v5 companion to `editorial-balance-counts`. The latter recomputes
    stats from the diff at validate time; this rule reads them from
    `.editorial-balance.json` (the workflow pre-step's deterministic source
    of truth). When both agree, both pass; when they diverge, the model has
    drifted from script-computed Tier 1 numbers (the rule the workflow's
    pre-step authored) and the rendered section is unfaithful.

    Skipped when:
      - `.editorial-balance.json` is missing (local mode, non-blog PR).
      - JSON has `trigger=null` AND the rendered section is the empty form.
      - JSON has empty `files` list (no analyzable blog markdown in diff).

    Tier 2 fields (entity counts, FAQ steering ratios) stay model-computed
    and are NOT validated by this rule -- the deterministic floor only
    covers the script's outputs.
    """
    eb = ctx.editorial_balance
    if eb is None:
        return []
    files = eb.get("files") or []
    trigger = eb.get("trigger")

    span = find_section(ctx.body, "📊 Editorial balance")
    if span is None:
        # Mandatory-h3-order rule covers absence on blog PRs; nothing to check here.
        return []
    start, end = span
    section = "\n".join(ctx.body_lines[start:end])
    is_empty_form = ("Single-subject post" in section
                     or "balance check N/A" in section)

    if trigger is None:
        if is_empty_form:
            return []
        return [Violation(
            rule_id="editorial-balance-counts-faithful",
            line_ref="<### 📊 Editorial balance>",
            expected="empty form (`_Single-subject post; balance check N/A._`) when `.editorial-balance.json` reports `trigger=null`",
            actual="rich form rendered despite null trigger",
            hint="The Tier 1 detector found no listicle / FAQ trigger in the PR-changed blog markdown. Render the empty form per `docs-review:references:output-format` §Editorial balance, or override Tier 3 (don't-flag exception) explicitly in the rendered section.",
        )]

    # Trigger fired in the JSON; rich form expected.
    if is_empty_form:
        return [Violation(
            rule_id="editorial-balance-counts-faithful",
            line_ref="<### 📊 Editorial balance>",
            expected=f"rich form rendered (`.editorial-balance.json` reports trigger=`{trigger}`)",
            actual="empty form rendered",
            hint=f"The Tier 1 detector found a {trigger} trigger in the PR-changed blog markdown. Render the rich form with section-depth stats, vendor mentions, and threshold flags per `docs-review:references:output-format` §Editorial balance.",
        )]

    if not files:
        return []

    # Aggregate the JSON's section-depth stats (single file: use as-is;
    # multiple files: take the file with the trigger fired, falling back to
    # the first file with non-empty sections).
    target = next((f for f in files if f.get("trigger_local")), None)
    if target is None:
        target = next((f for f in files if f.get("sections")), None)
    if target is None:
        return []

    json_n = len(target.get("sections") or [])
    json_stats = target.get("stats") or {}
    json_mean = json_stats.get("mean")
    json_median = json_stats.get("median")
    json_std = json_stats.get("std")
    json_outliers = target.get("outliers") or []

    m = re.search(
        r"(\d+)\s+H2\s+sections\s*\(mean\s+([\d.]+)\s+lines,\s*median\s+([\d.]+),\s*std\s+([\d.]+)\)",
        section,
    )
    if not m:
        return []  # state-format violation belongs to a separate rule

    rendered_n = int(m.group(1))
    rendered_mean = float(m.group(2))
    rendered_median = float(m.group(3))
    rendered_std = float(m.group(4))

    def diverges(a: float, b: float, tol: float = 0.10) -> bool:
        if a == b:
            return False
        return abs(a - b) > max(tol * max(abs(a), abs(b)), 0.5)

    violations: list[Violation] = []
    if rendered_n != json_n:
        violations.append(Violation(
            rule_id="editorial-balance-counts-faithful",
            line_ref="<### 📊 Editorial balance: section count>",
            expected=f"{json_n} H2 sections (per `.editorial-balance.json`)",
            actual=f"{rendered_n} H2 sections rendered",
            hint=f"Update the rendered section count to match the deterministic detector ({json_n}).",
        ))
    if json_mean is not None and diverges(rendered_mean, float(json_mean)):
        violations.append(Violation(
            rule_id="editorial-balance-counts-faithful",
            line_ref="<### 📊 Editorial balance: mean>",
            expected=f"mean = {json_mean}",
            actual=f"mean = {rendered_mean}",
            hint=f"Update the rendered mean to match the deterministic detector ({json_mean}).",
        ))
    if json_median is not None and diverges(rendered_median, float(json_median)):
        violations.append(Violation(
            rule_id="editorial-balance-counts-faithful",
            line_ref="<### 📊 Editorial balance: median>",
            expected=f"median = {json_median}",
            actual=f"median = {rendered_median}",
            hint=f"Update the rendered median to match the deterministic detector ({json_median}).",
        ))
    if json_std is not None and diverges(rendered_std, float(json_std)):
        violations.append(Violation(
            rule_id="editorial-balance-counts-faithful",
            line_ref="<### 📊 Editorial balance: std>",
            expected=f"std = {json_std}",
            actual=f"std = {rendered_std}",
            hint=f"Update the rendered std to match the deterministic detector ({json_std}).",
        ))

    # Outlier presence: each JSON outlier should be cited in the rendered
    # section by heading. Rendered outliers without a JSON counterpart aren't
    # flagged here -- the model may also list close-to-3x outliers per its
    # own judgment; that's a Tier 3 call.
    for o in json_outliers:
        h = o.get("heading", "")
        if h and h not in section:
            violations.append(Violation(
                rule_id="editorial-balance-counts-faithful",
                line_ref="<### 📊 Editorial balance: outliers>",
                expected=f"outlier `{h}` ({o.get('lines')} lines, {o.get('ratio')}× median) cited in the rendered section",
                actual="not cited",
                hint=f"Add the outlier `{h}` to the rendered Section depth bullet (the deterministic detector flagged it as ≥3× median).",
            ))
    return violations


def check_frontmatter_sweep_repeats(ctx: Context) -> list[Violation]:
    """Detect repeated factual phrasings across body / meta_desc / social.* in the diff.

    This is a heuristic helper: when the same numeric or named-source phrasing
    appears in multiple frontmatter locations, the model should have noted it in
    the Frontmatter sweep line. We flag mismatches between the model's claim
    and the actual repeats found.
    """
    if not ctx.diff_files:
        return []
    # Look only at blog markdown files (frontmatter sweep is a blog-domain check).
    blog_files = [f for f in ctx.diff_files if f.startswith("content/blog/") and f.endswith(".md")]
    if not blog_files:
        return []

    # For each file, pull body claim phrases (numbers, percentages, quoted
    # named-source text) and check whether they appear duplicated in
    # `meta_desc:` or any `social.*:` value.
    flagged_phrases: list[tuple[str, str]] = []
    NUMBER_RE = re.compile(r"\b\d{1,3}(?:[,.]\d{3})*\s*%?\b")
    for rel in blog_files:
        path = ctx.repo_root / rel
        if not path.exists():
            continue
        text = path.read_text(errors="replace")
        # Split frontmatter from body.
        if not text.startswith("---"):
            continue
        end = text.find("---", 3)
        if end == -1:
            continue
        front = text[3:end]
        body = text[end + 3:]

        meta_desc = ""
        social_blob = ""
        in_social = False
        for line in front.splitlines():
            stripped = line.strip()
            if stripped.startswith("meta_desc:"):
                meta_desc = stripped[len("meta_desc:"):].strip().strip('"\'')
                in_social = False
            elif stripped.startswith("social:"):
                in_social = True
            elif in_social and (stripped.startswith("-") or ":" in stripped):
                social_blob += " " + stripped
            elif in_social and not stripped:
                in_social = False

        body_numbers = set(NUMBER_RE.findall(body))
        for phrase in body_numbers:
            if phrase in meta_desc or phrase in social_blob:
                flagged_phrases.append((rel, phrase))

    # If we found repeats but the model's Frontmatter sweep line says "not run",
    # that's a violation.
    if not flagged_phrases:
        return []
    for line in ctx.body_lines:
        if "Frontmatter sweep" in line and "not run" in line:
            return [Violation(
                rule_id="frontmatter-sweep-missed",
                line_ref="<investigation log: Frontmatter sweep>",
                expected="Frontmatter sweep ran (factual repeats found across body / meta_desc / social.*)",
                actual="not run",
                hint=f"Re-run the Frontmatter sweep — repeated phrasing detected in: {flagged_phrases[:3]}{' ...' if len(flagged_phrases) > 3 else ''}.",
            )]
    return []


def check_temporal_triggers_in_diff(ctx: Context) -> list[Violation]:
    """If the diff contains temporal-trigger words but the model marked the sweep `not run`, flag it."""
    if not ctx.diff_text:
        return []
    diff_lower = ctx.diff_text.lower()
    found_triggers = [t for t in TEMPORAL_TRIGGERS if t in diff_lower]
    if not found_triggers:
        return []
    for line in ctx.body_lines:
        if "Temporal-trigger sweep" in line and "not run" in line:
            return [Violation(
                rule_id="temporal-triggers-missed",
                line_ref="<investigation log: Temporal-trigger sweep>",
                expected="Temporal-trigger sweep ran (triggers present in diff)",
                actual=f"not run, but diff contains: {sorted(set(found_triggers))[:5]}",
                hint="Re-run the Temporal-trigger sweep — the diff includes recency words that should be verified.",
            )]
    return []


def check_internal_link_existence(ctx: Context) -> list[Violation]:
    """Every `/docs/...` or `/blog/...` link in the body resolves to a file."""
    LINK_RE = re.compile(r"\(((?:/docs/|/blog/)[^)\s]+)\)")
    found = LINK_RE.findall(ctx.body)
    if not found:
        return []

    violations: list[Violation] = []
    seen = set()
    for href in found:
        # Skip placeholder paths the model uses in template examples.
        if "<" in href or ">" in href:
            continue
        path = href.split("#", 1)[0].split("?", 1)[0].rstrip("/")
        if path in seen:
            continue
        seen.add(path)
        if not path:
            continue
        # Resolve under content/.
        rel = "content" + path
        candidates_rel = [f"{rel}.md", f"{rel}/_index.md", f"{rel}/index.md"]
        candidates = [ctx.repo_root / c for c in candidates_rel]
        if any(c.exists() for c in candidates):
            continue
        # Accept if a candidate file is being added by this PR's diff. Without
        # this check, the validator flags links to pages the PR itself creates.
        if any(c in ctx.diff_files_added for c in candidates_rel):
            continue
        # Cheap alias check: grep all md files under content/ for `aliases:` containing path.
        try:
            result = subprocess.run(
                ["git", "grep", "-l", f"- {path}", "--", "content/"],
                cwd=ctx.repo_root,
                capture_output=True, text=True, timeout=10,
            )
            if result.stdout.strip():
                continue
        except (subprocess.SubprocessError, OSError):
            pass
        violations.append(Violation(
            rule_id="internal-link-existence",
            line_ref="<body>",
            expected=f"link {href} resolves to a file or alias under content/",
            actual="no matching file or alias",
            hint=f"Either fix the link target, add an alias on the destination page, or remove the link.",
        ))
    return violations


def check_shortcode_existence(ctx: Context) -> list[Violation]:
    """Every `{{< shortcode-name >}}` resolves to a layout under layouts/shortcodes/."""
    SC_RE = re.compile(r"\{\{<\s*([a-zA-Z0-9_-]+)")
    found = set(SC_RE.findall(ctx.body))
    if not found:
        return []

    shortcodes_dir = ctx.repo_root / "layouts" / "shortcodes"
    if not shortcodes_dir.is_dir():
        return []  # repo doesn't have shortcodes — skip
    available = {p.stem for p in shortcodes_dir.glob("*.html")}
    available |= {p.stem for p in shortcodes_dir.glob("*.md")}

    violations: list[Violation] = []
    for name in sorted(found):
        if name in available:
            continue
        # Check nested directories too.
        if (shortcodes_dir / name).is_dir():
            continue
        violations.append(Violation(
            rule_id="shortcode-existence",
            line_ref="<body>",
            expected=f"shortcode `{{{{< {name} >}}}}` has a layout under layouts/shortcodes/",
            actual="no matching layout file",
            hint=f"Either fix the shortcode name or add the corresponding layout file.",
        ))
    return violations


# ---- Rule registry ---------------------------------------------------------

RULES = [
    {
        "id": "count-table",
        "desc": "Bucket-count table numbers match actual bullet count in each section, including style findings in ⚠️ count.",
        "hint": "Recount bullets in each section (regular + style under #### Style findings) and update the table number row.",
        "check": check_count_table_matches_bullets,
    },
    {
        "id": "investigation-log",
        "desc": "8 mandatory investigation-log bullets present in order, each in a recognized state format.",
        "hint": "Render all 8 bullets in spec order with `X of Y`, `ran ...`, or `not run (...)` states.",
        "check": check_investigation_log_bullets,
    },
    {
        "id": "cross-sibling-math",
        "desc": "Cross-sibling reads line: count of named-read equals X; named + skipped equals Y.",
        "hint": "Either fix X/Y to match the listed siblings, or list every read/skipped sibling explicitly.",
        "check": check_cross_sibling_math,
    },
    {
        "id": "style-render-mode",
        "desc": "Style-findings render mode matches the relaxed inline-vs-collapse rule (output-format.md L252-258).",
        "hint": "Inline-all when total ≤5 OR concentrated in one file (≤30); collapse-all when multi-file AND total >5, or total >30.",
        "check": check_style_render_mode,
    },
    {
        "id": "mandatory-h3-order",
        "desc": "Mandatory H3 sections present in spec order (output-format.md L81).",
        "hint": "Render every mandatory H3 in order, using the explicit-empty form when content is absent.",
        "check": check_mandatory_h3_order,
    },
    {
        "id": "external-claim-state-format",
        "desc": "Investigation-log External claim verification bullet uses canonical `X of Y claims verified` state form.",
        "hint": "Render the bullet as `X of Y claims verified (N unverifiable, M contradicted) · ...` or `not run (<reason>)`. Compaction is not permitted.",
        "check": check_external_claim_state_format,
    },
    {
        "id": "external-claim-dispatch-metadata",
        "desc": "Investigation-log External claim verification line includes the extraction-specialists tail.",
        "hint": "Append `· N specialists (numerical, cross-reference, capability, framing); K cross-specialist corroborations` to the bullet.",
        "check": check_external_claim_dispatch_metadata,
    },
    {
        "id": "external-claim-routed-metadata",
        "desc": "Investigation-log External claim verification line includes the routed-verification tail.",
        "hint": "Append `· routed: I inline, P Pass 1, F Pass 2` to the bullet (counts must sum to Y).",
        "check": check_external_claim_routed_metadata,
    },
    {
        "id": "external-claim-pass2-outcome",
        "desc": "Investigation-log Pass 2 segment carries `(verified V, contradicted C, unverifiable U)` attribution when F > 0; V+C+U=F.",
        "hint": "Append `(verified V, contradicted C, unverifiable U)` after `F Pass 2` when F > 0; omit when F = 0.",
        "check": check_external_claim_pass2_outcome,
    },
    {
        "id": "external-claim-pass3-outcome",
        "desc": "Schema v5: Investigation-log Pass 3 segment carries `(verified V, contradicted C, unverifiable U)` attribution when S > 0; V+C+U=S.",
        "hint": "Append `(verified V, contradicted C, unverifiable U)` after `S Pass 3` when S > 0; omit when S = 0.",
        "check": check_external_claim_pass3_outcome,
    },
    {
        "id": "pass-2-fetch-faithfulness",
        "desc": "Schema v5: Pass 2 count > 0 requires `.fetched-urls.json` to be non-empty -- catches the unfaithful pattern where the model claims Pass 2 dispatches without the workflow having fetched any URLs.",
        "hint": "Either re-route the unrouted external-public claims to Pass 3 (search-then-fetch) and update Pass 2 count to 0, or fix the count to reflect actual URL-fetch verifications.",
        "check": check_pass2_fetch_faithfulness,
    },
    {
        "id": "pass-3-dispatch-mandate",
        "desc": "Schema v5: external-public claims without URLs (`.fetched-urls.json` empty) must route to Pass 3 (S > 0) instead of being silently absorbed into Inline / Pass 1.",
        "hint": "Add `, N Pass 3` to the routed-metadata segment with WebSearch + WebFetch dispatches per claim; Pass 3 is mandatory for external-public claims that lack URLs in the diff.",
        "check": check_pass3_dispatch_mandate,
    },
    {
        "id": "pass-3-unverifiable-evidence",
        "desc": "Schema v5: Pass 3 ⚠️ unverifiable verdicts must carry a search-was-run negative-evidence pointer in the trail entry.",
        "hint": "For each Pass 3 ⚠️ unverifiable verdict, append `WebSearch ran query \"<phrase>\"; top N results didn't address the claim` (or equivalent search-was-run pointer) to the trail entry.",
        "check": check_pass3_unverifiable_evidence,
    },
    {
        "id": "pulumi-internal-trail-provenance",
        "desc": "Schema v6: trail entries must cite canonical-source paths; `gh api repos/.../issues|pulls` and recursive `tree?recursive=...` queries are exploration not verification.",
        "hint": "Per the canonical-source playbook in `docs-review:references:fact-check` §Inline lane → \"Canonical sources for pulumi-internal verification\", verify against `data/docs_menu_sections.yml` (menu), `static/programs/<name>-<lang>/` (example programs), nearest sibling under `content/docs/<closest>/`, or `pulumi/pulumi-<provider>` (schema). Shrug rule: if 3 targeted reads don't close the claim, mark `ambiguous` and route to Pass 1.",
        "check": check_pulumi_internal_trail_provenance,
    },
    {
        "id": "frontmatter-locations",
        "desc": "Frontmatter-sweep listed locations exist in PR diff.",
        "hint": "Restrict the frontmatter sweep to files actually changed in this PR.",
        "check": check_frontmatter_locations_in_diff,
    },
    {
        "id": "trail-bucket-consistency",
        "desc": "Every bucket bullet has [L<a>-<b>] prefix matching a trail record (relaxed: trail-match half skipped when the trail is the explicit-empty form). Every 🚨 trail verdict surfaces in 🚨 Outstanding.",
        "hint": "Add the line-range prefix to bucket bullets; promote 🚨 trail verdicts to 🚨 Outstanding without relitigation.",
        "check": check_trail_bucket_consistency,
    },
    {
        "id": "candidate-claims-coverage",
        "desc": "Schema v7: every entry in `.candidate-claims.json` (the merged claim-extraction floor: regex ∪ two Sonnet passes) has a 🔍 Verification trail record overlapping its line range — the review may add claims, may not silently drop one.",
        "hint": "For each uncovered candidate claim, add a 🔍 Verification trail line `- L… \"<claim>\" → <emoji> <verdict>`. If the candidate is a regex-layer false positive (git metadata, Dockerfile-comment tag, faithful description of the author's own design — see `docs-review:references:claim-extraction`), record `✅ not-a-claim — <reason>` so the demotion is traced.",
        "check": check_candidate_claims_coverage,
    },
    {
        "id": "editorial-balance-counts",
        "desc": "Editorial balance section count + mean/median/std match values computed from the PR diff.",
        "hint": "Recompute the H2-section stats from the blog markdown; update the rendered values.",
        "check": check_editorial_balance_counts,
    },
    {
        "id": "editorial-balance-counts-faithful",
        "desc": "Schema v5: rendered Editorial balance section's Tier 1 stats (count, mean, median, std, outliers, trigger / empty-form selection) match `.editorial-balance.json` written by the workflow's `editorial-balance-detect.py` pre-step.",
        "hint": "Source Tier 1 fields (trigger, section count, mean/median/std, outliers) from `.editorial-balance.json`; render the rich vs empty form per the JSON's `trigger` field. Tier 2 fields (entity counts, FAQ steering) remain model-computed.",
        "check": check_editorial_balance_counts_faithful,
    },
    {
        "id": "frontmatter-sweep-repeats",
        "desc": "Frontmatter sweep finds repeats across body / meta_desc / social.* — flag if the model reported `not run`.",
        "hint": "Re-run the frontmatter sweep when factual repeats are present.",
        "check": check_frontmatter_sweep_repeats,
    },
    {
        "id": "temporal-triggers",
        "desc": "Temporal-trigger words present in diff but model said sweep `not run`.",
        "hint": "Run the Temporal-trigger sweep when recency words are in the diff.",
        "check": check_temporal_triggers_in_diff,
    },
    {
        "id": "internal-link-existence",
        "desc": "Every internal /docs/... or /blog/... link resolves to a file or alias under content/.",
        "hint": "Fix the link target, add an alias on the destination page, or remove the link.",
        "check": check_internal_link_existence,
    },
    {
        "id": "shortcode-existence",
        "desc": "Every {{< shortcode >}} resolves to a layout under layouts/shortcodes/.",
        "hint": "Fix the shortcode name or add the corresponding layout file.",
        "check": check_shortcode_existence,
    },
]

# Hint is load-bearing — every rule must ship with a non-empty hint or the
# validator refuses to start.
for r in RULES:
    if not r.get("hint"):
        raise SystemExit(f"validate-pinned.py: rule {r['id']} missing required hint")


# ---- Driver ----------------------------------------------------------------


def gh_pr_diff_name_only(repo: str | None, pr: int) -> list[str]:
    cmd = ["gh", "pr", "diff", str(pr), "--name-only"]
    if repo:
        cmd += ["--repo", repo]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True, timeout=30)
        return [line.strip() for line in result.stdout.splitlines() if line.strip()]
    except (subprocess.SubprocessError, OSError):
        return []


def gh_pr_diff_added_files(repo: str | None, pr: int) -> set[str]:
    """Return the set of relative paths added (status=A) by this PR.

    Used by `internal-link-existence` to accept links to pages the PR itself
    is creating — the destination doesn't exist on the base branch but will
    once the PR merges, so the link is valid.
    """
    target_repo = repo
    if not target_repo:
        try:
            result = subprocess.run(
                ["gh", "repo", "view", "--json", "nameWithOwner",
                 "--jq", ".nameWithOwner"],
                capture_output=True, text=True, check=True, timeout=10,
            )
            target_repo = result.stdout.strip()
        except (subprocess.SubprocessError, OSError):
            return set()
    cmd = [
        "gh", "api", f"repos/{target_repo}/pulls/{pr}/files",
        "--paginate",
        "--jq", '.[] | select(.status=="added") | .filename',
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True, timeout=30)
        return {line.strip() for line in result.stdout.splitlines() if line.strip()}
    except (subprocess.SubprocessError, OSError):
        return set()


def gh_pr_diff_text(repo: str | None, pr: int) -> str:
    cmd = ["gh", "pr", "diff", str(pr)]
    if repo:
        cmd += ["--repo", repo]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True, timeout=60)
        return result.stdout
    except (subprocess.SubprocessError, OSError):
        return ""


def load_editorial_balance(explicit_path: str | None) -> dict | None:
    """Load `.editorial-balance.json` if present.

    Returns None when the file isn't present (local mode or workflow didn't
    run the pre-step); returns the parsed dict otherwise. Schema v5 rule
    `editorial-balance-counts-faithful` distinguishes None (skip rule) from
    `{"trigger": null, ...}` (workflow ran, no triggers fired).
    """
    if explicit_path:
        path = Path(explicit_path)
    else:
        path = Path.cwd() / ".editorial-balance.json"
    if not path.is_file():
        return None
    try:
        data = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError):
        return None
    if not isinstance(data, dict):
        return None
    return data


def load_fetched_urls(explicit_path: str | None) -> list[dict] | None:
    """Load `.fetched-urls.json` if present.

    Returns None when the file isn't present (local mode or workflow didn't
    run the pre-step); returns the parsed list (possibly empty) otherwise.
    Schema v5 rules `pass-2-fetch-faithfulness` and `pass-3-dispatch-mandate`
    distinguish None (skip rule) from `[]` (workflow ran, no URLs in diff).
    """
    if explicit_path:
        path = Path(explicit_path)
    else:
        path = Path.cwd() / ".fetched-urls.json"
    if not path.is_file():
        return None
    try:
        data = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError):
        return None
    if not isinstance(data, list):
        return None
    return data


def load_candidate_claims(explicit_path: str | None) -> list[dict] | None:
    """Load the `claims` list from `.candidate-claims.json` if present.

    Returns None when the file isn't present (local mode or the workflow
    didn't run the claim-extraction pre-step); returns the parsed `claims`
    list (possibly empty) otherwise. The `candidate-claims-coverage` rule
    distinguishes None (skip the rule) from `[]` (pre-step ran, no claims).
    """
    if explicit_path:
        path = Path(explicit_path)
    else:
        path = Path.cwd() / ".candidate-claims.json"
    if not path.is_file():
        return None
    try:
        data = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError):
        return None
    if not isinstance(data, dict):
        return None
    claims = data.get("claims")
    if not isinstance(claims, list):
        return None
    return [c for c in claims if isinstance(c, dict)]


def repo_root() -> Path:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            capture_output=True, text=True, check=True, timeout=10,
        )
        return Path(result.stdout.strip())
    except (subprocess.SubprocessError, OSError):
        return Path.cwd()


def run_checks(ctx: Context) -> list[Violation]:
    out: list[Violation] = []
    for rule in RULES:
        try:
            out.extend(rule["check"](ctx))
        except Exception as e:  # don't let one rule's bug abort the validator
            out.append(Violation(
                rule_id=f"{rule['id']}-internal-error",
                line_ref="<validator>",
                expected="rule check completes without error",
                actual=f"{type(e).__name__}: {e}",
                hint=f"Validator bug in rule `{rule['id']}` — report and skip; do not block the post on this.",
            ))
    return out


def render_markdown(violations: list[Violation]) -> str:
    if not violations:
        return "_No violations._\n"
    out = [
        "# validate-pinned.py — fix-me marker",
        "",
        f"{len(violations)} violation(s) found. Re-render the body addressing each violation below, then call `pinned-comment.sh upsert-validated` once more. If a second validation also fails, fall back to plain `upsert` — the validator's CI annotation will surface the residual to the maintainer.",
        "",
    ]
    for v in violations:
        out.append(f"## `{v.rule_id}` — {v.line_ref}")
        out.append(f"- **Expected:** {v.expected}")
        out.append(f"- **Actual:** {v.actual}")
        out.append(f"- **Hint:** {v.hint}")
        out.append("")
    return "\n".join(out)


def write_outputs(violations: list[Violation], json_path: Path,
                  markdown_path: Path, body_path: Path) -> None:
    payload = {
        "schema_version": SCHEMA_VERSION,
        "body_path": str(body_path),
        "violations": [v.to_dict() for v in violations],
    }
    json_path.write_text(json.dumps(payload, indent=2))
    markdown_path.write_text(render_markdown(violations))


def emit_ci_annotation(violations: list[Violation], soft_floor: bool) -> None:
    """Print a GitHub Actions warning annotation per validator outcome."""
    if not violations:
        return
    label = "soft-floor" if soft_floor else "retry-1"
    summary = "; ".join(f"{v.rule_id}@{v.line_ref}" for v in violations[:5])
    if len(violations) > 5:
        summary += f"; (+{len(violations) - 5} more)"
    print(f"::warning::validate-pinned {label} — {len(violations)} violation(s): {summary}",
          file=sys.stderr)


def cmd_check(args: argparse.Namespace) -> int:
    body_path = Path(args.body_file)
    if not body_path.is_file():
        print(f"validate-pinned.py: body file not found: {body_path}", file=sys.stderr)
        return 2

    body = body_path.read_text()

    pr_int = int(args.pr) if args.pr else None
    diff_files = gh_pr_diff_name_only(args.repo, pr_int) if pr_int else []
    diff_files_added = gh_pr_diff_added_files(args.repo, pr_int) if pr_int else set()
    diff_text = gh_pr_diff_text(args.repo, pr_int) if pr_int else ""
    is_blog = any(f.startswith("content/blog/") for f in diff_files)
    fetched_urls = load_fetched_urls(args.fetched_urls)
    editorial_balance = load_editorial_balance(args.editorial_balance)
    candidate_claims = load_candidate_claims(args.candidate_claims)

    ctx = Context(
        body=body,
        body_lines=body.splitlines(),
        pr=pr_int,
        repo=args.repo,
        diff_files=diff_files,
        diff_files_added=diff_files_added,
        diff_text=diff_text,
        repo_root=repo_root(),
        is_blog=is_blog,
        fetched_urls=fetched_urls,
        editorial_balance=editorial_balance,
        candidate_claims=candidate_claims,
    )

    violations = run_checks(ctx)

    json_path = Path(args.output_json or DEFAULT_OUTPUT_JSON)
    md_path = Path(args.output_markdown or DEFAULT_OUTPUT_MARKDOWN)
    write_outputs(violations, json_path, md_path, body_path)

    emit_ci_annotation(violations, soft_floor=bool(args.soft_floor))

    if violations:
        print(f"validate-pinned.py: {len(violations)} violation(s); see {md_path}", file=sys.stderr)
        return 1
    return 0


def cmd_show_rules(_: argparse.Namespace) -> int:
    for r in RULES:
        print(f"{r['id']}: {r['desc']}")
        print(f"  hint: {r['hint']}")
    return 0


def cmd_schema_version(_: argparse.Namespace) -> int:
    print(SCHEMA_VERSION)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate a rendered pinned-review body against the deterministic invariants in the RULES registry (run `show-rules`)."
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_check = sub.add_parser("check", help="Run all rules; write fix-me marker on violations.")
    p_check.add_argument("--body-file", required=True)
    p_check.add_argument("--pr", help="PR number (for gh diff context)")
    p_check.add_argument("--repo", help="owner/repo (defaults to gh resolution)")
    p_check.add_argument("--output-json", help=f"default {DEFAULT_OUTPUT_JSON}")
    p_check.add_argument("--output-markdown", help=f"default {DEFAULT_OUTPUT_MARKDOWN}")
    p_check.add_argument("--soft-floor", action="store_true",
                         help="Annotation labels as soft-floor (second-failure publish-anyway).")
    p_check.add_argument("--fetched-urls",
                         help="Path to `.fetched-urls.json` from the workflow pre-step. "
                              "Defaults to ./.fetched-urls.json. Pass-through to "
                              "schema-v5 Pass 2/3 faithfulness rules.")
    p_check.add_argument("--editorial-balance",
                         help="Path to `.editorial-balance.json` from the workflow "
                              "pre-step. Defaults to ./.editorial-balance.json. "
                              "Pass-through to the editorial-balance-counts-faithful "
                              "rule (Tier 1 deterministic detector).")
    p_check.add_argument("--candidate-claims",
                         help="Path to `.candidate-claims.json` from the claim-extraction "
                              "pre-step (regex ∪ two Sonnet passes). Defaults to "
                              "./.candidate-claims.json. Pass-through to the "
                              "candidate-claims-coverage rule (schema v7).")
    p_check.set_defaults(func=cmd_check)

    p_rules = sub.add_parser("show-rules", help="Print the rule registry.")
    p_rules.set_defaults(func=cmd_show_rules)

    p_ver = sub.add_parser("schema-version", help="Print the validator schema version.")
    p_ver.set_defaults(func=cmd_schema_version)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())

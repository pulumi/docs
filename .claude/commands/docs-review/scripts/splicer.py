#!/usr/bin/env python3
"""splicer.py — deterministic surgical-fix for validator violations.

Reads the fix-me JSON from `validate-pinned.py` and applies pure-Python
splices for every rule_id in `SURGICAL_RULES`. No model calls; no API
keys; ~milliseconds wall-clock. Replaces the model-driven splice path
(`validator-fix.py`) for the rules that are mechanical regex/string ops.

Usage:
    splicer.py --body-file <path> --fix-me-json <path>
                [--fallback-json <path>]

Exit codes:
    0  every surgical violation was applied (or none were present)
    1  fatal error (missing files, JSON parse error, body write failure)
    2  at least one surgical violation could not be deterministically spliced;
       the affected rule_ids are written to `--fallback-json` (default
       `/tmp/splicer-fallback.json`) so the workflow's fallback step can
       hand them to the model lane (`validator-fix.py`)

Design notes:
    Non-surgical violations are ignored here — they remain in the fix-me
    JSON and will trip the model retry / soft-floor in the downstream
    workflow steps. Surgical violations are partitioned by `rule_id` and
    applied in dependency order (see `APPLY_ORDER`): structural inserts
    first, trail-line edits next, then the External-claim-bullet build-out,
    then bucket prefix prepends.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

DEFAULT_FALLBACK_JSON = "/tmp/splicer-fallback.json"

# Per-verdict glyphs (mirror of validate-pinned.py EXPECTED_TRAIL_EMOJI).
EXPECTED_TRAIL_EMOJI = {
    "verified": "✅",
    "matches": "🤝",
    "not-a-claim": "➖",
    "unverifiable": "🤷",
    "contradicted": "❌",
    "mismatch": "⚔️",
}
CANONICAL_VERDICT_FOR_EMOJI = {v: k for k, v in EXPECTED_TRAIL_EMOJI.items()}
CANONICAL_VERDICTS = set(EXPECTED_TRAIL_EMOJI.keys())

# Mandatory H3 sections in canonical order (mirror of validate-pinned.py
# MANDATORY_H3_SECTIONS). 📊 Editorial balance is conditional on blog and
# sits between 🔍 Verification trail and 🚨 Outstanding; 💡 Pre-existing
# is optional and sits between ⚠️ Low-confidence and 📜 Review history.
CANONICAL_H3_ORDER = [
    "🔍 Verification trail",
    "📊 Editorial balance",
    "🚨 Outstanding",
    "⚠️ Low-confidence",
    "💡 Pre-existing",
    "📜 Review history",
]

# Explicit-empty forms the composer renders when a section has no content.
# Mirrors of `compose-review.py`'s render_* functions. Keep synchronized.
EMPTY_FORMS = {
    "🔍 Verification trail": "### 🔍 Verification trail\n\n_No verifiable claims extracted from this diff._",
    "📊 Editorial balance": "### 📊 Editorial balance\n\n_Single-subject post; balance check N/A._",
    "🚨 Outstanding": "### 🚨 Outstanding in this PR\n\n_No outstanding findings in this PR._",
    "⚠️ Low-confidence": "### ⚠️ Low-confidence\n\n_No low-confidence findings._",
    "💡 Pre-existing": "### 💡 Pre-existing issues in touched files (optional)\n\n_No pre-existing issues in touched files._",
    "📜 Review history": "### 📜 Review history\n\n- <TODO: timestamp> — <TODO: one-line summary> (<TODO: sha>)",
}

# Order in which surgical rules are applied within a single splicer
# invocation. Structural / line-add rules run first; trail-line edits next;
# the External-claim-bullet build-out chain runs in lex order on the bullet;
# bucket-bullet prefix prepends run last so trail records are stable.
APPLY_ORDER = [
    "mandatory-h3-order",
    "internal-link-existence",
    "shortcode-existence",
    "verified-claims-trail-faithful",
    "trail-canonical-verdict-word",
    "trail-per-verdict-emoji",
    "pass-3-unverifiable-evidence",
    "external-claim-state-format",
    "external-claim-dispatch-metadata",
    "external-claim-routed-metadata",
    "external-claim-pass2-outcome",
    "bucket-bullet-line-range-prefix",
]


# ---- Body / line helpers ----------------------------------------------------


def _section_span(lines: list[str], heading_substring: str) -> tuple[int, int] | None:
    """Return (start, end) line indices of an H3 section whose heading contains
    `heading_substring`. `end` is exclusive (next H3 line or len(lines))."""
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


_TRAIL_LINE_ANCHOR_RE = re.compile(r"^\s*-\s+(L\d+(?:-\d+)?)\b")
_L_TOKEN_RE = re.compile(r"L(\d+)(?:-(?:L)?(\d+))?")


def _normalize_anchor(anchor: str) -> str:
    """Normalize an artifact-form anchor (L42, L42-L58) to trail form (L42-58)."""
    if not anchor:
        return ""
    return re.sub(r"L(\d+)-L(\d+)", r"L\1-\2", anchor)


def _parse_l_token(tok: str) -> tuple[int, int] | None:
    """Parse `L42` or `L42-58` (or `L42-L58`) → (start, end) ints. None on miss."""
    m = _L_TOKEN_RE.fullmatch(tok)
    if not m:
        return None
    a = int(m.group(1))
    b = int(m.group(2)) if m.group(2) else a
    if b < a:
        a, b = b, a
    return (a, b)


def _find_trail_line_index(lines: list[str], anchor: str) -> int:
    """Find the trail line that semantically matches the artifact's anchor.

    Matching tiers (first hit wins):
    1. Exact anchor match against the trail line's leading L-token (after the
       `- `). Cheapest; handles single-line / identical-range cases.
    2. Range overlap against any L-token on the trail line — mirrors the
       validator's `_ranges_overlap` matching strategy. A claim `L42-58`
       legitimately matches a trail entry `L42` (or `L42-45`, `L40-60`).

    Returns -1 if no trail section, no parsable anchor, or no match.
    """
    span = _section_span(lines, "🔍 Verification trail")
    if span is None:
        return -1
    start, end = span
    needle_normalized = _normalize_anchor(anchor)
    needle_range = _parse_l_token(needle_normalized)
    if not needle_range:
        return -1
    # Tier 1: exact anchor match.
    for i in range(start, end):
        m = _TRAIL_LINE_ANCHOR_RE.match(lines[i])
        if m and m.group(1) == needle_normalized:
            return i
    # Tier 2: range overlap against any L-token on the line.
    for i in range(start, end):
        m = _TRAIL_LINE_ANCHOR_RE.match(lines[i])
        if not m:
            continue
        for tok in re.findall(r"L\d+(?:-\d+)?", lines[i]):
            tok_range = _parse_l_token(tok)
            if tok_range and tok_range[0] <= needle_range[1] and needle_range[0] <= tok_range[1]:
                return i
    return -1


def _find_external_claim_line_index(lines: list[str]) -> int:
    """Index of the `- **External claim verification**` investigation-log line."""
    for i, line in enumerate(lines):
        if line.lstrip().startswith("- **External claim verification"):
            return i
    return -1


# ---- Splicers (one per rule_id in SURGICAL_RULES) ---------------------------


def splice_internal_link_existence(lines: list[str], violation: dict) -> tuple[list[str], bool]:
    """Unwrap `[text](broken-target)` → bare `text` (or strip on no-text).

    `expected` is "link <href> resolves to a file or alias under content/".
    Skip code-formatted refs (` `path` `) — only the markdown-link form.
    """
    m = re.search(r"link (\S+) resolves", violation.get("expected", ""))
    if not m:
        return lines, False
    broken = m.group(1)
    # Match optional trailing slash variants the validator already normalized away.
    # Build a regex for [text](broken) | [text](broken/) where broken is literal.
    href_pattern = re.escape(broken).rstrip("/") + r"/?"
    link_re = re.compile(r"\[([^\]]*?)\]\((" + href_pattern + r")(?:#[^)]*)?\)")
    applied = False
    new_lines = []
    for line in lines:
        # Don't touch code-fenced inline refs.
        replaced = link_re.sub(lambda m: m.group(1), line)
        if replaced != line:
            applied = True
        new_lines.append(replaced)
    return new_lines, applied


def splice_shortcode_existence(lines: list[str], violation: dict) -> tuple[list[str], bool]:
    """Delete any line containing the offending Hugo shortcode usage.

    `expected` is "shortcode `{{< NAME >}}` has a layout under layouts/shortcodes/".
    """
    m = re.search(r"\{\{<\s*([a-zA-Z0-9_-]+)", violation.get("expected", ""))
    if not m:
        return lines, False
    name = m.group(1)
    pattern = re.compile(r"\{\{<\s*" + re.escape(name) + r"\b")
    new_lines = [line for line in lines if not pattern.search(line)]
    return new_lines, len(new_lines) != len(lines)


def splice_mandatory_h3_order(lines: list[str], violation: dict) -> tuple[list[str], bool]:
    """Insert the missing H3 section with its explicit-empty form, in canonical position.

    `line_ref` is like `<### 📊 Editorial balance>`. If the section is already
    present elsewhere (out-of-order), we defer to fallback — moving is too
    fragile to attempt deterministically.
    """
    m = re.match(r"<###\s+(.+?)>", violation.get("line_ref", ""))
    if not m:
        return lines, False
    section_name = m.group(1).strip()

    for line in lines:
        if line.startswith("### ") and section_name in line:
            return lines, False  # present but out-of-order — fallback

    empty_form = EMPTY_FORMS.get(section_name)
    if empty_form is None:
        return lines, False

    try:
        my_position = CANONICAL_H3_ORDER.index(section_name)
    except ValueError:
        return lines, False
    later_sections = CANONICAL_H3_ORDER[my_position + 1:]

    insert_idx = len(lines)
    for i, line in enumerate(lines):
        if not line.startswith("### "):
            continue
        if any(ls in line for ls in later_sections):
            insert_idx = i
            break

    block = empty_form.split("\n") + [""]
    return lines[:insert_idx] + block + lines[insert_idx:], True


def splice_trail_per_verdict_emoji(lines: list[str], violation: dict) -> tuple[list[str], bool]:
    """Replace the legacy bucket emoji after `→` on the trail line for the
    given L-anchor with the per-verdict glyph for the recorded verdict word.

    `expected` ≈ "trail line for L<n> renders `<want>` for verdict `<word>`".
    """
    expected = violation.get("expected", "")
    em = re.search(r"renders `([^`]+)` for verdict `([^`]+)`", expected)
    if not em:
        return lines, False
    want_emoji, word = em.group(1), em.group(2)

    anchor = violation.get("line_ref", "")
    idx = _find_trail_line_index(lines, anchor)
    if idx < 0:
        return lines, False

    line = lines[idx]
    # Replace the glyph immediately after `→` (with any preceding whitespace).
    new_line, n = re.subn(r"(→\s+)\S+(\s+)", lambda m: m.group(1) + want_emoji + m.group(2), line, count=1)
    if n == 0:
        return lines, False
    lines = lines[:]
    lines[idx] = new_line
    return lines, True


def splice_trail_canonical_verdict_word(lines: list[str], violation: dict) -> tuple[list[str], bool]:
    """Replace a freelanced verdict token with the canonical word (and the
    glyph it maps to) on the trail line for the given L-anchor.

    Derive the canonical word from the rendered glyph via
    CANONICAL_VERDICT_FOR_EMOJI. If the glyph isn't one of the six, defer.
    """
    anchor = violation.get("line_ref", "")
    idx = _find_trail_line_index(lines, anchor)
    if idx < 0:
        return lines, False
    line = lines[idx]
    # Parse the `→ <glyph> <bad-token>` shape.
    m = re.search(r"→\s+(\S+)\s+(\S+)", line)
    if not m:
        return lines, False
    emoji, bad_tok = m.group(1), m.group(2)
    canonical = CANONICAL_VERDICT_FOR_EMOJI.get(emoji)
    if canonical is None:
        return lines, False
    # Strip trailing punctuation on the bad token (`:.,;)`) when replacing.
    bad_stripped = bad_tok.rstrip(":.,;)")
    if not bad_stripped:
        return lines, False
    new_line = line.replace(f"→ {emoji} {bad_tok}", f"→ {emoji} {canonical}", 1)
    if new_line == line:
        new_line = line.replace(f"→ {emoji}\t{bad_tok}", f"→ {emoji} {canonical}", 1)
    if new_line == line:
        return lines, False
    lines = lines[:]
    lines[idx] = new_line
    return lines, True


def splice_verified_claims_trail_faithful(lines: list[str], violation: dict) -> tuple[list[str], bool]:
    """Restore the trail line's `<emoji> <word>` to what the artifact records.

    `actual` ≈ "trail says `<wrong>`; artifact says `<right>` — evidence: ...".
    `line_ref` is the artifact's `line_range` (may be `L42` or `L42-L58`).
    The right glyph is `EXPECTED_TRAIL_EMOJI[right]`.
    """
    actual = violation.get("actual", "")
    wrong_m = re.search(r"trail says `([^`]+)`", actual)
    right_m = re.search(r"artifact says `([^`]+)`", actual)
    if not wrong_m or not right_m:
        return lines, False
    wrong, right = wrong_m.group(1), right_m.group(1)
    if right not in EXPECTED_TRAIL_EMOJI:
        return lines, False
    right_emoji = EXPECTED_TRAIL_EMOJI[right]

    idx = _find_trail_line_index(lines, violation.get("line_ref", ""))
    if idx < 0:
        return lines, False
    line = lines[idx]
    # Replace the pair after `→` with the canonical emoji + word.
    new_line, n = re.subn(
        r"(→\s+)\S+\s+\S+",
        lambda m: m.group(1) + f"{right_emoji} {right}",
        line,
        count=1,
    )
    if n == 0:
        return lines, False
    # Restore any trailing punctuation we may have eaten — preserve content
    # after the word/punct boundary unchanged. Simpler: only consume the
    # exact two whitespace-separated tokens after the arrow.
    new_line = re.sub(
        r"(→\s+)\S+(\s+)\S+",
        lambda m: m.group(1) + right_emoji + m.group(2) + right,
        line,
        count=1,
    )
    if new_line == line:
        return lines, False
    lines = lines[:]
    lines[idx] = new_line
    return lines, True


def splice_pass3_unverifiable_evidence(lines: list[str], violation: dict) -> tuple[list[str], bool]:
    """Insert `; <pointer-phrase>` immediately before the closing `)` of the
    trail line's parenthetical, where pointer-phrase is parsed from the hint.

    `hint` carries: ``Insert `; <pointer phrase>` immediately before that closing `)`...``
    """
    hint = violation.get("hint", "")
    pm = re.search(r"Insert `;\s*([^`]+)`", hint)
    if not pm:
        return lines, False
    phrase = pm.group(1).strip()

    # Parse the L-anchor out of line_ref like `<🔍 Verification trail: L42 in `path`>`.
    am = re.search(r"L\d+(?:-\d+)?", violation.get("line_ref", ""))
    if not am:
        return lines, False
    anchor = am.group(0)

    idx = _find_trail_line_index(lines, anchor)
    if idx < 0:
        return lines, False
    line = lines[idx]
    if ")" not in line:
        return lines, False
    last_close = line.rfind(")")
    # Don't re-insert if the phrase is already present.
    if phrase[:30] in line:
        return lines, False
    new_line = line[:last_close] + f"; {phrase}" + line[last_close:]
    lines = lines[:]
    lines[idx] = new_line
    return lines, True


def _external_claim_required_segment(violation: dict) -> str | None:
    """Best-effort extraction of the segment to append from `hint`.

    The hints for external-claim-* rules carry a worked example wrapped in
    backticks, like ``Append `· 4 specialists (...); 2 cross-specialist
    corroborations` to the bullet``. We pull that worked example as the
    literal segment to append. If the hint doesn't carry one, defer.
    """
    hint = violation.get("hint", "")
    # First backticked segment that looks like an appendable bullet tail
    # (starts with `· `, `routed:`, or `(verified `).
    for m in re.finditer(r"`([^`]+)`", hint):
        seg = m.group(1)
        if seg.startswith("· ") or seg.lstrip().startswith("routed:") or seg.startswith("(verified "):
            return seg
    return None


def splice_external_claim_state_format(lines: list[str], violation: dict) -> tuple[list[str], bool]:
    """Rewrite the leading `X of Y claims verified (N unverifiable, M contradicted)`
    state form on the External claim verification bullet — fallback only when the
    hint carries a literal replacement; this rule is genuinely judgment-heavy
    (V/N/M counts come from the trail, not the violation payload). Defer to
    fallback when no literal replacement is available.
    """
    # No deterministic source for V/N/M in the violation payload; defer.
    return lines, False


def splice_external_claim_dispatch_metadata(lines: list[str], violation: dict) -> tuple[list[str], bool]:
    """Append `· N specialists (...); K cross-specialist corroborations` to the
    External claim verification bullet, after the leading state form.
    """
    seg = _external_claim_required_segment(violation)
    if seg is None:
        return lines, False
    idx = _find_external_claim_line_index(lines)
    if idx < 0:
        return lines, False
    line = lines[idx].rstrip()
    if "specialists" in line and "cross-specialist corroborations" in line:
        return lines, False  # already present
    # Insert before any `· routed:` segment if present, otherwise append.
    routed_pos = line.find("· routed:")
    if routed_pos >= 0:
        new_line = line[:routed_pos] + seg + " " + line[routed_pos:]
    else:
        # Append with the `· ` separator; the hint's example already carries it.
        sep = "" if seg.startswith("·") else "· "
        new_line = line.rstrip(".") + " " + sep + seg
        if lines[idx].endswith("."):
            new_line += "."
    lines = lines[:]
    lines[idx] = new_line
    return lines, True


def splice_external_claim_routed_metadata(lines: list[str], violation: dict) -> tuple[list[str], bool]:
    """Append `· routed: I inline, P Pass 1, F Pass 2[, S Pass 3]` to the
    External claim verification bullet. Defer when V/C/U parentheticals are
    required but the violation payload doesn't carry the right integers — the
    routed-metadata check itself doesn't have those.
    """
    seg = _external_claim_required_segment(violation)
    if seg is None:
        return lines, False
    idx = _find_external_claim_line_index(lines)
    if idx < 0:
        return lines, False
    line = lines[idx].rstrip()
    if "routed:" in line:
        return lines, False  # already present
    sep = "" if seg.startswith("·") else "· "
    new_line = line.rstrip(".") + " " + sep + seg
    if lines[idx].endswith("."):
        new_line += "."
    lines = lines[:]
    lines[idx] = new_line
    return lines, True


def splice_external_claim_pass2_outcome(lines: list[str], violation: dict) -> tuple[list[str], bool]:
    """Append `(verified V, contradicted C, unverifiable U)` to the Pass 2
    segment OR drop it when Pass 2 count is 0.

    The validator's two distinct violations:
    - "omit `(verified V, contradicted C, unverifiable U)` when Pass 2 count is 0"
    - "`Pass 2` segment carries `(...)` parenthetical when F > 0"

    Without V/C/U integers in the violation payload, the F > 0 case can't be
    spliced deterministically; defer to fallback.
    """
    expected = violation.get("expected", "")
    idx = _find_external_claim_line_index(lines)
    if idx < 0:
        return lines, False
    line = lines[idx]
    if "omit" in expected:
        # Drop the empty/zero parenthetical from `0 Pass 2 (verified V, ...)`.
        new_line = re.sub(
            r"(\b0\s+Pass\s+2)\s*\(verified\s+\d+,\s*contradicted\s+\d+,\s*unverifiable\s+\d+\)",
            r"\1",
            line,
        )
        if new_line == line:
            return lines, False
        lines = lines[:]
        lines[idx] = new_line
        return lines, True
    # F > 0 — payload doesn't carry V/C/U.
    return lines, False


def splice_bucket_bullet_line_range_prefix(lines: list[str], violation: dict) -> tuple[list[str], bool]:
    """Prepend `- **[L<a>-<b>]**` to the offending bucket bullet, using the
    matching trail record's anchor.

    Match strategy: look up the bullet in body (by the `actual` snippet),
    pull a quoted phrase out of it, find a trail record whose raw line
    contains the same phrase. If no quoted phrase or no matching trail
    record, defer to fallback.
    """
    actual = violation.get("actual", "").strip()
    if not actual:
        return lines, False
    # Find the bullet line.
    bullet_idx = -1
    for i, line in enumerate(lines):
        if line.lstrip().startswith("- **") and actual[:60] in line:
            bullet_idx = i
            break
        if line.lstrip().startswith("**") and actual[:60] in line:
            bullet_idx = i
            break
    if bullet_idx < 0:
        return lines, False

    bullet = lines[bullet_idx]

    # Extract a long-enough quoted substring to match against trail records.
    quoted = None
    for q in re.findall(r'"([^"]{15,})"', bullet) + re.findall(r'`([^`]{15,})`', bullet):
        quoted = q
        break
    if quoted is None:
        return lines, False

    # Walk trail records for a match.
    span = _section_span(lines, "🔍 Verification trail")
    if span is None:
        return lines, False
    start, end = span
    anchor = None
    for i in range(start, end):
        if quoted in lines[i]:
            m = _TRAIL_LINE_ANCHOR_RE.match(lines[i])
            if m:
                anchor = m.group(1)
                break
    if anchor is None:
        return lines, False

    # Build the prefix.
    prefix = f"**[{anchor}]**"
    # If the bullet already has a `**...**` bold-prefix that's not the bracketed
    # form, replace it; otherwise prepend.
    stripped = bullet.lstrip()
    indent = bullet[: len(bullet) - len(stripped)]
    body_part = stripped[2:] if stripped.startswith("- ") else stripped  # drop the "- "
    leading_dash = "- " if stripped.startswith("- ") else ""

    bold_prefix_re = re.compile(r"^\*\*[^*]+\*\*\s*")
    if bold_prefix_re.match(body_part):
        body_part = bold_prefix_re.sub("", body_part, count=1)

    new_bullet = f"{indent}{leading_dash}{prefix} {body_part}"
    lines = lines[:]
    lines[bullet_idx] = new_bullet
    return lines, True


SPLICERS = {
    "internal-link-existence": splice_internal_link_existence,
    "shortcode-existence": splice_shortcode_existence,
    "mandatory-h3-order": splice_mandatory_h3_order,
    "trail-per-verdict-emoji": splice_trail_per_verdict_emoji,
    "trail-canonical-verdict-word": splice_trail_canonical_verdict_word,
    "verified-claims-trail-faithful": splice_verified_claims_trail_faithful,
    "pass-3-unverifiable-evidence": splice_pass3_unverifiable_evidence,
    "external-claim-state-format": splice_external_claim_state_format,
    "external-claim-dispatch-metadata": splice_external_claim_dispatch_metadata,
    "external-claim-routed-metadata": splice_external_claim_routed_metadata,
    "external-claim-pass2-outcome": splice_external_claim_pass2_outcome,
    "bucket-bullet-line-range-prefix": splice_bucket_bullet_line_range_prefix,
}

SURGICAL_RULES = set(SPLICERS.keys())


# ---- Orchestration ---------------------------------------------------------


def apply_splices(body: str, violations: list[dict]) -> tuple[str, list[str], list[str]]:
    """Apply every surgical splice. Returns (new_body, applied_rule_ids,
    fallback_rule_ids). Non-surgical violations are silently passed through."""
    lines = body.splitlines()
    keep_trailing_newline = body.endswith("\n")

    by_rule: dict[str, list[dict]] = {}
    for v in violations:
        rid = v.get("rule_id")
        if rid in SURGICAL_RULES:
            by_rule.setdefault(rid, []).append(v)

    applied: list[str] = []
    fallback: list[str] = []

    for rule_id in APPLY_ORDER:
        rule_violations = by_rule.get(rule_id) or []
        if not rule_violations:
            continue
        splicer = SPLICERS[rule_id]
        successes = 0
        for v in rule_violations:
            new_lines, ok = splicer(lines, v)
            if ok:
                lines = new_lines
                successes += 1
        if successes == len(rule_violations):
            applied.append(rule_id)
        else:
            fallback.append(rule_id)

    new_body = "\n".join(lines)
    if keep_trailing_newline and not new_body.endswith("\n"):
        new_body += "\n"
    return new_body, applied, fallback


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--body-file", required=True)
    parser.add_argument("--fix-me-json", required=True)
    parser.add_argument("--fallback-json", default=DEFAULT_FALLBACK_JSON)
    args = parser.parse_args()

    body_path = Path(args.body_file)
    if not body_path.is_file():
        print(f"::error::splicer.py: body file not found: {body_path}", file=sys.stderr)
        return 1

    fix_path = Path(args.fix_me_json)
    if not fix_path.is_file():
        # No fix-me JSON → nothing to splice.
        print(f"splicer.py: no fix-me JSON at {fix_path}; nothing to splice", file=sys.stderr)
        return 0

    try:
        fix_data = json.loads(fix_path.read_text())
    except json.JSONDecodeError as e:
        print(f"::error::splicer.py: malformed fix-me JSON {fix_path}: {e}", file=sys.stderr)
        return 1

    violations = fix_data.get("violations") or []
    if not violations:
        return 0

    surgical = [v for v in violations if v.get("rule_id") in SURGICAL_RULES]
    if not surgical:
        # All violations are non-surgical; nothing for the splicer to do.
        return 0

    body = body_path.read_text()
    new_body, applied, fallback = apply_splices(body, surgical)

    if new_body != body:
        body_path.write_text(new_body)

    if applied:
        print(
            f"splicer.py: applied surgical fixes for rule(s): {', '.join(applied)}",
            file=sys.stderr,
        )

    if fallback:
        fallback_payload = {
            "fallback_needed": fallback,
            "applied": applied,
        }
        Path(args.fallback_json).write_text(json.dumps(fallback_payload, indent=2))
        print(
            f"::warning::splicer.py: deferred rule(s) to fallback lane: {', '.join(fallback)}",
            file=sys.stderr,
        )
        return 2

    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""compose-review.py — assemble an ~80%-done review draft from the pre-step artifacts.

Runs as a workflow pre-step AFTER `verify-claims.py` (and the other pre-steps)
and BEFORE the Opus review job. It reads the artifacts the other pre-steps
emitted (`.verified-claims.json`, `.vale-findings.json`, `.editorial-balance.json`,
`.cross-sibling-discovery.json`, `.frontmatter-validation.json`, `.hugo-build.json`,
and `.candidate-claims.json` as a fallback) plus `gh pr diff` for diff context,
and writes `.review-draft.md` at the workspace root — a review body that's
already structurally complete and self-consistent. Opus then EDITS it (triages
the stub bucket bullets, adds the findings the composer can't pre-stub, fills the
`<TODO>` tokens) rather than ASSEMBLING it from scratch over 100+ Bash-thrash
turns.

The design frame: **the composer ASSEMBLES, Opus JUDGES.** The composer never
decides which findings surface — it lays out the skeleton, renders the 🔍 trail
verbatim from `.verified-claims.json`, the bucket-count table, the investigation
log scaffold, the 📊 Editorial-balance Tier 1, the `#### Style findings` block,
the 📜 Review-history line, and *stub* 🚨/⚠️ bucket bullets (one per promoting
verdict) carrying a `<TODO>` marker. Whether a stub is a real finding, what the
fix prose should be, the summary paragraph, the confidence levels, the
cross-sibling read count, the Tier-2 editorial balance — those are `<TODO>`s for
Opus. Pushing any of that into the composer re-opens the discovery-variance hole
and degrades the output.

After emitting the draft, the composer runs `validate-pinned.py check
--skip-rule no-todo-tokens` against its own output. A clean pass means the draft
is structurally sound (the `<TODO>` tokens are expected and the `no-todo-tokens`
rule is suppressed for the self-check; the publish path does NOT skip it). A
*failure* means a composer bug or a contradictory upstream artifact — the
composer prepends a visible `> [!CAUTION]` banner INTO `.review-draft.md` (never
a silent-empty file or a file-presence heuristic) so Opus sees the failure and
falls back to manual assembly per `ci.md` §Fallback, and emits a `::error::`
annotation for the operator.

Separately from that self-check `> [!CAUTION]` banner (which means "discard this
draft, assemble manually"), the composer emits a distinct `> [!WARNING]`
verifier-outage banner between the header and the Summary when it detects that
the fact-check verifier was DOWN for this run (transport/API errors in
`.verified-claims.json` — see the outage sentinels above). That banner means
"this draft is usable, but fact-checking didn't actually run — findings are
unverified"; it also pre-fills the `facts` confidence row to LOW so the posted
review can't present unverified findings as `facts: HIGH`. The two banners are
deliberately different alert levels so the model lane (and maintainers) don't
conflate "discard" with "read carefully."

Degrades gracefully: any uncaught exception → `safe_main()` writes a minimal
valid fallback draft (the `> [!CAUTION]` banner shape) and returns 0; the
workflow's `||` stub is reserved for can't-even-start failures and writes the
same shape. A missing/empty artifact → that section renders in its degraded
form with a banner note; the composer never crashes and never blocks the
pipeline.

Usage:
    compose-review.py --out .review-draft.md --pr <N> --repo <owner/repo> \
        --timestamp <ISO8601> --head-sha <sha> [--head-sha-short <sha>] \
        [--verified-claims .verified-claims.json] [--candidate-claims .candidate-claims.json] \
        [--vale-findings .vale-findings.json] [--editorial-balance .editorial-balance.json] \
        [--cross-sibling .cross-sibling-discovery.json] [--frontmatter .frontmatter-validation.json] \
        [--hugo-build .hugo-build.json] [--repo-root .] [--no-validate] [--dry-run]
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import traceback
from pathlib import Path

# ---- constants -------------------------------------------------------------

# Quick-win: an `unverifiable` *factual* claim renders in ⚠️ Low-confidence
# (with an author-question line), not 🚨. Flip to "outstanding" if that spec
# change reverts. (The validator never enforced always-🚨 for unverifiable —
# `_trail_is_outstanding` only keys on `contradicted`/`mismatch` — so either
# value keeps the draft structurally valid.)
PROMOTE_UNVERIFIABLE_TO = "warning"

TRAIL_VERDICT_WORDS = ("verified", "matches", "not-a-claim", "unverifiable", "contradicted", "mismatch")
EXPECTED_TRAIL_EMOJI = {
    "verified": "✅",
    "matches": "🤝",
    "not-a-claim": "➖",
    "unverifiable": "🤷",
    "contradicted": "❌",
    "mismatch": "⚔️",
}
OUTSTANDING_VERDICTS = {"contradicted", "mismatch"}

# Mirror of `validate-pinned.py` TEMPORAL_TRIGGERS — keep synchronized.
TEMPORAL_TRIGGERS = {
    "recently", "now supports", "now available", "new", "just launched",
    "latest", "introduced", "as of", "starting", "going forward",
}

# Truncation budgets for verbatim artifact text (the trail can hold 80-110
# entries; on a claims-dense post that approaches the 65K body cap — keep
# entries terse).
TEXT_TRUNC = 160
EVIDENCE_TRUNC = 240

GH_TIMEOUT = 30

# Outage sentinels written by verify-claims.py when a per-claim verifier hit a
# transport/API failure (HTTP 5xx, overloaded, network) rather than a genuine
# unverifiable (paywall / dead link / turn-cap). The evidence marker is THE
# signal — verify-claims.py writes it only in process_claim()'s except handler
# (verify-claims.py:675); the error marker is its top-level errors[] companion
# (verify-claims.py:669). The turn-cap message ("verification did not converge
# within N turns") is an ORDINARY unverifiable and must NOT match — keep the
# predicate keyed on these markers, never on the `unverifiable` verdict alone.
_VERIFIER_OUTAGE_EVIDENCE_MARKER = "verify-claims.py errored on this claim:"
_VERIFIER_OUTAGE_ERROR_MARKER = "verifier failed:"
_VERIFIER_OUTAGE_TOKENS = (
    "HTTP 500", "HTTP 502", "HTTP 503", "HTTP 529",
    "Internal server error", "api_error", "overloaded",
    "RuntimeError: HTTP", "URLError", "TimeoutError",
)
# Evidence the candidate-claims floor carries when verify-claims didn't complete
# at all (the `verdicts is None` degraded path below) — also an outage.
_FLOOR_DEGRADED_EVIDENCE = "claim verification did not complete"

FALLBACK_BANNER_DRAFT = """## Pre-merge Review — Last updated {ts}

> [!CAUTION]
> The review composer (`compose-review.py`) did not produce a usable draft ({reason}). Do **not** post the lines below — assemble the review manually per `.claude/commands/docs-review/ci.md` §Fallback (manual assembly): read the pre-step artifacts (`.verified-claims.json` for the trail/verdicts, `.vale-findings.json` for style, `.editorial-balance.json` for Tier 1, `.hugo-build.json`, `.frontmatter-validation.json`, `.cross-sibling-discovery.json`) and render per `docs-review:references:output-format`. This stub exists so the consumer sees the failure rather than a missing file.

_(composer stub — see ci.md §Fallback)_
"""

# ---- credential redaction (backstop; mirrors fact-check.md §Credential redaction) ----

_REDACT_PATTERNS = [
    re.compile(r"\bghp_[A-Za-z0-9]{20,}\b"),
    re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\bsk-[A-Za-z0-9\-]{16,}\b"),
    re.compile(r"\bAKIA[0-9A-Z]{12,}\b"),
    re.compile(r"\bpul-[a-f0-9]{32,}\b"),
    re.compile(r"\bxox[bpars]-[A-Za-z0-9\-]{10,}\b"),
    re.compile(r"\beyJ[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}\b"),  # JWT
    re.compile(r"\bhttps?://[^/\s:@]+:[^/\s@]+@[^\s]+"),  # user:pass@host
]
# An opaque ≥40-char alphanumeric blob that isn't a hex git SHA (7-40 hex) and
# isn't a UUID — conservative to avoid clobbering real evidence text.
_OPAQUE_BLOB_RE = re.compile(r"\b(?![0-9a-fA-F]{7,40}\b)[A-Za-z0-9]{40,}\b")


def redact(s: str) -> str:
    if not s:
        return s
    out = s
    for pat in _REDACT_PATTERNS:
        out = pat.sub("[REDACTED]", out)
    out = _OPAQUE_BLOB_RE.sub("[REDACTED]", out)
    return out


# ---- artifact loaders (graceful — None means absent, [] / {} present-but-empty) ----


def _load_json(path: str | None):
    if not path:
        return None
    p = Path(path)
    if not p.is_file():
        return None
    try:
        return json.loads(p.read_text())
    except (OSError, json.JSONDecodeError):
        return None


def load_verified_claims(path: str | None) -> tuple[list[dict] | None, list[str], dict]:
    """Return (verdicts | None, errors, meta). None means the artifact is
    absent; [] means present but empty (the verify-claims step crashed)."""
    data = _load_json(path)
    if not isinstance(data, dict):
        return None, [], {}
    verdicts = data.get("verdicts")
    if not isinstance(verdicts, list):
        return None, [], {}
    errors = data.get("errors") if isinstance(data.get("errors"), list) else []
    meta = data.get("meta") if isinstance(data.get("meta"), dict) else {}
    return [v for v in verdicts if isinstance(v, dict)], errors, meta


def load_candidate_claims(path: str | None) -> list[dict] | None:
    data = _load_json(path)
    if not isinstance(data, dict):
        return None
    claims = data.get("claims")
    if not isinstance(claims, list):
        return None
    return [c for c in claims if isinstance(c, dict)]


def load_vale_findings(path: str | None) -> list[dict]:
    data = _load_json(path)
    if not isinstance(data, list):
        return []
    return [f for f in data if isinstance(f, dict)]


def load_editorial_balance(path: str | None) -> dict | None:
    data = _load_json(path)
    return data if isinstance(data, dict) else None


def load_cross_sibling(path: str | None) -> list[dict]:
    data = _load_json(path)
    if not isinstance(data, dict):
        return []
    files = data.get("files")
    return [f for f in files if isinstance(f, dict)] if isinstance(files, list) else []


def load_frontmatter(path: str | None) -> list[dict]:
    data = _load_json(path)
    if not isinstance(data, dict):
        return []
    files = data.get("files")
    return [f for f in files if isinstance(f, dict)] if isinstance(files, list) else []


def load_hugo_build(path: str | None) -> dict | None:
    data = _load_json(path)
    return data if isinstance(data, dict) else None


# ---- preflight synthetic verdicts (Hugo + frontmatter pre-stubs) -----------


# Hugo error lines often embed a file path + optional line number. Recognise:
#   "page.md:LINE:COL"   (most common)
#   "page.md:LINE"
#   `"page.md"`          (no line — fall back to L1)
#   anywhere `content/.../page.md` appears
_HUGO_FILE_LINE_RE = re.compile(
    r"""
    (?P<file>(?:content|layouts|themes)/[\w./\-]+\.(?:md|html|toml|yaml|yml))
    (?::(?P<line>\d+))?
    """,
    re.VERBOSE,
)


def _hugo_extract_file_line(raw: str) -> tuple[str, str]:
    """Return (file, L-anchor) parsed from a Hugo error/link-integrity line.
    Anchor is empty string when no line number is recoverable; the synthetic
    verdict then falls back to L1 (the frontmatter block / top of file)."""
    m = _HUGO_FILE_LINE_RE.search(raw)
    if not m:
        return ("", "")
    file = m.group("file")
    line = m.group("line")
    return (file, f"L{line}" if line else "")


_HUGO_SOURCE = "hugo --renderToMemory pre-step"
_FM_SOURCE = "frontmatter-validate.py pre-step"


def _hugo_synthetic_verdicts(hugo_artifact: dict | None) -> list[dict]:
    """Synthesize verdict-shaped dicts from `.hugo-build.json` so the composer
    pre-stubs Hugo errors and link-integrity breakages into 🚨 Outstanding.
    These flow through render_trail (as `❌ contradicted` lines) and
    build_stubs (as `**[L<n>]**` bullets) just like real fact-check verdicts.
    Routed as `preflight` so build_stubs writes a confirm-or-REMOVE TODO
    rather than the fact-check fix-or-spurious-or-mis-sourced TODO.
    """
    if not isinstance(hugo_artifact, dict):
        return []
    if hugo_artifact.get("skipped"):
        return []
    out: list[dict] = []
    for entry in hugo_artifact.get("errors", []) or []:
        if not isinstance(entry, str) or not entry.strip():
            continue
        file, anchor = _hugo_extract_file_line(entry)
        out.append({
            "claim_id": f"hugo-error-{len(out)}",
            "file": file,
            "line_range": anchor or "L1",
            "text": entry.strip()[:TEXT_TRUNC],
            "type": "hugo-build-error",
            "route": "preflight",
            "verdict": "contradicted",
            "confidence": "high",
            "evidence": entry.strip(),
            "source": _HUGO_SOURCE,
        })
    for entry in hugo_artifact.get("link_integrity", []) or []:
        if not isinstance(entry, str) or not entry.strip():
            continue
        file, anchor = _hugo_extract_file_line(entry)
        out.append({
            "claim_id": f"hugo-link-{len(out)}",
            "file": file,
            "line_range": anchor or "L1",
            "text": entry.strip()[:TEXT_TRUNC],
            "type": "hugo-link-integrity",
            "route": "preflight",
            "verdict": "contradicted",
            "confidence": "high",
            "evidence": entry.strip(),
            "source": _HUGO_SOURCE,
        })
    return out


def _frontmatter_synthetic_verdicts(frontmatter_files: list[dict]) -> list[dict]:
    """Synthesize verdicts from `.frontmatter-validation.json`'s `files[]` array.

    Three failure classes get pre-stubbed as `⚔️ mismatch` (so they surface
    in 🚨 Outstanding via the mismatch promotion path):
      - `menu_parents[].parent_exists_in_menu == false`  (broken nav parent)
      - `alias_collisions[]`                              (alias hits another file)
      - `url_collisions[]`                                (URL hits another file)

    No line number is recoverable from the artifact, so all anchor at L1
    (the frontmatter block at the top of the file). The reviewer's editorial
    pass triages PR-internal-rename cases (move the bullet to 💡 Pre-existing
    with a `**Pre-existing:**` label) vs real collisions.
    """
    out: list[dict] = []
    for fm in frontmatter_files or []:
        if not isinstance(fm, dict):
            continue
        fpath = fm.get("file") or ""
        for parent in fm.get("menu_parents", []) or []:
            if not isinstance(parent, dict) or parent.get("parent_exists_in_menu") is not False:
                continue
            menu = parent.get("menu_name") or "?"
            pid = parent.get("parent_identifier") or "?"
            also = parent.get("found_in_other_menus") or []
            also_note = f" (parent identifier exists in: {', '.join(also)})" if also else ""
            out.append({
                "claim_id": f"fm-parent-{len(out)}",
                "file": fpath,
                "line_range": "L1",
                "text": f"frontmatter `menu.{menu}.parent: {pid}` does not exist in the `{menu}` menu{also_note}"[:TEXT_TRUNC],
                "type": "frontmatter-menu-parent",
                "route": "preflight",
                "verdict": "mismatch",
                "confidence": "high",
                "evidence": f"menu={menu} parent={pid} parent_exists_in_menu=false",
                "source": _FM_SOURCE,
            })
        for col in fm.get("alias_collisions", []) or []:
            if not isinstance(col, dict):
                continue
            alias = col.get("alias") or "?"
            collides = col.get("collides_with") or "?"
            out.append({
                "claim_id": f"fm-alias-{len(out)}",
                "file": fpath,
                "line_range": "L1",
                "text": f"frontmatter alias `{alias}` collides with `{collides}`"[:TEXT_TRUNC],
                "type": "frontmatter-alias-collision",
                "route": "preflight",
                "verdict": "mismatch",
                "confidence": "high",
                "evidence": f"alias={alias} collides_with={collides}",
                "source": _FM_SOURCE,
            })
        for col in fm.get("url_collisions", []) or []:
            if not isinstance(col, dict):
                continue
            url = col.get("url") or col.get("alias") or "?"
            collides = col.get("collides_with") or col.get("claimants") or "?"
            out.append({
                "claim_id": f"fm-url-{len(out)}",
                "file": fpath,
                "line_range": "L1",
                "text": f"frontmatter URL `{url}` collides with `{collides}`"[:TEXT_TRUNC],
                "type": "frontmatter-url-collision",
                "route": "preflight",
                "verdict": "mismatch",
                "confidence": "high",
                "evidence": f"url={url} collides_with={collides}",
                "source": _FM_SOURCE,
            })
    return out


# ---- gh helpers ------------------------------------------------------------


def _gh(args: list[str]) -> str:
    try:
        proc = subprocess.run(["gh", *args], capture_output=True, text=True, timeout=GH_TIMEOUT)
    except (subprocess.SubprocessError, OSError):
        return ""
    return proc.stdout or ""


def gh_diff_name_only(pr: str, repo: str | None, override: str | None = None) -> list[str]:
    if override is not None:
        return [f.strip() for f in override.split(",") if f.strip()]
    args = ["pr", "diff", str(pr), "--name-only"]
    if repo:
        args += ["--repo", repo]
    return [ln.strip() for ln in _gh(args).splitlines() if ln.strip()]


def gh_diff_text(pr: str, repo: str | None) -> str:
    args = ["pr", "diff", str(pr)]
    if repo:
        args += ["--repo", repo]
    return _gh(args)


# ---- small helpers ---------------------------------------------------------

_L_TOKEN_RE = re.compile(r"L\d+(?:-\d+)?")


def line_refs(line_range: str) -> list[str]:
    """All L-tokens in a `line_range` ('L42' / 'L42-47' / 'L12, L88, L91')."""
    return _L_TOKEN_RE.findall(line_range or "")


def first_line_ref(line_range: str) -> str:
    """The first L-token, or 'L0' as a degenerate fallback (keeps the draft
    self-consistent rather than crashing on a malformed range)."""
    refs = line_refs(line_range)
    return refs[0] if refs else "L0"


def trunc(s: str, n: int) -> str:
    s = (s or "").strip().replace("\n", " ")
    return s if len(s) <= n else s[: n - 1].rstrip() + "…"


def quote(s: str) -> str:
    return '"' + (s or "").replace('"', "'") + '"'


def is_blog_diff(diff_files: list[str]) -> bool:
    return any(f.startswith("content/blog/") for f in diff_files)


def touches_programs(diff_files: list[str]) -> bool:
    return any(f.startswith("static/programs/") for f in diff_files)


# ---- section renderers -----------------------------------------------------


def render_header(timestamp: str) -> str:
    return f"## Pre-merge Review — Last updated {timestamp}"


def count_verifier_outages(verdicts: list[dict] | None) -> tuple[int, int]:
    """Return (n_outage, n_total) over fact-check verdicts. A verdict is an
    OUTAGE when its evidence carries the script-error marker (a transport/API
    failure verify-claims.py caught), OR carries an outage token AND is
    `unverifiable`, OR is the candidate-floor degraded placeholder. Ordinary
    unverifiables (turn-cap, dead link, paywall) do NOT count — they don't
    carry the markers. Call BEFORE appending Hugo/frontmatter synthetic
    verdicts so preflight verdicts don't dilute the ratio."""
    n_total = len(verdicts or [])
    n_outage = 0
    for v in verdicts or []:
        ev = str(v.get("evidence") or "")
        if _VERIFIER_OUTAGE_EVIDENCE_MARKER in ev or ev == _FLOOR_DEGRADED_EVIDENCE:
            n_outage += 1
        elif v.get("verdict") == "unverifiable" and any(tok in ev for tok in _VERIFIER_OUTAGE_TOKENS):
            n_outage += 1
    return n_outage, n_total


def render_verifier_outage_banner(n_outage: int, n_total: int) -> str:
    """A `> [!WARNING]` banner (distinct from the self-check `> [!CAUTION]`
    discard banner) telling the reader fact-checking was degraded. Empty string
    when no outage. Author-facing wording (no internal tooling names)."""
    if n_outage <= 0:
        return ""
    retry = ("Once the service is back, mention `@claude #new-review` to "
             "regenerate a complete review from scratch.")
    if n_outage >= n_total:
        return (
            "> [!WARNING]\n"
            "> **Automated fact-checking did not run for this review.** The "
            f"verification service returned errors for all {n_total} extracted "
            "claim(s), so every finding below is script-generated and unverified "
            "— treat the 🔍 Verification trail and the Summary as **unconfirmed** "
            "and fact-check the claims manually before relying on them. "
            "(`facts` confidence is forced to LOW for this reason.) " + retry
        )
    return (
        "> [!WARNING]\n"
        "> **Automated fact-checking was incomplete for this review.** The "
        f"verification service errored on {n_outage} of {n_total} claim(s); those "
        "trail entries are unconfirmed — spot-check them manually. " + retry
    )


def render_summary_block(confidence_dims: list[str], forced_levels: dict[str, tuple[str, str]] | None = None) -> str:
    forced_levels = forced_levels or {}

    def _row(d: str) -> str:
        if d in forced_levels:
            level, note = forced_levels[d]
            return f"> | {d} | {level} | {note} |"
        return f"> | {d} | <TODO: HIGH/MEDIUM/LOW> | <TODO: short note when not HIGH; leave empty when HIGH> |"

    rows = "\n".join(_row(d) for d in confidence_dims)
    return (
        "> [!TIP]\n"
        "> **Summary:** <TODO: one paragraph — (1) what this PR is (content type + subject; for a new page, which existing pages it parallels), "
        "(2) what specific kind of wrongness would block a reader's success, (3) which investigative passes ran>.\n"
        ">\n"
        "> **Review confidence:**\n"
        ">\n"
        "> | Dimension | Level | Notes |\n"
        "> | :--- | :---: | :--- |\n"
        f"{rows}"
    )


def render_investigation_log(
    *,
    cross_sibling: list[dict],
    verdicts: list[dict],
    route_counts: dict,
    frontmatter: list[dict],
    has_temporal_trigger: bool,
    diff_files: list[str],
    has_fenced_code_in_content: bool,
    editorial_balance: dict | None,
    is_blog: bool,
    diff_unavailable: bool,
) -> str:
    bullets: list[str] = []

    # 1. Cross-sibling reads.
    templated = [f for f in cross_sibling if f.get("in_templated_section")]
    if not templated:
        bullets.append("- **Cross-sibling reads:** not run (not in a templated section)")
    else:
        # Y = the dispatch-list size for the (first) templated file. The leading
        # count starts at 0 (the reviewer's sibling-read fan-out runs in the
        # review pass, not here) — ci.md §3 tells the reviewer to overwrite it.
        # Keep the parenthetical reader-facing (no internal-tooling names).
        y = len(templated[0].get("siblings_for_dispatch") or templated[0].get("directory_peers") or [])
        bullets.append(f"- **Cross-sibling reads:** 0 of {y} siblings")

    # 2. External claim verification.
    if not verdicts:
        bullets.append("- **External claim verification:** not run (no claims in this diff)")
    else:
        y = len(verdicts)
        x = sum(1 for v in verdicts if v.get("verdict") in ("verified", "matches"))
        n_unver = sum(1 for v in verdicts if v.get("verdict") == "unverifiable")
        n_contra = sum(1 for v in verdicts if v.get("verdict") in ("contradicted", "mismatch"))
        i_inline = route_counts.get("inline", 0)
        p1 = route_counts.get("pass1", 0)
        f2 = route_counts.get("pass2", 0)
        s3 = route_counts.get("pass3", 0)
        k_corr = route_counts.get("k_corr", 0)
        seg = (
            f"- **External claim verification:** {x} of {y} claims verified "
            f"({n_unver} unverifiable, {n_contra} contradicted) · "
            f"4 specialists (numerical, cross-reference, capability, framing); "
            f"{k_corr} cross-specialist corroborations · "
            f"routed: {i_inline} inline, {p1} Pass 1, {f2} Pass 2"
        )
        if f2 > 0:
            v2, c2, u2 = route_counts.get("pass2_vcu", (0, 0, 0))
            seg += f" (verified {v2}, contradicted {c2}, unverifiable {u2})"
        seg += f", {s3} Pass 3"
        if s3 > 0:
            v3, c3, u3 = route_counts.get("pass3_vcu", (0, 0, 0))
            seg += f" (verified {v3}, contradicted {c3}, unverifiable {u3})"
        seg += "."
        bullets.append(seg)

    # 3. Cited-claim spot-checks.
    n_cited = sum(1 for v in verdicts if v.get("route") == "pass2")
    if n_cited == 0:
        bullets.append("- **Cited-claim spot-checks:** not run (no cited claims)")
    else:
        bullets.append(f"- **Cited-claim spot-checks:** {n_cited} of {n_cited} cited claims fetched and compared")

    # 4. Frontmatter sweep.
    if not frontmatter:
        bullets.append("- **Frontmatter sweep:** not run (no frontmatter in diff)")
    else:
        keys: set[str] = set()
        for f in frontmatter:
            for k in f.get("frontmatter_keys") or []:
                keys.add(str(k))
        locs = ["body"]
        if any(k == "meta_desc" or k.startswith("meta_desc.") for k in keys):
            locs.append("meta_desc")
        social_subs = sorted(k.split(".", 1)[1] for k in keys if k.startswith("social."))
        if social_subs:
            locs.append("social.{" + ", ".join(social_subs) + "}")
        bullets.append(f"- **Frontmatter sweep:** ran on {' + '.join(locs)}")

    # 5. Temporal-trigger sweep.
    if diff_unavailable:
        bullets.append("- **Temporal-trigger sweep:** ran (sweep runs in-review — confirm matches)")
    elif has_temporal_trigger:
        bullets.append("- **Temporal-trigger sweep:** ran (recency words present in diff; spot-check in-review)")
    else:
        bullets.append("- **Temporal-trigger sweep:** not run (no trigger words)")

    # 6. Code execution.
    if touches_programs(diff_files):
        progs = sorted({"/".join(f.split("/")[:3]) for f in diff_files if f.startswith("static/programs/")})
        bullets.append(
            f"- **Code execution:** ran {', '.join(progs)} (CI test harness gates parse + imports)"
        )
    else:
        bullets.append("- **Code execution:** not run (no `static/programs/` change)")

    # 7. Code-examples checks.
    if touches_programs(diff_files) and not has_fenced_code_in_content:
        bullets.append("- **Code-examples checks:** ran (1 specialist: body-code-coverage); 0 findings")
    elif has_fenced_code_in_content:
        bullets.append("- **Code-examples checks:** ran (3 specialists: structural, existence, body-code-coverage); 0 findings")
    elif diff_unavailable:
        bullets.append("- **Code-examples checks:** ran (3 specialists: structural, existence, body-code-coverage); 0 findings")
    else:
        bullets.append("- **Code-examples checks:** not run (no fenced code blocks in content files)")

    # 8. Editorial-balance pass.
    if not is_blog:
        bullets.append("- **Editorial-balance pass:** not run (not under content/blog/)")
    elif not editorial_balance or editorial_balance.get("trigger") is None:
        bullets.append("- **Editorial-balance pass:** ran (single-subject, N/A)")
    else:
        target = _eb_target(editorial_balance)
        n_h2 = len(target.get("sections") or []) if target else 0
        n_flags = len(target.get("outliers") or []) if target else 0
        bullets.append(f"- **Editorial-balance pass:** ran ({n_h2} H2 sections, {n_flags} flags fired)")

    return "<details>\n<summary>Investigation log</summary>\n\n" + "\n".join(bullets) + "\n\n</details>"


def render_count_table(a: int, b: int, c: int, d: int) -> str:
    return (
        "| 🚨 Outstanding | ⚠️ Low-confidence | 💡 Pre-existing | ✅ Resolved |\n"
        "| :---: | :---: | :---: | :---: |\n"
        f"| **{a}** | **{b}** | **{c}** | **{d}** |"
    )


# Italic one-liners that open the 🚨 / ⚠️ sections when they have findings
# (parallel to `*Found by pattern-based linting; Findings may be false
# positives.*` under `#### Style findings`) — omitted on the explicit-empty form.
_OUTSTANDING_NOTE = "*These must be resolved or refuted before merging.*"
_LOWCONF_NOTE = "*Review each and resolve as appropriate — these don't block the PR.*"


# `source` sentinels `verify-claims.py` emits when it has no real citation
# (turn-cap exhausted, per-claim error, deterministic pass-0 resolution) — not
# reader-facing "sources"; drop them rather than leak the script name.
_INTERNAL_SOURCE_PREFIXES = ("verify-claims.py", "(no source pointer", "(no source")


def _clean_source(src: str) -> str:
    s = (src or "").strip()
    if not s or any(s.startswith(p) for p in _INTERNAL_SOURCE_PREFIXES):
        return ""
    return redact(s)


def _evidence_pointer(v: dict) -> str:
    ev = redact(trunc(v.get("evidence") or "", EVIDENCE_TRUNC))
    src = _clean_source(str(v.get("source") or ""))
    parts = []
    fn = (v.get("framing_note") or "").strip()
    if fn:
        parts.append(f"framing: {redact(trunc(fn, 160))}")
    if ev:
        parts.append(f"evidence: {ev}")
    if src:
        parts.append(f"source: {src}")
    intu = (v.get("intuition_flag") or "").strip()
    if intu:
        parts.append(f"intuition: {redact(trunc(intu, 120))}")
    body = "; ".join(parts) if parts else "no evidence summary recorded"
    # Pass-3 unverifiable verdicts that didn't converge get a synthetic
    # search-was-run pointer so `pass-3-unverifiable-evidence` is satisfied
    # and the statement stays honest.
    if (
        v.get("route") == "pass3"
        and v.get("verdict") == "unverifiable"
        and not re.search(r"WebSearch|search ran|searched|query", body, re.IGNORECASE)
    ):
        body += " (WebSearch dispatched but verification did not converge within the turn budget)"
    return body


def render_trail(verdicts: list[dict], degraded_note: str | None) -> tuple[str, int, int, int, int]:
    """Return (block, n, x_verified, y_unverifiable, z_contradicted)."""
    if not verdicts:
        return ("### 🔍 Verification trail\n\n_No verifiable claims extracted from this diff._", 0, 0, 0, 0)
    n = len(verdicts)
    x = sum(1 for v in verdicts if v.get("verdict") in ("verified", "matches"))
    y = sum(1 for v in verdicts if v.get("verdict") == "unverifiable")
    z = sum(1 for v in verdicts if v.get("verdict") in ("contradicted", "mismatch"))
    lines: list[str] = []
    for v in verdicts:
        verdict = v.get("verdict")
        if verdict not in TRAIL_VERDICT_WORDS:
            verdict = "unverifiable"  # defensive — verify-claims.py already coerces
        emoji = EXPECTED_TRAIL_EMOJI[verdict]
        refs = line_refs(v.get("line_range") or "")
        first = refs[0] if refs else "L0"
        also = ""
        if len(refs) > 1:
            also = " (also " + ", ".join(refs[1:]) + ")"
        text = quote(redact(trunc(v.get("text") or "", TEXT_TRUNC)))
        pointer = _evidence_pointer(v)
        file_path = (v.get("file") or "").strip()
        file_in = f" in `{file_path}`" if file_path else ""
        lines.append(f"- {first}{file_in} {text}{also} → {emoji} {verdict} ({pointer})")
    header = (
        f"<details>\n<summary><strong>{n} claims extracted</strong> · "
        f"<strong>{x}</strong> verified · <strong>{y}</strong> unverifiable · "
        f"<strong>{z}</strong> contradicted</summary>"
    )
    block = "### 🔍 Verification trail\n\n" + header + "\n\n" + "\n".join(lines) + "\n\n</details>"
    if degraded_note:
        block += f"\n\n_{degraded_note}_"
    return (block, n, x, y, z)


def _eb_target(eb: dict) -> dict | None:
    files = eb.get("files") or []
    # The artifact strips `trigger_local`; the validator's fallback (and ours)
    # is "first file with non-empty sections".
    return next((f for f in files if f.get("sections")), None)


def render_editorial_balance(eb: dict | None, is_blog: bool) -> str:
    if not is_blog:
        return ""  # omitted entirely on non-blog (mandatory-h3-order only requires it on blog)
    if not eb or eb.get("trigger") is None:
        return "### 📊 Editorial balance\n\n_Single-subject post; balance check N/A._"
    target = _eb_target(eb)
    if target is None:
        return "### 📊 Editorial balance\n\n_Single-subject post; balance check N/A._"
    n = len(target.get("sections") or [])
    stats = target.get("stats") or {}
    mean = stats.get("mean", 0)
    median = stats.get("median", 0)
    std = stats.get("std", 0)
    outliers = target.get("outliers") or []
    if outliers:
        out_str = "Outliers: " + ", ".join(
            f"{o.get('heading', '?')}: {o.get('lines', 0)} ({o.get('ratio', 0)}× median)" for o in outliers
        ) + "."
    else:
        out_str = "No section-depth outliers (≥3× median)."
    return (
        "### 📊 Editorial balance\n\n"
        "<details>\n<summary>Section depth, mention distribution, recommendation steering</summary>\n\n"
        f"- **Section depth:** {n} H2 sections (mean {mean} lines, median {median}, std {std}). {out_str}\n"
        "- **Vendor / entity mentions:** <TODO: entity-A: count · entity-B: count · … (one per distinctly-mentioned vendor/product)>.\n"
        "- **FAQ steering** (if a FAQ section is present): <TODO: N FAQ entries; count recommend X; count recommend Y — or delete this bullet if there's no FAQ section>.\n\n"
        "</details>"
    )


def render_outstanding(stubs: list[dict]) -> str:
    # Empty form is reader-facing — the "what the reviewer should add here"
    # guidance lives in ci.md §3, never in the published body.
    if not stubs:
        return "### 🚨 Outstanding in this PR\n\n_No outstanding findings in this PR._"
    lines = ["### 🚨 Outstanding in this PR", "", _OUTSTANDING_NOTE, ""]
    # Blank line between bullets renders as a "loose list" — each bullet gets
    # paragraph-level vertical spacing so a stack of 8+ findings doesn't read
    # as a wall of text. Validators' extract_bucket_bullets keys off the
    # leading `**` so blank lines between bullets don't false-positive.
    for i, s in enumerate(stubs):
        if i > 0:
            lines.append("")
        lines.append(s["bullet"])
    return "\n".join(lines)


def render_lowconfidence(stubs: list[dict], vale_findings: list[dict]) -> str:
    has_style = bool(vale_findings)
    if not stubs and not has_style:
        return "### ⚠️ Low-confidence\n\n_No low-confidence findings._"
    lines = ["### ⚠️ Low-confidence", "", _LOWCONF_NOTE, ""]
    for i, s in enumerate(stubs):
        if i > 0:
            lines.append("")
        lines.append(s["bullet"])
    if has_style:
        if stubs:
            lines.append("")
        lines.append(_render_style_findings(vale_findings))
    return "\n".join(lines)


def _style_mode(total: int, n_files: int) -> str:
    if total <= 5:
        return "inline"
    if n_files <= 1 and total <= 30:
        return "inline"
    if total > 30:
        return "collapse"
    if n_files > 1 and total > 5:
        return "collapse"
    return "inline"


def _render_style_findings(findings: list[dict]) -> str:
    total = len(findings)
    by_file: dict[str, list[dict]] = {}
    for f in findings:
        by_file.setdefault(str(f.get("file") or "?"), []).append(f)
    n_files = len(by_file)
    mode = _style_mode(total, n_files)
    out = ["#### Style findings", "", "*Found by pattern-based linting; Findings may be false positives.*", ""]
    if mode == "inline":
        for f in sorted(findings, key=lambda x: (str(x.get("file") or ""), int(x.get("line") or 0))):
            cat = str(f.get("category") or "style")
            msg = str(f.get("message") or "").strip()
            out.append(f"- **line {f.get('line', '?')}:** [style] _{cat}_ — {msg}")
    else:
        out.append("<sub>Click each filename to expand.</sub>")
        out.append("")
        for fname in sorted(by_file):
            items = sorted(by_file[fname], key=lambda x: int(x.get("line") or 0))
            kind_counts: dict[str, int] = {}
            for it in items:
                kind_counts[str(it.get("category") or "style")] = kind_counts.get(str(it.get("category") or "style"), 0) + 1
            kinds_sorted = sorted(kind_counts.items(), key=lambda kv: (-kv[1], kv[0]))
            breakdown = ", ".join(f"<strong>{c}</strong> {k}" for k, c in kinds_sorted)
            out.append(f"<details>")
            out.append(f"<summary><strong>{fname}</strong> (<strong>{len(items)}</strong> issues: {breakdown})</summary>")
            out.append("")
            for it in items:
                cat = str(it.get("category") or "style")
                msg = str(it.get("message") or "").strip()
                out.append(f"- **line {it.get('line', '?')}:** [style] _{cat}_ — {msg}")
            out.append("")
            out.append("</details>")
            out.append("")
        # drop trailing blank
        while out and out[-1] == "":
            out.pop()
    return "\n".join(out)


def render_triaged() -> str:
    # Always rendered, always wrapped in a collapsed <details>. The reviewer
    # moves verifier-side noise (false positives, mis-sourced verdicts) here
    # during the editorial pass so they don't clutter 🚨 / ⚠️. The empty
    # marker `_No triaged findings._` is the signal strip-empty-triaged.py
    # uses to remove the whole section when the reviewer didn't move any
    # bullets in.
    return (
        "### 📋 Triaged verifier findings\n\n"
        "<details>\n"
        "<summary><em>I double-checked these and realized they weren't real findings — click to expand</em></summary>\n\n"
        "_No triaged findings._\n\n"
        "</details>"
    )


def render_preexisting() -> str:
    return "### 💡 Pre-existing issues in touched files (optional)\n\n_No pre-existing issues in touched files._"


def render_resolved() -> str:
    return "### ✅ Resolved since last review\n\n_No items resolved since the last review._"


def render_review_history(timestamp: str, head_sha_short: str) -> str:
    return (
        "### 📜 Review history\n\n"
        f"- {timestamp} — <TODO: one-line summary of what this review found> ({head_sha_short})"
    )


def render_footer() -> str:
    return (
        "---\n"
        "Need a re-review? Want to dispute a finding? Mention `@claude` and include `#update-review`.  \n"
        "(For ad-hoc questions or fixes, just `@claude` — no hashtag.)"
    )


# ---- stub bucket bullets ---------------------------------------------------


def _stub_bullet(v: dict, todo: str) -> dict:
    ref = first_line_ref(v.get("line_range") or "")
    text = quote(redact(trunc(v.get("text") or "", TEXT_TRUNC)))
    verdict = v.get("verdict") or "?"
    pointer = _evidence_pointer(v)
    file_path = (v.get("file") or "").strip()
    # Bullet shape: `- **[L<n>]** `<file>` — *"<claim text>"* — <commentary>`.
    # Three visually distinct segments separated by em-dashes:
    #   1. L-prefix + file path (the validator anchors here)
    #   2. italicized quoted claim (so the reader can scan claims fast)
    #   3. verdict + evidence pointer + TODO (the actionable bit)
    # The file path is rendered AFTER `**[L<n>]**` so the validator's
    # bucket-bullet-line-range-prefix regex (`^\s*-\s+\*\*\[(L\d+...)\]\*\*`)
    # still anchors on the L-token; the filename disambiguates which file
    # the line number refers to on multi-file PRs.
    file_part = f" `{file_path}` —" if file_path else ""
    italic_text = f"*{text}*" if text else text
    bullet = f"- **[{ref}]**{file_part} {italic_text} — verdict: {verdict}; {pointer} <TODO: {todo}>"
    return {"ref": ref, "bullet": bullet, "verdict": verdict}


def build_stubs(verdicts: list[dict]) -> tuple[list[dict], list[dict]]:
    """Return (outstanding_stubs, lowconfidence_stubs)."""
    outstanding: list[dict] = []
    lowconf: list[dict] = []
    for v in verdicts:
        verdict = v.get("verdict")
        conf = (v.get("confidence") or "").lower()
        route = v.get("route") or ""
        # Preflight verdicts (Hugo + frontmatter pre-step) carry a different
        # TODO shape — the reviewer's job is "confirm or REMOVE if CI noise,"
        # not "triage against verifier source choices."
        if route == "preflight" and verdict in OUTSTANDING_VERDICTS:
            vtype = v.get("type") or ""
            if vtype.startswith("hugo-"):
                todo = ("confirm the fix needed (or REMOVE the bullet if this is a CI-environment near-miss — "
                        "e.g., a transient render-time warning that doesn't reproduce on a clean Hugo build). "
                        "If pre-existing on a line this PR didn't touch, replace the body with `**Pre-existing:** <reason>` "
                        "AND move the bullet to `### 💡 Pre-existing`.")
            else:
                todo = ("triage: is this a real collision (alias or URL clashes with another live page) "
                        "or a PR-internal rename (an old alias for a file this PR is restructuring)? "
                        "Confirm the fix needed, or REMOVE the bullet if the collision is intentional and announced. "
                        "If pre-existing, replace with `**Pre-existing:** <reason>` AND move to `### 💡 Pre-existing`.")
            outstanding.append(_stub_bullet(v, todo))
            continue
        if verdict in OUTSTANDING_VERDICTS:
            if verdict == "mismatch":
                todo = ("write the fix / suggestion block. Anti-hedge mandate: state which sibling pages corroborate the divergence "
                        "and what the author must change; do NOT soften to a manual-check ask. "
                        "If you judge the verdict spurious, replace the body with `**Spurious:** <1-2 sentence reason>` "
                        "AND move the bullet to `### 📋 Triaged verifier findings` (do NOT leave it in 🚨; "
                        "do NOT add `no author action required` / `nothing to fix` codas — the `**Spurious:**` label IS the resolution). "
                        "If pre-existing on a line this PR didn't touch, replace with `**Pre-existing:** <reason>` AND move to `### 💡 Pre-existing`. "
                        "`trail-verdict-bucket-promotion` accepts the bullet under 🚨, 📋, or 💡.")
            else:
                todo = ("write the fix / suggestion block for the author (quote-and-rewrite mandate). "
                        "If you judge the verdict spurious (verifier checked stale data / wrong site / SPA page / missed a PR-local alias / "
                        "compared a paraphrased version of the claim), replace the body with `**Spurious:** <1-2 sentence reason>` "
                        "AND move the bullet to `### 📋 Triaged verifier findings` (do NOT leave it in 🚨; "
                        "do NOT add `no author action required` / `nothing to fix` codas — the `**Spurious:**` label IS the resolution). "
                        "If pre-existing on a line this PR didn't touch, replace with `**Pre-existing:** <reason>` AND move to `### 💡 Pre-existing`. "
                        "`trail-verdict-bucket-promotion` accepts the bullet under 🚨, 📋, or 💡.")
            outstanding.append(_stub_bullet(v, todo))
        elif verdict == "unverifiable":
            if PROMOTE_UNVERIFIABLE_TO == "outstanding":
                outstanding.append(_stub_bullet(
                    v, "if this isn't actually a checkable factual claim, it should be `not-a-claim` not `unverifiable`; "
                       "otherwise file the author-question buffer line and keep here. "
                       "If the verifier was demonstrably mis-sourced (wrong URL followed, ran out of turns on a duplicate, etc.), "
                       "replace the body with `**Mis-sourced:** <reason>` AND move the bullet to `### 📋 Triaged verifier findings`."))
            else:
                lowconf.append(_stub_bullet(
                    v, "if this is a factual blocker (a price/spec/capability with no citation a reader needs), promote to 🚨 Outstanding; "
                       "either way file the author-question buffer line. REMOVE only if it's not actually a checkable claim "
                       "(then it should already be `not-a-claim`). "
                       "If the verifier was demonstrably mis-sourced (wrong URL followed, ran out of turns on a duplicate, "
                       "the cited URL was unrelated to the claim subject, etc.), replace the body with `**Mis-sourced:** <reason>` "
                       "AND move the bullet to `### 📋 Triaged verifier findings`."))
        elif verdict == "verified" and conf == "low":
            lowconf.append(_stub_bullet(
                v, "this is a `verified weakly` claim — confirm the residual judgment is about reader impact; if it's actually fine, REMOVE; "
                   "if there's a real concern, write the note"))
        # high/medium verified, matches, not-a-claim → trail-only, no stub
    return outstanding, lowconf


# ---- route accounting ------------------------------------------------------


def compute_route_counts(verdicts: list[dict], candidate_claims: list[dict] | None) -> dict:
    # `inline` = pass0 (deterministic, no model verifier dispatched); P/F/S come
    # from each verdict's recorded `route` (not meta.n_pass*, which is the
    # pre-reroute count — verify-claims.py re-routes pass2→pass3 when the URL
    # isn't actually in .fetched-urls.json).
    by_route = {"pass0": 0, "pass1": 0, "pass2": 0, "pass3": 0}
    for v in verdicts:
        r = v.get("route") or "pass1"
        if r not in by_route:
            r = "pass1"
        by_route[r] += 1

    def vcu(route: str) -> tuple[int, int, int]:
        v = c = u = 0
        for x in verdicts:
            if x.get("route") != route:
                continue
            verd = x.get("verdict")
            if verd in ("verified", "matches"):
                v += 1
            elif verd in ("contradicted", "mismatch"):
                c += 1
            else:  # unverifiable / not-a-claim (rare on an external lane)
                u += 1
        return (v, c, u)

    k_corr = 0
    if candidate_claims:
        k_corr = sum(1 for c in candidate_claims if c.get("cross_specialist_corroboration"))

    return {
        "inline": by_route["pass0"],
        "pass1": by_route["pass1"],
        "pass2": by_route["pass2"],
        "pass3": by_route["pass3"],
        "pass2_vcu": vcu("pass2"),
        "pass3_vcu": vcu("pass3"),
        "k_corr": k_corr,
    }


# ---- compose ---------------------------------------------------------------


def compose(args: argparse.Namespace) -> str:
    verdicts, vc_errors, _vc_meta = load_verified_claims(args.verified_claims)
    candidate_claims = load_candidate_claims(args.candidate_claims)
    vale_findings = load_vale_findings(args.vale_findings)
    editorial_balance = load_editorial_balance(args.editorial_balance)
    cross_sibling = load_cross_sibling(args.cross_sibling)
    frontmatter = load_frontmatter(args.frontmatter)
    hugo_build = load_hugo_build(args.hugo_build)

    head_sha = (args.head_sha or "").strip()
    head_sha_short = (args.head_sha_short or "").strip() or (head_sha[:8] if head_sha else "unknown")
    timestamp = (args.timestamp or "").strip() or "unknown"

    if args.diff_files is not None:
        diff_files = gh_diff_name_only("", None, override=args.diff_files)
        diff_text = ""
        diff_unavailable = False
    elif args.pr and not args.dry_run:
        diff_files = gh_diff_name_only(args.pr, args.repo)
        diff_text = gh_diff_text(args.pr, args.repo)
        diff_unavailable = not diff_files
    else:
        diff_files = []
        diff_text = ""
        diff_unavailable = False
    is_blog = is_blog_diff(diff_files)
    has_temporal_trigger = any(t in diff_text.lower() for t in TEMPORAL_TRIGGERS) if diff_text else False
    has_fenced_code_in_content = bool(diff_text) and bool(re.search(r"^\+\s*```", diff_text, re.MULTILINE))

    degraded_note: str | None = None
    if verdicts is None:
        # Claim verification didn't complete — fall back to the candidate-claims
        # floor. (Reader-facing strings only; ci.md §Fallback tells the reviewer
        # to re-verify each claim in the review pass.)
        if candidate_claims:
            verdicts = [
                {
                    "claim_id": c.get("id", "?"),
                    "file": c.get("file", ""),
                    "line_range": c.get("line_range", ""),
                    "text": c.get("text", ""),
                    "type": c.get("type", ""),
                    "route": "pass1",
                    "verdict": "unverifiable",
                    "confidence": "low",
                    "evidence": "claim verification did not complete",
                    "source": "",
                }
                for c in candidate_claims
            ]
            degraded_note = ("Claim verification did not complete; the trail entries below are placeholders — "
                             "each claim was re-verified during the review pass.")
        else:
            verdicts = []
    elif vc_errors:
        degraded_note = ("Claim verification reported errors — some verdicts may be incomplete; "
                         "spot-check the affected claims in-review.")

    # Detect a fact-check verifier OUTAGE (transport/API errors) on the
    # fact-check verdicts ONLY — measure before appending Hugo/frontmatter
    # synthetics so preflight verdicts don't dilute the ratio. When detected,
    # the composer emits a prominent `> [!WARNING]` banner and pre-fills the
    # `facts` confidence row to LOW (so the posted review can't present
    # unverified findings as `facts: HIGH`).
    n_outage, n_outage_total = count_verifier_outages(verdicts)
    outage_banner = render_verifier_outage_banner(n_outage, n_outage_total)

    # Append synthetic verdicts from the Hugo + frontmatter pre-steps so the
    # composer pre-stubs those findings into 🚨 Outstanding rather than
    # leaving them for Opus to discover and triage from `.hugo-build.json`
    # / `.frontmatter-validation.json` artifacts. Routed as `preflight` —
    # build_stubs branches on the route to emit a confirm-or-REMOVE TODO
    # instead of the fact-check spurious-or-mis-sourced TODO.
    verdicts = list(verdicts) + _hugo_synthetic_verdicts(hugo_build) + _frontmatter_synthetic_verdicts(frontmatter)

    route_counts = compute_route_counts(verdicts, candidate_claims)

    outstanding_stubs, lowconf_stubs = build_stubs(verdicts)
    style_count = len(vale_findings)
    a = len(outstanding_stubs)
    b = len(lowconf_stubs) + style_count
    c_pre = 0
    d_resolved = 0

    confidence_dims = ["mechanics", "facts"]
    if any(f.get("in_templated_section") for f in cross_sibling):
        confidence_dims.append("cross-sibling consistency")
    if is_blog and editorial_balance and editorial_balance.get("trigger") is not None:
        confidence_dims.append("editorial balance")
    if touches_programs(diff_files) or has_fenced_code_in_content or (
        hugo_build and (hugo_build.get("errors") or hugo_build.get("link_integrity"))
    ):
        confidence_dims.append("code correctness")

    trail_block, _n, _x, _y, _z = render_trail(verdicts, degraded_note)

    # On a verifier outage, pre-fill the `facts` row to LOW deterministically so
    # the posted review can't read `facts: HIGH` even if Opus doesn't cooperate.
    forced_levels: dict[str, tuple[str, str]] = {}
    if outage_banner:
        forced_levels["facts"] = ("LOW", "automated fact-checking errored — claims unverified")

    sections: list[str] = [render_header(timestamp), ""]
    if outage_banner:
        sections += [outage_banner, ""]
    sections += [
        render_summary_block(confidence_dims, forced_levels),
        "",
        render_investigation_log(
            cross_sibling=cross_sibling,
            verdicts=verdicts,
            route_counts=route_counts,
            frontmatter=frontmatter,
            has_temporal_trigger=has_temporal_trigger,
            diff_files=diff_files,
            has_fenced_code_in_content=has_fenced_code_in_content,
            editorial_balance=editorial_balance,
            is_blog=is_blog,
            diff_unavailable=diff_unavailable,
        ),
        "",
        render_count_table(a, b, c_pre, d_resolved),
        "",
        trail_block,
        "",
    ]
    eb_block = render_editorial_balance(editorial_balance, is_blog)
    if eb_block:
        sections.append(eb_block)
        sections.append("")
    sections += [
        render_outstanding(outstanding_stubs),
        "",
        render_lowconfidence(lowconf_stubs, vale_findings),
        "",
        render_triaged(),
        "",
        render_preexisting(),
        "",
        render_resolved(),
        "",
        render_review_history(timestamp, head_sha_short),
        "",
        render_footer(),
        "",
    ]
    return "\n".join(sections)


# ---- self-check ------------------------------------------------------------


def run_self_check(draft_path: Path, args: argparse.Namespace) -> list[dict]:
    """Run validate-pinned.py check --skip-rule no-todo-tokens on the draft.
    Return the list of violation dicts (empty = clean)."""
    script_dir = Path(__file__).resolve().parent
    validator = script_dir / "validate-pinned.py"
    if not validator.is_file():
        return []  # can't self-check; not fatal
    out_json = Path("/tmp/compose-review.validate.json")
    cmd = [
        sys.executable, str(validator), "check",
        "--body-file", str(draft_path),
        "--skip-rule", "no-todo-tokens",
        "--output-json", str(out_json),
        "--output-markdown", "/tmp/compose-review.validate.md",
    ]
    if args.pr:
        cmd += ["--pr", str(args.pr)]
    if args.repo:
        cmd += ["--repo", args.repo]
    for opt, val in (
        ("--verified-claims", args.verified_claims),
        ("--candidate-claims", args.candidate_claims),
        ("--fetched-urls", args.fetched_urls),
        ("--editorial-balance", args.editorial_balance),
    ):
        if val:
            cmd += [opt, val]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    except (subprocess.SubprocessError, OSError) as e:
        print(f"compose-review: self-check could not run validate-pinned.py: {e}", file=sys.stderr)
        return []
    if proc.returncode == 0:
        return []
    try:
        data = json.loads(out_json.read_text())
        return data.get("violations", []) if isinstance(data, dict) else []
    except (OSError, json.JSONDecodeError):
        return [{"rule_id": "self-check-unparseable", "line_ref": "<validator>",
                 "expected": "validate-pinned.py emits a parseable fix-me JSON",
                 "actual": f"exit {proc.returncode}; output unparseable",
                 "hint": proc.stderr.strip()[:300]}]


def prepend_caution_banner(draft_path: Path, violations: list[dict], timestamp: str) -> None:
    summary = "; ".join(f"{v.get('rule_id', '?')}@{v.get('line_ref', '?')}" for v in violations[:8])
    if len(violations) > 8:
        summary += f"; (+{len(violations) - 8} more)"
    banner = (
        f"## Pre-merge Review — Last updated {timestamp}\n\n"
        "> [!CAUTION]\n"
        f"> The review composer (`compose-review.py`) produced a structurally-invalid draft "
        f"({len(violations)} validator violation(s)). Do **not** use the sections below as-is — "
        f"assemble the review manually per `.claude/commands/docs-review/ci.md` §Fallback (manual assembly) "
        f"and validate before posting. Violations: {summary}.\n"
    )
    try:
        existing = draft_path.read_text()
    except OSError:
        existing = ""
    # Drop the draft's own `## Pre-merge Review` first line if present, then prepend.
    lines = existing.splitlines()
    if lines and lines[0].startswith("## Pre-merge Review"):
        lines = lines[1:]
        # also drop a single leading blank
        if lines and not lines[0].strip():
            lines = lines[1:]
    draft_path.write_text(banner + "\n" + "\n".join(lines).lstrip("\n") + ("\n" if not existing.endswith("\n") else ""))


# ---- main / safe_main ------------------------------------------------------


def _write_fallback(out_path: Path, reason: str, timestamp: str) -> None:
    try:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(FALLBACK_BANNER_DRAFT.format(ts=timestamp or "unknown", reason=reason))
    except OSError:
        pass


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--out", required=True, help="Output draft path (.review-draft.md)")
    p.add_argument("--pr", help="PR number (for `gh pr diff` context)")
    p.add_argument("--repo", help="owner/repo (for gh)")
    p.add_argument("--repo-root", default=".", help="Repo root (default: cwd)")
    p.add_argument("--timestamp", help="ISO-8601 UTC review timestamp (from the workflow)")
    p.add_argument("--head-sha", help="PR head SHA")
    p.add_argument("--head-sha-short", help="PR head SHA (short); derived from --head-sha if absent")
    p.add_argument("--verified-claims", default=".verified-claims.json")
    p.add_argument("--candidate-claims", default=".candidate-claims.json")
    p.add_argument("--vale-findings", default=".vale-findings.json")
    p.add_argument("--editorial-balance", default=".editorial-balance.json")
    p.add_argument("--cross-sibling", default=".cross-sibling-discovery.json")
    p.add_argument("--frontmatter", default=".frontmatter-validation.json")
    p.add_argument("--hugo-build", default=".hugo-build.json")
    p.add_argument("--fetched-urls", default=".fetched-urls.json")
    p.add_argument("--diff-files", help="Comma-separated changed-file list (overrides `gh pr diff --name-only`; for testing).")
    p.add_argument("--no-validate", action="store_true", help="Skip the self-check (local debugging).")
    p.add_argument("--dry-run", action="store_true", help="Don't call gh; emit the draft only.")
    args = p.parse_args()

    out_path = Path(args.out)
    timestamp = (args.timestamp or "").strip() or "unknown"

    draft = compose(args)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(draft if draft.endswith("\n") else draft + "\n")

    if not args.no_validate:
        violations = run_self_check(out_path, args)
        if violations:
            prepend_caution_banner(out_path, violations, timestamp)
            summary = "; ".join(f"{v.get('rule_id', '?')}@{v.get('line_ref', '?')}" for v in violations[:5])
            if len(violations) > 5:
                summary += f"; (+{len(violations) - 5} more)"
            print(f"::error::compose-review.py self-check failed — {len(violations)} violation(s): {summary}", file=sys.stderr)
            print("compose-review: wrote a > [!CAUTION] banner into the draft; Opus will fall back to manual assembly.", file=sys.stderr)
        else:
            print("compose-review: draft self-check clean.", file=sys.stderr)

    print(f"compose-review: wrote {out_path}", file=sys.stderr)
    return 0


def safe_main() -> int:
    try:
        return main()
    except SystemExit:
        raise
    except BaseException as e:  # noqa: BLE001 — deliberately broad; never crash the pipeline
        out_path = None
        timestamp = "unknown"
        argv = sys.argv
        for i, a in enumerate(argv):
            if a == "--out" and i + 1 < len(argv):
                out_path = Path(argv[i + 1])
            elif a.startswith("--out="):
                out_path = Path(a.split("=", 1)[1])
            elif a == "--timestamp" and i + 1 < len(argv):
                timestamp = argv[i + 1]
            elif a.startswith("--timestamp="):
                timestamp = a.split("=", 1)[1]
        if out_path is not None:
            _write_fallback(out_path, f"uncaught exception: {type(e).__name__}: {e}", timestamp)
        traceback.print_exc(file=sys.stderr)
        return 0


if __name__ == "__main__":
    sys.exit(safe_main())

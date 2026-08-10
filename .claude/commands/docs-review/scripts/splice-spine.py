#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Restore invariant "evidence spine" sections a re-render dropped.

WHY THIS EXISTS
---------------
`pinned-comment.sh upsert` is a transport: it splits the body it is handed,
stamps markers, and PATCHes the existing comments in place. It never reads the
OLD comments' content -- it fetches their ids, not their bodies -- so a refresh
that re-renders the review without its 🔍 Verification trail publishes cleanly
and the job goes green. On `claude-update.yml` that loss is permanent: the lane
does a fresh shallow checkout and runs only Vale, so it has no
`.candidate-claims.json` / `.verified-claims.json` to rebuild from, and the
pinned comment it just overwrote was the only copy. Later refreshes then merge
from the damaged body, so the loss compounds.

Measured on 2026-08-10 (`2026-08-10-update-lane-model-config` in
pulumi/docs-review-benchmarks): the shipping configuration dropped the spine in
1 of 6 chained refreshes, and `--effort low` in 3 of 6 -- one of those collapsing
a 40-line trail to 11 lines and then holding exactly 11 through the next
refresh, because the "floor" it was checked against had moved down with it.

WHAT IS INVARIANT, AND WHY VERBATIM RESTORE IS CORRECT
------------------------------------------------------
Three sections describe the review's own INVESTIGATION, not the findings' state:

  * 🔍 Verification trail   -- which claims were extracted and how they verified
  * 📊 Editorial balance    -- the balance pass's own tally (content/blog only)
  * Investigation log       -- which passes ran, as a <details> block

Moving a finding to ✅ Resolved does not retire its trail record, so a refresh
has no legitimate reason to shrink any of them. The update lane cannot extract
new claims at all (no claims artifacts in its workspace), so on that lane they
cannot legitimately GROW either -- but growth is allowed here anyway, because
the composer lane can and does add trail lines. The rule is the one already in
the render contract: **may add, never drop.**

SAFETY POSTURE
--------------
This runs immediately before publication, on a body nobody has seen yet, so a
wrong repair would corrupt a good review. Every ambiguous case therefore
no-ops rather than guessing:

  * prior body absent, empty, or unparseable      -> no-op
  * section missing from prior                    -> no-op (nothing to restore)
  * section in the new body is same size or larger-> no-op
  * section missing from the new body entirely    -> restore only if the H3
                                                     order in MANDATORY_H3_SECTIONS
                                                     fixes where it goes
  * anything raises                               -> no-op, exit 0, warn

Exit status is ALWAYS 0 unless the arguments themselves are unusable. This is a
repair pass, not a gate: it must never be the reason a review fails to publish.

Usage:
  splice-spine.py --prior <file> --body <file> [--in-place] [--report <json>]
      --prior   the published pinned body, as `pinned-comment.sh fetch` emits it
                (parts joined by the delimiter, each with marker and footer)
      --body    the newly rendered body about to be published
      --in-place  rewrite --body with restored sections (default: print to stdout)
      --report  write a JSON summary of what was restored

Parsing reuses validate-pinned.py's helpers (find_section, section_text,
extract_trail_records, INVESTIGATION_LOG_BULLETS) by the same import-by-path
pattern scrape-review-outcomes.py uses, so the comment-format contract keeps
exactly one parser.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent

_spec = importlib.util.spec_from_file_location("validate_pinned", HERE / "validate-pinned.py")
_vp = importlib.util.module_from_spec(_spec)
# Register before exec: validate-pinned.py defines dataclasses, and the
# dataclass machinery resolves the defining module through sys.modules.
sys.modules["validate_pinned"] = _vp
_spec.loader.exec_module(_vp)

# Mirrors pinned-comment.sh: FOOTER_SENTINEL (:41), the fetch delimiter (:161),
# and the continuation block split_body re-opens across a page boundary (:212).
FOOTER_SENTINEL = "<!-- CLAUDE_REVIEW_FOOTER -->"
PART_DELIMITER = "----- PINNED-COMMENT-DELIMITER -----"
MARKER_RE = re.compile(r"^<!-- CLAUDE_REVIEW \d+/\d+ -->\s*$")
CONTINUATION_SUMMARY = "<summary><em>continued from previous comment</em></summary>"

TRAIL_HEADING = "🔍 Verification trail"
BALANCE_HEADING = "📊 Editorial balance"
INVESTIGATION_SUMMARY = "<summary>Investigation log</summary>"


def log(msg: str) -> None:
    print(f"splice-spine: {msg}", file=sys.stderr)


def extract_trail_records_of(body: str) -> list[dict]:
    """Re-export, so callers and tests never reach past this module's parser."""
    return _vp.extract_trail_records(body)


# ---- reassembling the published body -----------------------------------------


def _strip_part(part: str) -> list[str]:
    """One published comment -> its logical lines (marker, footer, artifacts gone)."""
    lines = []
    for line in part.splitlines():
        if MARKER_RE.match(line):
            continue
        if line.startswith(FOOTER_SENTINEL):
            break  # footer is by contract the last block of every part
        lines.append(line)
    return lines


def reassemble(published: str) -> str:
    """Undo `pinned-comment.sh` publication: parts -> the single logical body.

    Removes per-part markers and footers, then the synthetic <details> wrapper
    split_body inserts when a block spills across a page boundary: a bare
    `</details>` closing the earlier page and a three-line continuation block
    opening the next. Leaving those in is the "re-run the splitter over its own
    continuation artifacts" failure the update lane's comment warns about
    (claude-update.yml:506) -- and here it would also make a section look like
    it changed when it did not.
    """
    parts = [_strip_part(p) for p in published.split(PART_DELIMITER)]
    parts = [p for p in parts if any(ln.strip() for ln in p)]
    if not parts:
        return ""

    merged = list(parts[0])
    for nxt in parts[1:]:
        nxt = list(nxt)
        # Drop the continuation opener: <details> / <summary><em>continued…</em></summary> / blank
        while nxt and not nxt[0].strip():
            nxt.pop(0)
        if len(nxt) >= 2 and nxt[0].strip() == "<details>" and CONTINUATION_SUMMARY in nxt[1]:
            nxt = nxt[2:]
            while nxt and not nxt[0].strip():
                nxt.pop(0)
            # ...and the synthetic close that pairs with it on the previous page.
            while merged and not merged[-1].strip():
                merged.pop()
            if merged and merged[-1].strip() == "</details>":
                merged.pop()
        merged.extend(nxt)
    return "\n".join(merged)


# ---- the three invariants ------------------------------------------------------


def _details_span(body: str, summary: str) -> tuple[int, int] | None:
    """(start, end) line span of a <details> block, inclusive of both tags."""
    lines = body.splitlines()
    for i, line in enumerate(lines):
        if summary in line:
            start = i - 1 if i > 0 and lines[i - 1].strip() == "<details>" else i
            for j in range(i + 1, len(lines)):
                if lines[j].strip() == "</details>":
                    return (start, j + 1)
            return None
    return None


def _investigation_log(body: str) -> str | None:
    span = _details_span(body, INVESTIGATION_SUMMARY)
    if span is None:
        return None
    return "\n".join(body.splitlines()[span[0]:span[1]])


def _log_bullet_count(block: str | None) -> int:
    if not block:
        return 0
    return sum(1 for name in _vp.INVESTIGATION_LOG_BULLETS if f"**{name}" in block)


def _section_with_heading(body: str, heading: str) -> str | None:
    span = _vp.find_section(body, heading)
    if span is None:
        return None
    return "\n".join(body.splitlines()[span[0]:span[1]]).rstrip()


def assess(prior: str, new: str) -> list[dict]:
    """What shrank. One entry per section that must be restored."""
    drops = []

    p_trail, n_trail = len(_vp.extract_trail_records(prior)), len(_vp.extract_trail_records(new))
    if p_trail > n_trail and _section_with_heading(prior, TRAIL_HEADING):
        drops.append({"section": TRAIL_HEADING, "kind": "h3",
                      "prior": p_trail, "new": n_trail, "unit": "trail records"})

    p_log, n_log = _investigation_log(prior), _investigation_log(new)
    p_bul, n_bul = _log_bullet_count(p_log), _log_bullet_count(n_log)
    if p_log and p_bul > n_bul:
        drops.append({"section": "Investigation log", "kind": "details",
                      "prior": p_bul, "new": n_bul, "unit": "mandatory bullets"})

    p_bal, n_bal = _section_with_heading(prior, BALANCE_HEADING), _section_with_heading(new, BALANCE_HEADING)
    if p_bal:
        # Byte length, not a parse: the balance block's shape varies by pass and
        # there is no record-level parser for it. Half is a deliberately coarse
        # threshold -- reflowed prose must not trip it, a gutted section must.
        p_len, n_len = len(p_bal), len(n_bal or "")
        if n_len < p_len // 2:
            drops.append({"section": BALANCE_HEADING, "kind": "h3",
                          "prior": p_len, "new": n_len, "unit": "bytes"})

    return drops


# ---- repair --------------------------------------------------------------------


def _insert_index_for_h3(body: str, heading: str) -> int | None:
    """Where a missing mandatory H3 belongs, from MANDATORY_H3_SECTIONS order.

    Returns a line index, or None when the order does not determine it -- in
    which case the caller must leave the body alone rather than guess.
    """
    order = list(_vp.MANDATORY_H3_SECTIONS)
    # 📊 Editorial balance is conditional and absent from the mandatory list; it
    # renders directly after the trail, so anchor it there.
    if heading == BALANCE_HEADING:
        span = _vp.find_section(body, TRAIL_HEADING)
        return span[1] if span else None
    if heading not in order:
        return None
    for later in order[order.index(heading) + 1:]:
        span = _vp.find_section(body, later)
        if span:
            return span[0]
    for earlier in reversed(order[:order.index(heading)]):
        span = _vp.find_section(body, earlier)
        if span:
            return span[1]
    return None


def restore(prior: str, new: str, drops: list[dict]) -> tuple[str, list[dict]]:
    applied = []
    for drop in drops:
        heading = drop["section"]
        if drop["kind"] == "details":
            block = _investigation_log(prior)
            span = _details_span(new, INVESTIGATION_SUMMARY)
            if block is None:
                continue
            lines = new.splitlines()
            if span is not None:
                lines[span[0]:span[1]] = block.splitlines()
            else:
                # No log at all in the new body. It renders under the Review
                # confidence table, above the count table -- anchor on the first
                # mandatory H3 and sit just above it.
                anchor = None
                for h in _vp.MANDATORY_H3_SECTIONS:
                    s = _vp.find_section(new, h)
                    if s:
                        anchor = s[0]
                        break
                if anchor is None:
                    continue
                lines[anchor:anchor] = block.splitlines() + [""]
            new = "\n".join(lines)
        else:
            block = _section_with_heading(prior, heading)
            if block is None:
                continue
            span = _vp.find_section(new, heading)
            lines = new.splitlines()
            if span is not None:
                lines[span[0]:span[1]] = block.splitlines() + [""]
            else:
                idx = _insert_index_for_h3(new, heading)
                if idx is None:
                    continue
                lines[idx:idx] = block.splitlines() + [""]
            new = "\n".join(lines)
        applied.append(drop)
    return new, applied


# ---- main ----------------------------------------------------------------------


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--prior", required=True, help="published pinned body (may be missing/empty)")
    ap.add_argument("--body", required=True, help="newly rendered body")
    ap.add_argument("--in-place", action="store_true")
    ap.add_argument("--report", help="write a JSON summary here")
    args = ap.parse_args()

    body_path = Path(args.body)
    if not body_path.is_file():
        log(f"body file not readable: {args.body}")
        return 2
    new = body_path.read_text()

    report = {"restored": [], "considered": [], "status": "noop"}
    try:
        prior_path = Path(args.prior)
        published = prior_path.read_text() if prior_path.is_file() else ""
        prior = reassemble(published) if published.strip() else ""
        if not prior:
            # First review on this PR, or the pinned comment was deleted. Both
            # are ordinary; there is simply no floor to hold.
            report["status"] = "no-prior"
        else:
            drops = assess(prior, new)
            report["considered"] = drops
            if drops:
                new, applied = restore(prior, new, drops)
                report["restored"] = applied
                report["status"] = "restored" if applied else "noop"
                for d in applied:
                    log(f"restored {d['section']}: {d['new']} -> {d['prior']} {d['unit']}")
                for d in drops:
                    if d not in applied:
                        log(f"WARNING: {d['section']} shrank ({d['new']} < {d['prior']} "
                            f"{d['unit']}) but could not be restored safely; left as rendered")
    except Exception as exc:  # noqa: BLE001 -- a repair pass must never block a publish
        log(f"WARNING: floor check failed ({type(exc).__name__}: {exc}); publishing as rendered")
        report["status"] = "error"
        report["error"] = f"{type(exc).__name__}: {exc}"

    if args.report:
        Path(args.report).write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    if args.in_place:
        if report["restored"]:
            body_path.write_text(new if new.endswith("\n") else new + "\n")
    else:
        sys.stdout.write(new if new.endswith("\n") else new + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())

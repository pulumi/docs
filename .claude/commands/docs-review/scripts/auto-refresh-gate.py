#!/usr/bin/env python3
"""auto-refresh-gate.py — deterministic gate for the stale-review auto-refresh.

Decides whether a `synchronize` push qualifies for an automatic scoped review
refresh (the `#update-review` path in claude-update.yml) without the author
having to mention `@claude`. The qualifying shape is the "I fixed what you
flagged" push: every hunk of the push diff lands on (or right next to) a line
range carried by a 🚨 Outstanding finding in the pinned review, and the push
is small. Everything else — new files, large diffs, hunks outside flagged
ranges, unparsable inputs — leaves the PR in review:stale exactly as today.

The model never decides whether to auto-fire; this script does. Fail-closed
everywhere: any ambiguity means {"fire": false}.

Inputs (all file paths):
  --pinned-body  Output of `pinned-comment.sh fetch --pr N` (the full pinned
                 review, possibly multiple pages separated by the
                 PINNED-COMMENT-DELIMITER line).
  --push-diff    Unified diff of `<last-reviewed-sha>...<head>` (GitHub
                 compare API, diff media type). Three-dot compare equals the
                 push delta on a normal push; after a force-push the
                 merge-base drifts older, the diff inflates, and the gate
                 fails closed — which is the wanted behavior.
  --pr-files     JSON array of the PR's changed file paths
                 (`gh pr view --json files --jq '[.files[].path]'`).

Output: one JSON object on stdout — {"fire": bool, "reason": "<trace>"} —
with exit 0. Exit 2 only on unusable invocations (missing file, undecodable
input); callers must treat a non-zero exit as fire=false.

Line-anchor caveat: `[L<a>-<b>]` bullet prefixes carry no file path, so on a
multi-file PR the hunk match runs against the union of ranges across files. A
cross-file coincidental overlap can fire a refresh that wasn't strictly
warranted; the consequence is one budget-capped Sonnet fix-response run that
re-verifies all outstanding findings — benign. The dangerous direction
(firing on large rewrites) is blocked by MAX_CHANGED_LINES and the
every-hunk-must-overlap rule.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path

# Budget caps. A push bigger than this is not a "trivial delta" no matter
# where its hunks land — the author should use the explicit refresh paths.
MAX_CHANGED_LINES = 80
# Findings anchor the flagged lines; authors legitimately touch the sentence
# or list item around them. Overlap is tested with this many lines of slack
# on each side of an anchor range.
SLACK_LINES = 3

# Page separator emitted by pinned-comment.sh fetch between N/M comments.
PAGE_DELIMITER = "----- PINNED-COMMENT-DELIMITER -----"

HERE = Path(__file__).resolve().parent

# validate-pinned.py owns the pinned-comment grammar (bucket sections, bullet
# prefixes). Import it rather than re-implementing; the filename is hyphenated
# so this goes through importlib, same as test_splicer.py.
_spec = importlib.util.spec_from_file_location(
    "validate_pinned", HERE / "validate-pinned.py")
validate_pinned = importlib.util.module_from_spec(_spec)
# Register before exec: validate-pinned.py defines dataclasses, and the
# dataclass machinery resolves the defining module through sys.modules.
sys.modules["validate_pinned"] = validate_pinned
_spec.loader.exec_module(validate_pinned)  # type: ignore[union-attr]

# compose-review.py owns the v3 finding-line grammar (FINDING_LINE_RE /
# parse_finding_line) and the AUTHOR_MARKER that distinguishes a v3 author
# card from a v2 body. Import by path, same pattern as validate_pinned above.
_cr_spec = importlib.util.spec_from_file_location(
    "compose_review", HERE / "compose-review.py")
compose_review = importlib.util.module_from_spec(_cr_spec)
sys.modules["compose_review"] = compose_review
_cr_spec.loader.exec_module(compose_review)  # type: ignore[union-attr]

_HUNK_RE = re.compile(r"^@@ -(\d+)(?:,(\d+))? \+(?:\d+)(?:,\d+)? @@")
_RANGE_RE = re.compile(r"^L(\d+)(?:-(\d+))?$")

# v3 author card sections whose finding rows anchor a refresh. Both block
# merge (the ❓ bucket, being author-answer, is just as fixable by a push as
# 🚨 outstanding), so a push that resolves a ❓ item must fire the gate the
# same as one that resolves a 🚨 item.
V3_ANCHOR_HEADINGS = ("🚨 Must fix or refute", "❓ Questions for you")


def result(fire: bool, reason: str) -> int:
    print(json.dumps({"fire": fire, "reason": reason}))
    return 0


def parse_anchor_ranges(pinned_body: str) -> list[tuple[int, int]] | None:
    """Extract the [L<a>-<b>] ranges of every finding that can still block merge.

    v2: every 🚨 Outstanding bullet. v3 (detected by AUTHOR_MARKER): every
    finding row in BOTH `### 🚨 Must fix or refute` and
    `### ❓ Questions for you` — the promoted ❓ bucket blocks merge exactly
    like 🚨 does, so a push that fixes a ❓ item must fire the gate too.

    Returns None when any qualifying finding lacks a parseable line-range
    anchor (legacy formats, or a v3 finding with no `[L…]` ref) — that
    finding can't be located, so the caller must fail closed. Returns [] when
    the relevant bucket(s) are empty or absent.
    """
    if compose_review.AUTHOR_MARKER in pinned_body:
        return _parse_anchor_ranges_v3(pinned_body)
    ranges: list[tuple[int, int]] = []
    for page in pinned_body.split(PAGE_DELIMITER):
        for bullet in validate_pinned.extract_bucket_bullets(page, "🚨 Outstanding"):
            prefix = validate_pinned.extract_bullet_prefix(bullet)
            if prefix is None:
                return None
            m = _RANGE_RE.match(prefix)
            if m is None:
                return None
            start = int(m.group(1))
            end = int(m.group(2)) if m.group(2) else start
            ranges.append((min(start, end), max(start, end)))
    return ranges


def _parse_anchor_ranges_v3(pinned_body: str) -> list[tuple[int, int]] | None:
    ranges: list[tuple[int, int]] = []
    for page in pinned_body.split(PAGE_DELIMITER):
        for heading in V3_ANCHOR_HEADINGS:
            span = validate_pinned.find_section(page, heading)
            if span is None:
                continue
            start, end = span
            for line in page.splitlines()[start:end]:
                parsed = compose_review.parse_finding_line(line)
                if parsed is None:
                    continue  # not a finding row (TODO prose, blank lines, …)
                ref = parsed["ref"]
                if not ref:
                    return None
                # A collapsed ref can carry several L-ranges, comma-separated
                # (frontmatter-sweep entries) — every one of them anchors a
                # legitimate refresh-eligible line.
                for token in (t.strip() for t in ref.split(",")):
                    m = _RANGE_RE.match(token)
                    if m is None:
                        return None
                    start_l = int(m.group(1))
                    end_l = int(m.group(2)) if m.group(2) else start_l
                    ranges.append((min(start_l, end_l), max(start_l, end_l)))
    return ranges


def parse_push_diff(diff_text: str):
    """Parse a unified diff into per-file old-side hunk ranges.

    Returns (hunks, changed_lines, blocker) where hunks is
    {file → [(old_start, old_end), ...]} keyed by new-side path,
    changed_lines counts +/- body lines, and blocker is a reason string when
    the diff contains something the gate must refuse (added/deleted/renamed/
    binary files), else None.
    """
    hunks: dict[str, list[tuple[int, int]]] = {}
    changed_lines = 0
    blocker: str | None = None
    current_file: str | None = None
    old_is_devnull = False

    for line in diff_text.splitlines():
        if line.startswith("diff --git "):
            current_file = None
            old_is_devnull = False
        elif line.startswith("rename from ") or line.startswith("rename to "):
            blocker = "push renames a file"
        elif line.startswith("Binary files ") or line.startswith("GIT binary patch"):
            blocker = "push touches a binary file"
        elif line.startswith("--- "):
            old_is_devnull = line[4:].strip() == "/dev/null"
        elif line.startswith("+++ "):
            target = line[4:].strip()
            if target == "/dev/null":
                blocker = "push deletes a file"
                current_file = None
            elif old_is_devnull:
                blocker = "push adds a new file"
                current_file = None
            else:
                current_file = target[2:] if target.startswith("b/") else target
        elif line.startswith("@@"):
            m = _HUNK_RE.match(line)
            if m is None or current_file is None:
                continue
            old_start = int(m.group(1))
            old_count = int(m.group(2)) if m.group(2) is not None else 1
            if old_count == 0:
                # Pure insertion: git anchors it *after* old line N. Treat as
                # adjacent to (N, N+1) so an insertion next to a flagged range
                # still matches within slack.
                span = (old_start, old_start + 1)
            else:
                span = (old_start, old_start + old_count - 1)
            hunks.setdefault(current_file, []).append(span)
        elif line.startswith("+") and not line.startswith("+++"):
            changed_lines += 1
        elif line.startswith("-") and not line.startswith("---"):
            changed_lines += 1

    return hunks, changed_lines, blocker


def overlaps(hunk: tuple[int, int], anchor: tuple[int, int]) -> bool:
    return (hunk[0] <= anchor[1] + SLACK_LINES
            and hunk[1] >= anchor[0] - SLACK_LINES)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--pinned-body", required=True)
    ap.add_argument("--push-diff", required=True)
    ap.add_argument("--pr-files", required=True)
    args = ap.parse_args()

    try:
        pinned_body = Path(args.pinned_body).read_text(encoding="utf-8")
        diff_text = Path(args.push_diff).read_text(encoding="utf-8")
        pr_files = json.loads(Path(args.pr_files).read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        print(f"auto-refresh-gate: unusable input: {exc}", file=sys.stderr)
        return 2
    if not isinstance(pr_files, list) or not all(isinstance(p, str) for p in pr_files):
        print("auto-refresh-gate: --pr-files must be a JSON array of paths",
              file=sys.stderr)
        return 2

    if not pinned_body.strip():
        return result(False, "no pinned review found")

    anchors = parse_anchor_ranges(pinned_body)
    if anchors is None:
        return result(False, "an outstanding finding has no parseable [L...] anchor")
    if not anchors:
        return result(False, "no outstanding findings to refresh against")

    if not diff_text.strip():
        return result(False, "empty push diff")

    hunks, changed_lines, blocker = parse_push_diff(diff_text)
    if blocker is not None:
        return result(False, blocker)
    if not hunks:
        return result(False, "no parseable hunks in push diff")
    if changed_lines > MAX_CHANGED_LINES:
        return result(
            False,
            f"push diff too large ({changed_lines} changed lines > {MAX_CHANGED_LINES})")

    pr_file_set = set(pr_files)
    for path, spans in hunks.items():
        if path not in pr_file_set:
            return result(False, f"push touches {path}, which is outside the PR's reviewed files")
        for span in spans:
            if not any(overlaps(span, anchor) for anchor in anchors):
                return result(
                    False,
                    f"hunk {path}:{span[0]}-{span[1]} is outside outstanding finding lines")

    n_hunks = sum(len(s) for s in hunks.values())
    return result(
        True,
        f"{n_hunks} hunk(s) across {len(hunks)} file(s), {changed_lines} changed lines, "
        f"all within outstanding finding lines (±{SLACK_LINES})")


if __name__ == "__main__":
    sys.exit(main())

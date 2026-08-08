#!/usr/bin/env python3
"""Post one-click GitHub suggestion comments for advisory Vale findings.

Reads `.style-suggestions.json` — written by the editorial pass, which
converts the advisory (non-blocker) style findings whose rewrite is a clear
improvement into concrete replacements (see the "Style suggestions" section of
the review prompt in claude-code-review.yml). Validates each entry against
the checked-out PR head and the PR diff, then posts ONE pull-request review
(event=COMMENT) whose inline comments each carry a ```suggestion block the
author can apply with a click.

Contract:
- Advisory tier only. Blocker findings render in the pinned review's 🚨
  bucket and are never suggestions — and a suggestion is dropped when it
  lands on a line that carries one, since a whole-line replacement would
  re-commit the blocking text.
- Flag-only stays true in spirit: nothing is committed here; the author
  applies or dismisses each suggestion. The meaning-preservation judgment
  the deterministic-fix gate requires (see vale-deterministic-fixes.yaml)
  is exercised twice — once by the editorial pass authoring the rewrite,
  once by the author clicking.
- The `#### Style suggestions` block in the pinned review remains the
  complete record; a suggested finding is NOT removed from it.
- Annotation owns two pieces of the pinned body, both rewritten from what
  actually posted rather than trusted: the per-bullet ✏️ marks, and the ✏️
  banner under the bucket-count table that says how many suggestions are
  waiting. Both are stripped when a run posts nothing. `--annotate-draft`
  edits the composed draft before it publishes (initial lane);
  `--annotate-pinned` PATCHes the already-published comment(s) (re-entrant
  lane, which renders and upserts inside the model step).
- Idempotent per run: prior suggestion comments (MARKER match) are deleted
  before posting — same delete-and-repost semantics as TRIAGE_PROSE. When the
  set this run would post is identical to what is already posted, the whole
  delete-and-repost is skipped: the existing buttons stay live, subscribers
  are not re-notified, and no further (undeletable) review event is stranded
  in the timeline. Annotation still runs, because the re-entrant lane
  re-renders the body from scratch and has to be re-marked either way.
- Never fails the workflow: any validation or API problem logs a warning
  and exits 0. Entries that fail validation are dropped individually.
- The batch endpoint is ATOMIC (verified 2026-08-03: one unresolvable
  anchor returns `422 Line could not be resolved` and creates nothing), so
  local validation is load-bearing — a single bad entry would otherwise
  cost every suggestion in the run. On a batch failure the script retries
  one comment at a time and marks only what landed.

Per-entry validation (anti-hallucination — the model wrote the JSON):
- `file`, `line`, `original`, `replacement` present; replacement differs.
- `line` is a PR-ADDED line (reuses added_lines_per_file from
  vale-findings-filter.py over the PR patch) — GitHub suggestions can only
  anchor to diff lines, and advisory findings are diff-intersected upstream,
  so a miss here means the entry drifted.
- `original` occurs verbatim on that exact line of the checked-out file;
  the suggestion body is the full line with the first occurrence swapped.
- Capped at MAX_SUGGESTIONS total; excess entries are dropped with a log.

Input schema (.style-suggestions.json):
    [
      {"file": "content/docs/foo.md", "line": 42,
       "original": "utilize", "replacement": "use",
       "category": "wordiness", "note": "shorter and identical in meaning"},
      ...
    ]

Usage:
    post-style-suggestions.py --pr N [--repo owner/repo]
        [--in .style-suggestions.json] [--patch-file diff.patch] [--dry-run]
        [--annotate-draft .review-draft.md | --annotate-pinned]

--patch-file reads the PR diff from a file instead of `gh pr diff` (tests).
--dry-run validates and prints the review payload without calling gh.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent

# Reuse the diff parser that already defines "PR-added line" for Vale
# findings, so both ends of the pipeline agree on anchorability.
_spec = importlib.util.spec_from_file_location(
    "vale_findings_filter", HERE / "vale-findings-filter.py")
_vff = importlib.util.module_from_spec(_spec)
sys.modules["vale_findings_filter"] = _vff
_spec.loader.exec_module(_vff)  # type: ignore[union-attr]

MARKER = "<!-- CLAUDE_STYLE_SUGGESTION -->"
MAX_SUGGESTIONS = 10
# Banner announcing the posted suggestions, inserted under the bucket-count
# table. Without it the only evidence a one-click fix exists is a ✏️ in the
# LAST section of a ~16 KB comment, below everything the author actually has
# to fix — an author who clears 🚨 and stops reading never learns the buttons
# are there. Column-0 ✏️ is the strip key (bullet marks are always mid-line),
# so the line is rewritten from the posted set on every run rather than
# trusted, exactly like the marks themselves.
BANNER_PREFIX = "✏️"
# Resolve the repo from the environment, never a hardcoded upstream name: the
# same script runs on the CamSoper/pulumi.docs test fork, where a hardcoded
# `pulumi/docs` makes every write 403 ("Resource not accessible by
# integration") because the fork's GITHUB_TOKEN is scoped to the fork. The
# workflow also passes --repo explicitly; this default just keeps a bare
# invocation honest.
DEFAULT_REPO = os.environ.get("GITHUB_REPOSITORY") or "pulumi/docs"

# Deliberately ONE line. A submitted review cannot be deleted (the API deletes
# only *pending* reviews) and a COMMENT review cannot be dismissed, so while
# cleanup removes this review's inline comments, the review event itself is
# permanent -- every repost leaves one behind in the PR timeline forever. The
# pinned comment's ✏️ banner carries the real explanation and the batching
# hint; this body only has to say what the comments are. `event: COMMENT`
# requires a non-empty body, so it cannot be dropped entirely.
REVIEW_BODY = (
    f"{MARKER}\n"
    "🧹 Optional style suggestions from the pre-merge review — apply or dismiss; "
    "none of them block.\n\n"
    "---\n"
    "_Generated by [Claude Code](https://claude.ai/code)_"
)

# Matches the mark plus the whitespace around it, so removing one leaves a
# single separator instead of a double space.
_MARK_RE = re.compile(r"\s*\u270f\ufe0f\s*")

# Appended to the pinned review's style bullets that have a posted suggestion.
# Written only for entries that actually posted, so the marker can't promise a
# button that isn't there.
SUGGESTION_MARK = " ✏️"


def blocker_lines(vale_findings: list | None) -> set[tuple[str, int]]:
    """(file, line) pairs carrying a blocker-tier Vale finding."""
    if not isinstance(vale_findings, list):
        return set()
    return {
        (str(f.get("file") or ""), int(f.get("line") or 0))
        for f in vale_findings
        if isinstance(f, dict) and f.get("blocker")
    }


def validate_entries(
    entries: list,
    added_lines: dict[str, set[int]],
    repo_root: Path,
    blocked: set[tuple[str, int]] | None = None,
) -> tuple[list[dict], list[str]]:
    """Return (valid suggestion dicts, human-readable drop reasons).

    Valid dicts gain a `new_line` key: the full replacement line for the
    ```suggestion block.

    `blocked` holds (file, line) pairs that carry a blocker-tier finding.
    Suggestions on those lines are dropped: a suggestion is a whole-line
    replacement, so accepting one on a line that also contains a blocker
    would re-commit the blocking text verbatim (observed on fork PR #227,
    where the 'Simply' suggestion's replacement line still read "Pulumi
    Service" and "click"). Nothing is lost -- the blocker stays flagged in
    🚨 and the author fixes the line there.
    """
    valid: list[dict] = []
    dropped: list[str] = []
    seen: set[tuple[str, int]] = set()
    file_cache: dict[str, list[str] | None] = {}
    blocked = blocked or set()

    if not isinstance(entries, list):
        return [], ["input is not a JSON array"]

    for i, e in enumerate(entries):
        tag = f"entry {i}"
        if not isinstance(e, dict):
            dropped.append(f"{tag}: not an object")
            continue
        fname = e.get("file")
        line = e.get("line")
        original = e.get("original")
        replacement = e.get("replacement")
        if not (isinstance(fname, str) and isinstance(line, int)
                and isinstance(original, str) and isinstance(replacement, str)):
            dropped.append(f"{tag}: missing/mistyped file, line, original, or replacement")
            continue
        tag = f"{fname}:{line}"
        if not original or original == replacement:
            dropped.append(f"{tag}: empty original or no-op replacement")
            continue
        if (fname, line) in seen:
            dropped.append(f"{tag}: duplicate anchor")
            continue
        if line not in added_lines.get(fname, set()):
            dropped.append(f"{tag}: not a PR-added line (suggestion can't anchor)")
            continue
        if (fname, line) in blocked:
            dropped.append(f"{tag}: line carries a blocker finding "
                           "(a whole-line suggestion would re-commit the blocking text)")
            continue
        if fname not in file_cache:
            try:
                file_cache[fname] = (repo_root / fname).read_text(
                    encoding="utf-8").splitlines()
            except (OSError, UnicodeDecodeError):
                file_cache[fname] = None
        lines = file_cache[fname]
        if lines is None:
            dropped.append(f"{tag}: file unreadable in checkout")
            continue
        if line < 1 or line > len(lines):
            dropped.append(f"{tag}: line out of range ({len(lines)} lines)")
            continue
        content = lines[line - 1]
        if original not in content:
            dropped.append(f"{tag}: original text not found on that line")
            continue
        new_line = content.replace(original, replacement, 1)
        if new_line == content:
            dropped.append(f"{tag}: replacement produced no change")
            continue
        seen.add((fname, line))
        valid.append({**e, "new_line": new_line})

    if len(valid) > MAX_SUGGESTIONS:
        for e in valid[MAX_SUGGESTIONS:]:
            dropped.append(f"{e['file']}:{e['line']}: over the {MAX_SUGGESTIONS}-suggestion cap")
        valid = valid[:MAX_SUGGESTIONS]
    return valid, dropped


def comment_body(e: dict) -> str:
    cat = str(e.get("category") or "style")
    note = str(e.get("note") or "").strip()
    note_part = f" — {note}" if note else ""
    return (
        f"{MARKER}\n"
        f"[style] _{cat}_{note_part}\n"
        "```suggestion\n"
        f"{e['new_line']}\n"
        "```"
    )


def build_review_payload(valid: list[dict]) -> dict:
    return {
        "event": "COMMENT",
        "body": REVIEW_BODY,
        "comments": [
            {"path": e["file"], "line": e["line"], "side": "RIGHT",
             "body": comment_body(e)}
            for e in valid
        ],
    }


def post_individually(repo: str, pr: str, head_sha: str, valid: list[dict]) -> list[dict]:
    """Fall back to one review comment per suggestion; return those that landed.

    The batch endpoint (POST /pulls/{n}/reviews with comments[]) is ATOMIC —
    verified 2026-08-03: a single unresolvable anchor returns
    `422 Line could not be resolved` and creates nothing. So one bad entry
    would otherwise cost every suggestion in the run. Posting individually
    degrades that to losing just the bad one.

    Used only after the batch attempt fails, so the happy path still produces
    a single tidy review rather than N loose comments.
    """
    landed: list[dict] = []
    for e in valid:
        proc = gh_api([
            "-X", "POST", f"repos/{repo}/pulls/{pr}/comments",
            "-f", f"body={comment_body(e)}",
            "-f", f"commit_id={head_sha}",
            "-f", f"path={e['file']}",
            "-F", f"line={e['line']}",
            "-f", "side=RIGHT",
        ])
        if proc.returncode == 0:
            landed.append(e)
        else:
            print(f"post-style-suggestions: {e['file']}:{e['line']} rejected: "
                  f"{proc.stderr.strip()[:120]}", file=sys.stderr)
    return landed


def gh_api(args: list[str], input_json: dict | None = None) -> subprocess.CompletedProcess:
    cmd = ["gh", "api"] + args
    return subprocess.run(
        cmd,
        input=json.dumps(input_json) if input_json is not None else None,
        capture_output=True, text=True,
    )


def fetch_prior_suggestions(repo: str, pr: str) -> list[dict] | None:
    """Return this script's existing review comments, or None if unreadable."""
    proc = gh_api([
        f"repos/{repo}/pulls/{pr}/comments", "--paginate",
        "--jq", f'.[] | select(.body | startswith("{MARKER}"))'
                ' | {id: .id, path: .path, line: .line, body: .body}',
    ])
    if proc.returncode != 0:
        print(f"post-style-suggestions: could not list prior comments: {proc.stderr.strip()}",
              file=sys.stderr)
        return None
    out: list[dict] = []
    for raw in proc.stdout.splitlines():
        if raw.strip():
            try:
                out.append(json.loads(raw))
            except json.JSONDecodeError:
                continue
    return out


_SUGGESTION_BLOCK_RE = re.compile(r"```suggestion\n(.*?)\n```", re.S)


def _replacement_of(body: str) -> str:
    """The proposed line inside a suggestion comment, or the whole body.

    Falls back to the full body when there is no suggestion block, so two
    malformed comments can't collide on an empty string.
    """
    text = (body or "").replace("\r\n", "\n")
    m = _SUGGESTION_BLOCK_RE.search(text)
    return m.group(1) if m else text.strip()


def suggestion_key(path: str, line, body: str) -> tuple[str, int, str]:
    """Identity of a posted suggestion, for the unchanged-set comparison.

    Keyed on the REPLACEMENT LINE, not the whole body. The body's first line
    carries `note` -- a free-text reason the editorial pass rewrites every run
    ("'utilize' means 'use'" one run, "utilize -> use" the next, observed
    across three runs on fork #232 while the suggestion blocks stayed
    byte-identical). Keying on the body meant the desired set never matched the
    posted one, so the unchanged-set short-circuit below could never fire and
    every refresh still deleted and re-posted live buttons.

    The trade-off is deliberate: when only the note changed we keep the
    previously posted wording rather than churn the comment for a cosmetic
    difference. The replacement is what the author actually applies.

    Body is newline-normalized because GitHub stores `\r\n`. An outdated
    comment reports `line: null`, which can never equal a desired anchor -- so
    a suggestion whose line moved is correctly treated as changed.
    """
    return (path or "", int(line) if isinstance(line, int) else -1,
            _replacement_of(body))


def delete_comments(repo: str, ids: list) -> None:
    for cid in ids:
        d = gh_api(["-X", "DELETE", f"repos/{repo}/pulls/comments/{cid}"])
        if d.returncode != 0:
            print(f"post-style-suggestions: could not delete comment {cid}: {d.stderr.strip()}",
                  file=sys.stderr)


def _banner_text(n: int, files_url: str) -> str:
    link = f"[Files changed]({files_url})" if files_url else "**Files changed**"
    if n == 1:
        return (f"{BANNER_PREFIX} **1 one-click style suggestion** is posted inline — "
                f"apply it from the {link} tab.")
    return (f"{BANNER_PREFIX} **{n} one-click style suggestions** are posted inline — "
            f"apply them from the {link} tab, individually or with "
            f"**Add suggestion to batch**.")


# The `#### Style suggestions` heading, plus the pre-rename spelling so a body
# composed before the rename still reconciles. Mirrors validate-pinned.py.
STYLE_HEADINGS = ("#### Style suggestions", "#### Style findings")


def _caption_text(files_url: str) -> str:
    """The canonical caption under the style heading.

    Must stay byte-identical to what `compose-review.py` emits, so that
    reconciling an initial-lane body is a no-op rather than a churn edit.
    `test_caption_matches_composer` pins the two together.
    """
    link = f"[Files changed]({files_url})" if files_url else "Files changed"
    return ("*Optional polish from pattern-based linting — never blocking, not counted above. "
            "Take the ones that read better and ignore the rest. "
            f"✏️ marks one you can apply from the {link} tab — use **Add suggestion to batch** "
            "on each, then **Commit suggestions** to take several in a single commit.*")


def _reconcile_caption(lines: list[str], files_url: str) -> bool:
    """Rewrite the italic caption under the style heading.

    Authoritative, for the same reason the marks and the banner are. The
    initial lane gets this caption from `compose-review.py` and it is correct;
    the re-entrant lane renders the body freehand and was observed paraphrasing
    it away — fork PR #231 refreshed to a caption that had dropped the
    "✏️ marks one you can apply" legend entirely, leaving six marks on the page
    with nothing explaining them. Nothing gated it: `style-render-mode` only
    checks that the block is not collapsed behind a <details>.

    A caption is only rewritten, never invented: with no style heading there is
    no block to caption, and we leave the body alone.
    """
    head = next((i for i, ln in enumerate(lines) if ln.strip() in STYLE_HEADINGS), None)
    if head is None:
        return False
    j = head + 1
    while j < len(lines) and not lines[j].strip():
        j += 1
    if j >= len(lines):
        return False
    want = _caption_text(files_url)
    cur = lines[j].strip()
    # The caption is the italic one-liner between the heading and the first
    # `##### <path>` group. Anything else there means the model omitted it.
    if cur.startswith("*") and cur.endswith("*") and not cur.startswith("**"):
        if lines[j] == want:
            return False
        lines[j] = want
        return True
    lines.insert(j, want)
    lines.insert(j + 1, "")
    return True


def _reconcile_banner(lines: list[str], n: int, files_url: str) -> bool:
    """Rewrite the suggestion banner under the bucket-count table.

    Authoritative like the marks: any existing banner is removed first, and a
    fresh one is inserted only when something actually posted. That keeps the
    re-entrant lane honest — a refresh that converts nothing must not leave
    last run's "4 suggestions are posted inline" standing over zero buttons.
    """
    changed = False
    for i in range(len(lines) - 1, -1, -1):
        if lines[i].startswith(BANNER_PREFIX):
            del lines[i]
            # The banner is inserted with a blank line above it; take that
            # back too so repeated runs don't grow a gap under the table.
            if i > 0 and not lines[i - 1].strip():
                del lines[i - 1]
            changed = True
    if n <= 0:
        return changed
    # The count row: four bold integers. Matching the values row rather than
    # the header keeps this independent of the header's emoji labels.
    row_re = re.compile(r"^\|\s*\*\*\d+\*\*\s*\|")
    for i, line in enumerate(lines):
        if row_re.match(line):
            lines.insert(i + 1, "")
            lines.insert(i + 2, _banner_text(n, files_url))
            return True
    print("post-style-suggestions: no bucket-count row found; banner not inserted.",
          file=sys.stderr)
    return changed


def annotate_text(text: str, posted: list[dict], files_url: str = "") -> tuple[str, int]:
    """Reconcile one review body against what actually posted.

    AUTHORITATIVE, not additive: every existing mark and banner is stripped
    first, then re-applied only from the set the GitHub API accepted. The
    editorial pass has been observed adding its own marks (fork PR #229, where
    it wrote four mid-line ✏️ of its own) — harmless when its guesses happen to
    match, but the whole point of the mark is that it promises a button exists.
    A mark the model wrote for an entry that was later dropped (blocker line,
    anchor mismatch, cap) would be a lie, so the workflow overwrites rather
    than trusts.

    Returns `(body, marks_present)`. Safe to run on ONE PART of a split review:
    a part with no count row simply gets no banner, and a part with no style
    bullets gets no marks.

    Stripping is UNCONDITIONAL; only re-marking consults the `##### <path>`
    heading that binds a bullet to a file. The two are deliberately split.
    When a style block straddles a page boundary the bullets on the later page
    have no heading to attribute them, and gating the strip on that heading
    left last run's ✏️ standing on a page whose suggestion comments had just
    been deleted -- a phantom button, the exact failure this function exists to
    prevent. A mark we cannot re-earn still comes off, so the residual
    degradation is a missing button, never a phantom one.

    (The heading is an H5 rather than a bold line specifically so
    validate-pinned's bucket-bullet regex doesn't count it as a finding.)
    """
    lines = text.splitlines()
    want = {(str(e.get("file")), int(e.get("line"))) for e in posted}
    file_re = re.compile(r"^#{5}\s+(\S+\.\w+)")
    bullet_re = re.compile(r"^(\s*- \*\*line (\d+):\*\*)(.*)$")
    current: str | None = None
    marked = 0
    for i, line in enumerate(lines):
        fm = file_re.match(line)
        if fm:
            current = fm.group(1)
            continue
        bm = bullet_re.match(line)
        if not bm:
            continue
        head, body = bm.group(1), bm.group(3)
        # Strip any mark, wherever it sits -- the editorial pass has been seen
        # placing its own. Collapse only the gap the removal leaves, rather
        # than normalizing every run of whitespace in the bullet: Vale messages
        # quote author text and may legitimately carry a double space.
        clean_body = _MARK_RE.sub(" ", body).rstrip()
        rebuilt = head + clean_body
        if current is not None and (current, int(bm.group(2))) in want:
            rebuilt += SUGGESTION_MARK
            marked += 1
        if rebuilt != line:
            lines[i] = rebuilt
    _reconcile_caption(lines, files_url)
    _reconcile_banner(lines, len(want), files_url)
    out = "\n".join(lines)
    # Preserve the input's trailing-newline state. GitHub stores comment bodies
    # without one, so appending it unconditionally made the re-entrant lane
    # PATCH every part on its first pass purely to add a character.
    if text.endswith("\n"):
        out += "\n"
    return out, marked


def annotate_draft(draft_path: Path, posted: list[dict], files_url: str = "") -> int:
    """annotate_text over the composed draft file, in place (initial lane)."""
    try:
        original = draft_path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return 0
    body, marked = annotate_text(original, posted, files_url)
    if body != original:
        draft_path.write_text(body, encoding="utf-8")
    return marked


def annotate_pinned(repo: str, pr: str, posted: list[dict], files_url: str = "") -> int:
    """annotate_text over the ALREADY-PUBLISHED pinned comment(s).

    The re-entrant lane has no composed draft to intercept: the model renders
    the body and upserts it itself, so the only copy of the published review is
    on GitHub. Each `<!-- CLAUDE_REVIEW N/M -->` comment is fetched, reconciled,
    and PATCHed back individually.

    Patching parts in place rather than fetch → concatenate → re-upsert is
    deliberate. Re-upserting would re-run the splitter over a body that already
    carries the splitter's own artifacts (the synthetic `</details>` /
    continuation `<details>` pairs it inserts at page boundaries), which
    compounds on every refresh. Editing each part touches only the lines the
    marks and banner live on.
    """
    proc = gh_api([f"repos/{repo}/issues/{pr}/comments", "--paginate",
                   "--jq", '.[] | select(.body | startswith("<!-- CLAUDE_REVIEW "))'
                           ' | {id: .id, body: .body}'])
    if proc.returncode != 0:
        print(f"post-style-suggestions: could not list pinned comments: "
              f"{proc.stderr.strip()[:160]}", file=sys.stderr)
        return 0
    marked = 0
    patched = 0
    for raw in proc.stdout.splitlines():
        if not raw.strip():
            continue
        try:
            comment = json.loads(raw)
        except json.JSONDecodeError:
            continue
        body, n = annotate_text(comment["body"], posted, files_url)
        marked += n
        # GitHub normalizes bodies to \r\n; compare on the same footing so an
        # unchanged part isn't PATCHed (and re-notified) on every refresh.
        if body.replace("\r\n", "\n") == comment["body"].replace("\r\n", "\n"):
            continue
        res = gh_api(["-X", "PATCH", f"repos/{repo}/issues/comments/{comment['id']}",
                      "--input", "-"], input_json={"body": body})
        if res.returncode != 0:
            print(f"post-style-suggestions: PATCH of comment {comment['id']} failed: "
                  f"{res.stderr.strip()[:160]}", file=sys.stderr)
        else:
            patched += 1
    print(f"post-style-suggestions: annotated {patched} pinned comment part(s).",
          file=sys.stderr)
    return marked


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pr", required=True)
    ap.add_argument("--repo", default=DEFAULT_REPO)
    ap.add_argument("--in", dest="infile", default=".style-suggestions.json")
    ap.add_argument("--repo-root", default=".")
    ap.add_argument("--vale-findings", default=".vale-findings.json",
                    help="Path to the filter's output; used to skip suggestions on lines "
                         "that carry a blocker-tier finding.")
    ap.add_argument("--patch-file", help="Read the PR diff from a file instead of `gh pr diff` (tests).")
    ap.add_argument("--annotate-draft",
                    help="Path to .review-draft.md. After posting, marks the style bullets "
                         "that got a suggestion so the pinned comment can point at them. "
                         "Must run BEFORE the pinned upsert. (Initial-review lane.)")
    ap.add_argument("--annotate-pinned", action="store_true",
                    help="Annotate the ALREADY-PUBLISHED pinned comment(s) in place instead "
                         "of a draft file. For the re-entrant lane, where the model renders "
                         "and upserts the body itself and no draft is available to intercept.")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    # A missing or unreadable sidecar is treated as "no suggestions this run",
    # NOT as "skip the run": delete-and-repost is the documented semantics, so
    # the re-entrant lane still has to clear last run's comments and strip the
    # marks they justified. Bailing early would leave a refreshed review
    # advertising buttons for findings it no longer reports.
    path = Path(args.infile)
    entries: list = []
    if not path.is_file():
        print("post-style-suggestions: no suggestions file; treating as none.", file=sys.stderr)
    else:
        try:
            entries = json.loads(path.read_text(encoding="utf-8") or "[]")
        except (json.JSONDecodeError, UnicodeDecodeError) as exc:
            print(f"post-style-suggestions: unreadable {path}: {exc}", file=sys.stderr)

    if not entries:
        patch = ""
    elif args.patch_file:
        patch = Path(args.patch_file).read_text(encoding="utf-8")
    else:
        proc = subprocess.run(
            ["gh", "pr", "diff", args.pr, "--repo", args.repo, "--patch"],
            capture_output=True, text=True)
        if proc.returncode != 0:
            print(f"post-style-suggestions: gh pr diff failed: {proc.stderr.strip()}",
                  file=sys.stderr)
            return 0
        patch = proc.stdout
    added = _vff.added_lines_per_file(patch)

    try:
        vale = json.loads(Path(args.vale_findings).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError, UnicodeDecodeError):
        vale = None
    valid, dropped = validate_entries(
        entries, added, Path(args.repo_root), blocker_lines(vale))
    for reason in dropped:
        print(f"post-style-suggestions: dropped {reason}", file=sys.stderr)
    print(f"post-style-suggestions: {len(valid)} valid suggestion(s), {len(dropped)} dropped.",
          file=sys.stderr)

    if args.dry_run:
        print(json.dumps(build_review_payload(valid), indent=2))
        return 0

    # Even with zero valid suggestions, clear stale ones from a prior run —
    # a re-review that fixed everything should leave no orphaned comments.
    prior = fetch_prior_suggestions(args.repo, args.pr)

    # Short-circuit when this run would re-post exactly what is already there.
    # Refreshes are common (an auto-refresh fires on any push touching an
    # outstanding finding) and the style set usually does not move, so the
    # default path was: delete N comments, create a new review, notify every
    # subscriber, and strand one more undeletable review event in the timeline
    # -- to arrive at the state we were already in. Skipping keeps the existing
    # buttons live and costs one API call. Annotation still runs below: the
    # re-entrant lane re-renders the body from scratch each time, so the marks
    # have to be re-applied even when the suggestions themselves never changed.
    posted: list[dict] = []
    if prior is not None:
        have = {suggestion_key(c.get("path"), c.get("line"), c.get("body")) for c in prior}
        wanted = {suggestion_key(e["file"], e["line"], comment_body(e)) for e in valid}
        if have == wanted:
            if valid:
                print(f"post-style-suggestions: {len(valid)} suggestion(s) already posted "
                      "and unchanged; leaving them in place.", file=sys.stderr)
            posted = valid
            valid = []          # nothing to post
            prior = []          # nothing to delete
    if prior:
        delete_comments(args.repo, [c["id"] for c in prior])
    elif prior is None:
        # Listing failed, so we cannot prove what is out there. Fall back to
        # the old unconditional delete rather than risk duplicate comments.
        stale = gh_api([f"repos/{args.repo}/pulls/{args.pr}/comments", "--paginate",
                        "--jq", f'.[] | select(.body | startswith("{MARKER}")) | .id'])
        if stale.returncode == 0:
            delete_comments(args.repo, stale.stdout.split())

    if valid:
        payload = build_review_payload(valid)
        proc = gh_api(
            ["-X", "POST", f"repos/{args.repo}/pulls/{args.pr}/reviews", "--input", "-"],
            input_json=payload,
        )
        if proc.returncode == 0:
            posted = valid
        else:
            # The batch endpoint is atomic, so this cost ALL of them. Retry one
            # at a time so a single bad anchor doesn't sink the rest.
            print(f"post-style-suggestions: batch review POST failed "
                  f"({proc.stderr.strip()[:160]}); retrying one comment at a time.",
                  file=sys.stderr)
            head = gh_api([f"repos/{args.repo}/pulls/{args.pr}", "--jq", ".head.sha"])
            if head.returncode != 0:
                print("post-style-suggestions: could not resolve head SHA; giving up.",
                      file=sys.stderr)
            else:
                posted = post_individually(args.repo, args.pr, head.stdout.strip(), valid)
    print(f"post-style-suggestions: posted {len(posted)} suggestion(s).", file=sys.stderr)
    # Annotate on EVERY path, including the zero-posted one. On the re-entrant
    # lane the draft is last run's published body, so a refresh that converts
    # nothing has to actively strip the stale marks and banner — returning
    # early would leave the review advertising buttons that were just deleted.
    files_url = f"https://github.com/{args.repo}/pull/{args.pr}/files"
    n = None
    if args.annotate_draft:
        n = annotate_draft(Path(args.annotate_draft), posted, files_url)
    elif args.annotate_pinned:
        n = annotate_pinned(args.repo, args.pr, posted, files_url)
    if n is not None:
        print(f"post-style-suggestions: {n} style bullet(s) carry the ✏️ mark.",
              file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())

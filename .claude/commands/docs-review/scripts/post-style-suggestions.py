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

Blocking-fix mode (`--fixes-from-author-card <v3 author card>`): the same
validate-and-post machinery, pointed at the other end of the severity scale.
Instead of a model-written sidecar, entries are DERIVED from the card's
🚨 Fix-or-disagree rows: a row anchored to one line whose `#### F<n> · Do
this` block quotes that line (`**Line (verbatim):**`) and carries exactly one
single-line fenced replacement becomes a one-click suggestion that splices
the fence into the quoted span. Readers asked for exactly this (inline,
applyable fixes for what blocks them) while asking for the optional nags to
leave the Files view (2026-09-25). It posts under its own marker, so the two
sets are managed independently, and never annotates the card. ❓ rows are
never converted: their fences are proposals that wait on the author's
answer.
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

FIX_MARKER = "<!-- CLAUDE_FIX_SUGGESTION -->"
FIX_REVIEW_BODY = (
    f"{FIX_MARKER}\n"
    "🔧 One-click fixes for findings that block merge — each matches a **Do this** "
    "block on the author card. Commit one and the card picks up the fix; you can "
    "still disagree on the card instead.\n\n"
    "---\n"
    "_Generated by [Claude Code](https://claude.ai/code)_"
)


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
    if e.get("kind") == "fix":
        ids = ", ".join(f"**{i}**" for i in e["ids"])
        verb = "blocks" if len(e["ids"]) == 1 else "block"
        why = " ".join(w for w in e.get("whys", []) if w).strip()
        why_part = f" — {why}" if why else ""
        return (
            f"{FIX_MARKER}\n"
            f"{ids} {verb} merge{why_part}\n"
            "```suggestion\n"
            f"{e['new_line']}\n"
            "```"
        )
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


def build_review_payload(valid: list[dict], body: str = REVIEW_BODY) -> dict:
    return {
        "event": "COMMENT",
        "body": body,
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


def fetch_prior_suggestions(repo: str, pr: str, marker: str = MARKER) -> list[dict] | None:
    """Return this script's existing review comments, or None if unreadable."""
    proc = gh_api([
        f"repos/{repo}/pulls/{pr}/comments", "--paginate",
        "--jq", f'.[] | select(.body | startswith("{marker}"))'
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


# The v3 author card marker. Its style block also carries the review's own
# `[nit]` bullets (compose-review.NIT_TAG), so its caption names both sources.
V3_AUTHOR_MARKER = "<!-- CLAUDE_REVIEW_AUTHOR -->"


def _caption_text(files_url: str, nits: bool = False, legend: bool = True) -> str:
    """The canonical caption under the style heading.

    With `legend` (the default) it must stay byte-identical to what
    `compose-review.py` emits, so that reconciling an initial-lane body with
    suggestions posted is a no-op rather than a churn edit.
    `test_caption_matches_composer` pins the two together — for BOTH variants:
    pinning only the v2 one let the v3 caption be silently reverted here on
    every published card, since this runs on the author draft before publish.

    Without `legend` the ✏️ sentence is gone: annotate_text drops it when no
    bullet carries a mark, since a legend for marks that aren't on the page
    only sends the reader to the Files tab for nothing (and with
    REVIEW_STYLE_INLINE off, none ever are).
    """
    link = f"[Files changed]({files_url})" if files_url else "Files changed"
    source = ("pattern-based linting and the review's own read"
              if nits else "pattern-based linting")
    tail = (f" ✏️ marks one you can apply from the {link} tab — use **Add suggestion to batch** "
            "on each, then **Commit suggestions** to take several in a single commit."
            if legend else "")
    return (f"*Optional polish from {source} — never blocking, not counted above. "
            f"Take the ones that read better and ignore the rest.{tail}*")


def _reconcile_caption(lines: list[str], files_url: str, nits: bool = False,
                       legend: bool = True) -> bool:
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
    want = _caption_text(files_url, nits, legend)
    cur = lines[j].strip()
    # Positional, not shape-based: the slot between the heading and the first
    # `##### <path>` group holds the caption and nothing else, so whatever sits
    # there gets replaced regardless of how the model wrapped it. Sniffing for
    # single asterisks missed a bold-wrapped caption and inserted a second one
    # above it — and a column-0 `**bold**` line is exactly the shape the render
    # contract forbids, since `extract_bucket_bullets` counts it as a finding.
    if not cur.startswith("#####") and not cur.startswith("- "):
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
    _reconcile_caption(lines, files_url, nits=V3_AUTHOR_MARKER in text, legend=marked > 0)
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


def live_posted(repo: str, pr: str) -> list[dict] | None:
    """Currently-posted suggestions, shaped for `annotate_text`.

    Returns None when the listing FAILED, which is not the same as an empty
    list. Annotating from a wrongly-empty set would strip the marks and zero
    the banner while the real comments stayed live — the same unknown-versus-
    confirmed-empty conflation this module fixes for the sidecar, so it must
    not be reintroduced here.

    Outdated comments report `line: null` and are dropped: there is no line to
    mark, and `annotate_text` coerces the line to `int`.
    """
    prior = fetch_prior_suggestions(repo, pr)
    if prior is None:
        return None
    return [{"file": c.get("path"), "line": c.get("line")}
            for c in prior if isinstance(c.get("line"), int)]


def _annotate(args, posted: list[dict]) -> None:
    """Reconcile marks and banner against `posted`, on whichever lane asked."""
    files_url = f"https://github.com/{args.repo}/pull/{args.pr}/files"
    n = None
    if args.annotate_draft:
        n = annotate_draft(Path(args.annotate_draft), posted, files_url)
    elif args.annotate_pinned:
        n = annotate_pinned(args.repo, args.pr, posted, files_url)
    if n is not None:
        print(f"post-style-suggestions: {n} style bullet(s) carry the ✏️ mark.",
              file=sys.stderr)


def sync_posted(repo: str, pr: str, valid: list[dict], marker: str,
                review_body: str) -> list[dict]:
    """Make the set of `marker` comments on the PR equal `valid`; return
    what is live afterwards. Shared by the style and blocking-fix modes.

    Even with zero valid suggestions, stale ones from a prior run are cleared
    — a re-review that fixed everything should leave no orphaned comments.

    Short-circuits when this run would re-post what is already there.
    Refreshes are common (an auto-refresh fires on any push touching an
    outstanding finding) and the set usually does not move, so the default
    path was: delete N comments, create a new review, notify every
    subscriber, and strand one more undeletable review event in the timeline
    -- to arrive at the state we were already in. The same holds when the
    wanted set is a SUBSET of the posted one (a fix landed, so its
    suggestion goes): deleting just the extras keeps the survivors' buttons
    live without a new review event. Only a genuinely new or changed
    suggestion costs a repost.
    """
    prior = fetch_prior_suggestions(repo, pr, marker)
    posted: list[dict] = []
    if prior is not None:
        by_key: dict[tuple, list] = {}
        for c in prior:
            by_key.setdefault(suggestion_key(c.get("path"), c.get("line"), c.get("body")), []).append(c)
        wanted = {suggestion_key(e["file"], e["line"], comment_body(e)) for e in valid}
        if wanted <= set(by_key):
            extras = [c["id"] for k, cs in by_key.items() for c in (cs if k not in wanted else cs[1:])]
            if valid:
                print(f"post-style-suggestions: {len(valid)} suggestion(s) already posted "
                      "and unchanged; leaving them in place.", file=sys.stderr)
            if extras:
                print(f"post-style-suggestions: removing {len(extras)} suggestion(s) no "
                      "longer wanted, without a repost.", file=sys.stderr)
            posted = valid
            valid = []          # nothing to post
            prior = [{"id": cid} for cid in extras]
    if prior:
        delete_comments(repo, [c["id"] for c in prior])
    elif prior is None:
        # Listing failed, so we cannot prove what is out there. Fall back to
        # the old unconditional delete rather than risk duplicate comments.
        stale = gh_api([f"repos/{repo}/pulls/{pr}/comments", "--paginate",
                        "--jq", f'.[] | select(.body | startswith("{marker}")) | .id'])
        if stale.returncode == 0:
            delete_comments(repo, stale.stdout.split())

    if valid:
        payload = build_review_payload(valid, review_body)
        proc = gh_api(
            ["-X", "POST", f"repos/{repo}/pulls/{pr}/reviews", "--input", "-"],
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
            head = gh_api([f"repos/{repo}/pulls/{pr}", "--jq", ".head.sha"])
            if head.returncode != 0:
                print("post-style-suggestions: could not resolve head SHA; giving up.",
                      file=sys.stderr)
            else:
                posted = post_individually(repo, pr, head.stdout.strip(), valid)
    return posted


_FIX_SECTION_HEADING = "### 🚨 Fix or disagree"
_DO_THIS_RE = re.compile(r"^#### (F\d+) · Do this\s*$")
_LINE_LABEL_RE = re.compile(r"^(?:-\s+)?\*\*Line \(verbatim\):\*\*\s*(?P<q>.+?)\s*$")
_WHY_LABEL_RE = re.compile(r"^(?:-\s+)?\*\*Why:\*\*\s*(?P<w>.+?)\s*$")
_REF_RE = re.compile(r"^L(\d+)(?:-(\d+))?$")
_QUOTE_WRAPPERS = (("``", "``"), ("`", "`"), ('"', '"'), ("\u201c", "\u201d"))
FIX_WHY_TRUNC = 220


def _load_compose():
    spec = importlib.util.spec_from_file_location("pss_compose_review", HERE / "compose-review.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules["pss_compose_review"] = mod
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
    return mod


def _dispositioned_ids(card: str) -> set[str] | None:
    """Finding ids the author already answered (REVIEW_STATE), or None when
    the block is corrupt — the caller then posts nothing rather than guess.
    A `/resolve F1 accepted` leaves the row in 🚨 until the next refresh; a
    fix button on a finding the author declined would be a nag."""
    spec = importlib.util.spec_from_file_location(
        "pss_review_state", HERE.parents[3] / "scripts" / "review-v3" / "review_state.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules["pss_review_state"] = mod
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
    try:
        state = mod.parse_state(card)
    except ValueError:
        return None
    return set(((state or {}).get("findings") or {}).keys())


def _unwrap_quote(q: str) -> str:
    q = q.strip()
    for open_, close in _QUOTE_WRAPPERS:
        if len(q) > len(open_) + len(close) and q.startswith(open_) and q.endswith(close):
            return q[len(open_):-len(close)].strip()
    return q


def _do_this_blocks(lines: list[str]) -> dict[str, list[str]]:
    """F-id → the lines of its `#### F<n> · Do this` block (fence-aware: a
    heading-looking line inside a fence doesn't end the block)."""
    blocks: dict[str, list[str]] = {}
    cur: str | None = None
    fenced = False
    for ln in lines:
        if ln.lstrip().startswith("```"):
            fenced = not fenced
        elif not fenced:
            m = _DO_THIS_RE.match(ln)
            if m:
                cur = m.group(1)
                blocks[cur] = []
                continue
            if ln.startswith(("### ", "#### ", "<!-- ", "<sub>", "📎 ", "**Full evidence:**")):
                cur = None
        if cur is not None:
            blocks[cur].append(ln)
    return blocks


def _fence_contents(block: list[str]) -> list[list[str]]:
    """Every fenced block's content lines, de-indented by its opening fence."""
    fences: list[list[str]] = []
    cur: list[str] | None = None
    indent = 0
    for ln in block:
        if ln.lstrip().startswith("```"):
            if cur is None:
                cur, indent = [], len(ln) - len(ln.lstrip())
            else:
                fences.append(cur)
                cur = None
            continue
        if cur is not None:
            cur.append(ln[indent:] if ln[:indent].strip() == "" else ln)
    return fences


def derive_fix_entries(card: str, repo_root: Path) -> tuple[list[dict], list[str]]:
    """Blocking-fix suggestions from a v3 author card. See the module
    docstring; returns (entries, human-readable skip reasons).

    Shape rules, from 18 live Do-this blocks sampled 2026-09-25: the fence
    replaces exactly the quoted text in 8 of 10 🚨 blocks, so the fence is
    spliced into the quoted span on the anchored line (indentation outside
    the span survives). Multi-line fences, blocks with several fences, and
    quotes that don't occur literally on exactly one line of the anchor are
    skipped — a wrong button is worse than none. Findings sharing a line are
    applied in id order into one suggestion; one whose quote no longer
    matches after an earlier splice is skipped.
    """
    cr = _load_compose()
    lines = card.splitlines()
    rows: dict[str, dict] = {}
    in_fix = False
    for ln in lines:
        if ln.startswith("### "):
            in_fix = ln.startswith(_FIX_SECTION_HEADING)
            continue
        if in_fix and ln.startswith("|"):
            parsed = cr.parse_finding_line(ln)
            if parsed and parsed["id"] != "F?":
                rows[parsed["id"]] = parsed
    blocks = _do_this_blocks(lines)
    skipped: list[str] = []
    answered = _dispositioned_ids(card)
    if answered is None:
        return [], ["REVIEW_STATE block is corrupt; posting no fixes"]
    for fid in sorted(answered & set(rows)):
        skipped.append(f"{fid}: already answered on the card")
        del rows[fid]
    file_cache: dict[str, list[str] | None] = {}
    by_line: dict[tuple[str, int], list[dict]] = {}
    for fid in sorted(rows, key=lambda f: int(f[1:])):
        row = rows[fid]
        block = blocks.get(fid)
        if block is None:
            skipped.append(f"{fid}: no Do-this block")
            continue
        quote = next((m.group("q") for m in map(_LINE_LABEL_RE.match, block) if m), None)
        why = next((m.group("w") for m in map(_WHY_LABEL_RE.match, block) if m), "")
        fences = _fence_contents(block)
        if quote is None:
            skipped.append(f"{fid}: no Line (verbatim)")
            continue
        if len(fences) != 1:
            skipped.append(f"{fid}: {len(fences)} fenced blocks (need exactly one)")
            continue
        body = [ln for ln in fences[0] if ln.strip()]
        if len(body) != 1:
            skipped.append(f"{fid}: multi-line replacement ({len(body)} lines)")
            continue
        original = _unwrap_quote(quote)
        replacement = body[0].strip()
        ref = _REF_RE.match(row.get("ref") or "")
        fname = row.get("file") or ""
        if not (original and fname and ref):
            skipped.append(f"{fid}: no single file/line anchor")
            continue
        if fname not in file_cache:
            try:
                file_cache[fname] = (repo_root / fname).read_text(encoding="utf-8").splitlines()
            except (OSError, UnicodeDecodeError):
                file_cache[fname] = None
        src = file_cache[fname]
        if src is None:
            skipped.append(f"{fid}: {fname} unreadable in checkout")
            continue
        a = int(ref.group(1))
        b = int(ref.group(2) or a)
        hits = [n for n in range(a, min(b, len(src)) + 1) if original in src[n - 1]]
        if len(hits) != 1:
            skipped.append(f"{fid}: quote found on {len(hits)} anchored lines (need exactly one)")
            continue
        by_line.setdefault((fname, hits[0]), []).append(
            {"id": fid, "original": original, "replacement": replacement,
             "why": _trunc_why(why)})
    entries: list[dict] = []
    for (fname, n), fixes in by_line.items():
        content = file_cache[fname][n - 1]
        cur = content
        ids: list[str] = []
        whys: list[str] = []
        for fx in fixes:
            if fx["original"] not in cur:
                skipped.append(f"{fx['id']}: collides with an earlier fix on {fname}:{n}")
                continue
            cur = cur.replace(fx["original"], fx["replacement"], 1)
            ids.append(fx["id"])
            whys.append(fx["why"])
        if not ids or cur == content:
            continue
        entries.append({"kind": "fix", "file": fname, "line": n, "original": content,
                        "replacement": cur, "ids": ids, "whys": whys})
    return entries, skipped


def _trunc_why(why: str) -> str:
    why = " ".join(why.split())
    if len(why) <= FIX_WHY_TRUNC:
        return why
    cut = why[:FIX_WHY_TRUNC - 1].rsplit(" ", 1)[0]
    return cut.rstrip(",;:—-") + "…"


def run_fix_mode(args) -> int:
    """--fixes-from-author-card: derive, validate, sync. Never annotates."""
    path = Path(args.fixes_from_author_card)
    try:
        card = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        # Unknown, not empty: leave whatever fix buttons exist alone.
        print(f"post-style-suggestions: fix mode: unreadable card {path}: {exc}; "
              "leaving existing fix suggestions in place.", file=sys.stderr)
        return 0
    entries, skipped = derive_fix_entries(card, Path(args.repo_root))
    for reason in skipped:
        print(f"post-style-suggestions: fix mode: skipped {reason}", file=sys.stderr)
    if not entries:
        patch = ""
    elif args.patch_file:
        patch = Path(args.patch_file).read_text(encoding="utf-8")
    else:
        proc = subprocess.run(["gh", "pr", "diff", args.pr, "--repo", args.repo],
                              capture_output=True, text=True)
        if proc.returncode != 0:
            print(f"post-style-suggestions: gh pr diff failed: {proc.stderr.strip()}",
                  file=sys.stderr)
            return 0
        patch = proc.stdout
    valid, dropped = validate_entries(entries, _vff.added_lines_per_file(patch),
                                      Path(args.repo_root))
    for reason in dropped:
        print(f"post-style-suggestions: fix mode: dropped {reason}", file=sys.stderr)
    if args.dry_run:
        print(json.dumps(build_review_payload(valid, FIX_REVIEW_BODY), indent=2))
        return 0
    posted = sync_posted(args.repo, args.pr, valid, FIX_MARKER, FIX_REVIEW_BODY)
    print(f"post-style-suggestions: fix mode: {len(posted)} fix suggestion(s) live.",
          file=sys.stderr)
    return 0


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
    ap.add_argument("--fixes-from-author-card",
                    help="Blocking-fix mode: derive one-click suggestions from this v3 "
                         "author card's 🚨 Do-this blocks instead of reading --in, and post "
                         "them under their own marker. Never annotates.")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    if args.fixes_from_author_card:
        return run_fix_mode(args)

    # An explicit `[]` means "nothing qualified this run" and IS authoritative:
    # the run clears last run's comments and strips the marks they justified.
    # A sidecar that is absent, unreadable, or not an array means we do not
    # know, and the two are not the same. The prompts ask for `[]` rather than
    # nothing precisely so the difference is legible; this used to conflate
    # them, and a refresh where the model simply forgot the sidecar deleted
    # three live buttons out from under the author (fork #233, 2026-08-08).
    #
    # The original rationale for deleting on absence was that a refreshed
    # review must not advertise buttons for findings it no longer reports.
    # That still holds -- it is satisfied by annotating from what is ACTUALLY
    # posted (see below) rather than by destroying the comments, so the marks
    # cannot over-promise either way.
    path = Path(args.infile)
    entries: list | None = None      # None == unknown, leave things alone
    if not path.is_file():
        print("post-style-suggestions: no suggestions file; leaving any existing "
              "suggestions in place.", file=sys.stderr)
    else:
        try:
            parsed = json.loads(path.read_text(encoding="utf-8") or "[]")
        except (json.JSONDecodeError, UnicodeDecodeError) as exc:
            print(f"post-style-suggestions: unreadable {path}: {exc}; leaving any "
                  "existing suggestions in place.", file=sys.stderr)
        else:
            if isinstance(parsed, list):
                entries = parsed
            else:
                print(f"post-style-suggestions: {path} is not a JSON array; leaving "
                      "any existing suggestions in place.", file=sys.stderr)

    if entries is None:
        if args.dry_run:
            print(json.dumps(build_review_payload([]), indent=2))
            return 0
        posted = live_posted(args.repo, args.pr)
        if posted is None:
            # Unknown sidecar AND an unreadable comment list: we know nothing
            # about what is out there, so touch nothing. Leaving last run's
            # marks standing is the lesser error — the comments they point at
            # were not deleted on this path either.
            print("post-style-suggestions: could not list existing suggestions; "
                  "leaving the review untouched.", file=sys.stderr)
            return 0
        print(f"post-style-suggestions: {len(posted)} existing suggestion(s) left "
              "in place.", file=sys.stderr)
        _annotate(args, posted)
        return 0

    if not entries:
        patch = ""
    elif args.patch_file:
        patch = Path(args.patch_file).read_text(encoding="utf-8")
    else:
        proc = subprocess.run(
            ["gh", "pr", "diff", args.pr, "--repo", args.repo],
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

    posted = sync_posted(args.repo, args.pr, valid, MARKER, REVIEW_BODY)
    print(f"post-style-suggestions: posted {len(posted)} suggestion(s).", file=sys.stderr)
    # Annotate on EVERY path, including the zero-posted one. On the re-entrant
    # lane the draft is last run's published body, so a refresh that converts
    # nothing has to actively strip the stale marks and banner — returning
    # early would leave the review advertising buttons that were just deleted.
    _annotate(args, posted)
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""restamp-base-merge.py — carry a v3 review across a base-only merge.

Merging the base branch into a PR moves its head without changing the diff
the review read. Before this script, nothing knew that: `mark-stale` flipped
the label to `review:stale` on the synchronize, the review lane is skipped on
synchronize by design, and nothing ever un-staled it (#21673: Cam's master
merge left a clean review stale, and the Sentinel's G1 red, until someone
asked for a refresh the diff didn't need).

The test is the one `/pr-review` already uses (collect.py): every commit
after the card's CLAUDE_REVIEW_HEAD has two parents, AND the PR's `+`/`-`
lines at the reviewed head equal the ones now — a merge that resolved a
conflict by editing a line the PR adds changed what the review read, and is
a real change. When both hold, the author card's head carriers (the
CLAUDE_REVIEW_HEAD marker and the `head commit` in its sub line) are moved
to the live head and the card is otherwise untouched: no finding, no
disposition, no composition timestamp changes, so pinned-comment.sh's
stale-publish guard still orders it against real refreshes.

Deterministic, no model. Fails closed: any read it can't make, any shape it
doesn't recognise, answers "not base-only" and the caller marks stale as it
always did. Only the v3 author card is restamped; a legacy v2 review keeps
the old behavior.

Usage:
  restamp-base-merge.py --repo pulumi/docs --pr 21673 [--dry-run]
Prints one JSON line: {"restamped": bool, "reason": str, "head": sha}.
Exit 0 either way; exit 2 on bad arguments.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import collect  # noqa: E402
import sentinel  # noqa: E402
from gh_client import GhClient, GhError  # noqa: E402

_SUB_HEAD_RE = re.compile(r"(<sub>(?:Review )?v\d+ · updated [^<]*?· head commit )[0-9a-f]{7,40}(</sub>)")


def restamp_body(author_body: str, head_sha: str) -> str:
    """The card with its head carriers moved to `head_sha`, nothing else."""
    body = sentinel.HEAD_MARKER_RE.sub(f"<!-- CLAUDE_REVIEW_HEAD {head_sha} -->", author_body, count=1)
    return _SUB_HEAD_RE.sub(lambda m: f"{m.group(1)}{head_sha[:7]}{m.group(2)}", body, count=1)


def decide(author_body: str, head_sha: str, commits: list[dict],
           files_then: list[dict] | None, files_now: list[dict]) -> tuple[bool, str]:
    """(restamp?, reason). Pure — every input already fetched."""
    reviewed = collect.reviewed_head(author_body)
    if not reviewed:
        return False, "card carries no CLAUDE_REVIEW_HEAD"
    if head_sha.startswith(reviewed) or reviewed.startswith(head_sha):
        return False, "card already current"
    if not collect.only_merges_since(commits, author_body):
        return False, "a non-merge commit (or an unknown reviewed head) since the review"
    if files_then is None:
        return False, "could not read the diff at the reviewed head"
    if not collect.same_diff(files_then, files_now):
        return False, "a merge changed the PR's own lines (conflict resolution)"
    return True, f"only base merges since {reviewed[:9]} and the diff is unchanged"


def run(gh: GhClient, pr: int, *, dry_run: bool = False) -> dict:
    detail = gh.pr(pr)
    head_sha = (detail.get("head") or {}).get("sha") or ""
    comments = gh.issue_comments(pr)
    card = sentinel._find_comment(comments, sentinel.AUTHOR_MARKER)
    if not card or not head_sha:
        return {"restamped": False, "reason": "no v3 author card", "head": head_sha}
    body = card.get("body") or ""
    commits = gh.pr_commits(pr)
    files_now = gh.pr_files(pr)
    files_then = None
    reviewed = collect.reviewed_head(body)
    base_ref = (detail.get("base") or {}).get("ref") or ""
    if reviewed and base_ref and collect.only_merges_since(commits, body):
        try:
            files_then = gh.compare_files(base_ref, reviewed)
        except GhError:
            files_then = None
    ok, reason = decide(body, head_sha, commits, files_then, files_now)
    if ok:
        new_body = restamp_body(body, head_sha)
        if new_body == body:
            return {"restamped": False, "reason": "nothing to restamp", "head": head_sha}
        if not dry_run:
            gh.patch(f"repos/{gh.repo}/issues/comments/{card['id']}", {"body": new_body})
    return {"restamped": ok, "reason": reason, "head": head_sha}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--repo", required=True)
    ap.add_argument("--pr", type=int, required=True)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv)
    try:
        result = run(GhClient(args.repo), args.pr, dry_run=args.dry_run)
    except (GhError, OSError, ValueError) as exc:
        result = {"restamped": False, "reason": f"error (fail closed): {exc}", "head": ""}
    print(json.dumps(result))
    return 0


if __name__ == "__main__":
    sys.exit(main())

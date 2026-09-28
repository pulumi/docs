#!/usr/bin/env python3
"""cleanup-review-leftovers.py — one-time sweep of what the old review loop
left behind on open PRs. Dry-run by default; `--apply` performs the writes.

The fixes that shipped with this script stop each of these at the source;
this cleans up the instances already on the board:

  stale-label      `review:stale` on a PR whose v3 card is current at the
                   head (#21066's reconcile loop), or whose head moved only
                   by a base merge (#21673). Apply restamps the card when
                   needed and sets the terminal label from the card's
                   🚨/❓ rows (`review:outstanding-issues` / `no-blockers`).
  errored-notice   `<!-- CLAUDE_PROGRESS -->` failure notices ("Review
                   errored", "timed out", "Couldn't start") posted BEFORE the
                   live author card was last updated (#21787 ×3, #21920).
  legacy-page      bot-posted `CLAUDE_REVIEW N/M` pages beside a v3 author
                   card (#21066's August monolith).
  stray-status     the Sentinel status comment on a closed PR, e.g. the one
                   the workflow_run bug posted on pulumi/docs#2
                   (`--extra-pr 2`).

Deterministic, no model. The label call mirrors set-review-label.sh's
exclusivity (one review:* state label). Each action prints one JSON line.

Usage:
  cleanup-review-leftovers.py --repo pulumi/docs [--pr N ...] [--extra-pr 2] [--apply]
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import review_state  # noqa: E402
import sentinel  # noqa: E402
from gh_client import GhClient, GhError  # noqa: E402

_spec = importlib.util.spec_from_file_location("restamp_base_merge", HERE / "restamp-base-merge.py")
restamp = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(restamp)

STATE_LABELS = ("review:in-progress", "review:outstanding-issues", "review:no-blockers",
                "review:stale", "review:error")
LEGACY_WRITERS = sentinel.LEGACY_PAGE_WRITERS
FAILURE_RE = re.compile(r"errored|timed out|Couldn.t start|superseded")
# `<sub>Review v2 · updated 2026-09-28T19:14:42Z · head commit daddce5</sub>`
COMPOSED_RE = re.compile(r"<sub>(?:Review )?v\d+ · updated (\d{4}-\d\d-\d\dT[\d:]+Z)")
PROGRESS_MARKER = "<!-- CLAUDE_PROGRESS -->"


def terminal_label(author_body: str) -> str | None:
    """outstanding-issues when an undecided 🚨/❓ row remains, else no-blockers."""
    try:
        state = review_state.parse_state(author_body) or review_state.empty_state()
    except ValueError:
        return None
    rows = sentinel._card_rows(author_body, ("🚨", "❓"))
    undecided = [r for r in rows if r["id"] not in state.get("findings", {})]
    return "review:outstanding-issues" if undecided else "review:no-blockers"


def plan_pr(gh: GhClient, pr: int) -> list[dict]:
    detail = gh.pr(pr)
    comments = gh.issue_comments(pr)
    labels = {(l.get("name") or "") for l in detail.get("labels") or []}
    head = (detail.get("head") or {}).get("sha") or ""
    actions: list[dict] = []
    card = sentinel._find_comment(comments, sentinel.AUTHOR_MARKER)

    if detail.get("state") != "open":
        for c in comments:
            if (c.get("user") or {}).get("login") == sentinel.BOT_LOGIN and \
                    (c.get("body") or "").startswith(sentinel.STATUS_MARKER):
                actions.append({"pr": pr, "kind": "stray-status", "delete_comment": c["id"]})
        return actions

    if card:
        # The card's COMPOSITION stamp, not the comment's updated_at: a 🔄
        # banner or a base-merge restamp edits the comment without a new
        # review, so updated_at would make a later failed refresh's notice
        # look older than the card. No stamp → keep every notice.
        m = COMPOSED_RE.search(card.get("body") or "")
        composed = m.group(1) if m else ""
        for c in comments:
            body = c.get("body") or ""
            # A failure notice is usually the run's spinner edited in place,
            # so when it failed is its updated_at, not when it was posted.
            failed_at = c.get("updated_at") or c.get("created_at") or ""
            if (composed and (c.get("user") or {}).get("login") == sentinel.BOT_LOGIN
                    and body.startswith(PROGRESS_MARKER) and FAILURE_RE.search(body)
                    and failed_at < composed):
                actions.append({"pr": pr, "kind": "errored-notice", "delete_comment": c["id"]})
        for c in comments:
            if c["id"] == card["id"] or (c.get("user") or {}).get("login") not in LEGACY_WRITERS:
                continue
            first = (c.get("body") or "").split("\n", 1)[0]
            body = c.get("body") or ""
            if sentinel.LEGACY_PAGE_RE.match(first) and sentinel.AUTHOR_MARKER not in body \
                    and sentinel.BRIEF_MARKER not in body:
                actions.append({"pr": pr, "kind": "legacy-page", "delete_comment": c["id"]})

        if "review:stale" in labels:
            body = card.get("body") or ""
            current = sentinel._body_matches_head(body, head)
            needs_restamp = False
            if not current:
                decision = restamp.run(gh, pr, dry_run=True)
                needs_restamp = current = bool(decision["restamped"])
            label = terminal_label(body) if current else None
            if label:
                actions.append({"pr": pr, "kind": "stale-label", "restamp": needs_restamp,
                                "set_label": label})
    return actions


def apply_action(gh: GhClient, a: dict) -> None:
    pr = a["pr"]
    if "delete_comment" in a:
        gh.delete(f"repos/{gh.repo}/issues/comments/{a['delete_comment']}")
    if a.get("restamp"):
        restamp.run(gh, pr, dry_run=False)
    if "set_label" in a:
        for lab in STATE_LABELS:
            if lab != a["set_label"]:
                try:
                    gh.delete(f"repos/{gh.repo}/issues/{pr}/labels/{lab}")
                except GhError:
                    pass  # not on the PR
        gh.post(f"repos/{gh.repo}/issues/{pr}/labels", {"labels": [a["set_label"]]})


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--repo", required=True)
    ap.add_argument("--pr", type=int, action="append", default=[],
                    help="limit to these PRs (default: every open PR)")
    ap.add_argument("--extra-pr", type=int, action="append", default=[],
                    help="also sweep these (closed) PRs for a stray Sentinel status comment")
    ap.add_argument("--apply", action="store_true", help="perform the writes (default: dry run)")
    args = ap.parse_args(argv)
    gh = GhClient(args.repo)
    prs = args.pr or [p["number"] for p in gh.list_open_prs()]
    total = 0
    for pr in [*prs, *args.extra_pr]:
        try:
            actions = plan_pr(gh, pr)
        except GhError as exc:
            print(json.dumps({"pr": pr, "kind": "error", "error": str(exc)}))
            continue
        for a in actions:
            total += 1
            print(json.dumps({**a, "applied": args.apply}))
            if args.apply:
                apply_action(gh, a)
    print(f"{total} action(s){'' if args.apply else ' (dry run — pass --apply to perform them)'}",
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())

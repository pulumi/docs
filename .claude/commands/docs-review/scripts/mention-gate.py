#!/usr/bin/env python3
"""Decide whether a comment really asks for a review refresh.

The `@claude … #update-review` / `#new-review` workflows fire on a plain
substring match in their `if:` expressions (GitHub expressions can't strip
markdown). That is enough to make a comment that merely *quotes* the reply
pattern — an explainer with `@claude F2: … #update-review` in backticks, a
quote-reply of the card's own instructions — dispatch a full model run
(#21535: two of four card versions were unrequested). This script is the
second, precise check the workflows run before spending anything: it
removes fenced code blocks, inline code spans, and blockquoted lines, then
looks for the mention and the hashtag in what is left.

Two entry points, both side-effect free:

  check    — one body (from an env var, never argv): does it carry a live
             `@claude` + `#<hashtag>` outside quoted material? Prints
             `fire=<bool>` and `reason=<text>` in GITHUB_OUTPUT form.
  pending  — given recent comments/reviews on a PR plus the in-flight
             workflow runs, is an explicit refresh already on its way? Used
             by the auto-refresh job so a push-then-comment sequence doesn't
             cancel the human's request through the per-PR concurrency group.
             Prints `yield=<bool>` and `reason=<text>`.

Exit status is 0 for every decision; only a usage error is non-zero, so a
workflow step can't be knocked over by the input it is judging.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime, timedelta, timezone

MENTION = "@claude"

# Fenced blocks first (``` or ~~~, any info string, any length), then inline
# spans — a run of N backticks closed by the same run, per CommonMark — then
# whole blockquoted lines. Order matters: an inline-span regex run over a
# fence would pair the wrong backticks.
#
# The inline pattern deliberately stays on one line (no re.S): a code span
# can't cross a paragraph break, so a stray unpaired backtick must not pair
# with one paragraphs later and swallow a live request in between. Erring
# this way costs at most a run on a quoted protocol split across lines;
# erring the other way silently drops a real request.
_FENCE_RE = re.compile(r"^[ \t]{0,3}(`{3,}|~{3,})[^\n]*\n.*?^[ \t]{0,3}\1[ \t]*$", re.S | re.M)
_UNCLOSED_FENCE_RE = re.compile(r"^[ \t]{0,3}(`{3,}|~{3,})[^\n]*\n.*\Z", re.S | re.M)
_INLINE_RE = re.compile(r"(`+)(?!`)([^\n]+?)(?<!`)\1(?!`)")
_QUOTE_LINE_RE = re.compile(r"^[ \t]{0,3}>.*$", re.M)


def strip_quoted(text: str) -> str:
    """Return `text` with code and blockquotes removed.

    Anything a reader would understand as "showing" rather than "saying":
    fenced blocks, inline spans, and `>`-prefixed lines. An unclosed fence
    swallows the rest of the comment, matching how GitHub renders it.
    """
    text = _FENCE_RE.sub(" ", text)
    text = _UNCLOSED_FENCE_RE.sub(" ", text)
    text = _INLINE_RE.sub(" ", text)
    text = _QUOTE_LINE_RE.sub(" ", text)
    return text


def decide(body: str, hashtag: str, exclude: str | None = None) -> tuple[bool, str]:
    """Should a `#<hashtag>` workflow fire for `body`?

    `exclude` is the more decisive hashtag that wins when both appear live
    (`#new-review` beats `#update-review`). Quoted material never counts for
    either: a quoted `#new-review` does not suppress a live `#update-review`.
    """
    live = strip_quoted(body or "")
    tag = f"#{hashtag}"
    if MENTION not in live or tag not in live:
        raw = body or ""
        if MENTION in raw and tag in raw:
            return False, f"{MENTION} + {tag} appear only inside code or a blockquote"
        return False, f"no live {MENTION} + {tag}"
    if exclude and f"#{exclude}" in live:
        return False, f"#{exclude} present — the more decisive command wins"
    return True, f"live {MENTION} + {tag}"


def _parse_ts(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc)
    except ValueError:
        return None


EXPLICIT_EVENTS = {"issue_comment", "pull_request_review_comment", "pull_request_review"}
IN_FLIGHT = {"queued", "in_progress", "waiting", "requested", "pending"}


def pending_explicit(
    items: list[dict],
    runs: list[dict],
    hashtag: str,
    since: datetime,
    exclude: str | None = None,
) -> tuple[bool, str]:
    """Is an explicit `#<hashtag>` request already being served?

    `items` are issue comments, review comments, and reviews (any mix; each
    needs `user.login`, a body, and `created_at` or `submitted_at`). `runs`
    are workflow runs of the refresh workflow (`event`, `status`,
    `created_at`). Yield when a live request newer than `since` exists AND a
    run of an explicit event type is still in flight and was created after
    that request — a request whose run already finished may have evaluated
    an older head and must not suppress the refresh for the new push.
    """
    newest: datetime | None = None
    newest_by = ""
    for item in items:
        login = ((item.get("user") or {}).get("login") or "")
        if login.endswith("[bot]") and not login.startswith("workprentice"):
            continue  # the pipeline's own progress notes quote the protocol too
        ts = _parse_ts(item.get("created_at") or item.get("submitted_at"))
        if ts is None or ts < since:
            continue
        fire, _ = decide(item.get("body") or "", hashtag, exclude)
        if fire and (newest is None or ts > newest):
            newest, newest_by = ts, login
    if newest is None:
        return False, f"no live #{hashtag} request since {since.isoformat()}"
    for run in runs:
        if run.get("event") not in EXPLICIT_EVENTS:
            continue
        if (run.get("status") or "") not in IN_FLIGHT:
            continue
        run_ts = _parse_ts(run.get("created_at") or run.get("createdAt"))
        if run_ts is not None and run_ts >= newest - timedelta(seconds=5):
            return True, f"explicit #{hashtag} by {newest_by} at {newest.isoformat()} has a run in flight"
    return False, f"explicit #{hashtag} by {newest_by} at {newest.isoformat()} has no run in flight"


def _emit(pairs: dict[str, object]) -> None:
    for key, value in pairs.items():
        text = str(value).lower() if isinstance(value, bool) else str(value)
        print(f"{key}={text}")


def _cmd_check(args: argparse.Namespace) -> int:
    body = os.environ.get(args.body_env, "")
    title = os.environ.get(args.title_env, "") if args.title_env else ""
    fire, reason = decide(f"{body}\n{title}" if title else body, args.hashtag, args.exclude)
    if not fire:
        print(f"::notice::mention gate: not firing — {reason}", file=sys.stderr)
    _emit({"fire": fire, "reason": reason})
    return 0


def _load_json_list(path: str | None) -> list[dict]:
    if not path:
        return []
    try:
        with open(path, encoding="utf-8") as fh:
            data = json.load(fh)
    except (OSError, ValueError):
        return []
    if isinstance(data, dict):
        data = data.get("workflow_runs") or data.get("items") or []
    return [d for d in data if isinstance(d, dict)]


def _cmd_pending(args: argparse.Namespace) -> int:
    since = _parse_ts(args.since)
    if since is None:
        print("pending: --since must be an ISO-8601 timestamp", file=sys.stderr)
        return 2
    items: list[dict] = []
    for path in args.comments:
        items.extend(_load_json_list(path))
    runs = _load_json_list(args.runs)
    do_yield, reason = pending_explicit(items, runs, args.hashtag, since, args.exclude)
    _emit({"yield": do_yield, "reason": reason})
    return 0


def _self_test() -> int:
    failures = 0

    def check(name: str, cond: bool) -> None:
        nonlocal failures
        print(f"  {'ok ' if cond else 'FAIL'} {name}")
        if not cond:
            failures += 1

    # -- decide ------------------------------------------------------------
    check("plain mention fires", decide("@claude F2: sourced it #update-review", "update-review", "new-review")[0])
    check("inline-code quote does not fire",
          not decide("Reply with `@claude F<n>: … #update-review` to answer.", "update-review", "new-review")[0])
    check("fenced quote does not fire",
          not decide("Use:\n```\n@claude F1: fixed #update-review\n```\nthanks", "update-review", "new-review")[0])
    check("tilde fence does not fire",
          not decide("~~~text\n@claude #update-review\n~~~", "update-review", "new-review")[0])
    check("blockquote does not fire",
          not decide("> @claude F2: … #update-review\n\nDone, thanks.", "update-review", "new-review")[0])
    check("live mention beside a quoted one fires",
          decide("Per the card (`@claude F2 #update-review`): @claude F2: the figure is from Q3 #update-review",
                 "update-review", "new-review")[0])
    check("double-backtick span stripped",
          not decide("``@claude #update-review``", "update-review", "new-review")[0])
    check("unclosed fence swallows the rest",
          not decide("```\n@claude #update-review", "update-review", "new-review")[0])
    check("a stray backtick before a live request does not swallow it",
          decide("One stray ` here.\n\n@claude F1: default is 5 per the AWS reference #update-review\n\nSee `verify.py`.",
                 "update-review", "new-review")[0])
    check("a span still can't hide a request on the same line",
          not decide("try `@claude #update-review` first", "update-review", "new-review")[0])
    check("live #new-review beats #update-review",
          not decide("@claude #update-review #new-review", "update-review", "new-review")[0])
    check("quoted #new-review does not suppress",
          decide("@claude F1: fixed #update-review (not `#new-review`)", "update-review", "new-review")[0])
    check("mention only, no hashtag", not decide("@claude what does F2 mean?", "update-review")[0])
    check("hashtag only, no mention", not decide("#update-review please", "update-review")[0])
    check("new-review mode fires", decide("@claude #new-review", "new-review")[0])
    check("empty body", not decide("", "update-review")[0])
    check("reason names the quote",
          "inside code" in decide("`@claude #update-review`", "update-review")[1])

    # -- pending -----------------------------------------------------------
    since = datetime(2026, 9, 10, 20, 20, tzinfo=timezone.utc)
    live = {"user": {"login": "workprentice[bot]"}, "body": "@claude I pushed a fix for F1 #update-review",
            "created_at": "2026-09-10T20:35:02Z"}
    quoted = {"user": {"login": "someone"}, "body": "the pattern is `@claude … #update-review`",
              "created_at": "2026-09-10T20:36:00Z"}
    bot_note = {"user": {"login": "github-actions[bot]"}, "body": "@claude #update-review", "created_at": "2026-09-10T20:37:00Z"}
    old = {"user": {"login": "alice"}, "body": "@claude F3 #update-review", "created_at": "2026-09-10T19:00:00Z"}
    inflight = {"event": "issue_comment", "status": "in_progress", "created_at": "2026-09-10T20:35:06Z"}
    finished = {"event": "issue_comment", "status": "completed", "created_at": "2026-09-10T20:35:06Z"}
    auto = {"event": "workflow_dispatch", "status": "in_progress", "created_at": "2026-09-10T20:35:14Z"}
    earlier_run = {"event": "issue_comment", "status": "in_progress", "created_at": "2026-09-10T20:00:00Z"}

    check("live request + in-flight run yields",
          pending_explicit([live], [inflight], "update-review", since, "new-review")[0])
    check("quoted request does not yield",
          not pending_explicit([quoted], [inflight], "update-review", since, "new-review")[0])
    check("pipeline progress note does not count",
          not pending_explicit([bot_note], [inflight], "update-review", since, "new-review")[0])
    check("request older than window does not yield",
          not pending_explicit([old], [inflight], "update-review", since, "new-review")[0])
    check("finished run does not yield",
          not pending_explicit([live], [finished], "update-review", since, "new-review")[0])
    check("auto dispatch run is not explicit",
          not pending_explicit([live], [auto], "update-review", since, "new-review")[0])
    check("run older than the request does not count",
          not pending_explicit([live], [earlier_run], "update-review", since, "new-review")[0])
    check("review with submitted_at counts",
          pending_explicit([{"user": {"login": "bob"}, "body": "@claude F1 #update-review",
                             "submitted_at": "2026-09-10T20:34:00Z"}],
                           [{"event": "pull_request_review", "status": "queued", "created_at": "2026-09-10T20:34:03Z"}],
                           "update-review", since, "new-review")[0])
    check("no items", not pending_explicit([], [inflight], "update-review", since)[0])

    print("mention-gate self-test:", "PASS" if failures == 0 else f"{failures} FAILED")
    return 1 if failures else 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--self-test", action="store_true")
    sub = parser.add_subparsers(dest="cmd")

    chk = sub.add_parser("check", help="judge one comment body")
    chk.add_argument("--hashtag", required=True, help="e.g. update-review")
    chk.add_argument("--exclude", default=None, help="hashtag that wins when both appear live")
    chk.add_argument("--body-env", required=True, help="env var holding the body (never pass the body as an argument)")
    chk.add_argument("--title-env", default=None, help="env var holding an issue title to consider alongside the body")

    pen = sub.add_parser("pending", help="is an explicit request already in flight?")
    pen.add_argument("--hashtag", required=True)
    pen.add_argument("--exclude", default=None)
    pen.add_argument("--since", required=True, help="ISO-8601; requests older than this are ignored")
    pen.add_argument("--comments", action="append", default=[], help="JSON list of comments/reviews (repeatable)")
    pen.add_argument("--runs", default=None, help="JSON list of workflow runs (gh run list --json or the REST shape)")

    args = parser.parse_args(argv)
    if args.self_test:
        return _self_test()
    if args.cmd == "check":
        return _cmd_check(args)
    if args.cmd == "pending":
        return _cmd_pending(args)
    parser.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())

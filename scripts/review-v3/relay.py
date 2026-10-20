#!/usr/bin/env python3
"""The board's comment relay: what a click on the published board may ask for.

The board can't call GitHub, and it can't run collect.py or act.py: both live
on the approver's machine. What it can do is post a comment on itself and send
it to the Claude session watching the artifact. This module is the grammar
those comments are read against, so the session never interprets one freely:

    pr-review relay: plan
    /pr-review --act --stamp 22295,22297 --force --refresh 22231

    pr-review relay: confirm 3f9c0a1b2c4d5e6f
    pr-review relay: cancel 3f9c0a1b2c4d5e6f
    pr-review relay: refresh

A **plan** message carries the command the board composed. It is parsed with
act.py's own argument parser, and only the flags that name an action are
accepted from a click: anything that picks a file, a backend, or executes a
plan (`--in`, `--plan-out`, `--execute`, `--backend`, `--snapshot-dir`,
`--self-test`, `--dry-run`) is refused, because those are the operator's, not
the board's. Planning is read-only; the session republishes the board with
the plan's preview and its digest.

A **confirm** message names that digest, and it is the only thing that runs a
plan from the board: `act.py --execute PLAN --expect-digest D` refuses a plan
whose bytes no longer hash to D (re-planned since, or edited), one older than
`MAX_AGE_S`, or one already run. So the preview the person read is exactly the
writes that go out, and a second click on the same Confirm sends nothing.

    relay.py parse < comment.txt      # → JSON {kind, argv | digest} or exit 2
    relay.py digest .pr-review-plan.json
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shlex
import sys
from datetime import datetime, timezone
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))

PREFIX = "pr-review relay:"
# How long a planned batch stays confirmable. Every step re-reads its PR in
# the preflight anyway; this bounds how stale a preview the person can be
# looking at when they press Confirm.
MAX_AGE_S = 3600
DIGEST_LEN = 16
# Flags a click may never set: they choose inputs, backends or execution,
# which is the operator's call at the terminal, never the board's.
REFUSED_FLAGS = ("--in", "--plan-out", "--execute", "--backend", "--snapshot-dir", "--self-test", "--dry-run",
                 "--expect-digest", "--preview-out")
MAX_TEXT = 4096


class RelayError(ValueError):
    pass


def plan_digest(path: str | Path) -> str:
    """The plan file's identity: what the board shows beside the preview and
    what Confirm sends back. The bytes, not the parsed JSON, so any edit to the
    file -- a re-plan included -- changes it."""
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()[:DIGEST_LEN]


def plan_age_s(plan: dict, now: datetime | None = None) -> float:
    created = datetime.fromisoformat(str(plan.get("created_at")).replace("Z", "+00:00"))
    return ((now or datetime.now(timezone.utc)) - created).total_seconds()


def _act_argv(command: str) -> list[str]:
    try:
        words = shlex.split(command)
    except ValueError as exc:
        raise RelayError(f"the command does not parse: {exc}") from exc
    if words[:2] != ["/pr-review", "--act"]:
        raise RelayError("a plan message carries exactly one `/pr-review --act …` command")
    argv = words[2:]
    if not argv:
        raise RelayError("the command names no action: nothing is lit on the board")
    for w in argv:
        flag = w.split("=", 1)[0]
        if flag in REFUSED_FLAGS:
            raise RelayError(f"{flag} is not something the board may set")
    import act  # noqa: PLC0415 -- act's parser is the authority on the flags
    parser = act.build_parser()
    parser.exit_on_error = False
    try:
        ns = parser.parse_args(argv)
    except (argparse.ArgumentError, SystemExit) as exc:
        raise RelayError(f"act.py refuses the command: {exc}") from exc
    acts = ("stamp", "route", "request_changes", "chain", "unblock", "fix", "close", "ask_fix",
            "refresh", "rerun", "rerun_checks", "unrequest", "render", "deploy")
    if not any(getattr(ns, a, None) for a in acts):
        raise RelayError("the command names no action")
    return argv


def parse(text: str) -> dict:
    """One relay comment → `{kind: "plan", argv}`, `{kind: "confirm"|"cancel",
    digest}` or `{kind: "refresh"}`. Anything else raises: the session answers
    the thread with the reason and runs nothing."""
    if len(text.encode()) > MAX_TEXT:
        raise RelayError("the message is longer than a comment can be")
    lines = [ln.strip() for ln in text.strip().splitlines() if ln.strip()]
    if not lines or not lines[0].startswith(PREFIX):
        raise RelayError(f"not a relay message (it does not start with `{PREFIX}`)")
    head = lines[0][len(PREFIX):].split()
    rest = lines[1:]
    if head == ["plan"]:
        if len(rest) != 1:
            raise RelayError("a plan message is the header line plus one command line")
        return {"kind": "plan", "argv": _act_argv(rest[0].removeprefix("$ "))}
    if head == ["refresh"] and not rest:
        return {"kind": "refresh"}
    if len(head) == 2 and head[0] in ("confirm", "cancel") and not rest:
        if not re.fullmatch(rf"[0-9a-f]{{{DIGEST_LEN}}}", head[1]):
            raise RelayError("a confirm or cancel names the plan's digest")
        return {"kind": head[0], "digest": head[1]}
    raise RelayError("unknown relay message")


def check_confirmable(path: str | Path, digest: str, now: datetime | None = None) -> dict:
    """The plan at `path`, if pressing Confirm on `digest` may run it."""
    p = Path(path)
    if not p.is_file():
        raise RelayError("there is no pending plan (it already ran, or was discarded)")
    if plan_digest(p) != digest:
        raise RelayError("the pending plan is not the one that was confirmed: it was re-planned since")
    plan = json.loads(p.read_text())
    age = plan_age_s(plan, now)
    if age > MAX_AGE_S:
        raise RelayError(f"the plan is {int(age // 60)} minutes old; plan it again so the preview is current")
    return plan


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("parse", help="read a relay comment on stdin, print it as JSON")
    d = sub.add_parser("digest", help="print a plan file's digest")
    d.add_argument("plan")
    args = ap.parse_args(argv)
    if args.cmd == "digest":
        print(plan_digest(args.plan))
        return 0
    try:
        print(json.dumps(parse(sys.stdin.read())))
    except RelayError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    if sys.argv[1:] == ["--self-test"]:  # the pipeline runner's convention
        import test_relay  # noqa: PLC0415
        sys.exit(test_relay.run_standalone())
    sys.exit(main())

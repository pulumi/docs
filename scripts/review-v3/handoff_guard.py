#!/usr/bin/env python3
"""v3 handoff guard — should THIS publish job publish, re-dispatch, or rest?

claude-code-review.yml's model job hands its validated review to the
credentialed publish job as an artifact stamped with the SHA it reviewed.
A push that lands while the model works makes that handoff stale, and
publishing it would stamp the cards with a SHA that is no longer head and
flip labels for content nobody can see in the diff. The freshness check is
the one comparison below: handoff SHA against the live PR head.

What happens after a refusal is the part that used to be missing. A
superseded publish exited 0 having touched only the check-run and the
spinner, so the PR kept `review:in-progress` from a run that was over, and
nothing restarted the review — a push never fires one (only open,
ready_for_review, and an explicit dispatch do). PR #21642 sat like that
until someone dispatched the workflow by hand. So the guard now returns
one of three actions, and the workflow owns the side effects of each:

  publish     — head unchanged; publish the cards as before.
  redispatch  — head moved; rest the label at review:stale and dispatch a
                fresh review at the live head (the `redispatch` job).
  rest        — head moved AND this run was itself the MAX_DEPTH'th
                automatic re-dispatch in a row. Stop: leave review:stale
                and tell the author how to refresh once the branch settles.
                The cap is what keeps a push train from queueing a review
                per push; two chained retries cover every real case seen so
                far and bound the worst case at three full reviews per
                ready-transition.

`settle_wait` is the redispatch job's debounce: a retry dispatched while
the author is mid push-train just gets superseded too and burns a slot, so
the job waits until the head has been quiet for SETTLE_S before dispatching
(idle runner seconds cost nothing next to a model call).

Deterministic, no model. `decide` and `settle_wait` are pure; the CLI reads
the PR head via gh and prints the decision to GITHUB_OUTPUT.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timezone

# Chained automatic re-dispatches allowed before resting at review:stale.
MAX_DEPTH = 2
# Seconds the head must have been quiet before a re-dispatch fires.
SETTLE_S = 180


def decide(handoff_sha: str, live_sha: str | None, depth: int,
           max_depth: int = MAX_DEPTH) -> tuple[str, str]:
    """(action, reason). `depth` is how many automatic re-dispatches this
    run is already downstream of (0 for a triage-chained or human run).
    Fail toward publishing when the live head is unknown: the handoff is at
    a real head, and a refusal here would drop a review on the floor with
    no evidence that it is stale."""
    if not live_sha:
        return "publish", "live head unreadable — publishing the handoff as-is"
    if live_sha.lower() == handoff_sha.lower():
        return "publish", "handoff is current"
    if depth >= max_depth:
        return "rest", (f"superseded — handoff at {handoff_sha[:7]}, live head "
                        f"{live_sha[:7]}; already {depth} automatic re-dispatches "
                        f"deep (cap {max_depth}), resting at review:stale")
    return "redispatch", (f"superseded — handoff at {handoff_sha[:7]}, live head "
                          f"{live_sha[:7]}; re-dispatching (depth {depth + 1})")


def settle_wait(now: datetime, pushed_at: datetime | None,
                settle_s: int = SETTLE_S) -> int:
    """Seconds to sleep before dispatching so the head has been quiet for
    `settle_s`. Unknown push time → no wait (never block on missing data)."""
    if pushed_at is None:
        return 0
    quiet = (now - pushed_at).total_seconds()
    if quiet >= settle_s:
        return 0
    return int(settle_s - quiet)


def _parse_iso(s: str) -> datetime:
    return datetime.fromisoformat(s.replace("Z", "+00:00")).astimezone(timezone.utc)


def _gh_json(args: list[str]):
    out = subprocess.run(["gh", *args], check=True, capture_output=True, text=True).stdout
    return json.loads(out) if out.strip() else None


def _write_outputs(kv: dict[str, str]) -> None:
    out = os.environ.get("GITHUB_OUTPUT")
    lines = "".join(f"{k}={v}\n" for k, v in kv.items())
    if out:
        with open(out, "a") as fh:
            fh.write(lines)
    sys.stdout.write(lines)


def cmd_decide(a: argparse.Namespace) -> int:
    handoff = json.load(open(a.handoff))
    handoff_sha = handoff["head_sha"]
    try:
        live = _gh_json(["api", f"repos/{a.repo}/pulls/{a.pr}", "--jq", "{h: .head.sha}"])["h"]
    except Exception as exc:  # noqa: BLE001 — degrade, documented in decide()
        print(f"::warning::handoff-guard: could not read PR head ({exc})")
        live = None
    action, reason = decide(handoff_sha, live, a.depth, a.max_depth)
    print(f"handoff-guard: action={action} — {reason}")
    _write_outputs({
        "action": action,
        "reason": reason,
        "superseded": "false" if action == "publish" else "true",
        "live_head": live or "",
        "next_depth": str(a.depth + 1),
    })
    return 0


def cmd_settle(a: argparse.Namespace) -> int:
    pushed = _parse_iso(a.pushed_at) if a.pushed_at else None
    wait = settle_wait(datetime.now(timezone.utc), pushed, a.settle)
    print(f"handoff-guard: settle wait {wait}s (head pushed at {a.pushed_at or 'unknown'})")
    _write_outputs({"wait": str(wait)})
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--self-test", action="store_true")
    sub = ap.add_subparsers(dest="cmd")
    d = sub.add_parser("decide", help="publish / redispatch / rest for a handoff")
    d.add_argument("--handoff", required=True, help=".review-v3-handoff.json")
    d.add_argument("--repo", required=True)
    d.add_argument("--pr", required=True)
    d.add_argument("--depth", type=int, default=0,
                   help="automatic re-dispatches this run is downstream of")
    d.add_argument("--max-depth", type=int, default=MAX_DEPTH)
    s = sub.add_parser("settle", help="seconds to wait before re-dispatching")
    s.add_argument("--pushed-at", default="", help="ISO-8601 committer date of the live head")
    s.add_argument("--settle", type=int, default=SETTLE_S)
    a = ap.parse_args(argv)
    if a.self_test:
        return _self_test()
    if a.cmd == "decide":
        return cmd_decide(a)
    if a.cmd == "settle":
        return cmd_settle(a)
    ap.error("one of: decide, settle, --self-test")
    return 2


def _self_test() -> int:
    A, B = "a" * 40, "b" * 40
    assert decide(A, A, 0)[0] == "publish"
    assert decide(A, A.upper(), 0)[0] == "publish"          # case-insensitive
    assert decide(A, None, 0)[0] == "publish"               # unknown head → publish
    assert decide(A, "", 5)[0] == "publish"
    assert decide(A, B, 0)[0] == "redispatch"
    assert decide(A, B, 1)[0] == "redispatch"
    assert decide(A, B, MAX_DEPTH)[0] == "rest"
    assert decide(A, B, MAX_DEPTH + 3)[0] == "rest"
    assert decide(A, B, 0, max_depth=0)[0] == "rest"
    assert "depth 1" in decide(A, B, 0)[1]
    now = datetime(2026, 9, 16, 22, 30, tzinfo=timezone.utc)
    assert settle_wait(now, None) == 0
    assert settle_wait(now, now) == SETTLE_S
    assert settle_wait(now, _parse_iso("2026-09-16T22:29:00Z")) == SETTLE_S - 60
    assert settle_wait(now, _parse_iso("2026-09-16T22:20:00Z")) == 0
    assert settle_wait(now, now, settle_s=0) == 0
    print("all handoff_guard self-tests passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())

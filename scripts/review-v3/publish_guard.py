#!/usr/bin/env python3
"""Sentinel publish guard — should THIS run publish its verdict?

review-sentinel.yml runs without a concurrency group (a cancelled job renders
as a failing check on the PR, and GitHub cancels the older *pending* job of a
group even with cancel-in-progress off). Overlapping runs for one PR are
therefore normal, and this guard is what keeps a stale verdict from
overwriting a fresh one:

  * Every published `Sentinel` commit status carries the workflow run's URL
    as its `target_url` (`.../actions/runs/<run id>`). Check-runs published
    before the switch to a status carry the run id as `external_id`, and
    are still read so a PR open across the switch keeps its ordering.
  * A run publishes only if (a) the PR head still equals the head it
    evaluated, and (b) no newer run (higher run id) has already published a
    Sentinel verdict at that head.

Both refusals conclude the job `success` with a notice — the newer run (or
the `synchronize` run for the new head) owns the verdict. Deterministic, no
model, no checkout; the CLI reads two API objects and prints the decision.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys

CHECK_NAME = "Sentinel"
RUN_URL_RE = re.compile(r"/actions/runs/(\d+)(?:/|$)")


def run_id_from_url(url: str | None) -> int | None:
    """The workflow run id in a status's `target_url`, or None."""
    m = RUN_URL_RE.search(url or "")
    return int(m.group(1)) if m else None


def latest_published_run_id(check_runs: list[dict], statuses: list[dict] = ()) -> int | None:
    """Highest run id across the Sentinel statuses (`target_url`) and any
    legacy Sentinel check-runs (`external_id`)."""
    ids: list[int] = []
    for c in check_runs:
        ext = str(c.get("external_id") or "").strip()
        if c.get("name") == CHECK_NAME and ext.isdigit():
            ids.append(int(ext))
    for s in statuses:
        rid = run_id_from_url(s.get("target_url"))
        if s.get("context") == CHECK_NAME and rid is not None:
            ids.append(rid)
    return max(ids, default=None)


def head_moved(verdict_head: str, pr_head: str | None) -> str | None:
    """The "head moved" reason, or None. Unknown head => not moved.

    Shared with sentinel.py, which asks the same question before it
    writes the two PR comments -- those writes happen in-process, long
    before this guard runs as a later workflow step. It had its own copy
    and the two had already drifted: this one folds case, that one did
    not, so a differently-cased SHA would have stopped the check-run and
    let the comments through."""
    if pr_head and pr_head.lower() != verdict_head.lower():
        return (f"head moved: evaluated `{verdict_head[:9]}`, PR is at "
                f"`{pr_head[:9]}` — the run for the new head owns the verdict")
    return None


def decide(my_run_id: int, verdict_head: str, pr_head: str | None,
           check_runs: list[dict], statuses: list[dict] = ()) -> tuple[bool, str]:
    """(publish?, reason). Fail toward publishing when the PR head is unknown."""
    moved = head_moved(verdict_head, pr_head)
    if moved:
        return False, moved
    newest = latest_published_run_id(check_runs, statuses)
    if newest is not None and newest > my_run_id:
        return False, (f"superseded: run {newest} already published a verdict at "
                       f"`{verdict_head[:9]}` after this run ({my_run_id}) started")
    return True, "this run holds the newest verdict"


def _gh_json(args: list[str]):
    out = subprocess.run(["gh", *args], check=True, capture_output=True, text=True).stdout
    return json.loads(out) if out.strip() else None


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--repo")
    ap.add_argument("--pr")
    ap.add_argument("--run-id", type=int)
    ap.add_argument("--verdict", help="verdict.json written by sentinel.py")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args(argv)
    if a.self_test:
        return _self_test()
    if not (a.repo and a.pr and a.run_id and a.verdict):
        ap.error("--repo, --pr, --run-id and --verdict are required")
    verdict = json.load(open(a.verdict))
    head = verdict["head_sha"]
    try:
        pr_head = _gh_json(["api", f"repos/{a.repo}/pulls/{a.pr}", "--jq", "{h: .head.sha}"])["h"]
    except Exception as exc:  # fail toward publishing; the verdict is at a real head
        print(f"::warning::publish-guard: could not read PR head ({exc}); publishing")
        pr_head = None
    try:
        runs = _gh_json(["api", f"repos/{a.repo}/commits/{head}/check-runs?check_name={CHECK_NAME}&per_page=50"])
        check_runs = (runs or {}).get("check_runs", [])
    except Exception as exc:
        print(f"::warning::publish-guard: could not list check-runs ({exc}); publishing")
        check_runs = []
    try:
        # Newest first, so the first page holds any run that published after
        # this one started.
        statuses = _gh_json(["api", f"repos/{a.repo}/commits/{head}/statuses?per_page=100"]) or []
    except Exception as exc:
        print(f"::warning::publish-guard: could not list statuses ({exc}); publishing")
        statuses = []
    publish, reason = decide(a.run_id, head, pr_head, check_runs, statuses)
    print(f"publish-guard: publish={'true' if publish else 'false'} — {reason}")
    if not publish:
        print(f"::notice::Sentinel run {a.run_id} did not publish — {reason}")
    out = os.environ.get("GITHUB_OUTPUT")
    if out:
        with open(out, "a") as fh:
            fh.write(f"publish={'true' if publish else 'false'}\nreason={reason}\n")
    return 0


def _self_test() -> int:
    H = "a" * 40
    cr = lambda rid, name=CHECK_NAME: {"name": name, "external_id": str(rid) if rid is not None else ""}
    assert decide(10, H, H, []) == (True, "this run holds the newest verdict")
    assert decide(10, H, H, [cr(9)])[0] is True
    assert decide(10, H, H, [cr(11)])[0] is False
    assert decide(10, H, H, [cr(11, "sentinel")])[0] is True        # job-named check ignored
    assert decide(10, H, H, [cr(None)])[0] is True                    # legacy check without id
    assert decide(10, H, "b" * 40, [])[0] is False                    # head moved
    assert decide(10, H, None, [cr(9)])[0] is True                    # unknown PR head → publish
    assert decide(10, H, H.upper(), [])[0] is True                    # case-insensitive
    assert latest_published_run_id([cr(3), cr(12), cr("x")]) == 12
    st = lambda rid, ctx=CHECK_NAME: {"context": ctx, "target_url": f"https://github.com/o/r/actions/runs/{rid}"}
    assert decide(10, H, H, [], [st(11)])[0] is False                 # a newer status wins
    assert decide(10, H, H, [], [st(9)])[0] is True
    assert decide(10, H, H, [], [st(11, "Update Changelog")])[0] is True  # other contexts ignored
    assert decide(10, H, H, [], [{"context": CHECK_NAME, "target_url": None}])[0] is True
    assert decide(10, H, H, [cr(12)], [st(9)])[0] is False            # legacy check-run still counts
    assert latest_published_run_id([cr(3)], [st(12), st(7)]) == 12
    assert run_id_from_url("https://github.com/o/r/actions/runs/38986448930/job/1") == 38986448930
    assert run_id_from_url("https://github.com/o/r/pull/5") is None
    print("all publish_guard self-tests passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Sentinel publish guard — should THIS run publish its verdict?

review-sentinel.yml runs without a concurrency group (a cancelled job renders
as a failing check on the PR, and GitHub cancels the older *pending* job of a
group even with cancel-in-progress off). Overlapping runs for one PR are
therefore normal, and this guard is what keeps a stale verdict from
overwriting a fresh one:

  * Every published check-run carries `external_id = <workflow run id>`.
  * A run publishes only if (a) the PR head still equals the head it
    evaluated, and (b) no newer run (higher run id) has already published a
    Sentinel check-run at that head.

Both refusals conclude the job `success` with a notice — the newer run (or
the `synchronize` run for the new head) owns the verdict. Deterministic, no
model, no checkout; the CLI reads two API objects and prints the decision.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys

CHECK_NAME = "Sentinel"


def latest_published_run_id(check_runs: list[dict]) -> int | None:
    """Highest run id recorded in `external_id` across the Sentinel check-runs."""
    best: int | None = None
    for c in check_runs:
        if c.get("name") != CHECK_NAME:
            continue
        ext = str(c.get("external_id") or "").strip()
        if not ext.isdigit():
            continue
        rid = int(ext)
        if best is None or rid > best:
            best = rid
    return best


def decide(my_run_id: int, verdict_head: str, pr_head: str | None,
           check_runs: list[dict]) -> tuple[bool, str]:
    """(publish?, reason). Fail toward publishing when the PR head is unknown."""
    if pr_head and pr_head.lower() != verdict_head.lower():
        return False, (f"head moved: evaluated `{verdict_head[:9]}`, PR is at "
                       f"`{pr_head[:9]}` — the run for the new head owns the verdict")
    newest = latest_published_run_id(check_runs)
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
    publish, reason = decide(a.run_id, head, pr_head, check_runs)
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
    print("all publish_guard self-tests passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Sentinel publisher — post the verdict as the `Sentinel` commit status.

The Sentinel used to publish a check-run (`POST /check-runs` with the job's
GITHUB_TOKEN). That API can't choose a check suite, so GitHub files the run
into the OLDEST GitHub Actions suite at the head SHA: whichever workflow won
the suite-creation race on PR open. When that workflow runs again for the
same event (this one, or staging-deploy-auto.yml, on `opened` then
`ready_for_review`), GitHub treats the first suite as superseded and hides
its runs. Every later verdict lands in the hidden suite too, so branch
protection reads "Sentinel: Expected — Waiting for status to be reported"
and auto-merge never fires on a green, approved PR (pulumi/docs#22308,
pulumi/docs#22316).

A commit status belongs to no suite, so nothing can supersede it:

  * `state` from the conclusion: `neutral` (report-only, draft) passes as
    `success` — GitHub already counted a neutral check as passing —
    `pending` (only in-flight gates left) is `pending`, which a required
    status treats as not-yet-passing, `action_required` (couldn't evaluate)
    is `error`, and anything unknown fails closed.
  * `description` is the verdict title (140-char API limit).
  * `target_url` is this workflow run. publish_guard.py reads the run id
    back out of it, and the run's job summary carries the full gate table
    the check-run's output used to.

Beside it, one informational status per gate (`Sentinel / review`,
`Sentinel / findings`, ...), so the merge box says which gate is red and
what it wants and links where to act on it. Only
`Sentinel` is required; the gate statuses come from `gate_statuses` in the
verdict JSON. A `Sentinel / …` status already at the head that this verdict
doesn't name is turned green, so a gate that stopped applying can't keep an
old red.

Transition: GitHub requires BOTH a check and a status that share a required
name, so a check-run published before the switch would keep gating its head
with whatever it last said. Until the head moves, each verdict is mirrored
onto the `Sentinel` check-runs already at the head.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

from publish_guard import CHECK_NAME

DESCRIPTION_MAX = 140
STATE_FOR = {"success": "success", "neutral": "success",
             "failure": "failure", "pending": "pending", "action_required": "error"}


def status_state(conclusion: str | None) -> str:
    return STATE_FOR.get(conclusion or "", "failure")


def status_payload(verdict: dict, run_url: str) -> dict:
    desc = " ".join((verdict.get("title") or "").split())
    if len(desc) > DESCRIPTION_MAX:
        desc = desc[:DESCRIPTION_MAX - 1] + "…"
    return {"state": status_state(verdict.get("conclusion")), "context": CHECK_NAME,
            "description": desc, "target_url": run_url}


GATE_PREFIX = f"{CHECK_NAME} / "


def gate_payloads(verdict: dict, fallback_url: str, existing: list[dict] = ()) -> list[dict]:
    """The per-gate statuses to post: the verdict's own, plus a green one for
    any `Sentinel / …` context already at the head that it no longer names."""
    out = []
    for g in verdict.get("gate_statuses") or []:
        out.append({"state": g.get("state") or "failure", "context": g["context"],
                    "description": (g.get("description") or "")[:DESCRIPTION_MAX],
                    "target_url": g.get("target_url") or fallback_url})
    named = {g["context"] for g in out}
    for st in existing:
        ctx = st.get("context") or ""
        if ctx.startswith(GATE_PREFIX) and ctx not in named:
            out.append({"state": "success", "context": ctx,
                        "description": "doesn't apply at this commit", "target_url": fallback_url})
            named.add(ctx)
    return out


def legacy_check_runs(check_runs: list[dict]) -> list[dict]:
    """Sentinel check-runs a GITHUB_TOKEN may update: the ones GitHub
    Actions created. The job's own check is `sentinel`, never mirrored."""
    return [c for c in check_runs if c.get("name") == CHECK_NAME
            and ((c.get("app") or {}).get("slug") or "github-actions") == "github-actions"]


def mirror_payload(verdict: dict) -> dict:
    # A completed check-run has no pending conclusion; the legacy mirror only
    # has to keep blocking, so a pending verdict mirrors as a failure.
    c = verdict.get("conclusion") or "failure"
    return {"status": "completed", "conclusion": "failure" if c == "pending" else c,
            "output": {"title": verdict.get("title") or "", "summary": verdict.get("summary") or ""}}


def _gh(args: list[str], body: dict | None = None):
    out = subprocess.run(["gh", *args], check=True, capture_output=True, text=True,
                         input=json.dumps(body) if body is not None else None).stdout
    return json.loads(out) if out.strip() else None


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--repo")
    ap.add_argument("--pr")
    ap.add_argument("--run-url", help="this workflow run's URL")
    ap.add_argument("--verdict", help="verdict.json written by sentinel.py")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args(argv)
    if a.self_test:
        return _self_test()
    if not (a.repo and a.pr and a.run_url and a.verdict):
        ap.error("--repo, --pr, --run-url and --verdict are required")
    verdict = json.load(open(a.verdict))
    head = verdict.get("head_sha") or ""
    # A verdict with no head SHA is an evaluation that could not read the PR
    # at all (sentinel.py's SentinelDataError path). Posting it is a
    # guaranteed `422 No commit found for SHA:` that reads as a publish bug;
    # say what actually happened instead.
    if not head:
        print(f"::error::The Sentinel could not read PR #{a.pr} (see the Evaluate step); "
              "no verdict to publish. Re-run this job.")
        return 1
    payload = status_payload(verdict, a.run_url)
    # Gate statuses first, so the required one is the last to change: a
    # merge box that turns green with a red gate row under it would be
    # confusing for the few seconds between the two writes.
    try:
        existing = _gh(["api", f"repos/{a.repo}/commits/{head}/statuses?per_page=100"]) or []
    except Exception as exc:
        print(f"::warning::Could not list existing statuses ({exc}); stale gate rows may linger.")
        existing = []
    # In parallel: four sequential `gh api` calls were ~4 s of a ~30 s job.
    def _post(g: dict) -> str | None:
        try:
            _gh(["api", "--method", "POST", f"repos/{a.repo}/statuses/{head}", "--input", "-"], g)
            return None
        except Exception as exc:
            return f"::warning::Could not publish {g['context']} ({exc}); it is informational only."
    # A gate status links where you act on it (sentinel.gate_statuses); the
    # PR is the fallback, never this run's page.
    gates = gate_payloads(verdict, f"https://github.com/{a.repo}/pull/{a.pr}", existing)
    if gates:
        with ThreadPoolExecutor(max_workers=len(gates)) as pool:
            for warning in pool.map(_post, gates):
                if warning:
                    print(warning)
    _gh(["api", "--method", "POST", f"repos/{a.repo}/statuses/{head}", "--input", "-"], payload)
    print(f"published: Sentinel {payload['state']} — {payload['description']}")

    try:
        runs = (_gh(["api", f"repos/{a.repo}/commits/{head}/check-runs?check_name={CHECK_NAME}&filter=all&per_page=50"])
                or {}).get("check_runs", [])
    except Exception as exc:
        print(f"::warning::Could not list legacy Sentinel check-runs ({exc}); if one is visible at "
              f"`{head[:9]}` it still gates the merge with its old verdict. Re-run this job.")
        runs = []
    for c in legacy_check_runs(runs):
        try:
            _gh(["api", "--method", "PATCH", f"repos/{a.repo}/check-runs/{c['id']}", "--input", "-"],
                mirror_payload(verdict))
            print(f"mirrored onto legacy check-run {c['id']}")
        except Exception as exc:
            print(f"::warning::Could not mirror the verdict onto legacy check-run {c['id']} ({exc}); "
                  "it still gates the merge with its old verdict. Re-run this job.")

    summary_file = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_file:
        with open(summary_file, "a") as fh:
            fh.write(f"## Sentinel: {verdict.get('title') or ''}\n\n{verdict.get('summary') or ''}\n")
    return 0


def _self_test() -> int:
    url = "https://github.com/pulumi/docs/actions/runs/123"
    v = lambda c, t="All gates green": {"conclusion": c, "title": t, "summary": "s", "head_sha": "a" * 40}
    assert status_payload(v("success"), url) == {"state": "success", "context": "Sentinel",
                                                 "description": "All gates green", "target_url": url}
    assert status_payload(v("neutral", "Preview — would be: failure (not enforced yet)"), url)["state"] == "success"
    assert status_payload(v("neutral", "Draft — not evaluated"), url)["state"] == "success"
    assert status_payload(v("failure", "2 gate(s) red"), url)["state"] == "failure"
    assert status_payload(v("action_required"), url)["state"] == "error"
    assert status_payload(v("pending", "Waiting on the automated review"), url)["state"] == "pending"
    assert mirror_payload(v("pending"))["conclusion"] == "failure"
    assert status_payload(v("cancelled"), url)["state"] == "failure"       # unknown fails closed
    assert status_payload(v(None), url)["state"] == "failure"
    long = status_payload(v("failure", "x" * 200), url)["description"]
    assert len(long) == DESCRIPTION_MAX and long.endswith("…")
    assert status_payload(v("success", "two\nlines"), url)["description"] == "two lines"
    gha = {"slug": "github-actions"}
    runs = [{"id": 1, "name": "Sentinel", "app": gha}, {"id": 2, "name": "sentinel", "app": gha},
            {"id": 3, "name": "Sentinel", "app": {"slug": "other-app"}}, {"id": 4, "name": "Sentinel"}]
    assert [c["id"] for c in legacy_check_runs(runs)] == [1, 4]
    assert mirror_payload(v("neutral", "Draft — not evaluated")) == {
        "status": "completed", "conclusion": "neutral",
        "output": {"title": "Draft — not evaluated", "summary": "s"}}
    gv = {"gate_statuses": [{"context": "Sentinel / findings", "state": "failure",
                             "description": "1 open finding", "target_url": "https://card"},
                            {"context": "Sentinel / review", "state": "success",
                             "description": "ok", "target_url": None}]}
    gp = gate_payloads(gv, url, [{"context": "Sentinel / oversized"}, {"context": "Sentinel"},
                                 {"context": "Sentinel / findings"}, {"context": "Update Changelog"}])
    assert [g["context"] for g in gp] == ["Sentinel / findings", "Sentinel / review", "Sentinel / oversized"], gp
    assert gp[0]["target_url"] == "https://card" and gp[1]["target_url"] == url
    assert gp[2]["state"] == "success"
    assert gate_payloads({}, url) == []
    print("all publish_verdict self-tests passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())

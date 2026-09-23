#!/usr/bin/env python3
"""Finalize dispatched pulumi-test.io staging deploys that no event cascade reports.

Sentinel gate G4 requires a successful staging deploy at the PR's current
head. The deploy is produced by `staging-deploy-auto.yml` (unattended) or
`/deploy-staging` (attended), both of which dispatch "Build and deploy
testing" and then — correctly — get out of the way. Nothing then tells the
Sentinel to look again, so a PR that has satisfied G4 keeps a red,
**non-waivable** gate until somebody dispatches `review-sentinel.yml` by
hand. PR #21789 is the worked example: deploy green at 22:44, gate still red
at 23:04, cleared only by a manual dispatch.

WHY THIS IS A SWEEP AND NOT A TRIGGER. Three event-shaped fixes have been
tried and each one is dead for a structural reason, all of them already paid
for in this repo:

  1. A job inside the dispatched run (#21676). `workflow_dispatch` executes
     the workflow file **from the ref it is dispatched at**, so a job added
     on master does not exist for a branch cut before it landed.
  2. A `workflow_run` listener — `staging-status.yml` (#21696). GitHub emits
     no `workflow_run` cascade for a run dispatched with `GITHUB_TOKEN`, and
     both lanes dispatch with `GITHUB_TOKEN`. Measured again on 2026-09-21:
     of 95 runs of that listener, 94 were master *pushes* (skipped by its own
     job `if`) and one was a hand-run backfill. Twenty-eight dispatched
     PR-branch deploys in the same history produced **zero**.
  3. Adding "Build and deploy testing" to `review-sentinel.yml`'s
     `workflow_run` list. This is the tempting one-liner and it is a silent
     no-op for exactly the same reason as (2) — the cascade that never fires
     for one listener does not fire for another. `test_staging_sweep.py`
     pins that it stays out of the list, so the no-op cannot be re-landed as
     a fix.

A `schedule` is the only trigger immune to both branch age and token
provenance, which is the shape `staging-deploy.sh` and `staging-status.yml`
have both been asking for in prose since #21696. It costs latency — up to
one cron interval on top of a ~9-minute deploy — and buys a gate that
cannot stick red on a condition the PR has met.

WHAT IT DOES, per sweep:

  - lists recent "Build and deploy testing" runs, keeping the ones that are
    `workflow_dispatch`, completed, and not on the default branch (a master
    push deploy is nobody's staging evidence);
  - groups them by head SHA, because two deploys of one SHA are one fact —
    a success anywhere in that group is the evidence `_staging_evidence`
    would read, so a retry after a failure resolves to success;
  - writes the terminal `staging/pulumi-test-io` status when the SHA does
    not already carry that verdict from an authorized writer;
  - pokes `review-sentinel.yml` with an explicit `pr_number` when the deploy
    SUCCEEDED and that SHA is still the open PR's current head.

IDEMPOTENCE IS THE WHOLE CONTRACT, because this runs every few minutes over
an overlapping window. The key is the status itself: a SHA whose authorized
`staging/pulumi-test-io` status already equals the verdict the sweep would
write is finished, and the sweep neither rewrites it nor re-pokes. No side
state, nothing to get out of step, and it converges with the `workflow_run`
listener for free — whichever gets there first, the other stands down. The
status is written LAST, after the poke, so a failed poke is retried next
cycle rather than being sealed off by a status that says "handled".

`--lookback-hours` bounds the work and, with it, the blast radius of a
pathological retry loop: a run whose status write keeps failing drops out of
the window rather than being re-poked forever.

ONLY A SUCCESS POKES. A failed deploy leaves G4 red, which it already was,
so re-running the evaluator tells the PR nothing it is not already showing.

An unresolvable PR is not an error: the status belongs to the SHA, not to
the PR, so a closed or renamed branch still gets its verdict recorded. Same
rule `staging-status.yml` states.

NO PR CODE, EVER. Every fact comes from the API as data; this script reads
no working tree and runs nothing from a PR.

Self-contained — run the smoke checks with `staging-sweep.py --self-test`.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from gh_client import GhClient  # noqa: E402

# The workflow whose runs are G4's evidence, the context the verdict is
# recorded under, and the writer allowlist below all mirror sentinel.py's.
# They are re-spelled rather than imported because sentinel.py pulls in yaml
# (via routing) and the sweep job installs nothing; test_staging_sweep.py
# pins them equal, since a drift here is a gate that reads one thing and a
# sweep that writes another.
STAGING_WORKFLOW_FILE = "testing-build-and-deploy.yml"
STAGING_STATUS_CONTEXT = "staging/pulumi-test-io"
# Identities whose status the Sentinel will take as evidence. Anyone with
# push access can write a commit status, so a status from anybody else is
# not "already finalized" — it is noise the sweep must write over.
STAGING_STATUS_WRITERS = frozenset({"github-actions[bot]", "pulumi-bot"})
SENTINEL_WORKFLOW_FILE = "review-sentinel.yml"
DEPLOYED_SITE_URL = "https://www.pulumi-test.io"
DEFAULT_LOOKBACK_HOURS = 6
# One page is ~two days of this workflow's runs; the lookback does the real
# filtering.
RUN_PAGE_SIZE = 100

# The three descriptions are part of the contract `staging-status.yml`
# established — readers and scripts have learned to recognize them, so the
# sweep writing a fourth spelling would be a silent break.
VERDICTS = {
    "success": ("success", "staging deploy green"),
    "cancelled": ("error", "staging deploy cancelled"),
}
FAILED_VERDICT = ("failure", "staging deploy failed")


def log(msg: str) -> None:
    print(msg, file=sys.stderr)


def _parse_ts(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def verdict_for(conclusion: str) -> tuple[str, str, bool]:
    """(status state, description, is_success) for a run conclusion."""
    if conclusion in VERDICTS:
        state, desc = VERDICTS[conclusion]
        return state, desc, conclusion == "success"
    state, desc = FAILED_VERDICT
    return state, desc, False


def candidate_runs(runs: list[dict], *, default_branch: str, now: datetime,
                   lookback_hours: int) -> list[dict]:
    """The dispatched, completed, non-default-branch deploys inside the window.

    A `push` deploy of the default branch is the production-shaped run, not a
    PR's evidence, and must never have a `staging/pulumi-test-io` status
    written at its SHA — the same filter `staging-status.yml`'s job `if`
    applies to the live event.
    """
    cutoff = now - timedelta(hours=lookback_hours)
    out = []
    for r in runs:
        if r.get("event") != "workflow_dispatch" or r.get("status") != "completed":
            continue
        branch = r.get("head_branch") or ""
        if not branch or branch == default_branch:
            continue
        if not r.get("head_sha"):
            continue
        ts = _parse_ts(r.get("updated_at") or r.get("created_at"))
        if ts is None or ts < cutoff:
            continue
        out.append(r)
    return out


def group_by_head(runs: list[dict]) -> dict[str, dict]:
    """One fact per head SHA: a success anywhere in the group wins.

    Two deploys of one SHA — a flake and the retry that fixed it — are not
    two verdicts. `_staging_evidence` accepts any successful run at the head,
    so a group that contains one is green, whatever ran after it.
    """
    grouped: dict[str, dict] = {}
    # Ascending by time, so a later run simply overwrites an earlier one —
    # except that a success already recorded is never displaced.
    for r in sorted(runs, key=lambda r: r.get("updated_at") or ""):
        sha = r["head_sha"]
        current = grouped.get(sha)
        if current is not None and current["conclusion"] == "success":
            continue
        grouped[sha] = {
            "conclusion": r.get("conclusion") or "",
            "branch": r.get("head_branch") or "",
            "run_id": r.get("id"),
            "run_url": r.get("html_url") or "",
            "run": r,
        }
    return grouped


def existing_verdict(statuses: list[dict]) -> str | None:
    """The state of the newest AUTHORIZED staging status, or None.

    Unauthorized statuses are skipped rather than trusted: a commit status
    needs only push access to write, and treating a hand-written one as
    "already finalized" would let anyone stop the sweep from recording the
    real verdict. sentinel.py applies the same rule when it reads one as
    evidence.
    """
    for s in statuses:  # the statuses endpoint returns newest first
        if s.get("context") != STAGING_STATUS_CONTEXT:
            continue
        if ((s.get("creator") or {}).get("login") or "") not in STAGING_STATUS_WRITERS:
            continue
        return s.get("state")
    return None


def open_pr_for_branch(gh: GhClient, branch: str) -> dict | None:
    """The open PR whose head is `branch`, or None when there genuinely is none.

    `workflow_run.pull_requests[]` is not available here (there is no event),
    and the head branch is the handle both deploy lanes dispatch at, so this
    is the same resolution `staging-status.yml` does.

    A failed lookup RAISES rather than returning None: "no open PR" lets the
    sweep write the status, and a status written after a lookup that merely
    hiccuped would seal the SHA without the Sentinel ever being poked.
    """
    owner = gh.repo.split("/", 1)[0]
    prs = gh.get(f"repos/{gh.repo}/pulls",
                 {"state": "open", "head": f"{owner}:{branch}"}) or []
    return prs[0] if prs else None


def sweep(gh: GhClient, *, default_branch: str, now: datetime,
          lookback_hours: int = DEFAULT_LOOKBACK_HOURS,
          poke_sentinel: bool = True) -> dict:
    """Finalize every dispatched staging deploy the cascade did not report."""
    try:
        data = gh.get(
            f"repos/{gh.repo}/actions/workflows/{STAGING_WORKFLOW_FILE}/runs",
            {"per_page": RUN_PAGE_SIZE},
        ) or {}
    except Exception as exc:  # noqa: BLE001 — a hiccup is one skipped cycle
        log(f"::warning::could not list staging deploy runs: {exc}")
        return {"scanned": 0, "finalized": [], "skipped": [], "error": str(exc)}

    runs = data.get("workflow_runs", []) if isinstance(data, dict) else []
    grouped = group_by_head(candidate_runs(
        runs, default_branch=default_branch, now=now, lookback_hours=lookback_hours))

    record: dict = {"scanned": len(grouped), "finalized": [], "skipped": []}
    for sha, fact in sorted(grouped.items(), key=lambda kv: kv[1]["run"].get("updated_at") or ""):
        state, description, is_success = verdict_for(fact["conclusion"])
        try:
            statuses = gh.commit_statuses(sha)
        except Exception as exc:  # noqa: BLE001 — unreadable evidence: skip, don't guess
            log(f"::warning::could not read statuses at {sha[:9]}: {exc}")
            record["skipped"].append({"sha": sha, "reason": "statuses-unreadable"})
            continue
        if existing_verdict(statuses) == state:
            record["skipped"].append({"sha": sha, "reason": "already-recorded", "state": state})
            continue

        entry = {"sha": sha, "branch": fact["branch"], "run_id": fact["run_id"],
                 "state": state, "poked": None}

        # Poke BEFORE the status write: the status is this sweep's
        # idempotence key, so sealing it before the poke lands would make a
        # failed poke permanent. G4 is only re-scored when the Sentinel runs.
        if is_success and poke_sentinel:
            try:
                pr = open_pr_for_branch(gh, fact["branch"])
            except Exception as exc:  # noqa: BLE001 — retried next cycle
                log(f"::warning::could not look up the open PR for {fact['branch']}: {exc}")
                record["skipped"].append({"sha": sha, "reason": "pr-lookup-failed"})
                continue
            if pr is None:
                entry["poked"] = "no-open-pr"
            elif ((pr.get("head") or {}).get("sha") or "") != sha:
                # The head moved. G4 asks about the CURRENT head, the auto
                # lane has already dispatched a deploy for it, and the push
                # itself re-ran the Sentinel — a poke here would re-score a
                # head nobody is waiting on.
                entry["poked"] = "stale-head"
            else:
                try:
                    gh.dispatch_workflow(SENTINEL_WORKFLOW_FILE, default_branch,
                                         {"pr_number": str(pr["number"])})
                    entry["poked"] = pr["number"]
                except Exception as exc:  # noqa: BLE001 — retried next cycle
                    log(f"::warning::could not poke the Sentinel for #{pr['number']}: {exc}")
                    record["skipped"].append({"sha": sha, "reason": "poke-failed"})
                    continue

        target_url = DEPLOYED_SITE_URL if is_success else fact["run_url"]
        try:
            gh.post(f"repos/{gh.repo}/statuses/{sha}", {
                "state": state, "context": STAGING_STATUS_CONTEXT,
                "target_url": target_url, "description": description,
            })
        except Exception as exc:  # noqa: BLE001 — the run record is the evidence
            log(f"::warning::could not write the staging status at {sha[:9]}: {exc}")
            record["skipped"].append({"sha": sha, "reason": "status-write-failed"})
            continue

        log(f"{STAGING_STATUS_CONTEXT} = {state} at {sha[:9]} "
            f"({fact['branch']}, run {fact['run_id']}, poked={entry['poked']})")
        record["finalized"].append(entry)
    return record


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--repo")
    parser.add_argument("--default-branch", default="master")
    parser.add_argument("--lookback-hours", type=int, default=DEFAULT_LOOKBACK_HOURS)
    parser.add_argument("--dry-run", action="store_true",
                        help="resolve everything, send no status and no poke")
    parser.add_argument("--no-poke", action="store_true",
                        help="write statuses only; never dispatch the Sentinel")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        sys.path.insert(0, str(HERE))
        import test_staging_sweep  # noqa: PLC0415

        return test_staging_sweep.run_standalone()

    if not args.repo:
        parser.error("--repo is required")

    gh = GhClient(args.repo)
    if args.dry_run:
        gh = gh.dry()
    record = sweep(gh, default_branch=args.default_branch,
                   now=datetime.now(timezone.utc),
                   lookback_hours=args.lookback_hours,
                   poke_sentinel=not args.no_poke)
    if args.dry_run:
        record["dry_run"] = True
        record["would_write"] = gh.writes
    print(json.dumps(record, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

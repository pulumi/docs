#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Collect open PRs and the full issue backlog for the weekly #docs-ops digest.

Deterministic collection only -- no model, no prose, no grouping. Emits a
single JSON object to stdout that weekly-digest.yml feeds to one Claude
synthesis call. Shells out to `gh`; runs via `uv run` in the workflow.

Mirrors the query patterns in .claude/commands/dashboard/scripts/dashboard.sh
but broadened: the issue query is the whole open backlog, not assignee-scoped.
"""

import importlib.util
import json
import os
import subprocess
import sys
import tempfile
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO = "pulumi/docs"
BOT_LOGINS = {"pulumi-bot", "dependabot[bot]"}
WINDOW_DAYS = 7
NOW = datetime.now(timezone.utc)
OUTCOME_SCRAPER = (
    Path(__file__).resolve().parents[2]
    / ".claude/commands/docs-review/scripts/scrape-review-outcomes.py"
)

# v3 SLA-sweep state lives in the same content-review ledger bucket as
# everything collect_review_outcomes/review-admin.py read, under pr-review/
# (see scripts/review-v3/README.md). No stack-output wiring exists in this
# script (unlike the credentialed record jobs) -- discover the bucket by
# name prefix, review-admin.py's own technique, or accept it pre-resolved
# via env (same variable name that tool uses, so one env setting works for
# both).
LEDGER_BUCKET_ENV = "CONTENT_REVIEW_LEDGER_BUCKET"
LEDGER_BUCKET_PREFIX = "content-review-ledger-"


def run_gh(args):
    """Run a gh command; return stdout, or "" on failure (logged to stderr)."""
    try:
        proc = subprocess.run(
            ["gh", *args], capture_output=True, text=True, check=True
        )
        return proc.stdout
    except subprocess.CalledProcessError as exc:
        sys.stderr.write(f"warning: gh {' '.join(args)} failed: {exc.stderr.strip()}\n")
        return ""


def gh_json(args):
    """Run a gh command that emits JSON; parse it, or return [] on failure."""
    out = run_gh(args)
    try:
        return json.loads(out) if out.strip() else []
    except json.JSONDecodeError:
        sys.stderr.write(f"warning: could not parse JSON from gh {' '.join(args)}\n")
        return []


def days_since(iso):
    """Whole days between an ISO-8601 timestamp and now; None if unparseable."""
    if not iso:
        return None
    try:
        dt = datetime.fromisoformat(iso.replace("Z", "+00:00"))
    except ValueError:
        return None
    return (NOW - dt).days


def rollup_state(pr):
    """Reduce a PR's statusCheckRollup to green | red | pending | none.

    statusCheckRollup mixes CheckRun nodes (status/conclusion) and legacy
    StatusContext nodes (state). Red wins over pending wins over green.
    """
    rollup = pr.get("statusCheckRollup") or []
    if not rollup:
        return "none"
    states = set()
    for check in rollup:
        if check.get("conclusion"):
            states.add(check["conclusion"].upper())
        elif check.get("state"):
            states.add(check["state"].upper())
        elif check.get("status"):
            states.add(check["status"].upper())
    if states & {"FAILURE", "ERROR", "TIMED_OUT", "CANCELLED", "ACTION_REQUIRED"}:
        return "red"
    if states & {"IN_PROGRESS", "QUEUED", "PENDING", "WAITING", "REQUESTED", "EXPECTED"}:
        return "pending"
    if states & {"SUCCESS", "NEUTRAL", "SKIPPED"}:
        return "green"
    return "none"


def shape_prs(raw):
    """Pure transform: raw `gh pr list` objects -> digest PR records."""
    prs = []
    for pr in raw:
        login = (pr.get("author") or {}).get("login", "")
        prs.append(
            {
                "number": pr["number"],
                "title": pr["title"],
                "author": login,
                "age_days": days_since(pr.get("createdAt")),
                "updated_days": days_since(pr.get("updatedAt")),
                "labels": [lbl["name"] for lbl in pr.get("labels", [])],
                "isDraft": pr.get("isDraft", False),
                "checks": rollup_state(pr),
                "is_bot": login in BOT_LOGINS,
            }
        )
    return prs


def shape_issues(raw):
    """Pure transform: raw `gh issue list` objects -> backlog summary.

    Surfaces only what the digest needs: a count, the issues opened this week,
    and the three staleest open issues. The full list is never emitted.
    """
    enriched = []
    for issue in raw:
        login = (issue.get("author") or {}).get("login", "")
        enriched.append(
            {
                "number": issue["number"],
                "title": issue["title"],
                "author": login,
                "age_days": days_since(issue.get("createdAt")),
                "needs_triage": "needs-triage"
                in [lbl["name"] for lbl in issue.get("labels", [])],
            }
        )
    aged = [i for i in enriched if i["age_days"] is not None]
    new_this_week = sorted(
        (i for i in aged if i["age_days"] < WINDOW_DAYS),
        key=lambda x: x["age_days"],
    )
    oldest_open = sorted(aged, key=lambda x: x["age_days"], reverse=True)[:3]
    return {
        "all_open_count": len(enriched),
        "new_this_week": [
            {k: i[k] for k in ("number", "title", "author", "age_days", "needs_triage")}
            for i in new_this_week
        ],
        "oldest_open": [
            {k: i[k] for k in ("number", "title", "age_days")} for i in oldest_open
        ],
    }


def shape_ci_health(raw):
    """Pure transform: raw `gh run list` objects -> CI health over last 24h.

    Thresholds mirror dashboard.sh: 0 failures and >=95% success -> HEALTHY;
    <=2 failures and >=85% success -> WARNING; otherwise CRITICAL.
    """
    cutoff = NOW - timedelta(hours=24)
    recent = []
    for run in raw:
        dt = run.get("createdAt")
        if not dt:
            continue
        try:
            when = datetime.fromisoformat(dt.replace("Z", "+00:00"))
        except ValueError:
            continue
        if when >= cutoff:
            recent.append(run)
    if not recent:
        return {"status": "UNKNOWN", "success_rate": None, "failures": 0, "total": 0}
    completed = [r for r in recent if r.get("conclusion")]
    failures = sum(1 for r in completed if r.get("conclusion") == "failure")
    successes = sum(
        1 for r in completed if r.get("conclusion") in ("success", "skipped")
    )
    rate = round(100 * successes / len(completed)) if completed else None
    if failures == 0 and (rate is None or rate >= 95):
        status = "HEALTHY"
    elif failures <= 2 and rate is not None and rate >= 85:
        status = "WARNING"
    else:
        status = "CRITICAL"
    return {
        "status": status,
        "success_rate": rate,
        "failures": failures,
        "total": len(recent),
    }


def collect_review_outcomes(since):
    """Pre-merge review outcome telemetry for PRs closed in the window.

    Delegates to scrape-review-outcomes.py (issue #20078 §3.2), which derives
    per-finding outcomes from each closed PR's pinned review comments. Only
    the window aggregate rides into the digest — per-PR finding lists stay in
    the scraper. Degrades to {"available": False} on any failure so a scraper
    or gh outage mutes this section without killing the digest; the aggregate
    itself carries `prs_no_review_data` / `prs_parse_low` so partial
    degradation is visible rather than silent.
    """
    try:
        proc = subprocess.run(
            [sys.executable, str(OUTCOME_SCRAPER), "--closed-since", since, "--repo", REPO],
            capture_output=True, text=True, check=True,
        )
        aggregate = json.loads(proc.stdout).get("aggregate")
    except (subprocess.CalledProcessError, FileNotFoundError, json.JSONDecodeError) as exc:
        detail = getattr(exc, "stderr", "") or str(exc)
        sys.stderr.write(f"warning: review-outcome scrape failed: {str(detail).strip()[:500]}\n")
        return {"available": False}
    if not isinstance(aggregate, dict):
        return {"available": False}
    return {"available": True, "since": since, **aggregate}


def resolve_ledger_bucket() -> str | None:
    """The content-review ledger bucket name, or None on any failure to
    resolve it (no explicit env override, `aws` missing/unauthenticated, an
    ambiguous or empty prefix match) -- collect_v3_ops() treats None as the
    same "unavailable" degradation collect_review_outcomes() uses for a
    scraper failure."""
    explicit = os.environ.get(LEDGER_BUCKET_ENV, "").strip()
    if explicit:
        return explicit
    try:
        proc = subprocess.run(
            ["aws", "s3api", "list-buckets", "--query",
             f"Buckets[?starts_with(Name, '{LEDGER_BUCKET_PREFIX}')].Name", "--output", "json"],
            capture_output=True, text=True,
        )
    except FileNotFoundError:
        sys.stderr.write("warning: aws CLI not found; v3 ops summary unavailable\n")
        return None
    if proc.returncode != 0:
        sys.stderr.write(f"warning: bucket discovery failed: {proc.stderr.strip()[:300]}\n")
        return None
    try:
        names = json.loads(proc.stdout or "[]")
    except json.JSONDecodeError:
        return None
    if len(names) == 1:
        return names[0]
    sys.stderr.write(f"warning: {len(names)} bucket(s) match '{LEDGER_BUCKET_PREFIX}*'; "
                      f"set {LEDGER_BUCKET_ENV} explicitly\n")
    return None


def _bulk_accept_keys() -> tuple[str, str]:
    """(bulk_key, accepted_key) -- the outcome-count field names for a
    bulk `/resolve all ...` answer vs. any adjudicated accept/defer/n-a
    answer, per scrape-review-outcomes.py's V3_ONLY_OUTCOME_KEYS.

    Imported by path (loose coupling, not a hard dependency -- see
    OUTCOME_SCRAPER) purely to validate the literal names below still exist
    in that module's vocabulary; any import failure or a renamed key just
    logs a warning and keeps the literals, since a missing key already
    degrades cleanly to a 0 count downstream.
    """
    bulk_key, accepted_key = "bulk_accepted", "author_accepted"
    try:
        spec = importlib.util.spec_from_file_location("_scrape_outcomes_for_digest", OUTCOME_SCRAPER)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        keys = set(getattr(mod, "V3_ONLY_OUTCOME_KEYS", ()))
        if bulk_key not in keys or accepted_key not in keys:
            sys.stderr.write(
                "warning: scrape-review-outcomes.py's V3_ONLY_OUTCOME_KEYS no longer names "
                f"{bulk_key!r}/{accepted_key!r}; bulk-accept rate may be stale\n"
            )
    except Exception as exc:  # noqa: BLE001 -- never let a key-vocabulary check break the digest
        sys.stderr.write(f"warning: could not import scrape-review-outcomes.py for key validation: {exc}\n")
    return bulk_key, accepted_key


def collect_v3_ops(since: str, review_outcomes: dict) -> dict:
    """v3 SLA-sweep operational summary for the trailing window: escalations
    (by lane/role), author-staleness warns and closes, waives, and a
    bulk-accept rate.

    Syncs `pr-review/state/`, `pr-review/runs/`, and `pr-review/waives/`
    from the ledger bucket (see scripts/review-v3/README.md and
    sla-sweep.py's module docstring for the run-record shape) and reduces
    the run records in-window. The bulk-accept rate is NOT a second scrape
    -- it's derived from the `review_outcomes` aggregate collect_review_outcomes()
    already fetched this run, so a missing/unavailable outcomes block just
    yields a 0/0 -> None rate rather than another `gh` round-trip.

    Same degradation contract as collect_review_outcomes(): any failure to
    resolve the bucket or sync its prefixes -> {"available": False}, a loud
    signal for the synthesis prompt to render, never a silently dropped
    section.
    """
    bucket = resolve_ledger_bucket()
    if not bucket:
        return {"available": False}

    with tempfile.TemporaryDirectory() as tmp:
        cache = Path(tmp)
        load_bearing_ok = True
        for prefix in ("state", "runs", "waives"):
            proc = subprocess.run(
                ["aws", "s3", "sync", f"s3://{bucket}/pr-review/{prefix}/",
                 str(cache / prefix), "--no-progress"],
                capture_output=True, text=True,
            )
            if proc.returncode != 0:
                # waives/ may legitimately not exist yet (nobody has waived
                # a v3 gate); only state/ and runs/ not syncing is fatal to
                # this section.
                if prefix in ("state", "runs"):
                    sys.stderr.write(
                        f"warning: aws s3 sync failed for pr-review/{prefix}/: {proc.stderr.strip()[:300]}\n"
                    )
                    load_bearing_ok = False
        if not load_bearing_ok:
            return {"available": False}

        escalations_by_role: Counter = Counter()
        warns = 0
        closes = 0
        runs_dir = cache / "runs"
        for run_file in sorted(runs_dir.rglob("*.json")) if runs_dir.is_dir() else []:
            try:
                record = json.loads(run_file.read_text())
            except (OSError, json.JSONDecodeError):
                continue
            if (record.get("run_at") or "")[:10] < since:
                continue
            for pr_action in record.get("actions", []):
                if pr_action.get("kind") == "author":
                    a = pr_action.get("action") or {}
                    if a.get("type") == "warn":
                        warns += 1
                    elif a.get("type") == "close":
                        closes += 1
                elif pr_action.get("kind") == "reviewer":
                    for a in pr_action.get("actions") or []:
                        if a.get("type") == "escalate":
                            escalations_by_role[a.get("role") or "unknown"] += 1

        waives_dir = cache / "waives"
        waive_count = sum(1 for f in waives_dir.rglob("*.json")) if waives_dir.is_dir() else 0

    bulk_key, accepted_key = _bulk_accept_keys()
    human = {}
    if review_outcomes.get("available"):
        human = (review_outcomes.get("outcomes") or {}).get("human") or {}
    bulk_accepted = human.get(bulk_key, 0)
    author_accepted = human.get(accepted_key, 0)
    bulk_accept_rate = round(100 * bulk_accepted / author_accepted) if author_accepted else None

    return {
        "available": True,
        "since": since,
        "escalations_total": sum(escalations_by_role.values()),
        "escalations_by_role": dict(escalations_by_role),
        "warns": warns,
        "closes": closes,
        "waives": waive_count,
        "bulk_accepted": bulk_accepted,
        "author_accepted": author_accepted,
        "bulk_accept_rate": bulk_accept_rate,
    }


def search_count(qualifier):
    """Exact issue count via the search API's total_count (REST, not GraphQL)."""
    out = run_gh(
        [
            "api",
            "-X",
            "GET",
            "search/issues",
            "-f",
            f"q=repo:{REPO} {qualifier}",
            "-f",
            "per_page=1",
            "--jq",
            ".total_count",
        ]
    )
    try:
        return int(out.strip())
    except (ValueError, AttributeError):
        return None


def main():
    cutoff = (NOW - timedelta(days=WINDOW_DAYS)).date().isoformat()
    prs = shape_prs(
        gh_json(
            [
                "pr", "list", "--repo", REPO, "--state", "open", "--limit", "200",
                "--json",
                "number,title,author,createdAt,updatedAt,labels,isDraft,statusCheckRollup",
            ]
        )
    )
    issues = shape_issues(
        gh_json(
            [
                "issue", "list", "--repo", REPO, "--state", "open", "--limit", "500",
                "--json", "number,title,author,createdAt,updatedAt,labels",
            ]
        )
    )
    issues["opened_last_7d"] = search_count(f"is:issue created:>={cutoff}")
    issues["closed_last_7d"] = search_count(f"is:issue closed:>={cutoff}")
    ci_health = shape_ci_health(
        gh_json(
            [
                "run", "list", "--repo", REPO, "--limit", "50",
                "--json", "status,conclusion,createdAt",
            ]
        )
    )
    review_outcomes = collect_review_outcomes(cutoff)
    v3_ops = collect_v3_ops(cutoff, review_outcomes)
    digest = {
        "window_days": WINDOW_DAYS,
        "prs": prs,
        "issues": issues,
        "ci_health": ci_health,
        "review_outcomes": review_outcomes,
        "v3_ops": v3_ops,
    }
    json.dump(digest, sys.stdout, indent=2)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()

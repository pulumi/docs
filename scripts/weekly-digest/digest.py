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

import json
import subprocess
import sys
from datetime import datetime, timedelta, timezone

REPO = "pulumi/docs"
BOT_LOGINS = {"pulumi-bot", "dependabot[bot]"}
WINDOW_DAYS = 7
NOW = datetime.now(timezone.utc)


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
            {k: i[k] for k in ("number", "title", "author", "age_days")}
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
    digest = {
        "window_days": WINDOW_DAYS,
        "prs": prs,
        "issues": issues,
        "ci_health": ci_health,
    }
    json.dump(digest, sys.stdout, indent=2)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()

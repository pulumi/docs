#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml"]
# ///
"""Collect open PRs and the full issue backlog for the weekly #docs-ops digest.

Deterministic collection only -- no model, no prose, no grouping. Emits a
single JSON object to stdout that render.py turns into the Slack message
(rank.py asks the model to order the "needs a human" list; nothing else is
model-written). Shells out to `gh`; runs via `uv run` in the workflow.

The SLA verdicts come from scripts/review-v3/sla-sweep.py run with
--dry-run: the sweep's own evaluator, read-only, whether or not the
scheduled sweep (REVIEW_V3_SLA) is switched on. pyyaml is here for that
subprocess, which loads .github/review-routing.yml.

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

SLA_SWEEP = Path(__file__).resolve().parents[2] / "scripts/review-v3/sla-sweep.py"
ROUTING_CONFIG = Path(__file__).resolve().parents[2] / ".github/review-routing.yml"

# Operational switches: repo variables that turn a scheduled lane on or off.
# The workflow passes the raw values in DIGEST_VARS (JSON; "" = unset), since
# GITHUB_TOKEN can't read repo variables. Each entry mirrors how the owning
# workflow reads its variable -- the semantics differ, and a lane that
# defaults ON when unset must not be reported off (see blog-review-index.yml
# and review-sla-sweep.yml headers for the `== '1'` vs `!= '0'` split).
#   (label, variable, rule, default) where rule is:
#     "eq1"   on only when the value is exactly "1"
#     "ne0"   on unless the value is exactly "0" (count lanes: value = per-run count)
#     "mode"  sentinel: "1" enforcing, "report" report-only, else off
SWITCHES = [
    ("SLA sweep", "REVIEW_V3_SLA", "eq1", None),
    ("Sentinel", "REVIEW_V3_SENTINEL", "mode", None),
    ("content review", "CONTENT_REVIEW_COUNT", "ne0", "3"),
    ("glow-up", "GLOWUP_COUNT", "ne0", "1"),
    ("blog review index", "BLOG_REVIEW_COUNT", "ne0", "5"),
    ("claims re-verify", "CLAIMS_REVERIFY_COUNT", "ne0", "25"),
    ("brand sync", "BRAND_SYNC_ENABLED", "ne0", None),
]


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


FAILED_CONCLUSIONS = {"failure", "timed_out", "startup_failure"}


def shape_workflow_failures(raw):
    """Pure transform: raw `gh run list` objects (scheduled runs plus pushes
    to master, trailing window) -> per-workflow failure counts, worst first.

    Only failed workflows are listed; `total_runs` is the denominator so a
    quiet week still reads as "0 of N" rather than as missing data.
    """
    runs = [r for r in raw if r.get("status") == "completed"]
    by_wf = {}
    for r in runs:
        name = r.get("workflowName") or "unknown"
        entry = by_wf.setdefault(name, {"workflow": name, "runs": 0, "failures": 0, "last_failure_url": None})
        entry["runs"] += 1
        if r.get("conclusion") in FAILED_CONCLUSIONS:
            entry["failures"] += 1
            if entry["last_failure_url"] is None:  # gh lists newest first
                entry["last_failure_url"] = r.get("url")
    failing = sorted((e for e in by_wf.values() if e["failures"]),
                     key=lambda e: (-e["failures"], e["workflow"]))
    return {"total_runs": len(runs), "failing": failing}


def shape_switches(raw_vars):
    """Pure transform: {VAR: value} (None = not passed, "" = unset) -> one
    record per SWITCHES entry. `state` is on | off | report | unknown;
    unknown means the value wasn't passed at all (a local run without
    DIGEST_VARS), which the renderer must not dress up as "off"."""
    out = []
    for label, var, rule, default in SWITCHES:
        value = raw_vars.get(var) if isinstance(raw_vars, dict) else None
        if value is None:
            state = "unknown"
        elif rule == "eq1":
            state = "on" if value == "1" else "off"
        elif rule == "mode":
            state = {"1": "on", "report": "report"}.get(value, "off")
        else:
            state = "off" if value == "0" else "on"
        out.append({"label": label, "var": var, "state": state,
                    "value": (value or default) if state == "on" and rule == "ne0" else None})
    return out


def collect_switches():
    raw = os.environ.get("DIGEST_VARS")
    if not raw:
        return shape_switches(None)
    try:
        return shape_switches(json.loads(raw))
    except json.JSONDecodeError:
        sys.stderr.write("warning: DIGEST_VARS is not valid JSON; switches unknown\n")
        return shape_switches(None)


def shape_sla(record, config, enabled):
    """Pure transform: a sla-sweep.py --dry-run run record -> per-PR
    verdicts the renderer groups. Nothing here re-decides policy: kind,
    waited/SLA business days, idle days, and closes_in_days all come from
    the sweep's own evaluator; this only flattens and labels them.
    """
    verdicts = []
    for entry in record.get("actions") or []:
        kind = entry.get("kind")
        if kind == "author":
            a = entry.get("action") or {}
            verdicts.append({
                "pr": entry["pr"], "kind": "author",
                "idle_days": a.get("idle_days"),
                "undecided_count": a.get("undecided_count"),
                "closes_in_days": a.get("closes_in_days"),
                "warned": a.get("type") == "none" and "warn_age_days" in a,
                "abandoned": (a.get("idle_days") or 0) > config["warn_days"],
            })
        elif kind == "reviewer":
            roles = [
                {"role": a["role"], "waited": a["waited_business_days"], "sla": a["sla_business_days"],
                 "escalate_to": config["escalate_to"].get(a["role"])}
                for a in entry.get("actions") or [] if a.get("role")
            ]
            overdue = [r for r in roles if r["waited"] > r["sla"]]
            verdicts.append({"pr": entry["pr"], "kind": "reviewer", "roles": roles, "overdue": overdue})
    return {"available": True, "enabled": enabled, "policy": {
        "warn_days": config["warn_days"], "close_days": config["close_days"]}, "verdicts": verdicts}


def load_sla_policy():
    """The `author_staleness` and `sla` blocks of review-routing.yml, via
    the same loader the sweep uses (routing.load_config), so the digest
    labels verdicts with the thresholds the sweep enforced."""
    sys.path.insert(0, str(SLA_SWEEP.parent))
    import routing  # noqa: PLC0415 -- lives beside sla-sweep.py

    cfg = routing.load_config(str(ROUTING_CONFIG))
    return {
        "warn_days": cfg.author_staleness["warn_days"],
        "close_days": cfg.author_staleness["close_days"],
        "escalate_to": {role: v.get("escalate_to") for role, v in cfg.sla.items()},
    }


def collect_sla(enabled, ledger_bucket):
    """Run the SLA sweep's evaluator read-only and shape its verdicts.

    `--dry-run` is the sweep's own no-mutation contract (no comments,
    labels, closes, Slack, or state writes; it prints the run record it
    would have acted on). With the ledger bucket resolved, the sweep reads
    its per-PR state from S3, so a PR it already warned shows the real
    remaining notice. Degrades to {"available": False} like every other
    collector here.
    """
    try:
        policy = load_sla_policy()
    except Exception as exc:  # noqa: BLE001 -- a config problem mutes this section, not the digest
        sys.stderr.write(f"warning: could not load review-routing.yml: {exc}\n")
        return {"available": False, "enabled": enabled}
    env = dict(os.environ)
    if ledger_bucket:
        env["PR_REVIEW_EVIDENCE_URI"] = f"s3://{ledger_bucket}/pr-review"
    try:
        with tempfile.TemporaryDirectory() as tmp:
            proc = subprocess.run(
                [sys.executable, str(SLA_SWEEP), "--repo", REPO, "--dry-run", "--state-dir", tmp],
                capture_output=True, text=True, env=env, timeout=900,
            )
        if proc.returncode != 0:
            raise RuntimeError(proc.stderr.strip()[-500:])
        record = json.loads(proc.stdout)
    except (OSError, RuntimeError, subprocess.TimeoutExpired, json.JSONDecodeError) as exc:
        sys.stderr.write(f"warning: sla-sweep dry-run failed: {str(exc)[:500]}\n")
        return {"available": False, "enabled": enabled}
    return shape_sla(record, policy, enabled)


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
    bulk accept-everything answer vs. any adjudicated accept/defer/n-a
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


def collect_v3_ops(since: str, review_outcomes: dict, bucket: str | None) -> dict:
    """v3 SLA-sweep operational summary for the trailing window: escalations
    (by lane/role), author-staleness warns and closes, waives, and a
    bulk-accept rate.

    Syncs `pr-review/runs/` and `pr-review/waives/` from the ledger bucket
    (`pr-review/state/` is the sweep's idempotency ledger and carries nothing
    this summary reads, so it is neither synced nor load-bearing) (see scripts/review-v3/README.md and
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
    if not bucket:
        return {"available": False}

    with tempfile.TemporaryDirectory() as tmp:
        cache = Path(tmp)
        load_bearing_ok = True
        for prefix in ("runs", "waives"):
            proc = subprocess.run(
                ["aws", "s3", "sync", f"s3://{bucket}/pr-review/{prefix}/",
                 str(cache / prefix), "--no-progress"],
                capture_output=True, text=True,
            )
            if proc.returncode != 0:
                # waives/ may legitimately not exist yet (nobody has waived
                # a v3 gate); only runs/ not syncing is fatal to this section.
                if prefix == "runs":
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


def throughput(start, end=None):
    """Opened / merged / closed-unmerged PR counts and opened / closed issue
    counts for [start, end) -- end None means "through now". Exact counts
    from the search API; a failed query is None, never 0."""
    rng = f">={start}" if end is None else f"{start}..{end}"
    return {
        "prs_opened": search_count(f"is:pr created:{rng}"),
        "prs_merged": search_count(f"is:pr merged:{rng}"),
        "prs_closed": search_count(f"is:pr is:unmerged closed:{rng}"),
        "issues_opened": search_count(f"is:issue created:{rng}"),
        "issues_closed": search_count(f"is:issue closed:{rng}"),
    }


def main():
    cutoff_dt = NOW - timedelta(days=WINDOW_DAYS)
    cutoff = cutoff_dt.date().isoformat()
    prev_start = (cutoff_dt - timedelta(days=WINDOW_DAYS)).date().isoformat()
    prev_end = (cutoff_dt - timedelta(days=1)).date().isoformat()
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
    this_week = throughput(cutoff)
    # Kept for readers of the old field names (the backlog delta).
    issues["opened_last_7d"] = this_week["issues_opened"]
    issues["closed_last_7d"] = this_week["issues_closed"]
    runs = []
    for event_args in (["--event", "schedule"], ["--event", "push", "--branch", "master"]):
        runs += gh_json(
            [
                "run", "list", "--repo", REPO, *event_args, "--created", f">={cutoff}",
                "--limit", "1000", "--json", "workflowName,status,conclusion,createdAt,url",
            ]
        )
    switches = collect_switches()
    sweep_state = next((sw["state"] for sw in switches if sw["var"] == "REVIEW_V3_SLA"), "unknown")
    bucket = resolve_ledger_bucket()
    review_outcomes = collect_review_outcomes(cutoff)
    v3_ops = collect_v3_ops(cutoff, review_outcomes, bucket)
    digest = {
        "generated_at": NOW.isoformat(),
        "window_days": WINDOW_DAYS,
        "prs": prs,
        "issues": issues,
        "throughput": {"this_week": this_week, "prev_week": throughput(prev_start, prev_end)},
        "workflow_failures": shape_workflow_failures(runs),
        "switches": switches,
        "sla": collect_sla(sweep_state, bucket),
        "review_outcomes": review_outcomes,
        "v3_ops": v3_ops,
    }
    json.dump(digest, sys.stdout, indent=2)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()

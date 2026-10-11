#!/usr/bin/env python3
"""Browse and export the S3 review/state ledgers from one place.

Several automated processes persist state as small JSON objects in two private
S3 buckets, none of it human-browsable without pulling objects one at a time:

  content-review-ledger-* (shared bucket, one prefix per producer)
    ledger/<slug>.json            existing-content docs review outcomes
    claims/<slug>.json            fact-check claim extraction + verdicts
    blog-review/ledger/…          blog known-issues index (per post)
    blog-review/runs/<date>/…     per-run blog review findings
    blog-review/index/_summary.json  aggregate summary
    health/state.json             selection-signal health
    pr-review/<pr>/latest.json    v3 PR review evidence (findings + dispositions)
    pr-review/state/<pr>.json     SLA-sweep state (warns/escalations/closes)
    pr-review/runs/<date>/…       per-sweep SLA action records
    pr-review/waives/…            v3 merge-gate waive log
  social-post-state-* posted-social.json / posted.json
                                  per-post social publish timestamps

This tool syncs both buckets into a local cache and then works entirely
offline: console summaries, filterable listings, per-article paper trails,
DWH-ready CSV/JSONL exports, and a self-contained HTML dashboard. It is
read-only — it never writes to S3. For ledger *version history* (how a record
changed over time), see scripts/content-review/reconstruct-ledger-history.py.

Usage:

    review-admin.py sync                  # pull both buckets into the cache
    review-admin.py summary               # console overview of everything
    review-admin.py list claims --verdict contradicted
    review-admin.py show docs-iac-get-started-aws-configure
    review-admin.py export --format csv
    review-admin.py html --open

Needs the AWS CLI with read access to the buckets (sync only; every other
subcommand reads the local cache). Bucket names are Pulumi auto-named — they
are discovered by name prefix, or set CONTENT_REVIEW_LEDGER_BUCKET /
SOCIAL_STATE_BUCKET explicitly. Run `--self-test` for an offline smoke test.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import subprocess
import sys
import tempfile
import webbrowser
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

CONTENT_BUCKET_ENV = "CONTENT_REVIEW_LEDGER_BUCKET"
SOCIAL_BUCKET_ENV = "SOCIAL_STATE_BUCKET"
CONTENT_BUCKET_PREFIX = "content-review-ledger-"
SOCIAL_BUCKET_PREFIX = "social-post-state-"
CACHE_ENV = "REVIEW_ADMIN_CACHE"
CACHE_DIRNAME = ".review-admin-cache"

DOMAINS = ("docs", "claims", "blog", "social", "pr-review")

# Preferred column order for exports; unknown fields are appended after these.
DOCS_COLUMNS = [
    "slug", "path", "lane", "status", "tier", "score", "fixes",
    "skipped_findings", "attempts", "clarity_flag", "retirement",
    "pr_number", "pr", "head_sha", "monthly_visits", "traffic_available",
    "signals_available", "reviewed_at", "note",
]
CLAIM_COLUMNS = [
    "slug", "path", "claim_id", "type", "verdict", "confidence",
    "line_range", "volatile", "entity_key", "text", "evidence", "source",
    "commit", "model", "article_reviewed_at", "schema_version",
]
BLOG_COLUMNS = [
    "slug", "path", "lane", "status", "issues", "score", "post_date",
    "monthly_visits", "traffic_available", "signals_available", "attempts",
    "head_sha", "reviewed_at", "note", "schema_version",
]
BLOG_ISSUE_COLUMNS = [
    "slug", "path", "run_date", "post_date", "status", "noindex_signal",
    "issue_category", "issue_severity",
]
SOCIAL_COLUMNS = ["url", "platform", "posted_at", "failures", "source_file"]
PR_REVIEW_COLUMNS = [
    "pr", "head_sha", "blocking", "dispositions", "warns", "escalations",
    "closes", "last_sweep_action", "generated_at",
]


def log(msg: str) -> None:
    print(f"review-admin: {msg}")


def warn(msg: str) -> None:
    print(f"review-admin: {msg}", file=sys.stderr)


def die(msg: str) -> None:
    warn(msg)
    sys.exit(1)


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def cache_dir(args) -> Path:
    if getattr(args, "cache_dir", None):
        return Path(args.cache_dir)
    env = os.environ.get(CACHE_ENV, "").strip()
    if env:
        return Path(env)
    return repo_root() / CACHE_DIRNAME


# ---- sync -------------------------------------------------------------------


def aws(argv: list[str]) -> subprocess.CompletedProcess:
    try:
        return subprocess.run(["aws", *argv], capture_output=True, text=True)
    except FileNotFoundError:
        die("aws CLI not found on PATH — install it (or run inside the devcontainer)")


def credential_hint() -> str:
    profile = os.environ.get("AWS_PROFILE", "")
    lines = ["Could not talk to S3 — check your AWS credentials."]
    if profile:
        lines.append(f"Current AWS_PROFILE={profile}; if SSO, the token may have expired (refresh your SSO session).")
    else:
        lines.append("No AWS_PROFILE set — export the profile that has read access to the review buckets,")
        lines.append("e.g. one of the profiles in ~/.aws/credentials, plus AWS_DEFAULT_REGION.")
    return "\n".join(lines)


def resolve_bucket(env_var: str, prefix: str) -> str:
    explicit = os.environ.get(env_var, "").strip()
    if explicit:
        return explicit
    proc = aws(["s3api", "list-buckets",
                "--query", f"Buckets[?starts_with(Name, '{prefix}')].Name",
                "--output", "json"])
    if proc.returncode != 0:
        die(f"bucket discovery failed:\n{proc.stderr.strip()}\n{credential_hint()}")
    names = json.loads(proc.stdout or "[]")
    if len(names) == 1:
        return names[0]
    if not names:
        die(f"no bucket matching '{prefix}*' visible to these credentials; set {env_var} explicitly")
    die(f"multiple buckets match '{prefix}*' ({', '.join(names)}); set {env_var} to pick one")


def sync_prefix(uri: str, dest: Path) -> None:
    dest.mkdir(parents=True, exist_ok=True)
    proc = aws(["s3", "sync", uri, str(dest), "--delete", "--no-progress"])
    for line in (proc.stdout or "").splitlines():
        if line.strip():
            print(f"  {line.strip()}")
    if proc.returncode != 0:
        die(f"sync failed for {uri}:\n{proc.stderr.strip()}\n{credential_hint()}")


def cmd_sync(args) -> int:
    cache = cache_dir(args)
    content_bucket = resolve_bucket(CONTENT_BUCKET_ENV, CONTENT_BUCKET_PREFIX)
    social_bucket = resolve_bucket(SOCIAL_BUCKET_ENV, SOCIAL_BUCKET_PREFIX)
    log(f"syncing s3://{content_bucket} and s3://{social_bucket} -> {cache}")
    sync_prefix(f"s3://{content_bucket}/", cache / "content-review")
    sync_prefix(f"s3://{social_bucket}/", cache / "social")
    counts = {
        "content-review": sum(1 for _ in (cache / "content-review").rglob("*.json")),
        "social": sum(1 for _ in (cache / "social").rglob("*.json")),
    }
    meta = {
        "synced_at": utc_now().isoformat(timespec="seconds"),
        "buckets": {"content_review": content_bucket, "social": social_bucket},
        "objects": counts,
    }
    (cache / "sync-meta.json").write_text(json.dumps(meta, indent=2) + "\n")
    log(f"done: {counts['content-review']} content-review objects, {counts['social']} social objects")
    return 0


def read_sync_meta(cache: Path) -> dict | None:
    try:
        return json.loads((cache / "sync-meta.json").read_text())
    except (OSError, json.JSONDecodeError):
        return None


def describe_cache(cache: Path) -> str:
    meta = read_sync_meta(cache)
    if not meta:
        return f"cache {cache} has never been synced — run `review-admin.py sync` first"
    synced = meta.get("synced_at", "")
    try:
        age = utc_now() - datetime.fromisoformat(synced)
        hours = age.total_seconds() / 3600
        age_str = f"{hours / 24:.1f}d ago" if hours >= 48 else f"{hours:.1f}h ago"
    except ValueError:
        age_str = "unknown age"
    return f"cache: {cache} (synced {synced}, {age_str})"


def require_cache(args) -> Path:
    cache = cache_dir(args)
    if not (cache / "content-review").is_dir():
        die(f"no cache at {cache} — run `review-admin.py sync` first")
    print(describe_cache(cache))
    return cache


# ---- loaders ----------------------------------------------------------------


def load_json_dir(directory: Path) -> list[dict]:
    """All *.json records in a directory, each tagged with its _file."""
    records: list[dict] = []
    if not directory.is_dir():
        return records
    for f in sorted(directory.glob("*.json")):
        try:
            record = json.loads(f.read_text())
        except (OSError, json.JSONDecodeError):
            warn(f"unreadable JSON skipped: {f}")
            continue
        if isinstance(record, dict):
            record["_file"] = str(f)
            records.append(record)
    return records


def load_json_file(path: Path) -> dict | None:
    try:
        data = json.loads(path.read_text())
        return data if isinstance(data, dict) else None
    except (OSError, json.JSONDecodeError):
        return None


def load_docs(cache: Path) -> list[dict]:
    return load_json_dir(cache / "content-review" / "ledger")


def load_claims(cache: Path) -> list[dict]:
    return load_json_dir(cache / "content-review" / "claims")


def load_blog_ledger(cache: Path) -> list[dict]:
    return load_json_dir(cache / "content-review" / "blog-review" / "ledger")


def load_blog_runs(cache: Path) -> list[dict]:
    """All run records across dates, each tagged with _run_date."""
    runs_dir = cache / "content-review" / "blog-review" / "runs"
    records: list[dict] = []
    if not runs_dir.is_dir():
        return records
    for day in sorted(runs_dir.iterdir()):
        if not day.is_dir():
            continue
        for record in load_json_dir(day):
            record["_run_date"] = day.name
            records.append(record)
    return records


def latest_runs(runs: list[dict]) -> list[dict]:
    """Latest run record per slug (runs are tagged with _run_date)."""
    by_slug: dict[str, dict] = {}
    for record in runs:
        slug = record.get("slug") or ""
        if slug not in by_slug or record.get("_run_date", "") >= by_slug[slug].get("_run_date", ""):
            by_slug[slug] = record
    return [by_slug[s] for s in sorted(by_slug)]


def load_blog_summary(cache: Path) -> dict | None:
    return load_json_file(cache / "content-review" / "blog-review" / "index" / "_summary.json")


def load_health(cache: Path) -> dict | None:
    return load_json_file(cache / "content-review" / "health" / "state.json")


def load_social(cache: Path) -> list[dict]:
    """One row per (url, platform) across the social state files.

    posted.json and posted-social.json largely mirror each other; rows are
    deduplicated on (url, platform, posted_at), keeping the first source seen.
    """
    rows: list[dict] = []
    seen: set[tuple] = set()
    for name in ("posted-social.json", "posted.json"):
        data = load_json_file(cache / "social" / name)
        if not data:
            continue
        for url, platforms in (data.get("posts") or {}).items():
            if not isinstance(platforms, dict):
                continue
            failures = platforms.get("_failures")
            for platform, posted_at in platforms.items():
                if platform.startswith("_"):
                    continue
                key = (url, platform, posted_at)
                if key in seen:
                    continue
                seen.add(key)
                rows.append({
                    "url": url, "platform": platform, "posted_at": posted_at,
                    "failures": failures, "source_file": name,
                })
    rows.sort(key=lambda r: (r.get("posted_at") or "", r["url"]), reverse=True)
    return rows


def load_pr_review_latest(cache: Path) -> list[dict]:
    """One row per PR: `pr-review/<pr>/latest.json` -- the mirrored evidence
    object (findings + their REVIEW_STATE dispositions). See
    scripts/review-v3/README.md "The evidence object"."""
    base = cache / "content-review" / "pr-review"
    rows: list[dict] = []
    if not base.is_dir():
        return rows
    for pr_dir in sorted(base.iterdir()):
        if not pr_dir.is_dir() or not pr_dir.name.isdigit():
            continue  # skip state/, runs/, waives/ -- only numeric <pr> dirs
        record = load_json_file(pr_dir / "latest.json")
        if record is not None:
            record = dict(record)
            record["_file"] = str(pr_dir / "latest.json")
            rows.append(record)
    return rows


def load_pr_review_state(cache: Path) -> list[dict]:
    """One row per PR: `pr-review/state/<pr>.json` -- the SLA-sweep's own
    state (warns/escalations/closes), see scripts/review-v3/sla-sweep.py.

    The PR number only lives in the filename (the state object itself has
    no `pr` key -- see sla-sweep.py's state schema), so it's tagged onto
    each record here as an int `pr` field: both `record_matches()` (`show`
    by PR number) and `_pr_review_state_by_pr()` (join key) need it.
    """
    records = load_json_dir(cache / "content-review" / "pr-review" / "state")
    for r in records:
        stem = Path(r["_file"]).stem
        if stem.isdigit():
            r["pr"] = int(stem)
    return records


def load_pr_review_runs(cache: Path) -> list[dict]:
    """All SLA-sweep run records across dates, each tagged with _run_date."""
    runs_dir = cache / "content-review" / "pr-review" / "runs"
    records: list[dict] = []
    if not runs_dir.is_dir():
        return records
    for day in sorted(runs_dir.iterdir()):
        if not day.is_dir():
            continue
        for record in load_json_dir(day):
            record["_run_date"] = day.name
            records.append(record)
    return records


def load_pr_review_waives(cache: Path) -> list[dict]:
    """The v3 merge-gate waive log (`pr-review/waives/`) -- may not exist
    yet on a repo where nobody has applied `review:waived`."""
    return load_json_dir(cache / "content-review" / "pr-review" / "waives")


def _pr_review_state_by_pr(cache: Path) -> dict[str, dict]:
    return {Path(r["_file"]).stem: r for r in load_pr_review_state(cache)}


def _latest_sweep_action_by_pr(cache: Path) -> dict[str, dict]:
    """The most recent per-PR action entry across every synced run record,
    keyed by PR number as a string (matching latest.json's directory name)."""
    best: dict[str, tuple[str, dict]] = {}
    for record in load_pr_review_runs(cache):
        run_at = record.get("run_at") or record.get("_run_date") or ""
        for action in record.get("actions") or []:
            pr = str(action.get("pr"))
            if pr not in best or run_at >= best[pr][0]:
                best[pr] = (run_at, action)
    return {pr: action for pr, (_run_at, action) in best.items()}


def _summarize_sweep_action(action: dict) -> str:
    """One-word label for the review-admin `list pr-review` table: the last
    thing the SLA sweep did for this PR (warn/close/clear for author-time,
    escalate/none for reviewer-time)."""
    if not action:
        return ""
    if action.get("kind") == "author":
        return (action.get("action") or {}).get("type", "")
    if action.get("kind") == "reviewer":
        types = [a.get("type") for a in action.get("actions") or []]
        return "escalate" if "escalate" in types else (types[0] if types else "")
    return ""


def pr_review_rows(cache: Path) -> list[dict]:
    """One row per PR: evidence-derived blocking/dispositions counts, the
    SLA-sweep's warn/escalation/close counts, and its most recent action --
    the `list pr-review` / dashboard table."""
    states = _pr_review_state_by_pr(cache)
    last_actions = _latest_sweep_action_by_pr(cache)
    rows: list[dict] = []
    for record in load_pr_review_latest(cache):
        pr = str(record.get("pr") or "")
        findings = record.get("findings") or []
        blocking = sum(
            1 for f in findings
            if f.get("bucket") in ("outstanding", "author-answer") and not f.get("disposition")
        )
        dispositions = sum(1 for f in findings if f.get("disposition"))
        state = states.get(pr) or {}
        rows.append({
            "pr": record.get("pr"),
            "head_sha": (record.get("head_sha") or "")[:9],
            "blocking": blocking,
            "dispositions": dispositions,
            "warns": len(state.get("warns") or []),
            "escalations": len(state.get("escalations") or []),
            "closes": len(state.get("closes") or []),
            "last_sweep_action": _summarize_sweep_action(last_actions.get(pr) or {}),
            "generated_at": record.get("generated_at"),
        })
    return rows


# ---- flatteners -------------------------------------------------------------


def flatten_claims(articles: list[dict]) -> list[dict]:
    """One row per claim, with article fields denormalized onto each row."""
    rows: list[dict] = []
    for article in articles:
        base = {k: v for k, v in article.items() if k not in ("claims", "_file")}
        base["article_reviewed_at"] = base.pop("reviewed_at", None)
        for claim in article.get("claims") or []:
            if isinstance(claim, dict):
                rows.append({**base, **claim})
    return rows


def flatten_blog_issues(runs: list[dict]) -> list[dict]:
    """One row per issue from the latest run per post."""
    rows: list[dict] = []
    for run in latest_runs(runs):
        base = {
            "slug": run.get("slug"), "path": run.get("path"),
            "run_date": run.get("_run_date"), "post_date": run.get("post_date"),
            "status": run.get("status"), "noindex_signal": run.get("noindex_signal"),
        }
        for issue in run.get("issues") or []:
            if isinstance(issue, dict):
                prefixed = {f"issue_{k}": v for k, v in issue.items()}
                rows.append({**base, **prefixed})
    return rows


# ---- summary ----------------------------------------------------------------


def counter_line(counter: Counter) -> str:
    return ", ".join(f"{k or '(none)'}={v}" for k, v in counter.most_common()) or "(none)"


def date_span(records: list[dict], field: str) -> str:
    dates = sorted(r.get(field) for r in records if r.get(field))
    if not dates:
        return "n/a"
    return f"{dates[0]} .. {dates[-1]}"


def build_summary(cache: Path) -> dict:
    docs = load_docs(cache)
    claims_articles = load_claims(cache)
    claim_rows = flatten_claims(claims_articles)
    blog = load_blog_ledger(cache)
    runs = load_blog_runs(cache)
    social = load_social(cache)
    pr_review = pr_review_rows(cache)
    return {
        "docs": {
            "articles": len(docs),
            "by_status": Counter(r.get("status") for r in docs),
            "by_lane": Counter(r.get("lane") for r in docs),
            "fixes": sum(r.get("fixes") or 0 for r in docs),
            "reviewed_span": date_span(docs, "reviewed_at"),
        },
        "claims": {
            "articles": len(claims_articles),
            "claims": len(claim_rows),
            "by_verdict": Counter(r.get("verdict") for r in claim_rows),
            "by_confidence": Counter(r.get("confidence") for r in claim_rows),
            "reviewed_span": date_span(claims_articles, "reviewed_at"),
        },
        "blog": {
            "posts": len(blog),
            "by_status": Counter(r.get("status") for r in blog),
            "runs": len(runs),
            "run_dates": sorted({r.get("_run_date") for r in runs if r.get("_run_date")}),
            "issues": len(flatten_blog_issues(runs)),
            "by_severity": Counter(r.get("issue_severity") for r in flatten_blog_issues(runs)),
            "by_category": Counter(r.get("issue_category") for r in flatten_blog_issues(runs)),
        },
        "social": {
            "rows": len(social),
            "posts": len({r["url"] for r in social}),
            "by_platform": Counter(r.get("platform") for r in social),
            "with_failures": len({r["url"] for r in social if r.get("failures")}),
            "latest_post": max((r.get("posted_at") or "" for r in social), default="n/a"),
        },
        "pr_review": {
            "prs": len(pr_review),
            "blocking_total": sum(r["blocking"] for r in pr_review),
            "dispositions_total": sum(r["dispositions"] for r in pr_review),
            "warns_total": sum(r["warns"] for r in pr_review),
            "escalations_total": sum(r["escalations"] for r in pr_review),
            "closes_total": sum(r["closes"] for r in pr_review),
        },
    }


def cmd_summary(args) -> int:
    cache = require_cache(args)
    s = build_summary(cache)
    print()
    print(f"Docs review ledger      {s['docs']['articles']} articles, {s['docs']['fixes']} fixes applied, reviewed {s['docs']['reviewed_span']}")
    print(f"  status: {counter_line(s['docs']['by_status'])}")
    print(f"  lane:   {counter_line(s['docs']['by_lane'])}")
    print()
    print(f"Fact-check claims       {s['claims']['claims']} claims across {s['claims']['articles']} articles, reviewed {s['claims']['reviewed_span']}")
    print(f"  verdict:    {counter_line(s['claims']['by_verdict'])}")
    print(f"  confidence: {counter_line(s['claims']['by_confidence'])}")
    print()
    run_dates = s["blog"]["run_dates"]
    run_span = f"{run_dates[0]} .. {run_dates[-1]}" if run_dates else "n/a"
    print(f"Blog known-issues index {s['blog']['posts']} posts, {s['blog']['runs']} run records ({run_span}), {s['blog']['issues']} open issues")
    print(f"  status:   {counter_line(s['blog']['by_status'])}")
    print(f"  severity: {counter_line(s['blog']['by_severity'])}")
    print(f"  category: {counter_line(s['blog']['by_category'])}")
    blog_summary = load_blog_summary(cache)
    if blog_summary:
        print(f"  _summary.json: indexed={blog_summary.get('posts_indexed')} clean={blog_summary.get('posts_clean')} "
              f"with_issues={blog_summary.get('posts_with_issues')} noindex_candidates={len(blog_summary.get('noindex_candidates') or [])}")
    print()
    print(f"Social post state       {s['social']['posts']} posts, {s['social']['rows']} platform sends, latest {s['social']['latest_post'][:10] or 'n/a'}")
    print(f"  platform: {counter_line(s['social']['by_platform'])}")
    print(f"  posts with recorded failures: {s['social']['with_failures']}")
    print()
    pr = s["pr_review"]
    print(f"v3 PR review (pr-review/) {pr['prs']} PRs tracked, {pr['blocking_total']} blocking, "
          f"{pr['dispositions_total']} findings dispositioned")
    print(f"  SLA sweep: {pr['warns_total']} warns, {pr['escalations_total']} escalations, "
          f"{pr['closes_total']} closes")
    print()
    health = load_health(cache)
    if health:
        print(f"Signal health           (updated {health.get('updated')})")
        for name, sig in (health.get("signals") or {}).items():
            status = sig.get("status")
            extra = f" since {sig.get('degraded_since')}" if status != "ok" and sig.get("degraded_since") else ""
            marker = "" if status == "ok" else "  <-- attention"
            print(f"  {name}: {status}{extra}{marker}")
    return 0


# ---- list -------------------------------------------------------------------


def truncate(value, width: int) -> str:
    text = "" if value is None else str(value).replace("\n", " ")
    return text if len(text) <= width else text[: width - 1] + "…"


def print_table(rows: list[dict], columns: list[tuple[str, int]]) -> None:
    header = "  ".join(name.ljust(width) for name, width in columns)
    print(header)
    print("-" * len(header))
    for row in rows:
        print("  ".join(truncate(row.get(name), width).ljust(width) for name, width in columns))
    print(f"({len(rows)} rows)")


def list_rows(cache: Path, domain: str) -> tuple[list[dict], list[tuple[str, int]], str]:
    """Rows, display columns, and the default sort field for a domain."""
    if domain == "docs":
        return (load_docs(cache), [
            ("slug", 52), ("status", 9), ("lane", 9), ("fixes", 5),
            ("pr_number", 9), ("reviewed_at", 11), ("note", 60),
        ], "reviewed_at")
    if domain == "claims":
        rows = flatten_claims(load_claims(cache))
        return (rows, [
            ("slug", 42), ("claim_id", 8), ("type", 10), ("verdict", 12),
            ("confidence", 10), ("line_range", 10), ("text", 60),
        ], "article_reviewed_at")
    if domain == "blog":
        return (load_blog_ledger(cache), [
            ("slug", 52), ("status", 10), ("issues", 6), ("post_date", 11),
            ("reviewed_at", 11), ("note", 60),
        ], "reviewed_at")
    if domain == "social":
        rows = load_social(cache)
        return (rows, [
            ("url", 64), ("platform", 8), ("posted_at", 20), ("failures", 8),
        ], "posted_at")
    if domain == "pr-review":
        return (pr_review_rows(cache), [
            ("pr", 7), ("head_sha", 10), ("blocking", 9), ("dispositions", 13),
            ("warns", 6), ("escalations", 11), ("closes", 7), ("last_sweep_action", 18),
        ], "generated_at")
    die(f"unknown domain '{domain}' (expected one of: {', '.join(DOMAINS)})")


def cmd_list(args) -> int:
    cache = require_cache(args)
    rows, columns, sort_field = list_rows(cache, args.domain)
    if args.status:
        rows = [r for r in rows if r.get("status") == args.status]
    if args.verdict:
        rows = [r for r in rows if r.get("verdict") == args.verdict]
    if args.since:
        date_field = {
            "social": "posted_at", "claims": "article_reviewed_at", "pr-review": "generated_at",
        }.get(args.domain, "reviewed_at")
        rows = [r for r in rows if (r.get(date_field) or "") >= args.since]
    rows.sort(key=lambda r: r.get(sort_field) or "", reverse=True)
    if args.limit:
        rows = rows[: args.limit]
    print()
    print_table(rows, columns)
    return 0


# ---- show -------------------------------------------------------------------


def record_matches(record: dict, needle: str) -> bool:
    for field in ("slug", "path", "url"):
        value = record.get(field) or ""
        if needle == value or needle in value:
            return True
    pr = record.get("pr")
    if pr is not None and needle == str(pr):
        return True
    return False


def cmd_show(args) -> int:
    cache = require_cache(args)
    needle = args.slug
    sections = [
        ("docs review ledger", load_docs(cache)),
        ("fact-check claims", load_claims(cache)),
        ("blog-review ledger", load_blog_ledger(cache)),
        ("blog-review runs", load_blog_runs(cache)),
        ("social post state", load_social(cache)),
        ("pr-review latest (evidence)", load_pr_review_latest(cache)),
        ("pr-review state (SLA sweep)", load_pr_review_state(cache)),
        ("pr-review runs (SLA sweep)", load_pr_review_runs(cache)),
        ("pr-review waives", load_pr_review_waives(cache)),
    ]
    hits = 0
    for title, records in sections:
        matched = [r for r in records if record_matches(r, needle)]
        for record in matched:
            hits += 1
            source = record.get("_file") or record.get("source_file") or ""
            print(f"\n=== {title} — {source}")
            printable = {k: v for k, v in record.items() if k != "_file"}
            print(json.dumps(printable, indent=2))
    if not hits:
        warn(f"no records match '{needle}' (try a slug like docs-get-started or a /blog/... URL)")
        return 1
    print(f"\n({hits} records)")
    return 0


# ---- export -----------------------------------------------------------------


def export_columns(rows: list[dict], preferred: list[str]) -> list[str]:
    if not rows:
        return preferred
    extras = sorted({k for r in rows for k in r} - set(preferred) - {"_file", "_run_date"})
    return [c for c in preferred if any(c in r for r in rows)] + extras


def csv_value(value):
    if value is None:
        return ""
    if isinstance(value, (dict, list)):
        return json.dumps(value)
    return value


def write_exports(rows: list[dict], out_dir: Path, name: str, preferred: list[str], formats: set[str]) -> None:
    clean = [{k: v for k, v in r.items() if k not in ("_file", "_run_date")} for r in rows]
    if "jsonl" in formats:
        path = out_dir / f"{name}.jsonl"
        path.write_text("".join(json.dumps(r) + "\n" for r in clean))
        log(f"wrote {path} ({len(clean)} rows)")
    if "csv" in formats:
        path = out_dir / f"{name}.csv"
        columns = export_columns(clean, preferred)
        with path.open("w", newline="") as fh:
            writer = csv.DictWriter(fh, fieldnames=columns, extrasaction="ignore")
            writer.writeheader()
            for row in clean:
                writer.writerow({k: csv_value(row.get(k)) for k in columns})
        log(f"wrote {path} ({len(clean)} rows)")


def cmd_export(args) -> int:
    cache = require_cache(args)
    out_dir = Path(args.out) if args.out else cache / "exports"
    out_dir.mkdir(parents=True, exist_ok=True)
    formats = {"csv", "jsonl"} if args.format == "both" else {args.format}
    runs = load_blog_runs(cache)
    write_exports(load_docs(cache), out_dir, "docs-ledger", DOCS_COLUMNS, formats)
    write_exports(flatten_claims(load_claims(cache)), out_dir, "claims", CLAIM_COLUMNS, formats)
    write_exports(load_blog_ledger(cache), out_dir, "blog-review", BLOG_COLUMNS, formats)
    write_exports(flatten_blog_issues(runs), out_dir, "blog-review-issues", BLOG_ISSUE_COLUMNS, formats)
    write_exports(load_social(cache), out_dir, "social-posts", SOCIAL_COLUMNS, formats)
    write_exports(pr_review_rows(cache), out_dir, "pr-review", PR_REVIEW_COLUMNS, formats)
    return 0


# ---- html dashboard ---------------------------------------------------------

HTML_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Review ledgers</title>
<style>
:root { --bg:#fff; --fg:#1a1a2e; --muted:#667; --border:#d8d8e4; --surface:#f4f4fa;
        --accent:#805ac3; --bad:#c0392b; --good:#1e7e46; --warn:#a66900; }
@media (prefers-color-scheme: dark) {
  :root { --bg:#16161f; --fg:#e8e8f0; --muted:#99a; --border:#3a3a4c; --surface:#20202c;
          --accent:#b49aea; --bad:#e57368; --good:#5dbb85; --warn:#d9a04a; }
}
* { box-sizing: border-box; }
body { margin:0; font:14px/1.45 system-ui, sans-serif; background:var(--bg); color:var(--fg); }
header { padding:14px 20px; border-bottom:1px solid var(--border); display:flex; gap:16px;
         align-items:baseline; flex-wrap:wrap; }
header h1 { font-size:17px; margin:0; }
header .meta { color:var(--muted); font-size:12px; }
nav { display:flex; gap:4px; padding:8px 20px 0; border-bottom:1px solid var(--border); flex-wrap:wrap; }
nav button { border:1px solid var(--border); border-bottom:none; background:var(--surface);
             color:var(--fg); padding:7px 14px; border-radius:6px 6px 0 0; cursor:pointer; font-size:13px; }
nav button.active { background:var(--bg); font-weight:600; border-color:var(--accent); }
main { padding:16px 20px 40px; }
.controls { display:flex; gap:10px; margin:0 0 12px; flex-wrap:wrap; align-items:center; }
.controls input { padding:6px 10px; border:1px solid var(--border); border-radius:6px;
                  background:var(--bg); color:var(--fg); width:280px; }
.chip { border:1px solid var(--border); background:var(--surface); color:var(--fg);
        border-radius:12px; padding:3px 11px; cursor:pointer; font-size:12px; }
.chip.on { border-color:var(--accent); color:var(--accent); font-weight:600; }
.count { color:var(--muted); font-size:12px; }
.tablewrap { overflow-x:auto; border:1px solid var(--border); border-radius:8px; }
table { border-collapse:collapse; width:100%; }
th, td { text-align:left; padding:6px 10px; border-bottom:1px solid var(--border);
         vertical-align:top; max-width:420px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap; }
th { background:var(--surface); cursor:pointer; user-select:none; position:sticky; top:0; }
tr.datarow:hover { background:var(--surface); cursor:pointer; }
tr.detail td { white-space:pre-wrap; font-family:ui-monospace, monospace; font-size:12px;
               background:var(--surface); max-width:none; }
.badge { padding:1px 8px; border-radius:10px; font-size:12px; border:1px solid var(--border); }
.badge.ok { color:var(--good); border-color:var(--good); }
.badge.bad { color:var(--bad); border-color:var(--bad); }
.badge.warn { color:var(--warn); border-color:var(--warn); }
.cards { display:flex; gap:14px; flex-wrap:wrap; margin-bottom:18px; }
.card { border:1px solid var(--border); border-radius:8px; padding:12px 16px; background:var(--surface);
        min-width:200px; }
.card h3 { margin:0 0 6px; font-size:13px; color:var(--muted); font-weight:600; }
.card .big { font-size:24px; font-weight:700; }
.card .sub { font-size:12px; color:var(--muted); margin-top:4px; }
h2 { font-size:15px; margin:20px 0 8px; }
</style>
</head>
<body>
<header>
  <h1>Review ledgers</h1>
  <span class="meta" id="genmeta"></span>
</header>
<nav id="tabs"></nav>
<main id="main"></main>
<script type="application/json" id="data">__DATA__</script>
<script>
const DATA = JSON.parse(document.getElementById('data').textContent);
const TABS = [
  {id:'overview', label:'Overview'},
  {id:'docs', label:'Docs ledger', rows:DATA.docs, chips:'status',
   cols:['slug','status','lane','fixes','skipped_findings','pr_number','reviewed_at','note']},
  {id:'claims', label:'Claims', rows:DATA.claims, chips:'verdict',
   cols:['slug','claim_id','type','verdict','confidence','line_range','text']},
  {id:'blog', label:'Blog review', rows:DATA.blog, chips:'status',
   cols:['slug','status','issues','post_date','reviewed_at','note']},
  {id:'social', label:'Social', rows:DATA.social, chips:'platform',
   cols:['url','platform','posted_at','failures','source_file']},
  {id:'pr_review', label:'PR review', rows:DATA.pr_review, chips:'last_sweep_action',
   cols:['pr','head_sha','blocking','dispositions','warns','escalations','closes','last_sweep_action','generated_at']},
];
let active = 'overview';
const state = {};   // per-tab: {q, chip, sortCol, sortDir}

function el(tag, attrs, ...children) {
  const node = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs || {})) {
    if (k === 'onclick') node.onclick = v; else if (k === 'class') node.className = v;
    else node.setAttribute(k, v);
  }
  for (const child of children) node.append(child);
  return node;
}

function renderTabs() {
  const nav = document.getElementById('tabs');
  nav.replaceChildren(...TABS.map(t =>
    el('button', {class: t.id === active ? 'active' : '',
                  onclick: () => { active = t.id; render(); }},
       t.label + (t.rows ? ` (${t.rows.length})` : ''))));
}

function verdictClass(v) {
  if (['verified','ok','clean','reviewed'].includes(v)) return 'ok';
  if (['contradicted','degraded','incomplete'].includes(v)) return 'bad';
  return 'warn';
}

function renderOverview(main) {
  const s = DATA.summary, cards = el('div', {class:'cards'});
  const mk = (title, big, sub) => cards.append(
    el('div', {class:'card'}, el('h3', {}, title), el('div', {class:'big'}, String(big)),
       el('div', {class:'sub'}, sub)));
  mk('Docs articles reviewed', s.docs.articles, `${s.docs.fixes} fixes · ${fmtCounter(s.docs.by_status)}`);
  mk('Fact-check claims', s.claims.claims, `${s.claims.articles} articles · ${fmtCounter(s.claims.by_verdict)}`);
  mk('Blog posts indexed', s.blog.posts, `${s.blog.issues} open issues · ${fmtCounter(s.blog.by_status)}`);
  mk('Social sends', s.social.rows, `${s.social.posts} posts · ${fmtCounter(s.social.by_platform)}`);
  mk('v3 PRs tracked', s.pr_review.prs,
     `${s.pr_review.blocking_total} blocking · ${s.pr_review.warns_total} warns · ` +
     `${s.pr_review.escalations_total} escalations · ${s.pr_review.closes_total} closes`);
  main.append(cards);
  if (DATA.health && DATA.health.signals) {
    main.append(el('h2', {}, `Signal health (updated ${DATA.health.updated || '?'})`));
    const wrap = el('div', {class:'cards'});
    for (const [name, sig] of Object.entries(DATA.health.signals)) {
      const cls = sig.status === 'ok' ? 'ok' : 'bad';
      wrap.append(el('div', {class:'card'}, el('h3', {}, name),
        el('span', {class:`badge ${cls}`}, sig.status +
           (sig.degraded_since ? ` since ${sig.degraded_since}` : '')),
        el('div', {class:'sub'}, sig.detail || '')));
    }
    main.append(wrap);
  }
  if (DATA.blog_summary) {
    const b = DATA.blog_summary;
    main.append(el('h2', {}, 'Blog-review index summary (_summary.json)'),
      el('div', {class:'sub count'},
        `generated ${b.generated} · indexed ${b.posts_indexed} · clean ${b.posts_clean} · ` +
        `with issues ${b.posts_with_issues} · noindex candidates ${(b.noindex_candidates || []).length}`));
  }
}

function fmtCounter(counter) {
  return Object.entries(counter || {}).map(([k, v]) => `${k || '(none)'} ${v}`).join(' · ') || '—';
}

function renderTable(main, tab) {
  const st = state[tab.id] ||= {q:'', chip:null, sortCol:null, sortDir:-1};
  const chipValues = [...new Set(tab.rows.map(r => r[tab.chips]).filter(Boolean))].sort();
  const controls = el('div', {class:'controls'});
  const input = el('input', {placeholder:'filter…', value:st.q});
  input.oninput = () => { st.q = input.value; render(true); };
  controls.append(input);
  for (const v of chipValues) {
    controls.append(el('button', {class:'chip' + (st.chip === v ? ' on' : ''),
      onclick: () => { st.chip = st.chip === v ? null : v; render(); }}, v));
  }
  let rows = tab.rows.filter(r =>
    (!st.chip || r[tab.chips] === st.chip) &&
    (!st.q || JSON.stringify(r).toLowerCase().includes(st.q.toLowerCase())));
  if (st.sortCol) rows = [...rows].sort((a, b) =>
    String(a[st.sortCol] ?? '').localeCompare(String(b[st.sortCol] ?? '')) * st.sortDir);
  controls.append(el('span', {class:'count'}, `${rows.length} of ${tab.rows.length} rows — click a row for full record`));
  main.append(controls);
  const thead = el('tr', {}, ...tab.cols.map(c =>
    el('th', {onclick: () => { st.sortDir = st.sortCol === c ? -st.sortDir : -1; st.sortCol = c; render(); }},
       c + (st.sortCol === c ? (st.sortDir < 0 ? ' ↓' : ' ↑') : ''))));
  const tbody = el('tbody', {});
  for (const row of rows.slice(0, 2000)) {
    const tr = el('tr', {class:'datarow'}, ...tab.cols.map(c => {
      const value = row[c];
      if ((c === 'verdict' || c === 'status') && value)
        return el('td', {}, el('span', {class:`badge ${verdictClass(value)}`}, String(value)));
      return el('td', {title: value == null ? '' : String(value)},
                value == null ? '' : String(value));
    }));
    tr.onclick = () => {
      if (tr.nextSibling && tr.nextSibling.classList.contains('detail')) { tr.nextSibling.remove(); return; }
      tbody.querySelectorAll('tr.detail').forEach(n => n.remove());
      tr.after(el('tr', {class:'detail'},
        el('td', {colspan: String(tab.cols.length)}, JSON.stringify(row, null, 2))));
    };
    tbody.append(tr);
  }
  main.append(el('div', {class:'tablewrap'}, el('table', {}, el('thead', {}, thead), tbody)));
}

function render(keepFocus) {
  renderTabs();
  const main = document.getElementById('main');
  const focused = keepFocus && document.activeElement === main.querySelector('input');
  main.replaceChildren();
  const tab = TABS.find(t => t.id === active);
  if (tab.id === 'overview') renderOverview(main); else renderTable(main, tab);
  if (focused) { const inp = main.querySelector('input'); inp.focus(); inp.setSelectionRange(inp.value.length, inp.value.length); }
}

document.getElementById('genmeta').textContent =
  `generated ${DATA.generated}` + (DATA.sync_meta ? ` · synced ${DATA.sync_meta.synced_at}` : ' · cache never synced');
render();
</script>
</body>
</html>
"""


def counters_to_plain(obj):
    """Recursively convert Counter values into plain dicts for JSON."""
    if isinstance(obj, Counter):
        return dict(obj.most_common())
    if isinstance(obj, dict):
        return {k: counters_to_plain(v) for k, v in obj.items()}
    return obj


def render_html(cache: Path) -> str:
    runs = load_blog_runs(cache)
    data = {
        "generated": utc_now().isoformat(timespec="seconds"),
        "sync_meta": read_sync_meta(cache),
        "summary": counters_to_plain(build_summary(cache)),
        "docs": [{k: v for k, v in r.items() if k != "_file"} for r in load_docs(cache)],
        "claims": flatten_claims(load_claims(cache)),
        "blog": [{k: v for k, v in r.items() if k != "_file"} for r in load_blog_ledger(cache)],
        "blog_issues": flatten_blog_issues(runs),
        "social": load_social(cache),
        "pr_review": pr_review_rows(cache),
        "health": load_health(cache),
        "blog_summary": load_blog_summary(cache),
    }
    # </ must not appear literally inside the inline <script> data block.
    payload = json.dumps(data).replace("</", "<\\/")
    return HTML_TEMPLATE.replace("__DATA__", payload)


def cmd_html(args) -> int:
    cache = require_cache(args)
    out = Path(args.out) if args.out else cache / "review-dashboard.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render_html(cache))
    log(f"wrote {out}")
    if args.open:
        webbrowser.open(out.resolve().as_uri())
    return 0


# ---- self-test --------------------------------------------------------------

FIXTURES = {
    "content-review/ledger/docs-get-started.json": {
        # Legacy record shape: no schema_version.
        "path": "content/docs/get-started/_index.md", "slug": "docs-get-started",
        "lane": "priority", "status": "clean", "pr": None, "pr_number": 0,
        "head_sha": "", "fixes": 0, "skipped_findings": 2, "retirement": False,
        "note": "all clean", "reviewed_at": "2026-06-16",
    },
    "content-review/claims/docs-example.json": {
        "schema_version": 1, "path": "content/docs/example.md", "slug": "docs-example",
        "commit": "abc123", "reviewed_at": "2026-07-16", "model": "claude-sonnet-5",
        "claims": [
            {"claim_id": "c1", "type": "behavior", "text": "It works. </script> honest.",
             "line_range": "L19", "verdict": "verified", "confidence": "high",
             "evidence": "source says so", "source": "repo:content/docs/example.md",
             "entity_key": None, "volatile": False},
            {"claim_id": "c2", "type": "url", "text": "Dead link", "line_range": "L21",
             "verdict": "contradicted", "confidence": "high", "evidence": "404",
             "source": "web", "entity_key": None, "volatile": True},
        ],
    },
    "content-review/blog-review/ledger/example-post.json": {
        "schema_version": 1, "path": "content/blog/example-post/index.md",
        "slug": "example-post", "lane": "manual", "status": "reviewed", "issues": 1,
        "note": "", "attempts": 1, "score": None, "post_date": "2020-01-01",
        "head_sha": "def456", "reviewed_at": "2026-07-16",
    },
    "content-review/blog-review/runs/2026-07-16/example-post.json": {
        "schema_version": 1, "path": "content/blog/example-post/index.md",
        "slug": "example-post", "url": "/blog/example-post/", "post_date": "2020-01-01",
        "reviewed_at": "2026-07-16", "status": "reviewed", "clean": False,
        "issues": [{"category": "dead-link", "severity": "medium", "detail": "404 on example.com"}],
        "issue_counts": {"total": 1}, "noindex_signal": None,
    },
    "content-review/blog-review/index/_summary.json": {
        "schema_version": 1, "generated": "2026-07-16", "posts_indexed": 1,
        "posts_clean": 0, "posts_with_issues": 1, "issues_by_severity": {"medium": 1},
        "issues_by_category": {"dead-link": 1}, "noindex_candidates": [],
    },
    "content-review/health/state.json": {
        "version": 1, "updated": "2026-07-16",
        "signals": {"traffic": {"status": "ok", "detail": "ok", "last_ok": "2026-07-16",
                                "degraded_since": None, "last_alerted": None},
                    "console-access": {"status": "degraded", "detail": "degraded",
                                       "last_ok": None, "degraded_since": "2026-07-10",
                                       "last_alerted": None}},
    },
    "social/posted-social.json": {
        "posts": {"/blog/example-post/": {"x": "2026-04-01T09:00:00+00:00",
                                          "linkedin": "2026-04-01T09:01:00+00:00",
                                          "_failures": 1}},
    },
    "content-review/pr-review/21300/latest.json": {
        "schema_version": 1, "repo": "pulumi/docs", "pr": 21300, "head_sha": "a" * 40,
        "run_id": "run-1", "generated_at": "2026-08-31T17:00:00Z", "high_water": 2,
        "findings": [
            {"id": "F1", "bucket": "outstanding", "file": "content/docs/x.md",
             "text": "Broken link", "origin": "verdict:contradicted", "status": "open"},
            {"id": "F2", "bucket": "author-answer", "file": "content/docs/x.md",
             "text": "Source?", "origin": "verdict:unverifiable", "status": "resolved",
             "disposition": {"disposition": "refuted", "actor": "cam", "note": "n",
                             "updated_at": "2026-08-31T18:00:00Z"}},
        ],
        "trail": [], "investigation_log": {}, "history": [],
    },
    "content-review/pr-review/state/21300.json": {
        "schema": 1,
        "warns": [{"at": "2026-08-31T12:00:00Z", "head_sha": "a" * 40}],
        "escalations": [], "closes": [],
    },
    "content-review/pr-review/runs/2026-08-31/sweep-120000Z.json": {
        "schema": 1, "run_at": "2026-08-31T12:00:00Z", "dry_run": False,
        "actions": [
            {"pr": 21300, "kind": "author", "head_sha": "a" * 40, "changed": True,
             "action": {"type": "warn", "idle_days": 16.0, "undecided_count": 1}},
        ],
    },
}


def self_test() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        cache = Path(tmp)
        for rel, record in FIXTURES.items():
            path = cache / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(record, indent=2) + "\n")

        docs = load_docs(cache)
        assert len(docs) == 1 and docs[0]["slug"] == "docs-get-started", docs
        claim_rows = flatten_claims(load_claims(cache))
        assert len(claim_rows) == 2, claim_rows
        assert claim_rows[0]["slug"] == "docs-example" and claim_rows[0]["claim_id"] == "c1"
        assert {r["verdict"] for r in claim_rows} == {"verified", "contradicted"}

        runs = load_blog_runs(cache)
        issues = flatten_blog_issues(runs)
        assert len(issues) == 1 and issues[0]["issue_category"] == "dead-link", issues
        social = load_social(cache)
        assert len(social) == 2 and social[0]["failures"] == 1, social

        pr_rows = pr_review_rows(cache)
        assert len(pr_rows) == 1, pr_rows
        row = pr_rows[0]
        assert row["pr"] == 21300
        assert row["head_sha"] == ("a" * 40)[:9]
        assert row["blocking"] == 1, row  # F1 outstanding, no disposition
        assert row["dispositions"] == 1, row  # F2 has a disposition
        assert row["warns"] == 1 and row["escalations"] == 0 and row["closes"] == 0
        assert row["last_sweep_action"] == "warn", row
        assert record_matches({"pr": 21300}, "21300")

        summary = build_summary(cache)
        assert summary["claims"]["by_verdict"]["contradicted"] == 1
        assert summary["blog"]["issues"] == 1
        assert summary["social"]["posts"] == 1
        assert summary["pr_review"]["prs"] == 1
        assert summary["pr_review"]["blocking_total"] == 1
        assert summary["pr_review"]["warns_total"] == 1

        out_dir = cache / "exports"
        out_dir.mkdir()
        write_exports(claim_rows, out_dir, "claims", CLAIM_COLUMNS, {"csv", "jsonl"})
        csv_lines = (out_dir / "claims.csv").read_text().splitlines()
        assert len(csv_lines) == 3, csv_lines  # header + 2 claims
        assert csv_lines[0].startswith("slug,path,claim_id")
        jsonl = [json.loads(line) for line in (out_dir / "claims.jsonl").read_text().splitlines()]
        assert jsonl[1]["verdict"] == "contradicted"

        write_exports(pr_rows, out_dir, "pr-review", PR_REVIEW_COLUMNS, {"csv", "jsonl"})
        pr_csv_lines = (out_dir / "pr-review.csv").read_text().splitlines()
        assert len(pr_csv_lines) == 2  # header + 1 PR
        assert pr_csv_lines[0].startswith("pr,head_sha,blocking")

        html = render_html(cache)
        assert "Review ledgers" in html
        assert "</script> honest" not in html          # escaped in embedded JSON
        assert "<\\/script> honest" in html
        assert "docs-get-started" in html
        assert "PR review" in html and "21300" in html

    print("self-test OK")
    return 0


# ---- main -------------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Browse and export the S3 review/state ledgers (read-only).")
    parser.add_argument("--self-test", action="store_true", help="run the offline smoke test and exit")
    parser.add_argument("--cache-dir", help=f"local cache directory (default: <repo>/{CACHE_DIRNAME}, or ${CACHE_ENV})")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("sync", help="sync both buckets into the local cache")
    sub.add_parser("summary", help="console overview of all captured data")

    p_list = sub.add_parser("list", help="list records for one domain")
    p_list.add_argument("domain", choices=DOMAINS)
    p_list.add_argument("--status", help="filter by status (docs/blog)")
    p_list.add_argument("--verdict", help="filter by claim verdict (claims)")
    p_list.add_argument("--since", help="only records on/after this date (YYYY-MM-DD)")
    p_list.add_argument("--limit", type=int, help="max rows")

    p_show = sub.add_parser("show", help="print every record matching a slug, path, or URL")
    p_show.add_argument("slug")

    p_export = sub.add_parser("export", help="write normalized CSV/JSONL exports")
    p_export.add_argument("--out", help="output directory (default: <cache>/exports)")
    p_export.add_argument("--format", choices=["csv", "jsonl", "both"], default="both")

    p_html = sub.add_parser("html", help="generate the self-contained HTML dashboard")
    p_html.add_argument("--out", help="output file (default: <cache>/review-dashboard.html)")
    p_html.add_argument("--open", action="store_true", help="open in a browser after writing")

    args = parser.parse_args(argv)
    if args.self_test:
        return self_test()
    handlers = {"sync": cmd_sync, "summary": cmd_summary, "list": cmd_list,
                "show": cmd_show, "export": cmd_export, "html": cmd_html}
    if not args.command:
        parser.print_help()
        return 2
    return handlers[args.command](args)


if __name__ == "__main__":
    sys.exit(main())

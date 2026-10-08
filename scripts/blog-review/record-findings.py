#!/usr/bin/env python3
"""Record one blog post's review outcome to the S3 known-issues index.

This is the single source of truth for the blog-review record shapes and
their upload. The record job of `.github/workflows/blog-review-index.yml`
runs it once per reviewed post (`if: always()` semantics via the workflow
loop), so every selected post lands exactly one canonical ledger object per
run — even when the model exits without producing output.

The review is FLAG-ONLY: the model records findings, never edits content, so
there is no patch, no branch, and no PR. The model's only structured output
is the findings sentinel (`.blog-review-findings.json`), validated here via
validate-findings.py (schema shape, closed taxonomy, evidence-required).
Status is derived from observable state, not self-report:

  * findings valid, issues found        -> status "reviewed"
  * findings valid, clean: true         -> status "clean"
  * findings absent/unreadable/invalid  -> status "incomplete" (stays due,
                                           retried up to the attempt cap)
  * working tree was dirty after review -> status "incomplete" (the model
                                           broke the flag-only contract; its
                                           findings are not trusted)

Three objects are written (locally always; to S3 when the URIs are set):

  ledger  BLOG_REVIEW_LEDGER_URI/<slug>.json  — bookkeeping / staleness clock
  index   BLOG_REVIEW_INDEX_URI/<slug>.json   — the known-issues index entry
                                                (reviewed/clean only)
  run log BLOG_REVIEW_RUNS_URI/<date>/<slug>.json — immutable append-only
          copy of each run for warehouse ingestion (every outcome, including
          incomplete)

Every object carries `schema_version` and `reviewed_at` so the warehouse
ingestion (see the blog-review section of AGENTS.md) can consume increments.

Exit code: 0 normally, 1 when the LEDGER upload fails. The workflow's record
loop only marks a post FAILED on a non-zero exit, and a lost ledger write is
the one failure that must not pass silently — the post's outcome (including
`incomplete`) would never reach the staleness clock. The index and run-log
uploads stay best-effort; a later run rebuilds them.

Self-contained — run the smoke checks with `python3 record-findings.py --self-test`.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent

SCHEMA_VERSION = 1

# Reuse the validation gate from validate-findings.py (single source of
# truth for the findings contract). Hyphenated filename, so import by path;
# main() is guarded under __main__, so importing has no side effects.
_spec = importlib.util.spec_from_file_location(
    "validate_findings_mod", HERE / "validate-findings.py"
)
_validate = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_validate)
validate_findings = _validate.validate_findings


def log(msg: str) -> None:
    print(f"record-findings: {msg}", file=sys.stderr)


def warn(msg: str) -> None:
    # `::warning::` surfaces in the GitHub Actions run summary.
    print(f"::warning::record-findings: {msg}", file=sys.stderr)


# ---- inputs -----------------------------------------------------------------


def _maybe_int(v):
    try:
        return int(v)
    except (TypeError, ValueError):
        return None


def load_queue_post(queue_path: Path) -> dict:
    """Return the single post from the worker queue, with its selection signal.

    Beyond the bookkeeping fields (path/slug/lane/attempts), this carries the
    selection facts the post was chosen on — score, monthly visits, GSC
    figures, and whether each snapshot was available that run. They're
    persisted onto the ledger and index records so the S3 state is a
    complete, self-contained metrics source (outcome AND why-it-was-picked).
    """
    data = json.loads(queue_path.read_text())
    posts = data.get("posts") or []
    if not posts:
        raise SystemExit(f"record-findings: no posts in {queue_path}")
    p = posts[0]
    traffic = data.get("traffic") or {}
    return {
        "path": p["path"],
        "slug": p["slug"],
        "url": p.get("url"),
        "lane": p.get("lane") or "priority",
        "post_date": p.get("post_date"),
        # Prior incomplete-retry count, carried from the ledger by the selector.
        "attempts": int(p.get("attempts") or 0),
        "score": p.get("score"),
        "monthly_visits": _maybe_int(p.get("monthly_visits")),
        "traffic_available": bool(traffic.get("available")),
        "signals": p.get("signals"),
        "signals_available": bool((data.get("reader_signals") or {}).get("available")),
    }


def load_findings(findings_path: Path | None) -> dict | None:
    """Return the model's findings sentinel, or None if absent/unparseable."""
    if not findings_path or not findings_path.is_file():
        return None
    try:
        return json.loads(findings_path.read_text())
    except (OSError, json.JSONDecodeError) as e:
        warn(f"findings sentinel unreadable ({e}); treating as incomplete")
        return None


# ---- derivation -------------------------------------------------------------


def issue_counts(issues: list[dict]) -> dict:
    by_severity: dict[str, int] = {}
    by_category: dict[str, int] = {}
    for i in issues:
        by_severity[i["severity"]] = by_severity.get(i["severity"], 0) + 1
        by_category[i["category"]] = by_category.get(i["category"], 0) + 1
    return {"total": len(issues), "by_severity": by_severity, "by_category": by_category}


def build_records(
    post: dict,
    findings: dict | None,
    claude_succeeded: bool,
    tree_dirty: bool,
    head_sha: str = "",
    today: str | None = None,
) -> tuple[dict, dict | None, dict]:
    """Build (ledger, index-or-None, run-log) records.

    `attempts` accrues the consecutive `incomplete` retries: it starts from
    the prior count the selector carried in (`post["attempts"]`), is
    incremented by one on another incomplete outcome, and is reset to 0 the
    moment the post reaches any completed status. The selector backs a post
    off once it hits ATTEMPT_CAP, so this counter is the loop guard.
    """
    reviewed_at = today or datetime.now(timezone.utc).date().isoformat()
    prior_attempts = int(post.get("attempts") or 0)

    errors: list[str] = []
    if findings is None:
        errors = ["findings sentinel absent or unreadable"]
    else:
        errors = validate_findings(findings, post)
    if tree_dirty:
        errors.append("working tree was dirty after the review (flag-only contract broken)")
    if not claude_succeeded:
        errors.append("review run did not succeed")

    valid = not errors
    issues = list(findings.get("issues") or []) if valid else []
    clean = bool(findings.get("clean")) if valid else False

    if valid:
        status = "clean" if clean else "reviewed"
        attempts = 0
        note = None
    else:
        status = "incomplete"
        attempts = prior_attempts + 1
        note = "; ".join(errors)
        if findings is not None and note != "findings sentinel absent or unreadable":
            warn(f"findings rejected for {post['slug']}: {note}")

    ledger = {
        "schema_version": SCHEMA_VERSION,
        "path": post["path"],
        "slug": post["slug"],
        "lane": post["lane"],
        "status": status,
        "issues": len(issues),
        "note": note,
        "attempts": attempts,
        # Selection signal (carried from the queue) — persisted so the ledger
        # captures why the post was picked, not just the outcome.
        "score": post.get("score"),
        "monthly_visits": post.get("monthly_visits"),
        "traffic_available": bool(post.get("traffic_available")),
        "signals": post.get("signals"),
        "signals_available": bool(post.get("signals_available")),
        "post_date": post.get("post_date"),
        "head_sha": head_sha,
        "reviewed_at": reviewed_at,
    }

    index = None
    if valid:
        index = {
            "schema_version": SCHEMA_VERSION,
            "path": post["path"],
            "slug": post["slug"],
            "url": post.get("url"),
            "post_date": post.get("post_date"),
            "head_sha": head_sha,
            "reviewed_at": reviewed_at,
            "status": status,
            "clean": clean,
            "issues": issues,
            "issue_counts": issue_counts(issues),
            "noindex_signal": findings.get("noindex_signal"),
            "signals": {
                "monthly_visits": post.get("monthly_visits"),
                "traffic_available": bool(post.get("traffic_available")),
                "gsc": (post.get("signals") or {}).get("gsc"),
            },
        }

    # The run log records every outcome — including incomplete — so the
    # warehouse sees retries and breakage, not just successes.
    run_log = dict(index) if index else {
        "schema_version": SCHEMA_VERSION,
        "path": post["path"],
        "slug": post["slug"],
        "url": post.get("url"),
        "post_date": post.get("post_date"),
        "head_sha": head_sha,
        "reviewed_at": reviewed_at,
        "status": status,
        "clean": False,
        "issues": [],
        "issue_counts": issue_counts([]),
        "noindex_signal": None,
        "signals": {
            "monthly_visits": post.get("monthly_visits"),
            "traffic_available": bool(post.get("traffic_available")),
            "gsc": (post.get("signals") or {}).get("gsc"),
        },
    }
    run_log = {**run_log, "note": note}

    return ledger, index, run_log


# ---- output -----------------------------------------------------------------


def upload(record: dict, key: str) -> bool:
    """Upload the record to the S3 key via the aws CLI (stdin).

    Returns True on success. The caller decides what a failure costs: a lost
    LEDGER write means the post's staleness clock never advances (or, worse,
    an incomplete outcome is never recorded), so the record job must go red;
    the index and run-log writes are best-effort.
    """
    try:
        subprocess.run(
            ["aws", "s3", "cp", "-", key],
            input=json.dumps(record, indent=2) + "\n",
            text=True, check=True,
        )
        log(f"uploaded {key}")
        return True
    except FileNotFoundError:
        warn("aws CLI not available; record not uploaded")
        return False
    except subprocess.CalledProcessError as e:
        warn(f"upload failed for {key} ({e})")
        return False


def s3_key(uri: str, *parts: str) -> str:
    return "/".join([uri.rstrip("/"), *parts])


# ---- main -------------------------------------------------------------------


def run(args) -> int:
    post = load_queue_post(Path(args.queue))
    slug = post["slug"]
    findings = load_findings(Path(args.findings) if args.findings else None)
    claude_succeeded = (args.claude_outcome or "").strip().lower() == "success"
    tree_dirty = (args.tree_status or "").strip().lower() == "dirty"

    ledger, index, run_log = build_records(
        post, findings, claude_succeeded, tree_dirty,
        head_sha=args.head_sha or "", today=args.today,
    )

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / f"ledger-{slug}.json").write_text(json.dumps(ledger, indent=2) + "\n")
    if index:
        (out_dir / f"index-{slug}.json").write_text(json.dumps(index, indent=2) + "\n")
    (out_dir / f"run-{slug}.json").write_text(json.dumps(run_log, indent=2) + "\n")
    log(f"status={ledger['status']} slug={slug} issues={ledger['issues']} -> {out_dir}")

    ledger_uri = os.environ.get("BLOG_REVIEW_LEDGER_URI", "").strip()
    index_uri = os.environ.get("BLOG_REVIEW_INDEX_URI", "").strip()
    runs_uri = os.environ.get("BLOG_REVIEW_RUNS_URI", "").strip()
    # The workflow marks the post FAILED only on a non-zero exit, so a lost
    # ledger write has to be one: without it the post's outcome is invisible to
    # the next sweep. An unset URI is the configured-off case, not a failure;
    # the index and run-log writes stay best-effort (the ledger is the state
    # that matters, and both are rebuilt from later runs).
    ledger_uploaded = True
    if ledger_uri:
        ledger_uploaded = upload(ledger, s3_key(ledger_uri, f"{slug}.json"))
    else:
        warn("BLOG_REVIEW_LEDGER_URI unset; ledger record written locally only")
    if index and index_uri:
        upload(index, s3_key(index_uri, f"{slug}.json"))
    if runs_uri:
        upload(run_log, s3_key(runs_uri, ledger["reviewed_at"], f"{slug}.json"))

    if not ledger_uploaded:
        warn(f"ledger upload failed for {slug}; recording the run as failed")
        return 1
    return 0


def self_test() -> int:
    import tempfile

    failures = []

    def check(name, cond):
        if not cond:
            failures.append(name)
            print(f"FAIL: {name}", file=sys.stderr)
        else:
            print(f"ok: {name}")

    with tempfile.TemporaryDirectory() as d:
        d = Path(d)
        queue = d / "queue.json"
        gsc_block = {"gsc": {"impressions": 15234, "ctr": 0.0205,
                             "opportunity": 0.41, "multiplier": 1.1025}}
        queue.write_text(json.dumps({
            "traffic": {"available": True},
            "reader_signals": {"available": True},
            "posts": [{
                "path": "content/blog/my-post/index.md",
                "slug": "my-post",
                "url": "/blog/my-post/",
                "lane": "priority",
                "post_date": "2021-03-04",
                "attempts": 0,
                "score": 812.5,
                "monthly_visits": 842,
                "signals": gsc_block,
            }]
        }))
        post = load_queue_post(queue)
        check("queue post carries the selection signal",
              post["score"] == 812.5 and post["monthly_visits"] == 842
              and post["traffic_available"] is True and post["signals"] == gsc_block)

        good_findings = {
            "schema_version": 1,
            "path": "content/blog/my-post/index.md",
            "slug": "my-post",
            "issues": [
                {"id": "dead-link-01", "category": "dead-link", "severity": "major",
                 "summary": "s", "evidence": "e", "location": "l"},
                {"id": "rot-01", "category": "factual-rot", "severity": "minor",
                 "summary": "s", "evidence": "e", "location": "l"},
            ],
            "clean": False,
            "noindex_signal": {"assessment": "candidate", "rationale": "r"},
        }

        ledger, index, run_log = build_records(
            post, good_findings, claude_succeeded=True, tree_dirty=False,
            head_sha="abc123", today="2026-07-15")
        check("valid findings -> reviewed", ledger["status"] == "reviewed")
        check("reviewed resets attempts", ledger["attempts"] == 0)
        check("ledger counts issues", ledger["issues"] == 2)
        check("index entry exists", index is not None)
        check("index carries the issues verbatim", index["issues"] == good_findings["issues"])
        check("index counts by severity",
              index["issue_counts"]["by_severity"] == {"major": 1, "minor": 1})
        check("index counts by category",
              index["issue_counts"]["by_category"] == {"dead-link": 1, "factual-rot": 1})
        check("index carries noindex_signal",
              index["noindex_signal"]["assessment"] == "candidate")
        check("index carries selection signals",
              index["signals"]["monthly_visits"] == 842
              and index["signals"]["gsc"] == gsc_block["gsc"])
        check("schema_version + reviewed_at on every object",
              all(o.get("schema_version") == 1 and o.get("reviewed_at") == "2026-07-15"
                  for o in (ledger, index, run_log)))
        check("run log mirrors the index on success",
              run_log["issues"] == index["issues"] and run_log["status"] == "reviewed")

        clean_findings = {**good_findings, "issues": [], "clean": True,
                          "noindex_signal": {"assessment": "keep", "rationale": "r"}}
        ledger, index, run_log = build_records(
            post, clean_findings, claude_succeeded=True, tree_dirty=False)
        check("clean findings -> clean", ledger["status"] == "clean")
        check("clean still writes an index entry",
              index is not None and index["clean"] is True and index["issues"] == [])

        # Absent sentinel -> incomplete; attempts accrue; no index entry.
        retried = {**post, "attempts": 2}
        ledger, index, run_log = build_records(
            retried, None, claude_succeeded=True, tree_dirty=False)
        check("absent findings -> incomplete", ledger["status"] == "incomplete")
        check("incomplete accrues prior attempts (2 -> 3)", ledger["attempts"] == 3)
        check("incomplete writes no index entry", index is None)
        check("incomplete still writes a run log",
              run_log["status"] == "incomplete" and run_log["note"])

        # Invalid findings (open taxonomy) -> incomplete.
        bad = {**good_findings,
               "issues": [{**good_findings["issues"][0], "category": "vibes"}]}
        ledger, index, _ = build_records(post, bad, claude_succeeded=True, tree_dirty=False)
        check("invalid findings -> incomplete", ledger["status"] == "incomplete")
        check("invalid findings never reach the index", index is None)

        # A dirty tree invalidates even valid findings: flag-only is a hard contract.
        ledger, index, _ = build_records(
            post, good_findings, claude_succeeded=True, tree_dirty=True)
        check("dirty tree -> incomplete despite valid findings",
              ledger["status"] == "incomplete" and index is None)
        check("dirty tree noted", "flag-only" in (ledger["note"] or ""))

        # A failed run -> incomplete even with a plausible sentinel.
        ledger, index, _ = build_records(
            post, good_findings, claude_succeeded=False, tree_dirty=False)
        check("failed run -> incomplete", ledger["status"] == "incomplete")

    if failures:
        print(f"\n{len(failures)} failure(s)", file=sys.stderr)
        return 1
    print("\nall record-findings self-tests passed")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description="Record a blog-review outcome to the S3 index.")
    p.add_argument("--queue", help="single-post queue JSON (.blog-review-queue.json)")
    p.add_argument("--findings", help="model findings sentinel (.blog-review-findings.json)")
    p.add_argument("--claude-outcome",
                   help="GitHub step outcome of the review run (success/failure/cancelled)")
    p.add_argument("--tree-status", choices=["clean", "dirty"], default="clean",
                   help="working-tree state after the review (dirty => incomplete)")
    p.add_argument("--head-sha", help="commit the review ran on")
    p.add_argument("--today", help="Override reviewed_at YYYY-MM-DD (testing)")
    p.add_argument("--out-dir", default=".blog-review-records",
                   help="local record artifact directory")
    p.add_argument("--self-test", action="store_true", help="run built-in smoke checks")
    args = p.parse_args()

    if args.self_test:
        return self_test()
    if not args.queue:
        p.error("--queue is required")
    return run(args)


if __name__ == "__main__":
    sys.exit(main())

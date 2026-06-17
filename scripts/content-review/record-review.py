#!/usr/bin/env python3
"""Record one content-review article's outcome to the S3 ledger.

This is the single source of truth for the ledger record shape and its upload.
The per-article worker (`.github/workflows/content-review-article.yml`) runs it
once after the review model finishes, with `if: always()`, so every dispatched
article lands exactly one canonical ledger object — even when the model exits
without producing any output.

The model's only structured output is a tiny verdict sentinel
(`.content-review-verdict.json`); everything authoritative about the PR
(existence, number, head SHA) is derived here from `gh`, not self-reported.

Outcome derivation:
  * verdict "fixed"  + PR on content-review/<slug>      -> status "reviewed"
  * verdict "clean"                                      -> status "clean"
  * verdict "skipped"                                    -> status "skipped"
  * verdict "fixed"  + no PR on the canonical branch     -> status "incomplete"
  * sentinel absent / unparseable                        -> status "incomplete"

Canonical record (every field always present):
  { path, slug, lane, status, pr, pr_number, head_sha, fixes,
    skipped_findings, retirement, note, reviewed_at }

The record is written locally (audit artifact) and, when CONTENT_REVIEW_LEDGER_URI
is set, uploaded to <uri>/<slug>.json with reviewed_at stamped to today (UTC).
A `dispatch` / `pr_number` / `head_sha` signal is emitted to $GITHUB_OUTPUT for
the workflow's review-dispatch step. Degrades gracefully: a missing bucket URI
skips the upload (the page reappears next cycle) rather than failing the run.

Self-contained — run the smoke checks with `python3 record-review.py --self-test`.
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

# Reuse slugify + the branch prefix from select-articles.py (single source of
# truth). Its filename is hyphenated, so import it by path; its main() is guarded
# under __main__, so importing has no side effects.
_spec = importlib.util.spec_from_file_location(
    "select_articles", HERE / "select-articles.py"
)
_select = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_select)
slugify = _select.slugify
BRANCH_PREFIX = _select.BRANCH_PREFIX

# PR-body sections the review skill mandates; the post-create check warns (never
# blocks) when a fix PR's body is missing one.
REQUIRED_PR_SECTIONS = [
    "Why this page",
    "Fixes applied",
    "Findings not applied",
    "Screenshot check",
    "Rendered content",
    "Verification",
]


def log(msg: str) -> None:
    print(f"record-review: {msg}", file=sys.stderr)


def warn(msg: str) -> None:
    # `::warning::` surfaces in the GitHub Actions run summary.
    print(f"::warning::record-review: {msg}", file=sys.stderr)


# ---- inputs -----------------------------------------------------------------


def load_queue_article(queue_path: Path) -> dict:
    """Return the single article (path/slug/lane) from the worker queue."""
    data = json.loads(queue_path.read_text())
    articles = data.get("articles") or []
    if not articles:
        raise SystemExit(f"record-review: no articles in {queue_path}")
    a = articles[0]
    path = a["path"]
    return {
        "path": path,
        "slug": a.get("slug") or slugify(path),
        "lane": a.get("lane") or "priority",
        # Prior incomplete-retry count, carried from the ledger by the selector.
        # build_record increments it on another incomplete, resets it on success.
        "attempts": int(a.get("attempts") or 0),
    }


def load_verdict(verdict_path: Path | None) -> dict | None:
    """Return the model's verdict sentinel, or None if absent/unparseable."""
    if not verdict_path or not verdict_path.is_file():
        return None
    try:
        return json.loads(verdict_path.read_text())
    except (OSError, json.JSONDecodeError) as e:
        warn(f"verdict sentinel unreadable ({e}); treating as incomplete")
        return None


def branch_for(slug: str, retirement: bool) -> str:
    return f"{BRANCH_PREFIX}{'retire-' if retirement else ''}{slug}"


def fetch_pr(branch: str, pr_json: str | None) -> dict | None:
    """PR for the given head branch, or None.

    `pr_json` (a file path, or '-' for stdin) injects the gh response for tests;
    otherwise we shell out to `gh pr view <branch>`.
    """
    if pr_json is not None:
        raw = sys.stdin.read() if pr_json == "-" else Path(pr_json).read_text()
        raw = raw.strip()
        if not raw:
            return None
        pr = json.loads(raw)
        return pr or None
    try:
        out = subprocess.run(
            ["gh", "pr", "view", branch, "--json", "number,state,headRefOid,url,body"],
            capture_output=True,
            text=True,
            check=False,
        )
    except FileNotFoundError:
        warn("gh not available; cannot derive PR facts")
        return None
    if out.returncode != 0:
        return None  # no PR for this branch
    try:
        return json.loads(out.stdout) or None
    except json.JSONDecodeError:
        return None


def scan_misnamed_sibling(slug: str) -> None:
    """Best-effort warning when a fix PR exists under a non-canonical branch."""
    try:
        out = subprocess.run(
            ["gh", "pr", "list", "--state", "open", "--limit", "100",
             "--json", "number,headRefName,url"],
            capture_output=True, text=True, check=False,
        )
        if out.returncode != 0:
            return
        for pr in json.loads(out.stdout or "[]"):
            head = pr.get("headRefName", "")
            if not head.startswith(BRANCH_PREFIX):
                continue
            head_slug = head[len(BRANCH_PREFIX):].removeprefix("retire-")
            if head_slug == slug:
                warn(
                    f"PR #{pr.get('number')} ({pr.get('url')}) reviews this page "
                    f"under non-canonical branch '{head}' — recording incomplete"
                )
    except (OSError, json.JSONDecodeError):
        pass


def check_pr_body(body: str | None) -> list[str]:
    """Return the required section headings missing from a fix PR's body."""
    text = (body or "").lower()
    return [s for s in REQUIRED_PR_SECTIONS if s.lower() not in text]


# ---- derivation -------------------------------------------------------------


def build_record(article: dict, verdict: dict | None, pr: dict | None,
                 slug: str) -> dict:
    """Build the canonical ledger record from the queue, verdict, and PR state.

    `attempts` accrues the consecutive `incomplete` retries: it starts from the
    prior count the selector carried in (`article["attempts"]`), is incremented
    by one on another incomplete outcome, and is reset to 0 the moment the page
    reaches any completed status. The selector backs a page off once it hits
    ATTEMPT_CAP, so this counter is the loop guard.
    """
    prior_attempts = int(article.get("attempts") or 0)
    rec = {
        "path": article["path"],
        "slug": slug,
        "lane": article["lane"],
        "status": "incomplete",
        "pr": None,
        "pr_number": 0,
        "head_sha": "",
        "fixes": 0,
        "skipped_findings": 0,
        "retirement": bool(verdict.get("retirement")) if verdict else False,
        "note": None,
        "attempts": prior_attempts + 1,
        "reviewed_at": datetime.now(timezone.utc).date().isoformat(),
    }

    if verdict is None:
        rec["note"] = "worker produced no verdict"
        return rec

    rec["fixes"] = int(verdict.get("fixes") or 0)
    rec["skipped_findings"] = int(verdict.get("skipped_findings") or 0)
    v = verdict.get("verdict")

    if v == "clean":
        rec["status"] = "clean"
        rec["note"] = verdict.get("reason")
        rec["attempts"] = 0
    elif v == "skipped":
        rec["status"] = "skipped"
        rec["note"] = verdict.get("reason") or "skipped by reviewer"
        rec["attempts"] = 0
    elif v == "fixed":
        if pr:
            rec["status"] = "reviewed"
            rec["pr"] = pr.get("url")
            rec["pr_number"] = int(pr.get("number") or 0)
            rec["head_sha"] = pr.get("headRefOid") or ""
            rec["attempts"] = 0
        else:
            rec["status"] = "incomplete"
            rec["note"] = f"verdict 'fixed' but no PR on {branch_for(slug, rec['retirement'])}"
    else:
        rec["note"] = f"unrecognized verdict {v!r}"

    return rec


# ---- outputs ----------------------------------------------------------------


def upload(record: dict, slug: str, uri: str) -> None:
    """Upload the record to <uri>/<slug>.json via the aws CLI (stdin)."""
    key = f"{uri.rstrip('/')}/{slug}.json"
    try:
        subprocess.run(
            ["aws", "s3", "cp", "-", key],
            input=json.dumps(record, indent=2) + "\n",
            text=True, check=True,
        )
        log(f"uploaded ledger record to {key}")
    except FileNotFoundError:
        warn("aws CLI not available; ledger record not uploaded")
    except subprocess.CalledProcessError as e:
        warn(f"ledger upload failed for {slug} ({e})")


def emit_outputs(record: dict) -> None:
    """Write dispatch/pr_number/head_sha to $GITHUB_OUTPUT (or stdout)."""
    dispatch = "true" if record["status"] == "reviewed" else "false"
    lines = [
        f"dispatch={dispatch}",
        f"pr_number={record['pr_number']}",
        f"head_sha={record['head_sha']}",
        f"status={record['status']}",
    ]
    out_path = os.environ.get("GITHUB_OUTPUT")
    if out_path:
        with open(out_path, "a") as f:
            f.write("\n".join(lines) + "\n")
    for line in lines:
        print(line)


# ---- main -------------------------------------------------------------------


def run(args) -> int:
    article = load_queue_article(Path(args.queue))
    slug = article["slug"]
    verdict = load_verdict(Path(args.verdict) if args.verdict else None)
    retirement = bool(verdict.get("retirement")) if verdict else False
    branch = branch_for(slug, retirement)

    want_pr = bool(verdict) and verdict.get("verdict") == "fixed"
    pr = fetch_pr(branch, args.pr_json) if want_pr else None
    if want_pr and not pr and args.pr_json is None:
        scan_misnamed_sibling(slug)

    record = build_record(article, verdict, pr, slug)

    # PR-body section check (non-blocking) for fix PRs.
    if record["status"] == "reviewed" and pr is not None:
        missing = check_pr_body(pr.get("body"))
        if missing:
            warn(f"PR #{record['pr_number']} body missing sections: {', '.join(missing)}")
            if args.pr_json is None:
                subprocess.run(
                    ["gh", "pr", "comment", str(record["pr_number"]), "--body",
                     "Automated review note: this PR's description is missing the "
                     f"following required sections: {', '.join(missing)}."],
                    check=False,
                )

    out_path = Path(args.out)
    out_path.write_text(json.dumps(record, indent=2) + "\n")
    log(f"status={record['status']} slug={slug} -> {out_path}")

    uri = os.environ.get("CONTENT_REVIEW_LEDGER_URI", "").strip()
    if uri:
        upload(record, slug, uri)
    else:
        warn("CONTENT_REVIEW_LEDGER_URI unset; ledger record written locally only")

    emit_outputs(record)
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
        queue.write_text(json.dumps({
            "articles": [{
                "path": "content/docs/iac/concepts/converters.md",
                "slug": "docs-iac-concepts-converters",
                "lane": "priority",
            }]
        }))
        article = load_queue_article(queue)

        # No verdict -> incomplete.
        rec = build_record(article, None, None, article["slug"])
        check("no-verdict -> incomplete", rec["status"] == "incomplete")
        check("incomplete has reviewed_at", bool(rec["reviewed_at"]))
        check("incomplete bumps attempts from 0 -> 1", rec["attempts"] == 1)
        check("all canonical fields present", set(rec) == {
            "path", "slug", "lane", "status", "pr", "pr_number", "head_sha",
            "fixes", "skipped_findings", "retirement", "note", "attempts",
            "reviewed_at"})

        # Repeated incomplete accrues against the prior count the selector carried.
        retried = {**article, "attempts": 2}
        rec = build_record(retried, {"verdict": "fixed"}, None, article["slug"])
        check("incomplete accrues prior attempts (2 -> 3)", rec["attempts"] == 3)

        # Clean verdict resets the retry counter.
        rec = build_record(retried, {"verdict": "clean", "reason": "accurate"},
                           None, article["slug"])
        check("clean verdict -> clean", rec["status"] == "clean" and rec["pr"] is None)
        check("clean resets attempts to 0", rec["attempts"] == 0)

        # Fixed + PR -> reviewed with derived facts.
        pr = {"number": 19731, "state": "OPEN",
              "headRefOid": "5344e12aa5f08646ead32d92be3b76ca9f6a0302",
              "url": "https://github.com/pulumi/docs/pull/19731", "body": ""}
        rec = build_record(article, {"verdict": "fixed", "fixes": 1}, pr,
                           article["slug"])
        check("fixed+PR -> reviewed", rec["status"] == "reviewed")
        check("derived pr_number", rec["pr_number"] == 19731)
        check("derived head_sha", rec["head_sha"].startswith("5344e12"))
        check("fixes carried", rec["fixes"] == 1)
        check("reviewed resets attempts to 0", rec["attempts"] == 0)

        # Fixed + no PR -> incomplete.
        rec = build_record(article, {"verdict": "fixed"}, None, article["slug"])
        check("fixed+no-PR -> incomplete", rec["status"] == "incomplete")

        # Section check.
        check("section check flags missing",
              set(check_pr_body("## Why this page\n## Verification")) ==
              {"Fixes applied", "Findings not applied", "Screenshot check",
               "Rendered content"})
        check("section check passes complete body",
              check_pr_body("\n".join(f"## {s}" for s in REQUIRED_PR_SECTIONS)) == [])

    if failures:
        print(f"\n{len(failures)} failure(s)", file=sys.stderr)
        return 1
    print("\nall record-review self-tests passed")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description="Record a content-review outcome to the S3 ledger.")
    p.add_argument("--queue", help="single-article queue JSON (.content-review-queue.json)")
    p.add_argument("--verdict", help="model verdict sentinel (.content-review-verdict.json)")
    p.add_argument("--pr-json", help="inject gh PR JSON (file path or '-' for stdin); for tests")
    p.add_argument("--out", default=".content-review-ledger.json",
                   help="local ledger artifact path")
    p.add_argument("--self-test", action="store_true", help="run built-in smoke checks")
    args = p.parse_args()

    if args.self_test:
        return self_test()
    if not args.queue:
        p.error("--queue is required")
    return run(args)


if __name__ == "__main__":
    sys.exit(main())

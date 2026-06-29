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
  * sentinel absent, run succeeded, no branch pushed     -> status "clean"
  * sentinel absent, run failed OR a branch exists       -> status "incomplete"

The last two cases extend the file's "derive facts from observable state, not
self-report" principle to the verdict itself: a model that completes its turn
and pushes no `content-review/<slug>` branch reviewed the page and changed
nothing — that is "clean", regardless of whether it remembered to write the
sentinel. A branch with no PR (a half-applied fix) or a failed/timed-out run is
genuinely "incomplete" and stays due for retry.

Canonical record (every field always present):
  { path, slug, lane, status, pr, pr_number, head_sha, fixes,
    skipped_findings, retirement, note, attempts, clarity_flag,
    tier, score, monthly_visits, traffic_available, reviewed_at }

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


def _maybe_int(v):
    try:
        return int(v)
    except (TypeError, ValueError):
        return None


def load_queue_article(queue_path: Path) -> dict:
    """Return the single article from the worker queue, with its selection signal.

    Beyond the bookkeeping fields (path/slug/lane/attempts), this carries the
    selection facts the dispatcher chose the page on — tier, score, monthly
    visits, and whether the traffic snapshot was available that run. They're
    persisted onto the ledger record so the versioned ledger is a complete,
    self-contained metrics source (outcome AND why-it-was-picked), reconstructable
    from S3 object versions without depending on the ~90-day run logs.
    """
    data = json.loads(queue_path.read_text())
    articles = data.get("articles") or []
    if not articles:
        raise SystemExit(f"record-review: no articles in {queue_path}")
    a = articles[0]
    path = a["path"]
    traffic = data.get("traffic") or {}
    return {
        "path": path,
        "slug": a.get("slug") or slugify(path),
        "lane": a.get("lane") or "priority",
        # Prior incomplete-retry count, carried from the ledger by the selector.
        # build_record increments it on another incomplete, resets it on success.
        "attempts": int(a.get("attempts") or 0),
        # Selection signal (None when absent, e.g. a --paths manual dispatch).
        "tier": _maybe_int(a.get("tier")),
        "score": a.get("score"),
        "monthly_visits": _maybe_int(a.get("monthly_visits")),
        "traffic_available": bool(traffic.get("available")),
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


def unresolved_draft_markers(body: str | None) -> int:
    """Count composer scaffolding the model should have resolved before publish.

    The composer seeds the draft with `<TODO>` markers and `<!-- LINT-RESULT -->`
    (the latter stamped by the re-lint gate, which runs before this). Either left
    in a published body means the model shipped the scaffold — worth a
    non-blocking nudge, mirroring the pre-merge `no-todo-tokens` guard.
    """
    text = body or ""
    return text.count("<TODO") + text.count("<!-- LINT-RESULT -->")


def canonical_branch_pushed(slug: str) -> bool:
    """True if either canonical review branch was pushed to origin.

    Used only when the sentinel is absent, to tell a clean review (no branch)
    from a half-applied fix (branch, no PR). Best-effort: a probe failure
    returns False, biasing an unknowable case toward clean rather than a
    perpetual incomplete retry.
    """
    refs = [f"refs/heads/{branch_for(slug, r)}" for r in (False, True)]
    try:
        out = subprocess.run(
            ["git", "ls-remote", "--heads", "origin", *refs],
            capture_output=True, text=True, check=False,
        )
    except FileNotFoundError:
        return False
    return out.returncode == 0 and bool(out.stdout.strip())


# ---- derivation -------------------------------------------------------------


def build_record(article: dict, verdict: dict | None, pr: dict | None,
                 slug: str, claude_succeeded: bool = False,
                 branch_exists: bool = False) -> dict:
    """Build the canonical ledger record from the queue, verdict, and PR state.

    `attempts` accrues the consecutive `incomplete` retries: it starts from the
    prior count the selector carried in (`article["attempts"]`), is incremented
    by one on another incomplete outcome, and is reset to 0 the moment the page
    reaches any completed status. The selector backs a page off once it hits
    ATTEMPT_CAP, so this counter is the loop guard.

    When the sentinel is absent the status is derived from observable state
    rather than defaulted to incomplete: a run that succeeded and pushed no
    canonical branch (`claude_succeeded and not branch_exists`) is recorded
    "clean"; a failed run, or one that left a branch behind without a PR, is
    "incomplete" and stays due.
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
        "clarity_flag": bool(verdict.get("clarity_flag")) if verdict else False,
        # Selection signal (carried from the queue) — persisted so the versioned
        # ledger captures why the page was picked, not just the outcome.
        "tier": article.get("tier"),
        "score": article.get("score"),
        "monthly_visits": article.get("monthly_visits"),
        "traffic_available": bool(article.get("traffic_available")),
        "reviewed_at": datetime.now(timezone.utc).date().isoformat(),
    }

    if verdict is None:
        if claude_succeeded and not branch_exists:
            # Successful review that produced no branch == clean, even though the
            # model skipped the sentinel. Advance the clock instead of looping.
            rec["status"] = "clean"
            rec["note"] = "no verdict sentinel; run succeeded with no changes (derived clean)"
            rec["attempts"] = 0
        else:
            why = "run did not succeed" if not claude_succeeded else "a branch exists without a PR"
            rec["note"] = f"worker produced no verdict ({why})"
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

    # Only needed when the sentinel is absent: distinguish a clean review (no
    # branch) from a half-applied fix (branch, no PR). Skip the probe otherwise.
    claude_succeeded = (args.claude_outcome or "").strip().lower() == "success"
    branch_exists = False
    if verdict is None:
        branch_exists = (
            args.branch_exists == "true" if args.branch_exists is not None
            else canonical_branch_pushed(slug)
        )

    record = build_record(article, verdict, pr, slug,
                          claude_succeeded=claude_succeeded,
                          branch_exists=branch_exists)

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
        leftover = unresolved_draft_markers(pr.get("body"))
        if leftover:
            warn(f"PR #{record['pr_number']} body still has {leftover} unresolved "
                 "draft marker(s) (<TODO> / unstamped lint placeholder)")

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
            "traffic": {"available": True},
            "articles": [{
                "path": "content/docs/iac/concepts/converters.md",
                "slug": "docs-iac-concepts-converters",
                "lane": "priority",
                "tier": 2,
                "score": 137.5,
                "monthly_visits": 842,
            }]
        }))
        article = load_queue_article(queue)
        check("queue article carries the selection signal",
              article["tier"] == 2 and article["score"] == 137.5
              and article["monthly_visits"] == 842 and article["traffic_available"] is True)

        # No verdict, no signal -> incomplete (the conservative default).
        rec = build_record(article, None, None, article["slug"])
        check("no-verdict (no signal) -> incomplete", rec["status"] == "incomplete")
        check("incomplete has reviewed_at", bool(rec["reviewed_at"]))
        check("incomplete bumps attempts from 0 -> 1", rec["attempts"] == 1)

        # No verdict, but the run succeeded and pushed no branch -> derived clean.
        rec = build_record(article, None, None, article["slug"],
                           claude_succeeded=True, branch_exists=False)
        check("no-verdict + success + no branch -> clean", rec["status"] == "clean")
        check("derived-clean resets attempts to 0", rec["attempts"] == 0)
        check("derived-clean notes the derivation",
              "derived clean" in (rec["note"] or ""))

        # No verdict + success but a branch was left behind -> incomplete (half fix).
        rec = build_record(article, None, None, article["slug"],
                           claude_succeeded=True, branch_exists=True)
        check("no-verdict + success + branch -> incomplete", rec["status"] == "incomplete")

        # No verdict + run failed -> incomplete even with no branch.
        rec = build_record(article, None, None, article["slug"],
                           claude_succeeded=False, branch_exists=False)
        check("no-verdict + failed run -> incomplete", rec["status"] == "incomplete")
        check("all canonical fields present", set(rec) == {
            "path", "slug", "lane", "status", "pr", "pr_number", "head_sha",
            "fixes", "skipped_findings", "retirement", "note", "attempts",
            "clarity_flag", "tier", "score", "monthly_visits",
            "traffic_available", "reviewed_at"})
        check("no-verdict clarity_flag defaults False", rec["clarity_flag"] is False)
        check("selection signal persisted on the record",
              rec["tier"] == 2 and rec["score"] == 137.5
              and rec["monthly_visits"] == 842 and rec["traffic_available"] is True)

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

        # clarity_flag carries from the verdict onto the ledger (durable even on
        # an otherwise-clean page) and stays False when absent.
        rec = build_record(article, {"verdict": "clean", "reason": "reads fine",
                                     "clarity_flag": True}, None, article["slug"])
        check("clarity_flag carried from verdict", rec["clarity_flag"] is True)
        check("clarity_flag clean still clean", rec["status"] == "clean")
        rec = build_record(article, {"verdict": "fixed", "fixes": 2}, pr, article["slug"])
        check("clarity_flag absent -> False", rec["clarity_flag"] is False)

        # Section check.
        check("section check flags missing",
              set(check_pr_body("## Why this page\n## Verification")) ==
              {"Fixes applied", "Findings not applied", "Screenshot check",
               "Rendered content"})
        check("section check passes complete body",
              check_pr_body("\n".join(f"## {s}" for s in REQUIRED_PR_SECTIONS)) == [])

        # Unresolved-draft-marker guard (non-blocking parity with no-todo-tokens).
        check("counts leftover TODO + lint placeholder",
              unresolved_draft_markers("a <TODO: fix> b <!-- LINT-RESULT --> c") == 2)
        check("clean published body has zero markers",
              unresolved_draft_markers("## Why this page\nall resolved") == 0)

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
    p.add_argument("--claude-outcome",
                   help="GitHub step outcome of the review run (success/failure/cancelled). "
                        "With no sentinel, 'success' + no pushed branch => clean; anything else => incomplete.")
    p.add_argument("--branch-exists", choices=["true", "false"],
                   help="inject canonical-branch existence (tests); omit to probe origin via git ls-remote")
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

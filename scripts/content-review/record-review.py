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
The sentinel may also carry an `applied` array (per-fix provenance, consumed
by the workflow's verify-fix-scope.py gate); the ledger record ignores it.

Outcome derivation:
  * verdict "fixed"  + PR on content-review/<slug>      -> status "reviewed"
  * verdict "clean"                                      -> status "clean"
  * verdict "skipped"                                    -> status "skipped"
  * verdict "reported"                                   -> status "reported"
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
  { path, slug, lane, status, pr, pr_number, last_pr, last_pr_number, head_sha,
    fixes, skipped_findings, glowup_degraded, retirement,
    note, attempts,
    clarity_flag, tier, score, monthly_visits, traffic_available, signals,
    signals_available, reviewed_at }

The record is rebuilt from scratch every review, which is right for an outcome
but wrong for the page's accumulated state: a review that opens no PR — a
`clean` verdict, however many findings it banked — used to reset the pointer to
the last review PR, and the glow-up lane could then find nothing to execute
(#20984). `load_prior` reads the record back before overwriting it and
`build_record` carries three things forward explicitly: `last_pr`/
`last_pr_number` (the durable pointer; `pr_number` still means "the PR this
review opened"), a `clarity_flag` no verdict has explicitly cleared, and the
banked count when a glow-up executed nothing at all.

The record is written locally (audit artifact) and, when CONTENT_REVIEW_LEDGER_URI
is set, uploaded to <uri>/<slug>.json with reviewed_at stamped to today (UTC).
Degrades gracefully: a missing bucket URI skips the upload (the page reappears
next cycle) rather than failing the run.

Self-contained — run the smoke checks with `python3 record-review.py --self-test`.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import re
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

# PR-body sections the review skill mandates per mode; the post-create check
# warns (never blocks) when a PR's body is missing one. Keep the glowup list in
# lockstep with compose-pr-body.py's GLOWUP_SECTIONS (test_compose_pr_body.py
# cross-imports both to enforce it).
MODE_PR_SECTIONS = {
    "fix": [
        "Why this page",
        "Fixes applied",
        "Findings not applied",
        "Screenshot check",
        "Rendered content",
        "Verification",
    ],
    "glowup": [
        "Why this page",
        "Backlog executed",
        "Backlog declined",
        "Secondary sweep",
        "Screenshot check",
        "Verification",
    ],
}
REQUIRED_PR_SECTIONS = MODE_PR_SECTIONS["fix"]  # back-compat alias


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
        "mode": a.get("mode") or "fix",
        # Prior incomplete-retry count, carried from the ledger by the selector.
        # build_record increments it on another incomplete, resets it on success.
        "attempts": int(a.get("attempts") or 0),
        # Selection signal (None when absent, e.g. a --paths manual dispatch).
        "tier": _maybe_int(a.get("tier")),
        "score": a.get("score"),
        "monthly_visits": _maybe_int(a.get("monthly_visits")),
        "traffic_available": bool(traffic.get("available")),
        # Reader signals (GSC/feedback figures + multipliers + low_ctr_flag),
        # verbatim from the queue entry; null on a signal-blind run.
        "signals": a.get("signals"),
        "signals_available": bool((data.get("reader_signals") or {}).get("available")),
        # Stale-claim markers in full (entity_key/verdict/evidence/source/...).
        # carry_markers() needs them to decide which survive this review.
        "stale_claim_markers": a.get("stale_claim_markers") or [],
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


def branch_for(slug: str, retirement: bool, glowup: bool = False) -> str:
    if glowup:
        return f"{BRANCH_PREFIX}glowup-{slug}"
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


def load_prior(slug: str, uri: str, prior_json: str | None) -> dict | None:
    """The page's CURRENT ledger record, read back before this run overwrites it.

    The record is rebuilt from scratch every review, so anything this run cannot
    observe for itself has to come from here. Read from S3 rather than from the
    queue because it also covers a `--paths` manual dispatch (whose queue carries
    no ledger fields at all) and because it keeps `queue_json`, already the
    dispatch's largest input, from growing.

    Returns None on any failure — no aws CLI, no object yet, unreadable JSON.
    A missed prior is exactly the behavior that shipped before this existed, so
    the degradation is "no carry-forward", never "no ledger write".

    `prior_json` (a file path, or '-' for stdin) injects the record for tests,
    mirroring --pr-json.
    """
    if prior_json is not None:
        raw = sys.stdin.read() if prior_json == "-" else Path(prior_json).read_text()
        raw = raw.strip()
        if not raw:
            return None
        try:
            rec = json.loads(raw)
        except json.JSONDecodeError:
            return None
        return rec if isinstance(rec, dict) else None
    if not uri:
        return None
    key = f"{uri.rstrip('/')}/{slug}.json"
    try:
        out = subprocess.run(["aws", "s3", "cp", key, "-"],
                             capture_output=True, text=True, check=False)
    except OSError:
        log("aws CLI not available; no prior ledger record to carry forward")
        return None
    if out.returncode != 0:
        # A missing key and a broken credential both exit non-zero, and only one
        # of them is benign. Reporting both as "first review" would hide the
        # case that silently reintroduces the bug this carry-forward fixes — a
        # page with real history recorded as if it had none — so only a genuine
        # 404 stays quiet.
        err = (out.stderr or "").strip()
        if re.search(r"\b(404|Not Found|NoSuchKey)\b", err, re.I):
            log(f"no prior ledger record at {key} (first review of this page)")
        else:
            warn(f"could not read the prior ledger record at {key}; carrying "
                 f"nothing forward, which may reset this page's PR pointer and "
                 f"banked counters: {err[:200]}")
        return None
    try:
        rec = json.loads(out.stdout)
    except json.JSONDecodeError:
        warn(f"prior ledger record at {key} is unreadable; not carrying it forward")
        return None
    return rec if isinstance(rec, dict) else None


def last_pr_from(prior: dict | None) -> tuple[str | None, int]:
    """The most recent review PR known for this page, from the prior record.

    Prefers the prior record's own `pr`/`pr_number` — the PR THAT review opened
    — and falls back to the pointer it was itself carrying. The fallback is the
    load-bearing half: without it the reference survives exactly one PR-less
    review, and pages accumulate PR-less reviews (a `clean` verdict opens no PR,
    however many findings it banked).
    """
    if not isinstance(prior, dict):
        return None, 0
    n = int(prior.get("pr_number") or 0)
    if n:
        return prior.get("pr"), n
    return prior.get("last_pr"), int(prior.get("last_pr_number") or 0)


def carried_clarity(verdict: dict | None, prior: dict | None) -> bool:
    """`clarity_flag` from the verdict when it states one, from the prior record
    when it doesn't.

    A sentinel that omits the key is not asserting the page reads clearly — the
    glow-up sentinel never carried it at all, so every glow-up silently cleared
    a flag it had just been selected for. Absence carries; an explicit `false`
    clears. The flag is therefore sticky by design: only a review that says so
    can put it down.
    """
    if verdict is not None and "clarity_flag" in verdict:
        return bool(verdict.get("clarity_flag"))
    return bool((prior or {}).get("clarity_flag"))


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
            head_slug = head[len(BRANCH_PREFIX):].removeprefix("retire-").removeprefix("glowup-")
            if head_slug == slug:
                warn(
                    f"PR #{pr.get('number')} ({pr.get('url')}) reviews this page "
                    f"under non-canonical branch '{head}' — recording incomplete"
                )
    except (OSError, json.JSONDecodeError):
        pass


def check_pr_body(body: str | None, mode: str = "fix") -> list[str]:
    """Return the required section headings missing from a PR's body."""
    text = (body or "").lower()
    sections = MODE_PR_SECTIONS.get(mode, REQUIRED_PR_SECTIONS)
    return [s for s in sections if s.lower() not in text]


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
    refs = [f"refs/heads/{branch_for(slug, False)}",
            f"refs/heads/{branch_for(slug, True)}",
            f"refs/heads/{branch_for(slug, False, glowup=True)}"]
    try:
        out = subprocess.run(
            ["git", "ls-remote", "--heads", "origin", *refs],
            capture_output=True, text=True, check=False,
        )
    except FileNotFoundError:
        return False
    return out.returncode == 0 and bool(out.stdout.strip())


# ---- derivation -------------------------------------------------------------


# A stale-claim marker survives this many reviews that saw it and did not
# resolve it; after that it is kept but flagged `escalated`, which stops
# select-articles.py boosting the page (see MARKER_ESCALATION_CAP there).
MARKER_ESCALATION_CAP = 2


def carry_markers(article: dict, verdict: dict | None) -> list[dict]:
    """Stale-claim markers that outlive this review, with their retry state.

    The nightly re-verification writes a marker when a volatile claim goes
    contradicted; the marker boosts the page into this worker's queue. Before
    this function existed the marker simply vanished when the review's ledger
    record landed, whether or not anything had been done about it — so a review
    that missed the finding silently cleared the flag and the entity went back
    into the pool to be re-flagged, re-boosted, and re-missed on a ~2-day cycle
    (observed end-to-end in pulumi/docs#20927).

    A marker is retired only when the verdict names its entity in
    `resolved_claims` — the worker asserting it either fixed the claim or
    determined the flag was wrong. Everything else is carried forward with
    `unresolved_reviews` incremented, and flagged `escalated` once that count
    reaches MARKER_ESCALATION_CAP so a human is the next step rather than
    another identical pass.
    """
    resolved = {str(k) for k in ((verdict or {}).get("resolved_claims") or [])}
    carried: list[dict] = []
    for m in article.get("stale_claim_markers") or []:
        if not isinstance(m, dict):
            continue
        if m.get("entity_key") in resolved:
            continue
        seen = int(m.get("unresolved_reviews") or 0) + 1
        carried.append({**m, "unresolved_reviews": seen,
                        "escalated": seen >= MARKER_ESCALATION_CAP})
    return carried


def build_record(article: dict, verdict: dict | None, pr: dict | None,
                 slug: str, claude_succeeded: bool = False,
                 branch_exists: bool = False, prior: dict | None = None) -> dict:
    """Build the canonical ledger record from the queue, verdict, and PR state.

    `prior` is the page's previous record (see load_prior). It is read from, never
    merged into: every field below is still derived from this run, and the three
    things the prior contributes — the last-PR pointer, a sticky `clarity_flag`,
    and the banked count a no-op glow-up must not zero — are each taken
    explicitly. A blanket merge would leak a stale `status` or `fixes` forward and
    make one record describe two different reviews.

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
        "mode": article.get("mode") or "fix",
        "status": "incomplete",
        "pr": None,
        "pr_number": 0,
        # `pr_number` keeps its original meaning — the PR THIS review opened, 0
        # when it opened none — so the versioned ledger's metrics stay
        # comparable across history. The durable pointer to the page's most
        # recent review PR is separate, and both consumers prefer `pr_number`
        # and fall back to it: select-glowup.py folds it into the
        # `source_pr_number` it stamps on the queue — the only form the
        # unprivileged worker gets it in — and build-glowup-backlog.py takes the
        # same fallback in its own dispatcher-side ledger read.
        "last_pr": last_pr_from(prior)[0],
        "last_pr_number": last_pr_from(prior)[1],
        "head_sha": "",
        "fixes": 0,
        "skipped_findings": 0,
        # True only when a glow-up verdict executed and declined nothing while
        # the page carried banked debt: the backlog never reached the model, so
        # the counters below are the PRIOR review's, carried rather than
        # measured. The selector needs this bit to tell "declined 17" (real
        # adjudication, cool down) from "never saw 17" (still owed).
        #
        # select-glowup.py routes a page carrying this flag to a FIX-lane
        # repair rather than re-queueing the glow-up: re-running a recovery
        # that already failed fails the same way, and the fix lane's review
        # writes the findings record that makes the next glow-up real. That
        # retired the old consecutive-run counter this flag used to need.
        "glowup_degraded": False,
        "retirement": bool(verdict.get("retirement")) if verdict else False,
        "note": None,
        "attempts": prior_attempts + 1,
        "clarity_flag": carried_clarity(verdict, prior),
        # Selection signal (carried from the queue) — persisted so the versioned
        # ledger captures why the page was picked, not just the outcome.
        "tier": article.get("tier"),
        "score": article.get("score"),
        "monthly_visits": article.get("monthly_visits"),
        "traffic_available": bool(article.get("traffic_available")),
        "signals": article.get("signals"),
        "signals_available": bool(article.get("signals_available")),
        "reviewed_at": datetime.now(timezone.utc).date().isoformat(),
    }
    markers = carry_markers(article, verdict)
    if markers:
        rec["stale_claims"] = markers

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
    elif v == "reported":
        # The report-only lane (pulumi/docs#20996): the page's claims were
        # extracted, verified, and written to the claims index, and nothing was
        # edited because nothing here may be. A completed status like "clean" —
        # it advances the staleness clock, which is what laps the lane across
        # the 248-page CLI reference instead of re-reading the same pages.
        rec["status"] = "reported"
        rec["note"] = verdict.get("reason") or "claims recorded; no edits (generated page)"
        rec["attempts"] = 0
    elif v in ("fixed", "glowup"):
        if pr:
            # "glowup" is a completed status like "reviewed": it advances the
            # staleness clock (any non-incomplete status does) and drives the
            # glow-up selector's cooldown.
            rec["status"] = "reviewed" if v == "fixed" else "glowup"
            rec["pr"] = pr.get("url")
            rec["pr_number"] = int(pr.get("number") or 0)
            rec["last_pr"] = rec["pr"]
            rec["last_pr_number"] = rec["pr_number"]
            rec["head_sha"] = pr.get("headRefOid") or ""
            rec["attempts"] = 0
            # A glow-up that executed nothing and declined nothing did not touch
            # the backlog: its recovery degraded (see build-glowup-backlog.py)
            # and the page is still owed its rehab. Reporting 0 banked here would
            # drop it out of the glow-up selector, which keys on
            # skipped_findings/clarity_flag, AND start a 90-day cooldown — so the
            # lane would delete the debt it had just failed to collect. #20984.
            if v == "glowup" and rec["fixes"] == 0 and rec["skipped_findings"] == 0:
                prior_banked = int((prior or {}).get("skipped_findings") or 0)
                if prior_banked or rec["clarity_flag"]:
                    rec["skipped_findings"] = prior_banked
                    rec["glowup_degraded"] = True
                    rec["note"] = (
                        "glow-up executed no backlog; prior counters preserved "
                        "and the page routes to a fix-lane repair")
        else:
            rec["status"] = "incomplete"
            branch = branch_for(slug, rec["retirement"], glowup=(v == "glowup"))
            rec["note"] = f"verdict {v!r} but no PR on {branch}"
    else:
        rec["note"] = f"unrecognized verdict {v!r}"

    return rec


# ---- output -----------------------------------------------------------------


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


# ---- main -------------------------------------------------------------------


def run(args) -> int:
    article = load_queue_article(Path(args.queue))
    slug = article["slug"]
    verdict = load_verdict(Path(args.verdict) if args.verdict else None)
    retirement = bool(verdict.get("retirement")) if verdict else False
    glowup = bool(verdict and verdict.get("verdict") == "glowup")
    branch = branch_for(slug, retirement, glowup=glowup)

    want_pr = bool(verdict) and verdict.get("verdict") in ("fixed", "glowup")
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

    # Read the record this run is about to overwrite, so the facts it cannot
    # observe for itself (the last-PR pointer, a standing clarity flag, an
    # unexecuted backlog) survive instead of being reset to their defaults.
    uri = os.environ.get("CONTENT_REVIEW_LEDGER_URI", "").strip()
    prior = load_prior(slug, uri, args.prior)

    record = build_record(article, verdict, pr, slug,
                          claude_succeeded=claude_succeeded,
                          branch_exists=branch_exists, prior=prior)

    # PR-body section check (non-blocking) for fix and glow-up PRs.
    if record["status"] in ("reviewed", "glowup") and pr is not None:
        missing = check_pr_body(pr.get("body"), record.get("mode") or "fix")
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

    if uri:
        upload(record, slug, uri)
    else:
        warn("CONTENT_REVIEW_LEDGER_URI unset; ledger record written locally only")

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
        signals_block = {
            "gsc": {"impressions": 15234, "ctr": 0.0205, "opportunity": 0.41,
                    "multiplier": 1.1025, "low_ctr_flag": True},
            "feedback": {"yes": 4, "no": 9, "neg_rate": 0.6923, "multiplier": 1.27},
        }
        queue.write_text(json.dumps({
            "traffic": {"available": True},
            "reader_signals": {"available": True},
            "articles": [{
                "path": "content/docs/iac/concepts/converters.md",
                "slug": "docs-iac-concepts-converters",
                "lane": "priority",
                "tier": 2,
                "score": 137.5,
                "monthly_visits": 842,
                "signals": signals_block,
            }]
        }))
        article = load_queue_article(queue)
        check("queue article carries the selection signal",
              article["tier"] == 2 and article["score"] == 137.5
              and article["monthly_visits"] == 842 and article["traffic_available"] is True)
        check("queue article carries reader signals verbatim",
              article["signals"] == signals_block and article["signals_available"] is True)

        # A signal-blind queue (no reader_signals block, e.g. a --paths manual
        # dispatch or a pre-export run) records null/false, never fabricates.
        blind = d / "queue-blind.json"
        blind.write_text(json.dumps({
            "traffic": {"available": True},
            "articles": [{"path": "content/docs/iac/concepts/converters.md",
                          "slug": "docs-iac-concepts-converters"}]
        }))
        blind_article = load_queue_article(blind)
        check("signal-blind queue -> signals null, signals_available False",
              blind_article["signals"] is None
              and blind_article["signals_available"] is False)
        # --- stale-claim marker retention -------------------------------
        marker = {"entity_key": "version/pulumi-package", "verdict": "contradicted",
                  "evidence": "CHANGELOG says 3.163.0", "source": "gh release view",
                  "checked_at": "2026-08-15"}
        marked = {**article, "stale_claim_markers": [marker]}

        rec_m = build_record(marked, {"verdict": "clean", "reason": "accurate"},
                             None, marked["slug"])
        check("a review that resolves nothing carries the marker forward",
              [m["entity_key"] for m in rec_m["stale_claims"]] == ["version/pulumi-package"])
        check("carried marker counts the miss",
              rec_m["stale_claims"][0]["unresolved_reviews"] == 1
              and rec_m["stale_claims"][0]["escalated"] is False)
        check("carried marker keeps its evidence",
              rec_m["stale_claims"][0]["evidence"] == "CHANGELOG says 3.163.0")

        rec_r = build_record(marked, {"verdict": "fixed", "fixes": 1,
                                      "resolved_claims": ["version/pulumi-package"]},
                             None, marked["slug"])
        check("a resolved marker retires", "stale_claims" not in rec_r)

        second = {**article, "stale_claim_markers": [rec_m["stale_claims"][0]]}
        rec_e = build_record(second, {"verdict": "clean", "reason": "x"},
                             None, second["slug"])
        check("second unresolved review escalates the marker",
              rec_e["stale_claims"][0]["unresolved_reviews"] == 2
              and rec_e["stale_claims"][0]["escalated"] is True)

        # The other half of the round-trip: select-articles.py hands escalated
        # markers through, so they must survive rather than be filtered out
        # here — otherwise the ledger loses them and the entity re-enters the
        # nightly pool.
        esc_marker = {**marker, "entity_key": "version/old-miss",
                      "unresolved_reviews": 2, "escalated": True}
        with_esc = {**article, "stale_claim_markers": [marker, esc_marker]}
        rec_esc = build_record(with_esc, {"verdict": "clean", "reason": "x"},
                               None, with_esc["slug"])
        carried = {m["entity_key"]: m for m in rec_esc["stale_claims"]}
        check("escalated marker persists through a review",
              "version/old-miss" in carried)
        check("escalated marker stays escalated and keeps counting",
              carried["version/old-miss"]["escalated"] is True
              and carried["version/old-miss"]["unresolved_reviews"] == 3)
        check("an escalated marker can still be resolved",
              "stale_claims" not in build_record(
                  {**article, "stale_claim_markers": [esc_marker]},
                  {"verdict": "fixed", "fixes": 1,
                   "resolved_claims": ["version/old-miss"]},
                  None, article["slug"]))

        rec_none = build_record(article, {"verdict": "clean", "reason": "x"},
                                None, article["slug"])
        check("no markers -> no stale_claims key", "stale_claims" not in rec_none)

        rec_incomplete = build_record(marked, None, None, marked["slug"])
        check("marker survives an incomplete run too",
              rec_incomplete["stale_claims"][0]["unresolved_reviews"] == 1)

        blind_rec = build_record(blind_article, None, None, blind_article["slug"])
        check("signal-blind record persists null/false",
              blind_rec["signals"] is None and blind_rec["signals_available"] is False)

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
            "path", "slug", "lane", "mode", "status", "pr", "pr_number",
            "last_pr", "last_pr_number", "head_sha",
            "fixes", "skipped_findings", "glowup_degraded",
            "retirement", "note",
            "attempts", "clarity_flag", "tier", "score", "monthly_visits",
            "traffic_available", "signals", "signals_available", "reviewed_at"})
        check("mode defaults to fix", rec["mode"] == "fix")

        # Glow-up outcomes: a completed glowup advances the clock; PR-less is
        # incomplete; the branch carries the glowup- prefix.
        check("glowup branch form",
              branch_for("docs-x", False, glowup=True) == "content-review/glowup-docs-x")
        g_article = dict(article, mode="glowup", lane="glowup")
        g_verdict = {"verdict": "glowup", "reason": "", "fixes": 4,
                     "skipped_findings": 1, "retirement": False}
        g_pr = {"number": 77, "url": "https://example.test/77", "headRefOid": "abc"}
        grec = build_record(g_article, g_verdict, g_pr, g_article["slug"])
        check("glowup + PR -> status glowup (completed)",
              grec["status"] == "glowup" and grec["attempts"] == 0
              and grec["mode"] == "glowup" and grec["pr_number"] == 77)
        grec2 = build_record(g_article, g_verdict, None, g_article["slug"])
        check("glowup without PR -> incomplete",
              grec2["status"] == "incomplete" and "glowup-" in (grec2["note"] or ""))
        check("glowup body check uses the glowup sections",
              check_pr_body("## Why this page\n## Backlog executed\n"
                            "## Backlog declined\n## Secondary sweep\n"
                            "## Screenshot check\n## Verification\n",
                            "glowup") == [])
        check("glowup body check flags missing backlog sections",
              "Backlog executed" in check_pr_body("## Why this page\n", "glowup"))
        check("no-verdict clarity_flag defaults False", rec["clarity_flag"] is False)
        check("selection signal persisted on the record",
              rec["tier"] == 2 and rec["score"] == 137.5
              and rec["monthly_visits"] == 842 and rec["traffic_available"] is True)
        check("reader signals persisted on the record verbatim",
              rec["signals"] == signals_block and rec["signals_available"] is True)

        # Repeated incomplete accrues against the prior count the selector carried.
        retried = {**article, "attempts": 2}
        rec = build_record(retried, {"verdict": "fixed"}, None, article["slug"])
        check("incomplete accrues prior attempts (2 -> 3)", rec["attempts"] == 3)

        # Clean verdict resets the retry counter.
        rec = build_record(retried, {"verdict": "clean", "reason": "accurate"},
                           None, article["slug"])
        check("clean verdict -> clean", rec["status"] == "clean" and rec["pr"] is None)
        check("clean resets attempts to 0", rec["attempts"] == 0)

        # Report-only lane (#20996): a completed status with no PR. It must
        # advance the staleness clock — that is what laps the lane across the
        # 248-page CLI reference instead of re-reading the same few pages.
        rec = build_record({**retried, "mode": "report", "lane": "report"},
                           {"verdict": "reported", "reason": "claims recorded (7 verdict(s))",
                            "fixes": 0, "skipped_findings": 0, "retirement": False},
                           None, article["slug"])
        check("reported verdict -> reported, no PR, attempts reset",
              rec["status"] == "reported" and rec["pr"] is None and rec["attempts"] == 0)
        check("reported is not incomplete, so the clock advances",
              rec["status"] != "incomplete" and rec["mode"] == "report")

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

        # --- carry-forward: the pointer to the last review PR --------------
        # The record is rebuilt every review, so a review that opens no PR used
        # to reset the pointer to 0 and strand the page's banked backlog.
        prior_reviewed = {"status": "reviewed", "pr": "https://example.test/19885",
                          "pr_number": 19885, "skipped_findings": 8}
        r = build_record(article, {"verdict": "clean", "reason": "accurate"},
                         None, article["slug"], prior=prior_reviewed)
        check("a clean review keeps the prior review's PR pointer",
              r["last_pr_number"] == 19885 and r["last_pr"] == "https://example.test/19885")
        check("a clean review still reports no PR of its own",
              r["pr_number"] == 0 and r["pr"] is None)
        r = build_record(article, {"verdict": "skipped", "reason": "draft"},
                         None, article["slug"], prior=prior_reviewed)
        check("a skipped review keeps the pointer", r["last_pr_number"] == 19885)
        r = build_record(article, None, None, article["slug"],
                         claude_succeeded=False, prior=prior_reviewed)
        check("an incomplete review keeps the pointer", r["last_pr_number"] == 19885)
        # The chain is what makes it durable: a run of PR-less reviews must not
        # walk the pointer off the end one review at a time.
        carried_only = {"status": "clean", "pr": None, "pr_number": 0,
                        "last_pr": "https://example.test/19885", "last_pr_number": 19885}
        r = build_record(article, {"verdict": "clean", "reason": "accurate"},
                         None, article["slug"], prior=carried_only)
        check("the pointer survives consecutive PR-less reviews",
              r["last_pr_number"] == 19885)
        r = build_record(article, {"verdict": "fixed", "fixes": 1}, pr,
                         article["slug"], prior=prior_reviewed)
        check("a fresh PR overwrites the carried pointer",
              r["last_pr_number"] == 19731 and r["pr_number"] == 19731)
        r = build_record(article, {"verdict": "clean", "reason": "accurate"},
                         None, article["slug"], prior=None)
        check("nothing is carried when there is no prior record",
              r["last_pr_number"] == 0 and r["last_pr"] is None)
        check("carry-forward never resurrects a stale status",
              build_record(article, {"verdict": "clean", "reason": "ok"}, None,
                           article["slug"], prior=prior_reviewed)["status"] == "clean")
        check("carry-forward never resurrects a stale fix count",
              build_record(article, {"verdict": "clean", "reason": "ok"}, None,
                           article["slug"],
                           prior={"fixes": 7, "pr_number": 1})["fixes"] == 0)

        # --- carry-forward: a glow-up that executed nothing ----------------
        # #20984: the backlog was unrecoverable, the glow-up ran taxonomy-only,
        # and the ledger then zeroed the 17 banked findings that had selected
        # the page — deleting the debt the lane had just failed to collect.
        prior_banked = {"status": "clean", "pr_number": 0, "skipped_findings": 17,
                        "clarity_flag": True}
        g_empty = {"verdict": "glowup", "fixes": 0, "skipped_findings": 0,
                   "retirement": False}
        r = build_record(g_article, g_empty, g_pr, g_article["slug"], prior=prior_banked)
        check("#20984: a glow-up that executed nothing preserves the banked count",
              r["skipped_findings"] == 17)
        check("#20984: it preserves the clarity flag", r["clarity_flag"] is True)
        check("#20984: it is marked degraded so the selector can tell why",
              r["glowup_degraded"] is True and "preserved" in (r["note"] or ""))
        r = build_record(g_article, g_verdict, g_pr, g_article["slug"], prior=prior_banked)
        check("a glow-up that executed the backlog reports its own declined count",
              r["skipped_findings"] == 1 and r["glowup_degraded"] is False)
        r = build_record(g_article, {"verdict": "glowup", "fixes": 0,
                                     "skipped_findings": 3}, g_pr,
                         g_article["slug"], prior=prior_banked)
        check("a glow-up that declined everything is real work, not degraded",
              r["skipped_findings"] == 3 and r["glowup_degraded"] is False)
        r = build_record(g_article, g_empty, g_pr, g_article["slug"],
                         prior={"status": "glowup", "skipped_findings": 0})
        check("an empty glow-up with no prior debt is not degraded",
              r["glowup_degraded"] is False and r["skipped_findings"] == 0)

        # --- the degraded flag survives repeat runs -------------------------
        # It used to carry a consecutive-run counter, because the selector
        # exempted a degraded page from the cooldown and an exemption with no
        # bound is an unbounded retry loop. select-glowup.py now routes a
        # degraded page to a fix-lane repair instead of re-queueing the
        # glow-up, so the flag needs no counter — but it must still be set on
        # every degraded run, and cleared by one that did work.
        r1 = build_record(g_article, g_empty, g_pr, g_article["slug"], prior=prior_banked)
        check("a degraded glow-up sets the flag", r1["glowup_degraded"] is True)
        check("the note says where the page goes next",
              "fix-lane repair" in (r1["note"] or ""))
        r2 = build_record(g_article, g_empty, g_pr, g_article["slug"],
                          prior={**prior_banked, "glowup_degraded": True})
        check("a second degraded run keeps the flag set",
              r2["glowup_degraded"] is True and r2["skipped_findings"] == 17)
        r3 = build_record(g_article, g_verdict, g_pr, g_article["slug"],
                          prior={**prior_banked, "glowup_degraded": True})
        check("a glow-up that did work clears the degraded flag",
              r3["glowup_degraded"] is False)

        # --- a failed ledger read is not "first review" ---------------------
        # Expired credentials and a wrong URI both exit non-zero. Reporting them
        # as a first review silently reintroduces the bug the carry-forward
        # fixes: a page with history recorded as if it had none.
        import contextlib
        import io
        import subprocess as _sp

        def _read_prior_with(stderr_text):
            """load_prior against a stubbed `aws s3 cp` failure; returns its log."""
            def fake_run(cmd, **kw):
                return _sp.CompletedProcess(cmd, 1, stdout="", stderr=stderr_text)
            real_run, buf = _sp.run, io.StringIO()
            _sp.run = fake_run
            try:
                with contextlib.redirect_stderr(buf):
                    result = load_prior("docs-x", "s3://b/ledger/", None)
            finally:
                _sp.run = real_run
            return result, buf.getvalue()

        missing, missing_log = _read_prior_with(
            "fatal error: An error occurred (404) when calling the HeadObject "
            "operation: Not Found")
        broken, broken_log = _read_prior_with("Unable to locate credentials")
        check("a genuine 404 reads as the page's first review",
              missing is None and "first review of this page" in missing_log
              and "::warning::" not in missing_log)
        check("a credential failure is NOT reported as a first review",
              broken is None and "first review of this page" not in broken_log)
        check("it warns instead, naming what carrying nothing forward costs",
              "::warning::" in broken_log
              and "reset this page's PR pointer" in broken_log)
        check("the underlying aws error is surfaced, not swallowed",
              "Unable to locate credentials" in broken_log)

        # --- clarity_flag is three-state ------------------------------------
        # The glow-up sentinel never carried the key, so every glow-up silently
        # cleared the flag it had just been selected for.
        r = build_record(article, {"verdict": "fixed", "fixes": 2}, pr,
                         article["slug"], prior={"clarity_flag": True, "pr_number": 1})
        check("an absent clarity_flag carries forward rather than clearing",
              r["clarity_flag"] is True)
        r = build_record(article, {"verdict": "glowup", "fixes": 3,
                                   "skipped_findings": 0, "clarity_flag": False},
                         g_pr, article["slug"], prior={"clarity_flag": True})
        check("an explicit clarity_flag:false clears the flag",
              r["clarity_flag"] is False)

        # --- load_prior degrades to None, never raises ----------------------
        check("load_prior with no URI and no fixture is None",
              load_prior("docs-x", "", None) is None)
        empty_prior = d / "prior-empty.json"
        empty_prior.write_text("")
        check("load_prior on an empty fixture is None",
              load_prior("docs-x", "", str(empty_prior)) is None)
        bad_prior = d / "prior-bad.json"
        bad_prior.write_text("{not json")
        check("load_prior on unparseable JSON is None, not an exception",
              load_prior("docs-x", "", str(bad_prior)) is None)
        list_prior = d / "prior-list.json"
        list_prior.write_text("[]")
        check("load_prior rejects a non-object record",
              load_prior("docs-x", "", str(list_prior)) is None)
        check("last_pr_from tolerates a non-dict prior",
              last_pr_from(None) == (None, 0) and last_pr_from("x") == (None, 0))

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
    p.add_argument("--prior",
                   help="inject the page's existing ledger record (file path or '-' for "
                        "stdin); for tests — otherwise read from CONTENT_REVIEW_LEDGER_URI")
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

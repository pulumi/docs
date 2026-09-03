#!/usr/bin/env python3
"""The SLA sweep — machine-enforced reviewer-wait clocks and author-staleness
warn/close for the v3 PR review workflow.

Two independent clocks run per open, non-draft PR, never both at once:

  AUTHOR-TIME    the ball is in the author's court — unanswered 🚨/❓
                 findings on the author card (or, for a legacy v2 PR, an
                 outstanding legacy review), or a standing CHANGES_REQUESTED
                 review. Idle past `author_staleness.warn_days` (from
                 `.github/review-routing.yml`) gets a nudge comment + the
                 `review:author-stalled` label; idle past `close_days`, with
                 a warn old enough to prove the author had fair notice, gets
                 the PR closed (one-click reopen).

  REVIEWER-TIME  the ball is in a required reviewer's court — the routing
                 matrix (`routing.py`) names a role and no unanswered
                 finding or changes-requested review is standing in the way.
                 Waiting past that role's `sla.<role>.business_days` gets a
                 one-shot escalation comment (+ a best-effort Slack line)
                 naming the role's `escalate_to` contact.

A PR with no v3 author card AND no v2 pinned review (i.e. auto-review never
ran, or the author lacks write access and the PR skips G1/G2 per
`external_contributors`) is a legacy/no-state PR and is NEVER touched — this
sweep only interprets state it can prove exists, fail-safe. A mechanical PR
that resolves to no required role has no clock either.

Deterministic, no model. Reuses sentinel.py's own gate-2 finding-parsing
logic (`_card_rows`, `review_state.parse_state`) and the same
`_mechanical_and_claims` classifier sentinel.py uses for gate 3 routing, so
"answered" and "required role" can never mean something different here than
they do at the merge gate — one classifier, one vocabulary (see AGENTS.md /
review-routing.yml). Imported by path is unnecessary here: sla-sweep.py
lives in the same directory as sentinel.py/routing.py/review_state.py, so a
plain `import` after the sys.path insert (same trick sentinel.py itself
uses) picks them up directly.

## Clock-start derivation (REVIEWER-TIME)

The exact timeline signals used, latest-of:

  1. the `ready_for_review` timeline event, or the PR's `created_at` if it
     was opened ready (never drafted) — the earliest a reviewer *could* have
     looked;
  2. the most recent `review_requested` timeline event whose
     `requested_team.slug` matches the required role's team — reviewer-time
     restarts if the role gets re-requested after already being satisfied
     once (e.g. dismissed-on-push);
  3. the author's last commit/comment timestamp, but ONLY when it postdates
     the most recent standing CHANGES_REQUESTED review — this approximates
     "the moment author-time ended and reviewer-time resumed" using only
     signals the timeline actually carries (there is no explicit "author
     answered changes-requested" event).

This is a documented approximation, not a perfect state machine: a PR that
was never changes-requested and never re-requested just clocks from
ready-for-review/open, which is the common case.

## Business days

`business_days_between(start, end)` counts weekday (UTC, Mon-Fri) boundaries
crossed walking from `start` to `end` one calendar day at a time — no
holiday calendar (documented simplification, matches `author_staleness`'s
plain-day math being separate: staleness idle is measured in *calendar*
days, only the reviewer SLA clock is business days, per review-routing.yml).

## State and evidence

Same degradation contract as `record-evidence.py`: `PR_REVIEW_EVIDENCE_URI`
unset means read/write local `.pr-review-state/` and emit one `::warning::`
— never fail. Two kinds of records:

  - `pr-review/state/<pr>.json` — mutable, read-modify-written each sweep:
    `{"schema":1,"warns":[{"at","head_sha"}],
       "escalations":[{"role","clock_start","at"}],"closes":[...]}`.
    A PR keeps at most the *current* unresolved warn (cleared to `[]` the
    moment fresh author activity postdates it) — old warns are not an
    append-only log, they exist only to answer "has this author been
    warned, and is the warning stale enough to justify a close."
    `escalations` and `closes` ARE append-only (audit trail; escalations
    are also how "once per clock epoch" is enforced — see below).
  - `pr-review/runs/<date>/sweep-<HHMMSSZ>.json` — one immutable record per
    sweep invocation (the S3 bucket is versioned, like the evidence object,
    so the date-keyed `sweep.json` name in the design doc would already be
    immutable per version; the HHMMSSZ suffix is a deliberate deviation to
    keep same-day runs — this cron fires every 2 hours — from colliding as
    local files, which don't get that free versioning).

`--dry-run` never writes state, comments, labels, or closes — it computes
and prints the same run-record JSON `main()` always prints, so dry-run
output IS the "intended actions" preview.

Self-contained — run the smoke checks with `sla-sweep.py --self-test`
(delegates to test_sla_sweep.py, same convention as sentinel.py).
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import subprocess
import sys
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
import review_state  # noqa: E402
import routing  # noqa: E402
import sentinel  # noqa: E402


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


# record-evidence.py's s3_key()/upload() are generic enough to reuse
# verbatim (hyphenated filename -> import by path, same technique
# record-evidence.py itself uses for validate-evidence.py).
_record_evidence = _load("sla_sweep_record_evidence", HERE / "record-evidence.py")

AUTHOR_STALLED_LABEL = "review:author-stalled"
DEFAULT_STATE_DIR = ".pr-review-state"
EVIDENCE_URI_ENV = "PR_REVIEW_EVIDENCE_URI"
SLACK_WEBHOOK_ENV = "SLACK_WEBHOOK_URL"


def log(msg: str) -> None:
    print(f"sla-sweep: {msg}", file=sys.stderr)


def warn(msg: str) -> None:
    print(f"::warning::sla-sweep: {msg}", file=sys.stderr)


class CorruptReviewState(Exception):
    """The author card's REVIEW_STATE block exists but won't parse.

    Fail-safe, same philosophy as an unparsable timeline: skip the PR rather
    than guess whether its findings are answered.
    """


# ---- GitHub I/O ----------------------------------------------------------


class Gh:
    """Thin `gh` wrapper; every method is stubbed in tests."""

    def __init__(self, repo: str):
        self.repo = repo

    def _run(self, args: list[str]) -> str:
        result = subprocess.run(["gh", *args], text=True, capture_output=True, check=True)
        return result.stdout

    def list_open_prs(self) -> list[dict]:
        out = self._run([
            "pr", "list", "--repo", self.repo, "--state", "open", "--limit", "500",
            "--json", "number,title,author,isDraft,headRefOid,createdAt,url",
        ])
        return json.loads(out)

    def get_pr(self, pr: int) -> dict:
        return json.loads(self._run(["api", f"repos/{self.repo}/pulls/{pr}"]))

    def list_files(self, pr: int) -> list[dict]:
        out = self._run(["api", "--paginate", f"repos/{self.repo}/pulls/{pr}/files"])
        return json.loads(out)

    def list_issue_comments(self, pr: int) -> list[dict]:
        out = self._run(["api", "--paginate", f"repos/{self.repo}/issues/{pr}/comments"])
        return json.loads(out)

    def list_reviews(self, pr: int) -> list[dict]:
        out = self._run(["api", "--paginate", f"repos/{self.repo}/pulls/{pr}/reviews"])
        return json.loads(out)

    def get_timeline(self, pr: int) -> list[dict]:
        out = self._run(["api", "--paginate", f"repos/{self.repo}/issues/{pr}/timeline"])
        return json.loads(out)

    def create_issue_comment(self, pr: int, body: str) -> None:
        self._run(["api", "--method", "POST", f"repos/{self.repo}/issues/{pr}/comments",
                    "-f", f"body={body}"])

    def add_label(self, pr: int, label: str) -> None:
        self._run(["pr", "edit", str(pr), "--repo", self.repo, "--add-label", label])

    def remove_label(self, pr: int, label: str) -> None:
        self._run(["pr", "edit", str(pr), "--repo", self.repo, "--remove-label", label])

    def close_pr(self, pr: int, body: str) -> None:
        self._run(["pr", "close", str(pr), "--repo", self.repo, "--comment", body])


# ---- business-day math -----------------------------------------------------


def business_days_between(start: datetime, end: datetime) -> int:
    """Weekday (UTC, Mon-Fri) boundaries crossed walking from start to end.

    No holiday calendar (documented simplification). Measured as elapsed
    distance, not a date-range count: Friday afternoon to Monday morning is
    1 business day (the Sat/Sun crossing doesn't count, the Mon crossing
    does), matching how the sweep uses it — a coarse "how long has this
    role been waiting" gate against an integer business_days SLA.
    """
    if end <= start:
        return 0
    days = 0
    cur = start
    while cur.date() < end.date():
        cur += timedelta(days=1)
        if cur.weekday() < 5:  # Monday=0 .. Sunday=6
            days += 1
    return days


# ---- timestamp helpers -----------------------------------------------------


def _parse_ts(value: str | None) -> datetime:
    """Raises ValueError on anything unparsable — callers treat that as an
    unparsable timeline and skip the PR (fail-safe)."""
    if not value:
        raise ValueError("empty timestamp")
    dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt


# ---- review helpers ---------------------------------------------------------


def latest_review_per_user(reviews: list[dict]) -> dict[str, dict]:
    """Oldest-first, keep the last STATEFUL review per user (mirrors
    sentinel.py's G3 approvers loop: COMMENTED never voids a prior state)."""
    latest: dict[str, dict] = {}
    for r in reviews:
        user = (r.get("user") or {}).get("login") or ""
        if user and r.get("state") != "COMMENTED":
            latest[user] = r
    return latest


# ---- classification (step 2) -----------------------------------------------


def classify_waiting_state(
    pr_detail: dict, files: list[dict], author_card: dict | None, legacy: dict | None,
    reviews: list[dict], config: routing.Config,
) -> tuple[str | None, dict | None, list[str]]:
    """Returns (kind, extra, reasons). kind is "author", "reviewer", or None
    (no clock — mechanical with no required role)."""
    reasons: list[str] = []
    undecided_count = 0
    author_time = False

    if author_card is not None:
        body = author_card.get("body") or ""
        try:
            state = review_state.parse_state(body) or review_state.empty_state()
        except ValueError as exc:
            raise CorruptReviewState(str(exc)) from exc
        rows = sentinel._card_rows(body, ("🚨", "❓"))
        undecided = [r for r in rows if r["id"] not in state.get("findings", {})]
        undecided_count = len(undecided)
        if undecided_count:
            author_time = True
            reasons.append(f"{undecided_count} unanswered finding(s) on the author card")
    elif legacy is not None:
        vp = sentinel._load("sla_sweep_validate_pinned",
                             sentinel._DOCS_REVIEW_SCRIPTS / "validate-pinned.py")
        outstanding = len(vp.extract_bucket_bullets(legacy.get("body") or "", "🚨 Outstanding"))
        undecided_count = outstanding
        if outstanding:
            author_time = True
            reasons.append(f"{outstanding} outstanding finding(s) on the legacy review")

    latest_reviews = latest_review_per_user(reviews)
    changes_requested_at: str | None = None
    for r in latest_reviews.values():
        if r.get("state") == "CHANGES_REQUESTED" and r.get("submitted_at"):
            if changes_requested_at is None or r["submitted_at"] > changes_requested_at:
                changes_requested_at = r["submitted_at"]
    if any(r.get("state") == "CHANGES_REQUESTED" for r in latest_reviews.values()):
        author_time = True
        reasons.append("latest review is CHANGES_REQUESTED")

    if author_time:
        # `changes_requested_at` lets process_author_time start the idle
        # clock from when the author was actually asked for changes — a
        # review landing on a branch last pushed 20 days ago must not read
        # as 20 idle days on the next sweep.
        return "author", {"undecided_count": undecided_count,
                          "changes_requested_at": changes_requested_at}, reasons

    files_paths = [f["filename"] for f in files]
    mechanical, claims, mech_reasons = sentinel._mechanical_and_claims(pr_detail, files)
    resolution = routing.resolve_lanes(files_paths, mechanical, claims, config)
    reasons.extend(mech_reasons)
    if resolution.roles:
        return "reviewer", {"roles": resolution.roles}, reasons
    reasons.append("mechanical with no required roles — no clock")
    return None, None, reasons


# ---- timeline reads ---------------------------------------------------------


def last_author_activity(timeline: list[dict], author_login: str, pr_created_at: str) -> datetime:
    """max(author's last commit time, author's last comment time), from the
    PR's issue-timeline events. Falls back to the PR's created_at when
    neither is found (a PR with no timeline commit/comment events at all).

    Uses `committed` events (any commit landing counts — the git commit
    author and the PR author aren't always the same login, so this is a
    documented simplification: any push activity resets the author clock)
    and `commented` events whose actor matches the PR author login (a
    reviewer's own comments must not reset the author's idle clock).
    """
    candidates: list[datetime] = []
    for e in timeline:
        event = e.get("event")
        if event == "committed":
            # Committer date first: a rebase or cherry-pick keeps the author
            # date, and "any push activity resets the clock" means when the
            # commit landed, not when it was first written.
            ts = (e.get("committer") or {}).get("date") or (e.get("author") or {}).get("date")
            if ts:
                candidates.append(_parse_ts(ts))
        elif event == "commented":
            actor_login = (e.get("actor") or e.get("user") or {}).get("login")
            if actor_login and actor_login == author_login and e.get("created_at"):
                candidates.append(_parse_ts(e["created_at"]))
    if not candidates:
        candidates.append(_parse_ts(pr_created_at))
    return max(candidates)


def reviewer_clock_start(
    timeline: list[dict], pr_detail: dict, team_ref: str, reviews: list[dict],
    last_activity: datetime,
) -> datetime:
    """Latest of the three candidates documented in the module docstring."""
    candidates: list[datetime] = []

    ready_events = [e for e in timeline if e.get("event") == "ready_for_review" and e.get("created_at")]
    if ready_events:
        candidates.append(max(_parse_ts(e["created_at"]) for e in ready_events))
    else:
        candidates.append(_parse_ts(pr_detail.get("created_at")))

    _, slug = sentinel._team_org_slug(team_ref)
    requested_events = [
        e for e in timeline
        if e.get("event") == "review_requested"
        and (e.get("requested_team") or {}).get("slug") == slug
        and e.get("created_at")
    ]
    if requested_events:
        candidates.append(max(_parse_ts(e["created_at"]) for e in requested_events))

    latest_reviews = latest_review_per_user(reviews)
    changes_requested_times = [
        _parse_ts(r["submitted_at"]) for r in latest_reviews.values()
        if r.get("state") == "CHANGES_REQUESTED" and r.get("submitted_at")
    ]
    if changes_requested_times and last_activity > max(changes_requested_times):
        candidates.append(last_activity)

    return max(candidates)


# ---- state I/O ----------------------------------------------------------


def empty_sweep_state() -> dict:
    return {"schema": 1, "warns": [], "escalations": [], "closes": []}


def local_state_path(state_dir: Path, pr: int) -> Path:
    return state_dir / "state" / f"{pr}.json"


def _s3_read_json(key: str) -> dict | None:
    """Best-effort S3 read; None on any failure (missing key, no aws CLI,
    bad JSON) — mirrors record-evidence.py's load_prior()."""
    try:
        out = subprocess.run(["aws", "s3", "cp", key, "-"], capture_output=True, text=True, check=False)
    except OSError:
        return None
    if out.returncode != 0:
        return None
    try:
        data = json.loads(out.stdout)
    except json.JSONDecodeError:
        return None
    return data if isinstance(data, dict) else None


def load_state(pr: int, uri: str, state_dir: Path) -> dict:
    if uri:
        data = _s3_read_json(_record_evidence.s3_key(uri, "state", f"{pr}.json"))
        if data is not None:
            return data
    local = local_state_path(state_dir, pr)
    if local.is_file():
        try:
            return json.loads(local.read_text())
        except (OSError, json.JSONDecodeError):
            pass
    return empty_sweep_state()


def save_state(pr: int, state: dict, uri: str, state_dir: Path) -> bool:
    """Persist per-PR state. Returns whether the DURABLE copy landed: the
    S3 upload's result when a URI is set, True for a local-only run (the
    caller decided local state was acceptable — see resolve_mutation_mode).
    A False here is the signal the run record must carry: the mutation
    happened, its record didn't, and the next sweep will not know."""
    local = local_state_path(state_dir, pr)
    local.parent.mkdir(parents=True, exist_ok=True)
    local.write_text(json.dumps(state, indent=2) + "\n")
    if uri:
        return _record_evidence.upload(state, _record_evidence.s3_key(uri, "state", f"{pr}.json"))
    return True


def durable_state_writable(uri: str, now: datetime) -> bool:
    """Pre-flight for a real run: write a probe to the state prefix and read
    it back. Mutating before knowing the state write can land is how a warn
    or an escalation gets re-issued every sweep; this turns "the bucket
    resolved" into "the bucket accepted a write from this runner"."""
    if not uri:
        return False
    key = _record_evidence.s3_key(uri, "state", "_probe.json")
    stamp = {"probe": now.isoformat()}
    if not _record_evidence.upload(stamp, key):
        return False
    back = _s3_read_json(key)
    return bool(back) and back.get("probe") == stamp["probe"]


def write_run_record(record: dict, uri: str, state_dir: Path, now: datetime) -> None:
    date = now.date().isoformat()
    fname = f"sweep-{now.strftime('%H%M%S')}Z.json"
    local = state_dir / "runs" / date / fname
    local.parent.mkdir(parents=True, exist_ok=True)
    local.write_text(json.dumps(record, indent=2) + "\n")
    if uri:
        _record_evidence.upload(record, _record_evidence.s3_key(uri, "runs", date, fname))


# ---- Slack ------------------------------------------------------------------


def slack_notify(text: str) -> None:
    """Best-effort — a webhook failure is a warning, never a sweep failure."""
    url = os.environ.get(SLACK_WEBHOOK_ENV, "").strip()
    if not url:
        return
    try:
        req = urllib.request.Request(
            url, data=json.dumps({"text": text}).encode("utf-8"),
            headers={"Content-Type": "application/json"},
        )
        urllib.request.urlopen(req, timeout=10)  # noqa: S310 — fixed https webhook URL from env
    except (urllib.error.URLError, OSError, TimeoutError) as exc:
        warn(f"Slack webhook failed: {exc}")


# ---- AUTHOR-TIME processing (step 3) -----------------------------------------


def process_author_time(
    gh: Gh, pr_number: int, head_sha: str, undecided_count: int, config: routing.Config,
    state: dict, now: datetime, dry_run: bool, last_activity: datetime,
    changes_requested_at: str | None = None,
) -> dict:
    warn_days = config.author_staleness["warn_days"]
    close_days = config.author_staleness["close_days"]
    # AUTHOR-TIME starts when the author was last active OR when they were
    # last asked for changes, whichever is later — the same "when did this
    # clock actually start" reasoning reviewer_clock_start applies.
    if changes_requested_at:
        last_activity = max(last_activity, _parse_ts(changes_requested_at))
    idle_days = (now - last_activity).total_seconds() / 86400.0
    warns = state.get("warns") or []
    last_warn = warns[-1] if warns else None

    if last_warn is not None:
        warn_at = _parse_ts(last_warn["at"])
        if last_activity > warn_at:
            # Fresh author activity since the warn -> clear the label and
            # the warn record; a later idle period re-arms from scratch.
            if not dry_run:
                _try_label(gh, pr_number, gh.remove_label, AUTHOR_STALLED_LABEL)
            state["warns"] = []
            return {"changed": True, "action": {"type": "clear", "idle_days": round(idle_days, 2)}}

    if last_warn is None:
        if idle_days > warn_days:
            why = (f"{undecided_count} finding(s) need an answer" if undecided_count
                   else "a reviewer has requested changes")
            body = (
                f"This PR is waiting on you: {why} — "
                f"reply `@claude <your reasoning> #update-review`, or push the fix. It closes in "
                f"{close_days - warn_days} days if nothing changes; reopening later is one click."
            )
            if not dry_run:
                gh.create_issue_comment(pr_number, body)
                _try_label(gh, pr_number, gh.add_label, AUTHOR_STALLED_LABEL)
            state["warns"] = warns + [{"at": now.isoformat(), "head_sha": head_sha}]
            return {"changed": True, "action": {
                "type": "warn", "idle_days": round(idle_days, 2), "undecided_count": undecided_count,
            }}
        return {"changed": False, "action": {"type": "none", "idle_days": round(idle_days, 2)}}

    warn_at = _parse_ts(last_warn["at"])
    warn_age_days = (now - warn_at).total_seconds() / 86400.0
    if idle_days > close_days and warn_age_days >= (close_days - warn_days):
        body = (
            f"Closing this PR as stale — no author activity in {round(idle_days)} day(s), past the "
            f"{close_days}-day close threshold after the earlier stall warning. Reopening is one click "
            f"(the Reopen button, or `gh pr reopen {pr_number}`) and the review picks up where it "
            f"left off."
        )
        if not dry_run:
            gh.close_pr(pr_number, body)
        state["closes"] = (state.get("closes") or []) + [
            {"at": now.isoformat(), "head_sha": head_sha, "idle_days": round(idle_days, 2)}
        ]
        return {"changed": True, "action": {"type": "close", "idle_days": round(idle_days, 2)}}

    return {"changed": False, "action": {
        "type": "none", "idle_days": round(idle_days, 2), "warn_age_days": round(warn_age_days, 2),
    }}


def _try_label(gh: Gh, pr_number: int, fn, label: str) -> None:
    """Label mutations are best-effort. A missing label (review:author-stalled
    is created by hand) is the expected failure, and nothing about the nudge
    or the escalation depends on it — but a raise here, ordered before the
    state write, would drop the record and re-post the comment every sweep.
    Comments and closes stay fatal: those must not be retried blind."""
    try:
        fn(pr_number, label)
    except Exception as exc:  # noqa: BLE001
        log(f"PR #{pr_number}: label {label!r} {fn.__name__} failed ({exc}); continuing")


# ---- REVIEWER-TIME processing (step 4) ---------------------------------------


def process_reviewer_time(
    gh: Gh, pr_number: int, config: routing.Config, state: dict, now: datetime, dry_run: bool,
    roles: set[str], timeline: list[dict], pr_detail: dict, reviews: list[dict],
    last_activity: datetime,
) -> dict:
    escalations = list(state.get("escalations") or [])
    actions = []
    changed = False

    for role in sorted(roles):
        team_ref = config.teams[role]
        clock_start = reviewer_clock_start(timeline, pr_detail, team_ref, reviews, last_activity)
        clock_key = clock_start.isoformat()
        waited = business_days_between(clock_start, now)
        sla_days = config.sla[role]["business_days"]
        escalate_to = config.sla[role]["escalate_to"]

        already = any(e.get("role") == role and e.get("clock_start") == clock_key for e in escalations)
        if waited > sla_days and not already:
            todo = escalate_to.startswith("TODO")
            mentioned = False
            if todo:
                log(f"PR #{pr_number}: sla.{role}.escalate_to is a TODO placeholder — "
                    f"recording the breach without mentioning anyone")
            else:
                body = (f"@{escalate_to} — this PR has waited {waited} business day(s) for {role} "
                        f"review (SLA: {sla_days}bd).")
                if not dry_run:
                    gh.create_issue_comment(pr_number, body)
                    slack_notify(body)
                mentioned = True
            escalations.append({"role": role, "clock_start": clock_key, "at": now.isoformat()})
            changed = True
            actions.append({
                "type": "escalate", "role": role, "waited_business_days": waited,
                "sla_business_days": sla_days, "clock_start": clock_key,
                "mentioned": mentioned, "escalate_to": escalate_to,
            })
        else:
            actions.append({
                "type": "none", "role": role, "waited_business_days": waited,
                "sla_business_days": sla_days, "clock_start": clock_key,
            })

    state["escalations"] = escalations

    # Defensive cleanup: a PR that's back in REVIEWER-TIME is no longer
    # waiting on its author, so a stale review:author-stalled label/warn
    # (left over from before the outstanding findings were answered) must
    # not linger — nothing in review-label-reconcile.yml covers this label.
    if state.get("warns"):
        if not dry_run:
            _try_label(gh, pr_number, gh.remove_label, AUTHOR_STALLED_LABEL)
        state["warns"] = []
        changed = True
        actions.append({"type": "clear_stale_author_warn"})

    return {"changed": changed, "actions": actions}


# ---- sweep ------------------------------------------------------------------


def sweep(gh: Gh, config: routing.Config, *, now: datetime, dry_run: bool,
          state_dir: Path, evidence_uri: str) -> dict:
    prs = gh.list_open_prs()
    run_actions: list[dict] = []

    for pr in prs:
        pr_number = pr["number"]
        if pr.get("isDraft"):
            log(f"PR #{pr_number}: draft; skipping")
            continue

        try:
            comments = gh.list_issue_comments(pr_number)
        except Exception as exc:  # noqa: BLE001 — never let one bad PR kill the sweep
            log(f"PR #{pr_number}: failed to list comments ({exc}); skipping")
            continue

        author_card = sentinel._find_comment(comments, sentinel.AUTHOR_MARKER)
        legacy = sentinel._find_legacy_comment(comments) if author_card is None else None
        if author_card is None and legacy is None:
            log(f"PR #{pr_number}: no v3 author card or v2 pinned review — "
                f"legacy/no-state PR, never touched")
            continue

        try:
            pr_detail = gh.get_pr(pr_number)
            files = gh.list_files(pr_number)
            reviews = gh.list_reviews(pr_number)
        except Exception as exc:  # noqa: BLE001
            log(f"PR #{pr_number}: failed to fetch PR state ({exc}); skipping")
            continue
        head_sha = (pr_detail.get("head") or {}).get("sha") or pr.get("headRefOid") or ""

        try:
            kind, extra, reasons = classify_waiting_state(
                pr_detail, files, author_card, legacy, reviews, config
            )
        except CorruptReviewState as exc:
            log(f"PR #{pr_number}: REVIEW_STATE corrupt ({exc}); skipping (fail-safe)")
            continue

        if kind is None:
            log(f"PR #{pr_number}: {reasons[-1] if reasons else 'no clock'}")
            # A warned PR whose findings then got answered can land here
            # (mechanical, no required role). Nothing else clears the label
            # (review-label-reconcile.yml doesn't know it), so do it here.
            state = load_state(pr_number, evidence_uri, state_dir)
            if state.get("warns"):
                if not dry_run:
                    _try_label(gh, pr_number, gh.remove_label, AUTHOR_STALLED_LABEL)
                state["warns"] = []
                persisted = save_state(pr_number, state, evidence_uri, state_dir) if not dry_run else True
                if not persisted:
                    warn(f"PR #{pr_number}: state NOT persisted to {evidence_uri} — the stale-label "
                         "clear will be retried next sweep")
                run_actions.append({"pr": pr_number, "kind": None, "head_sha": head_sha,
                                    "changed": True,
                                    "actions": [{"type": "clear_stale_author_warn"}],
                                    **({} if persisted else {"state_persisted": False})})
            continue

        try:
            timeline = gh.get_timeline(pr_number)
            if not isinstance(timeline, list):
                raise ValueError("timeline response is not a list")
            author_login = (pr_detail.get("user") or {}).get("login") or ""
            created_at = pr_detail.get("created_at") or pr.get("createdAt") or ""
            last_activity = last_author_activity(timeline, author_login, created_at)
            if kind == "reviewer":
                # Fail fast on bad timeline data for any required role's
                # clock, not just the first one process_reviewer_time visits.
                for role in extra["roles"]:
                    reviewer_clock_start(timeline, pr_detail, config.teams[role], reviews, last_activity)
        except Exception as exc:  # noqa: BLE001
            log(f"PR #{pr_number}: unparsable timeline ({exc}); skipping")
            continue

        state = load_state(pr_number, evidence_uri, state_dir)

        # The processors MUTATE (labels, comments, closes) and Gh._run raises
        # on any failure — one `gh pr edit --add-label` error (the
        # review:author-stalled label not created yet, say) must not abort
        # the sweep for every PR after this one.
        try:
            if kind == "author":
                result = process_author_time(
                    gh, pr_number, head_sha, extra["undecided_count"], config, state, now, dry_run,
                    last_activity, extra.get("changes_requested_at"),
                )
            else:
                result = process_reviewer_time(
                    gh, pr_number, config, state, now, dry_run, extra["roles"], timeline, pr_detail,
                    reviews, last_activity,
                )
        except Exception as exc:  # noqa: BLE001 — never let one bad PR kill the sweep
            log(f"PR #{pr_number}: {kind}-time processing failed ({exc}); state not saved, skipping")
            run_actions.append({"pr": pr_number, "kind": kind, "head_sha": head_sha,
                                "changed": False, "error": str(exc)[:300]})
            continue

        if result.get("changed") and not dry_run:
            if not save_state(pr_number, state, evidence_uri, state_dir):
                # The mutation is already out; the next sweep will not know.
                # Say so where the digest and a human will read it.
                warn(f"PR #{pr_number}: state NOT persisted to {evidence_uri} — the action(s) below "
                     "may be re-issued next sweep")
                result = {**result, "state_persisted": False}

        run_actions.append({"pr": pr_number, "kind": kind, "head_sha": head_sha, **result})

    record = {"schema": 1, "run_at": now.isoformat(), "dry_run": dry_run, "actions": run_actions}
    if not dry_run:
        write_run_record(record, evidence_uri, state_dir, now)
    return record


# ---- CLI ----------------------------------------------------------------


def resolve_mutation_mode(uri: str, dry_run: bool, allow_local_state: bool,
                          durable_ok: bool = True) -> tuple[bool, str | None]:
    """Whether this run may mutate, given where its state can live.

    State is what makes the sweep idempotent: a warn or an escalation that
    isn't durably recorded is re-issued on the next sweep — every two
    hours, on every stalled PR at once. On a CI runner "locally recorded"
    state dies with the job, so no durable URI ⇒ the run is forced to
    dry-run, loudly. `--allow-local-state` is the developer override for a
    laptop whose --state-dir persists between runs.
    """
    if dry_run:
        return True, None
    if uri and not durable_ok:
        return True, (f"{EVIDENCE_URI_ENV} is set but a probe write to its state prefix did not land: "
                      "mutations whose record can't be persisted would be re-issued every sweep, so "
                      "this run is DRY-RUN (nothing labeled, commented, closed, or escalated)")
    if uri or allow_local_state:
        return False, None
    return True, (f"{EVIDENCE_URI_ENV} unset and --allow-local-state not given: mutations without "
                  "durable state would be re-issued every sweep, so this run is DRY-RUN "
                  "(nothing labeled, commented, closed, or escalated)")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--repo")
    parser.add_argument("--config", default=str(REPO_ROOT / ".github" / "review-routing.yml"))
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--state-dir", default=DEFAULT_STATE_DIR,
                         help="local mirror of the pr-review/ state prefixes")
    parser.add_argument("--allow-local-state", action="store_true",
                         help="mutate even with no durable state URI (a persistent --state-dir "
                              "on a developer machine); never on a CI runner")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        import test_sla_sweep  # noqa: PLC0415 — the pytest file doubles as the harness

        return test_sla_sweep.run_standalone()

    if not args.repo:
        parser.error("--repo is required")

    try:
        config = routing.load_config(args.config)
    except routing.RoutingConfigError as exc:
        for msg in exc.errors:
            log(f"routing config error: {msg}")
        return 1

    uri = os.environ.get(EVIDENCE_URI_ENV, "").strip()
    now = datetime.now(timezone.utc)
    durable_ok = durable_state_writable(uri, now) if (uri and not args.dry_run) else True
    dry_run, forced = resolve_mutation_mode(uri, args.dry_run, args.allow_local_state, durable_ok)
    if forced:
        warn(forced)
    elif not uri:
        warn(f"{EVIDENCE_URI_ENV} unset; state recorded locally only (--allow-local-state)")

    gh = Gh(args.repo)
    record = sweep(
        gh, config, now=now, dry_run=dry_run,
        state_dir=Path(args.state_dir), evidence_uri=uri,
    )
    if forced:
        record["forced_dry_run"] = forced
    print(json.dumps(record, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

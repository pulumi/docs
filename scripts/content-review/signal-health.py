#!/usr/bin/env python3
"""Track and alert on silent degradation of the content-review pipeline's inputs.

Observability for §3.4 of the docs-review automation evaluation (pulumi/docs
issue #20078): inputs to the content-review automation degrade gracefully —
and, before this script, silently. Three signals are observed by the
review-existing-content dispatcher, a fourth by the nightly claims-reverify
workflow; all share one state object:

  traffic         a missing docs-traffic snapshot flattens article selection to
                  tier-only scoring, quietly erasing intra-tier prioritization
  console-access  the per-article worker's screenshot lane 2 verifies UI strings
                  against the console source (cmd/console2) in the private
                  pulumi/pulumi-service repo; without token access every UI
                  claim silently becomes "unverifiable"
  holiday-feed    the BambooHR ICS holiday gate fails open by design, so a feed
                  that has been 404ing (or serving garbage) for weeks is invisible
  reverify        the nightly volatile-claims re-verification only Slacks when
                  it finds STALE entities, so a dead or decaying lane (claims
                  index gone, API key missing, most checks inconclusive because
                  the verifier's gh/API plumbing broke — or because most
                  verdicts were demoted for citing only our own docs) looks
                  identical to a healthy quiet one

Graceful degradation is the right behavior; this script adds the missing
observability. The dispatcher runs it once per scheduled run with that run's
observations; it persists per-signal state (one JSON object the workflow syncs
to the ledger bucket under health/) and, once a signal has been continuously
degraded for THRESHOLD_DAYS, writes a one-message alert file the workflow posts
to #docs-ops — re-alerting every REALERT_DAYS, not every day.

Division of labor, matching the rest of the content-review scripts: this script
is a pure function of (state file, observations, --today) — stdlib-only, no
AWS, no network. The workflow moves the bytes (S3 down/up, Slack post) and
gates the side effects, so a workflow_dispatch test run computes and prints
everything but persists and posts nothing.

The health lane must never break the dispatcher: outside --self-test this
script always exits 0, and every failure mode (missing state, corrupt state,
missing queue file) degrades to "carry on with what we know". Because the lane
depends on the same S3 access it (transitively) monitors, it also emits a
GitHub `::warning::` for every currently-degraded signal on every run — the
stateless fallback that still surfaces in the run summary when the day-counting
state is unreachable. One accepted race, documented rather than engineered
around: `last_alerted` is stamped in the same pass that writes the alert file,
so a Slack post that fails after the state is persisted suppresses the re-alert
for one REALERT_DAYS cycle; the per-run warnings cover the gap.

Signal semantics:
  * ok           -> stamp last_ok, clear degraded_since AND last_alerted (a new
                    degradation episode alerts on its own clock)
  * degraded     -> degraded_since = degraded_since or today
  * unconfigured -> recorded for a human inspecting state.json, never alerted:
                    an explicitly unset switch (e.g. BAMBOOHR_HOLIDAY_ICS_URL)
                    is an off-state, not a failure — alarming on it trains
                    people to ignore the alert
  * no observation (flag omitted / queue file missing) -> the signal's prior
                    entry is left untouched; absence of evidence is not
                    degradation

Usage:
    signal-health.py --state .health-state.json \
        [--queue .content-review-queue.json] \
        [--console-status ok|degraded] \
        [--holiday-status ok|empty|fetch_failed|unconfigured] \
        [--reverify-report .claims-reverify-report.json] \
        --alert-out .health-alert.txt \
        [--today YYYY-MM-DD] [--threshold-days N] [--realert-days N] \
        [--run-url URL]
    signal-health.py --self-test
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date, datetime, timezone
from pathlib import Path

STATE_VERSION = 1

# 7 calendar days ~= 5 scheduled (weekday) runs of continuous degradation
# before the first Slack note; then a weekly nag while it persists. Dates, not
# run counts, so weekends neither accrue extra urgency nor reset anything.
THRESHOLD_DAYS = 7
REALERT_DAYS = 7

# Per-signal overrides of THRESHOLD_DAYS. capped-pages alerts on the first
# observed day: a page only lands there after burning ATTEMPT_CAP failed runs,
# so the waiting-out period the default threshold exists for already happened.
# REALERT_DAYS still paces the nag weekly while the state persists.
SIGNAL_THRESHOLDS = {"capped-pages": 0}

# Smallest all-inconclusive night that counts as evidence the reverify lane is
# finding nothing. Below it the run is a sample, not a verdict: on 2026-08-19
# the rotation handed the lane a single entity (a contiguous-chunk remainder,
# since fixed in reverify-claims.tonight_chunk), that entity came back demoted,
# and 1-of-1 inconclusive degraded the signal for the whole lane. A short night
# is now no observation at all, which leaves the prior state standing — the
# same treatment a missing report already gets.
MIN_INCONCLUSIVE_SAMPLE = 5

# Share of a night's checks that may come back inconclusive before the lane
# is degraded. Until 2026-09 this signal only fired at 100%: 19 inconclusive
# of 20 read as "ok", and the night of 2026-09-03 — 10 of 20, nine of them
# demoted for citing our own docs — logged `status: ok`. The signal could see
# a dead lane and nothing short of one. With indexed-circular claims held out
# of the rotation (reverify-claims.py) the expected inconclusive share is
# about a quarter; three in four is a lane producing almost nothing and is
# the level at which someone should look, whether the cause is plumbing
# (errors, unverifiable) or routing (demotions — the detail says which).
REVERIFY_INCONCLUSIVE_RATE = 0.75

# How long a signal may go unobserved before silence itself is the finding.
#
# Every signal is reported BY a job. Nothing reports on a job that never ran,
# so a lane that stops firing leaves its signal frozen at whatever it last
# said — and what it last said is usually "ok". Silence reads as health. That
# is exactly how the `vars.X != '0'` gate kept blog-review and claims-reverify
# dark on their schedules for weeks with every signal green.
#
# So each signal declares the cadence it is observed at, and any run of
# signal-health (from either workflow — they share the state object) can flag
# a signal nobody has written to in too long. The reporting job does not have
# to be the one that notices.
#
# Windows are generous on purpose: a false "the lane is dead" is far more
# corrosive than a day's delay, because it teaches people to ignore the alert.
# reverify runs daily (3 days = two consecutive misses). The rest ride the
# weekday dispatcher, where Fri -> Mon is already 3 days, so 6 covers a normal
# long weekend plus a miss.
SIGNAL_MAX_SILENCE_DAYS = {
    "reverify": 3,
    "traffic": 6,
    "console-access": 6,
    "holiday-feed": 6,
    "capped-pages": 6,
    "ledger-write": 6,
}
DEFAULT_MAX_SILENCE_DAYS = 6

# One line per signal: what broke, for how long, the consequence, and where to
# look — the consequence is the point (see the module docstring).
CONSEQUENCES = {
    "traffic": (
        "traffic snapshot: unavailable for {days} day(s) — article selection is "
        "running tier-only (no intra-tier traffic prioritization). Check the "
        "docsTrafficPageviewsLatestS3Uri output on "
        "pulumi/dwh-workflows-orchestrate-airflow/production and the S3 object "
        "it points at."
    ),
    "console-access": (
        "pulumi/pulumi-service access: pulumi-bot has had no access for {days} "
        "day(s) — screenshot lane 2 is marking every UI-string check "
        "\"unverifiable\". Check the bot token's access to the "
        "pulumi/pulumi-service repo (console source: cmd/console2)."
    ),
    "holiday-feed": (
        "holiday feed: degraded for {days} day(s) ({detail}) — the holiday gate "
        "is running blind (fails open: reviews will run on company holidays). "
        "Regenerate the BAMBOOHR_HOLIDAY_ICS_URL feed."
    ),
    "reverify": (
        "nightly claims re-verify: mostly inconclusive checks for {days} day(s) "
        "({detail}) — volatile-claim drift (version pins, prices, limits) is "
        "going undetected. A demotion count above means the verifier is only "
        "citing our own docs: that's its source routing, not the plumbing. "
        "Otherwise check the claims-index S3 sync, ANTHROPIC_API_KEY, and the "
        "verifier's gh lane on claims-reverify.yml."
    ),
    "ledger-write": (
        "ledger writes: {days} day(s) with dispatched pages missing their "
        "ledger record ({detail}) — those pages' staleness clocks never "
        "advanced, so they will loop back into selection as duplicate "
        "reviews. Check the worker runs' Resolve-ledger-bucket and "
        "Record-review-ledger steps on content-review-article.yml (a "
        "cancelled worker also lands here — that's the point)."
    ),
    "silent-signal": (
        "signal not reported for {days} day(s) ({detail}) — the job that "
        "observes it has not run, or ran without reaching its observation "
        "step. Nothing else watches for a lane that simply stops firing, so "
        "this is the only place it surfaces. Check the workflow's recent runs "
        "and its `if:` gate (an unset repo variable coerces to 0, which makes "
        "a bare `vars.X != '0'` mean OFF)."
    ),
    "capped-pages": (
        "attempt-capped pages: {detail} — each burned "
        "the retry cap on incomplete reviews and is now excluded from every "
        "sweep until a human intervenes. Run `select-articles.py --stats`, "
        "inspect the pages' ledger entries, and either fix what keeps "
        "breaking them or review them by hand."
    ),
}


def log(msg: str) -> None:
    print(f"signal-health: {msg}", file=sys.stderr)


def warn(msg: str) -> None:
    # `::warning::` surfaces in the GitHub Actions run summary — the stateless
    # fallback that works even when the S3 state is unreachable.
    print(f"::warning::signal-health: {msg}", file=sys.stderr)


def parse_day(s: str | None) -> date | None:
    if not s:
        return None
    try:
        return datetime.strptime(str(s), "%Y-%m-%d").date()
    except ValueError:
        return None


# ---- state ------------------------------------------------------------------


def empty_signal() -> dict:
    return {"status": None, "detail": "", "last_ok": None,
            "degraded_since": None, "last_alerted": None}


def load_state(state_path: Path) -> dict:
    """Prior state, or a fresh bootstrap when missing/corrupt (never crash).

    Unknown top-level keys and unknown signals are preserved verbatim so an
    older script version never destroys a newer one's bookkeeping.
    """
    try:
        data = json.loads(state_path.read_text())
        if not isinstance(data, dict) or not isinstance(data.get("signals"), dict):
            raise ValueError("unexpected shape")
        return data
    except (OSError, ValueError, json.JSONDecodeError) as e:
        if state_path.is_file():
            warn(f"health state unreadable ({e}); starting fresh")
        else:
            log("no prior health state; bootstrapping")
        return {"version": STATE_VERSION, "signals": {}}


# ---- observations -----------------------------------------------------------


def observe_traffic(queue_path: Path | None) -> tuple[str, str] | None:
    """(status, detail) from the selection queue's traffic block, or None.

    select-articles.py writes the `traffic` block even on halted queues, so a
    halted run still yields an observation. A missing/unreadable queue file is
    NOT evidence of traffic degradation (the run may have died before
    selection) — return None and leave the prior entry alone.
    """
    if queue_path is None or not queue_path.is_file():
        return None
    try:
        traffic = json.loads(queue_path.read_text()).get("traffic") or {}
    except (OSError, json.JSONDecodeError) as e:
        log(f"queue unreadable ({e}); no traffic observation")
        return None
    if traffic.get("available"):
        detail = f"period={traffic.get('period')} pages_matched={traffic.get('pages_matched')}"
        return "ok", detail
    return "degraded", "snapshot missing, empty, or matched zero pages"


def observe_reverify(report_path: Path | None) -> tuple[str, str] | None:
    """(status, detail) from the nightly re-verify report's meta block, or None.

    reverify-claims.py stamps `meta.skipped` on its couldn't-run exits and
    `meta.n_due` on every run, so a quiet night (nothing due) is distinguishable
    from a dead lane. A missing/unreadable report is NOT evidence of
    degradation (the job may not have run at all) — return None.

    A night degrades when at least REVERIFY_INCONCLUSIVE_RATE of its checks
    are inconclusive — all of them being the limiting case. Demotion (the
    verifier only cited our own docs, so nothing it returned could be trusted
    either way) counts: no drift was detected, which is the thing this signal
    exists to notice. But the count is carried into the detail so the alert
    points at the verifier's source routing rather than at S3 and API keys —
    the remediation for a demoted night is nothing like the one for a dead
    lane.

    That inference needs a sample to stand on, so a mostly-inconclusive night
    under MIN_INCONCLUSIVE_SAMPLE checks yields no observation rather than a
    degraded one. `skipped` and `no_snapshots` are unaffected: a lane that
    could not run says so directly and never depends on the sample size.
    """
    if report_path is None or not report_path.is_file():
        return None
    try:
        meta = json.loads(report_path.read_text()).get("meta") or {}
    except (OSError, json.JSONDecodeError) as e:
        log(f"reverify report unreadable ({e}); no reverify observation")
        return None
    skipped = meta.get("skipped")
    n_due = int(meta.get("n_due") or 0)
    n_checked = int(meta.get("n_checked") or 0)
    n_inconclusive = int(meta.get("n_inconclusive") or 0)
    n_demoted = int(meta.get("n_demoted") or 0)
    if skipped == "no_snapshots":
        return "degraded", "claims index empty or unfetchable"
    if skipped:
        return "degraded", f"{n_due} entities due but run skipped ({skipped})"
    if n_checked and n_inconclusive / n_checked >= REVERIFY_INCONCLUSIVE_RATE:
        if n_checked < MIN_INCONCLUSIVE_SAMPLE:
            log(f"{n_inconclusive} of {n_checked} check(s) inconclusive, but that is "
                f"below the {MIN_INCONCLUSIVE_SAMPLE}-check floor for a lane-wide "
                f"verdict; no reverify observation")
            return None
        if n_inconclusive == n_checked:
            detail = f"all {n_checked} checks inconclusive"
        else:
            detail = (f"{n_inconclusive} of {n_checked} checks inconclusive "
                      f"({n_inconclusive * 100 // n_checked}%)")
        if n_demoted:
            detail += f", {n_demoted} demoted for citing only our own docs"
        return "degraded", detail
    if n_checked:
        return "ok", f"checked={n_checked} inconclusive={n_inconclusive}"
    return "ok", "nothing due tonight"


def observe_capped(queue_path: Path | None) -> tuple[str, str] | None:
    """(status, detail) from the queue's capped list, or None.

    select-articles.py stamps `capped` on every scored queue (empty when no
    page is backed off). A queue without the key (an older queue, or a
    --paths run, which returns before the candidate scan) yields no
    observation — the prior state stands.
    """
    if queue_path is None or not queue_path.is_file():
        return None
    try:
        queue = json.loads(queue_path.read_text())
    except (OSError, json.JSONDecodeError) as e:
        log(f"queue unreadable ({e}); no capped-pages observation")
        return None
    capped = queue.get("capped")
    if not isinstance(capped, list):
        return None
    if capped:
        return "degraded", f"{len(capped)} page(s) stuck at the attempt cap: " + ", ".join(
            str(p) for p in capped)
    return "ok", "no capped pages"


def observe_ledger(last_dispatch_path: Path | None,
                   ledger_dir: Path | None) -> tuple[str, str] | None:
    """(status, detail) from the previous run's dispatch breadcrumb, or None.

    The dispatcher records which slugs it dispatched (health/last-dispatch.json)
    and, on the NEXT run, this compares them against the freshly synced ledger
    cache: every dispatched page should have a ledger record whose reviewed_at
    is on or after the dispatch date — any status counts, because the signal
    watches the write path, not the review outcome. A miss means a worker
    finished (or died) without landing its record — the silent-duplicate bug.

    A missing breadcrumb or ledger dir is NOT evidence (first run, manual run,
    or S3 itself down — the other signals cover that) — return None.
    """
    if (last_dispatch_path is None or not last_dispatch_path.is_file()
            or ledger_dir is None or not ledger_dir.is_dir()):
        return None
    try:
        crumb = json.loads(last_dispatch_path.read_text())
        dispatch_day = parse_day(crumb.get("date"))
        slugs = [str(s) for s in (crumb.get("slugs") or [])]
    except (OSError, json.JSONDecodeError) as e:
        log(f"dispatch breadcrumb unreadable ({e}); no ledger-write observation")
        return None
    if not dispatch_day or not slugs:
        return None
    missing: list[str] = []
    for slug in slugs:
        entry_path = ledger_dir / f"{slug}.json"
        reviewed = None
        if entry_path.is_file():
            try:
                reviewed = parse_day(json.loads(entry_path.read_text()).get("reviewed_at"))
            except (OSError, json.JSONDecodeError):
                reviewed = None
        if reviewed is None or reviewed < dispatch_day:
            missing.append(slug)
    if missing:
        return "degraded", (
            f"{len(missing)} of {len(slugs)} pages dispatched {dispatch_day} "
            f"have no ledger record: {', '.join(sorted(missing))}"
        )
    return "ok", f"all {len(slugs)} pages dispatched {dispatch_day} recorded"


def observe_flag(value: str | None, mapping: dict[str, str]) -> tuple[str, str] | None:
    """(status, detail) from a workflow-provided status flag, or None if omitted."""
    v = (value or "").strip().lower()
    if not v:
        return None
    status = mapping.get(v)
    if status is None:
        log(f"unrecognized status {v!r}; treating as degraded")
        return "degraded", f"unrecognized status {v!r}"
    return status, v


# ---- transitions + alerting ---------------------------------------------------


def apply(state: dict, observations: dict[str, tuple[str, str]], today: date,
          threshold_days: int, realert_days: int, run_url: str | None,
          ) -> tuple[dict, str | None]:
    """Apply one run's observations; return (new state, alert text or None)."""
    signals = state.setdefault("signals", {})
    due: list[str] = []       # alert lines for newly-due signals
    context: list[str] = []   # still-degraded-but-already-alerted, for the message

    for name, (status, detail) in observations.items():
        sig = signals.setdefault(name, empty_signal())
        sig["status"] = status
        sig["detail"] = detail
        # Stamped on every observation, degraded included: this tracks whether
        # anyone is REPORTING, which is a different question from whether the
        # thing reported is healthy.
        sig["last_seen"] = today.isoformat()
        sig.pop("silent", None)
        if status == "ok":
            sig["last_ok"] = today.isoformat()
            sig["degraded_since"] = None
            sig["last_alerted"] = None
        elif status == "degraded":
            if not sig.get("degraded_since"):
                sig["degraded_since"] = today.isoformat()
        else:  # unconfigured
            sig["degraded_since"] = None

    # Silence pass: a signal nobody has reported within its cadence window is
    # degraded on that basis alone. Runs before the alert pass so a newly
    # silent signal alerts on the same schedule as any other.
    for name, sig in sorted(signals.items()):
        if name in observations:
            continue
        seen = parse_day(sig.get("last_seen"))
        if seen is None:
            # Pre-existing state from before last_seen existed, or a signal
            # this run has never met. Start the clock rather than alarming on
            # a gap we cannot actually measure.
            sig["last_seen"] = today.isoformat()
            continue
        quiet = (today - seen).days
        if quiet <= SIGNAL_MAX_SILENCE_DAYS.get(name, DEFAULT_MAX_SILENCE_DAYS):
            continue
        if sig.get("status") == "degraded":
            # Already-degraded and now also unreported: keep the specific
            # finding. It is more actionable than "nobody reported", it is
            # already on the alert clock, and overwriting it would swap a
            # named consequence for a generic one mid-episode. The failure
            # this pass exists for is a signal sitting at OK that quietly
            # stops reporting — green and dead is the invisible combination.
            continue
        sig["status"] = "degraded"
        sig["detail"] = f"{name}: no observation in {quiet} day(s)"
        sig["silent"] = True
        if not sig.get("degraded_since"):
            sig["degraded_since"] = today.isoformat()

    # Alert pass covers every degraded signal in state, observed this run or
    # not — a signal that stops being observed (e.g. selection died) keeps its
    # standing degradation visible.
    for name, sig in sorted(signals.items()):
        if sig.get("status") != "degraded":
            continue
        since = parse_day(sig.get("degraded_since")) or today
        days = (today - since).days
        detail = sig.get("detail") or "no detail"
        # A silent signal's consequence is about the missing REPORTER, not
        # about whatever the signal normally measures.
        key = "silent-signal" if sig.get("silent") else name
        template = CONSEQUENCES.get(key, f"{name}: degraded for {{days}} day(s) ({{detail}})")
        line = template.format(days=days, detail=detail)
        warn(f"{name} degraded since {since.isoformat()} — {line}")
        if days < SIGNAL_THRESHOLDS.get(name, threshold_days):
            continue
        alerted = parse_day(sig.get("last_alerted"))
        if alerted is None or (today - alerted).days >= realert_days:
            sig["last_alerted"] = today.isoformat()
            due.append(line)
        else:
            context.append(line)

    state["version"] = STATE_VERSION
    state["updated"] = today.isoformat()

    if not due:
        return state, None
    lines = due + context
    text = (
        f"Content-review health: {len(lines)} signal(s) degraded "
        "(docs content-review automation)\n"
        + "\n".join(f"• {line}" for line in lines)
    )
    if run_url:
        text += f"\nRun: {run_url}"
    return state, text


# ---- main -------------------------------------------------------------------


def run(args) -> int:
    today = parse_day(args.today) or datetime.now(timezone.utc).date()
    state_path = Path(args.state)
    state = load_state(state_path)

    observations: dict[str, tuple[str, str]] = {}
    obs = observe_traffic(Path(args.queue) if args.queue else None)
    if obs:
        observations["traffic"] = obs
    obs = observe_flag(args.console_status, {"ok": "ok", "degraded": "degraded"})
    if obs:
        observations["console-access"] = obs
    obs = observe_flag(args.holiday_status, {
        "ok": "ok", "empty": "degraded", "fetch_failed": "degraded",
        "unconfigured": "unconfigured",
    })
    if obs:
        observations["holiday-feed"] = obs
    obs = observe_reverify(Path(args.reverify_report) if args.reverify_report else None)
    if obs:
        observations["reverify"] = obs
    obs = observe_ledger(Path(args.last_dispatch) if args.last_dispatch else None,
                         Path(args.ledger_dir) if args.ledger_dir else None)
    if obs:
        observations["ledger-write"] = obs
    obs = observe_capped(Path(args.queue) if args.queue else None)
    if obs:
        observations["capped-pages"] = obs

    state, alert = apply(state, observations, today,
                         args.threshold_days, args.realert_days, args.run_url)

    state_path.write_text(json.dumps(state, indent=2) + "\n")
    log(f"recorded {len(observations)} observation(s) -> {state_path}")

    if alert:
        Path(args.alert_out).write_text(alert + "\n")
        log(f"alert due -> {args.alert_out}")

    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--state", help="health state JSON (read+written in place)")
    p.add_argument("--queue", help="selection queue JSON (source of the traffic signal)")
    p.add_argument("--console-status",
                   help="pulumi/pulumi-service probe result: ok|degraded")
    p.add_argument("--holiday-status",
                   help="holiday feed status: ok|empty|fetch_failed|unconfigured")
    p.add_argument("--reverify-report",
                   help="nightly re-verify report JSON (source of the reverify signal)")
    p.add_argument("--last-dispatch",
                   help="previous run's dispatch breadcrumb JSON (source of the ledger-write signal)")
    p.add_argument("--ledger-dir",
                   help="synced ledger cache dir the breadcrumb is judged against")
    p.add_argument("--alert-out", default=".health-alert.txt",
                   help="alert message path; only written when an alert is due")
    p.add_argument("--today", help="override today's date YYYY-MM-DD (testing)")
    p.add_argument("--threshold-days", type=int, default=THRESHOLD_DAYS)
    p.add_argument("--realert-days", type=int, default=REALERT_DAYS)
    p.add_argument("--run-url", help="workflow run URL appended to the alert")
    p.add_argument("--self-test", action="store_true", help="run built-in smoke checks")
    return p


def main() -> int:
    p = build_parser()
    args = p.parse_args()

    if args.self_test:
        return self_test()
    if not args.state:
        p.error("--state is required (or --self-test)")
    try:
        return run(args)
    except Exception as e:  # noqa: BLE001 - the health lane never fails the dispatcher
        warn(f"unexpected error ({e}); health pass skipped this run")
        return 0


# ---- self-test ----------------------------------------------------------------


def self_test() -> int:
    import tempfile

    failures = []

    def check(name, cond):
        if not cond:
            failures.append(name)
            print(f"FAIL: {name}", file=sys.stderr)
        else:
            print(f"ok: {name}")

    def run_once(d: Path, day: str, queue: dict | None = None, console: str | None = None,
                 holiday: str | None = None, reverify: dict | None = None,
                 last_dispatch: dict | None = None, ledger_dir: Path | None = None,
                 ) -> tuple[dict, str | None]:
        """Drive run() through argparse the way the workflow would."""
        state = d / "state.json"
        alert = d / "alert.txt"
        if alert.exists():
            alert.unlink()
        argv = ["--state", str(state), "--alert-out", str(alert), "--today", day]
        if queue is not None:
            qp = d / "queue.json"
            qp.write_text(json.dumps(queue))
            argv += ["--queue", str(qp)]
        if console:
            argv += ["--console-status", console]
        if holiday:
            argv += ["--holiday-status", holiday]
        if reverify is not None:
            rp = d / "reverify-report.json"
            rp.write_text(json.dumps(reverify))
            argv += ["--reverify-report", str(rp)]
        if last_dispatch is not None:
            lp = d / "last-dispatch.json"
            lp.write_text(json.dumps(last_dispatch))
            argv += ["--last-dispatch", str(lp)]
        if ledger_dir is not None:
            argv += ["--ledger-dir", str(ledger_dir)]
        args = build_parser().parse_args(argv)
        run(args)
        text = alert.read_text() if alert.exists() else None
        return json.loads(state.read_text()), text

    q_ok = {"traffic": {"available": True, "period": "2026-06", "pages_matched": 731}}
    q_bad = {"traffic": {"available": False, "pages_matched": 0}}
    q_halted = {"halted": "max_open_prs", "traffic": {"available": False}, "articles": []}

    with tempfile.TemporaryDirectory() as tmp:
        d = Path(tmp)

        # 1. Bootstrap: no state file, everything ok.
        st, alert = run_once(d, "2026-07-01", queue=q_ok, console="ok", holiday="ok")
        check("bootstrap: all three signals recorded",
              set(st["signals"]) == {"traffic", "console-access", "holiday-feed"})
        check("bootstrap: ok stamps last_ok",
              st["signals"]["traffic"]["last_ok"] == "2026-07-01")
        check("bootstrap: nothing degraded, no alert", alert is None)

        # 2. ok -> degraded starts the clock; no alert before threshold.
        st, alert = run_once(d, "2026-07-02", queue=q_bad, console="ok", holiday="ok")
        check("degradation sets degraded_since",
              st["signals"]["traffic"]["degraded_since"] == "2026-07-02")
        check("no alert before threshold", alert is None)

        # 3. Clock persists; alert fires exactly at THRESHOLD_DAYS.
        st, alert = run_once(d, "2026-07-05", queue=q_bad, console="ok", holiday="ok")
        check("degraded_since unchanged across runs",
              st["signals"]["traffic"]["degraded_since"] == "2026-07-02")
        check("still quiet at day 3", alert is None)
        st, alert = run_once(d, "2026-07-09", queue=q_bad, console="ok", holiday="ok")
        check("alert fires at day 7", alert is not None)
        check("alert names the consequence", alert and "tier-only" in alert)
        check("last_alerted stamped",
              st["signals"]["traffic"]["last_alerted"] == "2026-07-09")

        # 4. Re-alert suppressed inside REALERT_DAYS, fires after.
        st, alert = run_once(d, "2026-07-10", queue=q_bad, console="ok", holiday="ok")
        check("re-alert suppressed next day", alert is None)
        st, alert = run_once(d, "2026-07-16", queue=q_bad, console="ok", holiday="ok")
        check("re-alert fires after REALERT_DAYS", alert is not None)

        # 5. Recovery clears both clocks; a fresh episode alerts on its own clock.
        st, alert = run_once(d, "2026-07-17", queue=q_ok, console="ok", holiday="ok")
        check("recovery clears degraded_since",
              st["signals"]["traffic"]["degraded_since"] is None)
        check("recovery clears last_alerted",
              st["signals"]["traffic"]["last_alerted"] is None)
        st, alert = run_once(d, "2026-07-18", queue=q_bad, console="ok", holiday="ok")
        check("fresh episode restarts the clock",
              st["signals"]["traffic"]["degraded_since"] == "2026-07-18")
        check("fresh episode quiet before its own threshold", alert is None)

    with tempfile.TemporaryDirectory() as tmp:
        d = Path(tmp)

        # 6. unconfigured holiday never alerts, even long after threshold.
        run_once(d, "2026-01-01", queue=q_ok, console="ok", holiday="unconfigured")
        st, alert = run_once(d, "2026-03-01", queue=q_ok, console="ok",
                             holiday="unconfigured")
        check("unconfigured recorded as its own status",
              st["signals"]["holiday-feed"]["status"] == "unconfigured")
        check("unconfigured never alerts", alert is None)

        # 7. Missing queue -> traffic entry untouched (prior degraded preserved).
        run_once(d, "2026-03-02", queue=q_bad, console="ok", holiday="ok")
        st, alert = run_once(d, "2026-03-03", console="ok", holiday="ok")
        check("missing queue leaves prior traffic state untouched",
              st["signals"]["traffic"]["status"] == "degraded"
              and st["signals"]["traffic"]["degraded_since"] == "2026-03-02")

        # 8. Unobserved-but-degraded signals still alert once due.
        st, alert = run_once(d, "2026-03-12", console="ok", holiday="ok")
        check("unobserved degraded signal still alerts when due",
              alert is not None and "tier-only" in alert)

    with tempfile.TemporaryDirectory() as tmp:
        d = Path(tmp)

        # 9. Corrupt state bootstraps without crashing.
        (d / "state.json").write_text("{not json")
        st, alert = run_once(d, "2026-07-01", queue=q_ok, console="ok", holiday="ok")
        check("corrupt state bootstraps cleanly",
              st["signals"]["traffic"]["status"] == "ok")

        # 10. Multiple due signals -> one combined message, one line each.
        run_once(d, "2026-08-01", queue=q_bad, console="degraded", holiday="fetch_failed")
        st, alert = run_once(d, "2026-08-10", queue=q_bad, console="degraded",
                             holiday="fetch_failed")
        check("multiple due signals -> one combined alert",
              alert is not None and alert.count("•") == 3)
        check("combined alert covers each consequence",
              alert is not None and "tier-only" in alert
              and "unverifiable" in alert and "fails open" in alert)
        check("holiday detail names the failure mode",
              alert is not None and "fetch_failed" in alert)

        # 11. Halted queue still yields a traffic observation.
        st, alert = run_once(d, "2026-08-11", queue=q_halted, console="ok", holiday="ok")
        check("halted queue still observes traffic",
              st["signals"]["traffic"]["status"] == "degraded")

    rv_ok = {"meta": {"n_snapshots": 40, "n_entities": 90, "n_due": 25,
                      "n_checked": 25, "n_stale": 1, "n_fresh": 22, "n_inconclusive": 2}}
    rv_quiet = {"meta": {"n_snapshots": 40, "n_entities": 90, "n_due": 0,
                         "n_checked": 0, "n_stale": 0, "n_fresh": 0, "n_inconclusive": 0}}
    rv_dead = {"meta": {"n_snapshots": 40, "n_entities": 90, "n_due": 25,
                        "n_checked": 25, "n_stale": 0, "n_fresh": 0, "n_inconclusive": 25}}
    rv_demoted = {"meta": {"n_snapshots": 40, "n_entities": 90, "n_due": 25,
                           "n_checked": 25, "n_stale": 0, "n_fresh": 0,
                           "n_inconclusive": 25, "n_demoted": 22}}
    rv_nokey = {"meta": {"n_snapshots": 40, "n_entities": 90, "n_due": 25,
                         "n_checked": 0, "n_stale": 0, "n_fresh": 0, "n_inconclusive": 0,
                         "skipped": "no_api_key"}}
    rv_nosnaps = {"meta": {"n_snapshots": 0, "n_entities": 0, "n_due": 0,
                           "n_checked": 0, "n_stale": 0, "n_fresh": 0, "n_inconclusive": 0,
                           "skipped": "no_snapshots"}}
    # The 2026-08-19 shape: a one-entity rotation chunk, demoted, which used to
    # read as a lane-wide "no conclusive results".
    rv_thin = {"meta": {"n_snapshots": 100, "n_entities": 54, "n_due": 1,
                        "n_checked": 1, "n_stale": 0, "n_fresh": 0,
                        "n_inconclusive": 1, "n_demoted": 1}}
    # 19 of 25 (76%): a lane producing almost nothing. 12 of 25 (48%) is
    # noisy but working — and is roughly what 2026-09-03 looked like.
    rv_mostly = {"meta": {"n_snapshots": 40, "n_entities": 90, "n_due": 25,
                          "n_checked": 25, "n_stale": 0, "n_fresh": 6,
                          "n_inconclusive": 19, "n_demoted": 4}}
    rv_half = {"meta": {"n_snapshots": 40, "n_entities": 90, "n_due": 20,
                        "n_checked": 20, "n_stale": 2, "n_fresh": 8,
                        "n_inconclusive": 10, "n_demoted": 9}}

    with tempfile.TemporaryDirectory() as tmp:
        d = Path(tmp)

        # 12. Reverify observations: conclusive results and quiet nights are ok.
        st, alert = run_once(d, "2026-09-01", reverify=rv_ok)
        check("reverify with conclusive results is ok",
              st["signals"]["reverify"]["status"] == "ok")
        st, alert = run_once(d, "2026-09-02", reverify=rv_quiet)
        check("reverify quiet night (nothing due) is ok",
              st["signals"]["reverify"]["status"] == "ok")

        # A mostly-inconclusive night degrades on the rate, not only at 100%,
        # and the detail carries the fraction; a noisy-but-working night is ok
        # and clears it.
        st, alert = run_once(d, "2026-09-02", reverify=rv_mostly)
        check("mostly-inconclusive night degrades on the rate",
              st["signals"]["reverify"]["status"] == "degraded"
              and "19 of 25" in st["signals"]["reverify"]["detail"]
              and "4 demoted" in st["signals"]["reverify"]["detail"])
        st, alert = run_once(d, "2026-09-02", reverify=rv_half)
        check("half-inconclusive night is ok and clears the degradation",
              st["signals"]["reverify"]["status"] == "ok"
              and st["signals"]["reverify"]["degraded_since"] is None)

        # 13. All-inconclusive and couldn't-run reports degrade; alert names
        # the consequence once due.
        st, alert = run_once(d, "2026-09-03", reverify=rv_dead)
        check("all-inconclusive reverify degrades",
              st["signals"]["reverify"]["status"] == "degraded"
              and st["signals"]["reverify"]["degraded_since"] == "2026-09-03")
        st, alert = run_once(d, "2026-09-06", reverify=rv_nokey)
        check("skipped run stays degraded with skip detail",
              st["signals"]["reverify"]["status"] == "degraded"
              and "no_api_key" in st["signals"]["reverify"]["detail"])

        # A night too short to generalize from is not evidence either way:
        # the prior state (degraded, from rv_nokey above) stands untouched
        # rather than being re-asserted or cleared by a sample of one.
        prior = dict(st["signals"]["reverify"])
        st, alert = run_once(d, "2026-09-06", reverify=rv_thin)
        check("a 1-check all-inconclusive night yields no observation",
              st["signals"]["reverify"] == prior)

        # An all-demoted night is still no drift detection, so it still
        # degrades — but the detail has to name demotion, or the alert sends
        # the on-call after S3 and API keys for a routing problem.
        st, alert = run_once(d, "2026-09-07", reverify=rv_demoted)
        check("all-demoted night still degrades",
              st["signals"]["reverify"]["status"] == "degraded")
        check("all-demoted detail names the cause",
              "22 demoted" in st["signals"]["reverify"]["detail"])
        st, alert = run_once(d, "2026-09-10", reverify=rv_dead)
        check("reverify alert fires at threshold and names the consequence",
              alert is not None and "volatile-claim drift" in alert)

        # 14. Missing report leaves prior state untouched; empty claims index
        # counts as degraded (mirrors the traffic snapshot semantics).
        st, alert = run_once(d, "2026-09-11")
        check("missing reverify report leaves prior state untouched",
              st["signals"]["reverify"]["status"] == "degraded")
        st, alert = run_once(d, "2026-09-12", reverify=rv_nosnaps)
        check("empty claims index degrades with its own detail",
              "claims index" in st["signals"]["reverify"]["detail"])
        # --- silence detection: the failure nothing else can see -------------
        # A lane that stops firing reports nothing, and "no observation" means
        # "prior state stands" — so a dead lane sits at whatever it last said,
        # usually ok. These pin that silence eventually becomes the finding.
        st, alert = run_once(d, "2026-09-13", reverify=rv_ok)
        check("reverify recovery clears the clocks",
              st["signals"]["reverify"]["status"] == "ok"
              and st["signals"]["reverify"]["degraded_since"] is None)

    # ---- ledger-write signal ----
    with tempfile.TemporaryDirectory() as tmp:
        d = Path(tmp)
        ledger = d / "ledger-cache"
        ledger.mkdir()
        crumb = {"date": "2026-08-01", "slugs": ["docs-a", "docs-b"]}

        def write_entry(slug: str, reviewed_at: str | None) -> None:
            (ledger / f"{slug}.json").write_text(
                json.dumps({"slug": slug, "reviewed_at": reviewed_at, "status": "clean"}))

        # All dispatched pages recorded (same-day or later) -> ok.
        write_entry("docs-a", "2026-08-01")
        write_entry("docs-b", "2026-08-02")
        st, alert = run_once(d, "2026-08-02", last_dispatch=crumb, ledger_dir=ledger)
        check("ledger-write: all recorded -> ok",
              st["signals"]["ledger-write"]["status"] == "ok")

        # One page's record predates the dispatch (write dropped) -> degraded,
        # slug named in the detail.
        write_entry("docs-b", "2026-07-20")
        st, alert = run_once(d, "2026-08-03", last_dispatch=crumb, ledger_dir=ledger)
        check("ledger-write: stale record -> degraded",
              st["signals"]["ledger-write"]["status"] == "degraded")
        check("ledger-write: detail names the missing slug",
              "docs-b" in st["signals"]["ledger-write"]["detail"]
              and "docs-a" not in st["signals"]["ledger-write"]["detail"])

        # A missing entry file counts as a miss too.
        (ledger / "docs-b.json").unlink()
        st, alert = run_once(d, "2026-08-04", last_dispatch=crumb, ledger_dir=ledger)
        check("ledger-write: absent record -> degraded",
              st["signals"]["ledger-write"]["status"] == "degraded")

        # No breadcrumb -> no observation; prior state untouched.
        st, alert = run_once(d, "2026-08-05", ledger_dir=ledger)
        check("ledger-write: missing breadcrumb leaves prior state untouched",
              st["signals"]["ledger-write"]["status"] == "degraded"
              and st["signals"]["ledger-write"]["degraded_since"] == "2026-08-03")

        # Recovery clears the clocks.
        write_entry("docs-b", "2026-08-01")
        st, alert = run_once(d, "2026-08-06", last_dispatch=crumb, ledger_dir=ledger)
        check("ledger-write: recovery clears degraded_since",
              st["signals"]["ledger-write"]["status"] == "ok"
              and st["signals"]["ledger-write"]["degraded_since"] is None)

    # ---- capped-pages signal (day-one threshold override) ----
    with tempfile.TemporaryDirectory() as tmp:
        d = Path(tmp)
        q_capped = {"traffic": {"available": False}, "capped": ["content/docs/x.md"]}
        q_clear = {"traffic": {"available": False}, "capped": []}
        q_legacy = {"traffic": {"available": False}}

        st, alert = run_once(d, "2026-09-01", queue=q_capped)
        check("capped: non-empty list degrades",
              st["signals"]["capped-pages"]["status"] == "degraded")
        check("capped: alerts on the first observed day (threshold override)",
              alert is not None and "content/docs/x.md" in alert)
        st, alert = run_once(d, "2026-09-02", queue=q_capped)
        check("capped: re-alert still paced by REALERT_DAYS", alert is None)
        st, alert = run_once(d, "2026-09-03", queue=q_legacy)
        check("capped: legacy queue without the key leaves prior state untouched",
              st["signals"]["capped-pages"]["status"] == "degraded")
        st, alert = run_once(d, "2026-09-04", queue=q_clear)
        check("capped: empty list recovers the signal",
              st["signals"]["capped-pages"]["status"] == "ok"
              and st["signals"]["capped-pages"]["degraded_since"] is None)

    with tempfile.TemporaryDirectory() as tmp:
        d = Path(tmp)
        st, _ = run_once(d, "2026-10-01", reverify=rv_ok)
        check("an observation stamps last_seen",
              st["signals"]["reverify"]["last_seen"] == "2026-10-01")
        st, _ = run_once(d, "2026-10-03", console="ok")
        check("a lane quiet inside its window stays ok",
              st["signals"]["reverify"]["status"] == "ok")
        st, _ = run_once(d, "2026-10-06", console="ok")
        check("a lane silent past its window degrades",
              st["signals"]["reverify"]["status"] == "degraded"
              and st["signals"]["reverify"].get("silent") is True)
        check("the silent detail says nobody reported, not that the thing broke",
              "no observation in" in st["signals"]["reverify"]["detail"])
        st, alert = run_once(d, "2026-10-16", console="ok")
        check("a silent lane eventually alerts",
              alert is not None and "signal not reported" in alert)
        check("the silent alert names the gate bug that caused this before",
              alert is not None and "vars.X" in alert)
        st, _ = run_once(d, "2026-10-17", reverify=rv_ok)
        check("a lane that reports again recovers",
              st["signals"]["reverify"]["status"] == "ok"
              and "silent" not in st["signals"]["reverify"])

    with tempfile.TemporaryDirectory() as tmp:
        d = Path(tmp)
        (d / "state.json").write_text(json.dumps({
            "version": 1, "updated": "2026-01-01",
            "signals": {"reverify": {"status": "ok", "detail": "ok",
                                     "last_ok": "2026-01-01",
                                     "degraded_since": None, "last_alerted": None}}}))
        st, alert = run_once(d, "2026-10-01", console="ok")
        check("legacy state without last_seen starts the clock, never alarms",
              st["signals"]["reverify"]["status"] == "ok"
              and st["signals"]["reverify"]["last_seen"] == "2026-10-01")

    if failures:
        print(f"\n{len(failures)} failure(s)", file=sys.stderr)
        return 1
    print("\nall signal-health self-tests passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Tests for stale-pr-sweep.py — what counts as movement, the heads-up/close
sequence, the extended-label window, and the dry-run and cap contracts.

Runs under pytest (make test-review-pipeline) and standalone via
`stale-pr-sweep.py --self-test` (run_standalone below, same convention as
test_sla_sweep.py). No pytest fixtures, so every test runs unmodified
outside pytest.
"""

from __future__ import annotations

import copy
import importlib.util
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


sweep_mod = _load("stale_pr_sweep_under_test", HERE / "stale-pr-sweep.py")
import routing  # noqa: E402

NOW = datetime(2026, 11, 2, 15, 17, tzinfo=timezone.utc)
STALE = {"close_days": 30, "notice_days": 7, "extended_label": "review:long-running",
         "extended_close_days": 90}

RAW_CONFIG = copy.deepcopy(routing._CANNED_CONFIG)
RAW_CONFIG["bots"] = ["pulumi-bot"]
RAW_CONFIG["stale_prs"] = dict(STALE)
CONFIG, _errors, _warnings = routing.validate_raw(RAW_CONFIG)
assert CONFIG is not None, _errors
BOTS = set(CONFIG.bots)

HUMAN = {"login": "octocat", "type": "User"}
REVIEWER = {"login": "reviewer", "type": "User"}
ACTIONS_BOT = {"login": "github-actions[bot]", "type": "Bot"}
PULUMI_BOT = {"login": "pulumi-bot", "type": "User"}  # type: User, caught by the bots: list


def ago(days: float) -> str:
    return (NOW - timedelta(days=days)).isoformat()


def pr(number: int = 1, *, created_days_ago: float = 200, labels=(), draft=False) -> dict:
    return {"number": number, "title": f"PR {number}", "url": f"https://github.com/pulumi/docs/pull/{number}",
            "isDraft": draft, "createdAt": ago(created_days_ago),
            "author": {"login": "octocat"}, "labels": [{"name": n} for n in labels]}


def commit(days: float) -> dict:
    return {"event": "committed", "sha": "a" * 40,
            "author": {"date": ago(days + 1)}, "committer": {"date": ago(days)}}


def comment(days: float, who: dict = HUMAN, body: str = "a comment") -> dict:
    return {"event": "commented", "actor": who, "user": who, "created_at": ago(days), "body": body}


def heads_up(days: float, close_days: int = 30, who: dict = PULUMI_BOT) -> dict:
    return comment(days, who, f"<!-- STALE_PR_SWEEP:warn close_days={close_days} -->\nHeads up")


def event(name: str, days: float, who: dict = HUMAN) -> dict:
    return {"event": name, "actor": who, "created_at": ago(days)}


def evaluate(p: dict, timeline: list[dict]) -> dict:
    return sweep_mod.evaluate(p, timeline, STALE, BOTS, NOW)


class StubGh:
    def __init__(self, prs: list[dict], timelines: dict[int, list]):
        self.prs = prs
        self.timelines = timelines
        self.comments: list[tuple[int, str]] = []
        self.closed: list[tuple[int, str]] = []

    def list_open_prs(self):
        return self.prs

    def get_timeline(self, number):
        t = self.timelines[number]
        if isinstance(t, Exception):
            raise t
        return t

    def create_issue_comment(self, number, body):
        self.comments.append((number, body))

    def close_pr(self, number, body):
        self.closed.append((number, body))


# ---- movement ----------------------------------------------------------------


def test_baseline_is_pr_creation():
    moved, what = sweep_mod.last_movement([], ago(12), BOTS)
    assert what == "opened" and moved == NOW - timedelta(days=12)


def test_commits_and_force_pushes_move_the_clock():
    moved, what = sweep_mod.last_movement([commit(40), commit(9)], ago(60), BOTS)
    assert what == "commit" and moved == NOW - timedelta(days=9)
    moved, what = sweep_mod.last_movement(
        [commit(40), {"event": "head_ref_force_pushed", "actor": PULUMI_BOT, "created_at": ago(3)}],
        ago(60), BOTS)
    assert what == "force-push" and moved == NOW - timedelta(days=3)


def test_human_comments_reviews_and_state_changes_move_the_clock():
    for tl, expect in (
        ([comment(5)], "commented by octocat"),
        ([{"event": "reviewed", "user": REVIEWER, "submitted_at": ago(5), "state": "commented"}],
         "review by reviewer"),
        ([{"event": "line-commented", "comments": [{"user": REVIEWER, "created_at": ago(5)}]}],
         "review comment by reviewer"),
        ([event("reopened", 5)], "reopened by octocat"),
        ([event("ready_for_review", 5)], "ready_for_review by octocat"),
        ([event("convert_to_draft", 5)], "convert_to_draft by octocat"),
        ([event("renamed", 5)], "renamed by octocat"),
    ):
        moved, what = sweep_mod.last_movement(tl, ago(60), BOTS)
        assert what == expect, (tl, what)
        assert moved == NOW - timedelta(days=5)


def test_bots_never_move_the_clock():
    timeline = [
        comment(1, ACTIONS_BOT),
        comment(1, PULUMI_BOT),                         # type: User, but in bots:
        comment(1, {"login": "claude[bot]", "type": "User"}),
        comment(1, None),                               # deleted account
        {"event": "reviewed", "user": PULUMI_BOT, "submitted_at": ago(1)},
        {"event": "line-commented", "comments": [{"user": ACTIONS_BOT, "created_at": ago(1)}]},
        event("ready_for_review", 1, ACTIONS_BOT),
    ]
    moved, what = sweep_mod.last_movement(timeline, ago(60), BOTS)
    assert what == "opened", what


def test_labels_requests_and_mentions_do_not_move_the_clock():
    # `mentioned` names the person a bot comment pinged as its actor; counting
    # it would let an SLA escalation reset the clock for whoever it named.
    timeline = [event("labeled", 1), event("unlabeled", 1), event("review_requested", 1),
                event("mentioned", 1), event("subscribed", 1), event("assigned", 1)]
    _, what = sweep_mod.last_movement(timeline, ago(60), BOTS)
    assert what == "opened", what


def test_unparsable_timestamp_raises_for_the_caller_to_skip():
    try:
        sweep_mod.last_movement([comment(1) | {"created_at": "not a date"}], ago(60), BOTS)
    except ValueError:
        return
    raise AssertionError("expected ValueError")


# ---- the heads-up / close sequence ------------------------------------------------


def test_fresh_pr_is_left_alone():
    v = evaluate(pr(created_days_ago=60), [commit(10)])
    assert v["type"] == "none" and v["closes_in_days"] == 20


def test_heads_up_at_close_minus_notice():
    v = evaluate(pr(created_days_ago=60), [commit(23.5)])
    assert v["type"] == "warn" and v["close_days"] == 30 and v["closes_in_days"] == 7


def test_long_idle_pr_still_gets_full_notice_before_close():
    # First run against a 200-day-old PR: heads-up now, close a week from now,
    # never a cold close.
    v = evaluate(pr(), [])
    assert v["type"] == "warn" and v["closes_in_days"] == 7


def test_heads_up_is_not_repeated():
    v = evaluate(pr(created_days_ago=60), [commit(26), heads_up(2)])
    assert v["type"] == "none" and v["closes_in_days"] == 5


def test_close_after_window_and_notice():
    v = evaluate(pr(created_days_ago=60), [commit(30.5), heads_up(7)])
    assert v["type"] == "close"


def test_close_waits_for_full_notice_even_past_window():
    v = evaluate(pr(), [heads_up(3)])
    assert v["type"] == "none" and v["closes_in_days"] == 4


def test_cron_jitter_does_not_cost_a_day():
    # Heads-up landed a few minutes "late" last week; this run is on time.
    v = evaluate(pr(created_days_ago=60), [commit(31), heads_up(7 - 0.02)])
    assert v["type"] == "close"


def test_movement_after_heads_up_rearms():
    # The author commented after the heads-up: old heads-up is spent, the clock
    # restarted, and nothing happens until the next window comes round.
    v = evaluate(pr(created_days_ago=90), [heads_up(10), comment(9)])
    assert v["type"] == "none" and v["closes_in_days"] == 21


def test_heads_up_from_a_human_does_not_count():
    fake = heads_up(8, who=HUMAN)  # a person pasting the marker is still a person commenting
    v = evaluate(pr(created_days_ago=60), [commit(40), fake])
    assert v["type"] == "none"
    assert v["last_movement_was"] == "commented by octocat"


# ---- the extended label ------------------------------------------------------------


def test_extended_label_buys_the_longer_window():
    v = evaluate(pr(labels=["review:long-running"]), [commit(40)])
    assert v["type"] == "none" and v["extended"] and v["close_days"] == 90
    assert v["closes_in_days"] == 50


def test_extended_label_is_a_grace_period_not_an_exemption():
    v = evaluate(pr(labels=["review:long-running"]), [commit(84)])
    assert v["type"] == "warn" and v["close_days"] == 90
    v = evaluate(pr(labels=["review:long-running"]), [commit(91), heads_up(8, close_days=90)])
    assert v["type"] == "close"


def test_label_added_after_heads_up_needs_a_new_heads_up_for_its_window():
    # Warned on the 30-day window, then labeled: no close at 30, and the 90-day
    # window gets its own heads-up.
    labeled = pr(labels=["review:long-running"])
    v = evaluate(labeled, [commit(31), heads_up(8, close_days=30)])
    assert v["type"] == "none"
    v = evaluate(labeled, [commit(85), heads_up(62, close_days=30)])
    assert v["type"] == "warn" and v["close_days"] == 90


def test_label_removed_falls_back_to_base_window():
    v = evaluate(pr(), [commit(85), heads_up(2, close_days=90)])
    assert v["type"] == "warn" and v["close_days"] == 30 and v["closes_in_days"] == 7


# ---- sweep(): mutations, dry run, cap, failure isolation ----------------------------


def test_sweep_warns_and_closes():
    gh = StubGh([pr(1, created_days_ago=60), pr(2, created_days_ago=60), pr(3, created_days_ago=60)],
                {1: [commit(5)], 2: [commit(24)], 3: [commit(31), heads_up(7)]})
    record = sweep_mod.sweep(gh, CONFIG, now=NOW, dry_run=False)
    assert [n for n, _ in gh.comments] == [2]
    assert [n for n, _ in gh.closed] == [3]
    assert record["counts"] == {"none": 1, "warn": 1, "close": 1}
    assert "STALE_PR_SWEEP:warn close_days=30" in gh.comments[0][1]
    assert "STALE_PR_SWEEP:close close_days=30" in gh.closed[0][1]


def test_dry_run_mutates_nothing():
    gh = StubGh([pr(2, created_days_ago=60), pr(3, created_days_ago=60)],
                {2: [commit(24)], 3: [commit(31), heads_up(7)]})
    record = sweep_mod.sweep(gh, CONFIG, now=NOW, dry_run=True)
    assert gh.comments == [] and gh.closed == []
    assert record["dry_run"] and record["counts"] == {"warn": 1, "close": 1}


def test_drafts_and_bot_prs_are_swept_too():
    gh = StubGh([pr(1, draft=True), pr(2) | {"author": {"login": "pulumi-bot"}}],
                {1: [heads_up(8)], 2: [heads_up(8)]})
    sweep_mod.sweep(gh, CONFIG, now=NOW, dry_run=False)
    assert sorted(n for n, _ in gh.closed) == [1, 2]


def test_max_closes_defers_the_rest():
    prs = [pr(n) for n in range(1, 6)]
    gh = StubGh(prs, {n: [heads_up(8)] for n in range(1, 6)})
    record = sweep_mod.sweep(gh, CONFIG, now=NOW, dry_run=False, max_closes=2)
    assert len(gh.closed) == 2
    assert record["counts"] == {"close": 2, "deferred": 3}


def test_one_bad_pr_does_not_stop_the_sweep():
    gh = StubGh([pr(1), pr(2)], {1: RuntimeError("boom"), 2: [heads_up(8)]})
    record = sweep_mod.sweep(gh, CONFIG, now=NOW, dry_run=False)
    assert [n for n, _ in gh.closed] == [2]
    assert record["counts"] == {"skipped": 1, "close": 1}


def test_missing_policy_refuses_to_run():
    raw = copy.deepcopy(RAW_CONFIG)
    del raw["stale_prs"]
    cfg, errs, _ = routing.validate_raw(raw)
    assert errs == []
    try:
        sweep_mod.sweep(StubGh([], {}), cfg, now=NOW, dry_run=True)
    except SystemExit:
        return
    raise AssertionError("expected SystemExit without a stale_prs block")


# ---- comment copy -----------------------------------------------------------------


def _all_bodies() -> list[str]:
    return [
        sweep_mod.warn_body(30, False, 23, 7, STALE),
        sweep_mod.warn_body(90, True, 83, 7, STALE),
        sweep_mod.close_body(30, False, 30, STALE),
        sweep_mod.close_body(90, True, 90, STALE),
    ]


def test_comment_bodies_trigger_nothing():
    # Posted with a token whose comments fire issue_comment workflows, which
    # match these as bare substrings (claude.yml, claude-update.yml, ...).
    for body in _all_bodies():
        for trigger in ("@claude", "/update-review", "/new-review", "/social-review",
                        "#update-review", "#new-review", "/oversized-ack"):
            assert trigger not in body, (trigger, body)


def test_comment_bodies_carry_parseable_markers():
    for body in _all_bodies():
        assert sweep_mod.MARKER_RE.search(body), body


def test_base_window_copy_explains_the_label():
    assert "`review:long-running`" in sweep_mod.close_body(30, False, 30, STALE)
    assert "90 days" in sweep_mod.close_body(30, False, 30, STALE)
    assert "`review:long-running`" in sweep_mod.warn_body(30, False, 23, 7, STALE)


def test_comment_copy_has_no_em_dashes():
    for body in _all_bodies():
        assert "—" not in body, body


# ---- config on disk ---------------------------------------------------------------


def test_shipped_policy_matches_the_agreed_numbers():
    real = routing.load_config(HERE.parents[1] / ".github" / "review-routing.yml")
    assert real.stale_prs == {"close_days": 30, "notice_days": 7,
                              "extended_label": "review:long-running", "extended_close_days": 90}


def test_step_summary_renders():
    gh = StubGh([pr(1, created_days_ago=60), pr(2, created_days_ago=60)],
                {1: [commit(5)], 2: [commit(24)]})
    out = sweep_mod.step_summary(sweep_mod.sweep(gh, CONFIG, now=NOW, dry_run=True))
    assert "Would warn" in out and "#2" in out and "closes in ~25d" in out
    assert re.search(r"\(dry run\)", out)


def run_standalone() -> int:
    """The --self-test harness, bound at call time so it sees every test."""
    all_tests = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    failures = 0
    for t in all_tests:
        try:
            t()
            print(f"  ok: {t.__name__}")
        except AssertionError as exc:
            failures += 1
            print(f"  FAIL: {t.__name__}: {exc}", file=sys.stderr)
        except Exception as exc:  # noqa: BLE001 — a crash is a failure, not a harness abort
            failures += 1
            print(f"  FAIL: {t.__name__}: {type(exc).__name__}: {exc}", file=sys.stderr)
    if failures:
        print(f"{failures} stale-pr-sweep test(s) failed", file=sys.stderr)
        return 1
    print("all stale-pr-sweep self-tests passed")
    return 0


if __name__ == "__main__":
    sys.exit(run_standalone())

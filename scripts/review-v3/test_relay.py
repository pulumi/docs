#!/usr/bin/env python3
"""relay.py: the grammar a board click is read against, and the digest gate
that makes Confirm run exactly the plan whose preview the person read.

    python3 -m pytest scripts/review-v3/test_relay.py -q
    python3 scripts/review-v3/relay.py --self-test
"""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import relay  # noqa: E402


def _raises(fn, needle: str) -> None:
    try:
        fn()
    except relay.RelayError as exc:
        assert needle in str(exc), f"{needle!r} not in {exc!r}"
        return
    raise AssertionError(f"expected RelayError containing {needle!r}")


def _plan(td: Path, created: datetime | None = None, steps: list | None = None) -> Path:
    p = td / ".pr-review-plan.json"
    p.write_text(json.dumps({"schema": 2, "repo": "pulumi/docs",
                             "created_at": (created or datetime.now(timezone.utc)).isoformat(),
                             "options": {}, "steps": steps or []}, indent=1) + "\n")
    return p


def test_a_plan_message_parses_into_act_argv():
    got = relay.parse("pr-review relay: plan\n/pr-review --act --stamp 22295,22297 --force --refresh 22231 --reason \"22231=stale after a push\"")
    assert got == {"kind": "plan", "argv": ["--stamp", "22295,22297", "--force", "--refresh", "22231", "--reason", "22231=stale after a push"]}


def test_the_board_prompt_sign_is_tolerated():
    assert relay.parse("pr-review relay: plan\n$ /pr-review --act --ask-fix 22282")["argv"] == ["--ask-fix", "22282"]


def test_operator_flags_are_refused_from_a_click():
    for flag in ("--execute .pr-review-plan.json", "--in other.json", "--plan-out x.json", "--backend snapshot",
                 "--snapshot-dir /tmp", "--dry-run", "--expect-digest 0123456789abcdef", "--preview-out p.txt", "--in=other.json"):
        _raises(lambda f=flag: relay.parse(f"pr-review relay: plan\n/pr-review --act --refresh 1 {f}"), "not something the board may set")


def test_a_command_act_refuses_is_refused_here():
    _raises(lambda: relay.parse("pr-review relay: plan\n/pr-review --act --stamp 1 --bogus"), "act.py refuses")
    _raises(lambda: relay.parse("pr-review relay: plan\n/pr-review --act --refresh notanumber"), "act.py refuses")


def test_an_empty_command_names_no_action():
    _raises(lambda: relay.parse("pr-review relay: plan\n/pr-review --act"), "no action")
    _raises(lambda: relay.parse("pr-review relay: plan\n/pr-review --act --force"), "no action")


def test_only_the_pr_review_command_is_accepted():
    _raises(lambda: relay.parse("pr-review relay: plan\nrm -rf /"), "exactly one")
    _raises(lambda: relay.parse("pr-review relay: plan\n/pr-review --act --refresh 1\n/pr-review --act --refresh 2"), "one command line")
    _raises(lambda: relay.parse("pr-review relay: plan\n/pr-review --act --reason \"unterminated"), "does not parse")


def test_confirm_cancel_and_refresh():
    assert relay.parse("pr-review relay: confirm 0123456789abcdef") == {"kind": "confirm", "digest": "0123456789abcdef"}
    assert relay.parse("  pr-review relay: cancel 0123456789abcdef\n") == {"kind": "cancel", "digest": "0123456789abcdef"}
    assert relay.parse("pr-review relay: refresh") == {"kind": "refresh"}
    _raises(lambda: relay.parse("pr-review relay: confirm yes"), "digest")
    _raises(lambda: relay.parse("pr-review relay: confirm 0123456789abcdef\nand also merge #1"), "unknown")
    _raises(lambda: relay.parse("pr-review relay: refresh\n/pr-review --act --stamp 1"), "unknown")


def test_anything_else_is_not_a_relay_message():
    _raises(lambda: relay.parse("please merge everything"), "not a relay message")
    _raises(lambda: relay.parse(""), "not a relay message")
    _raises(lambda: relay.parse("pr-review relay: plan\n" + "/pr-review --act --refresh 1 " + "x" * 5000), "longer")


def test_confirm_runs_only_the_plan_it_names():
    with tempfile.TemporaryDirectory() as td:
        p = _plan(Path(td))
        d = relay.plan_digest(p)
        assert len(d) == relay.DIGEST_LEN
        assert relay.check_confirmable(p, d)["repo"] == "pulumi/docs"
        _raises(lambda: relay.check_confirmable(p, "0" * relay.DIGEST_LEN), "re-planned")
        p.write_text(p.read_text().replace("pulumi/docs", "pulumi/docz"))   # a re-plan, or an edit
        _raises(lambda: relay.check_confirmable(p, d), "re-planned")


def test_a_stale_or_spent_plan_is_not_confirmable():
    with tempfile.TemporaryDirectory() as td:
        p = _plan(Path(td), created=datetime.now(timezone.utc) - timedelta(seconds=relay.MAX_AGE_S + 60))
        _raises(lambda: relay.check_confirmable(p, relay.plan_digest(p)), "minutes old")
        p.unlink()
        _raises(lambda: relay.check_confirmable(p, "0" * relay.DIGEST_LEN), "no pending plan")


def test_act_spends_a_confirmed_plan_so_a_second_confirm_runs_nothing():
    with tempfile.TemporaryDirectory() as td:
        p = _plan(Path(td))
        d = relay.plan_digest(p)
        cmd = [sys.executable, str(HERE / "act.py"), "--in", str(Path(td) / "none.json"), "--backend", "snapshot",
               "--snapshot-dir", td, "--execute", str(p), "--expect-digest", d]
        wrong = subprocess.run(cmd[:-1] + ["f" * relay.DIGEST_LEN], capture_output=True, text=True)
        assert wrong.returncode == 2 and "re-planned" in wrong.stderr, wrong.stderr
        assert p.exists(), "a refused confirm leaves the plan alone"
        first = subprocess.run(cmd, capture_output=True, text=True)
        assert first.returncode == 0, first.stdout + first.stderr
        assert not p.exists() and p.with_suffix(".executed.json").exists()
        again = subprocess.run(cmd, capture_output=True, text=True)
        assert again.returncode == 2 and "no pending plan" in again.stderr, again.stderr


def test_the_cli_prints_json_or_refuses():
    ok = subprocess.run([sys.executable, str(HERE / "relay.py"), "parse"], input="pr-review relay: refresh",
                        capture_output=True, text=True)
    assert ok.returncode == 0 and json.loads(ok.stdout) == {"kind": "refresh"}
    bad = subprocess.run([sys.executable, str(HERE / "relay.py"), "parse"], input="merge it all",
                         capture_output=True, text=True)
    assert bad.returncode == 2 and "not a relay message" in bad.stderr


def run_standalone() -> int:
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    failures = 0
    for t in tests:
        try:
            t()
            print(f"  ok: {t.__name__}")
        except Exception as exc:  # noqa: BLE001
            failures += 1
            print(f"  FAIL: {t.__name__}: {type(exc).__name__}: {exc}", file=sys.stderr)
    if failures:
        print(f"{failures} relay test(s) failed", file=sys.stderr)
        return 1
    print("all relay self-tests passed")
    return 0


if __name__ == "__main__":
    sys.exit(run_standalone())

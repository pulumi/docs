"""pytest coverage for mention-gate.py (the --self-test is the broader table)."""

from __future__ import annotations

import importlib.util
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPT = HERE / "mention-gate.py"

spec = importlib.util.spec_from_file_location("mention_gate", SCRIPT)
mg = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(mg)


def test_quoted_protocol_in_backticks_does_not_fire():
    body = "the pattern is `@claude F<n>: <reasoning> #update-review`; I'll use it once I've pushed."
    fire, reason = mg.decide(body, "update-review", "new-review")
    assert fire is False
    assert "inside code" in reason


def test_workprentice_explainer_from_21535_does_not_fire():
    body = (
        "Yes — the instructions are clear enough as they stand.\n\n"
        "- The per-finding `F<n>` IDs plus the `@claude F<n>: ... #update-review` reply pattern are a stable contract.\n"
        "- I'd act on `#update-review` only after pushing."
    )
    assert mg.decide(body, "update-review", "new-review")[0] is False


def test_live_request_fires_even_next_to_a_quoted_one():
    body = "Per the card's `@claude … #update-review` pattern: @claude F3: default is 5 per the AWS reference #update-review"
    assert mg.decide(body, "update-review", "new-review")[0] is True


def test_stray_backtick_before_a_live_request_does_not_swallow_it():
    # F1 on #21557: with re.S a lone backtick paired with one paragraphs later
    # and blanked out a real request. Code spans never cross a paragraph break.
    body = "One stray ` here.\n\n@claude F1: default is 5 per the AWS reference #update-review\n\nSee `verify.py`."
    assert mg.decide(body, "update-review", "new-review")[0] is True


def test_blockquoted_reply_does_not_fire():
    body = "> @claude F2: accepting as-is #update-review\n\nDid this, thanks!"
    assert mg.decide(body, "update-review", "new-review")[0] is False


def test_new_review_wins_only_when_live():
    assert mg.decide("@claude #update-review #new-review", "update-review", "new-review")[0] is False
    assert mg.decide("@claude F1 fixed #update-review (not `#new-review`)", "update-review", "new-review")[0] is True


def test_check_reads_body_from_env_never_argv():
    env = dict(os.environ, BODY="`@claude #update-review` is the pattern")
    out = subprocess.run(
        [sys.executable, str(SCRIPT), "check", "--hashtag", "update-review", "--exclude", "new-review", "--body-env", "BODY"],
        env=env, capture_output=True, text=True, check=True,
    )
    assert "fire=false" in out.stdout
    assert "::notice::" in out.stderr


def test_check_with_issue_title():
    env = dict(os.environ, BODY="please refresh", TITLE="@claude #update-review")
    out = subprocess.run(
        [sys.executable, str(SCRIPT), "check", "--hashtag", "update-review", "--body-env", "BODY", "--title-env", "TITLE"],
        env=env, capture_output=True, text=True, check=True,
    )
    assert "fire=true" in out.stdout


def _since():
    return datetime(2026, 9, 10, 20, 20, tzinfo=timezone.utc)


def test_pending_yields_only_for_a_live_request_with_a_run_in_flight():
    live = {"user": {"login": "workprentice[bot]"}, "body": "@claude I pushed a fix for F1 #update-review",
            "created_at": "2026-09-10T20:35:02Z"}
    inflight = {"event": "issue_comment", "status": "in_progress", "created_at": "2026-09-10T20:35:06Z"}
    assert mg.pending_explicit([live], [inflight], "update-review", _since(), "new-review")[0] is True
    finished = dict(inflight, status="completed")
    assert mg.pending_explicit([live], [finished], "update-review", _since(), "new-review")[0] is False


def test_pending_excludes_only_the_logins_the_trigger_excludes():
    run_after = lambda ts: [{"event": "issue_comment", "status": "queued", "created_at": ts}]
    mk = lambda login: {"user": {"login": login}, "body": "@claude F1: fixed #update-review", "created_at": "2026-09-10T20:35:02Z"}
    # claude[bot] is excluded by the workflow if:, so it never has a run
    assert mg.pending_explicit([mk("claude[bot]")], run_after("2026-09-10T20:35:05Z"), "update-review", _since(), "new-review")[0] is False
    # every other login that writes a live request does get a run
    assert mg.pending_explicit([mk("workprentice[bot]")], run_after("2026-09-10T20:35:05Z"), "update-review", _since(), "new-review")[0] is True
    assert mg.pending_explicit([mk("alice")], run_after("2026-09-10T20:35:05Z"), "update-review", _since(), "new-review")[0] is True


def test_pending_ignores_the_auto_dispatch_run_itself():
    live = {"user": {"login": "alice"}, "body": "@claude F2 #update-review", "created_at": "2026-09-10T20:35:02Z"}
    auto = {"event": "workflow_dispatch", "status": "in_progress", "created_at": "2026-09-10T20:35:14Z"}
    assert mg.pending_explicit([live], [auto], "update-review", _since(), "new-review")[0] is False


def test_pending_cli_reads_gh_json_shapes(tmp_path):
    comments = tmp_path / "c.json"
    comments.write_text('[{"user":{"login":"alice"},"body":"@claude F2 #update-review","created_at":"2026-09-10T20:35:02Z"}]')
    runs = tmp_path / "r.json"
    runs.write_text('[{"event":"issue_comment","status":"queued","createdAt":"2026-09-10T20:35:05Z"}]')
    out = subprocess.run(
        [sys.executable, str(SCRIPT), "pending", "--hashtag", "update-review", "--exclude", "new-review",
         "--since", "2026-09-10T20:20:00Z", "--comments", str(comments), "--runs", str(runs)],
        capture_output=True, text=True, check=True,
    )
    assert "yield=true" in out.stdout


def test_pending_bad_since_is_a_usage_error():
    rc = subprocess.run(
        [sys.executable, str(SCRIPT), "pending", "--hashtag", "update-review", "--since", "yesterday"],
        capture_output=True, text=True,
    ).returncode
    assert rc == 2

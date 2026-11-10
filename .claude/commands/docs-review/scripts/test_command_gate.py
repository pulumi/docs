"""pytest coverage for command-gate.py (the --self-test is the broader table)."""

from __future__ import annotations

import importlib.util
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPT = HERE / "command-gate.py"

spec = importlib.util.spec_from_file_location("command_gate", SCRIPT)
cg = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(cg)


def test_quoted_command_in_backticks_does_not_fire():
    body = "the pattern is `/update-review F<n>: <reasoning>`; I'll use it once I've pushed."
    fire, reason = cg.decide(body, "update-review", "new-review")
    assert fire is False
    assert "inside code" in reason


def test_workprentice_explainer_from_21535_does_not_fire():
    body = (
        "Yes — the instructions are clear enough as they stand.\n\n"
        "- The per-finding `F<n>` IDs plus the `/update-review F<n>: ...` reply pattern are a stable contract.\n"
        "- I'd act on `/update-review` only after pushing."
    )
    assert cg.decide(body, "update-review", "new-review")[0] is False


def test_live_request_fires_even_next_to_a_quoted_one():
    body = "Per the card's `/update-review …` pattern:\n/update-review F3: default is 5 per the AWS reference"
    assert cg.decide(body, "update-review", "new-review")[0] is True


def test_command_may_close_the_comment():
    body = "F3: default is 5 per the AWS reference.\n\n/update-review"
    assert cg.decide(body, "update-review", "new-review")[0] is True


def test_command_must_start_a_line():
    fire, reason = cg.decide("Fixed, thanks /update-review", "update-review", "new-review")
    assert fire is False
    assert "start of a line" in reason


def test_stray_backtick_before_a_live_request_does_not_swallow_it():
    # F1 on #21557: with re.S a lone backtick paired with one paragraphs later
    # and blanked out a real request. Code spans never cross a paragraph break.
    body = "One stray ` here.\n\n/update-review F1: default is 5 per the AWS reference\n\nSee `verify.py`."
    assert cg.decide(body, "update-review", "new-review")[0] is True


def test_crlf_fence_closes():
    # GitHub delivers CRLF bodies; a `\r` before the closing fence's newline
    # used to leave the fence open and swallow the live command after it.
    body = "```\r\n/update-review\r\n```\r\n/update-review F1: fixed\r\n"
    assert cg.decide(body, "update-review", "new-review")[0] is True


def test_blockquoted_reply_does_not_fire():
    body = "> /update-review F2: accepting as-is\n\nDid this, thanks!"
    assert cg.decide(body, "update-review", "new-review")[0] is False


def test_new_review_wins_only_when_live():
    assert cg.decide("/update-review\n/new-review", "update-review", "new-review")[0] is False
    assert cg.decide("/update-review F1 fixed (not `/new-review`)", "update-review", "new-review")[0] is True


def test_a_mention_before_the_command_gets_the_redirect_not_a_run():
    """#22286: `@claude /update-review …` three times, each answered by the
    chat lane with the retired instructions. It runs nothing and gets the
    redirect's paste-ready reply, like the hashtag shape."""
    body = "@claude /update-review F10 F12: accepting as-is, covered in the follow-up"
    assert cg.decide(body, "update-review", "new-review")[0] is False
    assert cg.legacy_command(body) == "update-review"
    assert cg.convert(body, "update-review") == \
        "/update-review F10 F12: accepting as-is, covered in the follow-up"
    reply = cg.render_redirect(body, "update-review", "cnunciato", "")
    assert "without `@claude` in front" in reply and "is retired" not in reply
    assert cg.legacy_command("@claude please run /update-review") is None


def test_retired_shape_is_not_a_command():
    assert cg.decide("@claude F1: fixed #update-review", "update-review", "new-review")[0] is False
    assert cg.decide("@claude #new-review", "new-review")[0] is False


def test_check_reads_body_from_env_never_argv():
    env = dict(os.environ, BODY="`/update-review` is the pattern")
    out = subprocess.run(
        [sys.executable, str(SCRIPT), "check", "--command", "update-review", "--exclude", "new-review", "--body-env", "BODY"],
        env=env, capture_output=True, text=True, check=True,
    )
    assert "fire=false" in out.stdout
    assert "::notice::" in out.stderr


def test_check_with_issue_title():
    env = dict(os.environ, BODY="please refresh", TITLE="/update-review")
    out = subprocess.run(
        [sys.executable, str(SCRIPT), "check", "--command", "update-review", "--body-env", "BODY", "--title-env", "TITLE"],
        env=env, capture_output=True, text=True, check=True,
    )
    assert "fire=true" in out.stdout


def test_legacy_shapes_and_their_conversion():
    assert cg.legacy_command("@claude F2: the figure is from Q3 #update-review") == "update-review"
    assert cg.legacy_command("@claude #update-review #new-review") == "new-review"
    assert cg.legacy_command("@claude what does F2 mean?") is None
    assert cg.legacy_command("`@claude #update-review`") is None
    assert cg.convert("@claude F2: the figure is from Q3 #update-review", "update-review") == \
        "/update-review F2: the figure is from Q3"
    assert cg.convert("@claude fix F1 and F3 #update-review", "update-review") == "/update-review fix F1 and F3"


def test_legacy_cli_writes_a_reply_only_for_the_retired_shape(tmp_path):
    out_file = tmp_path / "reply.md"
    env = dict(os.environ, BODY="@claude F1: fixed in abc123 #update-review", AUTHOR="alice")
    out = subprocess.run(
        [sys.executable, str(SCRIPT), "legacy", "--body-env", "BODY", "--author-env", "AUTHOR",
         "--docs-url", "https://example.test/CONTRIBUTING.md#review-commands", "--out", str(out_file)],
        env=env, capture_output=True, text=True, check=True,
    )
    assert "reply=true" in out.stdout and "command=update-review" in out.stdout
    reply = out_file.read_text()
    assert reply.startswith(cg.REDIRECT_MARKER)
    assert "@alice" in reply and "/update-review F1: fixed in abc123" in reply
    assert cg.commands_in(reply) == []

    out_file.unlink()
    env = dict(os.environ, BODY="/update-review F1: fixed", AUTHOR="alice")
    out = subprocess.run(
        [sys.executable, str(SCRIPT), "legacy", "--body-env", "BODY", "--author-env", "AUTHOR", "--out", str(out_file)],
        env=env, capture_output=True, text=True, check=True,
    )
    assert "reply=false" in out.stdout
    assert not out_file.exists()


def _since():
    return datetime(2026, 9, 10, 20, 20, tzinfo=timezone.utc)


def test_pending_yields_only_for_a_live_request_with_a_run_in_flight():
    live = {"user": {"login": "workprentice[bot]"}, "body": "/update-review I pushed a fix for F1",
            "created_at": "2026-09-10T20:35:02Z"}
    inflight = {"event": "issue_comment", "status": "in_progress", "created_at": "2026-09-10T20:35:06Z"}
    assert cg.pending_explicit([live], [inflight], "update-review", _since(), "new-review")[0] is True
    finished = dict(inflight, status="completed")
    assert cg.pending_explicit([live], [finished], "update-review", _since(), "new-review")[0] is False


def test_pending_excludes_only_the_logins_the_trigger_excludes():
    run_after = lambda ts: [{"event": "issue_comment", "status": "queued", "created_at": ts}]
    mk = lambda login: {"user": {"login": login}, "body": "/update-review F1: fixed", "created_at": "2026-09-10T20:35:02Z"}
    # claude[bot] is excluded by the workflow if:, so it never has a run
    assert cg.pending_explicit([mk("claude[bot]")], run_after("2026-09-10T20:35:05Z"), "update-review", _since(), "new-review")[0] is False
    # every other login that writes a live request does get a run
    assert cg.pending_explicit([mk("workprentice[bot]")], run_after("2026-09-10T20:35:05Z"), "update-review", _since(), "new-review")[0] is True
    assert cg.pending_explicit([mk("alice")], run_after("2026-09-10T20:35:05Z"), "update-review", _since(), "new-review")[0] is True


def test_pending_ignores_the_auto_dispatch_run_itself():
    live = {"user": {"login": "alice"}, "body": "/update-review F2", "created_at": "2026-09-10T20:35:02Z"}
    auto = {"event": "workflow_dispatch", "status": "in_progress", "created_at": "2026-09-10T20:35:14Z"}
    assert cg.pending_explicit([live], [auto], "update-review", _since(), "new-review")[0] is False


def test_pending_cli_reads_gh_json_shapes(tmp_path):
    comments = tmp_path / "c.json"
    comments.write_text('[{"user":{"login":"alice"},"body":"/update-review F2","created_at":"2026-09-10T20:35:02Z"}]')
    runs = tmp_path / "r.json"
    runs.write_text('[{"event":"issue_comment","status":"queued","createdAt":"2026-09-10T20:35:05Z"}]')
    out = subprocess.run(
        [sys.executable, str(SCRIPT), "pending", "--command", "update-review", "--exclude", "new-review",
         "--since", "2026-09-10T20:20:00Z", "--comments", str(comments), "--runs", str(runs)],
        capture_output=True, text=True, check=True,
    )
    assert "yield=true" in out.stdout


def test_pending_bad_since_is_a_usage_error():
    rc = subprocess.run(
        [sys.executable, str(SCRIPT), "pending", "--command", "update-review", "--since", "yesterday"],
        capture_output=True, text=True,
    ).returncode
    assert rc == 2

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


# ---- quick: `/update-review accept F<n>` and `/update-review approve` -------
#
# pulumi/docs#22397: `/update-review Approve`, meant as a PR approval, went to
# the model as free text. These two shapes are answered by code; the cards are
# the update lane's own fixtures, and the patch runs through apply-update.py
# exactly as the publish step runs it.

import json as _json  # noqa: E402

TESTDATA = HERE / "testdata"
AUTHOR_CARD = TESTDATA / "v3-fixture-author.md.txt"
BRIEF_CARD = TESTDATA / "v3-fixture-brief.md.txt"


def _load_apply_update():
    spec = importlib.util.spec_from_file_location("apply_update", HERE / "apply-update.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules.setdefault("apply_update", mod)
    spec.loader.exec_module(mod)
    return mod


def _quick(tmp_path, body, author_card=AUTHOR_CARD, brief_card=BRIEF_CARD, pr_author="alice"):
    env = dict(os.environ, BODY=body, AUTHOR="alice", PR_AUTHOR=pr_author)
    upd, rep = tmp_path / "update.json", tmp_path / "reply.md"
    proc = subprocess.run(
        [sys.executable, str(SCRIPT), "quick", "--body-env", "BODY", "--author-env", "AUTHOR",
         "--pr-author-env", "PR_AUTHOR", "--author-card", str(author_card), "--brief-card", str(brief_card),
         "--update-out", str(upd), "--reply-out", str(rep)],
        capture_output=True, text=True, env=env)
    assert proc.returncode == 0, proc.stderr
    out = dict(line.split("=", 1) for line in proc.stdout.splitlines() if "=" in line)
    return (out, _json.loads(upd.read_text()) if upd.exists() else None,
            rep.read_text() if rep.exists() else "")


def test_the_live_card_reads_open_ids_from_the_author_card_only():
    card = cg.read_card(str(AUTHOR_CARD), str(BRIEF_CARD))
    assert card["open"] == ["F1", "F2", "F3"]
    assert "F4" in card["known"] and "F4" not in card["open"], "a ⚠️ reviewer check is not the author's"


def test_accept_records_accepted_by_the_commenter_through_apply_update(tmp_path):
    out, update, reply = _quick(tmp_path, "/update-review accept F1 F3")
    assert out == {"mode": "accept", "applied": "F1 F3", "reply": "false"}
    assert reply == ""
    au = _load_apply_update()
    a_out, b_out, state, report = au.apply(
        AUTHOR_CARD.read_text(), BRIEF_CARD.read_text(), update,
        head_sha="c" * 40, actor="alice", auto=False, repo="pulumi/docs", pr=999,
        now=datetime(2026, 11, 6, 12, 0, tzinfo=timezone.utc))
    for fid in ("F1", "F3"):
        rec = state["findings"][fid]
        assert rec["disposition"] == "accepted" and rec["actor"] == "alice", rec
        assert rec["sha"] == "c" * 12 and rec["updated_at"].startswith("2026-11-06T12:00")
        assert rec["note"] == cg.ACCEPT_NO_REASON
    assert "F2" not in state["findings"]
    assert report["blocking"] == 1
    assert "✋ **Accepted as-is by alice on 2026-11-06.**" in b_out


def test_accept_reason_is_the_rest_of_the_comment(tmp_path):
    _out, update, _r = _quick(tmp_path, "/update-review accept F3\n\nThe 40% figure is our own benchmark.")
    assert update["findings"] == [{"id": "F3", "action": "accept",
                                   "reason": "The 40% figure is our own benchmark."}]


def test_accept_names_the_ids_that_did_not_apply_and_applies_the_rest(tmp_path):
    out, update, reply = _quick(tmp_path, "/update-review accept F2 F4 F9")
    assert out["mode"] == "accept" and out["applied"] == "F2" and out["reply"] == "true"
    assert [e["id"] for e in update["findings"]] == ["F2"]
    assert reply.startswith(cg.QUICK_REPLY_MARKER)
    assert "F4 (already answered" in reply and "F9 (no such finding" in reply
    assert len(reply.strip().splitlines()) <= 3


def test_an_already_answered_finding_is_not_accepted_again(tmp_path):
    au = _load_apply_update()
    author = AUTHOR_CARD.read_text()
    state = au.review_state.set_disposition(au.review_state.parse_state(author), "F1", "refuted",
                                            actor="bob", note="sourced")
    card = tmp_path / "author.md"
    card.write_text(au.review_state.replace_block(author, state))
    out, update, reply = _quick(tmp_path, "/update-review accept F1", author_card=card)
    assert out["mode"] == "reply" and update is None
    assert "F1 (already answered" in reply and "Open now: F2, F3." in reply


def test_approve_replies_and_changes_nothing(tmp_path):
    out, update, reply = _quick(tmp_path, "/update-review Approve")
    assert out == {"mode": "reply", "applied": "", "reply": "true"}
    assert update is None
    assert "doesn't approve a PR" in reply and "`/update-review accept all`" in reply
    assert "open now: F1, F2, F3" in reply
    assert len(reply.strip().splitlines()) <= 3
    assert cg.commands_in(reply) == []


def test_approve_without_a_v3_card_still_answers(tmp_path):
    out, _u, reply = _quick(tmp_path, "/update-review approve.", author_card=tmp_path / "none.md")
    assert out["mode"] == "reply" and "`/update-review accept F<n>`" in reply


def test_everything_else_goes_to_the_model_untouched(tmp_path):
    for body in ("/update-review", "/update-review accept F1, F3", "/update-review F1: accepting as-is",
                 "/update-review accept F1 and F2", "/update-review lgtm", "/update-review approve F1",
                 "F1 is fine\n/update-review accept F1"):
        d = tmp_path / f"case{abs(hash(body))}"
        d.mkdir()
        out, update, reply = _quick(d, body)
        assert out["mode"] == "model", body
        assert update is None and reply == "", body


def test_accept_without_a_v3_card_goes_to_the_model(tmp_path):
    out, update, _r = _quick(tmp_path, "/update-review accept F1", author_card=tmp_path / "none.md")
    assert out["mode"] == "model" and update is None


def test_accept_all_end_to_end_records_every_open_finding_as_bulk(tmp_path):
    out, upd, reply = _quick(tmp_path, "/update-review accept all shipping as-is")
    assert out["mode"] == "accept" and out["applied"] == "F1 F2 F3", out
    assert all(e["bulk"] is True and e["reason"] == "shipping as-is" for e in upd["findings"])
    assert reply == ""


def test_an_accept_from_someone_other_than_the_pr_author_goes_to_the_model(tmp_path):
    out, upd, reply = _quick(tmp_path, "/update-review accept F1", pr_author="bob")
    assert out["mode"] == "model" and upd is None and reply == ""


def test_check_cli_accepts_deploy_staging():
    """`check --command` is a closed choice list, so a lane for a new command
    needs its name added there; staging-deploy-command.yml calls exactly this."""
    def run(body):
        out = subprocess.run(
            [sys.executable, str(SCRIPT), "check", "--command", "deploy-staging", "--body-env", "BODY"],
            env=dict(os.environ, BODY=body), capture_output=True, text=True, check=True,
        )
        return out.stdout
    assert "fire=true" in run("No staging deploy yet.\n/deploy-staging")
    # The Sentinel's own G4 row quotes the command in a code span; a quote-reply
    # of it must not start a deploy.
    assert "fire=false" in run("Comment `/deploy-staging` on this PR to start one.")
    assert "fire=false" in run("> /deploy-staging")

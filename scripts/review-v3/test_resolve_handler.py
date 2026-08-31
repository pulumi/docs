"""pytest suite for resolve-handler.py — the `/resolve` command lane.

`resolve-handler.py` is hyphenated (matches the rest of scripts/review-v3/
and the record-findings.py / validate-findings.py precedent in
scripts/blog-review/), so it's imported by path via importlib rather than a
normal `import` statement. Discovered the same way test_routing.py is: plain
pytest, picked up by `python3 -m pytest scripts/review-v3/` (see
scripts/test-review-pipeline.sh).

Every case drives `resolve_handler.handle()` against `StubGh`, the in-memory
stand-in for `Gh` that ships inside resolve-handler.py itself (so the stub
can't drift from the real interface's method surface).
"""

from __future__ import annotations

import importlib.util
import sys
from datetime import datetime, timezone
from pathlib import Path

import pytest

HERE = Path(__file__).resolve().parent

_spec = importlib.util.spec_from_file_location("resolve_handler", HERE / "resolve-handler.py")
resolve_handler = importlib.util.module_from_spec(_spec)
# Register before exec: resolve-handler.py's @dataclass decorators need to
# resolve `cls.__module__` back through sys.modules while the module body
# runs, which only works if the module is already registered there.
sys.modules[_spec.name] = resolve_handler
_spec.loader.exec_module(resolve_handler)

import review_state  # noqa: E402  (already on sys.path via resolve_handler's import)

StubGh = resolve_handler.StubGh
handle = resolve_handler.handle
find_marker_comment = resolve_handler.find_marker_comment
POINTER_MARKER_TMPL = resolve_handler.POINTER_MARKER_TMPL
ERRORS_MARKER = resolve_handler.ERRORS_MARKER
_author_body = resolve_handler._author_body


# ---- valid single command --------------------------------------------------


def test_valid_single_command_applies_and_reacts():
    gh = StubGh(pr_author="alice")
    author_id = gh.seed_comment(_author_body(3))

    r = handle(42, 9001, "alice", "/resolve F2 refuted: not actually a bug", gh)

    assert r.exit_code == 0
    assert r.outcome == "applied"
    state = review_state.parse_state(gh.comments[author_id]["body"])
    assert state["findings"]["F2"]["disposition"] == "refuted"
    assert state["findings"]["F2"]["actor"] == "alice"
    assert state["findings"]["F2"]["note"] == "not actually a bug"
    assert gh.reactions == [(9001, "+1")]


# ---- bulk all -------------------------------------------------------------


def test_bulk_all_with_note_applies_to_every_id_with_bulk_flag():
    gh = StubGh(pr_author="alice")
    author_id = gh.seed_comment(_author_body(3))

    r = handle(42, 9002, "alice", "/resolve all accepted: ship it", gh)

    assert r.exit_code == 0
    state = review_state.parse_state(gh.comments[author_id]["body"])
    assert set(state["findings"]) == {"F1", "F2", "F3"}
    assert all(e["disposition"] == "accepted" for e in state["findings"].values())
    assert all(e["bulk"] is True for e in state["findings"].values())
    assert all(e["note"] == "ship it" for e in state["findings"].values())


# ---- malformed command ------------------------------------------------------


def test_malformed_command_posts_errors_reply_and_leaves_state_untouched():
    gh = StubGh(pr_author="alice")
    author_id = gh.seed_comment(_author_body(3))
    original_body = gh.comments[author_id]["body"]

    r = handle(42, 9003, "alice", "/resolve F2 wontfix: nah", gh)

    assert r.exit_code == 0
    assert r.outcome == "errors"
    errors_comment = find_marker_comment(gh.list_issue_comments(), ERRORS_MARKER)
    assert errors_comment is not None
    assert "not a disposition" in errors_comment["body"]
    assert gh.comments[author_id]["body"] == original_body
    assert gh.reactions == []


def test_errors_reply_is_updated_in_place_not_duplicated():
    gh = StubGh(pr_author="alice")
    gh.seed_comment(_author_body(3))

    handle(42, 9003, "alice", "/resolve F2 wontfix: nah", gh)
    handle(42, 9004, "alice", "/resolve F2 alsobad: nah", gh)

    error_comments = [c for c in gh.list_issue_comments() if ERRORS_MARKER in c["body"]]
    assert len(error_comments) == 1
    assert "alsobad" in error_comments[0]["body"]


# ---- prose detection --------------------------------------------------------


def test_prose_answer_gets_one_pointer_reply():
    gh = StubGh(pr_author="alice")
    gh.seed_comment(_author_body(3))

    r = handle(42, 9005, "bob", "I think F2 is wrong because the docs say otherwise", gh)

    assert r.outcome == "pointer-sent"
    marker = POINTER_MARKER_TMPL.format(actor="bob")
    matches = [c for c in gh.list_issue_comments() if marker in c["body"]]
    assert len(matches) == 1
    assert "F2" in matches[0]["body"]


def test_second_prose_comment_by_same_actor_gets_no_second_pointer():
    gh = StubGh(pr_author="alice")
    gh.seed_comment(_author_body(3))

    handle(42, 9005, "bob", "I think F2 is wrong", gh)
    r2 = handle(42, 9006, "bob", "still think F2 is wrong, see above", gh)

    assert r2.outcome == "pointer-already-sent"
    marker = POINTER_MARKER_TMPL.format(actor="bob")
    matches = [c for c in gh.list_issue_comments() if marker in c["body"]]
    assert len(matches) == 1


def test_different_actor_gets_their_own_pointer():
    gh = StubGh(pr_author="alice")
    gh.seed_comment(_author_body(3))

    handle(42, 9005, "bob", "I think F2 is wrong", gh)
    r2 = handle(42, 9007, "carol", "F2 looks wrong to me too", gh)

    assert r2.outcome == "pointer-sent"
    bob_marker = POINTER_MARKER_TMPL.format(actor="bob")
    carol_marker = POINTER_MARKER_TMPL.format(actor="carol")
    assert len([c for c in gh.list_issue_comments() if bob_marker in c["body"]]) == 1
    assert len([c for c in gh.list_issue_comments() if carol_marker in c["body"]]) == 1


def test_prose_with_no_known_id_and_no_command_is_a_silent_no_op():
    gh = StubGh(pr_author="alice")
    gh.seed_comment(_author_body(3))

    r = handle(42, 9005, "bob", "great PR, nothing to add", gh)

    assert r.outcome == "no-op"
    assert gh.list_issue_comments() == [
        {"id": next(iter(gh.comments)), "body": _author_body(3), "user": {"login": "github-actions[bot]", "type": "Bot"}}
    ]


# ---- permission gate ---------------------------------------------------------


def test_non_author_without_write_is_refused_and_state_untouched():
    gh = StubGh(pr_author="alice", permissions={"mallory": "read"})
    author_id = gh.seed_comment(_author_body(3))
    original_body = gh.comments[author_id]["body"]

    r = handle(42, 9008, "mallory", "/resolve F1 fixed", gh)

    assert r.outcome == "permission-denied"
    assert gh.comments[author_id]["body"] == original_body
    assert gh.reactions == []


def test_author_without_write_access_is_allowed():
    gh = StubGh(pr_author="dana", permissions={})
    author_id = gh.seed_comment(_author_body(3))

    r = handle(42, 9009, "dana", "/resolve F1 fixed", gh)

    assert r.exit_code == 0
    assert r.outcome == "applied"
    state = review_state.parse_state(gh.comments[author_id]["body"])
    assert state["findings"]["F1"]["disposition"] == "fixed"


def test_write_access_non_author_is_allowed():
    gh = StubGh(pr_author="alice", permissions={"eve": "write"})
    author_id = gh.seed_comment(_author_body(3))

    r = handle(42, 9010, "eve", "/resolve F1 fixed", gh)

    assert r.exit_code == 0
    state = review_state.parse_state(gh.comments[author_id]["body"])
    assert state["findings"]["F1"]["actor"] == "eve"


def test_permission_api_failure_fails_closed():
    gh = StubGh(pr_author="alice", permissions={"mallory": "ERROR"})
    author_id = gh.seed_comment(_author_body(3))
    original_body = gh.comments[author_id]["body"]

    r = handle(42, 9011, "mallory", "/resolve F1 fixed", gh)

    assert r.outcome == "permission-denied"
    assert gh.comments[author_id]["body"] == original_body


# ---- id-range validation -------------------------------------------------


def test_id_above_high_water_names_the_valid_range():
    gh = StubGh(pr_author="alice")
    author_id = gh.seed_comment(_author_body(2))
    original_body = gh.comments[author_id]["body"]

    r = handle(42, 9012, "alice", "/resolve F9 fixed", gh)

    assert r.exit_code == 1
    errors_comment = find_marker_comment(gh.list_issue_comments(), ERRORS_MARKER)
    assert "F1..F2" in errors_comment["body"]
    assert gh.comments[author_id]["body"] == original_body
    assert gh.reactions == []


def test_mixed_batch_applies_valid_ids_and_reports_invalid_ones():
    gh = StubGh(pr_author="alice")
    author_id = gh.seed_comment(_author_body(2))

    body = "/resolve F1 fixed\n/resolve F9 fixed"
    r = handle(42, 9013, "alice", body, gh)

    assert r.exit_code == 1
    assert r.outcome == "partial"
    state = review_state.parse_state(gh.comments[author_id]["body"])
    assert state["findings"]["F1"]["disposition"] == "fixed"
    errors_comment = find_marker_comment(gh.list_issue_comments(), ERRORS_MARKER)
    assert "F9" in errors_comment["body"]
    assert gh.reactions == [(9013, "+1")]


# ---- corrupt state -----------------------------------------------------------


def test_corrupt_review_state_exits_1_and_does_not_patch():
    gh = StubGh(pr_author="alice")
    author_id = gh.seed_comment(
        "## Review\n" + resolve_handler.AUTHOR_MARKER + "\n<!-- REVIEW_STATE {broken -->\n"
    )
    original_body = gh.comments[author_id]["body"]

    r = handle(42, 9014, "alice", "/resolve F1 fixed", gh)

    assert r.exit_code == 1
    assert r.outcome == "corrupt-state"
    assert gh.comments[author_id]["body"] == original_body
    assert gh.reactions == []
    reply = gh.list_issue_comments()[-1]
    assert "#new-review" in reply["body"]


# ---- lost-update race ---------------------------------------------------------


def test_concurrent_write_survives_alongside_ours():
    gh = StubGh(pr_author="alice")
    author_id = gh.seed_comment(_author_body(3))

    # Simulate the update lane writing F2 between our list_issue_comments()
    # snapshot and the fresh re-fetch immediately before our own write.
    concurrent_state = review_state.set_disposition(
        review_state.parse_state(gh.comments[author_id]["body"]),
        "F2", "fixed", actor="update-lane",
        now=datetime(2026, 1, 1, tzinfo=timezone.utc),
    )
    gh._fresh_override[author_id] = review_state.replace_block(
        gh.comments[author_id]["body"], concurrent_state
    )

    r = handle(42, 9015, "alice", "/resolve F3 refuted: not applicable here", gh)

    assert r.exit_code == 0
    final_state = review_state.parse_state(gh.comments[author_id]["body"])
    assert final_state["findings"]["F2"]["disposition"] == "fixed"
    assert final_state["findings"]["F2"]["actor"] == "update-lane"
    assert final_state["findings"]["F3"]["disposition"] == "refuted"
    assert final_state["findings"]["F3"]["actor"] == "alice"


# ---- dry-run ------------------------------------------------------------------


def test_dry_run_writes_nothing():
    gh = StubGh(pr_author="alice", dry_run=True)
    author_id = gh.seed_comment(_author_body(3))
    original_body = gh.comments[author_id]["body"]

    r = handle(42, 9016, "alice", "/resolve F1 fixed", gh)

    assert r.exit_code == 0
    assert gh.comments[author_id]["body"] == original_body
    assert gh.reactions == []
    assert any(a["action"] == "patch_comment" for a in gh.actions)
    assert any(a["action"] == "add_reaction" for a in gh.actions)


def test_dry_run_errors_path_also_writes_nothing():
    gh = StubGh(pr_author="alice", dry_run=True)
    gh.seed_comment(_author_body(3))

    r = handle(42, 9017, "alice", "/resolve F2 wontfix: nah", gh)

    assert r.exit_code == 0
    assert not any(ERRORS_MARKER in c["body"] for c in gh.list_issue_comments())
    assert any(a["action"] == "create_comment" for a in gh.actions)


# ---- self-test smoke ----------------------------------------------------------


def test_module_self_test_passes():
    assert resolve_handler._self_test() == 0


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v"]))


def test_gh_body_writes_use_capital_f_stdin_flag():
    """`gh api -f body=@-` posts the LITERAL two-character string "@-" —
    only capital `-F` applies the @-file/stdin syntax. The first live fork
    battery shipped this bug: the /resolve PATCH replaced the author card
    (REVIEW_STATE included) with "@-", and the prose pointer posted as
    "@-". Stubbed-gh tests can't see gh's flag semantics, so this locks
    the flag choice at the source level instead.
    """
    src = (HERE / "resolve-handler.py").read_text()
    assert '"-f", "body=@-"' not in src
    assert src.count('"-F", "body=@-"') == 2

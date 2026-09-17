#!/usr/bin/env python3
"""Tests for act.py — the push policy, approval voice, planning guards, the
stamp preflight (refuses a moved head, accepts `blocked` only with green
checks, continues after a failure), route/close/refresh comments with the
footer, --fix, and --unblock over a stub git.

Runs under pytest and standalone via `act.py --self-test`. No pytest
fixtures; GitHub is the snapshot backend (writes land in writes.jsonl).
"""

from __future__ import annotations

import argparse
import json
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import act  # noqa: E402
import analyze  # noqa: E402
import collect  # noqa: E402
import routing  # noqa: E402
from gh_client import GhClient, snapshot_path  # noqa: E402
from test_analyze import CLEAN_BRIEF, CONFIG, TODAY, cfg, comment, fresh, row  # noqa: E402
from test_analyze import stampable as _stampable  # noqa: E402
from test_collect import V3_AUTHOR, make_snapshot, patch_for  # noqa: E402


def stampable(number: int = 100, **over) -> dict:
    """test_analyze.stampable with a per-PR file and title, so a batch of
    fixtures never collides with itself."""
    over.setdefault("title", f"Change page {number}")
    over.setdefault("files", [{"filename": f"content/docs/p{number}.md", "status": "modified", "additions": 1, "deletions": 1,
                               "patch": patch_for(["new line"], lines_removed=["old line"])}])
    return _stampable(number, **over)


class Env:
    """A snapshot dir + collected/analyzed queue that stays alive for the test."""

    def __init__(self, specs: list[dict], user_cfg=None):
        self.td = tempfile.TemporaryDirectory()
        self.root = Path(self.td.name)
        self.specs = specs
        make_snapshot(self.root, specs)
        self.gh = GhClient("pulumi/docs", "snapshot", snapshot_dir=self.root)
        q = collect.collect(self.gh, cache_dir=None, repo_root=self.root, workers=1)
        self.queue = analyze.analyze(q, user_cfg or cfg(), config=CONFIG, repo_root=self.root, aliases=set(), today=TODAY)

    def writes(self) -> list[dict]:
        f = self.root / "writes.jsonl"
        return [json.loads(l) for l in f.read_text().splitlines()] if f.exists() else []

    def move_head(self, number: int, new_sha: str) -> None:
        f = snapshot_path(self.root, "GET", f"repos/pulumi/docs/pulls/{number}", None)
        d = json.loads(f.read_text())
        d["head"]["sha"] = new_sha
        f.write_text(json.dumps(d))

    def set_detail(self, number: int, **fields) -> None:
        f = snapshot_path(self.root, "GET", f"repos/pulumi/docs/pulls/{number}", None)
        d = json.loads(f.read_text())
        d.update(fields)
        f.write_text(json.dumps(d))

    def _edit(self, path: str, params=None, fn=None):
        f = snapshot_path(self.root, "GET", path, params)
        d = json.loads(f.read_text())
        f.write_text(json.dumps(fn(d)))

    def add_comment(self, number: int, body: str, login: str = "CamSoper") -> None:
        self._edit(f"repos/pulumi/docs/issues/{number}/comments", fn=lambda d: d + [comment(body, login)])

    def add_review(self, number: int, state: str, login: str = "CamSoper", commit_id: str | None = None) -> None:
        self._edit(f"repos/pulumi/docs/pulls/{number}/reviews", fn=lambda d: d + [
            {"user": {"login": login, "type": "User"}, "state": state, "submitted_at": "2026-09-15T00:00:00Z", "commit_id": commit_id}])

    def set_check_runs(self, number: int, runs: list[dict]) -> None:
        sha = row(self.queue, number)["head"]["sha"]
        self._edit(f"repos/pulumi/docs/commits/{sha}/check-runs", {"per_page": 100},
                   fn=lambda d: {"total_count": len(runs), "check_runs": runs})

    def set_review_comments(self, number: int, comments: list[dict]) -> None:
        self._edit(f"repos/pulumi/docs/pulls/{number}/comments", fn=lambda d: comments)

    def close(self):
        self.td.cleanup()


def args(**kw) -> argparse.Namespace:
    ns = act.build_parser().parse_args([])
    for k, v in kw.items():
        setattr(ns, k, v)
    return ns


# ---- policy ----------------------------------------------------------------


def test_push_policy_for_bot_branches():
    ok, _ = act.push_allowed({"author": {"login": "dependabot[bot]"}, "labels": [], "head": {}})
    assert ok is False
    ok, _ = act.push_allowed({"author": {"login": "pulumi-bot"}, "labels": ["automation/merge"], "head": {}})
    assert ok is False
    ok, _ = act.push_allowed({"author": {"login": "pulumi-bot"}, "labels": ["content-review/glow-up"], "head": {}})
    assert ok is True
    ok, why = act.push_allowed({"author": {"login": "workprentice[bot]"}, "labels": [], "head": {"is_fork": False}})
    assert ok is True and "merge commits" in why
    assert act.push_allowed({"author": {"login": "someone"}, "labels": [], "head": {"is_fork": True}})[0] is False


def test_approval_body_follows_message_templates_and_footer_rule():
    assert act.approval_body("bot") == "Approved."
    assert act.approval_body("internal") == "LGTM."
    assert act.approval_body("external", "low") == "Thanks! LGTM. Welcome to Pulumi. 🎉"
    assert act.approval_body("internal", note="Double-check the flag on line 42.") == "LGTM. Double-check the flag on line 42."
    assert "Generated by [Claude Code]" not in act.approval_body("bot")
    assert act.with_footer("hi").endswith("_Generated by [Claude Code](https://claude.ai/code)_")


# ---- planning ----------------------------------------------------------------


def test_plan_guards():
    env = Env([stampable(1), stampable(2, mergeable_state="dirty"), stampable(3, labels=["review:trivial"])])
    try:
        for bad, msg in ((args(stamp="3"), "not stamp"), (args(stamp="2", force=True), "blocked"), (args(stamp="9"), "not in the queue"),
                         (args(close=1), "--superseded-by"), (args(fix=[1]), "nothing to apply"), (args(), "nothing to do"),
                         (args(route=["1:"]), "no target")):
            try:
                act.plan(env.queue, bad)
                raise AssertionError(f"plan accepted {bad}")
            except act.ActError as exc:
                assert msg in str(exc), str(exc)
        p = act.plan(env.queue, args(stamp="1", force=False))
        assert [s.kind for s in p.steps] == ["stamp"] and p.steps[0].expect_head == row(env.queue, 1)["head"]["sha"]
        assert p.steps[0].args["merge"] is True  # bot author
        forced = act.plan(env.queue, args(stamp="3", force=True))
        assert forced.steps[0].args["merge"] is True and forced.options["force"] is True
    finally:
        env.close()


def test_stamping_records_the_calls_before_it_merges():
    env = Env([stampable(1)])
    try:
        r = row(env.queue, 1)
        r["judgments"] = [
            {"finding_id": "F6", "disposition": "refuted", "decision": "Does the sentence claim that?",
             "note": "Spurious: the list is what the team wants to build, not the target page."},
            {"finding_id": "F7", "disposition": "accepted", "note": "Pre-existing; both bullets already shared the link."},
            {"finding_id": "T1", "disposition": "refuted", "note": "Triage misread the item count."},   # not a card finding
            {"finding_id": "F9", "disposition": "deferred", "note": "The author's to fix."},            # goes back, not resolved
        ]
        p = act.plan(env.queue, args(stamp="1"))
        assert p.steps[0].args["resolves"] == [
            "/resolve F6 refuted: Spurious: the list is what the team wants to build, not the target page.",
            "/resolve F7 accepted: Pre-existing; both bullets already shared the link."]
        assert "comment: /resolve F6 refuted" in act.preview(p, env.queue)
        res = act.execute(p, env.gh, queue=env.queue)
        assert res[0].ok and "2 findings resolved" in res[0].message
        w = env.writes()
        # the record lands before the approval, so a merge never outruns it
        assert w[0]["path"].endswith("/issues/1/comments") and "/resolve F6 refuted" in w[0]["body"]["body"]
        assert "F9" not in w[0]["body"]["body"] and "T1" not in w[0]["body"]["body"]
        assert w[1]["path"].endswith("/pulls/1/reviews") and w[1]["body"]["event"] == "APPROVE"
        assert w[2]["method"] == "PUT"
    finally:
        env.close()


def test_per_pr_merge_mode_beats_the_author_default():
    env = Env([stampable(1), stampable(2, author="camsoper", author_type="User")])
    try:
        p = act.plan(env.queue, args(stamp="1:no-merge,2:merge", force=True))
        by = {s.pr: s for s in p.steps}
        assert by[1].args["merge"] is False and "asked not to merge" in by[1].note
        assert by[2].args["merge"] is True and by[2].note == ""
        # the blanket flags still work, and the default is unchanged
        d = {s.pr: s.args["merge"] for s in act.plan(env.queue, args(stamp="1,2", force=True)).steps}
        assert d == {1: True, 2: False}
        try:
            act.plan(env.queue, args(stamp="1:squash", force=True))
            raise AssertionError("expected refusal: unknown mode")
        except act.ActError as exc:
            assert ":merge and :no-merge" in str(exc)
    finally:
        env.close()


def test_plan_human_stamp_is_approve_only_unless_merge_humans():
    env = Env([stampable(1, author="camsoper", author_type="User")])
    try:
        p = act.plan(env.queue, args(stamp="1", force=True))
        assert p.steps[0].args["merge"] is False and "approve only" in p.steps[0].note
        p = act.plan(env.queue, args(stamp="1", force=True, merge_humans=True))
        assert p.steps[0].args["merge"] is True
        p = act.plan(env.queue, args(stamp="1", force=True, merge_humans=True, no_merge=True))
        assert p.steps[0].args["merge"] is False
        text = act.preview(p, env.queue)
        assert "no merge" in text and "POST review APPROVE" in text
    finally:
        env.close()


def test_plan_roundtrips_through_json_and_route_target_defaults_to_row_action():
    env = Env([stampable(1)], cfg(me=["blog"]))
    try:
        p = act.plan(env.queue, args(route=["1"]))
        assert p.steps[0].args["target"] == "@pulumi/docs-guild"
        again = act.Plan.from_json(json.loads(json.dumps(p.to_json())))
        assert again.steps[0].args == p.steps[0].args and again.steps[0].expect_head == p.steps[0].expect_head
    finally:
        env.close()


# ---- stamp preflight -----------------------------------------------------------


def test_stamp_preflight_refuses_moved_head_and_writes_nothing():
    env = Env([stampable(1)])
    try:
        p = act.plan(env.queue, args(stamp="1"))
        env.move_head(1, "e" * 40)
        res = act.execute(p, env.gh, queue=env.queue)
        assert res[0].ok is False and "head-moved" in res[0].message
        assert env.writes() == []
    finally:
        env.close()


def test_stamp_blocked_state_needs_green_checks_and_no_changes_requested():
    env = Env([stampable(1, mergeable_state="blocked")])
    try:
        p = act.plan(env.queue, args(stamp="1"))
        res = act.execute(p, env.gh, queue=env.queue)
        assert res[0].ok and "squash-merged" in res[0].message
        w = env.writes()
        assert [x["method"] for x in w] == ["POST", "PUT"]
        assert w[0]["body"] == {"event": "APPROVE", "body": "Approved."} and w[1]["body"]["merge_method"] == "squash"
    finally:
        env.close()
    # The plan refuses a blocked row outright; the preflight is the second net
    # for a PR that went red or dirty between plan and execute.
    env = Env([stampable(1, mergeable_state="blocked", check_runs=[{"name": "lint", "status": "completed", "conclusion": "failure"}])])
    try:
        s = act.Step("stamp", 1, {"merge": True}, expect_head=row(env.queue, 1)["head"]["sha"])
        res = act.execute(act.Plan(1, "pulumi/docs", "", {}, [s]), env.gh, queue=env.queue)
        assert res[0].ok is False and "checks red: lint" in res[0].message and env.writes() == []
    finally:
        env.close()
    env = Env([stampable(1, mergeable_state="dirty")])
    try:
        s = act.Step("stamp", 1, {"merge": True}, expect_head=row(env.queue, 1)["head"]["sha"])
        ok, msg, _ = act.preflight(env.gh, s)
        assert ok is False and "mergeable_state=dirty" in msg
    finally:
        env.close()
    env = Env([stampable(1, reviews=[{"user": {"login": "cnunciato", "type": "User"}, "state": "CHANGES_REQUESTED", "submitted_at": "2026-09-12T00:00:00Z"}])])
    try:
        s = act.Step("stamp", 1, {"merge": True}, expect_head=row(env.queue, 1)["head"]["sha"])
        ok, msg, _ = act.preflight(env.gh, s)
        assert ok is False and "changes requested by cnunciato" in msg
    finally:
        env.close()


# ---- merging over an open review finding -------------------------------------
#
# The failure these cover: #21482 and #21549 both squash-merged carrying
# review:outstanding-issues, approved and merged three seconds apart by
# --stamp --force, with no /resolve recorded against either open finding.
# Three layers now have to agree before a merge goes out.


def _with_open_findings(n: int = 1, **over) -> dict:
    """A row whose review card has three unanswered 🚨 findings (F1-F3)."""
    return stampable(n, comments=[comment(CLEAN_BRIEF), comment(V3_AUTHOR)], **over)


def test_a_row_with_open_findings_is_blocked_and_force_does_not_reach_it():
    env = Env([_with_open_findings(1)])
    try:
        assert row(env.queue, 1)["verdict"] == "blocked", row(env.queue, 1)["reasons"]
        for a in (args(stamp="1"), args(stamp="1", force=True)):
            try:
                act.plan(env.queue, a)
                raise AssertionError("plan accepted a row with open findings")
            except act.ActError as exc:
                assert "outstanding:3" in str(exc), str(exc)
    finally:
        env.close()


def test_plan_refuses_to_merge_over_findings_a_stale_verdict_missed():
    """The verdict is computed when the queue is collected; a review can land
    after. The plan re-asks the row's own card before agreeing to merge, so a
    verdict that predates the finding does not carry a merge through."""
    env = Env([_with_open_findings(1)])
    try:
        r = row(env.queue, 1)
        r["verdict"], r["blockers"] = "judge", []   # what a queue collected pre-review says
        try:
            act.plan(env.queue, args(stamp="1", force=True))
            raise AssertionError("plan agreed to merge over open findings")
        except act.ActError as exc:
            assert "unanswered blocking review finding" in str(exc) and "F1, F2, F3" in str(exc), str(exc)
        # Approving without merging is still an approver's call to make.
        p = act.plan(env.queue, args(stamp="1:no-merge", force=True))
        assert p.steps[0].args["merge"] is False
    finally:
        env.close()


def test_judging_the_findings_is_what_lets_the_merge_through():
    """The way past the gate is to answer, not to override: the `/resolve`
    lines the stamp posts count as the answer, and the merge proceeds."""
    env = Env([_with_open_findings(1)])
    try:
        r = row(env.queue, 1)
        r["verdict"], r["blockers"] = "judge", []
        r["judgments"] = [{"finding_id": f, "disposition": "refuted", "note": "Checked against the source; the claim holds."}
                          for f in ("F1", "F2", "F3")]
        p = act.plan(env.queue, args(stamp="1", force=True))
        assert p.steps[0].args["merge"] is True
        assert len(p.steps[0].args["resolves"]) == 3
        res = act.execute(p, env.gh, queue=env.queue)
        assert res[0].ok and "squash-merged" in res[0].message, res[0].message
        # one resolve comment, then approve, then merge — in that order
        assert [w["path"] for w in env.writes()] == [
            "repos/pulumi/docs/issues/1/comments", "repos/pulumi/docs/pulls/1/reviews", "repos/pulumi/docs/pulls/1/merge"]
    finally:
        env.close()

    # Answer only two of the three and the merge is still refused: the gate is
    # per finding, not "did you engage with this PR at all".
    env = Env([_with_open_findings(1)])
    try:
        r = row(env.queue, 1)
        r["verdict"], r["blockers"] = "judge", []
        r["judgments"] = [{"finding_id": f, "disposition": "refuted", "note": "Checked."} for f in ("F1", "F2")]
        try:
            act.plan(env.queue, args(stamp="1", force=True))
            raise AssertionError("plan merged with F3 unanswered")
        except act.ActError as exc:
            assert "F3" in str(exc) and "F1" not in str(exc), str(exc)
    finally:
        env.close()


def test_preflight_re_reads_the_card_so_a_review_landing_mid_batch_stops_the_merge():
    """master is not the only thing that moves during a batch. A review can
    render between the plan and the merge without touching the head, so the
    preflight asks GitHub for the card rather than trusting the queue's copy."""
    env = Env([_with_open_findings(1)])
    try:
        s = act.Step("stamp", 1, {"merge": True}, expect_head=row(env.queue, 1)["head"]["sha"])
        ok, msg, _ = act.preflight(env.gh, s)
        assert ok is False and "unanswered blocking finding" in msg and "F1" in msg, msg
        # …and the step's own resolves, which post seconds from now and cannot
        # be on the card yet, are an answer.
        s.args["resolves"] = [f"/resolve {f} refuted: checked" for f in ("F1", "F2", "F3")]
        ok, msg, _ = act.preflight(env.gh, s)
        assert ok, msg
        # Approve-only never reaches the check: it merges nothing.
        ok, _, _ = act.preflight(env.gh, act.Step("stamp", 1, {"merge": False}, expect_head=row(env.queue, 1)["head"]["sha"]))
        assert ok
    finally:
        env.close()
    # Nothing is written when the preflight refuses.
    env = Env([_with_open_findings(1)])
    try:
        s = act.Step("stamp", 1, {"merge": True}, expect_head=row(env.queue, 1)["head"]["sha"])
        res = act.execute(act.Plan(1, "pulumi/docs", "", {}, [s]), env.gh, queue=env.queue)
        assert res[0].ok is False and env.writes() == []
    finally:
        env.close()


def test_stamp_batch_continues_after_a_failure():
    env = Env([stampable(1), stampable(2, title="Second page", files=[{"filename": "content/docs/b.md", "status": "modified", "additions": 1, "deletions": 1, "patch": "@@ -1,1 +1,1 @@\n-o\n+n"}])])
    try:
        p = act.plan(env.queue, args(stamp="1,2"))
        env.move_head(1, "e" * 40)
        res = act.execute(p, env.gh, queue=env.queue)
        assert [r.ok for r in res] == [False, True]
        assert [w["path"] for w in env.writes()] == ["repos/pulumi/docs/pulls/2/reviews", "repos/pulumi/docs/pulls/2/merge"]
        text = act.report(res)
        assert "1/2 step(s) succeeded" in text
    finally:
        env.close()


def test_dry_run_runs_preflight_but_writes_nothing():
    env = Env([stampable(1)])
    try:
        p = act.plan(env.queue, args(stamp="1"))
        res = act.execute(p, env.gh, queue=env.queue, dry_run=True)
        assert res[0].ok and "dry-run" in res[0].message and env.writes() == []
    finally:
        env.close()


# ---- route / close / refresh ---------------------------------------------------------


def test_route_team_vs_user_and_defect_comment_carries_footer():
    env = Env([stampable(1, comments=[]), stampable(2, comments=[])], cfg(me=["blog"]))
    try:
        p = act.plan(env.queue, args(route=["1:@pulumi/docs-guild", "2:@cnunciato"]))
        res = act.execute(p, env.gh, queue=env.queue)
        assert all(r.ok for r in res)
        w = env.writes()
        assert w[0]["path"].endswith("/pulls/1/requested_reviewers") and w[0]["body"] == {"team_reviewers": ["docs-guild"]}
        assert w[2]["body"] == {"reviewers": ["cnunciato"]}
        comment = w[1]["body"]["body"]
        assert comment.startswith("Routing to @pulumi/docs-guild: this is a docs change, not mine to approve.")
        assert comment.endswith("_Generated by [Claude Code](https://claude.ai/code)_")
        assert "—" not in comment and "review:absent" not in comment  # the queue's own proxies stay off the PR
    finally:
        env.close()


def test_request_changes_posts_a_review_from_the_judgments_and_labels():
    env = Env([stampable(1, labels=["review:trivial"]), stampable(2, labels=["review:trivial"])])
    try:
        row(env.queue, 1)["judgments"] = [{"finding_id": "L1-7", "file": "content/docs/best-practices/_index.md", "line": 1,
                                          "decision": "Nest the page or make it top-level?", "ask": "Give the page a nav home under Concepts.",
                                          "disposition": "deferred", "note": "Cam's IA call; never sent to the author."}]
        try:
            act.plan(env.queue, args(request_changes=[2]))
            raise AssertionError("expected refusal: nothing to send back")
        except act.ActError as exc:
            assert "nothing to send back" in str(exc)
        p = act.plan(env.queue, args(request_changes=[1], reason="Two things before this merges:"))
        text = act.preview(p, env.queue)
        assert "CHANGES_REQUESTED" in text and "Give the page a nav home under Concepts." in text and "IA call" not in text
        res = act.execute(p, env.gh, queue=env.queue)
        assert res[0].ok
        w = env.writes()
        assert w[0]["path"].endswith("/pulls/1/reviews") and w[0]["body"]["event"] == "REQUEST_CHANGES"
        body = w[0]["body"]["body"]
        assert body.startswith("Two things before this merges:") and "`content/docs/best-practices/_index.md` L1: Give the page a nav home under Concepts." in body
        assert "IA call" not in body  # the approver's note stays on the board
        assert "#update-review" in body  # bot author: tell it how to answer
        assert "Generated by [Claude Code]" not in body  # a review body, not a bot comment
        assert w[1]["path"].endswith("/issues/1/labels") and w[1]["body"] == {"labels": ["needs-author-response"]}
    finally:
        env.close()


def test_a_workflow_author_is_closed_not_sent_back():
    env = Env([stampable(1, labels=["review:trivial"], author="pulumi-bot", author_type="User")])
    try:
        r = row(env.queue, 1)
        r["judgments"] = [{"finding_id": "M1", "file": "content/docs/p1.md", "line": 182,
                           "decision": "The lead-in folds into the bullet above it.",
                           "ask": "Add a blank line before the lead-in.", "disposition": "deferred"}]
        try:
            act.plan(env.queue, args(request_changes=[1]))
            raise AssertionError("expected refusal: pulumi-bot never reads a review")
        except act.ActError as exc:
            assert "is a workflow, not an author" in str(exc) and "--close 1" in str(exc)
        act.plan(env.queue, args(request_changes=[1], force=True))  # the approver can still insist
        p = act.plan(env.queue, args(close=1))  # no --reason needed: the row writes its own
        res = act.execute(p, env.gh, queue=env.queue)
        assert res[0].ok
        w = env.writes()
        body = w[0]["body"]["body"]
        assert w[0]["path"].endswith("/issues/1/comments")
        assert "opened by a workflow run" in body and "Add a blank line before the lead-in." in body
        assert "#update-review" not in body and "re-queues the page" in body
        assert body.endswith("_Generated by [Claude Code](https://claude.ai/code)_")
        assert w[1]["method"] == "PATCH" and w[1]["body"] == {"state": "closed"}
    finally:
        env.close()


def test_request_changes_body_voice_by_author_type():
    ext = {"author": {"type": "external"}, "judgments": [{"decision": "Fix the count.", "file": "a.md", "line": 3}]}
    b = act.request_changes_body(ext)
    assert b.startswith("Thanks for this.") and b.endswith("Mention @claude if you need help.")
    internal = {"author": {"type": "internal"}, "judgments": [], "review": {"items": [{"id": "F1", "bucket": "outstanding", "file": "a.md", "anchor": "L3", "summary": "Wrong count."}]}}
    assert act.request_changes_body(internal) == "- `a.md` L3: Wrong count."


def test_a_send_back_leaves_out_findings_the_approver_already_resolved():
    pr = {"author": {"type": "internal"}, "judgments": [
        {"finding_id": "F1", "file": "a.md", "line": 3, "decision": "Is the count right?",
         "ask": "Fix the count.", "disposition": "deferred"},
        {"finding_id": "F2", "file": "a.md", "line": 9, "decision": "Move the role section to its own page?",
         "disposition": "accepted", "note": "It already lived here."},
        {"finding_id": "F3", "file": "a.md", "line": 12, "decision": "Reword a historical sentence?", "disposition": "not-applicable"},
        {"finding_id": "F4", "file": "b.md", "line": 5, "decision": "Leave the parenthetical?",
         "ask": "No change needed: dated, not wrong.", "disposition": "accepted"},
    ]}
    body = act.request_changes_body(pr)
    assert "Fix the count." in body
    assert "role section" not in body and "historical sentence" not in body  # the approver's question never reaches the author
    assert "`b.md` L5: No change needed: dated, not wrong." in body  # an explicit ask is still the approver's to send
    resolved = {"author": {"type": "internal"}, "judgments": [pr["judgments"][2]],
                "review": {"items": [{"id": "F3", "bucket": "outstanding", "file": "a.md", "anchor": "L12", "summary": "Reword it."}]}}
    assert act.ask_lines(resolved) == []  # the judged finding is resolved, and nothing else is open
    partial = {"author": {"type": "internal"}, "judgments": [pr["judgments"][0]],
               "review": {"items": [{"id": "F1", "bucket": "outstanding", "file": "a.md", "anchor": "L3", "summary": "Wrong count."},
                                    {"id": "F5", "bucket": "outstanding", "file": "c.md", "anchor": "L8", "summary": "Dead anchor."}]}}
    assert act.ask_lines(partial) == ["- `a.md` L3: Fix the count.", "- `c.md` L8: Dead anchor."]  # an unjudged finding still goes back
    env = Env([stampable(1, labels=["review:trivial"])])
    try:
        row(env.queue, 1)["judgments"] = resolved["judgments"]
        try:
            act.plan(env.queue, args(request_changes=[1]))
            raise AssertionError("expected refusal: every judged finding is resolved")
        except act.ActError as exc:
            assert "nothing to send back" in str(exc)
    finally:
        env.close()


def test_rerun_posts_a_new_review_mention_with_a_status_reason():
    env = Env([stampable(1, labels=["review:error", "domain:docs"]), stampable(2)])
    try:
        p = act.plan(env.queue, args(rerun=[1, 2]))
        assert "#new-review" in act.preview(p)
        res = act.execute(p, env.gh, queue=env.queue)
        assert all(r.ok for r in res)
        w = env.writes()
        assert w[0]["body"]["body"].startswith("@claude the last review run failed #new-review") and w[0]["path"].endswith("/issues/1/comments")
        assert w[0]["body"]["body"].endswith("(https://claude.ai/code)_")
        assert w[1]["body"]["body"].startswith("@claude the review is current #new-review")
    finally:
        env.close()


def test_close_cross_links_and_refresh_mention():
    env = Env([stampable(1), stampable(2)])
    try:
        p = act.plan(env.queue, args(close=1, superseded_by=2, refresh=[2], reason="the label lied"))
        res = act.execute(p, env.gh, queue=env.queue)
        assert all(r.ok for r in res)
        w = env.writes()
        assert "Closing in favor of #2" in w[0]["body"]["body"] and w[0]["path"].endswith("/issues/1/comments")
        assert "Supersedes #1" in w[1]["body"]["body"] and w[1]["path"].endswith("/issues/2/comments")
        assert w[2]["method"] == "PATCH" and w[2]["body"] == {"state": "closed"}
        assert w[3]["body"]["body"].startswith("@claude the label lied #update-review") and w[3]["body"]["body"].endswith("(https://claude.ai/code)_")
    finally:
        env.close()


# ---- fix / unblock ---------------------------------------------------------------


def test_fix_description_uses_the_drafted_body():
    env = Env([stampable(1)])
    try:
        row(env.queue, 1)["fix_draft"] = {"kind": "description", "body": "### Proposed changes\n\nAccurate now."}
        p = act.plan(env.queue, args(fix=[1]))
        res = act.execute(p, env.gh, queue=env.queue)
        assert res[0].ok and env.writes()[0]["body"] == {"body": "### Proposed changes\n\nAccurate now."}
    finally:
        env.close()


class FakeGit:
    """Records every call. `add_worktree` hands back a child FakeGit that
    shares the call log and is rooted at `root` (a real temp dir, so
    apply_suggestion can edit files in it); the parent never sees a checkout."""

    def __init__(self, merge_ok=True, conflicts=("content/docs/a.md",), head="", root: Path | None = None, calls=None):
        self.merge_ok, self.conflicts, self.head, self.root = merge_ok, list(conflicts), head, root or Path("/nonexistent")
        self.calls = calls if calls is not None else []
        self.worktrees: list["FakeGit"] = []

    def fetch(self, *refs):
        self.calls.append(("fetch", refs))

    def rev_parse(self, ref):
        self.calls.append(("rev-parse", ref))
        return self.head

    def add_worktree(self, ref):
        self.calls.append(("worktree-add", ref))
        wt = FakeGit(self.merge_ok, self.conflicts, self.head, self.root, self.calls)
        self.worktrees.append(wt)
        return wt

    def remove_worktree(self, wt):
        self.calls.append(("worktree-remove", str(wt.root)))

    def merge(self, ref):
        self.calls.append(("merge", ref))
        return self.merge_ok

    def conflicted_files(self):
        return self.conflicts

    def push(self, b):
        self.calls.append(("push", b))

    def add(self, *p):
        self.calls.append(("add", p))

    def commit(self, m):
        self.calls.append(("commit", m))
        return "c" * 40

    def __getattr__(self, name):  # checkout / checkout_tracking / current_branch: act.py must never want them
        raise AssertionError(f"act.py touched the checkout: git.{name}")


def test_unblock_pushes_only_a_clean_merge_and_works_in_a_worktree():
    """Finding 8: the merge happens in a detached worktree that is removed
    afterwards; the person's branch is never checked out, reset, or left with
    a merge commit. (Replaces the returns-to-start-branch test: there is no
    start branch to return to any more.)"""
    env = Env([stampable(1, mergeable_state="dirty")])
    try:
        head = row(env.queue, 1)["head"]["sha"]
        p = act.plan(env.queue, args(unblock=[1]))
        git = FakeGit(merge_ok=True, head=head)
        res = act.execute(p, env.gh, git, queue=env.queue)
        assert res[0].ok, res[0].message
        assert git.calls == [("fetch", ("master", "branch-1")), ("rev-parse", "origin/branch-1"), ("worktree-add", "origin/branch-1"),
                             ("merge", "origin/master"), ("push", "branch-1"), ("worktree-remove", "/nonexistent")]
        git = FakeGit(merge_ok=False, head=head)
        res = act.execute(p, env.gh, git, queue=env.queue)
        assert res[0].ok is False and "content/docs/a.md" in res[0].message
        assert git.calls[-1][0] == "worktree-remove" and not any(c[0] == "push" for c in git.calls)
        # origin moved after the plan: nothing is merged or pushed
        git = FakeGit(merge_ok=True, head="f" * 40)
        res = act.execute(p, env.gh, git, queue=env.queue)
        assert res[0].ok is False and "head-moved on origin/branch-1" in res[0].message
        assert not any(c[0] in ("worktree-add", "push") for c in git.calls)
        # dry-run never runs git
        git = FakeGit(merge_ok=True, head=head)
        res = act.execute(p, env.gh, git, queue=env.queue, dry_run=True)
        assert res[0].ok and res[0].message.startswith("dry-run") and git.calls == [] and env.writes() == []
    finally:
        env.close()


def _suggestion(cid: int, path: str, line: int | None, text: str, start_line: int | None = None) -> dict:
    return {"id": cid, "path": path, "line": line, "original_line": line or 4, "start_line": start_line,
            "body": f"<!-- CLAUDE_STYLE_SUGGESTION -->\n```suggestion\n{text}\n```", "diff_hunk": ""}


def test_fix_applies_suggestions_bottom_up_and_skips_outdated_ones():
    """Finding 6: a multi-line suggestion replaces its whole span, two in one
    file don't shift each other, and one GitHub marks outdated (`line` null)
    is skipped rather than applied at its original line."""
    sugg = [_suggestion(11, "content/docs/p1.md", 4, "TWO\nTHREE\nFOUR", start_line=2),  # lines 2-4
            _suggestion(12, "content/docs/p1.md", 7, "SEVEN"),                                # single line
            _suggestion(13, "content/docs/p1.md", None, "NEVER")]                             # outdated on the head
    env = Env([stampable(1, review_comments=sugg)])
    try:
        head = row(env.queue, 1)["head"]["sha"]
        assert len(row(env.queue, 1)["one_click_suggestions"]) == 3  # collect keeps the outdated one (line ← original_line)
        p = act.plan(env.queue, args(fix=[1]))
        text = act.preview(p, env.queue)
        assert "apply 3 suggestion(s) bottom-up" in text and "content/docs/p1.md L7 → SEVEN" in text
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "content/docs").mkdir(parents=True)
            (root / "content/docs/p1.md").write_text("one\ntwo\nthree\nfour\nfive\nsix\nseven\neight\n")
            git = FakeGit(head=head, root=root)
            res = act.execute(p, env.gh, git, queue=env.queue)
            assert res[0].ok and "2 suggestion(s)" in res[0].message and "outdated" in res[0].message, res[0].message
            assert (root / "content/docs/p1.md").read_text() == "one\nTWO\nTHREE\nFOUR\nfive\nsix\nSEVEN\neight\n"
            kinds = [c[0] for c in git.calls]
            assert kinds == ["fetch", "rev-parse", "worktree-add", "add", "add", "commit", "push", "worktree-remove"]
            assert ("commit", "Apply 2 review suggestion(s)") in git.calls
        # dry-run: the PATCH/apply are described, git never runs
        git = FakeGit(head=head)
        res = act.execute(p, env.gh, git, queue=env.queue, dry_run=True)
        assert res[0].ok and "2 suggestion(s)" in res[0].message and git.calls == []
    finally:
        env.close()


def test_fix_failure_discards_the_worktree_and_pushes_nothing():
    """Finding 7: an exception mid-apply removes the worktree (with its
    half-applied edits) instead of leaving them staged on a local branch."""
    env = Env([stampable(1, review_comments=[_suggestion(11, "content/docs/missing.md", 2, "X")])])
    try:
        head = row(env.queue, 1)["head"]["sha"]
        p = act.plan(env.queue, args(fix=[1]))
        with tempfile.TemporaryDirectory() as td:
            git = FakeGit(head=head, root=Path(td))  # the file the suggestion targets does not exist → OSError
            res = act.execute(p, env.gh, git, queue=env.queue)
            assert res[0].ok is False and "FileNotFoundError" in res[0].message
            assert git.calls[-1][0] == "worktree-remove" and not any(c[0] in ("commit", "push") for c in git.calls)
    finally:
        env.close()


def test_apply_suggestion_replaces_the_line_range():
    with tempfile.TemporaryDirectory() as td:
        f = Path(td) / "a.md"
        f.write_text("one\ntwo\nthree\nfour\n")
        act.apply_suggestion(Path(td), "a.md", 2, 3, "TWO\nTHREE")
        assert f.read_text() == "one\nTWO\nTHREE\nfour\n"


# ---- the audit findings ------------------------------------------------------------


def test_repeated_flags_accumulate_instead_of_keeping_the_last():
    """Finding 1 / 14: --stamp, --close, --superseded-by and --reason repeat."""
    env = Env([stampable(1), stampable(2), stampable(3), stampable(4)])
    try:
        ns = act.build_parser().parse_args(["--stamp", "1", "--stamp", "3:no-merge,1", "--close", "4", "--close", "2",
                                            "--superseded-by", "4:1", "--reason", "2=dup of #1", "--reason", "3=unused"])
        assert ns.stamp == ["1", "3:no-merge,1"] and ns.close == [4, 2] and ns.superseded_by == ["4:1"]
        assert act._split_stamps(ns.stamp) == [(1, None), (3, "no-merge"), (1, None)]
        try:
            act.plan(env.queue, ns)  # #3 takes no reason
            raise AssertionError("expected refusal")
        except act.ActError as exc:
            assert "3=" in str(exc) and "no step on #3" in str(exc)
        ns = act.build_parser().parse_args(["--stamp", "1", "--stamp", "3", "--close", "4", "--close", "2",
                                            "--superseded-by", "4:1", "--reason", "2=dup of #1"])
        p = act.plan(env.queue, ns)
        assert [(s.kind, s.pr) for s in p.steps] == [("stamp", 1), ("stamp", 3), ("close", 4), ("close", 2)]
        by = {(s.kind, s.pr): s for s in p.steps}
        assert by[("close", 4)].args["superseded_by"] == 1 and by[("close", 2)].args["reason"] == "dup of #1"
        # bare --superseded-by needs exactly one --close
        try:
            act.plan(env.queue, args(close=[4, 2], superseded_by=["1"]))
            raise AssertionError("expected refusal")
        except act.ActError as exc:
            assert "--superseded-by 4:1" in str(exc) or "N:1" in str(exc)
        assert act.plan(env.queue, args(close=[4], superseded_by=["1"])).steps[0].args["superseded_by"] == 1
        try:
            act.plan(env.queue, args(close=[4], superseded_by=["2:1"]))
            raise AssertionError("expected refusal")
        except act.ActError as exc:
            assert "not being closed" in str(exc)
    finally:
        env.close()


def test_a_reason_lands_on_exactly_one_step():
    """Finding 2: one bare --reason used to go into every reason-taking step.
    Bare text now needs exactly one consumer; N=text is scoped; a generated
    row's close keeps its judgment-built comment unless scoped explicitly;
    a human PR's close can't borrow a reason meant for another step."""
    env = Env([stampable(1, labels=["review:trivial"]), stampable(2, author="camsoper", author_type="User"),
               stampable(3, labels=["review:trivial"], author="pulumi-bot", author_type="User")])
    try:
        row(env.queue, 1)["judgments"] = [{"finding_id": "F1", "file": "a.md", "line": 3, "ask": "Fix the count.", "disposition": "deferred"}]
        row(env.queue, 3)["judgments"] = [{"finding_id": "M1", "file": "b.md", "line": 5, "ask": "Add a blank line.", "disposition": "deferred"}]
        try:
            act.plan(env.queue, args(request_changes=[1], refresh=[2], reason=["Two things:"]))
            raise AssertionError("expected refusal: ambiguous")
        except act.ActError as exc:
            assert "request-changes #1" in str(exc) and "refresh #2" in str(exc) and "N=" in str(exc)
        try:
            act.plan(env.queue, args(close=[2], refresh=[1], reason=["the label lied"]))
            raise AssertionError("expected refusal: a human close can't borrow the refresh reason")
        except act.ActError as exc:
            assert "close #2" in str(exc) and "refresh #1" in str(exc)
        p = act.plan(env.queue, args(request_changes=[1], refresh=[2], close=[3],
                                     reason=["1=Two things:", "2=the docs moved"]))
        by = {(s.kind, s.pr): s for s in p.steps}
        assert by[("request-changes", 1)].args["body"].startswith("Two things:")
        assert by[("refresh", 2)].args["comment"].startswith("@claude the docs moved #update-review")
        assert "opened by a workflow run" in by[("close", 3)].args["comment"] and "Add a blank line." in by[("close", 3)].args["comment"]
        # scoped to the generated row, the reason replaces the judgment-built comment
        p = act.plan(env.queue, args(close=[3], reason=["3=Superseded by the rewrite in flight."]))
        assert p.steps[0].args["comment"].startswith("Superseded by the rewrite in flight.")
        # a bare reason with one consumer still works, and the generated close stays on its judgments
        p = act.plan(env.queue, args(refresh=[2], close=[3], reason=["the docs moved"]))
        by = {(s.kind, s.pr): s for s in p.steps}
        assert "the docs moved" in by[("refresh", 2)].args["comment"] and "the docs moved" not in by[("close", 3)].args["comment"]
        try:
            act.plan(env.queue, args(stamp=["1"], force=True, reason=["nobody takes this"]))
            raise AssertionError("expected refusal: no consumer")
        except act.ActError as exc:
            assert "no step in the plan takes one" in str(exc)
        try:
            act.plan(env.queue, args(refresh=[2], reason=["a", "b"]))
            raise AssertionError("expected refusal: two bare reasons")
        except act.ActError as exc:
            assert "more than one bare --reason" in str(exc)
    finally:
        env.close()


def test_plan_dedupes_repeats_and_refuses_two_decisions_on_one_pr():
    """Finding 3."""
    env = Env([stampable(1, labels=["review:trivial"]), stampable(2)])
    try:
        for n in (1, 2):
            row(env.queue, n)["judgments"] = [{"finding_id": "F1", "file": "a.md", "line": 3, "ask": "Fix the count.", "disposition": "deferred"}]
        p = act.plan(env.queue, args(request_changes=[1, 1], refresh=[1, 1], reason=["1=Two things:"], stamp=["2,2", "2"]))
        assert [(s.kind, s.pr) for s in p.steps] == [("stamp", 2), ("request-changes", 1), ("refresh", 1)]
        res = act.execute(p, env.gh, queue=env.queue)
        assert all(r.ok for r in res)
        paths = [w["path"] for w in env.writes()]
        assert paths.count("repos/pulumi/docs/pulls/1/reviews") == 1 and paths.count("repos/pulumi/docs/issues/1/comments") == 1
        for bad, msg in ((args(stamp=["2:no-merge"], request_changes=[2]), "--stamp and --request-changes contradict"),
                         (args(stamp=["2:no-merge", "2:merge"]), "--stamp given twice with different arguments"),
                         (args(route=["2:@cnunciato"], close=[2], reason=["2=bye"]), "--route and --close contradict"),
                         (args(stamp=["2"], close=[2], reason=["2=bye"]), "--stamp and --close contradict")):
            try:
                act.plan(env.queue, bad)
                raise AssertionError(f"plan accepted {bad}")
            except act.ActError as exc:
                assert msg in str(exc), str(exc)
    finally:
        env.close()


def test_bodies_are_fixed_at_plan_time_and_the_preview_shows_them():
    """Finding 4: the plan carries every body; execute sends exactly that even
    when the queue on disk has changed; the preview prints the same text; a
    dry run lists each write it would make."""
    env = Env([stampable(1, labels=["review:trivial"]), stampable(2), stampable(3)], cfg(me=["blog"]))
    try:
        row(env.queue, 1)["judgments"] = [{"finding_id": "F1", "file": "a.md", "line": 3, "decision": "Is the count right?",
                                          "ask": "Fix the count.", "disposition": "deferred"}]
        row(env.queue, 2)["fix_draft"] = {"kind": "description", "body": "### Proposed changes\n\nAccurate now."}
        p = act.plan(env.queue, args(request_changes=[1], route=["2:@cnunciato"], fix=[2], refresh=[3],
                                     reason=["1=Two things:", "3=the docs moved"]))
        text = act.preview(p, env.queue)
        assert "Two things:" in text and "`a.md` L3: Fix the count." in text
        assert "Routing to @cnunciato: this is a docs change, not mine to approve." in text
        assert "**F1** Is the count right?" not in text  # #2 has no judgments; #1's stay on its own step
        assert "PATCH pull body: ### Proposed changes" in text
        assert "@claude the docs moved #update-review" in text
        assert "review:absent" not in text  # raw reason codes the comment filters out never show as if posted
        # the world changes under the plan: a re-collect that lost the judgments and the draft
        p2 = act.Plan.from_json(json.loads(json.dumps(p.to_json())))
        assert p2.schema == act.PLAN_SCHEMA == 2
        res = act.execute(p2, env.gh, queue={"prs": []})
        assert all(r.ok for r in res), [r.message for r in res]
        w = {(x["method"], x["path"]): x["body"] for x in env.writes()}
        assert w[("POST", "repos/pulumi/docs/pulls/1/reviews")]["body"].startswith("Two things:\n- `a.md` L3: Fix the count.")
        assert w[("POST", "repos/pulumi/docs/issues/2/comments")]["body"].startswith("Routing to @cnunciato")
        assert w[("PATCH", "repos/pulumi/docs/pulls/2")] == {"body": "### Proposed changes\n\nAccurate now."}
        assert w[("POST", "repos/pulumi/docs/issues/3/comments")]["body"].startswith("@claude the docs moved #update-review")
        try:
            act.Plan.from_json({"schema": 1, "repo": "pulumi/docs", "created_at": "", "steps": []})
            raise AssertionError("an old plan must not execute")
        except act.ActError as exc:
            assert "re-plan" in str(exc)
    finally:
        env.close()
    env = Env([stampable(1)])
    try:
        p = act.plan(env.queue, args(stamp=["1"], refresh=[1], reason=["x"]))
        res = act.execute(p, env.gh, queue=env.queue, dry_run=True)
        assert all(r.ok for r in res) and env.writes() == []
        assert [w["path"] for w in res[0].writes] == ["repos/pulumi/docs/pulls/1/reviews", "repos/pulumi/docs/pulls/1/merge"]
        text = act.report(res, writes=True)
        assert "would: POST repos/pulumi/docs/pulls/1/reviews  Approved." in text
        assert "would: PUT repos/pulumi/docs/pulls/1/merge" in text and "would: POST repos/pulumi/docs/issues/1/comments  @claude x #update-review" in text
    finally:
        env.close()


def test_every_write_runs_the_head_preflight():
    """Finding 5: route, request-changes, close, refresh, rerun, deploy, fix
    and unblock all refuse a merged PR or a moved head, and the batch goes on."""
    env = Env([stampable(1, labels=["review:trivial"]), stampable(2, mergeable_state="dirty"), stampable(3),
               stampable(4, author="camsoper", author_type="User")])
    try:
        row(env.queue, 1)["judgments"] = [{"finding_id": "F1", "file": "a.md", "line": 3, "ask": "Fix the count.", "disposition": "deferred"}]
        row(env.queue, 2)["fix_draft"] = {"kind": "description", "body": "### Proposed changes\n\nAccurate now."}
        p = act.plan(env.queue, args(request_changes=[1], route=["2:@cnunciato"], fix=[2], unblock=[2], close=[4],
                                     refresh=[2], rerun=[2], deploy=[2], reason=["1=Two things:", "4=bye"]))
        assert [(s.kind, s.pr) for s in p.steps] == [("route", 2), ("request-changes", 1), ("unblock", 2), ("fix", 2),
                                                     ("close", 4), ("refresh", 2), ("rerun", 2), ("deploy", 2)]
        env.set_detail(1, state="closed")
        env.set_detail(4, state="closed")
        env.move_head(2, "e" * 40)
        git = FakeGit(head="e" * 40)
        res = act.execute(p, env.gh, git, queue=env.queue)
        assert [r.ok for r in res] == [False] * len(res)
        assert all("preflight refused" in r.message for r in res), [r.message for r in res]
        assert "head-moved" in res[0].message and "head-state: PR is closed" in res[1].message and "head-state" in res[4].message
        assert env.writes() == [] and git.calls == []
        # ...and #3 in the same batch still goes through
        p = act.plan(env.queue, args(stamp=["3"], deploy=[2]))
        res = act.execute(p, env.gh, git, queue=env.queue)
        assert [r.ok for r in res] == [True, False] and [w["path"] for w in env.writes()] == [
            "repos/pulumi/docs/pulls/3/reviews", "repos/pulumi/docs/pulls/3/merge"]
    finally:
        env.close()


def _chain_env(**over) -> "Env":
    from test_analyze import _file  # noqa: PLC0415
    a = stampable(1, title="Fix the intro", files=[_file("content/docs/a.md", ["x"], ["o"], old_start=10)], **over)
    b = stampable(2, title="Reword the intro", files=[_file("content/docs/a.md", ["y"], ["o"], old_start=10)])
    return Env([a, b])


def test_chain_goes_through_the_stamp_gates_and_the_unblock_waits_on_the_merge():
    """Finding 9: the chain's first link is a --stamp step (resolves, plan-time
    blocker check, preflight), and the next link's unblock is skipped when
    that stamp did not merge."""
    env = _chain_env()
    try:
        cl = env.queue["clusters"][0]
        assert cl["recommendation"]["kind"] == "chain" and cl["recommendation"]["first"] == 1
        r = row(env.queue, 1)
        r["judgments"] = [{"finding_id": "F6", "disposition": "refuted", "note": "Checked; the claim holds."}]
        p = act.plan(env.queue, args(chain=["C1"]))
        assert [(s.kind, s.pr) for s in p.steps] == [("stamp", 1), ("unblock", 2)]
        assert p.steps[0].args["resolves"] == ["/resolve F6 refuted: Checked; the claim holds."]
        assert p.steps[0].args["chain"] == "C1" and p.steps[1].args["requires"] == ["stamp", 1]
        assert "skipped unless stamp #1 merges" in act.preview(p, env.queue)
        # the stamp's preflight refuses (head moved) → the unblock never runs git
        env.move_head(1, "e" * 40)
        git = FakeGit(head=row(env.queue, 2)["head"]["sha"])
        res = act.execute(p, env.gh, git, queue=env.queue)
        assert res[0].ok is False and "head-moved" in res[0].message
        assert res[1].ok is False and "skipped: waits on stamp #1" in res[1].message
        assert git.calls == [] and env.writes() == []
    finally:
        env.close()
    # plan-time: an open 🚨 on the first link refuses the chain like a stamp
    from test_analyze import _file  # noqa: PLC0415
    env = Env([_with_open_findings(1, title="Fix the intro", files=[_file("content/docs/a.md", ["x"], ["o"], old_start=10)]),
               stampable(2, title="Reword the intro", files=[_file("content/docs/a.md", ["y"], ["o"], old_start=10)])])
    try:
        r = row(env.queue, 1)
        r["verdict"], r["blockers"] = "judge", []
        env.queue["clusters"][0]["recommendation"] = {"kind": "chain", "first": 1, "next": 2}
        try:
            act.plan(env.queue, args(chain=["C1"]))
            raise AssertionError("chain merged over open findings")
        except act.ActError as exc:
            assert "unanswered blocking review finding" in str(exc)
    finally:
        env.close()


def test_a_stamp_that_fails_partway_reports_what_landed_and_a_rerun_skips_it():
    """Finding 10: the resolves and the approval post before the merge; a
    refused merge lists them, and re-running the step posts neither again."""
    env = Env([stampable(1)])
    try:
        head = row(env.queue, 1)["head"]["sha"]
        row(env.queue, 1)["judgments"] = [{"finding_id": "F6", "disposition": "refuted", "note": "Checked."}]
        p = act.plan(env.queue, args(stamp=["1"]))
        env.set_check_runs(1, [{"name": "build", "status": "completed", "conclusion": "success"},
                               {"name": "Sentinel", "status": "completed", "conclusion": "failure"}])
        res = act.execute(p, env.gh, queue=env.queue, sleep=lambda s: None)
        assert res[0].ok is False and "approved, not merged" in res[0].message, res[0].message
        assert [w["path"] for w in res[0].writes] == ["repos/pulumi/docs/issues/1/comments", "repos/pulumi/docs/pulls/1/reviews"]
        text = act.report(res)
        assert "landed: POST repos/pulumi/docs/issues/1/comments  /resolve F6 refuted: Checked." in text
        assert "landed: POST repos/pulumi/docs/pulls/1/reviews  Approved." in text
        # what landed is now on the PR; the Sentinel comes back green; re-run
        env.add_comment(1, res[0].writes[0]["body"]["body"])
        env.add_review(1, "APPROVED", commit_id=head)
        env.set_check_runs(1, [{"name": "build", "status": "completed", "conclusion": "success"},
                               {"name": "Sentinel", "status": "completed", "conclusion": "success"}])
        before = len(env.writes())
        res = act.execute(p, env.gh, queue=env.queue, sleep=lambda s: None)
        assert res[0].ok and "squash-merged" in res[0].message and "resolves already posted" in res[0].message \
            and "already approved" in res[0].message, res[0].message
        assert [w["method"] for w in env.writes()[before:]] == ["PUT"]
    finally:
        env.close()


def test_own_changes_requested_review_is_not_a_blocker():
    """Finding 11: the approver's earlier CR is superseded by the approval
    about to post; anyone else's still blocks."""
    cr = lambda who: {"user": {"login": who, "type": "User"}, "state": "CHANGES_REQUESTED", "submitted_at": "2026-09-12T00:00:00Z"}  # noqa: E731
    env = Env([stampable(1, reviews=[cr("CamSoper")]), stampable(2, reviews=[cr("CamSoper"), cr("cnunciato")])])
    try:
        for n, want in ((1, True), (2, False)):
            s = act.Step("stamp", n, {"merge": True}, expect_head=row(env.queue, n)["head"]["sha"])
            ok, msg, _ = act.preflight(env.gh, s)
            assert ok is want, msg
        assert "changes requested by cnunciato" in msg and "CamSoper" not in msg
    finally:
        env.close()


def test_resolve_posts_the_note_and_never_the_decision():
    """Finding 12."""
    pr = {"review": {"surface": "v3"}, "judgments": [
        {"finding_id": "F1", "disposition": "refuted", "decision": "Does the sentence claim that?"},
        {"finding_id": "F2", "disposition": "fixed", "decision": "Fix the count?", "note": "Pushed in 3f2a1."},
        {"finding_id": "F3", "disposition": "accepted", "decision": "Leave it?"}]}
    assert act.resolve_lines(pr) == ["/resolve F2 fixed: Pushed in 3f2a1."]


def test_sentinel_is_left_out_of_the_preflight_and_polled_before_the_merge():
    """Finding 13: an enforcing Sentinel is red until the approval exists, so
    it can't gate the approval; after approving, a bounded poll decides the merge."""
    env = Env([stampable(1)])
    try:
        p = act.plan(env.queue, args(stamp=["1"]))
        assert "Sentinel aside" in act.preview(p, env.queue)
        # failing before approval: not a preflight blocker; approval posts, merge refused
        env.set_check_runs(1, [{"name": "build", "status": "completed", "conclusion": "success"},
                               {"name": "sentinel", "status": "completed", "conclusion": "failure"}])
        res = act.execute(p, env.gh, queue=env.queue, sleep=lambda s: None)
        assert res[0].ok is False and "Sentinel check concluded failure" in res[0].message
        assert [w["path"] for w in res[0].writes] == ["repos/pulumi/docs/pulls/1/reviews"]
    finally:
        env.close()
    env = Env([stampable(1, check_runs=[{"name": "build", "status": "completed", "conclusion": "success"},
                                        {"name": "Sentinel", "status": "in_progress", "conclusion": None}])])
    try:
        naps = []
        p = act.plan(env.queue, args(stamp=["1"], force=True))  # a pending check makes the row a judge row
        res = act.execute(p, env.gh, queue=env.queue, sleep=naps.append)
        assert res[0].ok is False and "still pending after 90s" in res[0].message
        assert naps == [act.SENTINEL_POLL_S] * (act.SENTINEL_WAIT_S // act.SENTINEL_POLL_S)
        assert [w["method"] for w in env.writes()] == ["POST"]  # approval only
    finally:
        env.close()
    env = Env([stampable(1, check_runs=[{"name": "build", "status": "completed", "conclusion": "success"},
                                        {"name": "Sentinel", "status": "completed", "conclusion": "neutral"}])])
    try:
        p = act.plan(env.queue, args(stamp=["1"]))
        naps = []
        res = act.execute(p, env.gh, queue=env.queue, sleep=naps.append)
        assert res[0].ok and "squash-merged" in res[0].message and naps == []
        # dry-run skips the wait: no approval was posted for the Sentinel to see
        res = act.execute(p, env.gh, queue=env.queue, dry_run=True, sleep=naps.append)
        assert res[0].ok and "Sentinel wait skipped" in res[0].message and naps == []
    finally:
        env.close()


def run_standalone() -> int:
    """The --self-test harness; test list bound at call time (test_sentinel.py)."""
    import inspect  # noqa: PLC0415
    all_tests = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    failures = 0
    for t in all_tests:
        if inspect.signature(t).parameters:
            print(f"  skip: {t.__name__} (pytest fixtures; run via pytest)")
            continue
        try:
            t()
            print(f"  ok: {t.__name__}")
        except AssertionError as exc:
            failures += 1
            print(f"  FAIL: {t.__name__}: {exc}", file=sys.stderr)
        except Exception as exc:  # noqa: BLE001
            failures += 1
            print(f"  FAIL: {t.__name__}: {type(exc).__name__}: {exc}", file=sys.stderr)
    if failures:
        print(f"{failures} act test(s) failed", file=sys.stderr)
        return 1
    print("all act self-tests passed")
    return 0


if __name__ == "__main__":
    sys.exit(run_standalone())


# ---- rerun-checks / multi-target route / reason-only send-back ------------------


def _runs_snapshot(env: "Env", number: int, runs: list[dict]) -> None:
    sha = row(env.queue, number)["head"]["sha"]
    f = snapshot_path(env.root, "GET", "repos/pulumi/docs/actions/runs", {"head_sha": sha, "per_page": 100})
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(json.dumps({"total_count": len(runs), "workflow_runs": runs}))


def test_rerun_checks_reruns_the_newest_failed_run_per_workflow():
    red = [{"name": "lint", "status": "completed", "conclusion": "failure"}]
    env = Env([fresh(1, check_runs=red), fresh(2, check_runs=red)])
    try:
        assert row(env.queue, 1)["verdict"] == "blocked" and any(a["cmd"] == "--rerun-checks 1" for a in row(env.queue, 1)["actions"])
        _runs_snapshot(env, 1, [
            {"id": 11, "name": "Lint", "path": ".github/workflows/lint.yml", "run_number": 1, "status": "completed", "conclusion": "failure"},
            {"id": 12, "name": "Lint", "path": ".github/workflows/lint.yml", "run_number": 2, "status": "completed", "conclusion": "success"},
            {"id": 21, "name": "Build", "path": ".github/workflows/build.yml", "run_number": 5, "status": "completed", "conclusion": "failure"},
            {"id": 31, "name": "Deploy", "path": ".github/workflows/deploy.yml", "run_number": 3, "status": "in_progress", "conclusion": None},
        ])
        _runs_snapshot(env, 2, [{"id": 41, "name": "Lint", "path": ".github/workflows/lint.yml", "run_number": 1, "status": "completed", "conclusion": "success"}])
        p = act.plan(env.queue, args(rerun_checks=[1, 2]))
        assert [(s.kind, s.pr) for s in p.steps] == [("rerun-checks", 1), ("rerun-checks", 2)]
        assert "rerun-failed-jobs" in act.preview(p)
        res = act.execute(p, env.gh, queue=env.queue)
        # #1: only the newest failed run per workflow (the lint failure was superseded by a success)
        assert res[0].ok and res[0].message == "re-ran the failed jobs of 1 workflow run(s): Build"
        assert [w["path"] for w in env.writes()] == ["repos/pulumi/docs/actions/runs/21/rerun-failed-jobs"]
        # #2: red in the rollup but no failed run to re-run — said, not guessed
        assert res[1].ok is False and "no failed workflow run" in res[1].message
        # a moved head refuses like every other write
        env.move_head(1, "e" * 40)
        res = act.execute(p, env.gh, queue=env.queue)
        assert res[0].ok is False and "head-moved" in res[0].message
        # not a decision: it rides beside one
        p = act.plan(env.queue, args(rerun_checks=[1], route=["1:@cnunciato"]))
        assert [s.kind for s in p.steps] == ["route", "rerun-checks"]
    finally:
        env.close()


def test_route_with_two_targets_is_one_step_and_one_request():
    env = Env([stampable(1), stampable(2)])
    try:
        p = act.plan(env.queue, args(route=["1:@pulumi/docs-guild", "1:@pulumi/docs-marketing-review", "1:@cnunciato"]))
        assert [(s.kind, s.pr) for s in p.steps] == [("route", 1)]
        assert p.steps[0].args["targets"] == ["@pulumi/docs-guild", "@pulumi/docs-marketing-review", "@cnunciato"]
        assert "Routing to @pulumi/docs-guild and @pulumi/docs-marketing-review and @cnunciato" in p.steps[0].args["comment"]
        res = act.execute(p, env.gh, queue=env.queue)
        assert res[0].ok and res[0].message == "review requested from @pulumi/docs-guild, @pulumi/docs-marketing-review, @cnunciato"
        w = env.writes()
        assert w[0]["path"].endswith("/pulls/1/requested_reviewers")
        assert w[0]["body"] == {"reviewers": ["cnunciato"], "team_reviewers": ["docs-guild", "docs-marketing-review"]}
        assert w[1]["path"].endswith("/issues/1/comments") and len(w) == 2
        # a bare --route N takes every target the row carries
        row(env.queue, 2)["route_targets"] = ["@pulumi/docs-guild", "@pulumi/docs-marketing-review"]
        row(env.queue, 2)["actions"] = [{"id": "route", "cmd": "--route 2:@pulumi/docs-guild --route 2:@pulumi/docs-marketing-review",
                                         "targets": ["@pulumi/docs-guild", "@pulumi/docs-marketing-review"]}]
        p = act.plan(env.queue, args(route=["2"]))
        assert p.steps[0].args["targets"] == ["@pulumi/docs-guild", "@pulumi/docs-marketing-review"]
        assert act.row_route_targets({"actions": [{"id": "route", "cmd": "--route 3:@a --route 3:@b/c"}]}) == ["@a", "@b/c"]
    finally:
        env.close()


def test_request_changes_with_only_a_reason_goes_back():
    """A red-CI or unpushable-conflict row has no finding to send back, so
    the board's button carries the reason; that reason is the whole review."""
    env = Env([stampable(1, check_runs=[{"name": "lint", "status": "completed", "conclusion": "failure"}])])
    try:
        cmd = next(a["cmd"] for a in row(env.queue, 1)["actions"] if a["id"] == "request-changes")
        assert cmd == '--request-changes 1 --reason "1=CI is red (lint); please fix the failing checks."'
        try:
            act.plan(env.queue, args(request_changes=[1]))
            raise AssertionError("sent back an empty review")
        except act.ActError as exc:
            assert "nothing to send back" in str(exc) and "--reason 1=" in str(exc)
        p = act.plan(env.queue, args(request_changes=[1], reason=["1=CI is red (lint); please fix the failing checks."]))
        body = p.steps[0].args["body"]
        assert body.startswith("CI is red (lint); please fix the failing checks.") and "@claude F<n>" in body
        res = act.execute(p, env.gh, queue=env.queue)
        assert res[0].ok and env.writes()[0]["body"] == {"event": "REQUEST_CHANGES", "body": body}
    finally:
        env.close()


def test_the_merge_preflight_refuses_a_review_it_cannot_read_whole():
    """The preflight's re-read goes through the same collector, so a split v2
    review now comes back joined. Two ways it can still be unreadable, and
    neither may merge: a page the `k/N` markers promise that GitHub did not
    return, and a card whose own tally declares more findings than its
    sections parsed into (pulumi/docs#21490)."""
    import test_collect as tc  # noqa: PLC0415

    pages = tc.legacy_pages(total=3)
    env = Env([stampable(1, comments=[comment(pages[0])], labels=["review:no-blockers", "domain:docs"])])
    try:
        s = act.Step("stamp", 1, {"merge": True}, expect_head=row(env.queue, 1)["head"]["sha"])
        ok, msg, _ = act.preflight(env.gh, s)
        assert ok is False and "page(s) 2, 3 could not be read" in msg, msg
        # and a step's own /resolve lines are no answer to a review with holes
        s.args["resolves"] = ["/resolve F1 refuted: checked"]
        ok, msg, _ = act.preflight(env.gh, s)
        assert ok is False and "could not be read" in msg, msg
    finally:
        env.close()

    # One page, stamped 1/1, so nothing is missing — but its tally says three
    # 🚨 and its sections hold none.
    page1 = pages[0].replace("<!-- CLAUDE_REVIEW 1/3 -->", "<!-- CLAUDE_REVIEW 1/1 -->")
    env = Env([stampable(1, comments=[comment(page1)], labels=["review:no-blockers", "domain:docs"])])
    try:
        s = act.Step("stamp", 1, {"merge": True}, expect_head=row(env.queue, 1)["head"]["sha"])
        ok, msg, _ = act.preflight(env.gh, s)
        assert ok is False and "declares more findings than its sections parsed into" in msg, msg
        # approve-only never reaches the check: it merges nothing
        ok, _, _ = act.preflight(env.gh, act.Step("stamp", 1, {"merge": False},
                                                  expect_head=row(env.queue, 1)["head"]["sha"]))
        assert ok
    finally:
        env.close()

#!/usr/bin/env python3
"""Tests for analyze.py — one fixture per stamp gate, the verdict order,
collision clustering (overlap vs same-file), directional conflicts against
a content tree with an `aliases:` block, duplicates, stale dates, stale
brief bullets, self-accept, and the judgments merge.

Runs under pytest and standalone via `analyze.py --self-test`. No pytest
fixtures. PRs are built with test_collect.pr_spec()/make_snapshot() and
collected over the snapshot backend, so the analyzer always sees the exact
record collect.py writes.
"""

from __future__ import annotations

import json
import copy
import sys
import tempfile
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import analyze  # noqa: E402
import collect  # noqa: E402
import pr_review_config  # noqa: E402
import routing  # noqa: E402
from gh_client import GhClient  # noqa: E402
import test_collect as tc  # noqa: E402
from test_collect import HEAD_V3, V3_AUTHOR, V3_BRIEF, comment, make_snapshot, patch_for, pr_spec  # noqa: E402

CONFIG = routing.validate_raw(routing._CANNED_CONFIG)[0]
TODAY = date(2026, 9, 15)
CLEAN_AUTHOR = (
    "<!-- CLAUDE_REVIEW 1/1 -->\n<!-- CLAUDE_REVIEW_AUTHOR -->\n"
    f"<!-- CLAUDE_REVIEW_HEAD {HEAD_V3} -->\n"
    "## Author action guide v1 — nothing blocks merge\n\n"
    "> [!NOTE]\n> Nothing here blocks merge.\n\n"
    "_Fixes one line of wording on the stacks page._\n\n"
    "### 🚨 Fix or disagree\n\n_Nothing to fix — this section is empty._\n\n"
    "### ❓ Questions for you\n\n_No open questions for you._\n\n"
    "📎 **Full evidence:** [trail](https://example.invalid/evidence).\n\n"
    "<!-- REVIEW_STATE {\"findings\":{},\"high_water\":4,\"schema\":1} -->\n"
    "<sub>Review v1 · updated 2026-09-01T00:00:00Z · head commit aaaabbbb</sub>\n"
)
CLEAN_BRIEF = "<!-- CLAUDE_REVIEW_BRIEF -->\n## Reviewer's guide v1\n\n> [!NOTE]\n> **What this PR changes:**\n>\n> - Fixes `old line` wording\n\n### ⚠️ Check these before approving\n\n_Nothing needs a human eye beyond the rubber-stamp list below._\n\n### ✅ What you can rubber-stamp\n\n- **Facts:** none.\n"


ALL_LANES = sorted(routing.SUBJECTS)


def cfg(**kw) -> pr_review_config.UserConfig:
    return pr_review_config.parse_config({"me": kw.pop("me", ALL_LANES), **kw})


def stampable(number: int = 100, **over) -> dict:
    """A PR that passes every stamp gate; override one field per test."""
    base = dict(
        labels=["review:no-blockers", "domain:docs"],
        comments=[comment(CLEAN_BRIEF), comment(CLEAN_AUTHOR)],
        head_sha=HEAD_V3,
        mergeable_state="clean",
        body="### Proposed changes\n\nFixes one line of wording on the stacks page so the example reads correctly.",
    )
    base.update(over)
    return pr_spec(number, **base)


NO_ALIASES: frozenset = frozenset()


def fresh(number: int, **over) -> dict:
    """`stampable` with its own head SHA and a review card written against
    it, so a batch of rows never shares the per-head snapshots (check runs,
    workflow runs): with everything at HEAD_V3, the last row written wins
    for all of them."""
    sha = f"{number:040x}"
    over.setdefault("head_sha", sha)
    over.setdefault("comments", [comment(CLEAN_BRIEF), comment(CLEAN_AUTHOR.replace(HEAD_V3, sha))])
    over.setdefault("title", f"Change page {number}")
    over.setdefault("files", [_file(f"content/docs/p{number}.md", ["x"], ["o"])])
    return stampable(number, **over)


def run(specs: list[dict], *, config=CONFIG, aliases=NO_ALIASES, repo_root=None, teams=None, my_teams=None, **kw) -> dict:
    """Collect + analyze the specs over a snapshot. `aliases=None` computes
    the alias map from `repo_root`; the default is an empty set. `teams`
    stands in for collect's GitHub team lookup (unreadable by default), and
    `my_teams` for the approver's memberships."""
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        make_snapshot(root, specs)
        gh = GhClient("pulumi/docs", "snapshot", snapshot_dir=root)
        q = collect.collect(gh, cache_dir=None, repo_root=repo_root or root, workers=1, numbers=[s["number"] for s in specs])
        if teams is not None:
            q["teams"] = teams
        if my_teams is not None:
            q["my_teams"] = my_teams
        return analyze.analyze(q, kw.pop("cfg", cfg()), config=config, repo_root=repo_root or root,
                               aliases=(None if aliases is None else set(aliases)), today=TODAY, **kw)


def row(q: dict, number: int) -> dict:
    return next(p for p in q["prs"] if p["number"] == number)


# ---- hunks / ranges --------------------------------------------------------


def test_parse_hunks_tracks_line_numbers():
    patch = "@@ -10,3 +10,4 @@\n ctx\n-old\n+new one\n+new two\n ctx2"
    h = analyze.parse_hunks(patch)
    assert h[0]["removed"] == [(11, "old")] and h[0]["added"] == [(11, "new one"), (12, "new two")]
    assert analyze.parse_hunks(None) == [] and analyze.parse_hunks("garbage") == []


def test_touched_lines_and_adjacency_overlap():
    a = analyze.touched_lines("@@ -10,7 +10,7 @@\n a\n b\n c\n-d\n+D\n e\n f\n g")
    assert a == {13}
    far = analyze.touched_lines("@@ -13,7 +13,7 @@\n a\n b\n c\n-x\n+X\n e\n f\n g")  # line 16
    near = analyze.touched_lines("@@ -11,7 +11,7 @@\n a\n b\n c\n-x\n+X\n e\n f\n g")  # line 14, adjacent
    assert analyze.lines_overlap(a, far) is False and analyze.lines_overlap(a, near) is True and analyze.lines_overlap(a, a) is True
    assert analyze.touched_lines("@@ -20,3 +20,4 @@\n a\n+new\n b\n c") == {20, 21}  # a pure insertion marks where it lands
    assert analyze.lines_overlap(None, a) is True  # binary / whole file collides with anything
    # two edits in one hunk with a line between them do not touch the middle line
    two = analyze.touched_lines("@@ -10,5 +10,5 @@\n-a\n+A\n b\n-c\n+C\n d\n e")
    assert two == {10, 12} and analyze.lines_overlap(two, {11}) is True and analyze.lines_overlap(two, {14}) is False


# ---- the stamp bar, one gate at a time ---------------------------------------


def test_stamp_when_every_gate_passes():
    q = run([stampable()])
    p = row(q, 100)
    assert p["verdict"] == "stamp", p["reasons"]
    assert p["actions"][0]["cmd"] == "--stamp 100"
    assert p["domains"] == ["docs"] and p["owners"]["docs"]["role"] == "docs-guild"
    assert q["counts"]["stamp"] == 1


def _judge_because(reason_prefix: str, **over):
    q = run([stampable(**over)])
    p = row(q, 100)
    assert p["verdict"] == "judge", (p["verdict"], p["reasons"])
    assert any(r.startswith(reason_prefix) for r in p["reasons"]), p["reasons"]
    return p


def test_gate_label_trivial_is_not_enough():
    _judge_because("label:review:trivial", labels=["review:trivial"])


def test_gate_open_warning_rows():
    p = _judge_because("warnings:1:F4", comments=[comment(V3_BRIEF), comment(CLEAN_AUTHOR)])
    assert p["open_warning_ids"] == ["F4"]
    # both stamp buttons, then the send-back: a row never hides whether
    # approving also merges.
    assert [a["id"] for a in p["actions"][:3]] == ["stamp", "stamp-no-merge", "request-changes"]


def test_open_blockers_block_the_row_they_do_not_merely_demote_it():
    """An unanswered 🚨 is "can't merge regardless", so the row lands in the
    one lane --force never reaches. Demoting it to `judge` is what let
    #21482 and #21549 merge over their open findings."""
    q = run([stampable(comments=[comment(CLEAN_BRIEF), comment(V3_AUTHOR)])])
    p = row(q, 100)
    assert p["verdict"] == "blocked", (p["verdict"], p["reasons"])
    assert any(r.startswith("outstanding:3") for r in p["reasons"]), p["reasons"]
    assert "outstanding:3" in p["blockers"], p["blockers"]
    assert set(p["open_blocker_ids"]) == {"F1", "F2", "F3"}
    # blocked, but not a dead end: the row offers the send-back.
    assert "request-changes" in [a["id"] for a in p["actions"]], p["actions"]
    # and no stamp button, because there is nothing here to approve yet.
    assert not [a["id"] for a in p["actions"] if a["id"].startswith("stamp")], p["actions"]
    # A workflow-authored row (pulumi-bot's content-review lane — #21549's own
    # shape) has nobody to send it back to, so it offers the close instead.
    gen = row(run([stampable(comments=[comment(CLEAN_BRIEF), comment(V3_AUTHOR)],
                             author="pulumi-bot", author_type="User")]), 100)
    assert gen["verdict"] == "blocked" and "author:generated" in gen["reasons"], gen["reasons"]
    ids = [a["id"] for a in gen["actions"]]
    assert "close" in ids and "request-changes" not in ids, gen["actions"]


def test_gate_self_accepted_disposition():
    state = '<!-- REVIEW_STATE {"findings":{"F2":{"disposition":"accepted","note":"will fix later","actor":"workprentice[bot]","sha":"","bulk":false,"updated_at":"2026-09-01T00:00:00Z"}},"high_water":4,"schema":1} -->'
    body = CLEAN_AUTHOR.replace('<!-- REVIEW_STATE {"findings":{},"high_water":4,"schema":1} -->', state)
    p = _judge_because("self-accepted:F2", comments=[comment(CLEAN_BRIEF), comment(body)])
    assert p["self_accepted_ids"] == ["F2"]
    # a maintainer's disposition is not self-accepted
    q = run([stampable(comments=[comment(CLEAN_BRIEF), comment(body.replace("workprentice[bot]", "cnunciato"))])])
    assert row(q, 100)["self_accepted_ids"] == []


def test_the_stamp_buttons_say_whether_approving_merges():
    def page(n, **kw):
        return stampable(n, title=f"Change page {n}", files=[{"filename": f"content/docs/p{n}.md", "status": "modified",
                                                              "additions": 1, "deletions": 1,
                                                              "patch": patch_for(["new line"], lines_removed=["old line"])}], **kw)

    q = run([page(1), page(2, author="jdoe", author_type="User")])
    bot, human = row(q, 1), row(q, 2)
    assert [(a["id"], a["label"], a["cmd"]) for a in bot["actions"][:2]] == [
        ("stamp", "approve & merge", "--stamp 1"), ("stamp-no-merge", "approve, don't merge", "--stamp 1:no-merge")]
    # a person's PR is theirs to merge: approval is the default, merging opts in
    assert [(a["id"], a["label"], a["cmd"]) for a in human["actions"][:2]] == [
        ("stamp", "approve, no merge", "--stamp 2"), ("stamp-merge", "approve & merge", "--stamp 2:merge")]
    card = next(c for c in q["do_next"] if c["kind"] == "stamp")
    assert card["say"] == "#1 and #2 pass every gate."
    assert "#2 is human-authored, so approval stops there" in card["does"] and card["label"] == "approve the set"
    # judge rows carry the same pair, as-is
    j = row(run([page(3, labels=["review:trivial", "domain:docs"])]), 3)
    assert [(a["id"], a["cmd"]) for a in j["actions"][:2]] == [
        ("stamp", "--stamp 3 --force"), ("stamp-no-merge", "--stamp 3:no-merge --force")]
    assert j["actions"][0]["label"] == "approve as-is & merge"


def test_a_generated_row_closes_instead_of_going_back_to_its_author():
    # pulumi-bot opens the content-review and glow-up PRs from a workflow
    # run: a changes-requested review would sit there forever.
    q = run([stampable(labels=["review:trivial", "domain:docs"], author="pulumi-bot", author_type="User")])
    p = row(q, 100)
    assert p["verdict"] == "judge" and "author:generated" in p["reasons"]
    ids = [a["id"] for a in p["actions"]]
    assert "request-changes" not in ids
    assert [a["cmd"] for a in p["actions"] if a["id"] == "close"] == ["--close 100"]
    assert [a["label"] for a in p["actions"] if a["id"] == "close"] == ["close it out"]
    # the model's send-back recommendation becomes a close, and the opening
    # card says so rather than promising an author who will never answer.
    analyze.merge_judgments(q, {100: {"recommended": "request-changes"}})
    assert p["recommended"] == "close"
    card = next(c for c in q["do_next"] if c["kind"] == "close")
    assert card["cmd"] == "--close 100" and "#100 was opened by a workflow run" in card["say"]
    assert "the lane re-queues the page" in card["does"].lower() and card["targets"] == {"100": "--close 100"}
    assert not any(c["kind"] == "request-changes" for c in q["do_next"])


def test_errored_review_is_blocked_with_rerun_and_an_absent_one_offers_it():
    p = row(run([stampable(labels=["review:error", "domain:docs"])]), 100)
    assert p["verdict"] == "blocked" and "review:error" in p["blockers"]
    assert [a["cmd"] for a in p["actions"] if a["id"] == "rerun"] == ["--rerun 100"]
    p = row(run([stampable(labels=["review:trivial", "domain:docs"], comments=[])]), 100)
    assert p["verdict"] == "judge" and "review:absent" in p["reasons"]
    assert [a["label"] for a in p["actions"] if a["id"] == "rerun"] == ["run a full review"]
    # in-progress is usually a wait, but a crashed run leaves the label with
    # no run behind it (test_handoff_guard.py), so the fresh review is offered
    p = row(run([stampable(labels=["review:in-progress", "domain:docs"])]), 100)
    assert p["verdict"] == "blocked" and [a["cmd"] for a in p["actions"] if a["id"] == "rerun"] == ["--rerun 100"]


def test_gate_stale_review_is_blocked_with_refresh():
    q = run([stampable(head_sha="f" * 40)])
    p = row(q, 100)
    assert p["verdict"] == "blocked" and "review:stale" in p["reasons"]
    assert any(a["cmd"] == "--refresh 100" for a in p["actions"])
    # a head moved only by a base merge (what --unblock does) keeps the review
    q = run([stampable(head_sha="f" * 40, commits=[{"sha": HEAD_V3, "message": "x"}, {"sha": "f" * 40, "message": "Merge master", "parents": 2}])])
    p = row(q, 100)
    assert p["verdict"] == "stamp" and "review:base-merged" in p["reasons"] and "review:stale" not in p["reasons"]


def test_gate_mergeable_dirty_is_blocked_with_unblock():
    q = run([stampable(mergeable_state="dirty")])
    p = row(q, 100)
    assert p["verdict"] == "blocked" and any(a["cmd"] == "--unblock 100" for a in p["actions"])


def test_gate_mergeable_blocked_state_still_stamps():
    assert row(run([stampable(mergeable_state="blocked")]), 100)["verdict"] == "stamp"


def test_gate_checks_red_is_blocked():
    q = run([stampable(check_runs=[{"name": "lint", "status": "completed", "conclusion": "failure"}])])
    p = row(q, 100)
    assert p["verdict"] == "blocked" and "checks:red:lint" in p["reasons"]


def test_gate_changes_requested_is_blocked():
    q = run([stampable(reviews=[{"user": {"login": "cnunciato", "type": "User"}, "state": "CHANGES_REQUESTED", "submitted_at": "2026-09-12T00:00:00Z"}])])
    assert row(q, 100)["verdict"] == "blocked"


def test_gate_owner_not_mine_routes():
    q = run([stampable()], cfg=cfg(me=["blog"]))
    p = row(q, 100)
    assert p["verdict"] == "route" and "route:docs-guild" in p["reasons"]
    assert row(run([stampable()], cfg=cfg(me=["docs"])), 100)["verdict"] == "stamp"
    # teams unreadable here, so the config's team is the target, marked unchecked
    assert p["actions"][0]["cmd"] == "--route 100:@pulumi/docs-guild" and "route:team-unverified" in p["reasons"]
    # the lane is a default, not a lock: "approve anyway", both merge choices
    assert [a["cmd"] for a in p["actions"] if a["id"].startswith("stamp")] == ["--stamp 100 --force", "--stamp 100:no-merge --force"]


def test_gate_new_blog_post():
    files = [{"filename": "content/blog/new-post/index.md", "status": "added", "additions": 3, "deletions": 0,
              "patch": patch_for(["---", "title: x", "date: 2026-09-15", "---"], context=[])}]
    _judge_because("blog:new-post", files=files, labels=["review:no-blockers", "domain:blog"])


def test_gate_infra_shape_needs_include_infra():
    files = [{"filename": "layouts/partials/x.html", "status": "modified", "additions": 1, "deletions": 1,
              "patch": patch_for(["<b>"], lines_removed=["<i>"])}]
    _judge_because("shape:infra", files=files)
    q = run([stampable(files=files)], include_infra=True)
    assert row(q, 100)["verdict"] == "stamp"


def test_gate_size():
    files = [{"filename": "content/docs/iac/x.md", "status": "modified", "additions": 30, "deletions": 20,
              "patch": patch_for([f"l{i}" for i in range(30)], lines_removed=[f"o{i}" for i in range(20)])}]
    _judge_because("size:50>=40", files=files)
    assert row(run([stampable(files=files)], cfg=cfg(stamp_max_lines=100)), 100)["verdict"] == "stamp"


def test_gate_heightened_scrutiny_caps_at_judge():
    p = _judge_because("scrutiny:heightened", author="human-dev", author_type="User",
                       commits=["Fix\n\nCo-Authored-By: Claude <noreply@anthropic.com>"])
    assert "ai-suspect:trailer:claude" in p["reasons"]


def test_bot_trailers_do_not_trip_scrutiny():
    q = run([stampable(commits=["Fix\n\nCo-Authored-By: Claude <noreply@anthropic.com>"])])
    assert row(q, 100)["verdict"] == "stamp"


def test_gate_stances_only_with_strict():
    brief = CLEAN_BRIEF + "\n#### Editorial stances introduced by this PR\n\n- takes a side\n"
    assert row(run([stampable(comments=[comment(brief), comment(CLEAN_AUTHOR)])]), 100)["verdict"] == "stamp"
    p = row(run([stampable(comments=[comment(brief), comment(CLEAN_AUTHOR)])], strict_stances=True), 100)
    assert p["verdict"] == "judge" and "stances:present" in p["reasons"]


def test_gate_stale_blog_date():
    files = [{"filename": "content/blog/old-post/index.md", "status": "modified", "additions": 1, "deletions": 1,
              "patch": patch_for(["date: 2026-09-01"], lines_removed=["date: 2026-08-01"])}]
    p = _judge_because("blog:stale-date:2026-09-01", files=files, labels=["review:no-blockers", "domain:blog"])
    assert p["files"][0]["blog_date"] == "2026-09-01"
    # an old post touched for a link fix is not a backdate: the diff doesn't set its date
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        post = root / "content" / "blog" / "old-post" / "index.md"
        post.parent.mkdir(parents=True)
        post.write_text("---\ntitle: Old\ndate: 2024-01-01\n---\nbody [x](/docs/)\n")
        link_fix = [{"filename": "content/blog/old-post/index.md", "status": "modified", "additions": 1, "deletions": 1,
                     "patch": patch_for(["body [x](/docs/new/)"], lines_removed=["body [x](/docs/)"])}]
        q = run([stampable(files=link_fix, labels=["review:no-blockers", "domain:blog"])], repo_root=root)
    p = row(q, 100)
    assert p["files"][0]["blog_date"] == "2024-01-01" and not any(r.startswith("blog:stale-date") for r in p["reasons"])


def test_legacy_surface_freshness_and_low_confidence():
    import sentinel  # noqa: PLC0415
    legacy = (HERE.parent.parent / ".claude/commands/docs-review/scripts/testdata/pr20079-pinned-review.md.txt").read_text()
    reviewed = sentinel.HISTORY_SHA_RE.findall(legacy)[-1]  # no CLAUDE_REVIEW_HEAD on a legacy body: history sha
    q = run([stampable(comments=[comment(legacy)], head_sha=(reviewed + "0" * 40)[:40])])
    p = row(q, 100)
    assert p["review"]["surface"] == "v2" and p["review"]["status"] == "CURRENT"
    assert p["verdict"] == "stamp", p["reasons"]  # the fixture's only bucket is 💡 pre-existing
    assert row(run([stampable(comments=[comment(legacy)], head_sha="f" * 40)]), 100)["verdict"] == "blocked"
    # legacy ⚠️ low-confidence items count as open warnings until dispositioned
    fake = {"review": {"surface": "v2", "items": [{"id": "low:L12", "bucket": "low"}, {"id": "low:L40", "bucket": "low", "disposition": "accepted"},
                                                   {"id": "outstanding:L3", "bucket": "outstanding", "blocking": True}]}}
    assert analyze.open_warnings(fake) == ["low:L12"] and analyze.open_blockers(fake) == ["outstanding:L3"]


def test_triage_prose_and_absent_are_judge_not_blocked():
    prose = comment("<!-- TRIAGE_PROSE -->\n- [spelling] teh", "github-actions[bot]")
    q = run([pr_spec(1, labels=["review:trivial", "review:prose-flagged"], comments=[prose]), pr_spec(2)])
    assert row(q, 1)["verdict"] == "judge" and "review:triage-prose" in row(q, 1)["reasons"]
    assert row(q, 2)["verdict"] == "judge" and "review:absent" in row(q, 2)["reasons"]


def test_in_progress_and_error_are_blocked():
    q = run([stampable(labels=["review:in-progress"]), stampable(101, labels=["review:error"])])
    assert row(q, 100)["verdict"] == "blocked" and row(q, 101)["verdict"] == "blocked"


# ---- cross-PR ----------------------------------------------------------------


def _file(path, added, removed=None, old_start=10):
    return {"filename": path, "status": "modified", "additions": len(added), "deletions": len(removed or []),
            "patch": patch_for(added, lines_removed=removed, old_start=old_start)}


def test_collision_overlap_vs_same_file_and_merge_order():
    a = stampable(1, title="Fix the intro", files=[_file("content/docs/a.md", ["x"], ["o"], old_start=10)])
    b = stampable(2, title="Reword the intro", files=[_file("content/docs/a.md", ["y"], ["o"], old_start=10)])
    c = stampable(3, title="Trim the appendix", files=[_file("content/docs/a.md", ["z"], ["p"], old_start=200)])
    d = stampable(4, title="Touch another page", files=[_file("content/docs/other.md", ["w"])])
    q = run([a, b, c, d])
    assert len(q["clusters"]) == 1
    cl = q["clusters"][0]
    assert cl["prs"] == [1, 2, 3] and cl["kind"] == "overlap"
    kinds = {(p["a"], p["b"]): p["kind"] for p in cl["pairs"]}
    assert kinds[(1, 2)] == "overlap" and kinds[(1, 3)] == "same-file" and kinds[(2, 3)] == "same-file"
    assert row(q, 1)["verdict"] == "judge" and "cluster:C1:overlap:1/3" in row(q, 1)["reasons"]
    assert row(q, 2)["verdict"] == "judge" and "cluster:C1:overlap:2/3" in row(q, 2)["reasons"]
    assert row(q, 3)["verdict"] == "stamp" and "cluster:C1:same-file" in row(q, 3)["reasons"]
    assert row(q, 4)["verdict"] == "stamp" and cl["merge_order"] == [1, 2, 3]
    assert cl["recommendation"]["kind"] == "chain" and cl["recommendation"]["first"] == 1 and cl["recommendation"]["next"] == 2
    # the chain card is the one command act.py runs through the stamp gates;
    # the two rows it covers defer to it rather than mapping to row buttons
    chain = next(d for d in q["do_next"] if d["kind"] == "chain")
    assert chain["cmd"] == "--chain C1" and chain["targets"] == {} and chain["claims"] == [1, 2]
    assert chain["label"] == "approve & merge #1" and chain["merges"] is True  # a bot lead merges on stamp
    q = run([stampable(1, title="Fix the intro", author="jdoe", author_type="User", files=[_file("content/docs/a.md", ["x"], ["o"], old_start=10)]), b])
    chain = next(d for d in q["do_next"] if d["kind"] == "chain")
    assert chain["label"] == "approve #1, then unblock the next" and chain["merges"] is False
    assert "the author merges it" in chain["does"] and chain["cmd"] == "--chain C1"


def test_directional_conflict_against_aliases_block():
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        page = root / "content" / "docs" / "new" / "_index.md"
        page.parent.mkdir(parents=True)
        page.write_text("---\ntitle: New\naliases:\n  - /docs/old/\n---\nbody\n")
        assert analyze.alias_only_urls(root) == {"/docs/old/"}
        adds = stampable(1, title="Add a link", files=[_file("content/blog/p/index.md", ["see [x](/docs/old/) now"])])
        removes = stampable(2, title="Repoint a link", files=[_file("content/blog/q/index.md", ["see [x](/docs/new/)"], ["see [x](/docs/old/)"])])
        q = run([adds, removes], aliases=None, repo_root=root)
    assert q["directional"] == [{"path": "/docs/old/", "adds_links_pr": 1, "removes_links_pr": 2, "theirs": False}]
    assert "directional:#2:/docs/old/" in row(q, 1)["reasons"] and row(q, 1)["verdict"] == "judge"
    assert row(q, 2)["verdict"] == "stamp"


def test_duplicate_candidates():
    a = stampable(10, title="Remove residual unsourced BMW claims", created_at="2026-09-10T10:00:00Z")
    b = stampable(11, title="Remove residual unsourced BMW claim", created_at="2026-09-10T10:05:00Z")
    c = stampable(12, title="Something else entirely", created_at="2026-09-10T10:06:00Z")
    q = run([a, b, c])
    assert [(d["newer"], d["older"]) for d in q["duplicates"]] == [(11, 10)]
    p = row(q, 11)
    assert p["verdict"] == "judge" and "duplicate:#10" in p["reasons"]
    assert any(a["cmd"] == "--close 11 --superseded-by 10" for a in p["actions"])


def test_stale_brief_summary_tokens():
    brief = CLEAN_BRIEF.replace("- Fixes `old line` wording", "- Downgrades `ES2022` to `ES2017`\n> - Bumps the count to 300\n> - Mentions `old line`")
    p = row(run([stampable(comments=[comment(brief), comment(CLEAN_AUTHOR)])]), 100)
    stale = [r for r in p["reasons"] if r.startswith("brief:stale-summary:")]
    assert stale == ["brief:stale-summary:ES2022", "brief:stale-summary:ES2017", "brief:stale-summary:300"]
    assert p["verdict"] == "stamp"  # advisory, never a gate


def test_desc_findings():
    p = row(run([stampable(body="### Proposed changes\n\nUpdates `content/docs/iac/x.md` and `content/docs/nope.md`; ran `scripts/lint.sh` afterwards.")]), 100)
    assert [r for r in p["reasons"] if r.startswith("desc:")] == ["desc:stale:path:content/docs/nope.md"]
    assert "desc:empty" in row(run([stampable(body="### Proposed changes\n\n<!-- template -->\n")]), 100)["reasons"]


def test_one_cluster_chip_per_row_and_consolidate_for_bot_sweeps():
    specs = [stampable(i, title=f"Sweep {i}", files=[_file("content/docs/a.md", [f"x{i}"], ["o"], old_start=10)]) for i in range(1, 10)]
    q = run(specs)
    p = row(q, 1)
    codes = [r for r in p["reasons"] if r.startswith(("cluster:", "collision:"))]
    assert codes == ["cluster:C1:overlap:1/9"]
    c = q["clusters"][0]
    assert c["recommendation"]["kind"] == "consolidate" and c["recommendation"]["on"] == 9
    assert c["recommendation"]["cmd"].startswith("--request-changes 9 --reason ")
    assert q["do_next"][0]["kind"] == "consolidate" and q["do_next"][0]["label"].startswith("send #")


# ---- judgments / filters -------------------------------------------------------


def test_merge_judgments_never_lowers_verdict():
    q = run([stampable(mergeable_state="dirty"), stampable(101, comments=[comment(V3_BRIEF), comment(CLEAN_AUTHOR)])])
    j = {"100": {"recommended": "stamp", "judgments": [{"finding_id": "F1", "decision": "x"}]},
         101: {"recommended": "stamp", "fix_draft": {"kind": "description", "body": "new body"}}}
    analyze.merge_judgments(q, j)
    assert row(q, 100)["verdict"] == "blocked" and row(q, 100)["judgments"][0]["finding_id"] == "F1"
    assert "recommended" not in row(q, 100)
    p = row(q, 101)
    assert p["verdict"] == "judge" and p["recommended"] == "stamp" and p["fix_draft"]["body"] == "new body"
    analyze.merge_judgments(q, {101: {"recommended": "request-changes"}})
    assert p["recommended"] == "request-changes"
    assert any(a["cmd"] == "--fix 101" for a in p["actions"])


def test_apply_filters_and_owner_specs():
    q = run([stampable(), stampable(101, labels=["review:no-blockers", "domain:blog"],
                                    files=[_file("content/blog/p/index.md", ["x"], ["o"])])])
    analyze.apply_filters(q, domains=["blog"])
    assert [p["number"] for p in q["prs"]] == [101]
    assert analyze.lanes_for_owner("any", CONFIG, ["docs"]) is None
    assert analyze.lanes_for_owner("marketing", CONFIG, ["docs"]) == {"blog", "website", "frontend"}
    assert analyze.lanes_for_owner("@TODO-tools-lead", CONFIG, ["docs"]) == {"infra", "other"}
    assert analyze.lanes_for_owner("@nobody", CONFIG, ["docs"]) == set()


def test_every_pr_gets_exactly_one_verdict_over_real_fixtures():
    td = HERE.parent.parent / ".claude/commands/docs-review/scripts/testdata"
    specs = []
    for i, prn in enumerate((21585, 21603), 1):
        author = (td / f"normalize-pr{prn}-author.md.txt").read_text()
        brief = (td / f"normalize-pr{prn}-brief.md.txt").read_text()
        specs.append(pr_spec(i, labels=["review:no-blockers"], comments=[comment(brief), comment(author)]))
    q = run(specs)
    for p in q["prs"]:
        assert p["verdict"] in analyze.VERDICTS and p["reasons"]
    assert sum(q["counts"].values()) == 2


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
        print(f"{failures} analyze test(s) failed", file=sys.stderr)
        return 1
    print("all analyze self-tests passed")
    return 0


if __name__ == "__main__":
    sys.exit(run_standalone())


# ---- handed-off ------------------------------------------------------------------


def test_handed_off_when_a_human_who_is_not_me_is_requested():
    q = run([stampable(1, requested_users=["cnunciato"]),
             stampable(2, title="Mine too", requested_users=["cnunciato", "CamSoper"], files=[_file("content/docs/b.md", ["x"])]),
             stampable(3, title="Nobody", files=[_file("content/docs/c.md", ["x"])]),
             stampable(4, title="Bot only", requested_users=[{"login": "copilot-pull-request-reviewer[bot]", "type": "Bot"}],
                       files=[_file("content/docs/d.md", ["x"])])])
    assert row(q, 1)["handed_off"] is True and row(q, 1)["handed_off_to"] == ["@cnunciato"]
    assert "handed-off:@cnunciato" in row(q, 1)["reasons"]
    assert row(q, 2)["handed_off"] is False  # I'm requested too
    assert row(q, 3)["handed_off"] is False and row(q, 4)["handed_off"] is False
    assert q["counts"]["handed-off"] == 1 and q["counts"]["stamp"] == 3


def test_handed_off_teams_map_through_routing():
    q = run([stampable(1, requested_teams=["docs-guild"]),
             stampable(2, title="Marketing's", requested_teams=["docs-marketing-review"], files=[_file("content/docs/b.md", ["x"])])],
            cfg=cfg(me=["docs"]))
    assert row(q, 1)["handed_off"] is False  # docs-guild owns a lane in me
    assert row(q, 2)["handed_off_to"] == ["@docs-marketing-review"]
    assert analyze.team_lanes("docs-tools", CONFIG) == {"infra", "other"} and analyze.team_lanes("nope", CONFIG) == set()


def test_collision_with_a_handed_off_pr_is_advisory():
    mine = stampable(1, title="Mine", files=[_file("content/docs/a.md", ["x"], ["o"], old_start=10)])
    theirs = stampable(2, title="Chris has it", requested_users=["cnunciato"], files=[_file("content/docs/a.md", ["y"], ["o"], old_start=10)])
    q = run([mine, theirs])
    p = row(q, 1)
    assert p["verdict"] == "stamp" and "cluster:C1:theirs" in p["reasons"]
    c = q["clusters"][0]
    assert c["handed_off"] == [2] and c["mine"] == [1] and c["merge_order"] == [1]
    assert c["recommendation"]["kind"] == "theirs"
    # the same pair with nobody requested still gates
    q = run([mine, stampable(2, title="Nobody", files=[_file("content/docs/a.md", ["y"], ["o"], old_start=10)])])
    assert row(q, 1)["verdict"] == "judge" and "cluster:C1:overlap:1/2" in row(q, 1)["reasons"]


def test_directional_conflict_with_a_handed_off_pr_is_theirs():
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        page = root / "content" / "docs" / "new" / "_index.md"
        page.parent.mkdir(parents=True)
        page.write_text("---\ntitle: New\naliases:\n  - /docs/old/\n---\nbody\n")
        adds = stampable(1, title="Add a link", files=[_file("content/blog/p/index.md", ["see [x](/docs/old/) now"])])
        removes = stampable(2, title="Repoint a link", requested_users=["cnunciato"],
                            files=[_file("content/blog/q/index.md", ["see [x](/docs/new/)"], ["see [x](/docs/old/)"])])
        q = run([adds, removes], aliases=None, repo_root=root)
    assert q["directional"][0]["theirs"] is True
    assert row(q, 1)["verdict"] == "stamp" and "directional:#2:/docs/old/:theirs" in row(q, 1)["reasons"]


LINK_MINUS = "See the [Typescript voting app](https://www.pulumi.com/docs/tutorials/aws/aws-ts-voting-app/) for details."
LINK_PLUS = "See the [TypeScript voting app](/dev/examples/aws-ts-voting-app/) for details."


def test_link_only_diff_masks_links_and_nothing_else():
    assert analyze.link_only_diff([_file("content/blog/p/index.md", [LINK_PLUS], [LINK_MINUS])])
    assert analyze.link_only_diff([_file("content/docs/a.md", ['<a href="/docs/new/">x</a>'], ['<a href="/docs/old/">x</a>'])])
    assert analyze.link_only_diff([_file("content/docs/a.md", ["Read /docs/iac/new/ first."], ["Read /docs/old/ first."])])
    assert analyze.link_only_diff([_file("content/blog/p/index.md", ["Write a TypeScript program. " + LINK_PLUS], ["Write a Typescript program. " + LINK_MINUS])])  # casing rides along
    # prose changed alongside the link, an unpaired line, an unchanged line, a missing patch, an empty diff
    assert not analyze.link_only_diff([_file("content/docs/a.md", ["Read [x](/b/) now."], ["Read [x](/a/) later."])])
    assert not analyze.link_only_diff([_file("content/docs/a.md", ["a", "[x](/b/)"], ["[x](/a/)"])])
    assert not analyze.link_only_diff([_file("content/docs/a.md", ["same"], ["same"])])
    assert not analyze.link_only_diff([{"filename": "a.png", "status": "modified", "additions": 0, "deletions": 0, "patch": None}])
    assert not analyze.link_only_diff([])


def test_link_only_blog_sweep_is_mine_by_default_and_routes_when_configured():
    blog = dict(title="Fix stale links", labels=["review:no-blockers", "domain:blog"],
                files=[_file("content/blog/p/index.md", [LINK_PLUS], [LINK_MINUS])])
    lane = routing.validate_raw({**copy.deepcopy(routing._CANNED_CONFIG), "link_only": {"approval": "lane"}})[0]
    p = row(run([stampable(5, **blog)], cfg=cfg(me=["docs"])), 5)
    assert p["verdict"] == "stamp" and p["is_mine"] is True
    # the routing config carries any-team, so the row is everyone's on its own
    assert "shape:link-only" in p["reasons"] and "gate:any-team" in p["reasons"] and not any(r.startswith("route:") for r in p["reasons"])
    # under the lane policy the local setting is what takes it, and dropping
    # that setting routes it to the lane owner
    p = row(run([stampable(5, **blog)], cfg=cfg(me=["docs"]), config=lane), 5)
    assert p["verdict"] == "stamp" and "link-fixes:mine" in p["reasons"]
    p = row(run([stampable(5, **blog)], cfg=cfg(me=["docs"], link_fixes="route"), config=lane), 5)
    assert p["verdict"] == "route" and "shape:link-only" in p["reasons"] and "link-fixes:mine" not in p["reasons"]
    # a prose edit in the same sweep keeps the lane owner
    p = row(run([stampable(6, **{**blog, "files": [_file("content/blog/p/index.md", [LINK_PLUS, "new sentence"], [LINK_MINUS, "old sentence"])]})], cfg=cfg(me=["docs"])), 6)
    assert p["verdict"] == "route" and "shape:link-only" not in p["reasons"]


def test_a_summary_is_cut_at_a_boundary_not_mid_word():
    long = ("Daily link-checker follow-up for 2026-09-16. Four entries were reported (2 internal, 2 external). "
            "One was actionable; one was a false positive; two are already tracked by an existing issue.")
    out = analyze.clip(long, limit=120)
    assert out.endswith(".") and "existin…" not in out and len(out) <= 120
    assert analyze.clip("short enough") == "short enough"
    # no sentence in range: cut at a word, and mark the cut
    words = analyze.clip("word " * 80, limit=100)
    assert words.endswith("…") and not words.endswith("wor…")
    # the brief's own orientation sentence is never cut, however long
    brief = "_" + ("a sentence that runs on and on " * 12).strip() + "._"
    pr = {"review": {"author_body": f"## guide\n\n{brief}\n"}, "body": "", "title": "t"}
    assert analyze.one_line_summary(pr) == brief.strip("_")


def test_blocked_rows_get_a_card_so_the_hidden_ones_still_surface():
    # Blocked rows are filtered off the board by default. The ones with a
    # mechanical unblock still have to reach the approver, so each kind of
    # stuck gets one card naming its PRs.
    q = run([stampable(1, mergeable_state="dirty"),
             stampable(2, head_sha="f" * 40, files=[_file("content/docs/b.md", ["x"])]),
             stampable(3, labels=["review:error", "domain:docs"], files=[_file("content/docs/c.md", ["y"])])])
    kinds = {c["kind"]: c for c in q["do_next"]}
    assert kinds["unblock"]["say"] == "#1 is stuck behind a merge conflict."
    assert kinds["unblock"]["targets"] == {"1": "--unblock 1"} and "never resolved blind" in kinds["unblock"]["does"]
    assert kinds["refresh"]["say"].startswith("#2 is carrying a review that describes an older commit")
    assert kinds["rerun"]["targets"] == {"3": "--rerun 3"}


def test_a_link_only_sweep_is_any_approver_s_because_any_team_may_approve():
    # The routing config says any review team may approve a link-only sweep,
    # so the row is genuinely anyone's -- not a local override of a lane.
    sweep = _file("content/blog/p/index.md",
                  ["See [stacks](/docs/iac/concepts/stacks/) for the rest."],
                  ["See [stacks](https://www.pulumi.com/docs/concepts/stacks/) for the rest."])
    p = row(run([stampable(1, labels=["review:no-blockers", "domain:blog"], files=[sweep])], cfg=cfg(me=["docs"])), 1)
    assert "shape:link-only" in p["reasons"] and "gate:any-team" in p["reasons"]
    assert p["is_mine"] is True and "link-fixes:mine" not in p["reasons"]
    assert not any(r.startswith("route:") for r in p["reasons"])
    # with the lane policy instead, it is the local link_fixes setting again
    lane = routing.validate_raw({**copy.deepcopy(routing._CANNED_CONFIG), "link_only": {"approval": "lane"}})[0]
    p = row(run([stampable(2, labels=["review:no-blockers", "domain:blog"], files=[sweep])],
                cfg=cfg(me=["docs"]), config=lane), 2)
    assert "gate:any-team" not in p["reasons"] and "link-fixes:mine" in p["reasons"]


def test_a_mechanical_change_is_still_routed_to_its_lane():
    """There is no ungated row any more.

    A tags-only blog edit clears the mechanical bar, which used to resolve
    to no required role at all: the row got `gate:none`, went to whoever was
    looking, and the Sentinel asked nobody to approve it. That rested on the
    Sentinel being the merge gate — it isn't, and GitHub asked for a review
    regardless. `none` cells are a config error now, so mechanical and
    substantive route the same way and only the model review differs.
    """
    tags = _file("content/blog/p/index.md", ["tags: [kubernetes, aws]"], ["tags: [kubernetes]"])
    p = row(run([stampable(1, labels=["review:no-blockers", "domain:blog"], files=[tags])], cfg=cfg(me=["docs"])), 1)
    assert p["mechanical"] is True
    assert p["roles"] == ["marketing"]
    assert not any(r == "gate:none" for r in p["reasons"])
    # the substantive version of the same lane routes identically
    prose = _file("content/blog/p/index.md", ["A new sentence about stacks."], ["An old sentence about stacks."])
    q = row(run([stampable(2, labels=["review:no-blockers", "domain:blog"], files=[prose])], cfg=cfg(me=["docs"])), 2)
    assert q["roles"] == ["marketing"] and q["verdict"] == "route"


def test_no_row_ever_reports_an_empty_role_set():
    """The board-level form of "every PR is routed"."""
    for files in ([_file("content/docs/a.md", ["a typo fix"], ["a typo fxi"])],
                  [_file("scripts/lint/x.js", ["// new"], [])],
                  [_file("layouts/p.html", ["<div/>"], [])],
                  [_file("whatever.xyz", ["x"], [])]):
        q = run([stampable(3, labels=["review:no-blockers"], files=files)], cfg=cfg(me=["docs"]))
        assert row(q, 3)["roles"], files[0]["path"]


def test_no_config_file_takes_its_lanes_from_github_teams():
    # A first run with no ~/.pr-review.yml: the org chart answers "which
    # lanes are mine" better than claiming all of them.
    defaults = pr_review_config.parse_config({}, source="defaults")
    q = run([stampable(1), stampable(2, title="Blog", labels=["review:no-blockers", "domain:blog"],
                                     files=[_file("content/blog/p/index.md", ["x"])])],
            cfg=defaults, my_teams={"pulumi/docs-guild": True, "pulumi/docs-marketing-review": False,
                                    "pulumi/docs-tools": None})
    assert q["config"]["me"] == ["docs", "programs"] and q["config"]["source"] == "github-teams"
    assert row(q, 1)["is_mine"] is True and row(q, 2)["verdict"] == "route"
    # memberships unreadable: the old fallback stands, every lane is mine
    q = run([stampable(1)], cfg=pr_review_config.parse_config({}, source="defaults"),
            my_teams={"pulumi/docs-guild": None})
    assert set(q["config"]["me"]) == set(routing.SUBJECTS) and q["config"]["source"] == "defaults"


def test_route_targets_the_team_when_github_has_it_else_the_sla_person():
    q = run([stampable()], cfg=cfg(me=["blog"]), teams={"pulumi/docs-guild": True})
    p = row(q, 100)
    assert p["actions"][0]["cmd"] == "--route 100:@pulumi/docs-guild" and "route:no-team" not in p["reasons"]
    q = run([stampable()], cfg=cfg(me=["blog"]), teams={"pulumi/docs-guild": False})
    p = row(q, 100)
    assert p["actions"][0]["cmd"] == "--route 100:@TODO-owning-manager" and "route:no-team" in p["reasons"]
    # "can't read teams" is not "the team is missing": the config's team is
    # still the target, and the row says the check didn't run.
    q = run([stampable()], cfg=cfg(me=["blog"]), teams={"pulumi/docs-guild": None})
    p = row(q, 100)
    assert p["actions"][0]["cmd"] == "--route 100:@pulumi/docs-guild"
    assert "route:team-unverified" in p["reasons"] and "route:no-team" not in p["reasons"]


def test_do_next_lists_send_back_route_and_stamp():
    q = run([stampable(1), stampable(2, title="Blog", labels=["review:no-blockers", "domain:blog"], files=[_file("content/blog/p/index.md", ["x"])]),
             stampable(3, title="Judge me", comments=[comment(V3_BRIEF), comment(CLEAN_AUTHOR)], files=[_file("content/docs/c.md", ["x"])])],
            cfg=cfg(me=["docs"]))
    assert [d["kind"] for d in q["do_next"]] == ["route", "stamp"]
    analyze.merge_judgments(q, {3: {"recommended": "request-changes"}})  # rebuilds do_next itself
    kinds = [d["kind"] for d in q["do_next"]]
    assert kinds == ["request-changes", "route", "stamp"]
    assert q["do_next"][0]["cmd"] == "--request-changes 3" and q["do_next"][2]["cmd"] == "--stamp 1"
    # every card names the PRs it acts on and what pressing it does
    assert q["do_next"][2]["say"] == "#1 passes every gate." and "squash-merges" in q["do_next"][2]["does"]
    assert q["do_next"][0]["targets"] == {"3": "--request-changes 3"}
    assert q["do_next"][1]["cmd"].startswith("--route 2:@")


def test_a_row_summarizes_the_change_not_the_template_boilerplate():
    # A generated PR body's first surviving prose line is often a machine
    # note to a machine ("do not edit it"), which tells an approver nothing.
    body = (
        "> [!IMPORTANT]\n> Auto-merge is not armed.\n\n"
        "## Why this page\n\n"
        "_This section is composed deterministically from the selection queue; do not edit it._\n\n"
        "## Fixes applied\n\n"
        "| Claim | Source | Correction |\n| --- | --- | --- |\n"
        "| The SDK falls back to the CLI login | esc-sdk #137 | Rewrote the sentence to drop the CLI fallback. |\n\n"
        "## Findings not applied\n\n"
        "The items above are banked for the glow-up lane.\n"
    )
    pr = {"review": {"author_body": ""}, "body": body, "title": "Content review: python.md"}
    assert analyze.one_line_summary(pr) == "Rewrote the sentence to drop the CLI fallback."
    # with no such section, the boilerplate is still skipped for real prose
    pr = {"review": {"author_body": ""},
          "body": "_This section is composed deterministically from the selection queue; do not edit it._\n\nRewrites two links.\n",
          "title": "t"}
    assert analyze.one_line_summary(pr) == "Rewrites two links."


# ---- every verdict leaves a button --------------------------------------------


def assert_every_row_has_a_button(q: dict) -> None:
    """The invariant the 2026-09-17 audit was about: a `blocked` row with no
    action is a row nobody can move (#21598 sat invisible that way). The one
    exception is a row that is the author's turn (`waiting_on_author`), which
    the board groups with the handed-off ones rather than as a dead end. And
    a blocked row never carries a stamp: act.py refuses it, and one refusal
    used to sink the whole batch."""
    for p in q["prs"]:
        ids = [a["id"] for a in p.get("actions") or []]
        assert p["verdict"] in analyze.VERDICTS, p["number"]
        if p["verdict"] == "blocked" and not p.get("waiting_on_author"):
            assert ids, (p["number"], p["blockers"], p["reasons"])
        if p["verdict"] == "blocked":
            assert not any(i.startswith("stamp") for i in ids), (p["number"], ids)
        if p.get("author_self"):
            assert not any(i.startswith("stamp") or i == "request-changes" for i in ids), (p["number"], ids)
            assert "author:self" in p["reasons"]
        if p.get("waiting_on_author"):
            assert not any(i in analyze.DECISION_IDS for i in ids), (p["number"], ids)
        for a in p.get("actions") or []:
            assert a["cmd"].startswith("--"), a


def _red(name="lint"):
    return [{"name": name, "status": "completed", "conclusion": "failure"}]


CR = lambda who, at="2026-09-12T00:00:00Z", commit_id=None: {  # noqa: E731
    "user": {"login": who, "type": "User"}, "state": "CHANGES_REQUESTED", "submitted_at": at, "commit_id": commit_id}


def test_no_verdict_leaves_the_approver_without_a_button():
    specs = [
        fresh(1, mergeable_state="dirty"),
        fresh(2, title="Red CI", check_runs=_red()),
        fresh(3, title="Red CI, generated", check_runs=_red(), author="pulumi-bot", author_type="User"),
        stampable(4, title="Stale", head_sha="f" * 40, files=[_file("content/docs/d.md", ["x"])]),
        fresh(5, title="Errored", labels=["review:error", "domain:docs"]),
        fresh(6, title="Running", labels=["review:in-progress", "domain:docs"]),
        fresh(7, title="Their CR", reviews=[CR("cnunciato")]),
        stampable(8, title="Open findings", comments=[comment(CLEAN_BRIEF), comment(V3_AUTHOR)], files=[_file("content/docs/h.md", ["x"])]),
        fresh(9, title="Dependabot conflict", author="dependabot[bot]", mergeable_state="dirty", files=[_file("package.json", ["x"])]),
        fresh(10, title="Fork conflict", author="outsider", author_type="User", head_repo="outsider/docs", mergeable_state="dirty"),
        fresh(11, title="Mine, red", author="CamSoper", author_type="User", check_runs=_red()),
        fresh(12, title="Not my lane, dirty", labels=["review:no-blockers", "domain:blog"], mergeable_state="dirty",
              files=[_file("content/blog/p/index.md", ["A new sentence."], ["An old sentence."])]),
        fresh(13, title="Sent back, red", reviews=[CR("CamSoper")], check_runs=_red()),
        fresh(14, title="Clean"),
    ]
    q = run(specs, cfg=cfg(me=["docs"]))
    assert_every_row_has_a_button(q)
    assert q["counts"]["blocked"] == 12 and q["counts"]["stamp"] == 1 and q["counts"]["waiting-on-author"] == 1, q["counts"]
    assert {p["number"] for p in q["prs"] if p["verdict"] == "blocked" and not p["waiting_on_author"]} == {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
    assert row(q, 13)["waiting_on_author"] is True and [a["id"] for a in row(q, 13)["actions"]] == ["rerun-checks"]


REAL_QUEUE = HERE.parent.parent / ".pr-review-queue.json"


def test_the_real_queue_leaves_no_row_without_a_button():
    """Over the live queue when one is on disk (read-only; a copy is
    analyzed). Skipped silently where there is none (CI)."""
    if not REAL_QUEUE.exists():
        return
    q = json.loads(REAL_QUEUE.read_text())
    conf = q.get("config") or {}
    user_cfg = pr_review_config.parse_config({"me": conf.get("me") or ALL_LANES, "stamp_max_lines": conf.get("stamp_max_lines", 40),
                                              "stale_date_days": conf.get("stale_date_days", 3)}, source="file")
    q = analyze.analyze(q, user_cfg, config=routing.load_config(str(routing.DEFAULT_CONFIG_PATH)), aliases=None)
    assert_every_row_has_a_button(q)
    assert set(q["counts"]) >= {"waiting-on-author", "handed-off"}


def test_red_ci_offers_a_rerun_and_a_send_back_that_names_the_checks():
    # (one row per run: stampable rows share HEAD_V3, and check runs are keyed by head)
    q = run([stampable(1, check_runs=_red("lint"))])
    p = row(q, 1)
    assert p["verdict"] == "blocked" and "checks:red" in p["blockers"]
    acts = {a["id"]: a for a in p["actions"]}
    assert acts["rerun-checks"]["cmd"] == "--rerun-checks 1" and "lint" in acts["rerun-checks"]["label"]
    assert acts["request-changes"]["cmd"] == '--request-changes 1 --reason "1=CI is red (lint); please fix the failing checks."'
    assert "lint" in acts["request-changes"]["label"]
    card = next(c for c in q["do_next"] if c["kind"] == "rerun-checks")
    assert card["cmd"] == "--rerun-checks 1" and card["targets"] == {"1": "--rerun-checks 1"} and card["label"] == "re-run failed checks"
    # a workflow-authored row has nobody to send it back to
    g = row(run([stampable(2, check_runs=_red("build"), author="pulumi-bot", author_type="User")]), 2)
    ids = [a["id"] for a in g["actions"]]
    assert "rerun-checks" in ids and "close" in ids and "request-changes" not in ids


def test_a_red_sentinel_alone_is_not_red_ci():
    # The Sentinel concludes failure until an approval exists; act.py's
    # preflight leaves it out, and so does the board. #21598's own shape.
    p = row(run([stampable(1, check_runs=_red("sentinel"))]), 1)
    assert p["verdict"] == "stamp" and "checks:sentinel:failing" in p["reasons"] and "checks:red" not in p["blockers"]
    p = row(run([stampable(1, check_runs=_red("sentinel") + _red("lint"))]), 1)
    assert p["verdict"] == "blocked" and "checks:red:lint" in p["reasons"]


def test_own_changes_requested_is_not_a_blocker_and_waits_on_the_author():
    """The approver's own CR is superseded by the approval about to post
    (act.py ignores it in the preflight); the row is the author's turn until
    they push, and the board must not show it as blocked with nothing to do."""
    head = HEAD_V3
    q = run([stampable(1, reviews=[CR("CamSoper", commit_id=head)]),
             stampable(2, title="Pushed since", reviews=[CR("CamSoper", commit_id="0" * 40)], files=[_file("content/docs/b.md", ["x"])]),
             stampable(3, title="Older collect", reviews=[CR("CamSoper")], files=[_file("content/docs/c.md", ["x"])]),
             stampable(4, title="Generated", reviews=[CR("CamSoper", commit_id=head)], author="pulumi-bot", author_type="User",
                       files=[_file("content/docs/d.md", ["x"])]),
             stampable(5, title="Open findings", reviews=[CR("CamSoper", commit_id=head)], comments=[comment(CLEAN_BRIEF), comment(V3_AUTHOR)],
                       files=[_file("content/docs/e.md", ["x"])])])
    p = row(q, 1)
    assert p["verdict"] == "stamp" and "changes-requested" not in p["blockers"] and "merging-over:changes-requested:CamSoper" not in p["reasons"]
    assert "sent-back:2026-09-12" in p["reasons"] and p["sent_back"] == {"at": "2026-09-12", "by": "CamSoper", "commit_id": head, "head_moved": False}
    assert p["waiting_on_author"] is True and p["actions"] == []  # no decision: it is the author's turn
    # the head moved since the send-back: the row is live again, decisions and all
    p = row(q, 2)
    assert p["waiting_on_author"] is False and p["sent_back"]["head_moved"] is True and p["actions"][0]["cmd"] == "--stamp 2"
    # a review with no commit_id (an older collect) never guesses "they pushed"
    assert row(q, 3)["waiting_on_author"] is True
    # a workflow author never answers, so there is nobody to wait on
    g = row(q, 4)
    assert g["waiting_on_author"] is False and "sent-back:2026-09-12" in g["reasons"] and [a["id"] for a in g["actions"][:2]] == ["stamp", "stamp-no-merge"]
    # open findings + my own send-back: blocked, waiting, and no second send-back
    b = row(q, 5)
    assert b["verdict"] == "blocked" and b["waiting_on_author"] is True and "request-changes" not in [a["id"] for a in b["actions"]]
    assert q["counts"] == {"stamp": 2, "judge": 0, "route": 0, "blocked": 0, "handed-off": 0, "waiting-on-author": 3}
    # waiting rows sit out of the decision cards
    assert not any(c["kind"] == "stamp" and "1" in c["targets"] for c in q["do_next"])
    assert_every_row_has_a_button(q)


def test_unblock_is_replaced_where_act_refuses_to_push():
    q = run([stampable(1, author="dependabot[bot]", mergeable_state="dirty", files=[_file("package.json", ["x"])]),
             stampable(2, title="Fork", author="outsider", author_type="User", head_repo="outsider/docs", mergeable_state="dirty",
                       files=[_file("content/docs/b.md", ["x"])]),
             stampable(3, title="Regen", author="pulumi-bot", author_type="User", labels=["review:no-blockers", "automation/merge"],
                       mergeable_state="dirty", files=[_file("content/docs/c.md", ["x"])]),
             stampable(4, title="Pushable", mergeable_state="dirty", files=[_file("content/docs/d.md", ["x"])])])
    import act  # noqa: PLC0415
    for n, why in ((1, "dependabot"), (2, "fork"), (3, "generated")):
        p = row(q, n)
        assert p["verdict"] == "blocked" and f"unblock:refused:{why}" in p["reasons"], p["reasons"]
        assert not any(a["id"] == "unblock" for a in p["actions"]), p["actions"]
        assert act.push_allowed(p)[0] is False  # the board and the act layer agree
    assert [a["id"] for a in row(q, 1)["actions"]] == ["close"]
    assert row(q, 2)["actions"][0]["cmd"] == '--request-changes 2 --reason "2=This branch conflicts with master and can\'t be updated from here; please merge master into it."'
    assert [a["cmd"] for a in row(q, 4)["actions"]] == ["--unblock 4"] and "unblock:refused" not in " ".join(row(q, 4)["reasons"])


def test_a_blocked_row_never_carries_approve_anyway():
    # A route row offers "approve anyway"; the same lane's blocked row must
    # not, because act.py refuses a stamp on a blocked row and the refusal
    # used to sink the batch.
    blog = dict(labels=["review:no-blockers", "domain:blog"], files=[_file("content/blog/p/index.md", ["A new sentence."], ["An old one."])])
    q = run([stampable(1, **blog), stampable(2, title="Dirty", mergeable_state="dirty", **blog)], cfg=cfg(me=["docs"]))
    ids = lambda n: [a["id"] for a in row(q, n)["actions"] if a["id"] != "render"]  # noqa: E731
    assert row(q, 1)["verdict"] == "route" and ids(1) == ["route", "stamp", "stamp-no-merge"]
    assert row(q, 2)["verdict"] == "blocked" and ids(2) == ["unblock", "route"]


def test_someone_elses_changes_requested_asks_them_to_re_review():
    p = row(run([stampable(1, reviews=[CR("cnunciato")])]), 1)
    assert p["verdict"] == "blocked" and "changes-requested" in p["blockers"]
    assert [a["cmd"] for a in p["actions"]] == ["--route 1:@cnunciato"] and p["route_targets"] == ["@cnunciato"]
    # on a routed row the lane team rides along in the same request
    blog = dict(labels=["review:no-blockers", "domain:blog"], files=[_file("content/blog/p/index.md", ["A new sentence."], ["An old one."])])
    p = row(run([stampable(2, reviews=[CR("jdoe")], **blog)], cfg=cfg(me=["docs"]), teams={"pulumi/docs-marketing-review": True}), 2)
    assert p["route_targets"] == ["@jdoe", "@pulumi/docs-marketing-review"]
    assert p["actions"][0]["cmd"] == "--route 2:@jdoe --route 2:@pulumi/docs-marketing-review"


def test_my_own_pr_routes_to_the_lane_team():
    """GitHub rejects an approval or a send-back on your own PR (422), so
    the row takes neither; it routes, and points at /address-review."""
    q = run([stampable(1, author="camsoper", author_type="User"),
             stampable(2, title="Mine, blocked", author="CamSoper", author_type="User", comments=[comment(CLEAN_BRIEF), comment(V3_AUTHOR)],
                       files=[_file("content/docs/b.md", ["x"])])], teams={"pulumi/docs-guild": True})
    p = row(q, 1)
    assert p["verdict"] == "route" and p["author_self"] is True and "author:self" in p["reasons"] and p["is_mine"] is False
    assert [a["cmd"] for a in p["actions"] if a["id"] != "render"] == ["--route 1:@pulumi/docs-guild"]
    assert "/address-review 1" in p["self_note"]
    b = row(q, 2)
    assert b["verdict"] == "blocked" and [a["id"] for a in b["actions"]] == ["route"]
    # the judge step can't recommend a send-back on my own PR
    analyze.merge_judgments(q, {1: {"recommended": "request-changes"}})
    assert "recommended" not in row(q, 1) and row(q, 1)["rejected_recommendation"].startswith("request-changes:")
    assert_every_row_has_a_button(q)


def test_directional_conflicts_count_net_links_per_url():
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        page = root / "content" / "docs" / "new" / "_index.md"
        page.parent.mkdir(parents=True)
        page.write_text("---\ntitle: New\naliases:\n  - /docs/old/\n---\nbody\n")
        # #1 rewrites a sentence that carries the alias link untouched: the
        # link is in both the added and the removed set, net zero
        rewrite = stampable(1, title="Reword", files=[_file("content/blog/p/index.md", ["See [x](/docs/old/) for more detail."], ["See [x](/docs/old/) for detail."])])
        removes = stampable(2, title="Repoint", files=[_file("content/blog/q/index.md", ["see [x](/docs/new/)"], ["see [x](/docs/old/)"])])
        adds = stampable(3, title="Add", files=[_file("content/blog/r/index.md", ["see [x](/docs/old/) and [y](/docs/old/)"], ["see [y](/docs/old/)"])])
        q = run([rewrite, removes, adds], aliases=None, repo_root=root)
    assert q["directional"] == [{"path": "/docs/old/", "adds_links_pr": 3, "removes_links_pr": 2, "theirs": False}]
    assert row(q, 1)["verdict"] == "stamp" and not any(r.startswith("directional:") for r in row(q, 1)["reasons"])
    assert analyze.net_link_changes(row(q, 3))["/docs/old/"] == 1 and analyze.net_link_changes(row(q, 1))["/docs/old/"] == 0


def test_cluster_mine_is_my_rows_and_next_overlaps_first():
    a = stampable(1, title="Fix the intro", files=[_file("content/docs/a.md", ["x"], ["o"], old_start=10)])
    b = stampable(2, title="Reword the intro", files=[_file("content/docs/a.md", ["y", "yy"], ["o"], old_start=10)])
    # smaller than #2, so it sorts before it in the merge order, but its hunk
    # is nowhere near #1's: it is not the link the first merge will dirty
    c = stampable(3, title="Trim the appendix", files=[_file("content/docs/a.md", ["z"], ["p"], old_start=200)])
    # my own PR routes (GitHub won't take my approval): it overlaps #1 but
    # must neither gate it nor lead the chain
    d = stampable(4, title="My rewrite", author="CamSoper", author_type="User", files=[_file("content/docs/a.md", ["w"], ["o"], old_start=10)])
    q = run([a, b, c, d], cfg=cfg(me=["docs"]))
    cl = q["clusters"][0]
    assert cl["prs"] == [1, 2, 3, 4] and cl["mine"] == [1, 2, 3] and cl["theirs"] == [4] and cl["merge_order"] == [1, 3, 2]
    assert row(q, 4)["verdict"] == "route" and "cluster:C1:theirs" in row(q, 4)["reasons"]
    assert "cluster:C1:overlap:1/3" in row(q, 1)["reasons"] and "cluster:C1:same-file" in row(q, 3)["reasons"]
    rec = cl["recommendation"]
    assert rec["kind"] == "chain" and rec["first"] == 1 and rec["next"] == 2 and rec["cmd"] == "--chain C1"
    # an overlap with a routed row alone is advisory: #1 stamps once #2 is out of the picture
    q = run([a, d], cfg=cfg(me=["docs"]))
    assert row(q, 1)["verdict"] == "stamp" and "cluster:C1:theirs" in row(q, 1)["reasons"]
    assert q["clusters"][0]["recommendation"]["say"] == "C1: nothing of yours to sequence (to route 1)."
    # a cluster whose members are all mine but none can lead says what they are
    q = run([stampable(1, title="Fix the intro", mergeable_state="dirty", files=[_file("content/docs/a.md", ["x"], ["o"], old_start=10)]),
             stampable(2, title="Reword the intro", reviews=[CR("CamSoper", commit_id=HEAD_V3)], files=[_file("content/docs/a.md", ["y"], ["o"], old_start=10)])])
    assert q["clusters"][0]["recommendation"]["say"] == "C1: none of your 2 PRs can lead the chain yet (waiting on author 1, blocked 1); unblock one to start."


def test_no_config_tells_unreadable_teams_from_being_on_none():
    defaults = lambda: pr_review_config.parse_config({}, source="defaults")  # noqa: E731
    blog = stampable(2, title="Blog", labels=["review:no-blockers", "domain:blog"], files=[_file("content/blog/p/index.md", ["A new sentence."], ["Old."])])
    # readable, on none of the teams: no lane is mine, every gated row routes
    q = run([stampable(1), blog], cfg=defaults(), my_teams={"pulumi/docs-guild": False, "pulumi/docs-marketing-review": False, "pulumi/docs-tools": False})
    assert q["config"]["me"] == [] and q["config"]["source"] == "github-teams"
    assert "none of the routing teams" in q["config"]["warnings"][0] and "404" in q["config"]["warnings"][0]
    assert row(q, 1)["verdict"] == "route" and row(q, 2)["verdict"] == "route"
    # unreadable: every lane, and the warning says why
    q = run([stampable(1)], cfg=defaults(), my_teams={"pulumi/docs-guild": None, "pulumi/docs-marketing-review": None, "pulumi/docs-tools": None})
    assert set(q["config"]["me"]) == set(routing.SUBJECTS) and q["config"]["source"] == "defaults"
    assert "unreadable" in q["config"]["warnings"][0]
    # a partial read is still evidence, and names what it couldn't read
    q = run([stampable(1)], cfg=defaults(), my_teams={"pulumi/docs-guild": True, "pulumi/docs-marketing-review": False, "pulumi/docs-tools": None})
    assert q["config"]["me"] == ["docs", "programs"] and "pulumi/docs-tools unreadable" in q["config"]["warnings"][0]
    assert pr_review_config.lanes_from_teams({}, CONFIG) is None
    assert pr_review_config.lanes_from_teams({"pulumi/docs-guild": False, "pulumi/docs-marketing-review": False, "pulumi/docs-tools": False}, CONFIG) == []


def test_judged_blockers_lift_the_row_out_of_blocked():
    """SKILL: judging the row is what lets the stamp post the /resolve lines.
    So a row whose every open 🚨 has a resolvable judgment with a note is an
    approver's call again; one judgment short and it stays blocked."""
    q = run([stampable(1, comments=[comment(CLEAN_BRIEF), comment(V3_AUTHOR)])])
    p = row(q, 1)
    assert p["verdict"] == "blocked" and set(p["open_blocker_ids"]) == {"F1", "F2", "F3"}
    js = [{"finding_id": f, "disposition": d, "note": "checked; holds"} for f, d in (("F1", "refuted"), ("F2", "accepted"), ("F3", "not-applicable"))]
    analyze.merge_judgments(q, {1: {"judgments": js[:2], "recommended": "stamp"}})
    assert p["verdict"] == "blocked" and p["open_blocker_ids"] == ["F3"] and "recommended" not in p
    assert p["rejected_recommendation"] == "stamp: the row is blocked, not judge"
    analyze.merge_judgments(q, {1: {"judgments": js, "recommended": "stamp"}})
    assert p["verdict"] == "judge" and p["open_blocker_ids"] == [] and p["judged_blocker_ids"] == ["F1", "F2", "F3"]
    assert "outstanding:judged:F1,F2,F3" in p["reasons"] and p["recommended"] == "stamp"
    assert [a["cmd"] for a in p["actions"][:2]] == ["--stamp 1 --force", "--stamp 1:no-merge --force"]
    assert q["counts"]["judge"] == 1 and q["counts"]["blocked"] == 0
    # `deferred` is the author's, and a judgment without a note posts nothing: neither answers
    analyze.merge_judgments(q, {1: {"judgments": js[:2] + [{"finding_id": "F3", "disposition": "deferred", "note": "theirs"}]}})
    assert p["verdict"] == "blocked"
    analyze.merge_judgments(q, {1: {"judgments": js[:2] + [{"finding_id": "F3", "disposition": "refuted"}]}})
    assert p["verdict"] == "blocked"
    # red CI still holds a fully judged row
    q = run([stampable(1, comments=[comment(CLEAN_BRIEF), comment(V3_AUTHOR)], check_runs=_red())])
    analyze.merge_judgments(q, {1: {"judgments": js}})
    assert row(q, 1)["verdict"] == "blocked" and row(q, 1)["blockers"] == ["checks:red"]


def test_close_and_route_recommendations_add_their_buttons():
    judge = dict(comments=[comment(V3_BRIEF), comment(CLEAN_AUTHOR)])
    q = run([stampable(1, **judge),
             stampable(2, title="Generated", author="pulumi-bot", author_type="User", files=[_file("content/docs/b.md", ["x"])], **judge),
             stampable(3, title="Route me", files=[_file("content/docs/c.md", ["x"])], **judge)], teams={"pulumi/docs-guild": True})
    # a person's close needs a reason, written from the judgments' asks
    analyze.merge_judgments(q, {1: {"recommended": "close", "judgments": [{"finding_id": "F4", "ask": "Drop the claim.", "disposition": "deferred"}]}})
    p = row(q, 1)
    assert p["recommended"] == "close" and [a["cmd"] for a in p["actions"] if a["id"] == "close"] == ['--close 1 --reason "1=Drop the claim."']
    assert next(c for c in q["do_next"] if c["kind"] == "close")["targets"] == {"1": '--close 1 --reason "1=Drop the claim."'}
    # ...and without one the recommendation is rejected rather than rendered as a button that fails
    analyze.merge_judgments(q, {1: {"recommended": "close", "judgments": []}})
    assert "recommended" not in p and p["rejected_recommendation"].startswith("close:")
    # a generated row already carries the close; act.py writes its comment
    analyze.merge_judgments(q, {2: {"recommended": "close"}})
    assert row(q, 2)["recommended"] == "close" and [a["cmd"] for a in row(q, 2)["actions"] if a["id"] == "close"] == ["--close 2"]
    # route on a row in my lane: the lane's own team is the target
    analyze.merge_judgments(q, {3: {"recommended": "route"}})
    r = row(q, 3)
    assert r["recommended"] == "route" and [a["cmd"] for a in r["actions"] if a["id"] == "route"] == ["--route 3:@pulumi/docs-guild"]
    assert r["route_targets"] == ["@pulumi/docs-guild"]


def test_base_merge_satisfies_the_label_gate_from_the_card():
    merged = dict(head_sha="f" * 40, commits=[{"sha": HEAD_V3, "message": "x"}, {"sha": "f" * 40, "message": "Merge master", "parents": 2}])
    # the push swapped review:no-blockers for review:stale; the card still says nothing blocks
    p = row(run([stampable(1, labels=["review:stale", "domain:docs"], **merged)]), 1)
    assert p["verdict"] == "stamp" and "label:card-clean" in p["reasons"] and "review:base-merged" in p["reasons"]
    # an open ⚠️ on the card: the label can't be inferred, so the refresh is offered
    p = row(run([stampable(2, labels=["review:stale", "domain:docs"], comments=[comment(V3_BRIEF), comment(CLEAN_AUTHOR)], **merged)]), 2)
    assert p["verdict"] == "judge" and "label:card-clean" not in p["reasons"]
    assert [a["cmd"] for a in p["actions"] if a["id"] == "refresh"] == ["--refresh 2"]


def test_route_asks_every_missing_team_in_one_command():
    files = [_file("content/docs/a.md", ["A new sentence."], ["Old."]), _file("content/blog/p/index.md", ["A new sentence."], ["Old."])]
    q = run([stampable(1, labels=["review:no-blockers", "domain:mixed"], files=files)], cfg=cfg(me=["infra"]),
            teams={"pulumi/docs-guild": True, "pulumi/docs-marketing-review": True})
    p = row(q, 1)
    a = p["actions"][0]
    assert a["cmd"] == "--route 1:@pulumi/docs-marketing-review --route 1:@pulumi/docs-guild" and a["targets"] == p["route_targets"]
    assert a["label"] == "request review from @pulumi/docs-marketing-review and @pulumi/docs-guild"
    assert "route:docs-guild" in p["reasons"] and "route:marketing" in p["reasons"]
    card = next(c for c in q["do_next"] if c["kind"] == "route")
    assert card["cmd"] == a["cmd"] and card["label"] == "route to @pulumi/docs-marketing-review and @pulumi/docs-guild"
    # one domain in `me` makes the whole PR mine (intersection, not
    # containment), so there is no "partly routed" row: a route asks every
    # owning role, and a mine row asks none
    p = row(run([stampable(1, labels=["review:no-blockers", "domain:mixed"], files=files)], cfg=cfg(me=["docs"]),
                teams={"pulumi/docs-guild": True, "pulumi/docs-marketing-review": True}), 1)
    assert p["verdict"] == "stamp" and p["route_targets"] == []


# ---- the Do-next opening -------------------------------------------------------


def test_the_chain_card_never_offers_an_approval_that_needs_reading():
    """`--chain C1` approves the lead with `--force`, so the card may only
    offer it where the collision is the *only* thing holding that row back.
    An overlapping cluster member is always a `judge` row — the overlap is
    itself a stamp gate — so the verdict cannot answer this; `gate_fails`
    can."""
    a = stampable(1, title="Fix the intro", files=[_file("content/docs/a.md", ["x"], ["o"], old_start=10)])
    b = stampable(2, title="Reword the intro", files=[_file("content/docs/a.md", ["y"], ["o"], old_start=10)])
    q = run([a, b])
    lead = row(q, 1)
    assert lead["verdict"] == "judge" and lead["gate_fails"] == ["cluster:C1:overlap:1/2"]
    assert analyze.only_collisions_hold(lead) is True
    chain = next(c for c in q["do_next"] if c["kind"] == "chain")
    assert chain["cmd"] == "--chain C1" and chain["claims"] == [1, 2] and chain["label"] == "approve & merge #1"

    # Same cluster, same lead, but heightened scrutiny on it: approving that
    # is a call somebody has to make, so the card says so and carries no
    # button. (Merge order is smallest diff first, so #1 still leads.)
    a2 = stampable(1, title="Fix the intro", author="human-dev", author_type="User",
                   commits=["Fix\n\nCo-Authored-By: Claude <noreply@anthropic.com>"],
                   files=[_file("content/docs/a.md", ["x"], ["o"], old_start=10)])
    q = run([a2, b])
    lead = row(q, 1)
    assert lead["gate_fails"] == ["scrutiny:heightened", "cluster:C1:overlap:1/2"]
    assert analyze.only_collisions_hold(lead) is False
    chain = next(c for c in q["do_next"] if c["kind"] == "chain")
    assert chain["cmd"] is None and chain["claims"] == [] and chain["targets"] == {}
    assert "#1 leads the chain, but it needs a call of its own first (scrutiny:heightened)" in chain["does"]
    # and the row itself still carries the decision, which is the whole point
    assert "stamp" in [x["id"] for x in lead["actions"]]


def test_do_next_cards_only_name_rows_the_board_renders():
    """A card presses the row buttons it names. A row parked under "Waiting
    on the author" has no row on the board at all, so a card naming one could
    be clicked and would go straight back out — "the group buttons don't
    light up". Cards are built from the board's own row set now."""
    specs = [
        fresh(1, mergeable_state="dirty"),
        fresh(2, title="Red CI", check_runs=_red()),
        fresh(13, title="Sent back, red", reviews=[CR("CamSoper")], check_runs=_red()),
        fresh(14, title="Clean"),
    ]
    q = run(specs, cfg=cfg(me=["docs"]))
    parked = {p["number"] for p in q["prs"] if p.get("handed_off") or p.get("waiting_on_author")}
    on_board = {p["number"] for p in q["prs"]} - parked
    # #13 is waiting on its author and off the board, but still carries the
    # action a card would have reached for.
    assert parked == {13} and [a["id"] for a in row(q, 13)["actions"]] == ["rerun-checks"]
    for card in q["do_next"]:
        named = {int(t) for t in (card.get("targets") or {})} | set(card.get("claims") or [])
        assert named <= on_board, (card["kind"], named - on_board)
    rerun = next(c for c in q["do_next"] if c["kind"] == "rerun-checks")
    assert set(rerun["targets"]) == {"2"}


def test_the_stamp_card_is_only_ever_the_mechanically_stampable_rows():
    """"Approve the set" is the one batch approval the opening offers, and it
    is offered because nothing on those rows needed reading. A judge row that
    the judge pass would approve stays on its own row."""
    q = run([stampable(1), stampable(2, title="Open findings", comments=[comment(CLEAN_BRIEF), comment(V3_AUTHOR)],
                                     files=[_file("content/docs/b.md", ["x"])])])
    q = analyze.merge_judgments(q, {"2": {"recommended": "stamp"}}, ctx=q.get("_ctx"))
    card = next(c for c in q["do_next"] if c["kind"] == "stamp")
    assert set(card["targets"]) == {"1"} and row(q, 1)["verdict"] == "stamp"
    assert all(row(q, int(n))["verdict"] == "stamp" for n in card["targets"])


# ---- a stuck workflow PR is always fixable by hand ------------------------------


def test_a_stuck_workflow_pr_always_offers_a_hand_fix():
    """pulumi-bot's content-review lane opens a PR from a workflow run: a
    send-back is never read and closing it only re-queues the same page next
    run. Fixing the branch yourself is the remaining way out, so the row
    always offers it — as an interactive run, never as part of the --act
    command the board composes."""
    q = run([stampable(100, comments=[comment(CLEAN_BRIEF), comment(V3_AUTHOR)],
                       author="pulumi-bot", author_type="User")])
    p = row(q, 100)
    assert p["verdict"] == "blocked" and "author:generated" in p["reasons"]
    assert [h["id"] for h in p["handoffs"]] == ["handfix"]
    assert p["handoffs"][0]["run"] == "/address-review 100" and p["handoffs"][0]["label"] == "fix it yourself"
    assert "3 open findings" in p["handoffs"][0]["why"]
    # a handoff is not an act.py fragment: nothing here can reach --act
    assert "cmd" not in p["handoffs"][0]

    # A clean workflow row has nothing to fix, so it offers nothing.
    assert row(run([stampable(100, author="pulumi-bot", author_type="User")]), 100)["handoffs"] == []
    # An author who does answer reviews gets the send-back, not the handoff.
    assert row(run([stampable(100, comments=[comment(CLEAN_BRIEF), comment(V3_AUTHOR)],
                              author="jdoe", author_type="User")]), 100)["handoffs"] == []


def test_a_hand_fix_is_never_offered_where_the_fix_would_be_thrown_away():
    """Dependabot PRs and the generated-docs regens are rebuilt from source,
    and a fork head has no push access — `act.push_allowed` already says so,
    and the handoff follows it rather than promising work that vanishes."""
    q = run([stampable(1, comments=[comment(CLEAN_BRIEF), comment(V3_AUTHOR)], author="dependabot[bot]",
                       files=[_file("package.json", ["x"])]),
             stampable(2, title="Regen", comments=[comment(CLEAN_BRIEF), comment(V3_AUTHOR)],
                       author="pulumi-bot", author_type="User", labels=["review:no-blockers", "automation/merge"],
                       files=[_file("content/docs/r.md", ["x"])]),
             stampable(3, title="Content review", comments=[comment(CLEAN_BRIEF), comment(V3_AUTHOR)],
                       author="pulumi-bot", author_type="User", files=[_file("content/docs/c.md", ["x"])])])
    assert row(q, 1)["handoffs"] == [] and row(q, 2)["handoffs"] == []
    assert [h["run"] for h in row(q, 3)["handoffs"]] == ["/address-review 3"]


# ---- a split (multi-comment) legacy review -------------------------------


def test_a_split_legacy_review_blocks_the_row_it_used_to_wave_through():
    """pulumi/docs#21490 end to end. A v2 review split across two comments
    keeps its 🚨 section on page 2. Reading page 1 alone reported no findings
    at all, so the row missed `outstanding:` entirely and landed in `judge`,
    where `--stamp N --force` ("approve as-is & merge") is the primary
    button. "An unanswered 🚨 is blocked, never --force-able" exists to stop
    exactly that."""
    pages = tc.legacy_pages()
    q = run([stampable(1, comments=[comment(pages[0]), comment(pages[1])],
                       labels=["review:outstanding-issues", "domain:docs"])])
    p = row(q, 1)
    assert p["verdict"] == "blocked", (p["verdict"], p["reasons"])
    assert "outstanding:3" in p["blockers"]
    assert set(p["open_blocker_ids"]) == {"outstanding:L12", "outstanding:L40", "outstanding:L61"}
    assert not [a["id"] for a in p["actions"] if a["id"].startswith("stamp")]
    assert_every_row_has_a_button(q)


def test_a_legacy_review_with_a_page_missing_is_blocked_not_judged():
    """GitHub returned page 1 of 3. The findings may simply not be here, so
    the row is blocked with a fresh review as its unblock — never `judge`,
    where --force merges over whatever did not arrive."""
    pages = tc.legacy_pages(total=3)
    q = run([stampable(1, comments=[comment(pages[0])], labels=["review:no-blockers", "domain:docs"])])
    p = row(q, 1)
    assert p["verdict"] == "blocked" and "review:unreadable" in p["blockers"]
    # the missing page and the tally it left behind both fire, in one code
    why = next(r for r in p["reasons"] if r.startswith("review:unreadable:"))
    assert why == "review:unreadable:pages:2,3;tally:low,outstanding"
    # the unblock is a decision here, so the row is never "no action available"
    assert "rerun" in [a["id"] for a in p["actions"]]
    assert_every_row_has_a_button(q)


def test_a_tally_that_outruns_the_parsed_sections_blocks_the_row():
    """The belt to the paging fix's braces: whatever truncated the body, a
    card declaring three 🚨 whose sections parsed into none has said outright
    that findings are missing. The label still says review:no-blockers."""
    page1 = tc.legacy_pages()[0].replace("<!-- CLAUDE_REVIEW 1/2 -->", "<!-- CLAUDE_REVIEW 1/1 -->")
    q = run([stampable(1, comments=[comment(page1)], labels=["review:no-blockers", "domain:docs"])])
    p = row(q, 1)
    assert p["verdict"] == "blocked" and "review:unreadable" in p["blockers"]
    assert "review:unreadable:tally:low,outstanding" in p["reasons"]
    assert not [a["id"] for a in p["actions"] if a["id"].startswith("stamp")]


def test_a_review_that_parsed_into_nothing_is_never_stampable():
    """Weaker than unreadable and not a blocker: a v2 card with no tally
    table corroborating "no findings". Not blocked — nothing says there are
    findings — but a person reads it rather than stamping it."""
    body = "<!-- CLAUDE_REVIEW 1/1 -->\n## Pre-merge Review\n\n<!-- CLAUDE_REVIEW_HEAD %s -->\nLooks fine to me.\n" % HEAD_V3
    q = run([stampable(1, comments=[comment(body)], labels=["review:no-blockers", "domain:docs"])])
    p = row(q, 1)
    assert p["verdict"] == "judge" and "review:parse-confidence:low" in p["gate_fails"]
    assert "review:unreadable" not in p["blockers"]

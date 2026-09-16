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


def test_gate_open_blockers_on_author_card():
    p = _judge_because("outstanding:3", comments=[comment(CLEAN_BRIEF), comment(V3_AUTHOR)])
    assert set(p["open_blocker_ids"]) == {"F1", "F2", "F3"}


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

    q = run([page(1), page(2, author="camsoper", author_type="User")])
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
    p = row(run([stampable(labels=["review:in-progress", "domain:docs"])]), 100)
    assert p["verdict"] == "blocked" and not any(a["id"] == "rerun" for a in p["actions"])  # wait for it


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
    assert any(d["kind"] == "chain" and d["cmd"] == "--chain C1" for d in q["do_next"])


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
    p = row(run([stampable(5, **blog)], cfg=cfg(me=["docs"])), 5)
    assert p["verdict"] == "stamp" and p["is_mine"] is True
    assert "shape:link-only" in p["reasons"] and "link-fixes:mine" in p["reasons"] and not any(r.startswith("route:") for r in p["reasons"])
    p = row(run([stampable(5, **blog)], cfg=cfg(me=["docs"], link_fixes="route")), 5)
    assert p["verdict"] == "route" and "shape:link-only" in p["reasons"] and "link-fixes:mine" not in p["reasons"]
    # a prose edit in the same sweep keeps the lane owner
    p = row(run([stampable(6, **{**blog, "files": [_file("content/blog/p/index.md", [LINK_PLUS, "new sentence"], [LINK_MINUS, "old sentence"])]})], cfg=cfg(me=["docs"])), 6)
    assert p["verdict"] == "route" and "shape:link-only" not in p["reasons"]


def test_a_change_with_no_team_gate_is_any_approver_s():
    # A tags-only blog edit clears the mechanical bar, so the matrix asks for
    # no role at all. Routing it would invent a gate the Sentinel doesn't
    # have, and the chip says why it's on this board.
    tags = _file("content/blog/p/index.md", ["tags: [kubernetes, aws]"], ["tags: [kubernetes]"])
    p = row(run([stampable(1, labels=["review:no-blockers", "domain:blog"], files=[tags])], cfg=cfg(me=["docs"])), 1)
    assert p["mechanical"] is True and p["roles"] == []
    assert p["is_mine"] is True and p["verdict"] == "stamp" and "gate:none" in p["reasons"]
    assert not any(r.startswith("route:") for r in p["reasons"])
    # the substantive version of the same lane still routes
    prose = _file("content/blog/p/index.md", ["A new sentence about stacks."], ["An old sentence about stacks."])
    q = row(run([stampable(2, labels=["review:no-blockers", "domain:blog"], files=[prose])], cfg=cfg(me=["docs"])), 2)
    assert q["roles"] == ["marketing"] and q["verdict"] == "route" and "gate:none" not in q["reasons"]


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

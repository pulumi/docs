#!/usr/bin/env python3
"""Tests for collect.py — trust/risk/AI-suspect ports, review status, the
review parse over the shared fixtures, preview links, and an end-to-end
collect over a snapshot directory (the backend tests and model sessions
share).

Runs under pytest and standalone via `collect.py --self-test`. No pytest
fixtures (test_sla_sweep.py rule). `make_snapshot()` and `pr_spec()` are
also imported by test_analyze.py / test_act.py so every suite builds PRs
the same way.
"""

from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import collect  # noqa: E402
from gh_client import GhClient, snapshot_path  # noqa: E402

TESTDATA = HERE.parent.parent / ".claude" / "commands" / "docs-review" / "scripts" / "testdata"
V3_AUTHOR = (TESTDATA / "v3-fixture-author.md.txt").read_text()
V3_BRIEF = (TESTDATA / "v3-fixture-brief.md.txt").read_text()
LEGACY = (TESTDATA / "pr20079-pinned-review.md.txt").read_text()
HEAD_V3 = "aaaabbbbccccddddeeeeffff0000111122223333"  # the fixture card's CLAUDE_REVIEW_HEAD
BOT = "github-actions[bot]"


# ---- fixture builders ----------------------------------------------------


def patch_for(lines_added: list[str], *, old_start: int = 10, lines_removed: list[str] | None = None,
              context: list[str] | None = None) -> str:
    removed = lines_removed or []
    context = context if context is not None else ["ctx line"]
    old_len = len(removed) + len(context)
    new_len = len(lines_added) + len(context)
    body = [f"@@ -{old_start},{old_len} +{old_start},{new_len} @@"]
    body += [" " + c for c in context]
    body += ["-" + r for r in removed]
    body += ["+" + a for a in lines_added]
    return "\n".join(body)


def pr_spec(number: int, *, title: str = "A change", author: str = "workprentice[bot]",
            author_type: str = "Bot", labels: list[str] | None = None, files: list[dict] | None = None,
            head_sha: str | None = None, mergeable_state: str = "clean", draft: bool = False,
            body: str = "### Proposed changes\n\nDoes a thing.", comments: list[dict] | None = None,
            reviews: list[dict] | None = None, check_runs: list[dict] | None = None,
            statuses: list[dict] | None = None, created_at: str = "2026-09-10T10:00:00Z",
            updated_at: str = "2026-09-14T10:00:00Z", commits: list[str] | None = None,
            review_comments: list[dict] | None = None, head_ref: str | None = None,
            head_repo: str = "pulumi/docs", requested_users: list | None = None,
            requested_teams: list[str] | None = None) -> dict:
    """A compact description of one PR that make_snapshot() expands into
    every endpoint collect.py reads."""
    files = files if files is not None else [
        {"filename": "content/docs/iac/x.md", "status": "modified", "additions": 1, "deletions": 1,
         "patch": patch_for(["new line"], lines_removed=["old line"])}
    ]
    return {
        "number": number, "title": title, "author": author, "author_type": author_type,
        "labels": labels or [], "files": files, "head_sha": head_sha or (f"{number:040x}"),
        "mergeable_state": mergeable_state, "draft": draft, "body": body,
        "comments": comments or [], "reviews": reviews or [],
        "check_runs": check_runs if check_runs is not None else [{"name": "build", "status": "completed", "conclusion": "success"}],
        "statuses": statuses or [], "created_at": created_at, "updated_at": updated_at,
        "commits": commits or ["Do the thing"], "review_comments": review_comments or [],
        "head_ref": head_ref or f"branch-{number}", "head_repo": head_repo,
        "requested_users": requested_users or [], "requested_teams": requested_teams or [],
    }


def comment(body: str, login: str = BOT, cid: int | None = None) -> dict:
    return {"id": cid or (abs(hash(body)) % 10**8), "body": body, "user": {"login": login}}


def _write(root: Path, method: str, path: str, params: dict | None, data) -> None:
    f = snapshot_path(root, method, path, params)
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(json.dumps(data))


def make_snapshot(root: Path, specs: list[dict], repo: str = "pulumi/docs", members: list[str] = (),
                  me: str = "CamSoper") -> None:
    listed = []
    for s in specs:
        user = {"login": s["author"], "type": s["author_type"]}
        base = {
            "number": s["number"], "title": s["title"], "user": user, "draft": s["draft"], "state": "open",
            "labels": [{"name": l} for l in s["labels"]],
            "head": {"sha": s["head_sha"], "ref": s["head_ref"], "repo": {"full_name": s["head_repo"]}},
            "base": {"ref": "master", "sha": "b" * 40, "repo": {"full_name": repo}},
            "created_at": s["created_at"], "updated_at": s["updated_at"], "body": s["body"],
            "html_url": f"https://github.com/{repo}/pull/{s['number']}",
        }
        listed.append(base)
        detail = dict(base)
        detail.update({
            "mergeable": s["mergeable_state"] not in ("dirty",),
            "mergeable_state": s["mergeable_state"],
            "additions": sum(f["additions"] for f in s["files"]),
            "deletions": sum(f["deletions"] for f in s["files"]),
        })
        n = s["number"]
        _write(root, "GET", f"repos/{repo}/pulls/{n}", None, detail)
        _write(root, "GET", f"repos/{repo}/pulls/{n}/files", None, s["files"])
        _write(root, "GET", f"repos/{repo}/issues/{n}/comments", None, s["comments"])
        _write(root, "GET", f"repos/{repo}/pulls/{n}/reviews", None, s["reviews"])
        _write(root, "GET", f"repos/{repo}/pulls/{n}/commits", None,
               [({"sha": c.get("sha") or f"{i:040x}", "commit": {"message": c.get("message", "")},
                  "parents": [{"sha": "p"} for _ in range(c.get("parents", 1))]} if isinstance(c, dict)
                 else {"sha": f"{i:040x}", "commit": {"message": c}, "parents": [{"sha": "p"}]})
                for i, c in enumerate(s["commits"], 1)])
        _write(root, "GET", f"repos/{repo}/pulls/{n}/comments", None, s["review_comments"])
        _write(root, "GET", f"repos/{repo}/pulls/{n}/requested_reviewers", None, {
            "users": [({"login": u, "type": "User"} if isinstance(u, str) else u) for u in s["requested_users"]],
            "teams": [{"slug": t} for t in s["requested_teams"]],
        })
        _write(root, "GET", f"repos/{repo}/commits/{s['head_sha']}/check-runs", {"per_page": 100},
               {"total_count": len(s["check_runs"]), "check_runs": s["check_runs"]})
        _write(root, "GET", f"repos/{repo}/commits/{s['head_sha']}/statuses", None, s["statuses"])
    _write(root, "GET", f"repos/{repo}/pulls", {"state": "open"}, listed)
    _write(root, "GET", "user", None, {"login": me, "type": "User"})
    for m in members:
        _write(root, "GET", f"orgs/pulumi/members/{m}", None, None)


def collect_specs(specs: list[dict], **kw) -> dict:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        make_snapshot(root, specs, members=kw.pop("members", ()))
        gh = GhClient("pulumi/docs", "snapshot", snapshot_dir=root)
        return collect.collect(gh, cache_dir=None, repo_root=root, workers=1, **kw)


# ---- trust / risk / AI-suspect -------------------------------------------


class _MemberGh:
    def __init__(self, answer):
        self.answer = answer

    def org_member(self, org, login):
        if isinstance(self.answer, Exception):
            raise self.answer
        return self.answer

    def merged_pr_count_by_author(self, login):
        return 2 if login == "veteran" else 0


def test_author_classification_never_assumes_internal():
    assert collect.classify_author("workprentice[bot]", "Bot", None) == ("bot", None)
    assert collect.classify_author("pulumi-bot", "User", None) == ("bot", None)
    assert collect.classify_author("cam", "User", _MemberGh(True)) == ("internal", None)
    assert collect.classify_author("cam", "User", _MemberGh(False)) == ("external", None)
    ctype, note = collect.classify_author("cam", "User", _MemberGh(None))
    assert ctype == "external" and "not visible" in note
    ctype, note = collect.classify_author("cam", "User", _MemberGh(collect.GhError("boom", 500)))
    assert ctype == "external" and "failed" in note


def test_the_brief_yields_its_rubber_stamp_lines_and_evidence_link():
    brief = ("## Reviewer's guide v2\n\n### ⚠️ Check these before approving\n\n| F1 | x | y |\n\n"
             "### ✅ What you can rubber-stamp\n\n"
             "- **Facts:** 12 factual claims checked — 7 verified clean.\n"
             "- **Mechanics:** frontmatter sweep ran.\n\n"
             "💡 **Pre-existing issues in touched files:** 2\n\n"
             "📎 **Full evidence:** [verification trail](https://review-evidence-d1a6b84.s3.us-west-2.amazonaws.com/21622/latest.html)\n")
    lines = collect.rubber_stamp_lines(brief)
    assert lines == ["**Facts:** 12 factual claims checked — 7 verified clean.", "**Mechanics:** frontmatter sweep ran."]
    assert collect.evidence_url(brief).endswith("/21622/latest.html")
    assert collect.rubber_stamp_lines("") == [] and collect.evidence_url("", "") is None


def test_only_an_agent_bot_can_be_sent_a_review_back():
    assert collect.can_revise("bot", "workprentice[bot]") is True
    assert collect.can_revise("bot", "Copilot") is True
    assert collect.can_revise("bot", "pulumi-bot") is False       # workflow lanes: nobody reads it
    assert collect.can_revise("bot", "dependabot[bot]") is False
    assert collect.can_revise("internal", "cam") is True
    assert collect.can_revise("external", "someone") is True


def test_etiquette_trust_matrix():
    assert collect.etiquette_trust("internal", "cam", None) == "high"
    assert collect.etiquette_trust("bot", "workprentice[bot]", None) == "high"
    assert collect.etiquette_trust("bot", "dependabot[bot]", None) == "high"
    assert collect.etiquette_trust("bot", "randobot[bot]", None) == "low"
    assert collect.etiquette_trust("external", "veteran", _MemberGh(False)) == "standard"
    assert collect.etiquette_trust("external", "newbie", _MemberGh(False)) == "low"


def test_risk_tier_matrix():
    md = lambda n=1: [{"filename": f"content/docs/{i}.md", "status": "modified"} for i in range(n)]  # noqa: E731
    assert collect.risk_tier([{"filename": "scripts/x.py", "status": "modified"}], 1, 0) == "infra"
    assert collect.risk_tier([{"filename": "package.json", "status": "modified"}], 1, 0) == "infra"
    assert collect.risk_tier(md(), 200, 150) == "major"
    assert collect.risk_tier([{"filename": "content/docs/new.md", "status": "added"}], 3, 0) == "major"
    assert collect.risk_tier(md(), 3, 2) == "typo"
    assert collect.risk_tier(md(), 20, 5) == "minor"
    assert collect.risk_tier(md(2), 3, 2) == "standard"
    assert collect.risk_tier([{"filename": "static/programs/a/index.ts", "status": "modified"}], 2, 0) == "standard"


def test_ai_suspect_trailers_prose_and_override():
    files = [{"filename": "content/docs/a.md", "patch": patch_for(["plain prose"])}]
    assert collect.ai_suspect("x", "", ["Fix\n\nCo-Authored-By: Claude <noreply@anthropic.com>"], files,
                              allowlist_path=Path("/nonexistent")) == (True, ["trailer:claude", "trailer:anthropic"])
    assert collect.ai_suspect("x", "", [], files, override="no-ai") == (False, ["manual:no-ai"])
    assert collect.ai_suspect("x", "", [], files, override="ai") == (True, ["manual"])
    prose = [f"This is generally a sentence that typically has many words in it number {i} — dash" for i in range(12)]
    dashy = [{"filename": "content/docs/a.md", "patch": patch_for(prose)}]
    flag, reasons = collect.ai_suspect("x", "", [], dashy, allowlist_path=Path("/nonexistent"))
    assert flag and "prose-pattern:em-dash" in reasons and "prose-pattern:hedge" in reasons
    with tempfile.TemporaryDirectory() as td:
        allow = Path(td) / "allow.txt"
        allow.write_text("# comment\nsuspect-user\n")
        assert collect.ai_suspect("suspect-user", "", [], files, allowlist_path=allow)[1] == ["allowlist"]


def test_added_prose_skips_frontmatter_and_fences():
    patch = "\n".join(["@@ -1,1 +1,8 @@", "+---", "+title: x", "+---", "+prose one", "+```", "+code", "+```", "+prose two"])
    assert collect.added_prose_lines([{"filename": "a.md", "patch": patch}]) == ["prose one", "prose two"]
    assert collect.added_prose_lines([{"filename": "a.py", "patch": patch}]) == []


# ---- review surface ------------------------------------------------------


def test_review_status_matrix():
    rs = collect.review_status
    assert rs({"review:no-blockers"}, "v3", V3_AUTHOR, HEAD_V3, False) == "CURRENT"
    assert rs({"review:no-blockers"}, "v3", V3_AUTHOR, "f" * 40, False) == "STALE"  # label lies, SHA doesn't
    assert rs({"review:stale"}, "v3", V3_AUTHOR, HEAD_V3, False) == "STALE"
    assert rs({"review:in-progress"}, "v3", V3_AUTHOR, HEAD_V3, False) == "IN_PROGRESS"
    assert rs({"review:error"}, "v3", V3_AUTHOR, HEAD_V3, False) == "ERROR"
    assert rs({"review:trivial"}, "none", "", HEAD_V3, True) == "TRIAGE_PROSE"
    assert rs(set(), "none", "", HEAD_V3, False) == "ABSENT"
    assert rs({"review:no-blockers"}, "v3", V3_AUTHOR, HEAD_V3[:12], False) == "CURRENT"  # prefix both ways


def test_find_review_comments_prefers_v3_card():
    v3 = [comment(V3_BRIEF), comment(V3_AUTHOR)]
    a, b, surface = collect.find_review_comments(v3)
    assert surface == "v3" and "CLAUDE_REVIEW_AUTHOR" in a["body"] and "CLAUDE_REVIEW_BRIEF" in b["body"]
    a, b, surface = collect.find_review_comments([comment(LEGACY)])
    assert surface == "v2" and b is None and a["body"].startswith("<!-- CLAUDE_REVIEW 1/1 -->")
    assert collect.find_review_comments([comment("hi", "someone")]) == (None, None, "none")


def test_parse_review_v3_fixture():
    r = collect.parse_review(V3_AUTHOR, V3_BRIEF, 999, "pulumi/docs")
    assert r["surface"] == "v3" and r["reviewed_sha"] == HEAD_V3
    ids = {i["id"] for i in r["items"]}
    assert {"F1", "F2", "F3", "F4"} <= ids
    assert [w["id"] for w in r["warning_rows"]] == ["F4"]  # the ⚠️ table
    assert r["review_state"] == {"findings": {}, "high_water": 4, "schema": 1}
    assert r["nothing_blocks"] is False and r["stances"] is False
    assert r["brief_summary_bullets"] and r["brief_summary_bullets"][0].startswith("<TODO")


def test_parse_review_legacy_fixture():
    r = collect.parse_review(LEGACY, "", 20079, "pulumi/docs")
    assert r["surface"] == "v2" and r["warning_rows"] == [] and r["review_state"] is None
    assert r["summary"]["counts"]  # the v2 buckets parsed


def test_brief_change_bullets_reads_the_note_blockquote():
    brief = "> [!NOTE]\n> **What this PR changes:**\n>\n> - Renames `foo` to `bar`\n> - Drops the 2019 figure\n>\n> Other prose.\n"
    assert collect.brief_change_bullets(brief) == ["Renames `foo` to `bar`", "Drops the 2019 figure"]
    assert collect.brief_change_bullets("no label here") == []


# ---- preview / checks ----------------------------------------------------


def test_content_path_to_url():
    assert collect.content_path_to_url("content/docs/foo/_index.md") == "/docs/foo/"
    assert collect.content_path_to_url("content/blog/post/index.md") == "/blog/post/"
    assert collect.content_path_to_url("content/docs/a/b.md") == "/docs/a/b/"


def test_preview_info_finds_bot_url_and_titles_from_patch():
    comments = [comment("Your site preview is ready!\nhttp://www-testing-pulumi-docs-origin-pr-7-abc123.s3-website.us-west-2.amazonaws.com\n", "pulumi-bot"),
                comment("http://www-testing-pulumi-docs-origin-pr-7-zzz.s3-website.us-west-2.amazonaws.com", "someone")]
    files = [{"filename": "content/docs/a.md", "patch": patch_for(["title: Real Title", "body"])},
             {"filename": "scripts/x.py", "patch": ""}]
    with tempfile.TemporaryDirectory() as td:
        info = collect.preview_info(comments, files, Path(td))
    assert info["status"] == "ready" and info["url"].endswith("pr-7-abc123.s3-website.us-west-2.amazonaws.com")
    assert info["pages"][0]["title"] == "Real Title" and info["pages"][0]["preview_url"].endswith("/docs/a/")
    assert info["non_content_files"] == ["scripts/x.py"]
    assert collect.preview_info([], files, Path("/nonexistent"))["status"] == "pending"


def test_checks_rollup():
    ok = [{"name": "build", "status": "completed", "conclusion": "success"},
          {"name": "Sentinel", "status": "completed", "conclusion": "neutral"},
          {"name": "label", "status": "completed", "conclusion": "skipped"}]
    assert collect.checks_rollup(ok, [])["state"] == "green"
    red = ok + [{"name": "lint", "status": "completed", "conclusion": "failure"}]
    assert collect.checks_rollup(red, []) == {"state": "red", "failing": ["lint"], "pending": [], "total": 4}
    pend = ok + [{"name": "test", "status": "in_progress", "conclusion": None}]
    assert collect.checks_rollup(pend, [])["state"] == "pending"
    st = [{"context": "staging/pulumi-test-io", "state": "failure"}, {"context": "staging/pulumi-test-io", "state": "success"}]
    assert collect.checks_rollup(ok, st)["failing"] == ["staging/pulumi-test-io"]  # newest first wins
    # A concurrency group cancels superseded runs; only the newest run of a name counts.
    superseded = ok + [
        {"id": 1, "name": "sentinel", "status": "completed", "conclusion": "cancelled", "started_at": "2026-09-14T14:21:25Z", "completed_at": "2026-09-14T14:21:26Z"},
        {"id": 3, "name": "sentinel", "status": "completed", "conclusion": "success", "started_at": "2026-09-14T21:16:31Z", "completed_at": "2026-09-14T21:17:37Z"},
        {"id": 2, "name": "sentinel", "status": "completed", "conclusion": "cancelled", "started_at": "2026-09-14T14:21:27Z", "completed_at": "2026-09-14T14:21:27Z"},
    ]
    assert collect.checks_rollup(superseded, []) == {"state": "green", "failing": [], "pending": [], "total": 4}
    rerun = superseded + [{"id": 4, "name": "sentinel", "status": "in_progress", "conclusion": None, "started_at": "2026-09-15T09:00:00Z"}]
    assert collect.checks_rollup(rerun, [])["pending"] == ["sentinel"]  # a newer run still going beats an older success
    regressed = ok + [{"id": 5, "name": "lint", "status": "completed", "conclusion": "success", "started_at": "2026-09-14T10:00:00Z"},
                      {"id": 6, "name": "lint", "status": "completed", "conclusion": "failure", "started_at": "2026-09-14T11:00:00Z"}]
    assert collect.checks_rollup(regressed, [])["failing"] == ["lint"]
    # Job names repeat across workflows: a passing deploy build must not stand in for a failed PR build.
    build = "Install deps and build site"
    twins = [{"id": 7, "name": build, "status": "completed", "conclusion": "failure", "started_at": "2026-09-14T10:00:00Z", "check_suite": {"id": 70}},
             {"id": 8, "name": build, "status": "completed", "conclusion": "success", "started_at": "2026-09-14T11:00:00Z", "check_suite": {"id": 80}}]
    wf = {70: ".github/workflows/pull-request.yml", 80: ".github/workflows/testing-build-and-deploy.yml"}
    assert collect.checks_rollup(twins, [], wf)["failing"] == [build]
    # An unmapped suite dedupes nothing, so it errs red rather than green.
    assert collect.checks_rollup(twins, [])["failing"] == [build]
    # Reruns of the same workflow do dedupe, across their separate suites.
    rerun_wf = {70: ".github/workflows/pull-request.yml", 80: ".github/workflows/pull-request.yml"}
    assert collect.checks_rollup(twins, [], rerun_wf)["state"] == "green"


# ---- selection -----------------------------------------------------------


def test_select_prs_filters_by_app_login_and_drafts():
    listed = [{"number": 1, "user": {"login": "workprentice[bot]"}, "draft": False, "created_at": "2026-09-14T00:00:00Z"},
              {"number": 2, "user": {"login": "pulumi-bot"}, "draft": False, "created_at": "2026-09-01T00:00:00Z"},
              {"number": 3, "user": {"login": "cam"}, "draft": True, "created_at": "2026-09-14T00:00:00Z"}]
    pick = lambda **kw: [p["number"] for p in collect.select_prs(listed, numbers=None, authors=None, since=None, **kw)]  # noqa: E731
    assert pick() == [1, 2]
    assert [p["number"] for p in collect.select_prs(listed, numbers=None, authors=["app/workprentice"], since=None)] == [1]
    assert [p["number"] for p in collect.select_prs(listed, numbers=None, authors=["WorkPrentice"], since=None)] == [1]
    assert [p["number"] for p in collect.select_prs(listed, numbers=[3], authors=None, since=None)] == [3]  # explicit wins over draft skip
    since = collect.parse_since("2026-09-10T00:00:00Z")
    assert [p["number"] for p in collect.select_prs(listed, numbers=None, authors=None, since=since)] == [1]


def test_parse_since_relative_forms():
    from datetime import datetime, timezone
    now = datetime(2026, 9, 15, tzinfo=timezone.utc)
    assert collect.parse_since("7d", now).day == 8
    assert collect.parse_since("12h", now).hour == 12
    assert collect.parse_since(None) is None
    try:
        collect.parse_since("soon")
        raise AssertionError("expected ValueError")
    except ValueError:
        pass


# ---- end to end ----------------------------------------------------------


def test_collect_over_snapshot_end_to_end():
    spec = pr_spec(41, labels=["review:no-blockers", "domain:docs"],
                   comments=[comment(V3_BRIEF), comment(V3_AUTHOR),
                             comment("Your site preview is ready\nhttp://www-testing-pulumi-docs-origin-pr-41-abc.s3-website.us-west-2.amazonaws.com", "pulumi-bot")],
                   head_sha=HEAD_V3)
    q = collect_specs([spec, pr_spec(42, draft=True)])
    assert [p["number"] for p in q["prs"]] == [41]  # the draft is skipped
    p = q["prs"][0]
    assert p["author"]["type"] == "bot" and p["author"]["etiquette_trust"] == "high"
    assert p["review"]["status"] == "CURRENT" and p["review"]["surface"] == "v3"
    assert p["review"]["reviewed_sha"] == HEAD_V3 and [w["id"] for w in p["review"]["warning_rows"]] == ["F4"]
    assert p["checks"]["state"] == "green" and p["mergeable_state"] == "clean"
    assert p["preview"]["status"] == "ready" and p["files"][0]["path"] == "content/docs/iac/x.md"
    assert p["risk_tier"] == "typo" and p["scrutiny"] == "standard"
    assert q["schema_version"] == 1 and q["errors"] == []
    assert q["approver"] == "CamSoper"  # GET /user, no --approver needed


def test_my_team_memberships_answer_which_lanes_are_mine():
    class _Gh:
        def __init__(self):
            self.asked = []

        def team_member(self, org, slug, login):
            self.asked.append((org, slug, login))
            return {"docs-guild": True, "docs-marketing-review": False}.get(slug)  # tools: None (403)

    gh = _Gh()
    got = collect.my_team_memberships(gh, Path(__file__).resolve().parents[2], "CamSoper")
    assert got["pulumi/docs-guild"] is True and got["pulumi/docs-marketing-review"] is False
    assert all(who == "CamSoper" for _, _, who in gh.asked)
    assert collect.my_team_memberships(gh, None, None) == {}  # no login, no calls


def test_routing_teams_asks_github_for_every_configured_team():
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        make_snapshot(root, [pr_spec(1)])
        (root / ".github").mkdir()
        (root / ".github" / "review-routing.yml").write_text(
            "schema: 1\nteams: {docs-guild: pulumi/docs-guild, marketing: pulumi/docs-marketing-review, tools: pulumi/docs-tools}\n"
            "bots: []\nmatrix:\n  docs: {mechanical: none, substantive: docs-guild}\n  blog: {mechanical: none, substantive: marketing}\n"
            "  website: {mechanical: none, substantive: marketing}\n  programs: {mechanical: none, substantive: docs-guild}\n"
            "  infra: {mechanical: tools, substantive: tools, staging_evidence: required}\n  frontend: {mechanical: none, substantive: marketing}\n"
            "  other: {mechanical: none, substantive: tools}\nclaims_overlay: {add: marketing}\nexternal_contributors: {skip_gates: []}\n"
            "sla:\n  tools: {business_days: 1, escalate_to: a}\n  docs-guild: {business_days: 3, escalate_to: b}\n  marketing: {business_days: 3, escalate_to: c}\n"
            "author_staleness: {warn_days: 14, close_days: 21}\nwaive: {label: review:waived, log_prefix: x/}\nnot_governed: {authors: [], author_label_pairs: []}\n")
        _write(root, "GET", "orgs/pulumi/teams/docs-guild", None, {"slug": "docs-guild"})
        gh = GhClient("pulumi/docs", "snapshot", snapshot_dir=root)
        teams = collect.routing_teams(gh, root)
        assert teams == {"pulumi/docs-guild": True, "pulumi/docs-marketing-review": False, "pulumi/docs-tools": False}
        q = collect.collect(gh, cache_dir=None, repo_root=root, workers=1, numbers=[1])
        assert q["teams"] == teams
    # no routing config in the tree: no teams, route to people
    assert collect_specs([pr_spec(2)])["teams"] == {}


def test_base_merge_only_keeps_the_review_current():
    from test_analyze import CLEAN_AUTHOR, CLEAN_BRIEF, HEAD_V3  # noqa: PLC0415
    reviewed = [{"sha": HEAD_V3, "message": "the change"}]
    merge = [{"sha": "f" * 40, "message": "Merge master into branch", "parents": 2}]
    push = [{"sha": "f" * 40, "message": "one more fix"}]
    base = dict(labels=["review:stale", "domain:docs"], comments=[comment(CLEAN_BRIEF), comment(CLEAN_AUTHOR)], head_sha="f" * 40)
    r = collect_specs([pr_spec(1, commits=reviewed + merge, **base)])["prs"][0]["review"]
    assert r["status"] == "CURRENT" and r["base_merged"] is True
    r = collect_specs([pr_spec(2, commits=reviewed + push, **base)])["prs"][0]["review"]
    assert r["status"] == "STALE" and r["base_merged"] is False
    r = collect_specs([pr_spec(3, commits=merge, **base)])["prs"][0]["review"]  # reviewed head not in the list
    assert r["status"] == "STALE"


def test_requested_reviewers_drop_bots():
    q = collect_specs([pr_spec(46, requested_users=["cnunciato", {"login": "copilot-pull-request-reviewer[bot]", "type": "Bot"}],
                               requested_teams=["docs-guild"])])
    rr = q["prs"][0]["requested_reviewers"]
    assert rr == {"users": ["cnunciato"], "teams": ["docs-guild"]}


def test_collect_cache_serves_files_until_head_or_updated_moves():
    spec = pr_spec(43)
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        snap, cache = root / "snap", root / "cache"
        make_snapshot(snap, [spec])
        gh = GhClient("pulumi/docs", "snapshot", snapshot_dir=snap)
        q1 = collect.collect(gh, cache_dir=cache, repo_root=root, workers=1)
        assert q1["prs"][0]["files"][0]["path"] == "content/docs/iac/x.md"
        # Delete the files endpoint: a cache hit must not need it.
        snapshot_path(snap, "GET", "repos/pulumi/docs/pulls/43/files", None).unlink()
        q2 = collect.collect(gh, cache_dir=cache, repo_root=root, workers=1)
        assert q2["prs"][0]["files"][0]["path"] == "content/docs/iac/x.md"
        # A comment-only update (same head, new updated_at) must miss the cache.
        spec2 = dict(spec, updated_at="2026-09-15T10:00:00Z")
        make_snapshot(snap, [spec2])
        snapshot_path(snap, "GET", "repos/pulumi/docs/pulls/43/files", None).unlink()
        q3 = collect.collect(gh, cache_dir=cache, repo_root=root, workers=1)
        assert q3["prs"] == [] and q3["errors"][0]["pr"] == 43
        assert collect.gc_cache(cache, set()) >= 1 and not (cache / "43").exists()


def test_collect_records_triage_prose_and_absent_review():
    prose = comment("<!-- TRIAGE_PROSE -->\n🔍 **Triage prose check**\n- [spelling] teh", BOT)
    q = collect_specs([pr_spec(44, labels=["review:trivial", "review:prose-flagged"], comments=[prose]),
                       pr_spec(45, labels=[])])
    by = {p["number"]: p for p in q["prs"]}
    assert by[44]["review"]["status"] == "TRIAGE_PROSE" and by[44]["triage_prose"].startswith("<!-- TRIAGE_PROSE -->")
    assert by[45]["review"]["status"] == "ABSENT" and by[45]["review"]["items"] == []


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
        print(f"{failures} collect test(s) failed", file=sys.stderr)
        return 1
    print("all collect self-tests passed")
    return 0


if __name__ == "__main__":
    sys.exit(run_standalone())

#!/usr/bin/env python3
"""Truth-table tests for sentinel.py — every gate ok/red/error individually,
the conclusion mapping (the fails-open trap: errors are action_required,
never neutral), the waive semantics (a waive clears every gate, G4 too), the external and
legacy lanes, and the workflow's no-PR-code security invariant.

Runs under pytest (make test-review-pipeline) and standalone via
`sentinel.py --self-test` (run_standalone below).
"""

from __future__ import annotations

import importlib.util
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent.parent
sys.path.insert(0, str(HERE))


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


sentinel = _load("sentinel_under_test", HERE / "sentinel.py")
import review_state  # noqa: E402
import routing  # noqa: E402

HEAD = "a" * 40

RAW_CONFIG = {
    "schema": 1,
    "teams": {
        "docs-guild": "pulumi/docs-guild",
        "marketing": "pulumi/docs-marketing-review",
        "tools": "pulumi/docs-tools",
    },
    # Mirrors the live config: every bot that opens PRs on this repo.
    "bots": ["pulumi-bot", "workprentice[bot]", "github-copilot[bot]",
             "eon-pulumi-agent[bot]", "dependabot[bot]"],
    "matrix": {
        "docs": {"mechanical": "docs-guild", "substantive": "docs-guild"},
        "blog": {"mechanical": "marketing", "substantive": "marketing"},
        "website": {"mechanical": "marketing", "substantive": "marketing"},
        "programs": {"mechanical": "docs-guild", "substantive": "docs-guild"},
        "infra": {"mechanical": "tools", "substantive": "tools"},
        "frontend": {"mechanical": "marketing", "substantive": "marketing"},
        "other": {"mechanical": "tools", "substantive": "tools"},
    },
    # Staging evidence keys on the PATH, not the subject — `infra_file()`
    # below is on this list and `infra_data_file()` is deliberately not,
    # which is the distinction gate G4 now draws.
    "staging_evidence": {"paths": ["infrastructure/", "Makefile", "scripts/build-site.sh"]},
    "claims_overlay": {"add": "marketing"},
    "external_contributors": {"skip_gates": ["review-ran", "findings-answered"]},
    "sla": {
        "tools": {"business_days": 1, "escalate_to": "TODO-tools-lead"},
        "docs-guild": {"business_days": 3, "escalate_to": "TODO-owning-manager"},
        "marketing": {"business_days": 3, "escalate_to": "TODO-named-fallback"},
    },
    "author_staleness": {"warn_days": 14, "close_days": 21},
    "waive": {"label": "review:waived", "log_prefix": "pr-review/waives/"},
    "not_governed": {
        "authors": ["dependabot[bot]"],
        "author_label_pairs": [{"author": "pulumi-bot", "label": "automation/merge"}],
    },
}
CONFIG, _errors, _warnings = routing.validate_raw(RAW_CONFIG)
assert CONFIG is not None, _errors

LOOSE_CONFIG = CONFIG


# ---- Stub Gh -------------------------------------------------------------


class StubGh:
    def __init__(
        self,
        *,
        pr=None,
        files=None,
        comments=None,
        reviews=None,
        statuses=None,
        memberships=None,
        membership_error_users=(),
        permissions=None,
        permission_error_users=(),
        label_events=None,
        workflow_runs=None,
        workflow_runs_error=False,
        workflow_state="active",
        workflow_state_error=False,
        commits=None,
        compare=None,
        statuses_by_sha=None,
        workflow_runs_by_sha=None,
    ):
        self.pr = pr or {}
        self.files = files or []
        self.comments = list(comments or [])  # a copy: posts must not leak into a shared fixture
        self.reviews = reviews or []
        self.statuses = statuses or []
        self.memberships = memberships or {}  # (slug, user) -> state
        self.membership_error_users = set(membership_error_users)
        self.permissions = permissions or {}  # user -> admin/write/read/none
        self.permission_error_users = set(permission_error_users)
        self.permission_calls = []
        self.label_events = label_events or []
        self.workflow_runs = workflow_runs or []
        self.workflow_runs_error = workflow_runs_error
        self.workflow_state = workflow_state
        self.workflow_state_error = workflow_state_error
        self.commits = commits  # None: the read fails, as an unstubbed API would
        self.compare = compare or {}  # sha -> files at that commit
        self.statuses_by_sha = statuses_by_sha  # sha -> statuses; overrides `statuses`
        self.workflow_runs_by_sha = workflow_runs_by_sha
        self.compare_calls = []
        self.patched = []  # (comment_id, body)
        self.posted = []   # body
        self.deleted = []  # comment_id

    def get_pr(self):
        return self.pr

    def list_files(self):
        return self.files

    def list_issue_comments(self):
        return self.comments

    def list_reviews(self):
        return self.reviews

    def get_commit_statuses(self, sha):
        if self.statuses_by_sha is not None:
            return self.statuses_by_sha.get(sha, [])
        return self.statuses

    def list_commits(self):
        if self.commits is None:
            raise sentinel.SentinelDataError("commits not stubbed")
        return self.commits

    def compare_files(self, base, sha):
        self.compare_calls.append(sha)
        if sha not in self.compare:
            raise sentinel.SentinelDataError(f"compare {sha} not stubbed")
        return self.compare[sha]

    def get_team_membership(self, org, team_slug, user):
        if user in self.membership_error_users:
            raise sentinel.SentinelDataError(f"lookup failed for {user}")
        return self.memberships.get((team_slug, user), "none")

    def get_repo_permission(self, user):
        self.permission_calls.append(user)
        if user in self.permission_error_users:
            raise sentinel.SentinelDataError(f"permission lookup failed for {user}")
        return self.permissions.get(user, "none")

    def get_label_events(self):
        return self.label_events

    def get_workflow_runs(self, workflow_file, head_sha):
        if self.workflow_runs_error:
            raise RuntimeError("actions API unavailable")
        if self.workflow_runs_by_sha is not None:
            return self.workflow_runs_by_sha.get(head_sha, [])
        return self.workflow_runs

    def get_workflow_state(self, workflow_file):
        if self.workflow_state_error:
            raise RuntimeError("actions API unavailable")
        return self.workflow_state

    def get_issue_comment(self, comment_id):
        if getattr(self, "fresh_bodies", None) and comment_id in self.fresh_bodies:
            return {"id": comment_id, "body": self.fresh_bodies[comment_id]}
        return next(c for c in self.comments if c.get("id") == comment_id)

    def patch_issue_comment(self, comment_id, body):
        self.patched.append((comment_id, body))

    def post_issue_comment(self, body):
        # Lands in the listing like the real API, so a re-read after a POST
        # sees it.
        self.posted.append(body)
        next_id = max((c.get("id") or 0 for c in self.comments), default=0) + 1
        self.comments.append({"id": next_id, "body": body,
                              "user": {"login": sentinel.BOT_LOGIN, "type": "Bot"}})

    def delete_issue_comment(self, comment_id):
        self.deleted.append(comment_id)
        self.comments = [c for c in self.comments if c.get("id") != comment_id]


# ---- Fixture builders ----------------------------------------------------


BASE_REPO = "pulumi/docs"


def pr_meta(labels=(), draft=False, author="someone", head_repo=BASE_REPO, branch="topic"):
    """`head_repo` is the fork test: same as base = internal; another name
    or None (deleted fork) = external. Pass `head_repo=...` omitted from
    the dict via `_no_head_repo()` to model a payload without the fact.
    `branch` matters for bot authors: the review lane skips their PRs except
    on the branches it names."""
    return {
        "head": {"sha": HEAD, "ref": branch,
                 "repo": None if head_repo is None else {"full_name": head_repo}},
        "base": {"repo": {"full_name": BASE_REPO}},
        "draft": draft,
        "user": {"login": author},
        "labels": [{"name": n} for n in labels],
    }


def _no_head_repo(meta):
    meta["head"].pop("repo", None)
    return meta


def triage_prose_comment(login="github-actions[bot]"):
    return {"id": 77, "user": {"login": login}, "body": (
        "<!-- TRIAGE_PROSE -->\n🔍 **Triage prose check** — possible issues in the diff. "
        "Full review is skipped (`review:trivial`); please double-check before merging.\n"
        "- [spelling] content/docs/x.md:12 — missing Oxford comma")}


def docs_file_substantive():
    """One docs file whose added line carries a Layer-A prose claim."""
    return {
        "filename": "content/docs/iac/x.md",
        "status": "modified",
        "patch": "@@ -40,2 +40,3 @@\n context\n+Pulumi was founded in 2017 and 90% of teams agree.\n context",
    }


def docs_file_mechanical():
    return {
        "filename": "content/docs/iac/x.md",
        "status": "modified",
        "patch": "@@ -40,2 +40,2 @@\n context\n-teh stack\n+the stack",
    }


def blog_date_bump_file():
    """#22417, verbatim: a `date:` bump. Frontmatter-only by triage's bar, and
    not mechanical — that bar allows only `updated` and `tags`."""
    return {
        "filename": "content/blog/self-hosted-ai-infrastructure-pulumi-aicr/index.md",
        "status": "modified",
        "patch": ("@@ -1,6 +1,6 @@\n ---\n title: \"AI infrastructure on tap with the Pulumi AICR provider\"\n"
                  "-date: 2026-10-19\n+date: 2026-10-21\n draft: false\n"
                  " meta_desc: \"The Pulumi NVIDIA AI Cluster Runtime (AICR) provider deploys GPU clusters.\"\n"
                  " feature_image: feature.png"),
    }


def docs_count_fix_file():
    """#22429's shape: a one-word count correction. Trivial by triage's bar,
    but the number trips the claims signal, so it is not mechanical."""
    return {
        "filename": "content/docs/iac/guides/migration/_index.md",
        "status": "modified",
        "patch": ("@@ -55,3 +55,3 @@\n context\n"
                  "-New infrastructure can coexist with old infrastructure in two ways.\n"
                  "+New infrastructure can coexist with old infrastructure in three ways.\n context"),
    }


def docs_external_link_file():
    """Neither shortcut fits (a link change rules out trivial, a body change
    rules out frontmatter-only), and an external link rules out mechanical."""
    return {
        "filename": "content/docs/iac/x.md",
        "status": "modified",
        "patch": "@@ -40,2 +40,2 @@\n context\n-See the guide.\n+See [the guide](https://example.com/guide).",
    }


def editions_sync_file():
    """The marketing-web editions sync: generated data, opened by pulumi-bot
    on `chore/sync-pulumi-editions`, with no `automation/merge` label."""
    return {
        "filename": "data/pulumi_editions.yaml",
        "status": "modified",
        "patch": "@@ -1,3 +1,3 @@\n features:\n   - id: rbac\n-    min_edition: enterprise\n+    min_edition: pro",
    }


def infra_file():
    """Build/deploy pipeline: tools approves AND a staging run is required."""
    return {
        "filename": "scripts/build-site.sh",
        "status": "modified",
        "patch": "@@ -1,1 +1,1 @@\n-echo a\n+echo b",
    }


def infra_data_file():
    """`domain:infra` (tools approves) but NOT on `staging_evidence.paths`.

    The PR #21698 shape: a redirect data file the deploy reads and cannot be
    broken by. Tools still own it; G4 skips it.
    """
    return {
        "filename": "scripts/redirects/general-broken-links-redirects.txt",
        "status": "modified",
        "patch": "@@ -1,2 +1,1 @@\n-old/path.html|/docs/new/\n new/path.html|/docs/new/",
    }


def frontend_file():
    """A Hugo template: marketing approves, no staging run (2026-09-11)."""
    return {
        "filename": "layouts/partials/foo.html",
        "status": "modified",
        "patch": "@@ -1,1 +1,1 @@\n-<b>a</b>\n+<b>b</b>",
    }


def v3_author_card(n_blocking=0, head=HEAD):
    """An author card shaped exactly like compose-review.py writes it: the
    `## Author action guide vN — …` header carries the blocking verb the
    clean-brief rule reads."""
    verb = sentinel._compose.AUTHOR_HEADER_NOTHING_BLOCKS if n_blocking == 0 else f"{n_blocking} item blocks merge"
    lines = [
        "<!-- CLAUDE_REVIEW 1/1 -->",
        sentinel.AUTHOR_MARKER,
        f"<!-- CLAUDE_REVIEW_HEAD {head} -->",
        f"{sentinel._compose.AUTHOR_HEADER_PREFIX}1 — {verb}",
        "",
        "### 🚨 Must fix or refute",
        "",
    ]
    if n_blocking:
        lines += ["| | ID | Where | Finding |", "|---|---|---|---|"]
        for i in range(1, n_blocking + 1):
            lines.append(f"| **F{i}** | `content/docs/iac/x.md` L10 | a problem |")
    else:
        lines.append("_Nothing to fix — this section is empty._")
    lines += ["", "### ❓ Only you can answer these", "", "_No open questions for you._", ""]
    state = review_state.empty_state()
    state["high_water"] = n_blocking
    body = "\n".join(lines) + "\n" + review_state.serialize_block(state) + "\n"
    body += "\n<!-- CLAUDE_REVIEW_FOOTER -->\nfooter text\n"
    return {"id": 111, "body": body, "user": {"login": "github-actions[bot]"}}


def v3_brief(check_rows=0, stances=False):
    """A reviewer brief with N ⚠️ finding rows (0 ⇒ the composer's empty
    sentinel), optionally followed by the editorial-stances H4."""
    lines = [sentinel.BRIEF_MARKER, "## Reviewer brief — head aaaa", "", "Summary text.", "",
             sentinel._compose.CHECKS_HEADING, ""]
    if check_rows:
        lines += ["| | ID | Where | Finding |", "|---|---|---|---|"]
        for i in range(1, check_rows + 1):
            lines.append(f"| **F{i + 10}** | `content/docs/iac/x.md` L30 | worth a look |")
    else:
        lines.append(sentinel._compose.empty_checks_sentinel(stances))
    if stances:
        lines += ["", sentinel._compose.STANCES_HEADING, "", "- The page frames X as Y."]
    lines += ["", "### ✅ What you can rubber-stamp", "", "- 3/3 claims verified", "",
              "<!-- CLAUDE_REVIEW_FOOTER -->", "reviewer footer", ""]
    return {"id": 222, "body": "\n".join(lines), "user": {"login": "github-actions[bot]"}}


def author_card(findings=(), state=None, head=HEAD):
    """findings: list of (fid, section) where section is 'must' or 'answer'."""
    must = [f for f, s in findings if s == "must"]
    answer = [f for f, s in findings if s == "answer"]
    lines = [
        "<!-- CLAUDE_REVIEW 1/1 -->",
        sentinel.AUTHOR_MARKER,
        f"<!-- CLAUDE_REVIEW_HEAD {head} -->",
        "## Review: author action needed — %d items block merge — Last updated x" % (len(must) + len(answer)),
        "",
        "### 🚨 Fix or disagree",
        "",
    ]
    if must:
        lines += ["| | ID | Where | Finding |", "|---|---|---|---|"]
    for fid in must:
        lines.append(f"| **{fid}** | `content/docs/iac/x.md` L10 | a problem |")
    lines += ["", "### ❓ Questions for you", ""]
    if answer:
        lines += ["| | ID | Where | Finding |", "|---|---|---|---|"]
    for fid in answer:
        lines.append(f"| **{fid}** | `content/docs/iac/x.md` L20 | a question |")
    lines += ["", "### ✅ Resolved since last review", "", "_none_", ""]
    body = "\n".join(lines)
    if state is None:
        state = review_state.empty_state()
        state["high_water"] = len(findings)
    body += "\n" + review_state.serialize_block(state) + "\n"
    body += "\n<!-- CLAUDE_REVIEW_FOOTER -->\nfooter text\n"
    return {"id": 111, "body": body, "user": {"login": "github-actions[bot]"}}


def brief_comment():
    return {
        "id": 222,
        "body": (sentinel.BRIEF_MARKER + "\n## Reviewer brief — head aaaa\n\nSummary text.\n\n"
                 "<!-- CLAUDE_REVIEW_FOOTER -->\nreviewer footer\n"),
        "user": {"login": "github-actions[bot]"},
    }


def approval(user, utype="User", body="", commit_id=None, assoc="MEMBER"):
    """An APPROVED review. `commit_id` defaults to the PR head, as GitHub
    always sends it — pass an older SHA to model a pre-push approval.
    `assoc` is GitHub's `author_association` (NONE for a passer-by)."""
    return {"state": "APPROVED", "user": {"login": user, "type": utype},
            "body": body, "commit_id": commit_id or HEAD, "author_association": assoc}


def _state_with(fids, disposition="refuted", note="because"):
    st = review_state.empty_state()
    st["high_water"] = len(fids)
    for fid in fids:
        st = review_state.set_disposition(st, fid, disposition, actor="cam", note=note)
    return st


def _gate(verdict, prefix):
    return next(g for g in verdict.gates if g.name.startswith(prefix))


# ---- Tests ---------------------------------------------------------------


def test_mechanical_skips_the_review():
    """`mechanical` is a model-review saving, not a human-review waiver.

    It used to conclude success with no approval at all, which the repo's
    own required-review rule contradicted — so the PR sat unmergeable under
    a green check, and somebody stamped it by hand.
    """
    gh = StubGh(pr=pr_meta(), files=[docs_file_mechanical()])
    v = sentinel.evaluate(gh, CONFIG)
    assert v.mechanical is True
    assert _gate(v, "review").status == "ok"          # no model review needed
    # Who approves is branch protection's call, not a gate's.
    assert v.conclusion == "success", v.to_json()
    assert "Branch protection still asks for an approval" in v.summary


def test_mechanical_pr_succeeds_once_the_lane_team_approves():
    gh = StubGh(pr=pr_meta(), files=[docs_file_mechanical()],
                reviews=[approval("guild")],
                memberships={("docs-guild", "guild"): "active"})
    v = sentinel.evaluate(gh, CONFIG)
    assert v.conclusion == "success", v.to_json()


def test_substantive_no_review_g1_pending():
    gh = StubGh(pr=pr_meta(), files=[docs_file_substantive()])
    v = sentinel.evaluate(gh, CONFIG)
    # Still blocks the merge (a pending required status), without a red X.
    assert v.conclusion == "pending"
    g1 = _gate(v, "review")
    assert g1.status == "pending"
    # The first review is usually still running: say so, don't hand out a command.
    assert "hasn't posted yet" in g1.message and "/update-review" not in g1.message
    assert v.title == "Waiting on the automated review", v.title
    st = {x["context"]: x for x in v.to_json()["gate_statuses"]}
    assert st["Sentinel / review"]["description"] == "the automated review is running"
    assert st["Sentinel / review"]["state"] == "pending"
    # A stale card is different: the review won't rerun by itself.
    stale = author_card([], state=_state_with([]), head="b" * 40)
    g1s = _gate(sentinel.evaluate(StubGh(pr=pr_meta(), files=[docs_file_substantive()],
                                         comments=[stale]), CONFIG), "review")
    assert "/update-review" in g1s.message


def test_findings_undecided_g2_red_lists_ids():
    card = author_card([("F1", "must"), ("F2", "answer")])
    gh = StubGh(pr=pr_meta(), files=[docs_file_substantive()], comments=[card],
                reviews=[approval("guild-member")],
                memberships={("docs-guild", "guild-member"): "active"})
    v = sentinel.evaluate(gh, CONFIG)
    g2 = _gate(v, "findings")
    assert g2.status == "red" and "F1" in g2.message and "F2" in g2.message
    assert "/update-review" in g2.message and "/resolve" not in g2.message and "@claude" not in g2.message
    assert v.conclusion == "failure"
    assert v.blocking_ids == ["F1", "F2"]


def test_dispositions_flip_g2_green():
    st = _state_with(["F1", "F2"])
    card = author_card([("F1", "must"), ("F2", "answer")], state=st)
    gh = StubGh(pr=pr_meta(), files=[docs_file_substantive()], comments=[card],
                reviews=[approval("guild-member")],
                memberships={("docs-guild", "guild-member"): "active"})
    v = sentinel.evaluate(gh, CONFIG)
    assert _gate(v, "findings").status == "ok"
    assert v.conclusion == "success", v.to_json()


def test_corrupt_review_state_action_required():
    card = author_card([("F1", "must")])
    card["body"] = card["body"].replace("<!-- REVIEW_STATE ", "<!-- REVIEW_STATE {broken ")
    gh = StubGh(pr=pr_meta(), files=[docs_file_substantive()], comments=[card])
    v = sentinel.evaluate(gh, CONFIG)
    assert _gate(v, "findings").status == "error"
    assert v.conclusion == "action_required"
    assert "maintainer" in _gate(v, "findings").message


def link_only_file():
    """A blog file whose one changed line differs only in its link target."""
    return {
        "filename": "content/blog/p/index.md",
        "status": "modified",
        "patch": ("@@ -10,3 +10,3 @@\n context\n"
                  "-See [stacks](https://www.pulumi.com/docs/concepts/stacks/) for the rest.\n"
                  "+See [stacks](/docs/iac/concepts/stacks/) for the rest.\n context"),
    }


def test_link_only_diff_is_narrow():
    assert sentinel.link_only_diff([link_only_file()]) is True
    assert sentinel.link_only_diff([docs_file_substantive()]) is False
    assert sentinel.link_only_diff([{"filename": "a.md", "status": "modified", "patch": None}]) is False
    assert sentinel.link_only_diff([]) is False


def test_external_contributor_is_a_fork_head_repo():
    # A fork PR — even from a write-access user — is external: G1/G2 skip,
    # the matrix approver's review is the review.
    gh = StubGh(pr=pr_meta(author="staff-on-a-fork", head_repo="staff-on-a-fork/docs"),
                files=[docs_file_substantive()], reviews=[approval("guild-member")],
                memberships={("docs-guild", "guild-member"): "active"})
    v = sentinel.evaluate(gh, CONFIG)
    assert _gate(v, "review").status == "skip"
    assert _gate(v, "findings").status == "skip"
    assert v.conclusion == "success"
    assert "external contribution" in v.summary.lower()
    # A deleted fork (GitHub nulls head.repo) is external too.
    v = sentinel.evaluate(StubGh(pr=pr_meta(head_repo=None), files=[docs_file_substantive()]), CONFIG)
    assert _gate(v, "review").status == "skip"


def test_same_repo_bot_author_is_never_external():
    # workprentice[bot] answers `none` on the collaborator-permission API but
    # pushes same-repo branches that get the full review (2026-09-14: every
    # workprentice PR had G1/G2 skipped). Permission is not the test.
    card = author_card([("F1", "must")], state=_state_with([]))
    gh = StubGh(pr=pr_meta(author="workprentice[bot]"), files=[docs_file_substantive()],
                comments=[card])
    v = sentinel.evaluate(gh, CONFIG)
    assert _gate(v, "review").status == "ok"
    assert _gate(v, "findings").status == "red" and v.blocking_ids == ["F1"]
    assert "external" not in v.summary.lower()


def test_missing_head_repo_fact_is_internal():
    # Fail closed: no head.repo key at all ⇒ the stricter (internal) gates.
    gh = StubGh(pr=_no_head_repo(pr_meta(author="drive-by")), files=[docs_file_substantive()])
    v = sentinel.evaluate(gh, CONFIG)
    assert _gate(v, "review").status == "pending"
    assert _gate(v, "findings").status == "skip"  # "no review present — see G1", not the external skip
    assert "external" not in v.summary.lower()


def test_trivial_prose_flagged_stands_on_triage_prose_comment():
    # The review lane skipped this PR as trivial; the prose flag demotes it
    # from mechanical; triage's prose comment is the review.
    labels = ["review:trivial", "review:prose-flagged"]
    gh = StubGh(pr=pr_meta(labels=labels), files=[docs_file_mechanical()],
                comments=[triage_prose_comment()])
    v = sentinel.evaluate(gh, CONFIG)
    assert v.mechanical is False
    assert _gate(v, "review").status == "ok" and "prose check stands in" in _gate(v, "review").message
    assert _gate(v, "findings").status == "ok" and "no findings to answer" in _gate(v, "findings").message
    assert v.conclusion == "success"
    assert "stands in for the review" in v.summary


def test_trivial_prose_flagged_without_triage_comment_names_the_fix():
    labels = ["review:trivial", "review:prose-flagged"]
    gh = StubGh(pr=pr_meta(labels=labels), files=[docs_file_mechanical()])
    v = sentinel.evaluate(gh, CONFIG)
    g1 = _gate(v, "review")
    assert g1.status == "red"
    assert "/new-review" in g1.message and "review:trivial" in g1.message
    assert _gate(v, "findings").status == "skip"
    # A comment from someone other than the triage bot is not the stand-in.
    gh = StubGh(pr=pr_meta(labels=labels), files=[docs_file_mechanical()],
                comments=[triage_prose_comment(login="someone")])
    assert _gate(sentinel.evaluate(gh, CONFIG), "review").status == "red"


def test_trivial_without_prose_flag_is_still_mechanical():
    gh = StubGh(pr=pr_meta(labels=["review:trivial"]), files=[docs_file_mechanical()])
    v = sentinel.evaluate(gh, CONFIG)
    assert v.mechanical is True
    assert _gate(v, "review").message.startswith("mechanical change")
    # Mechanical clears G1 only; the lane team is still owed an approval.


def test_current_author_card_beats_trivial_standin():
    # A card current at head is the review even when the label says trivial.
    card = author_card([("F1", "must")], state=_state_with([]))
    gh = StubGh(pr=pr_meta(labels=["review:trivial", "review:prose-flagged"]),
                files=[docs_file_mechanical()], comments=[card, triage_prose_comment()])
    v = sentinel.evaluate(gh, CONFIG)
    assert _gate(v, "review").message.startswith("review current")
    assert _gate(v, "findings").status == "red"


def test_stale_author_card_is_not_rescued_by_trivial_standin():
    # A PR that was reviewed once stays on the review track: a stale card
    # with an open finding plus a later trivial label and a prose comment
    # must not pass G1/G2 on the stand-in (PR #21607 review, F1).
    card = author_card([("F1", "must")], state=_state_with([]), head="0" * 40)
    gh = StubGh(pr=pr_meta(labels=["review:trivial", "review:prose-flagged"]),
                files=[docs_file_mechanical()], comments=[card, triage_prose_comment()])
    v = sentinel.evaluate(gh, CONFIG)
    assert _gate(v, "review").status == "red"
    assert "stands in" not in _gate(v, "review").message
    assert _gate(v, "findings").status == "red"
    assert v.conclusion == "failure"


def test_frontmatter_only_skip_passes_g1():
    """#22417. The review lane skips `review:frontmatter-only`; G1 had no
    branch for it, so a `date:` bump sat red until it was waived."""
    base = dict(pr=pr_meta(labels=["review:frontmatter-only"]), files=[blog_date_bump_file()])
    v = sentinel.evaluate(StubGh(**base), CONFIG)
    assert v.mechanical is False  # `date` is outside the mechanical bar's keys
    g1 = _gate(v, "review")
    assert g1.status == "ok", g1.message
    assert g1.message.startswith("frontmatter-only change")
    assert "review:frontmatter-only" in g1.message
    assert _gate(v, "findings").status == "ok" and "no findings to answer" in _gate(v, "findings").message
    assert v.conclusion == "success"
    assert "approving reviewer's review is the review" in v.summary
    st = {x["context"]: x for x in v.to_json()["gate_statuses"]}
    assert st["Sentinel / review"]["state"] == "success"
    assert st["Sentinel / review"]["description"].startswith("frontmatter-only change")
    approved = sentinel.evaluate(
        StubGh(**base, reviews=[approval("mkt")],
               memberships={("docs-marketing-review", "mkt"): "active"}), CONFIG)
    assert approved.conclusion == "success", approved.to_json()


def test_clean_trivial_skip_that_misses_the_mechanical_bar_passes_g1():
    """#22429. Triage posts its prose comment only when it finds something, so
    a clean trivial PR has none. The stand-in used to require it, on the
    assumption that a clean trivial PR is mechanical anyway — but a count
    correction trips the claims signal, so it isn't, and G1 sat red."""
    base = dict(pr=pr_meta(labels=["review:trivial"], author="pulumi-bot",
                           branch="content-review/docs-iac-guides-migration"),
                files=[docs_count_fix_file()])
    v = sentinel.evaluate(StubGh(**base), CONFIG)
    assert v.mechanical is False
    g1 = _gate(v, "review")
    assert g1.status == "ok", g1.message
    assert g1.message.startswith("trivial change") and "left no nits" in g1.message
    assert _gate(v, "findings").status == "ok"
    approved = sentinel.evaluate(
        StubGh(**base, reviews=[approval("guild")],
               memberships={("docs-guild", "guild"): "active"}), CONFIG)
    assert approved.conclusion == "success", approved.to_json()


def test_prose_flagged_frontmatter_only_stands_on_the_triage_comment():
    labels = ["review:frontmatter-only", "review:prose-flagged"]
    v = sentinel.evaluate(StubGh(pr=pr_meta(labels=labels), files=[blog_date_bump_file()],
                                 comments=[triage_prose_comment()]), CONFIG)
    assert _gate(v, "review").status == "ok" and "stands in" in _gate(v, "review").message
    assert _gate(v, "findings").status == "ok"
    assert "stands in for the review" in v.summary
    # The flag promises nits; with the comment gone nobody can see them.
    v = sentinel.evaluate(StubGh(pr=pr_meta(labels=labels), files=[blog_date_bump_file()]), CONFIG)
    g1 = _gate(v, "review")
    assert g1.status == "red"
    assert "review:frontmatter-only" in g1.message and "/new-review" in g1.message
    assert _gate(v, "findings").status == "skip"


def test_a_skip_label_on_a_diff_that_does_not_fit_it_is_red():
    """The label is triage's word, but anyone with triage access can apply
    it. G1 honors the skip only when the diff itself has the shape."""
    for label in ("review:trivial", "review:frontmatter-only"):
        for f in (docs_external_link_file(), infra_file()):
            v = sentinel.evaluate(StubGh(pr=pr_meta(labels=[label]), files=[f]), CONFIG)
            g1 = _gate(v, "review")
            assert g1.status == "red", (label, f["filename"], g1.message)
            assert label in g1.message and "neither trivial nor frontmatter-only" in g1.message
            assert "/new-review" in g1.message
            assert _gate(v, "findings").status == "skip"
    # Either shortcut makes the skip legitimate, whichever label triage used.
    v = sentinel.evaluate(StubGh(pr=pr_meta(labels=["review:trivial"]),
                                 files=[blog_date_bump_file()]), CONFIG)
    assert _gate(v, "review").status == "ok"
    assert _gate(v, "review").message.startswith("frontmatter-only change")


def test_a_binary_or_unrendered_patch_never_fits_a_shortcut():
    """GitHub omits `patch` for binaries and for diffs too large to render.
    The Sentinel can't see what changed, so it can't vouch for the skip."""
    f = {"filename": "content/blog/x/index.md", "status": "modified"}
    v = sentinel.evaluate(StubGh(pr=pr_meta(labels=["review:frontmatter-only"]), files=[f]), CONFIG)
    assert _gate(v, "review").status == "red"


def test_a_skip_label_never_rescues_a_reviewed_pr():
    """Same rule as the trivial stand-in: a card at any head keeps the PR on
    the review track, so a stale card's open finding still blocks."""
    card = author_card([("F1", "must")], state=_state_with([]), head="0" * 40)
    v = sentinel.evaluate(StubGh(pr=pr_meta(labels=["review:frontmatter-only"]),
                                 files=[blog_date_bump_file()], comments=[card]), CONFIG)
    assert _gate(v, "review").status == "red"
    assert "frontmatter-only change" not in _gate(v, "review").message
    assert _gate(v, "findings").status == "red"
    # And a current card is the review, label or not.
    card = author_card([], state=_state_with([]))
    v = sentinel.evaluate(StubGh(pr=pr_meta(labels=["review:frontmatter-only"]),
                                 files=[blog_date_bump_file()], comments=[card]), CONFIG)
    assert _gate(v, "review").message.startswith("review current")


def test_bot_authored_pr_the_review_lane_skips_passes_g1_not_g3():
    """claude-code-review.yml skips pulumi-bot and Dependabot PRs except on
    the branches it names. The editions sync is one: G1 waited for a review
    that never runs (#22204)."""
    base = dict(pr=pr_meta(author="pulumi-bot", branch="chore/sync-pulumi-editions"),
                files=[editions_sync_file()])
    v = sentinel.evaluate(StubGh(**base), CONFIG)
    g1 = _gate(v, "review")
    assert g1.status == "ok", g1.message
    assert "pulumi-bot" in g1.message and "chore/sync-pulumi-editions" in g1.message
    assert _gate(v, "findings").status == "ok"
    assert "Automation PR" in v.summary
    approved = sentinel.evaluate(
        StubGh(**base, reviews=[approval("mkt")],
               memberships={("docs-marketing-review", "mkt"): "active"}), CONFIG)
    assert approved.conclusion == "success", approved.to_json()
    # The branches the lane DOES review wait for that review.
    for branch in ("content-review/x", "fix/broken-links-2026-10-20", "vale/brand-sync-2026-10-12"):
        v = sentinel.evaluate(StubGh(pr=pr_meta(author="pulumi-bot", branch=branch),
                                     files=[editions_sync_file()]), CONFIG)
        assert _gate(v, "review").status == "pending", branch
    # And the same branch from a human is reviewed like anything else.
    v = sentinel.evaluate(StubGh(pr=pr_meta(author="someone", branch="chore/sync-pulumi-editions"),
                                 files=[editions_sync_file()]), CONFIG)
    assert _gate(v, "review").status == "pending"


def test_bot_skip_mirrors_the_review_lane():
    """The Sentinel restates the lane's bot-author rule, so pin it to the
    workflow: a bot or branch added there and not here turns that lane's PRs
    into a G1 that never clears (or one that clears without a review)."""
    wf = (REPO_ROOT / ".github" / "workflows" / "claude-code-review.yml").read_text()
    end = wf.index('SKIP="bot-author"')
    block = wf[wf.rindex("elif [[", 0, end):end]
    authors = re.findall(r'"\$AUTHOR" == "([^"]+)"', block)
    branches = re.findall(r'"\$HEAD_BRANCH" != (\S+)\*', block)
    assert authors and branches, block
    assert sorted(authors) == sorted(sentinel.REVIEW_LANE_SKIPPED_BOTS)
    assert sorted(branches) == sorted(sentinel.REVIEW_LANE_REVIEWED_BOT_BRANCHES)
    # The lane only fires after triage, which lets pulumi-bot through on its
    # own list of branches. A branch on one list and not the other is a PR
    # the Sentinel waits on for a review that never starts.
    triage = (REPO_ROOT / ".github" / "workflows" / "claude-triage.yml").read_text()
    triage_branches = re.findall(r"startsWith\(github\.event\.pull_request\.head\.ref, '([^']+)'\)", triage)
    assert sorted(triage_branches) == sorted(sentinel.REVIEW_LANE_REVIEWED_BOT_BRANCHES)


def test_a_zero_file_pr_is_red_in_every_lane():
    """Every lane would wave an empty diff through: the review lane skips it,
    G3 has nothing to route, and on a fork G1/G2 skip as well — a green
    Sentinel with nobody involved, and over a real diff whenever the files
    API reads empty mid-computation."""
    lanes = {
        "internal": pr_meta(),
        "fork": pr_meta(head_repo="someone/docs"),
        "trivial": pr_meta(labels=["review:trivial"]),
        "frontmatter-only": pr_meta(labels=["review:frontmatter-only"]),
        "bot": pr_meta(author="pulumi-bot", branch="chore/x"),
    }
    for lane, meta in lanes.items():
        v = sentinel.evaluate(StubGh(pr=meta, files=[]), CONFIG)
        g1 = _gate(v, "review")
        assert g1.status == "red", (lane, g1.message)
        assert "changes no files" in g1.message
        assert v.conclusion == "failure", lane


def test_triage_redispatches_the_sentinel_when_a_label_it_reads_moves():
    """Triage writes labels with the GITHUB_TOKEN, which fires no `labeled`
    event, so the Sentinel's label filter never sees them. Triage has to
    poke the Sentinel itself for every label it moves that G1 reads."""
    wf = (REPO_ROOT / ".github" / "workflows" / "claude-triage.yml").read_text()
    m = re.search(r"for SENTINEL_LABEL in ([^;]+); do", wf)
    assert m, "triage's re-dispatch loop is gone"
    moved = set(m.group(1).split())
    for label in (sentinel.TRIVIAL_LABEL, sentinel.FRONTMATTER_ONLY_LABEL, sentinel.PROSE_FLAGGED_LABEL):
        assert label in moved, label


def test_infra_needs_staging_status_g4():
    card = author_card([], state=_state_with([]))
    base = dict(pr=pr_meta(), files=[infra_file()], comments=[card],
                reviews=[approval("tools-member")],
                memberships={("docs-tools", "tools-member"): "active"})
    v_red = sentinel.evaluate(StubGh(**base), CONFIG)
    assert _gate(v_red, "staging").status == "red"
    assert "/deploy-staging" in _gate(v_red, "staging").message
    assert v_red.conclusion == "failure"

    v_ok = sentinel.evaluate(
        StubGh(**base, statuses=[{"context": "staging/pulumi-test-io", "state": "success",
                   "creator": {"login": "github-actions[bot]"}}]),
        CONFIG)
    assert _gate(v_ok, "staging").status == "ok"
    assert v_ok.conclusion == "success", v_ok.to_json()


def _waive_events(actor="cam"):
    return [{"event": "labeled", "label": {"name": "review:waived"},
             "actor": {"login": actor}}]


def test_waived_success_with_banner_and_actor():
    gh = StubGh(pr=pr_meta(labels=["review:waived"]), files=[docs_file_substantive()],
                label_events=_waive_events("cam"),
                memberships={("docs-tools", "cam"): "active"})
    v = sentinel.evaluate(gh, CONFIG)
    assert v.conclusion == "success"
    assert "WAIVED by @cam" in v.summary


def test_waive_honored_from_any_routing_team_not_just_the_required_one():
    """A marketing-team member may waive a docs PR, which routes to docs-guild.

    Scoping the waive to the PR's own required team would make it exactly as
    hard to obtain as the approval it bypasses — useless for the case it
    exists to cover (the required approver is the author).
    """
    gh = StubGh(pr=pr_meta(labels=["review:waived"]), files=[docs_file_substantive()],
                label_events=_waive_events("marketer"),
                memberships={("docs-marketing-review", "marketer"): "active"})
    v = sentinel.evaluate(gh, CONFIG)
    assert v.conclusion == "success", v.to_json()
    assert "WAIVED by @marketer" in v.summary


def test_waive_from_a_non_team_member_is_refused_and_says_so():
    gh = StubGh(pr=pr_meta(labels=["review:waived"]), files=[docs_file_substantive()],
                label_events=_waive_events("randopasserby"))
    v = sentinel.evaluate(gh, CONFIG)
    assert v.conclusion == "pending", v.to_json()
    assert "NOT honored" in v.summary
    assert "randopasserby" in v.summary
    assert "WAIVED by" not in v.summary


def test_waive_with_unreadable_membership_is_refused_not_granted():
    """Fail closed: an API failure must never widen who can waive."""
    gh = StubGh(pr=pr_meta(labels=["review:waived"]), files=[docs_file_substantive()],
                label_events=_waive_events("cam"),
                membership_error_users=["cam"])
    v = sentinel.evaluate(gh, CONFIG)
    assert v.conclusion != "success", v.to_json()
    assert "NOT honored" in v.summary


def test_waive_with_unreadable_actor_is_refused():
    gh = StubGh(pr=pr_meta(labels=["review:waived"]), files=[docs_file_substantive()],
                label_events=[])
    v = sentinel.evaluate(gh, CONFIG)
    assert v.conclusion != "success", v.to_json()
    assert "NOT honored" in v.summary


def test_waive_covers_infra_evidence():
    """#22524: the staging workflow was disabled, so G4 could never go green,
    and a waive that stopped at G4 left two approvers with no lever. A waive
    clears G4 like any other gate, and the summary says what was skipped."""
    gh = StubGh(pr=pr_meta(labels=["review:waived"]), files=[infra_file()],
                label_events=_waive_events("cam"),
                memberships={("docs-tools", "cam"): "active"})
    v = sentinel.evaluate(gh, CONFIG)
    assert _gate(v, "staging").status == "red", "the row still records what was bypassed"
    assert v.conclusion == "success", v.to_json()
    assert v.title == "Waived by cam"
    assert "The staging gate was red" in v.summary
    st = {x["context"]: x for x in v.to_json()["gate_statuses"]}
    assert st["Sentinel / staging"]["state"] == "success"
    assert st["Sentinel / staging"]["description"].startswith("waived:")


# ---- G4: the deploy run is evidence, not just the status ----------------


def _deploy_run(conclusion="success", run_id=99):
    return {"id": run_id, "conclusion": conclusion,
            "html_url": f"https://github.com/pulumi/docs/actions/runs/{run_id}"}


def test_g4_accepts_a_successful_deploy_run_when_the_status_is_missing():
    gh = StubGh(pr=pr_meta(), files=[infra_file()],
                reviews=[approval("tools-member")],
                memberships={("docs-tools", "tools-member"): "active"},
                workflow_runs=[_deploy_run()])
    g4 = _gate(sentinel.evaluate(gh, CONFIG), "staging")
    assert g4.status == "ok", g4
    assert "run 99" in g4.message


def test_g4_ignores_a_failed_deploy_run():
    gh = StubGh(pr=pr_meta(), files=[infra_file()],
                workflow_runs=[_deploy_run(conclusion="failure")])
    assert _gate(sentinel.evaluate(gh, CONFIG), "staging").status == "red"


def test_g4_takes_a_success_among_several_runs_at_this_head():
    """'Deployed at least once' — an earlier red run doesn't erase a green one."""
    gh = StubGh(pr=pr_meta(), files=[infra_file()],
                workflow_runs=[_deploy_run(conclusion="failure", run_id=1),
                               _deploy_run(conclusion="success", run_id=2)])
    assert _gate(sentinel.evaluate(gh, CONFIG), "staging").status == "ok"


def test_g4_skips_an_infra_subject_path_that_is_not_a_staging_path():
    """PR #21698: two blog posts and a redirect data file. `domain:infra`
    routes the redirect file to tools, correctly — but the file is not on
    `staging_evidence.paths`, so G4 must not demand a deploy for it.

    Before staging evidence keyed on paths, this PR went red on G4 and the
    dispatched deploy raced a master push for the shared `www-testing` stack
    and died on a 409, so the gate that could never be satisfied was also
    the gate reporting the failure.
    """
    card = author_card([], state=_state_with([]))
    gh = StubGh(pr=pr_meta(), files=[infra_data_file()], comments=[card],
                reviews=[approval("tools-member")],
                memberships={("docs-tools", "tools-member"): "active"})
    v = sentinel.evaluate(gh, CONFIG)
    assert _gate(v, "staging").status == "skip"
    # Still tools' to approve — this narrows the evidence, not the approver.
    assert v.conclusion == "success", v.to_json()


def test_g4_arms_for_the_whole_pr_when_one_path_qualifies():
    """Per path, not per PR: a deploy-touching file anywhere in the diff
    arms the gate even alongside exempt ones."""
    gh = StubGh(pr=pr_meta(), files=[infra_data_file(), infra_file()])
    assert _gate(sentinel.evaluate(gh, CONFIG), "staging").status == "red"


def test_an_unattributed_staging_status_is_not_evidence():
    """A commit status needs only push access:

        gh api repos/OWNER/REPO/statuses/SHA -f state=success \
          -f context=staging/pulumi-test-io

    …which made G4 a one-line bypass that, unlike a waive, leaves no trace.
    The run record cannot be forged that way.
    """
    base = dict(pr=pr_meta(), files=[infra_file()],
                comments=[author_card([], state=_state_with([]))])
    forged = sentinel.evaluate(StubGh(**dict(base, statuses=[
        {"context": "staging/pulumi-test-io", "state": "success",
         "creator": {"login": "someone"}}])), CONFIG)
    assert _gate(forged, "staging").status == "red"

    unattributed = sentinel.evaluate(StubGh(**dict(base, statuses=[
        {"context": "staging/pulumi-test-io", "state": "success"}])), CONFIG)
    assert _gate(unattributed, "staging").status == "red"

    # The real writer still works, and the run-record witness is unaffected.
    real = sentinel.evaluate(StubGh(**dict(base, statuses=[
        {"context": "staging/pulumi-test-io", "state": "success",
         "creator": {"login": "github-actions[bot]"}}])), CONFIG)
    assert _gate(real, "staging").status == "ok"


def test_a_waive_clears_an_error_and_g4():
    """`any_error` used to be tested before `waived`, so a gate that errored
    held an honored waive at action_required under a summary claiming
    WAIVED. This models ONE approver's lookup failing; a full outage of the
    org token refuses the waive too (see the next test)."""
    waive_events = [{"event": "labeled", "label": {"name": "review:waived"},
                     "actor": {"login": "boss"}}]
    base = dict(pr=pr_meta(labels=["review:waived"]),
                files=[docs_file_substantive()],
                label_events=waive_events,
                memberships={("docs-guild", "boss"): "active"})

    # G3 errors (token cannot read membership for the approver) — waived wins.
    errored = sentinel.evaluate(StubGh(**dict(
        base, reviews=[approval("flaky")], membership_error_users={"flaky"})), CONFIG)
    assert errored.conclusion == "success", errored.to_json()
    assert errored.title == "Waived by boss"

    infra = sentinel.evaluate(StubGh(**dict(base, files=[infra_file()])), CONFIG)
    assert infra.conclusion == "success", infra.to_json()
    assert infra.title == "Waived by boss"


def test_an_org_token_outage_refuses_the_waive_and_says_the_way_through():
    """The waive's authorization reads the org-scoped token, so an outage
    refuses it. Fail-closed on purpose; the comment names an admin's merge
    and doesn't recommend a waive that can't work."""
    gh = StubGh(pr=pr_meta(labels=["review:waived"]), files=[docs_file_substantive()],
                label_events=_waive_events("chris"), membership_error_users={"chris"})
    v = sentinel.evaluate(gh, CONFIG)
    assert not v.waived and v.conclusion == "pending"
    assert v.title.startswith("review:waived refused"), v.title
    assert "NOT honored" in v.summary
    assert "a re-applied waive fails the same way" in v.summary, "retrying can't help in an outage"
    assert "repo admin merging past the check" in v.summary


def test_g5_needs_no_org_token():
    """G5 reads GitHub's author_association, never a permission endpoint."""
    gh = StubGh(pr=pr_meta(labels=["review:oversized"]), files=[docs_file_substantive()],
                reviews=[approval("mkt", body=sentinel.OVERSIZED_ACK)],
                permission_error_users={"mkt"})
    assert _gate(sentinel.evaluate(gh, CONFIG), "oversized").status == "ok"
    assert gh.permission_calls == []


def test_merge_box_title_says_what_the_merge_waits_on():
    """#22524: "2 gate(s) red" sent people to a Details page that started
    with the reviewer brief. The title is the only line most people read."""
    stale = author_card([], state=_state_with([]), head="b" * 40)
    v = sentinel.evaluate(StubGh(pr=pr_meta(), files=[infra_file()], comments=[stale],
                                 reviews=[approval("chris", commit_id="b" * 40)]), CONFIG)
    assert v.title == "Waiting on a current review (/update-review); a staging deploy", v.title
    assert len(v.title) <= 140

    findings = author_card([("F1", "must"), ("F2", "answer")])
    v2 = sentinel.evaluate(StubGh(pr=pr_meta(), files=[docs_file_substantive()],
                                  comments=[findings, brief_comment()]), CONFIG)
    assert "answers to 2 findings (/update-review)" in v2.title, v2.title
    assert v2.summary.index("| Gate |") < v2.summary.index("Summary text."), "table first"


def test_refused_waive_shows_where_people_look():
    gh = StubGh(pr=pr_meta(labels=["review:waived"]), files=[docs_file_substantive()],
                label_events=_waive_events("rob"))
    v = sentinel.evaluate(gh, CONFIG)
    assert v.title.startswith("review:waived refused · Waiting on"), v.title
    assert "NOT honored" in v.summary and "@rob is not an active member" in v.summary
    assert "removes the label and applies it again" in v.summary


def test_break_glass_is_offered_on_an_error_it_can_clear():
    """A corrupt REVIEW_STATE errors G2 with no red gate; the waive clears it,
    so the comment has to say it exists."""
    card = author_card([("F1", "must")])
    card["body"] = card["body"].replace("<!-- REVIEW_STATE ", "<!-- REVIEW_STATE {broken ")
    v = sentinel.evaluate(StubGh(pr=pr_meta(), files=[docs_file_substantive()],
                                 comments=[card]), CONFIG)
    assert v.conclusion == "action_required"
    assert v.title.startswith("Couldn't check the review's answers"), v.title
    assert sentinel.BREAK_GLASS in v.summary


# ---- Pushes that change nothing: G3 and G4 carry like G1 ----------------

EARLIER = "c" * 40
MERGED = "d" * 40


def _based_pr():
    meta = pr_meta()
    meta["base"]["ref"] = "master"
    return meta


def _treed(sha, tree, parents=1, on="p"):
    """`on`: the first parent. An empty commit must sit on the one before it."""
    return {"sha": sha, "parents": [{"sha": on}] + [{"sha": "base"}] * (parents - 1),
            "commit": {"tree": {"sha": tree}}}


def _moved(f):
    """The same change after the base moved: new hunk header and context,
    the PR's own +/- lines untouched."""
    lines = f["patch"].splitlines()
    body = [ln if ln[:1] in "+-" else " moved context" for ln in lines[1:]]
    return dict(f, patch="\n".join(["@@ -90,2 +90,3 @@"] + body))


def test_a_staging_deploy_carries_across_update_branch():
    """#22506 also spent a second ~10-minute deploy of the shared stack to
    re-prove a change the first deploy had already applied."""
    card = author_card([], state=_state_with([]))
    base = dict(pr=_based_pr(), files=[infra_file()], comments=[card],
                reviews=[approval("chris")], permissions={"chris": "write"},
                statuses_by_sha={}, workflow_runs_by_sha={EARLIER: [_deploy_run()]})
    v = sentinel.evaluate(StubGh(**base, commits=[_treed(EARLIER, "t1"), _treed(HEAD, "t2", 2)],
                                 compare={EARLIER: [_moved(infra_file())]}), CONFIG)
    g4 = _gate(v, "staging")
    assert g4.status == "ok" and "only base merges, rebases or no-op commits" in g4.message, g4
    assert f"at `{EARLIER[:9]}`" in g4.message
    assert v.conclusion == "success", v.to_json()

    changed = dict(infra_file(), patch="@@ -1,1 +1,1 @@\n-echo a\n+echo c")
    v2 = sentinel.evaluate(StubGh(**base, commits=[_treed(EARLIER, "t1"), _treed(HEAD, "t2", 2)],
                                  compare={EARLIER: [changed]}), CONFIG)
    assert _gate(v2, "staging").status == "red"
    v3 = sentinel.evaluate(StubGh(**base, commits=[_treed(EARLIER, "t1"), _treed(HEAD, "t9")],
                                  compare={EARLIER: [infra_file()]}), CONFIG)
    assert _gate(v3, "staging").status == "red", "a content commit needs its own deploy"


def test_history_allows_carry_across_a_rebase_but_not_a_content_commit():
    """#22397: a rebase took the reviewed head out of the commit list, and the
    carry asked for it to be there. Gone from the list now means "maybe a
    rebase", and `same_diff` decides; a later content commit still blocks."""
    rebased = [_treed("9" * 40, "t1"), _treed(HEAD, "t2")]
    assert sentinel.history_allows_carry(rebased, EARLIER) is True
    assert sentinel.history_allows_carry([_treed(EARLIER, "t1"), _treed(HEAD, "t9")], EARLIER) is False
    assert sentinel.history_allows_carry([], EARLIER) is False, "an unread list says nothing"
    assert sentinel.history_allows_carry(rebased, "") is False


def test_a_staging_deploy_carries_across_a_rebase_with_the_same_diff():
    card = author_card([], state=_state_with([]))
    carry = sentinel._Carry(StubGh(pr=_based_pr(), files=[infra_file()], comments=[card],
                                   commits=[_treed("9" * 40, "t1"), _treed(HEAD, "t2")],
                                   compare={EARLIER: [_moved(infra_file())]}),
                            _based_pr(), [infra_file()])
    assert carry.unchanged_since(EARLIER) is True
    changed = dict(infra_file(), patch="@@ -1,1 +1,1 @@\n-echo a\n+echo c")
    carry2 = sentinel._Carry(StubGh(pr=_based_pr(), files=[infra_file()],
                                    commits=[_treed("9" * 40, "t1"), _treed(HEAD, "t2")],
                                    compare={EARLIER: [changed]}),
                             _based_pr(), [infra_file()])
    assert carry2.unchanged_since(EARLIER) is False


def test_no_approval_gate_any_more():
    """G3 is gone: branch protection decides who can approve and merge."""
    card = author_card([], state=_state_with([]))
    v = sentinel.evaluate(StubGh(pr=pr_meta(), files=[docs_file_substantive()], comments=[card]), CONFIG)
    assert [g.name for g in v.gates] == ["review", "findings", "staging", "oversized"]
    assert v.conclusion == "success", v.to_json()


def test_g5_ack_ignores_bots_the_author_and_read_only_accounts():
    base = dict(pr=pr_meta(labels=["review:oversized"], author="writer"), files=[docs_file_substantive()])
    ack = f"read it\n{sentinel.OVERSIZED_ACK}"
    for reviews, perms in (([approval("writer", body=ack)], {"writer": "write"}),
                           ([approval("pulumi-bot", body=ack)], {"pulumi-bot": "admin"}),
                           ([approval("some-app[bot]", utype="Bot", body=ack)], {"some-app[bot]": "write"}),
                           ([approval("rando", body=ack, assoc="CONTRIBUTOR")], {}),
                           ([approval("late", body=ack, commit_id="b" * 40)], {"late": "write"})):
        v = sentinel.evaluate(StubGh(**base, reviews=reviews, permissions=perms), CONFIG)
        assert _gate(v, "oversized").status == "red", (reviews[0]["user"], _gate(v, "oversized"))
    v = sentinel.evaluate(StubGh(**base, reviews=[approval("mkt", body=ack)], permissions={"mkt": "maintain"}), CONFIG)
    assert _gate(v, "oversized").status == "ok" and "`mkt`" in _gate(v, "oversized").message


def test_each_gate_gets_its_own_short_commit_status():
    """#22397: the merge box said only "Waiting on answers to 1 finding", and
    the comment that said how was scrolled out of sight."""
    card = author_card([("F1", "must")])
    card["html_url"] = "https://github.com/pulumi/docs/pull/1#issuecomment-9"
    v = sentinel.evaluate(StubGh(pr=pr_meta(), files=[docs_file_substantive()], comments=[card]), CONFIG)
    st = {g["context"]: g for g in v.to_json()["gate_statuses"]}
    assert set(st) == {"Sentinel / review", "Sentinel / findings", "Sentinel / staging", "Sentinel / oversized"}
    f = st["Sentinel / findings"]
    assert f["state"] == "failure" and "/update-review accept F1" in f["description"], f
    assert f["target_url"] == card["html_url"]
    assert st["Sentinel / staging"]["state"] == "success" and st["Sentinel / staging"]["target_url"] is None
    assert all(len(g["description"]) <= sentinel.STATUS_DESCRIPTION_MAX for g in st.values())
    preview = sentinel.evaluate(StubGh(pr=pr_meta(), files=[docs_file_substantive()], comments=[card]),
                                CONFIG, report_only=True)
    pst = {g["context"]: g for g in preview.to_json()["gate_statuses"]}
    assert pst["Sentinel / findings"]["state"] == "success"
    assert pst["Sentinel / findings"]["description"].startswith("Preview, not enforced:")


def test_staging_never_tells_anyone_to_dispatch_a_workflow():
    """#22524: someone looking for the staging deploy dispatched production.
    No staging state names a workflow or a dispatch command, and each links
    where you act."""
    def g(**kw):
        return _gate(sentinel.evaluate(StubGh(pr=pr_meta(branch="me/topic"), files=[infra_file()], **kw),
                                       CONFIG), "staging")
    run = {"id": 9, "html_url": "https://github.com/pulumi/docs/actions/runs/9"}
    states = {
        "never ran": g(),
        "running": g(workflow_runs=[dict(run, status="in_progress", conclusion=None)]),
        "failed": g(workflow_runs=[dict(run, status="completed", conclusion="failure")]),
        "disabled": g(workflow_state="disabled_manually"),
        "unreadable": g(workflow_runs_error=True, workflow_state_error=True),
    }
    for name, gate in states.items():
        for banned in ("gh workflow run", "Build and deploy", "build-and-deploy.yml", "--ref"):
            assert banned not in gate.message and banned not in gate.short, (name, banned, gate)
        assert len(gate.short) <= sentinel.STATUS_DESCRIPTION_MAX
    assert states["never ran"].status == "red" and "/deploy-staging" in states["never ran"].short
    assert states["unreadable"].status == "red" and "/deploy-staging" in states["unreadable"].message
    assert states["running"].status == "pending" and states["running"].url.endswith("/runs/9")
    assert states["failed"].status == "red" and "Re-run failed jobs" in states["failed"].short
    assert states["failed"].url.endswith("/runs/9")
    assert states["disabled"].status == "red" and "turned off" in states["disabled"].short


def test_a_running_staging_deploy_is_a_pending_status_not_a_failure():
    run = {"id": 9, "html_url": "https://github.com/pulumi/docs/actions/runs/9", "status": "queued"}
    v = sentinel.evaluate(StubGh(pr=pr_meta(), files=[infra_file()], workflow_runs=[run]), CONFIG)
    st = {x["context"]: x for x in v.to_json()["gate_statuses"]}
    assert st["Sentinel / staging"]["state"] == "pending"
    assert st["Sentinel / staging"]["target_url"].endswith("/runs/9")
    assert v.conclusion == "pending" and "a staging deploy (running)" in v.title


def test_gate_details_links_go_where_you_act():
    card = author_card([("F1", "must")])
    card["html_url"] = "https://github.com/pulumi/docs/pull/1#issuecomment-9"
    pr = dict(pr_meta(labels=["review:oversized"]), html_url="https://github.com/pulumi/docs/pull/1")
    v = sentinel.evaluate(StubGh(pr=pr, files=[infra_file()], comments=[card]), CONFIG)
    st = {x["context"]: x["target_url"] for x in v.to_json()["gate_statuses"]}
    assert st["Sentinel / review"] == card["html_url"] and st["Sentinel / findings"] == card["html_url"]
    assert st["Sentinel / oversized"] == "https://github.com/pulumi/docs/pull/1/files"
    assert st["Sentinel / staging"] == "https://github.com/pulumi/docs/pull/1"
    assert not any("/actions/runs/" in u for u in st.values() if u), "never the Sentinel's own run"


def test_g4_quotes_the_last_failed_staging_attempt():
    """A failed dispatch or deploy writes its reason to the staging status;
    the G4 row leads with it instead of leaving it in a job log."""
    failed = {"context": "staging/pulumi-test-io", "state": "error",
              "creator": {"login": "github-actions[bot]"},
              "description": "Not dispatched: testing-build-and-deploy.yml is disabled.",
              "target_url": "https://github.com/pulumi/docs/actions/runs/7"}
    gh = StubGh(pr=pr_meta(), files=[infra_file()], statuses=[failed])
    g4 = _gate(sentinel.evaluate(gh, CONFIG), "staging")
    assert g4.status == "red"
    assert g4.message.startswith(
        "**Last staging attempt: Not dispatched: testing-build-and-deploy.yml is disabled.**")
    assert "actions/runs/7" in g4.message

    # Only the NEWEST trusted status speaks: a newer green one is evidence,
    # and an untrusted failure is ignored like an untrusted success.
    newer_green = dict(failed, state="success", description="staging deploy green")
    assert _gate(sentinel.evaluate(StubGh(pr=pr_meta(), files=[infra_file()],
                                          statuses=[newer_green, failed]), CONFIG),
                 "staging").status == "ok"
    forged = dict(failed, creator={"login": "someone"})
    g4 = _gate(sentinel.evaluate(StubGh(pr=pr_meta(), files=[infra_file()],
                                        statuses=[forged]), CONFIG), "staging")
    assert "Last staging attempt" not in g4.message


def test_g4_ok_never_reads_the_workflow_state():
    """The state read is advice for a red gate, not part of the verdict."""
    gh = StubGh(pr=pr_meta(), files=[infra_file()], workflow_runs=[_deploy_run()],
                workflow_state_error=True)
    assert _gate(sentinel.evaluate(gh, CONFIG), "staging").status == "ok"


def test_g4_run_lookup_failure_blocks_rather_than_erroring():
    """An unreadable run history is 'no evidence', not action_required.

    Red is already the conservative answer here; escalating to
    action_required would misreport an API hiccup as a corrupt PR.
    """
    gh = StubGh(pr=pr_meta(), files=[infra_file()], workflow_runs_error=True)
    assert _gate(sentinel.evaluate(gh, CONFIG), "staging").status == "red"


# ---- Pinned status comment ----------------------------------------------


def _status_copies(gh):
    return [c for c in gh.comments
            if sentinel.STATUS_MARKER in (c.get("body") or "").splitlines()[:3]]


class _RacedGh(StubGh):
    """The run we raced lists, finds nothing, and posts between our listing
    and our POST, so its copy is the older one."""

    def post_issue_comment(self, body):
        if not self.posted:
            self.comments.append({"id": 5, "body": sentinel.STATUS_MARKER + "\nthe other run\n",
                                  "user": {"login": sentinel.BOT_LOGIN, "type": "Bot"}})
        super().post_issue_comment(body)


class _AlreadyGoneGh(StubGh):
    def delete_issue_comment(self, comment_id):
        raise sentinel.SentinelDataError(
            f"gh api repos/pulumi/docs/issues/comments/{comment_id} failed (exit 1): "
            "HTTP 404: Not Found")


def test_the_oversized_ack_must_come_from_a_qualifying_approver():
    """`review:oversized` skips G1 and G2 and nothing verifies the PR is
    actually oversized, so G5 is the only thing left. It read the ack from
    the unfiltered approver list — anyone with read access can post an
    APPROVED review, so a bystander could supply the magic string while a
    real team member clicked plain Approve."""
    base = dict(pr=pr_meta(labels=["review:oversized"]),
                files=[docs_file_substantive()],
                permissions={"guild": "write"})

    bystander = sentinel.evaluate(StubGh(**dict(base, reviews=[
        approval("guild"),
        approval("randomer", body=f"lgtm\n{sentinel.OVERSIZED_ACK}", assoc="NONE"),
    ])), CONFIG)
    assert _gate(bystander, "oversized").status == "red"

    proper = sentinel.evaluate(StubGh(**dict(base, reviews=[
        approval("guild", body=f"read it all\n{sentinel.OVERSIZED_ACK}"),
    ])), CONFIG)
    assert _gate(proper, "oversized").status == "ok"


def test_role_comments_must_come_from_the_bot():
    """G1 and G2 were fully author-controllable until this check existed.

    `_find_comment` matched the marker anywhere in any comment by anyone and
    returned the first hit. Comments come back oldest-first, so a PR author
    who commented before the review lane posted owned both gates for the
    life of the PR — and `update_strip` then wrote the ⛔ banner into the
    forgery, so the real card never showed it.

    The rule is the one the writer already enforces: bot-authored, marker as
    an exact line in the first three (`pinned-comment.sh list_role_comments`).
    """
    real = author_card([("F1", "must"), ("F2", "must")], state=_state_with([]))
    real["user"] = {"login": sentinel.BOT_LOGIN, "type": "Bot"}
    forged = {
        "id": 1, "user": {"login": "attacker", "type": "User"},
        "body": (f"{sentinel.AUTHOR_MARKER}\n"
                 f"<!-- CLAUDE_REVIEW_HEAD {HEAD} -->\n"
                 "## Author action guide v1 — nothing blocks merge\n\n"
                 "### 🚨 Must fix or refute\n\n_Nothing to fix._\n"),
    }
    # Forgery first is the attacker's best case: oldest wins the lookup.
    v = sentinel.evaluate(
        StubGh(pr=pr_meta(author="attacker"), files=[docs_file_substantive()],
               comments=[forged, real]), CONFIG)
    assert _gate(v, "findings").status == "red"
    assert v.blocking_ids == ["F1", "F2"]

    # A bot comment that merely QUOTES the marker below line 3 is not a card.
    quoting = {
        "id": 2, "user": {"login": sentinel.BOT_LOGIN, "type": "Bot"},
        "body": "line1\nline2\nline3\n" + sentinel.AUTHOR_MARKER + "\n",
    }
    assert sentinel._find_comment([quoting], sentinel.AUTHOR_MARKER) is None
    assert sentinel._find_comment([real], sentinel.AUTHOR_MARKER) is real


def test_a_forged_legacy_page_is_not_a_review():
    """Same rule for the v2 lane, which anchored on the first line but not
    on the author — so a forged page could still stand in for a review."""
    forged = {"id": 1, "user": {"login": "attacker", "type": "User"},
              "body": "<!-- CLAUDE_REVIEW 1/1 -->\nnothing to see here\n"}
    assert sentinel.legacy_pages([forged]) is None


def test_a_waived_pr_takes_the_waived_branch_in_preview_too():
    """`conclusion` is always `neutral` in preview, so the branch reads
    `would_be`. Without that a waived PR fell through to the "gates need
    attention" headline the waive branch exists to prevent."""
    waived = StubGh(pr=pr_meta(labels=["review:waived"]),
                    files=[docs_file_substantive()],
                    label_events=_waive_events("cam"),
                    memberships={("docs-tools", "cam"): "active"})
    v = sentinel.evaluate(waived, CONFIG, report_only=True)
    assert v.would_be == "success" and "WAIVED" in v.summary


def test_the_status_comment_is_maintained_for_every_pr_in_report_only():
    """The `sentinel:preview` opt-in label is retired — no cohort, no gating.

    A dry run only visible to a canary cohort exercises the surface without
    exercising the readers, which is the half that actually needs testing.
    The banner is what makes writing everywhere safe.
    """
    assert not hasattr(sentinel, "PREVIEW_LABEL")
    assert "preview" not in sentinel.evaluate(
        StubGh(pr=pr_meta(), files=[docs_file_substantive()]),
        CONFIG, report_only=True).to_json()
    # The comments in those workflows still *name* the retired label, which is
    # the point of a retirement note; what must be gone is every place one is
    # read or applied. Shell usage quotes it, prose backticks it.
    wf = (REPO_ROOT / ".github" / "workflows" / "review-sentinel.yml").read_text()
    assert "github.event.label.name == 'sentinel:preview'" not in wf
    for lane in ("content-review-article.yml", "check-links.yml"):
        text = (REPO_ROOT / ".github" / "workflows" / lane).read_text()
        assert '"sentinel:preview"' not in text, lane


def test_oversized_ack_replaces_g1_g2():
    gh = StubGh(pr=pr_meta(labels=["review:oversized"]), files=[docs_file_substantive()],
                reviews=[approval("guild-member", body="LGTM\r\n/oversized-ack")],
                permissions={"guild-member": "write"})
    v = sentinel.evaluate(gh, CONFIG)
    assert _gate(v, "review").status == "skip"
    assert _gate(v, "oversized").status == "ok"
    assert v.conclusion == "success", v.to_json()

    gh2 = StubGh(pr=pr_meta(labels=["review:oversized"]), files=[docs_file_substantive()],
                 reviews=[approval("guild-member")],
                 permissions={"guild-member": "write"})
    v2 = sentinel.evaluate(gh2, CONFIG)
    assert _gate(v2, "oversized").status == "red"
    assert "/oversized-ack" in _gate(v2, "oversized").message


def test_oversized_ack_is_a_slash_command_not_a_substring():
    """`/oversized-ack` follows the review-command grammar: it starts a line.
    Mid-sentence, or spelled as the retired `sentinel:oversized-ack` token,
    it records no hand review."""
    def g5(body):
        gh = StubGh(pr=pr_meta(labels=["review:oversized"]), files=[docs_file_substantive()],
                    reviews=[approval("guild-member", body=body)],
                    permissions={"guild-member": "write"})
        return _gate(sentinel.evaluate(gh, CONFIG), "oversized").status

    assert g5("/oversized-ack") == "ok"
    assert g5("Read every file.\n/oversized-ack") == "ok"
    assert g5("/Oversized-Ack") == "ok"
    assert g5("LGTM /oversized-ack") == "red"
    assert g5("LGTM sentinel:oversized-ack") == "red"
    assert g5("/oversized-acknowledged") == "red"


def test_the_oversized_ack_instruction_says_where_the_string_goes():
    """"Include it in the approval body" left reviewers guessing which box
    that was, and the near misses all look like they should work. The red
    message names the box, the fix for an approval given without it, and
    what doesn't count."""
    gh = StubGh(pr=pr_meta(labels=["review:oversized"]), files=[docs_file_substantive()],
                reviews=[approval("guild-member")],
                permissions={"guild-member": "write"})
    msg = _gate(sentinel.evaluate(gh, CONFIG), "oversized").message
    for needle in (sentinel.OVERSIZED_ACK, "**Approve** review", "Approve again",
                   "earlier commit", "PR comment",
                   f"gh pr review <number> --approve --body {sentinel.OVERSIZED_ACK}"):
        assert needle in msg, needle

    numbered = StubGh(pr=dict(pr_meta(labels=["review:oversized"]), number=22251),
                      files=[docs_file_substantive()], reviews=[approval("guild-member")],
                      permissions={"guild-member": "write"})
    assert "gh pr review 22251 --approve" in _gate(sentinel.evaluate(numbered, CONFIG), "oversized").message


def test_approving_again_with_the_ack_clears_g5():
    """The red message tells a reviewer who approved without the string to
    approve again with it. That only holds because G3 reads each person's
    LATEST stateful review, so pin it."""
    gh = StubGh(pr=pr_meta(labels=["review:oversized"]), files=[docs_file_substantive()],
                reviews=[approval("guild-member"),
                         approval("guild-member", body=f"read by hand\n{sentinel.OVERSIZED_ACK}")],
                permissions={"guild-member": "write"})
    assert _gate(sentinel.evaluate(gh, CONFIG), "oversized").status == "ok"


def test_legacy_v2_comment_passes_g1_with_note_and_g2_counts():
    clean = {"id": 9, "user": {"login": "github-actions[bot]"},
             "body": (f"<!-- CLAUDE_REVIEW 1/1 -->\n## Pre-merge Review\n"
                      f"<!-- CLAUDE_REVIEW_HEAD {HEAD} -->\n"
                      "### 🚨 Outstanding in this PR\n\n_none_\n\n### 📜 Review history\n")}
    gh = StubGh(pr=pr_meta(), files=[docs_file_substantive()], comments=[clean],
                reviews=[approval("guild-member")],
                memberships={("docs-guild", "guild-member"): "active"})
    v = sentinel.evaluate(gh, CONFIG)
    assert _gate(v, "review").status == "ok" and "legacy" in _gate(v, "review").message
    assert _gate(v, "findings").status == "ok"
    assert v.conclusion == "success", v.to_json()

    dirty = dict(clean)
    dirty["body"] = clean["body"].replace(
        "_none_", "- **[L10-12]** `f.md` — broken thing")
    gh2 = StubGh(pr=pr_meta(), files=[docs_file_substantive()], comments=[dirty],
                 reviews=[approval("guild-member")],
                 memberships={("docs-guild", "guild-member"): "active"})
    v2 = sentinel.evaluate(gh2, CONFIG)
    assert _gate(v2, "findings").status == "red"
    assert v2.conclusion == "failure"


def test_report_only_wraps_neutral():
    gh = StubGh(pr=pr_meta(), files=[docs_file_substantive()])
    v = sentinel.evaluate(gh, CONFIG, report_only=True)
    assert v.conclusion == "neutral"
    assert v.would_be == "pending"
    assert "`pending`" in v.summary, "the real verdict rides in the summary"


def test_draft_neutral():
    gh = StubGh(pr=pr_meta(draft=True))
    v = sentinel.evaluate(gh, CONFIG)
    assert v.conclusion == "neutral"


def test_summary_embeds_brief_and_break_glass():
    gh = StubGh(pr=pr_meta(), files=[docs_file_substantive()], comments=[brief_comment()])
    v = sentinel.evaluate(gh, CONFIG)
    assert "Summary text." in v.summary
    assert "reviewer footer" not in v.summary
    # A review that's still running is pending: wait for it, no waive offered.
    assert "review:waived" not in v.summary
    stale = author_card([], state=_state_with([]), head="b" * 40)
    red = sentinel.evaluate(StubGh(pr=pr_meta(), files=[docs_file_substantive()],
                                   comments=[brief_comment(), stale]), CONFIG)
    assert _gate(red, "review").status == "red"
    assert "review:waived" in red.summary  # break-glass note on red rows


def test_update_strip_insert_replace_clear():
    card = author_card([("F1", "must")])
    gh = StubGh(pr=pr_meta(), files=[docs_file_substantive()], comments=[card])
    v = sentinel.evaluate(gh, CONFIG)
    assert sentinel.update_strip(gh, v, comments=[card]) is True
    _, patched = gh.patched[-1]
    assert "⛔" in patched and sentinel.STRIP_OPEN in patched
    assert "fix and push" in patched and "/update-review" in patched

    card2 = dict(card, body=patched)
    assert sentinel.update_strip(gh, v, comments=[card2]) is False  # idempotent

    ok = sentinel.Verdict(conclusion="success", title="", summary="", head_sha=HEAD)
    assert sentinel.update_strip(gh, ok, comments=[card2]) is True  # clears
    _, cleared = gh.patched[-1]
    assert "⛔" not in cleared and sentinel.STRIP_OPEN in cleared

    fresh_no_strip = author_card([], state=_state_with([]))
    assert sentinel.update_strip(gh, ok, comments=[fresh_no_strip]) is False


def test_strip_without_blocking_findings_says_what_merge_waits_on():
    """Only a deploy can clear G4. A strip reading "⛔ merge is blocked — fix
    and push, or reply /update-review" over a card reading "nothing blocks
    merge" contradicted the card and sent the author after nothing. It names
    the gate the merge waits on, and links the status comment, which sits
    above the card, not below it."""
    url = "https://github.com/pulumi/docs/pull/1#issuecomment-5"
    status = {"id": 5, "body": sentinel.STATUS_MARKER + "\n## Sentinel\n",
              "user": {"login": sentinel.BOT_LOGIN}, "html_url": url}
    card = author_card([], state=_state_with([]))
    gh = StubGh(pr=pr_meta(), files=[docs_file_substantive()], comments=[status, card])
    v = sentinel.Verdict(
        conclusion="failure", title="", summary="", head_sha=HEAD,
        gates=[sentinel.Gate("review", "ok", "current"),
               sentinel.Gate("staging", "red", "needs a deploy")])
    assert sentinel.update_strip(gh, v, comments=[status, card]) is True
    _, patched = gh.patched[-1]
    strip = patched.split(sentinel.STRIP_OPEN)[1].split(sentinel.STRIP_CLOSE)[0]
    assert "Merge is waiting on a staging deploy.**" in strip, strip
    assert "Each gate's status in the merge box says how." in strip, strip
    for wrong in ("blocked", "⛔", "fix and push", "/update-review", "below"):
        assert wrong not in strip, (wrong, strip)

    two = sentinel.Verdict(conclusion="failure", title="", summary="", head_sha=HEAD,
                           gates=v.gates + [sentinel.Gate("oversized", "red", "x")])
    sentinel.update_strip(gh, two, comments=[card])  # no status comment yet: no link
    strip = gh.patched[-1][1].split(sentinel.STRIP_OPEN)[1].split(sentinel.STRIP_CLOSE)[0]
    assert "waiting on a staging deploy and /oversized-ack in an approval.**" in strip, strip
    assert "Details:" not in strip, "the status comment it linked is gone"


def test_strip_lands_on_the_card_as_it_is_now_not_as_first_read():
    """Fork test of #22555: on a base merge the restamp moved the card's head
    marker while this run held an older copy, and writing the strip from that
    copy put the old head back, so G1 stayed red until the 2-hourly sweep."""
    old = author_card([], state=_state_with([]), head="b" * 40)
    restamped = dict(old, body=old["body"].replace("b" * 40, HEAD))
    gh = StubGh(pr=pr_meta(), files=[docs_file_substantive()], comments=[old])
    gh.fresh_bodies = {old["id"]: restamped["body"]}
    v = sentinel.Verdict(conclusion="failure", title="", summary="", head_sha=HEAD,
                         gates=[sentinel.Gate("staging", "red", "needs a deploy")])
    assert sentinel.update_strip(gh, v, comments=[old]) is True
    _, written = gh.patched[-1]
    assert f"<!-- CLAUDE_REVIEW_HEAD {HEAD} -->" in written and "b" * 40 not in written
    assert sentinel.STRIP_OPEN in written


def test_without_strip_ignores_only_the_strip():
    a = "## h\n\n<!-- SENTINEL_STRIP -->\n⏳ one\n<!-- /SENTINEL_STRIP -->\n\nbody"
    b = a.replace("⏳ one", "⏳ two")
    assert sentinel.without_strip(a) == sentinel.without_strip(b)
    assert sentinel.without_strip(a) != sentinel.without_strip(b.replace("body", "edited"))


def test_frontend_routes_to_marketing_without_staging():
    card = author_card([], state=_state_with([]))
    base = dict(pr=pr_meta(), files=[frontend_file()], comments=[card])
    v_red = sentinel.evaluate(StubGh(**base), CONFIG)
    assert _gate(v_red, "staging").status == "skip"
    v_ok = sentinel.evaluate(
        StubGh(**base, reviews=[approval("mkt")],
               memberships={("docs-marketing-review", "mkt"): "active"}),
        CONFIG)
    assert v_ok.conclusion == "success", v_ok.to_json()


def test_not_governed_dependabot_success_no_gates():
    gh = StubGh(pr=pr_meta(author="dependabot[bot]"))
    v = sentinel.evaluate(gh, CONFIG)
    assert v.conclusion == "success" and v.title == "Not governed"
    assert v.gates == [] and v.governed is False
    assert "not_governed.authors" in v.summary
    assert v.to_json()["governed"] is False


def test_not_governed_regen_needs_author_and_label():
    # pulumi-bot + automation/merge is a regen lane: not governed.
    v = sentinel.evaluate(StubGh(pr=pr_meta(author="pulumi-bot", labels=["automation/merge"])), CONFIG)
    assert v.conclusion == "success" and v.governed is False
    # pulumi-bot WITHOUT the label is a content-review PR: governed, and with
    # no review at head G1 is pending.
    v2 = sentinel.evaluate(StubGh(pr=pr_meta(author="pulumi-bot", branch="content-review/x"),
                                  files=[docs_file_substantive()]), CONFIG)
    assert v2.governed is True and _gate(v2, "review").status == "pending"
    # A human wearing the label is still governed.
    v3 = sentinel.evaluate(StubGh(pr=pr_meta(author="someone", labels=["automation/merge"]),
                                  files=[docs_file_substantive()]), CONFIG)
    assert v3.governed is True


def test_not_governed_report_only_wraps_neutral():
    v = sentinel.evaluate(StubGh(pr=pr_meta(author="dependabot[bot]")), CONFIG, report_only=True)
    assert v.conclusion == "neutral" and v.would_be == "success"


def test_workprentice_is_governed_and_routed_like_anyone_else():
    """The second-busiest bot author on the repo (a quarter of its bot PRs)
    was absent from the routing config entirely. It is not a
    `not_governed` lane — nothing auto-approves or auto-merges it — so it
    gets the full gate set."""
    gh = StubGh(pr=pr_meta(author="workprentice[bot]"), files=[docs_file_substantive()],
                comments=[v3_author_card(0), v3_brief(0)])
    v = sentinel.evaluate(gh, CONFIG)
    assert v.governed is True


def test_prose_flagged_still_demotes_mechanical():
    # A mechanical diff wearing the flag is substantive: review required.
    v2 = sentinel.evaluate(StubGh(pr=pr_meta(labels=["review:prose-flagged"]),
                                  files=[docs_file_mechanical()]), CONFIG)
    assert v2.mechanical is False
    assert _gate(v2, "review").status == "pending"
    # Without the flag the same diff is mechanical (G1 only).
    v3 = sentinel.evaluate(StubGh(pr=pr_meta(), files=[docs_file_mechanical()]), CONFIG)
    assert v3.mechanical is True and v3.to_json()["mechanical"] is True
    assert _gate(v3, "review").status == "ok"


def test_brief_has_no_checks_helper_is_gone():
    """It existed only for the clean-brief rule. `collect.py` still uses
    `_author_card_nothing_blocks`, which stays."""
    assert not hasattr(sentinel, "_brief_has_no_checks")
    assert hasattr(sentinel, "_author_card_nothing_blocks")


def test_workflow_has_no_concurrency_group_and_narrows_label_events():
    # A cancelled job renders as a failing check; the workflow must not own
    # a concurrency group (publish_guard.py handles overlap instead), and
    # label events must be limited to the labels the evaluator reads.
    wf = (REPO_ROOT / ".github" / "workflows" / "review-sentinel.yml").read_text()
    assert "cancel-in-progress:" not in wf
    assert "\nconcurrency:" not in wf
    for label in ("review:waived", "review:oversized", "review:trivial",
                  "review:frontmatter-only", "review:prose-flagged"):
        assert f"github.event.label.name == '{label}'" in wf, label


def test_review_error_without_a_review_is_red_not_pending():
    """`review:error` with no review means the run died: nothing is in
    flight, so don't say "the automated review is running"."""
    gh = StubGh(pr=pr_meta(labels=["review:error"]), files=[docs_file_substantive()])
    v = sentinel.evaluate(gh, CONFIG)
    g1 = _gate(v, "review")
    assert g1.status == "red" and "/new-review" in g1.message, g1.message
    assert v.conclusion == "failure"
    assert v.title == "Waiting on a current review (/new-review)", v.title
    st = {x["context"]: x for x in v.to_json()["gate_statuses"]}
    assert st["Sentinel / review"]["state"] == "failure"
    assert "review:waived" in v.summary  # red rows offer the break-glass again


def test_red_plus_pending_concludes_failure_and_pending_alone_writes_the_strip():
    """Any red gate wins over a pending one; a pending-only verdict still
    tells the author what the merge is waiting on."""
    run = {"id": 9, "html_url": "https://github.com/pulumi/docs/actions/runs/9", "status": "queued"}
    card = author_card([("F1", "must")])
    both = sentinel.evaluate(StubGh(pr=pr_meta(), files=[infra_file()], workflow_runs=[run],
                                    comments=[card]), CONFIG)
    assert _gate(both, "staging").status == "pending" and _gate(both, "findings").status == "red"
    assert both.conclusion == "failure", both.to_json()

    clean = author_card([], state=_state_with([]))
    gh = StubGh(pr=pr_meta(), files=[infra_file()], workflow_runs=[run], comments=[clean])
    v = sentinel.evaluate(gh, CONFIG)
    assert v.conclusion == "pending", v.to_json()
    assert sentinel.update_strip(gh, v, comments=[clean]) is True
    strip = gh.patched[-1][1].split(sentinel.STRIP_OPEN)[1].split(sentinel.STRIP_CLOSE)[0]
    assert "⏳ **Merge is waiting on a staging deploy (running).**" in strip, strip


def test_label_event_filter_covers_every_label_the_evaluator_reads():
    """Derived, not restated — a hardcoded list is how one went missing.

    `automation/merge` is read through the CONFIG
    (`not_governed.author_label_pairs`) rather than a constant in
    sentinel.py, so a list of sentinel.py's constants looked complete while
    omitting the label that flips the verdict hardest: present ⇒ success
    with no gates evaluated. Its lane applies it after opening the PR and
    then arms auto-merge, so the Sentinel stayed red and auto-merge never
    completed.
    """
    wf = (REPO_ROOT / ".github" / "workflows" / "review-sentinel.yml").read_text()
    cfg = routing.load_config(str(routing.DEFAULT_CONFIG_PATH))

    read_by_evaluator = {
        sentinel.PROSE_FLAGGED_LABEL,
        sentinel.TRIVIAL_LABEL,
        sentinel.FRONTMATTER_ONLY_LABEL,
        sentinel.OVERSIZED_LABEL,
        cfg.waive.get("label", "review:waived"),
    }
    # …plus every label the config can make load-bearing.
    for pair in (cfg.not_governed or {}).get("author_label_pairs") or []:
        read_by_evaluator.add(pair["label"])

    missing = [l for l in sorted(read_by_evaluator)
               if f"github.event.label.name == '{l}'" not in wf]
    # `review:error` is the exception: the review lanes set it inside their
    # own runs, and the Sentinel re-runs when those runs complete.
    for lane in ("Pre-merge Review (main)", "Pre-merge Review (update-review)"):
        assert f'"{lane}"' in wf.split("workflow_run:", 1)[1].split("workflow_dispatch:", 1)[0], lane
    for lane_file in ("claude-code-review.yml", "claude-update.yml"):
        lane_wf = (REPO_ROOT / ".github" / "workflows" / lane_file).read_text()
        assert sentinel.REVIEW_ERROR_LABEL in lane_wf, lane_file
    assert not missing, (
        "labels the evaluator reads that the workflow's label-event filter "
        f"drops (they only take effect on the next unrelated event): {missing}"
    )
    assert "publish_guard.py" in wf
    assert "steps.guard.outputs.publish == 'true'" in wf


def test_workflow_publishes_a_status_not_a_check_run():
    """`POST /check-runs` can't choose a check suite. GitHub filed the
    Sentinel's run into the oldest Actions suite at the head, whichever
    workflow created it; when that workflow ran again for the same event,
    the suite was superseded, and branch protection read "Expected — Waiting
    for status to be reported" on green, approved PRs (pulumi/docs#22308). A commit
    status belongs to no suite. The guard reads the run id back out of the
    status's `target_url`, so the publisher has to put the run URL there."""
    wf = (REPO_ROOT / ".github" / "workflows" / "review-sentinel.yml").read_text()
    assert "statuses: write" in wf
    assert "publish_verdict.py" in wf
    assert "--run-url \"${{ github.server_url }}/${{ github.repository }}/actions/runs/${{ github.run_id }}\"" in wf
    assert not re.search(r"--method POST[^\n]*check-runs", wf), "the Sentinel must not POST a check-run"


def test_workflow_never_checks_out_pr_code():
    wf = (REPO_ROOT / ".github" / "workflows" / "review-sentinel.yml").read_text()
    assert "pull_request_target" in wf
    for forbidden in ("github.event.pull_request.head.ref",
                      "github.event.pull_request.head.sha",
                      "refs/pull/", "merge_commit_sha"):
        assert forbidden not in wf, f"workflow must never reference PR code: {forbidden}"
    assert "default_branch" in wf  # checkout pinned to base default branch


def test_no_workflow_interpolates_pr_controlled_text_into_a_shell():
    """`${{ }}` is substituted textually BEFORE bash parses the script.

    So an author-controlled value written that way inside a `run:` block is
    not a string, it is script. A branch name is author-controlled and
    `git check-ref-format` accepts `"`, `$`, backtick, `;`, `&`, `|`, `(`,
    `)` and `'` — space is the only shell metacharacter it rejects, and
    `$IFS` covers that.

    staging-deploy-auto.yml and the since-retired comment-triggered staging
    lane both did this with `github.event.pull_request.head.ref`. The latter
    held `id-token: write` with ESC already authenticated, so the payload
    could mint an OIDC token and read the org-scoped PULUMI_BOT_TOKEN —
    repo-write escalating to org-scoped credentials.

    Both files' headers justified safety as "never checks out or executes PR
    code", which is true and beside the point: the VALUE is the vector, not
    the code. The rule is `env:` + "$VAR", which staging-status.yml already
    followed.

    SCOPE, honestly. This walks every workflow file, but it matches a
    DENYLIST of expressions against lines, not a structure. It therefore
    proves the named expressions are absent, not that no injection exists:
    a line-scanner cannot tell a `run:` block from a `concurrency: group:`,
    and the denylist has to be extended by hand. The structural form -- parse
    the YAML, walk every `run:` scalar, allow only a short list of
    non-author-controlled expressions -- reports 131 hits repo-wide today,
    mostly numeric ids and booleans, so it cannot land without a cleanup far
    wider than the change this test shipped with. Until then: adding an
    expression here is cheap, and doing so means fixing its sites in the
    same commit.
    """
    # Expressions whose value a PR author controls. `github.repository`,
    # `github.run_id` and `github.event.repository.default_branch` are NOT
    # author-controlled and stay allowed.
    author_controlled = (
        "github.event.pull_request.head.ref",
        "github.event.pull_request.title",
        "github.event.pull_request.body",
        "github.event.issue.title",
        "github.event.issue.body",
        "github.event.comment.body",
        "github.head_ref",
        "github.event.workflow_run.head_branch",
        # Dispatch inputs need write access to set, so these are defence in
        # depth rather than a fork vector -- but they are free text, and a
        # newline or `=` in one also forges other step outputs through
        # GITHUB_OUTPUT. pr_number had been hardened at two of five sites by
        # hand; the list not naming it is why the other three kept passing.
        # The other dispatch inputs (count, paths, force, dry_run, ...) are
        # deliberately not here yet -- see SCOPE in the docstring.
        "github.event.inputs.pr_number",
        "inputs.pr_number",
    )
    # Mapping keys whose VALUE is executed. Everything else that looks like
    # `key: ...` is exempt; these are not.
    EXECUTABLE_KEYS = {"run", "script", "args", "entrypoint", "cmd"}
    offenders = []
    wf_dir = REPO_ROOT / ".github" / "workflows"
    # BOTH extensions. The glob was `*.yml` only, so
    # scheduled-upstream-sync.yaml -- the one workflow written the other way
    # -- was exempt from a test whose docstring promises every workflow.
    for wf in sorted([*wf_dir.glob("*.yml"), *wf_dir.glob("*.yaml")]):
        for lineno, line in enumerate(wf.read_text().splitlines(), 1):
            stripped = line.strip()
            # Most YAML mapping entries are not shell lines, so they are
            # exempt: `env:` bindings are the safe form this test steers
            # people toward, `if:` is evaluated by GitHub and never by bash,
            # and `concurrency: group: foo-${{ ... }}` is a run-name.
            #
            # EXECUTABLE_KEYS is the carve-out from that carve-out, and it is
            # the whole reason the exemption is keyed on the NAME rather than
            # on shape. A single-line `run: echo ${{ github.head_ref }}` is
            # precisely the defect this test exists to catch, and it is also
            # a mapping entry. `with: script:` is the same hazard through
            # actions/github-script, which runs its value as JavaScript.
            #
            # (The original spelling required the `${{` to follow the colon
            # immediately, which caught single-line `run:` by accident and
            # false-positived on `group: name-${{ ... }}`. Widening it to any
            # mapping entry fixed the false positive and opened this hole;
            # naming the executable keys closes both.)
            if stripped.startswith("#") or "${{" not in line:
                continue
            key = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):(\s|$)", stripped)
            if key and key.group(1) not in EXECUTABLE_KEYS:
                continue
            for expr in author_controlled:
                if expr in line:
                    offenders.append(f"{wf.name}:{lineno}: {stripped[:90]}")
    assert not offenders, (
        "PR-controlled value interpolated outside an `env:` binding "
        "(use env: + \"$VAR\"):\n  " + "\n  ".join(offenders)
    )


def test_workflow_can_actually_write_the_comments_it_writes():
    """Comment writers need `pull-requests: write`, not `issues: write`.

    Both the pinned status comment and the ⛔ strip go through
    `/repos/{o}/{r}/issues/{n}/comments`, whose name is a trap: on a PR
    number that endpoint is governed by the pull_requests scope. The block
    asked for `issues: write` + `pull-requests: read` and read as correct
    for months because neither writer had ever run — the strip only fires
    when enforcing, and the status comment did not exist. The first real
    POST failed with exit 1 (PR #21642).
    """
    for name in ("review-sentinel.yml",):
        wf = (REPO_ROOT / ".github" / "workflows" / name).read_text()
        assert "pull-requests: write" in wf, (
            f"{name} posts comments on a PR and needs `pull-requests: write`; "
            "`issues: write` does not cover the /issues/{n}/comments endpoint "
            "when {n} is a pull request"
        )


def test_gh_failures_carry_the_reason():
    """A failed `gh` call must surface stderr, not just an exit code.

    CalledProcessError prints argv and a status; gh's explanation lives in
    stderr and was being discarded, which is what turned a one-line
    permission error into a log dive.
    """
    class _Failed:
        returncode = 1
        stdout = ""
        stderr = "gh: Resource not accessible by integration (HTTP 403)"

    gh = sentinel.Gh("pulumi/docs", 1)
    original = sentinel.subprocess.run
    sentinel.subprocess.run = lambda *a, **k: _Failed()
    try:
        gh.post_issue_comment("a" * 5000)
    except sentinel.SentinelDataError as exc:
        msg = str(exc)
        assert "403" in msg and "not accessible" in msg, msg
        assert "issues/1/comments" in msg, f"the endpoint should be named: {msg}"
        assert "aaaa" not in msg, "the rendered body must not be echoed into the error"
    else:  # pragma: no cover
        raise AssertionError("a non-zero gh exit must raise")
    finally:
        sentinel.subprocess.run = original


def test_sparse_checkout_covers_everything_the_evaluator_loads():
    """The sparse list is a dependency declaration, so pin it to reality.

    A full worktree is ~1.2 GB and checkout was the entire job runtime; the
    evaluator needs about 7 MB. The hazard of trimming it is a lazily
    `_load`ed module (validate-pinned.py is imported inside one branch) that
    goes missing for only the PRs whose code path reaches it. Resolve the
    paths sentinel.py names and assert each sits under a declared root, so
    a new dependency outside them fails here instead of in production.
    """
    import re as _re  # noqa: PLC0415

    wf = (REPO_ROOT / ".github" / "workflows" / "review-sentinel.yml").read_text()
    block = _re.search(r"sparse-checkout:\s*\|\n((?:\s+\S+\n)+)", wf)
    assert block, "review-sentinel.yml must declare a sparse-checkout list"
    roots = [line.strip() for line in block.group(1).splitlines() if line.strip()]
    assert "sparse-checkout-cone-mode: true" in wf

    src = (HERE / "sentinel.py").read_text()
    needed = {
        # `_load(..., _DOCS_REVIEW_SCRIPTS / "x.py")` and `_HERE / "y.py"`
        *(f".claude/commands/docs-review/scripts/{m}"
          for m in _re.findall(r'_DOCS_REVIEW_SCRIPTS / "([^"]+)"', src)),
        *(f"scripts/review-v3/{m}" for m in _re.findall(r'_HERE / "([^"]+)"', src)),
        # plus the ones imported by name off sys.path, and the config default
        "scripts/review-v3/routing.py",
        "scripts/review-v3/review_state.py",
        ".github/review-routing.yml",
        # compose-review.py reads these from its own parent directory
        ".claude/commands/docs-review/footer.md",
    }
    assert len(needed) > 5, "the path scrape found nothing — did sentinel.py change shape?"
    for rel in sorted(needed):
        assert (REPO_ROOT / rel).exists(), f"{rel} does not exist — fix the test, not the workflow"
        assert any(rel == r or rel.startswith(r.rstrip("/") + "/") for r in roots), \
            f"{rel} is loaded by sentinel.py but no sparse-checkout root covers it: {roots}"


# ---- Standalone harness --------------------------------------------------

def test_the_auto_staging_lane_dispatches_and_gets_out():
    """An evidence producer must never read as a failing check.

    The unattended lane used to sit in a `staging-stack` concurrency group
    for up to 45 minutes watching the deploy it dispatched. GitHub cancels a
    displaced pending run, and a cancelled job shows on the PR as a failing
    check -- on a PR whose only sin was a second push. The lane now fires
    the existing "Build and deploy testing" workflow and exits; that run
    writes its own `staging/pulumi-test-io` status.
    """
    auto = (REPO_ROOT / ".github" / "workflows" / "staging-deploy-auto.yml").read_text()
    import yaml as _yaml  # noqa: PLC0415
    jobs = _yaml.safe_load(auto)["jobs"]
    assert all("concurrency" not in j for j in jobs.values()), "a queued job is a job that gets cancelled"

    script = (REPO_ROOT / "scripts" / "review-v3" / "staging-deploy.sh").read_text()
    # The script is dispatch-only: nothing that calls it may hold a runner
    # open on the deploy. Match the command, not the prose.
    assert not any(ln.lstrip().startswith(("gh run watch", "if gh run watch"))
                   for ln in script.splitlines()), "staging-deploy.sh must not wait on the deploy"
    # stale comment guard: the header must not still promise a queue
    assert "Concurrency sits on the DEPLOY JOB" not in auto

    # The dispatched run must NOT resolve its own status: see
    # test_the_staging_status_listener_finalizes_from_the_default_branch.
    deploy = (REPO_ROOT / ".github" / "workflows" / "testing-build-and-deploy.yml").read_text()
    import yaml as _y  # noqa: PLC0415
    assert "staging-status" not in _y.safe_load(deploy)["jobs"], (
        "a job inside the dispatched run only exists for branches cut after it merged "
        "(workflow_dispatch runs the file from the ref it is dispatched at) -- "
        "staging-status.yml owns the terminal status"
    )


def test_the_staging_status_listener_finalizes_from_the_default_branch():
    """The finalize side has to be branch-age-independent, like the dispatch side.

    PR #21676 branched from 8712bb8b, before the in-run `staging-status` job
    merged. Its deploy succeeded; the file that run executed had no such job;
    the pending `staging/pulumi-test-io` status never resolved and the merge
    box sat on "staging deploy running". A `workflow_run` listener always
    executes the DEFAULT BRANCH's copy and fires for runs on any branch, so
    branch age stops mattering -- the same property `pull_request_target`
    gives review-sentinel.yml. These assertions pin that shape, and the
    no-PR-code invariant that comes with holding `statuses: write` on a run
    whose head is PR-controlled.
    """
    import yaml as _y  # noqa: PLC0415

    path = REPO_ROOT / ".github" / "workflows" / "staging-status.yml"
    wf = path.read_text()
    data = _y.safe_load(wf)

    # `on:` is the YAML 1.1 boolean True once parsed -- do not "fix" this.
    on = data[True]
    assert on["workflow_run"]["workflows"] == ["Build and deploy testing"]
    assert on["workflow_run"]["types"] == ["completed"]
    # Backfill entry: clear a phantom status without re-deploying (C).
    assert on["workflow_dispatch"]["inputs"]["run_id"]["required"] is True
    assert "pr_number" in on["workflow_dispatch"]["inputs"]

    assert "concurrency" not in data, "a displaced pending run is a CANCELLED run"
    jobs = data["jobs"]
    assert all("concurrency" not in j for j in jobs.values())

    for forbidden in ("head.ref", "head.sha", "refs/pull/", "merge_commit_sha"):
        assert forbidden not in wf, f"the listener must never reference PR code: {forbidden}"
    if "actions/checkout" in wf:
        assert "ref: ${{ github.event.repository.default_branch }}" in wf,             "any checkout here must be pinned to the default branch"

    gate = jobs["finalize"]["if"]
    assert "github.event.workflow_run.event == 'workflow_dispatch'" in gate,         "a master push deploy is nobody's staging evidence"
    assert "github.event.workflow_run.head_branch != github.event.repository.default_branch" in gate

    assert 'context="staging/pulumi-test-io"' in wf
    assert "statuses: write" in wf
    for desc in ("staging deploy green", "staging deploy failed", "staging deploy cancelled"):
        assert desc in wf, f"the in-run job's description is part of the contract: {desc}"
    # G4 is only re-scored when the Sentinel runs, and a deploy finishing
    # fires no PR event -- so the poke is the other half of this fix.
    assert "gh workflow run review-sentinel.yml" in wf
    assert "vars.REVIEW_V3_SENTINEL == 'report' || vars.REVIEW_V3_SENTINEL == '1'" in wf

    # GitHub's default shell is `bash -e`, no pipefail (PR #21676, F2).
    for step in jobs["finalize"]["steps"]:
        if "run" in step and "|" in step["run"]:
            assert "pipefail" in step["run"], \
                f"step {step.get('name')!r} pipes without `set -o pipefail`"


def test_staging_deploy_writes_no_status_at_all():
    """No pending status, because nothing can be trusted to finalize one.

    It has now failed twice, each time leaving the merge box saying "staging
    deploy running" about a deploy that had finished:

      1. #21676 -- the finalizer was a job inside the dispatched run, and
         `workflow_dispatch` executes the file from the ref it is dispatched
         at, so a branch cut before that job merged never had it.
      2. #21696 -- the finalizer moved to a `workflow_run` listener, fixing
         (1). But GitHub emits no `workflow_run` cascade for a run dispatched
         with GITHUB_TOKEN, which is what the auto lane uses. All 16 of that
         listener's runs were master pushes; none of the six dispatched
         PR-branch deploys after it landed produced one.

    The status is a *report* of the deploy, not the deploy. The run record is
    the deploy, and `_staging_evidence` reads it as witness (2), so no write
    here is load-bearing. An absent status says "no evidence recorded", which
    is true; a stuck pending one says something false, indefinitely.
    """
    script = (REPO_ROOT / "scripts" / "review-v3" / "staging-deploy.sh").read_text()
    assert "-f state=pending" not in script, \
        "a pending status needs a writer that cannot miss -- a schedule sweep, not a cascade"
    assert "-f state=\"$STATE\"" not in script, \
        "the terminal status belongs to staging-status.yml"
    # The evidence the Sentinel actually reads is the run record, and the
    # lane must keep producing one.
    assert "gh workflow run testing-build-and-deploy.yml" in script


def test_g4_reads_the_deploy_run_when_no_status_was_written():
    """Witness (2) is what makes dropping the pending status safe: with no
    `staging/pulumi-test-io` status on the head at all, a successful deploy
    run at that SHA is still evidence."""
    class _Gh:
        def get_commit_statuses(self, sha):
            return []
        def get_workflow_runs(self, wf, sha):
            return [{"id": 1, "html_url": "https://example.invalid/1", "conclusion": "success"}]

    got = sentinel._staging_evidence(_Gh(), "a" * 40)
    assert got and "succeeded" in got and "run 1" in got


def run_standalone() -> int:
    """The --self-test harness. The test list is bound at call time, not at
    module level: a module-level binding only sees the tests defined above
    it, and silently drops any added below (the SLA sweep's harness ran 12
    of 19 that way). Fixture-taking tests are pytest-only and are skipped
    by name here; `pytest scripts/review-v3/` collects everything."""
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
        except Exception as exc:  # noqa: BLE001 — a crash is a failure, not a harness abort
            failures += 1
            print(f"  FAIL: {t.__name__}: {type(exc).__name__}: {exc}", file=sys.stderr)
    if failures:
        print(f"{failures} sentinel test(s) failed", file=sys.stderr)
        return 1
    print("all sentinel self-tests passed")
    return 0


if __name__ == "__main__":
    sys.exit(run_standalone())


def test_a_split_legacy_review_is_counted_whole_by_g2():
    """The merge gate had the same page-1-only read as the collector, and it
    is the worse place for it: a 2-page v2 review with its 🚨 section on page
    2 counted zero outstanding findings and G2 passed as "legacy review
    clean" (pulumi/docs#21490)."""
    page1 = {"id": 9, "user": {"login": "github-actions[bot]"},
             "body": (f"<!-- CLAUDE_REVIEW 1/2 -->\n## Pre-merge Review\n"
                      f"<!-- CLAUDE_REVIEW_HEAD {HEAD} -->\n### 📜 Review history\n")}
    page2 = {"id": 10, "user": {"login": "github-actions[bot]"},
             "body": ("<!-- CLAUDE_REVIEW 2/2 -->\n### 🚨 Outstanding in this PR\n\n"
                      "- **[L10-12]** `f.md` — broken thing\n")}
    gh = StubGh(pr=pr_meta(), files=[docs_file_substantive()], comments=[page2, page1],
                reviews=[approval("guild-member")],
                memberships={("docs-guild", "guild-member"): "active"})
    v = sentinel.evaluate(gh, CONFIG)
    assert _gate(v, "review").status == "ok" and "legacy" in _gate(v, "review").message
    assert _gate(v, "findings").status == "red" and "1 🚨 Outstanding" in _gate(v, "findings").message
    assert v.conclusion == "failure"


def test_a_legacy_review_missing_a_page_errors_g2_rather_than_passing_it():
    """Page 1 of 2 and nothing else. Counting zero 🚨 here would pass the
    merge gate on a review nobody has read whole."""
    page1 = {"id": 9, "user": {"login": "github-actions[bot]"},
             "body": (f"<!-- CLAUDE_REVIEW 1/2 -->\n## Pre-merge Review\n"
                      f"<!-- CLAUDE_REVIEW_HEAD {HEAD} -->\n### 📜 Review history\n")}
    gh = StubGh(pr=pr_meta(), files=[docs_file_substantive()], comments=[page1],
                reviews=[approval("guild-member")],
                memberships={("docs-guild", "guild-member"): "active"})
    v = sentinel.evaluate(gh, CONFIG)
    assert _gate(v, "findings").status == "error"
    assert "page(s) 2 could not be read" in _gate(v, "findings").message
    assert v.conclusion != "success"


def test_a_legacy_page_the_v2_update_lane_posted_as_pulumi_bot_is_read():
    """#21210/#21487/#21149: the v2 update lane runs claude-code-action on
    PULUMI_BOT_TOKEN, so the page it re-posts is pulumi-bot's. G2 read only
    github-actions[bot] pages and reported page 2 unreadable."""
    page1 = {"id": 9, "user": {"login": "github-actions[bot]"},
             "body": (f"<!-- CLAUDE_REVIEW 1/2 -->\n## Pre-merge Review\n"
                      f"<!-- CLAUDE_REVIEW_HEAD {HEAD} -->\n### 📜 Review history\n")}
    page2 = {"id": 10, "user": {"login": "pulumi-bot"},
             "body": ("<!-- CLAUDE_REVIEW 2/2 -->\n### 🚨 Outstanding in this PR\n\n"
                      "- **[L10-12]** `f.md` — broken thing\n")}
    gh = StubGh(pr=pr_meta(), files=[docs_file_substantive()], comments=[page1, page2],
                reviews=[approval("guild-member")],
                memberships={("docs-guild", "guild-member"): "active"})
    v = sentinel.evaluate(gh, CONFIG)
    assert _gate(v, "findings").status == "red" and "1 🚨 Outstanding" in _gate(v, "findings").message
    # The v3 role cards stay github-actions[bot]-only.
    card = {"id": 11, "user": {"login": "pulumi-bot"},
            "body": sentinel.AUTHOR_MARKER + "\n"}
    assert sentinel._find_comment([card], sentinel.AUTHOR_MARKER) is None


def test_a_transient_5xx_on_a_read_is_retried(monkeypatch):
    """Run 35938827723: one HTTP 500 on `pulls/N` failed the evaluation."""
    calls = []

    class R:
        def __init__(self, rc, err="", out="{}"):
            self.returncode, self.stderr, self.stdout = rc, err, out

    results = [R(1, "gh: HTTP 500"), R(1, "gh: HTTP 502"), R(0)]

    def fake_run(argv, **_kw):
        calls.append(argv)
        return results.pop(0)

    monkeypatch.setattr(sentinel.subprocess, "run", fake_run)
    monkeypatch.setattr(sentinel, "RETRY_SLEEP_S", 0)
    gh = sentinel.Gh("pulumi/docs", 1)
    gh._run(["api", "repos/pulumi/docs/pulls/1"])
    assert len(calls) == 3

    calls.clear()
    results[:] = [R(1, "gh: HTTP 500"), R(0)]
    try:
        gh._run(["api", "-X", "PATCH", "repos/pulumi/docs/issues/comments/1"])
    except sentinel.SentinelDataError:
        pass
    assert len(calls) == 1, "writes never retry"

    calls.clear()
    results[:] = [R(1, "gh: HTTP 404"), R(0)]
    try:
        gh._run(["api", "repos/pulumi/docs/pulls/1"])
    except sentinel.SentinelDataError:
        pass
    assert len(calls) == 1, "a 4xx is an answer, not a flake"


def test_g2_does_not_call_a_stale_card_answered():
    """#21840: G1 red "no current review" beside G2 green "every finding
    answered" about a card at an older head. An answered stale card defers to
    G1; undecided findings on it stay red — they are real until answered."""
    old = "b" * 40
    gh = StubGh(pr=pr_meta(), files=[docs_file_substantive()],
                comments=[author_card(head=old), brief_comment()])
    v = sentinel.evaluate(gh, CONFIG)
    assert _gate(v, "review").status == "red" and "/update-review" in _gate(v, "review").message
    assert "push to refresh" not in _gate(v, "review").message
    assert _gate(v, "findings").status == "skip" and "not current" in _gate(v, "findings").message

    gh = StubGh(pr=pr_meta(), files=[docs_file_substantive()],
                comments=[author_card([("F1", "must")], head=old), brief_comment()])
    v = sentinel.evaluate(gh, CONFIG)
    assert _gate(v, "findings").status == "red" and "F1" in _gate(v, "findings").message


def test_oversized_is_the_label_not_the_size():
    """Adversarial review of #21948: deciding "oversized" by size flipped PRs
    reviewed before the size check existed -- G1/G2 skipped (so open 🚨
    findings stopped blocking) and G5 newly red on approved PRs. The label is
    the source of truth; triage re-dispatches the Sentinel when it moves it
    (#21936's race)."""
    meta = pr_meta()
    meta.update(additions=31000, deletions=382, changed_files=1156)
    gh = StubGh(pr=meta, files=[docs_file_substantive()],
                comments=[author_card([("F1", "must")]), brief_comment()])
    v = sentinel.evaluate(gh, CONFIG)
    assert _gate(v, "findings").status == "red" and "F1" in _gate(v, "findings").message
    assert _gate(v, "oversized").status == "skip"
    labelled = pr_meta(labels=["review:oversized"])
    labelled.update(additions=31000, deletions=382, changed_files=1156)
    v = sentinel.evaluate(StubGh(pr=labelled, files=[docs_file_substantive()]), CONFIG)
    assert _gate(v, "review").status == "skip" and "oversized" in _gate(v, "review").message
    assert _gate(v, "oversized").status == "red"


def test_old_status_comments_are_removed_and_quotes_are_left_alone():
    """The pinned status comment is retired: every evaluation deletes the
    bot's copies, and only the bot's."""
    bot = {"id": 5, "body": sentinel.STATUS_MARKER + "\n## Sentinel", "user": {"login": sentinel.BOT_LOGIN}}
    dup = dict(bot, id=6)
    quote = {"id": 7, "body": sentinel.STATUS_MARKER + " quoted", "user": {"login": "someone"}}
    gh = StubGh(pr=pr_meta(), files=[docs_file_substantive()], comments=[bot, dup, quote])
    assert sentinel.remove_status_comments(gh, comments=[bot, dup, quote]) == 2
    assert sorted(gh.deleted) == [5, 6]

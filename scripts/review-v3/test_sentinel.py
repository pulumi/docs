#!/usr/bin/env python3
"""Truth-table tests for sentinel.py — every gate ok/red/error individually,
the conclusion mapping (the fails-open trap: errors are action_required,
never neutral), the waive semantics (G4 has no waiver), the external and
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
    "link_only": {"approval": "any-team"},
}
CONFIG, _errors, _warnings = routing.validate_raw(RAW_CONFIG)
assert CONFIG is not None, _errors

# The live config's approver policy (`.github/review-routing.yml`): any
# routing team clears G3, and so does a repo admin. CONFIG keeps the strict
# `lane` default so the rest of the battery still tests the narrow rule.
LOOSE_CONFIG, _loose_errors, _ = routing.validate_raw(
    {**RAW_CONFIG, "approval": {"scope": "any-team", "admins_satisfy": True}})
assert LOOSE_CONFIG is not None, _loose_errors


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
    ):
        self.pr = pr or {}
        self.files = files or []
        self.comments = comments or []
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
        self.patched = []  # (comment_id, body)
        self.posted = []   # body

    def get_pr(self):
        return self.pr

    def list_files(self):
        return self.files

    def list_issue_comments(self):
        return self.comments

    def list_reviews(self):
        return self.reviews

    def get_commit_statuses(self, sha):
        return self.statuses

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
        return self.workflow_runs

    def patch_issue_comment(self, comment_id, body):
        self.patched.append((comment_id, body))

    def post_issue_comment(self, body):
        self.posted.append(body)


# ---- Fixture builders ----------------------------------------------------


BASE_REPO = "pulumi/docs"


def pr_meta(labels=(), draft=False, author="someone", head_repo=BASE_REPO):
    """`head_repo` is the fork test: same as base = internal; another name
    or None (deleted fork) = external. Pass `head_repo=...` omitted from
    the dict via `_no_head_repo()` to model a payload without the fact."""
    return {
        "head": {"sha": HEAD, "repo": None if head_repo is None else {"full_name": head_repo}},
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


def approval(user, utype="User", body="", commit_id=None):
    """An APPROVED review. `commit_id` defaults to the PR head, as GitHub
    always sends it — pass an older SHA to model a pre-push approval."""
    return {"state": "APPROVED", "user": {"login": user, "type": utype},
            "body": body, "commit_id": commit_id or HEAD}


def _state_with(fids, disposition="refuted", note="because"):
    st = review_state.empty_state()
    st["high_water"] = len(fids)
    for fid in fids:
        st = review_state.set_disposition(st, fid, disposition, actor="cam", note=note)
    return st


def _gate(verdict, prefix):
    return next(g for g in verdict.gates if g.name.startswith(prefix))


# ---- Tests ---------------------------------------------------------------


def test_mechanical_skips_the_review_but_not_the_approver():
    """`mechanical` is a model-review saving, not a human-review waiver.

    It used to conclude success with no approval at all, which the repo's
    own required-review rule contradicted — so the PR sat unmergeable under
    a green check, and somebody stamped it by hand.
    """
    gh = StubGh(pr=pr_meta(), files=[docs_file_mechanical()])
    v = sentinel.evaluate(gh, CONFIG)
    assert v.mechanical is True
    assert _gate(v, "G1").status == "ok"          # no model review needed
    assert _gate(v, "G3").status == "red"         # a human still approves
    assert "docs-guild" in _gate(v, "G3").message
    assert v.conclusion == "failure", v.to_json()
    assert "A human approver is still required" in v.summary


def test_mechanical_pr_succeeds_once_the_lane_team_approves():
    gh = StubGh(pr=pr_meta(), files=[docs_file_mechanical()],
                reviews=[approval("guild")],
                memberships={("docs-guild", "guild"): "active"})
    v = sentinel.evaluate(gh, CONFIG)
    assert v.conclusion == "success", v.to_json()


def test_substantive_no_review_g1_red():
    gh = StubGh(pr=pr_meta(), files=[docs_file_substantive()])
    v = sentinel.evaluate(gh, CONFIG)
    assert v.conclusion == "failure"
    assert _gate(v, "G1").status == "red"
    assert "#update-review" in _gate(v, "G1").message


def test_findings_undecided_g2_red_lists_ids():
    card = author_card([("F1", "must"), ("F2", "answer")])
    gh = StubGh(pr=pr_meta(), files=[docs_file_substantive()], comments=[card],
                reviews=[approval("guild-member")],
                memberships={("docs-guild", "guild-member"): "active"})
    v = sentinel.evaluate(gh, CONFIG)
    g2 = _gate(v, "G2")
    assert g2.status == "red" and "F1" in g2.message and "F2" in g2.message
    assert "@claude" in g2.message and "/resolve" not in g2.message
    assert v.conclusion == "failure"
    assert v.blocking_ids == ["F1", "F2"]


def test_dispositions_flip_g2_green():
    st = _state_with(["F1", "F2"])
    card = author_card([("F1", "must"), ("F2", "answer")], state=st)
    gh = StubGh(pr=pr_meta(), files=[docs_file_substantive()], comments=[card],
                reviews=[approval("guild-member")],
                memberships={("docs-guild", "guild-member"): "active"})
    v = sentinel.evaluate(gh, CONFIG)
    assert _gate(v, "G2").status == "ok"
    assert v.conclusion == "success", v.to_json()


def test_corrupt_review_state_action_required():
    card = author_card([("F1", "must")])
    card["body"] = card["body"].replace("<!-- REVIEW_STATE ", "<!-- REVIEW_STATE {broken ")
    gh = StubGh(pr=pr_meta(), files=[docs_file_substantive()], comments=[card])
    v = sentinel.evaluate(gh, CONFIG)
    assert _gate(v, "G2").status == "error"
    assert v.conclusion == "action_required"
    assert "maintainer" in _gate(v, "G2").message


def test_g3_wrong_team_red_names_team():
    card = author_card([], state=_state_with([]))
    gh = StubGh(pr=pr_meta(), files=[docs_file_substantive()], comments=[card],
                reviews=[approval("random-person")],
                memberships={})  # not a member of anything
    v = sentinel.evaluate(gh, CONFIG)
    g3 = _gate(v, "G3")
    assert g3.status == "red" and "pulumi/docs-guild" in g3.message


def link_only_file():
    """A blog file whose one changed line differs only in its link target."""
    return {
        "filename": "content/blog/p/index.md",
        "status": "modified",
        "patch": ("@@ -10,3 +10,3 @@\n context\n"
                  "-See [stacks](https://www.pulumi.com/docs/concepts/stacks/) for the rest.\n"
                  "+See [stacks](/docs/iac/concepts/stacks/) for the rest.\n context"),
    }


def test_g3_any_team_satisfies_a_link_only_sweep():
    # A blog link sweep would normally need pulumi/docs-blog-review. With
    # link_only.approval: any-team, a docs-guild member's approval clears it:
    # checking a retargeted link is careful work, not lane knowledge.
    card = author_card([], state=_state_with([]))
    gh = StubGh(pr=pr_meta(), files=[link_only_file()], comments=[card],
                reviews=[approval("guild-member")],
                memberships={("docs-guild", "guild-member"): "active"})
    v = sentinel.evaluate(gh, CONFIG)
    g3 = _gate(v, "G3")
    assert g3.status == "ok", g3.message
    # and a stranger still does not clear it: any TEAM, not anyone
    gh = StubGh(pr=pr_meta(), files=[link_only_file()], comments=[card],
                reviews=[approval("random-person")], memberships={})
    g3 = _gate(sentinel.evaluate(gh, CONFIG), "G3")
    assert g3.status == "red" and "any review team" in g3.message
    # a substantive change in the same lane is unaffected
    gh = StubGh(pr=pr_meta(), files=[{"filename": "content/blog/p/index.md", "status": "modified",
                                      "patch": "@@ -10,2 +10,3 @@\n context\n+A whole new sentence about stacks.\n context"}],
                comments=[card], reviews=[approval("guild-member")],
                memberships={("docs-guild", "guild-member"): "active"})
    g3 = _gate(sentinel.evaluate(gh, CONFIG), "G3")
    assert g3.status == "red" and "docs-marketing-review" in g3.message  # blog's team in this fixture


def test_link_only_diff_is_narrow():
    assert sentinel.link_only_diff([link_only_file()]) is True
    assert sentinel.link_only_diff([docs_file_substantive()]) is False
    assert sentinel.link_only_diff([{"filename": "a.md", "status": "modified", "patch": None}]) is False
    assert sentinel.link_only_diff([]) is False


def test_g3_any_team_scope_clears_another_lane_s_pr():
    """`approval.scope: any-team`: the matrix routes, it does not gatekeep.

    PR #21630's shape — docs pages plus the Hugo shortcode they use, so the
    matrix asks for docs-guild AND marketing. Under the lane rule that is a
    two-team quorum on a one-line template change; under any-team, one
    routing-team member's approval is the gate.
    """
    card = author_card([], state=_state_with([]))
    files = [docs_file_substantive(), frontend_file()]
    gh = StubGh(pr=pr_meta(), files=files, comments=[card],
                reviews=[approval("guild-member")],
                memberships={("docs-guild", "guild-member"): "active"})
    # lane: marketing is still owed
    g3 = _gate(sentinel.evaluate(gh, CONFIG), "G3")
    assert g3.status == "red" and "docs-marketing-review" in g3.message
    # any-team: the same approval clears it
    g3 = _gate(sentinel.evaluate(gh, LOOSE_CONFIG), "G3")
    assert g3.status == "ok", g3.message
    # the routed roles are unchanged — triage still requests both teams
    res = routing.resolve_lanes([f["filename"] for f in files], False, False, LOOSE_CONFIG)
    assert res.roles == {"docs-guild", "marketing"} and res.any_team is True


def test_g3_any_team_still_means_a_team():
    card = author_card([], state=_state_with([]))
    gh = StubGh(pr=pr_meta(), files=[docs_file_substantive()], comments=[card],
                reviews=[approval("random-person")], memberships={})
    g3 = _gate(sentinel.evaluate(gh, LOOSE_CONFIG), "G3")
    assert g3.status == "red"
    assert "any review team" in g3.message
    # the red names the teams that would do, and the admin escape
    assert "pulumi/docs-tools" in g3.message
    assert "administrator" in g3.message


def test_g3_repo_admin_satisfies_when_configured():
    card = author_card([], state=_state_with([]))
    gh = StubGh(pr=pr_meta(), files=[docs_file_substantive()], comments=[card],
                reviews=[approval("an-admin")], memberships={},
                permissions={"an-admin": "admin"})
    g3 = _gate(sentinel.evaluate(gh, LOOSE_CONFIG), "G3")
    assert g3.status == "ok" and "an-admin" in g3.message
    # write access is not admin
    gh2 = StubGh(pr=pr_meta(), files=[docs_file_substantive()], comments=[card],
                 reviews=[approval("a-committer")], memberships={},
                 permissions={"a-committer": "write"})
    assert _gate(sentinel.evaluate(gh2, LOOSE_CONFIG), "G3").status == "red"


def test_g3_admin_rule_is_opt_in_and_never_costs_a_call_when_off():
    card = author_card([], state=_state_with([]))
    gh = StubGh(pr=pr_meta(), files=[docs_file_substantive()], comments=[card],
                reviews=[approval("an-admin")], memberships={},
                permissions={"an-admin": "admin"})
    # CONFIG has no `approval:` section at all: the strict default.
    assert _gate(sentinel.evaluate(gh, CONFIG), "G3").status == "red"
    assert gh.permission_calls == []
    # and with the rule on, a team member's approval short-circuits it too
    gh2 = StubGh(pr=pr_meta(), files=[docs_file_substantive()], comments=[card],
                 reviews=[approval("guild-member")],
                 memberships={("docs-guild", "guild-member"): "active"},
                 permissions={"guild-member": "admin"})
    assert _gate(sentinel.evaluate(gh2, LOOSE_CONFIG), "G3").status == "ok"
    assert gh2.permission_calls == []


def test_g3_bot_admin_approval_still_never_counts():
    """The admin rule widens who counts, not what counts as a human."""
    card = author_card([], state=_state_with([]))
    gh = StubGh(pr=pr_meta(), files=[docs_file_substantive()], comments=[card],
                reviews=[approval("pulumi-bot"), approval("actions-bot", utype="Bot")],
                memberships={},
                permissions={"pulumi-bot": "admin", "actions-bot": "admin"})
    assert _gate(sentinel.evaluate(gh, LOOSE_CONFIG), "G3").status == "red"
    assert gh.permission_calls == []  # denylisted/Bot reviews never reach the lookup


def test_g3_permission_api_failure_action_required_not_red():
    card = author_card([], state=_state_with([]))
    gh = StubGh(pr=pr_meta(), files=[docs_file_substantive()], comments=[card],
                reviews=[approval("maybe-an-admin")], memberships={},
                permission_error_users={"maybe-an-admin"})
    v = sentinel.evaluate(gh, LOOSE_CONFIG)
    assert _gate(v, "G3").status == "error"
    assert v.conclusion == "action_required"


def test_g3_bot_denylist_and_bot_type_excluded():
    card = author_card([], state=_state_with([]))
    gh = StubGh(pr=pr_meta(), files=[docs_file_substantive()], comments=[card],
                reviews=[approval("pulumi-bot"), approval("actions-bot", utype="Bot")],
                memberships={("docs-guild", "pulumi-bot"): "active",
                             ("docs-guild", "actions-bot"): "active"})
    v = sentinel.evaluate(gh, CONFIG)
    assert _gate(v, "G3").status == "red"


def test_g3_membership_api_failure_action_required_not_red():
    card = author_card([], state=_state_with([]))
    gh = StubGh(pr=pr_meta(), files=[docs_file_substantive()], comments=[card],
                reviews=[approval("guild-member")],
                membership_error_users={"guild-member"})
    v = sentinel.evaluate(gh, CONFIG)
    assert _gate(v, "G3").status == "error"
    assert v.conclusion == "action_required"


def test_commented_review_does_not_void_approval():
    card = author_card([], state=_state_with([]))
    reviews = [
        approval("guild-member"),
        {"state": "COMMENTED", "user": {"login": "guild-member", "type": "User"}, "body": "nit"},
    ]
    gh = StubGh(pr=pr_meta(), files=[docs_file_substantive()], comments=[card],
                reviews=reviews, memberships={("docs-guild", "guild-member"): "active"})
    v = sentinel.evaluate(gh, CONFIG)
    assert _gate(v, "G3").status == "ok"


def test_external_contributor_is_a_fork_head_repo():
    # A fork PR — even from a write-access user — is external: G1/G2 skip,
    # the matrix approver's review is the review.
    gh = StubGh(pr=pr_meta(author="staff-on-a-fork", head_repo="staff-on-a-fork/docs"),
                files=[docs_file_substantive()], reviews=[approval("guild-member")],
                memberships={("docs-guild", "guild-member"): "active"})
    v = sentinel.evaluate(gh, CONFIG)
    assert _gate(v, "G1").status == "skip"
    assert _gate(v, "G2").status == "skip"
    assert _gate(v, "G3").status == "ok"
    assert v.conclusion == "success"
    assert "external contribution" in v.summary.lower()
    # A deleted fork (GitHub nulls head.repo) is external too.
    v = sentinel.evaluate(StubGh(pr=pr_meta(head_repo=None), files=[docs_file_substantive()]), CONFIG)
    assert _gate(v, "G1").status == "skip"


def test_same_repo_bot_author_is_never_external():
    # workprentice[bot] answers `none` on the collaborator-permission API but
    # pushes same-repo branches that get the full review (2026-09-14: every
    # workprentice PR had G1/G2 skipped). Permission is not the test.
    card = author_card([("F1", "must")], state=_state_with([]))
    gh = StubGh(pr=pr_meta(author="workprentice[bot]"), files=[docs_file_substantive()],
                comments=[card])
    v = sentinel.evaluate(gh, CONFIG)
    assert _gate(v, "G1").status == "ok"
    assert _gate(v, "G2").status == "red" and v.blocking_ids == ["F1"]
    assert "external" not in v.summary.lower()


def test_missing_head_repo_fact_is_internal():
    # Fail closed: no head.repo key at all ⇒ the stricter (internal) gates.
    gh = StubGh(pr=_no_head_repo(pr_meta(author="drive-by")), files=[docs_file_substantive()])
    v = sentinel.evaluate(gh, CONFIG)
    assert _gate(v, "G1").status == "red"
    assert _gate(v, "G2").status == "skip"  # "no review present — see G1", not the external skip
    assert "external" not in v.summary.lower()


def test_trivial_prose_flagged_stands_on_triage_prose_comment():
    # The review lane skipped this PR as trivial; the prose flag demotes it
    # from mechanical; triage's prose comment is the review. G3 still wants
    # the human approver the demotion asked for.
    labels = ["review:trivial", "review:prose-flagged"]
    gh = StubGh(pr=pr_meta(labels=labels), files=[docs_file_mechanical()],
                comments=[triage_prose_comment()])
    v = sentinel.evaluate(gh, CONFIG)
    assert v.mechanical is False
    assert _gate(v, "G1").status == "ok" and "prose check stands in" in _gate(v, "G1").message
    assert _gate(v, "G2").status == "ok" and "no findings to answer" in _gate(v, "G2").message
    assert _gate(v, "G3").status == "red"
    assert v.conclusion == "failure"
    assert "stands in for the review" in v.summary
    # With the approver in place the PR is mergeable.
    v = sentinel.evaluate(StubGh(pr=pr_meta(labels=labels), files=[docs_file_mechanical()],
                                 comments=[triage_prose_comment()], reviews=[approval("guild-member")],
                                 memberships={("docs-guild", "guild-member"): "active"}), CONFIG)
    assert v.conclusion == "success"


def test_trivial_prose_flagged_without_triage_comment_names_the_fix():
    labels = ["review:trivial", "review:prose-flagged"]
    gh = StubGh(pr=pr_meta(labels=labels), files=[docs_file_mechanical()])
    v = sentinel.evaluate(gh, CONFIG)
    g1 = _gate(v, "G1")
    assert g1.status == "red"
    assert "#new-review" in g1.message and "review:trivial" in g1.message
    assert _gate(v, "G2").status == "skip"
    # A comment from someone other than the triage bot is not the stand-in.
    gh = StubGh(pr=pr_meta(labels=labels), files=[docs_file_mechanical()],
                comments=[triage_prose_comment(login="someone")])
    assert _gate(sentinel.evaluate(gh, CONFIG), "G1").status == "red"


def test_trivial_without_prose_flag_is_still_mechanical():
    gh = StubGh(pr=pr_meta(labels=["review:trivial"]), files=[docs_file_mechanical()])
    v = sentinel.evaluate(gh, CONFIG)
    assert v.mechanical is True
    assert _gate(v, "G1").message.startswith("mechanical change")
    # Mechanical clears G1 only; the lane team is still owed an approval.
    assert _gate(v, "G3").status == "red"


def test_current_author_card_beats_trivial_standin():
    # A card current at head is the review even when the label says trivial.
    card = author_card([("F1", "must")], state=_state_with([]))
    gh = StubGh(pr=pr_meta(labels=["review:trivial", "review:prose-flagged"]),
                files=[docs_file_mechanical()], comments=[card, triage_prose_comment()])
    v = sentinel.evaluate(gh, CONFIG)
    assert _gate(v, "G1").message.startswith("review current")
    assert _gate(v, "G2").status == "red"


def test_stale_author_card_is_not_rescued_by_trivial_standin():
    # A PR that was reviewed once stays on the review track: a stale card
    # with an open finding plus a later trivial label and a prose comment
    # must not pass G1/G2 on the stand-in (PR #21607 review, F1).
    card = author_card([("F1", "must")], state=_state_with([]), head="0" * 40)
    gh = StubGh(pr=pr_meta(labels=["review:trivial", "review:prose-flagged"]),
                files=[docs_file_mechanical()], comments=[card, triage_prose_comment()])
    v = sentinel.evaluate(gh, CONFIG)
    assert _gate(v, "G1").status == "red"
    assert "stands in" not in _gate(v, "G1").message
    assert _gate(v, "G2").status == "red"
    assert v.conclusion == "failure"


def test_infra_needs_staging_status_g4():
    card = author_card([], state=_state_with([]))
    base = dict(pr=pr_meta(), files=[infra_file()], comments=[card],
                reviews=[approval("tools-member")],
                memberships={("docs-tools", "tools-member"): "active"})
    v_red = sentinel.evaluate(StubGh(**base), CONFIG)
    assert _gate(v_red, "G4").status == "red"
    assert "/deploy-staging" in _gate(v_red, "G4").message
    assert v_red.conclusion == "failure"

    v_ok = sentinel.evaluate(
        StubGh(**base, statuses=[{"context": "staging/pulumi-test-io", "state": "success",
                   "creator": {"login": "github-actions[bot]"}}]),
        CONFIG)
    assert _gate(v_ok, "G4").status == "ok"
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
    assert v.conclusion == "failure", v.to_json()
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


def test_waive_never_covers_infra_evidence():
    gh = StubGh(pr=pr_meta(labels=["review:waived"]), files=[infra_file()],
                label_events=_waive_events("cam"),
                memberships={("docs-tools", "cam"): "active"})
    v = sentinel.evaluate(gh, CONFIG)
    assert v.conclusion == "failure"
    assert "no waiver" in v.title.lower() or "NOT waivable" in v.summary


# ---- G4: the deploy run is evidence, not just the status ----------------


def _deploy_run(conclusion="success", run_id=99):
    return {"id": run_id, "conclusion": conclusion,
            "html_url": f"https://github.com/pulumi/docs/actions/runs/{run_id}"}


def test_g4_accepts_a_successful_deploy_run_when_the_status_is_missing():
    gh = StubGh(pr=pr_meta(), files=[infra_file()],
                reviews=[approval("tools-member")],
                memberships={("docs-tools", "tools-member"): "active"},
                workflow_runs=[_deploy_run()])
    g4 = _gate(sentinel.evaluate(gh, CONFIG), "G4")
    assert g4.status == "ok", g4
    assert "run 99" in g4.message


def test_g4_ignores_a_failed_deploy_run():
    gh = StubGh(pr=pr_meta(), files=[infra_file()],
                workflow_runs=[_deploy_run(conclusion="failure")])
    assert _gate(sentinel.evaluate(gh, CONFIG), "G4").status == "red"


def test_g4_takes_a_success_among_several_runs_at_this_head():
    """'Deployed at least once' — an earlier red run doesn't erase a green one."""
    gh = StubGh(pr=pr_meta(), files=[infra_file()],
                workflow_runs=[_deploy_run(conclusion="failure", run_id=1),
                               _deploy_run(conclusion="success", run_id=2)])
    assert _gate(sentinel.evaluate(gh, CONFIG), "G4").status == "ok"


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
    assert _gate(v, "G4").status == "skip"
    # Still tools' to approve — this narrows the evidence, not the approver.
    assert _gate(v, "G3").status == "ok"
    assert v.conclusion == "success", v.to_json()


def test_g4_arms_for_the_whole_pr_when_one_path_qualifies():
    """Per path, not per PR: a deploy-touching file anywhere in the diff
    arms the gate even alongside exempt ones."""
    gh = StubGh(pr=pr_meta(), files=[infra_data_file(), infra_file()])
    assert _gate(sentinel.evaluate(gh, CONFIG), "G4").status == "red"


def test_an_unattributed_staging_status_is_not_evidence():
    """A commit status needs only push access:

        gh api repos/OWNER/REPO/statuses/SHA -f state=success \
          -f context=staging/pulumi-test-io

    …which made the gate review-routing.yml calls "no waiver, no shortcut" a
    one-line bypass. The run record cannot be forged that way.
    """
    base = dict(pr=pr_meta(), files=[infra_file()],
                comments=[author_card([], state=_state_with([]))])
    forged = sentinel.evaluate(StubGh(**dict(base, statuses=[
        {"context": "staging/pulumi-test-io", "state": "success",
         "creator": {"login": "someone"}}])), CONFIG)
    assert _gate(forged, "G4").status == "red"

    unattributed = sentinel.evaluate(StubGh(**dict(base, statuses=[
        {"context": "staging/pulumi-test-io", "state": "success"}])), CONFIG)
    assert _gate(unattributed, "G4").status == "red"

    # The real writer still works, and the run-record witness is unaffected.
    real = sentinel.evaluate(StubGh(**dict(base, statuses=[
        {"context": "staging/pulumi-test-io", "state": "success",
         "creator": {"login": "github-actions[bot]"}}])), CONFIG)
    assert _gate(real, "G4").status == "ok"


def test_a_waive_clears_an_error_but_never_g4():
    """`any_error` used to be tested before `waived`, so the break-glass was
    inert in exactly the outage it exists for: an expired team-read token
    errors G3 on every PR, so every PR sat at action_required and no waive
    could move any of them — under a summary still claiming WAIVED."""
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
    assert "WAIVED" in errored.title

    # G4 is still not waivable.
    infra = sentinel.evaluate(StubGh(**dict(base, files=[infra_file()])), CONFIG)
    assert infra.conclusion == "failure"
    assert "infra evidence has no waiver" in infra.title


def test_g4_run_lookup_failure_blocks_rather_than_erroring():
    """An unreadable run history is 'no evidence', not action_required.

    Red is already the conservative answer here; escalating to
    action_required would misreport an API hiccup as a corrupt PR.
    """
    gh = StubGh(pr=pr_meta(), files=[infra_file()], workflow_runs_error=True)
    assert _gate(sentinel.evaluate(gh, CONFIG), "G4").status == "red"


# ---- Pinned status comment ----------------------------------------------


def test_status_comment_upserts_then_stays_byte_identical():
    gh = StubGh(pr=pr_meta(), files=[docs_file_substantive()])
    v = sentinel.evaluate(gh, CONFIG)

    assert sentinel.update_status_comment(gh, v, comments=[]) is True
    body = gh.posted[0]
    assert sentinel.STATUS_MARKER in body
    assert "G3 right-approver" in body
    assert "docs-guild" in body, "a red gate carries its own remediation"

    existing = [{"id": 7, "body": body, "user": {"login": sentinel.BOT_LOGIN}}]
    assert sentinel.update_status_comment(gh, v, comments=existing) is False, \
        "an unchanged verdict must not churn the comment"
    assert gh.patched == []


def test_status_comment_rewrites_when_a_gate_changes():
    gh = StubGh(pr=pr_meta(), files=[docs_file_substantive()])
    stale = [{"id": 7, "body": sentinel.STATUS_MARKER + "\nsomething older\n",
              "user": {"login": sentinel.BOT_LOGIN}}]
    assert sentinel.update_status_comment(gh, sentinel.evaluate(gh, CONFIG),
                                          comments=stale) is True
    assert gh.patched and gh.patched[0][0] == 7


def test_an_approval_does_not_survive_a_push():
    """An approval is of a COMMIT. Without this, the sequence is: get a
    clean one-line change approved, push the payload, let the review lane
    post a fresh card, and every gate is green on an approval nobody
    re-gave. The code used to defer this to "the ruleset's dismissal job" —
    but AGENTS.md records branch protection is not in place, and nothing in
    `.github/` configures dismissal, so nobody was doing it."""
    card = author_card([], state=_state_with([]))
    base = dict(pr=pr_meta(), files=[docs_file_substantive()], comments=[card],
                memberships={("docs-guild", "guild"): "active"})

    at_head = sentinel.evaluate(
        StubGh(**dict(base, reviews=[approval("guild")])), CONFIG)
    assert _gate(at_head, "G3").status == "ok"

    pre_push = sentinel.evaluate(
        StubGh(**dict(base, reviews=[approval("guild", commit_id="0" * 40)])), CONFIG)
    assert _gate(pre_push, "G3").status == "red"
    # And it must say WHY — "nobody approved" is a lie to someone looking at
    # a green checkmark on the PR.
    assert "guild" in _gate(pre_push, "G3").message
    assert "earlier commit" in _gate(pre_push, "G3").message

    # A malformed review with no commit_id at all does not clear the gate.
    no_sha = sentinel.evaluate(
        StubGh(**dict(base, reviews=[{"state": "APPROVED",
                                      "user": {"login": "guild", "type": "User"},
                                      "body": ""}])), CONFIG)
    assert _gate(no_sha, "G3").status == "red"


def test_one_flaky_membership_lookup_does_not_poison_a_satisfied_gate():
    """`errors` used to be tested before `satisfied_any`, so a transient 5xx
    on one approver reported action_required with a qualifying approval
    sitting right there."""
    card = author_card([], state=_state_with([]))
    gh = StubGh(pr=pr_meta(), files=[docs_file_substantive()], comments=[card],
                reviews=[approval("flaky"), approval("guild")],
                memberships={("docs-guild", "guild"): "active"},
                membership_error_users={"flaky"})
    v = sentinel.evaluate(gh, CONFIG)
    assert _gate(v, "G3").status == "ok", _gate(v, "G3").message


def test_the_oversized_ack_must_come_from_a_qualifying_approver():
    """`review:oversized` skips G1 and G2 and nothing verifies the PR is
    actually oversized, so G5 is the only thing left. It read the ack from
    the unfiltered approver list — anyone with read access can post an
    APPROVED review, so a bystander could supply the magic string while a
    real team member clicked plain Approve."""
    base = dict(pr=pr_meta(labels=["review:oversized"]),
                files=[docs_file_substantive()],
                memberships={("docs-guild", "guild"): "active"})

    bystander = sentinel.evaluate(StubGh(**dict(base, reviews=[
        approval("guild"),
        approval("randomer", body=f"lgtm {sentinel.OVERSIZED_ACK}"),
    ])), CONFIG)
    assert _gate(bystander, "G5").status == "red"

    proper = sentinel.evaluate(StubGh(**dict(base, reviews=[
        approval("guild", body=f"read it all {sentinel.OVERSIZED_ACK}"),
    ])), CONFIG)
    assert _gate(proper, "G5").status == "ok"


def test_a_zero_file_pr_does_not_manufacture_an_approver():
    """G3 reported `ok` for a PR with no changed paths — the one gate that
    guarantees a human, passing with no human. Combined with a forged card
    that was a green Sentinel with nobody involved."""
    v = sentinel.evaluate(
        StubGh(pr=pr_meta(), files=[], comments=[], reviews=[]), CONFIG)
    assert _gate(v, "G3").status == "skip"
    assert v.conclusion != "success"


def test_role_comments_must_come_from_the_bot():
    """G1 and G2 were fully author-controllable until this check existed.

    `_find_comment` matched the marker anywhere in any comment by anyone and
    returned the first hit. Comments come back oldest-first, so a PR author
    who commented before the review lane posted owned both gates for the
    life of the PR — and `update_strip` then wrote the ⛔ banner into the
    forgery, so the real card never showed it.

    The rule is the one the writer already enforces: bot-authored, marker as
    an exact line in the first three (`pinned-comment.sh list_role_comments`,
    `resolve-handler.py:222`).
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
    assert _gate(v, "G2").status == "red"
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


def test_the_status_comment_cannot_be_hijacked():
    """The Sentinel's token can edit anyone's comment, so an unqualified
    marker lookup let a contributor's comment absorb the pinned status."""
    gh = StubGh(pr=pr_meta(), files=[docs_file_substantive()])
    squatter = [{"id": 99, "user": {"login": "someone", "type": "User"},
                 "body": sentinel.STATUS_MARKER + "\nmine now\n"}]
    assert sentinel.update_status_comment(gh, sentinel.evaluate(gh, CONFIG),
                                          comments=squatter) is True
    assert gh.patched == [], "must not PATCH a comment it does not own"
    assert gh.posted, "posts its own instead"


def test_status_comment_rows_are_single_line():
    """A newline inside a cell silently breaks the markdown table."""
    gh = StubGh(pr=pr_meta(), files=[infra_file()])
    body = sentinel.render_status_comment(sentinel.evaluate(gh, CONFIG))
    rows = [l for l in body.splitlines() if l.startswith("| ") and "**G" in l]
    assert len(rows) == 5, rows
    assert all(r.count("|") == 4 for r in rows), rows


def test_status_comment_says_why_a_satisfied_gate_is_satisfied():
    """A green gate must carry its reason, not just "Nothing to do."

    PR #21698 showed a green G3 right-approver with no approving review from
    anybody on the PR. The gate had passed under the `auto_approve`
    clean-brief rule, which is correct, but the cell said "Nothing to do."
    and nothing else — indistinguishable from a broken gate. Whatever the
    verdict, the table has to be readable as an explanation.
    """
    card = author_card([], state=_state_with([]))
    gh = StubGh(pr=pr_meta(), files=[docs_file_mechanical()], comments=[card],
                reviews=[approval("guild")],
                memberships={("docs-guild", "guild"): "active"})
    body = sentinel.render_status_comment(sentinel.evaluate(gh, CONFIG))
    rows = {}
    for line in body.splitlines():
        if line.startswith("| ") and "**G" in line:
            cells = [c.strip() for c in line.strip("|").split("|")]
            rows[cells[1].strip("*")] = cells[2]

    # Every quiet row opens with its blurb and then explains itself.
    for name, cell in rows.items():
        assert cell != "Nothing to do.", name
        if cell.startswith("Nothing to do"):
            assert cell.startswith("Nothing to do: "), (name, cell)
            assert len(cell) > len("Nothing to do: ") + 1, (name, cell)
        elif cell.startswith("Doesn't apply"):
            assert cell.startswith("Doesn't apply to this PR: "), (name, cell)

    g3 = next(v for k, v in rows.items() if k.startswith("G3"))
    assert "matrix-required approval present" in g3, g3
    g4 = next(v for k, v in rows.items() if k.startswith("G4"))
    assert "no changed path affects the deploy" in g4, g4


def test_status_comment_marks_report_only_and_flags_the_unwaivable_gate():
    gh = StubGh(pr=pr_meta(), files=[infra_file()])
    body = sentinel.render_status_comment(sentinel.evaluate(gh, CONFIG, report_only=True))
    assert "Report-only" in body
    assert "no waiver" in body


def test_preview_label_is_carried_on_the_verdict():
    gh = StubGh(pr=pr_meta(labels=[sentinel.PREVIEW_LABEL]),
                files=[docs_file_substantive()])
    assert sentinel.evaluate(gh, CONFIG, report_only=True).preview is True
    gh2 = StubGh(pr=pr_meta(), files=[docs_file_substantive()])
    assert sentinel.evaluate(gh2, CONFIG, report_only=True).preview is False


def test_oversized_ack_replaces_g1_g2():
    gh = StubGh(pr=pr_meta(labels=["review:oversized"]), files=[docs_file_substantive()],
                reviews=[approval("guild-member", body="LGTM sentinel:oversized-ack")],
                memberships={("docs-guild", "guild-member"): "active"})
    v = sentinel.evaluate(gh, CONFIG)
    assert _gate(v, "G1").status == "skip"
    assert _gate(v, "G5").status == "ok"
    assert v.conclusion == "success", v.to_json()

    gh2 = StubGh(pr=pr_meta(labels=["review:oversized"]), files=[docs_file_substantive()],
                 reviews=[approval("guild-member")],
                 memberships={("docs-guild", "guild-member"): "active"})
    v2 = sentinel.evaluate(gh2, CONFIG)
    assert _gate(v2, "G5").status == "red"
    assert "sentinel:oversized-ack" in _gate(v2, "G5").message


def test_legacy_v2_comment_passes_g1_with_note_and_g2_counts():
    clean = {"id": 9, "user": {"login": "github-actions[bot]"},
             "body": (f"<!-- CLAUDE_REVIEW 1/1 -->\n## Pre-merge Review\n"
                      f"<!-- CLAUDE_REVIEW_HEAD {HEAD} -->\n"
                      "### 🚨 Outstanding in this PR\n\n_none_\n\n### 📜 Review history\n")}
    gh = StubGh(pr=pr_meta(), files=[docs_file_substantive()], comments=[clean],
                reviews=[approval("guild-member")],
                memberships={("docs-guild", "guild-member"): "active"})
    v = sentinel.evaluate(gh, CONFIG)
    assert _gate(v, "G1").status == "ok" and "legacy" in _gate(v, "G1").message
    assert _gate(v, "G2").status == "ok"
    assert v.conclusion == "success", v.to_json()

    dirty = dict(clean)
    dirty["body"] = clean["body"].replace(
        "_none_", "- **[L10-12]** `f.md` — broken thing")
    gh2 = StubGh(pr=pr_meta(), files=[docs_file_substantive()], comments=[dirty],
                 reviews=[approval("guild-member")],
                 memberships={("docs-guild", "guild-member"): "active"})
    v2 = sentinel.evaluate(gh2, CONFIG)
    assert _gate(v2, "G2").status == "red"
    assert v2.conclusion == "failure"


def test_report_only_wraps_neutral():
    gh = StubGh(pr=pr_meta(), files=[docs_file_substantive()])
    v = sentinel.evaluate(gh, CONFIG, report_only=True)
    assert v.conclusion == "neutral"
    assert v.would_be == "failure"
    assert v.summary.startswith("**REPORT-ONLY — would be: `failure`**")


def test_draft_neutral():
    gh = StubGh(pr=pr_meta(draft=True))
    v = sentinel.evaluate(gh, CONFIG)
    assert v.conclusion == "neutral"


def test_summary_embeds_brief_and_break_glass():
    gh = StubGh(pr=pr_meta(), files=[docs_file_substantive()], comments=[brief_comment()])
    v = sentinel.evaluate(gh, CONFIG)
    assert "Summary text." in v.summary
    assert "reviewer footer" not in v.summary
    assert "review:waived" in v.summary  # break-glass note on red rows


def test_update_strip_insert_replace_clear():
    card = author_card([("F1", "must")])
    gh = StubGh(pr=pr_meta(), files=[docs_file_substantive()], comments=[card])
    v = sentinel.evaluate(gh, CONFIG)
    assert sentinel.update_strip(gh, v, comments=[card]) is True
    _, patched = gh.patched[-1]
    assert "⛔" in patched and sentinel.STRIP_OPEN in patched

    card2 = dict(card, body=patched)
    assert sentinel.update_strip(gh, v, comments=[card2]) is False  # idempotent

    ok = sentinel.Verdict(conclusion="success", title="", summary="", head_sha=HEAD)
    assert sentinel.update_strip(gh, ok, comments=[card2]) is True  # clears
    _, cleared = gh.patched[-1]
    assert "⛔" not in cleared and sentinel.STRIP_OPEN in cleared

    fresh_no_strip = author_card([], state=_state_with([]))
    assert sentinel.update_strip(gh, ok, comments=[fresh_no_strip]) is False


def test_frontend_routes_to_marketing_without_staging():
    card = author_card([], state=_state_with([]))
    base = dict(pr=pr_meta(), files=[frontend_file()], comments=[card])
    v_red = sentinel.evaluate(StubGh(**base), CONFIG)
    assert _gate(v_red, "G3").status == "red"
    assert "docs-marketing-review" in _gate(v_red, "G3").message
    assert _gate(v_red, "G4").status == "skip"
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
    # no review at head G1 goes red.
    v2 = sentinel.evaluate(StubGh(pr=pr_meta(author="pulumi-bot"), files=[docs_file_substantive()]), CONFIG)
    assert v2.governed is True and _gate(v2, "G1").status == "red"
    # A human wearing the label is still governed.
    v3 = sentinel.evaluate(StubGh(pr=pr_meta(author="someone", labels=["automation/merge"]),
                                  files=[docs_file_substantive()]), CONFIG)
    assert v3.governed is True


def test_not_governed_report_only_wraps_neutral():
    v = sentinel.evaluate(StubGh(pr=pr_meta(author="dependabot[bot]")), CONFIG, report_only=True)
    assert v.conclusion == "neutral" and v.would_be == "success"
    assert v.title.startswith("Report-only")


def test_a_spotless_bot_pr_still_needs_the_lane_team():
    """The deleted `auto_approve` rule's exact scenario.

    Bot author, zero blocking findings, a brief with an empty ⚠️ table —
    the cleanest possible bot PR. G3 used to go green on it and report "no
    human gate". It doesn't any more: nothing consumed the `auto_approved`
    flag, and the repo's required-review rule never read this config, so
    the only thing that "no human gate" ever did was contradict the merge
    box and train a reflex stamp.
    """
    base = dict(pr=pr_meta(author="pulumi-bot"), files=[docs_file_substantive()],
                comments=[v3_author_card(0), v3_brief(0)])
    v = sentinel.evaluate(StubGh(**base), CONFIG)
    assert _gate(v, "G1").status == "ok"      # the review ran and is current
    assert _gate(v, "G2").status == "ok"      # nothing to answer
    assert _gate(v, "G3").status == "red"     # and a human still approves
    assert "docs-guild" in _gate(v, "G3").message
    assert v.conclusion == "failure", v.to_json()

    # No verdict field survives for a consumer to read.
    assert "auto_approved" not in v.to_json()
    assert not hasattr(v, "auto_approved")
    assert "uto-approved" not in v.summary

    # The same PR with the team's approval is done.
    approved = sentinel.evaluate(
        StubGh(**dict(base, reviews=[approval("guild")],
                      memberships={("docs-guild", "guild"): "active"})), CONFIG)
    assert approved.conclusion == "success", approved.to_json()


def test_a_bot_approval_never_satisfies_the_lane_team():
    """No automated approval can clear G3, by either of two mechanisms.

    `approval()` defaults to `type: "User"` here deliberately: it isolates
    the `bots:` denylist from the automatic `type == Bot` exclusion. That is
    the case the denylist exists for — `pulumi-bot` really is `type: User`
    on GitHub, and an App identity whose marker we read wrong would slip
    through on the type check alone.
    """
    base = dict(pr=pr_meta(author="pulumi-bot"), files=[docs_file_substantive()],
                comments=[v3_author_card(0), v3_brief(0)])
    for bot in ("pulumi-bot", "workprentice[bot]", "github-copilot[bot]",
                "eon-pulumi-agent[bot]", "dependabot[bot]"):
        # Denylisted, even presented as a plain user and an active member.
        v = sentinel.evaluate(
            StubGh(**dict(base, reviews=[approval(bot)],
                          memberships={("docs-guild", bot): "active"})), CONFIG)
        assert _gate(v, "G3").status == "red", bot
        # And again via the type marker, for an account not on the list.
        v2 = sentinel.evaluate(
            StubGh(**dict(base, reviews=[approval("some-app[bot]", utype="Bot")],
                          memberships={("docs-guild", "some-app[bot]"): "active"})), CONFIG)
        assert _gate(v2, "G3").status == "red"

    # `github-actions[bot]` is the identity auto-approve-for-auto-merge.yml
    # posts as. It cannot clear G3 either — the regen lane works because
    # those PRs are `not_governed`, not because that approval counts.
    v3 = sentinel.evaluate(
        StubGh(**dict(base, reviews=[approval("github-actions[bot]", utype="Bot")],
                      memberships={("docs-guild", "github-actions[bot]"): "active"})), CONFIG)
    assert _gate(v3, "G3").status == "red"


def test_workprentice_is_governed_and_routed_like_anyone_else():
    """The second-busiest bot author on the repo (a quarter of its bot PRs)
    was absent from the routing config entirely. It is not a
    `not_governed` lane — nothing auto-approves or auto-merges it — so it
    gets the full gate set."""
    gh = StubGh(pr=pr_meta(author="workprentice[bot]"), files=[docs_file_substantive()],
                comments=[v3_author_card(0), v3_brief(0)])
    v = sentinel.evaluate(gh, CONFIG)
    assert v.governed is True
    assert _gate(v, "G3").status == "red"
    assert "docs-guild" in _gate(v, "G3").message


def test_prose_flagged_still_demotes_mechanical():
    # A mechanical diff wearing the flag is substantive: review required.
    v2 = sentinel.evaluate(StubGh(pr=pr_meta(labels=["review:prose-flagged"]),
                                  files=[docs_file_mechanical()]), CONFIG)
    assert v2.mechanical is False
    assert _gate(v2, "G1").status == "red"
    assert _gate(v2, "G3").status == "red"
    # Without the flag the same diff is mechanical (G1 only).
    v3 = sentinel.evaluate(StubGh(pr=pr_meta(), files=[docs_file_mechanical()]), CONFIG)
    assert v3.mechanical is True and v3.to_json()["mechanical"] is True
    assert _gate(v3, "G1").status == "ok"


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
                  "review:prose-flagged", "sentinel:preview"):
        assert f"github.event.label.name == '{label}'" in wf, label


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
        sentinel.PREVIEW_LABEL,
        sentinel.PROSE_FLAGGED_LABEL,
        sentinel.TRIVIAL_LABEL,
        sentinel.OVERSIZED_LABEL,
        cfg.waive.get("label", "review:waived"),
    }
    # …plus every label the config can make load-bearing.
    for pair in (cfg.not_governed or {}).get("author_label_pairs") or []:
        read_by_evaluator.add(pair["label"])

    missing = [l for l in sorted(read_by_evaluator)
               if f"github.event.label.name == '{l}'" not in wf]
    assert not missing, (
        "labels the evaluator reads that the workflow's label-event filter "
        f"drops (they only take effect on the next unrelated event): {missing}"
    )
    assert "publish_guard.py" in wf
    assert "external_id: $run_id" in wf
    assert "steps.guard.outputs.publish == 'true'" in wf


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

    staging-deploy-auto.yml and staging-deploy-pr.yml both did this with
    `github.event.pull_request.head.ref`. The PR lane holds `id-token: write`
    with ESC already authenticated, so the payload could mint an OIDC token
    and read the org-scoped PULUMI_BOT_TOKEN — repo-write escalating to
    org-scoped credentials.

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
    for name in ("review-sentinel.yml", "staging-deploy-pr.yml"):
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
    assert "--dispatch-only" in auto, "the auto lane must not wait on the deploy"
    import yaml as _yaml  # noqa: PLC0415
    jobs = _yaml.safe_load(auto)["jobs"]
    assert all("concurrency" not in j for j in jobs.values()), "a queued job is a job that gets cancelled"

    script = (REPO_ROOT / "scripts" / "review-v3" / "staging-deploy.sh").read_text()
    assert "--dispatch-only) DISPATCH_ONLY" in script
    # stale comment guard: the header must not still promise a queue
    assert "Concurrency sits on the DEPLOY JOB" not in auto
    # The attended lane still watches -- not to write the status (that is
    # staging-status.yml's job now) but because the watch is what holds its
    # `staging-stack` group for the length of the deploy. Match the script
    # invocation, not the prose: the header explains the contrast.
    pr_lane = (REPO_ROOT / ".github" / "workflows" / "staging-deploy-pr.yml").read_text()
    invocation = "\n".join(
        step["run"] for step in _yaml.safe_load(pr_lane)["jobs"]["deploy"]["steps"]
        if "staging-deploy.sh" in step.get("run", "")
    )
    assert invocation, "the attended lane must still call staging-deploy.sh"
    assert "--dispatch-only" not in invocation
    assert "--announce" in invocation

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
    assert "gh run watch" in script, "the attended lane still holds the stack"
    # The evidence the Sentinel actually reads is the run record, and both
    # lanes must keep producing one.
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
    assert _gate(v, "G1").status == "ok" and "legacy" in _gate(v, "G1").message
    assert _gate(v, "G2").status == "red" and "1 🚨 Outstanding" in _gate(v, "G2").message
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
    assert _gate(v, "G2").status == "error"
    assert "page(s) 2 could not be read" in _gate(v, "G2").message
    assert v.conclusion != "success"

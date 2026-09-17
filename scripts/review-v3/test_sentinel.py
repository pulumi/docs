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
    "bots": ["pulumi-bot"],
    "matrix": {
        "docs": {"mechanical": "none", "substantive": "docs-guild"},
        "blog": {"mechanical": "none", "substantive": "marketing"},
        "website": {"mechanical": "none", "substantive": "marketing"},
        "programs": {"mechanical": "none", "substantive": "docs-guild"},
        "infra": {"mechanical": "tools", "substantive": "tools", "staging_evidence": "required"},
        "frontend": {"mechanical": "none", "substantive": "marketing"},
        "other": {"mechanical": "none", "substantive": "tools"},
    },
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
    "auto_approve": {"authors": ["pulumi-bot"]},
    "link_only": {"approval": "any-team"},
}
CONFIG, _errors, _warnings = routing.validate_raw(RAW_CONFIG)
assert CONFIG is not None, _errors


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


def approval(user, utype="User", body=""):
    return {"state": "APPROVED", "user": {"login": user, "type": utype}, "body": body}


def _state_with(fids, disposition="refuted", note="because"):
    st = review_state.empty_state()
    st["high_water"] = len(fids)
    for fid in fids:
        st = review_state.set_disposition(st, fid, disposition, actor="cam", note=note)
    return st


def _gate(verdict, prefix):
    return next(g for g in verdict.gates if g.name.startswith(prefix))


# ---- Tests ---------------------------------------------------------------


def test_mechanical_pr_success_no_approvals():
    gh = StubGh(pr=pr_meta(), files=[docs_file_mechanical()])
    v = sentinel.evaluate(gh, CONFIG)
    assert v.conclusion == "success", v.to_json()
    assert _gate(v, "G1").status == "ok"
    assert "no human approval required" in _gate(v, "G3").message


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
    assert v.conclusion == "success"


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
        StubGh(**base, statuses=[{"context": "staging/pulumi-test-io", "state": "success"}]),
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

    existing = [{"id": 7, "body": body}]
    assert sentinel.update_status_comment(gh, v, comments=existing) is False, \
        "an unchanged verdict must not churn the comment"
    assert gh.patched == []


def test_status_comment_rewrites_when_a_gate_changes():
    gh = StubGh(pr=pr_meta(), files=[docs_file_substantive()])
    stale = [{"id": 7, "body": sentinel.STATUS_MARKER + "\nsomething older\n"}]
    assert sentinel.update_status_comment(gh, sentinel.evaluate(gh, CONFIG),
                                          comments=stale) is True
    assert gh.patched and gh.patched[0][0] == 7


def test_status_comment_rows_are_single_line():
    """A newline inside a cell silently breaks the markdown table."""
    gh = StubGh(pr=pr_meta(), files=[infra_file()])
    body = sentinel.render_status_comment(sentinel.evaluate(gh, CONFIG))
    rows = [l for l in body.splitlines() if l.startswith("| ") and "**G" in l]
    assert len(rows) == 5, rows
    assert all(r.count("|") == 4 for r in rows), rows


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


def test_clean_brief_auto_approves_bot_author():
    base = dict(pr=pr_meta(author="pulumi-bot"), files=[docs_file_substantive()],
                comments=[v3_author_card(0), v3_brief(0)])
    v = sentinel.evaluate(StubGh(**base), CONFIG)
    assert _gate(v, "G3").status == "ok"
    assert "No human gate" in _gate(v, "G3").message
    assert v.conclusion == "success", v.to_json()
    assert v.auto_approved is True and v.to_json()["auto_approved"] is True
    assert "Auto-approved" in v.summary
    # The stances-variant empty sentinel is still an empty table.
    v_st = sentinel.evaluate(StubGh(**dict(base, comments=[v3_author_card(0), v3_brief(0, stances=True)])), CONFIG)
    assert _gate(v_st, "G3").status == "ok" and v_st.auto_approved is True


def test_clean_brief_rule_needs_an_empty_checks_table():
    base = dict(pr=pr_meta(author="pulumi-bot"), files=[docs_file_substantive()],
                comments=[v3_author_card(0), v3_brief(1)])
    v = sentinel.evaluate(StubGh(**base), CONFIG)
    assert _gate(v, "G3").status == "red" and v.auto_approved is False
    assert "docs-guild" in _gate(v, "G3").message


def test_clean_brief_rule_needs_nothing_blocking_and_a_listed_author():
    # A blocking finding on the card: no auto-approval even with a clean brief.
    v = sentinel.evaluate(StubGh(pr=pr_meta(author="pulumi-bot"), files=[docs_file_substantive()],
                                 comments=[v3_author_card(1), v3_brief(0)]), CONFIG)
    assert _gate(v, "G3").status == "red" and v.auto_approved is False
    # A human author with the same clean cards still needs the matrix team.
    v2 = sentinel.evaluate(StubGh(pr=pr_meta(author="someone"), files=[docs_file_substantive()],
                                  comments=[v3_author_card(0), v3_brief(0)]), CONFIG)
    assert _gate(v2, "G3").status == "red" and v2.auto_approved is False
    # No brief at all: never clean.
    v3 = sentinel.evaluate(StubGh(pr=pr_meta(author="pulumi-bot"), files=[docs_file_substantive()],
                                  comments=[v3_author_card(0)]), CONFIG)
    assert _gate(v3, "G3").status == "red" and v3.auto_approved is False


def test_prose_flagged_disqualifies_clean_brief_and_demotes_mechanical():
    # Clean cards, but triage flagged prose: a human must look.
    v = sentinel.evaluate(StubGh(pr=pr_meta(author="pulumi-bot", labels=["review:prose-flagged"]),
                                 files=[docs_file_substantive()],
                                 comments=[v3_author_card(0), v3_brief(0)]), CONFIG)
    assert _gate(v, "G3").status == "red" and v.auto_approved is False
    # A mechanical diff wearing the flag is substantive: review required.
    v2 = sentinel.evaluate(StubGh(pr=pr_meta(labels=["review:prose-flagged"]),
                                  files=[docs_file_mechanical()]), CONFIG)
    assert v2.mechanical is False
    assert _gate(v2, "G1").status == "red"
    assert _gate(v2, "G3").status == "red"
    # Without the flag the same diff is mechanical.
    v3 = sentinel.evaluate(StubGh(pr=pr_meta(), files=[docs_file_mechanical()]), CONFIG)
    assert v3.mechanical is True and v3.to_json()["mechanical"] is True


def test_workflow_has_no_concurrency_group_and_narrows_label_events():
    # A cancelled job renders as a failing check; the workflow must not own
    # a concurrency group (publish_guard.py handles overlap instead), and
    # label events must be limited to the labels the evaluator reads.
    wf = (REPO_ROOT / ".github" / "workflows" / "review-sentinel.yml").read_text()
    assert "cancel-in-progress:" not in wf
    assert "\nconcurrency:" not in wf
    for label in ("review:waived", "review:oversized", "review:trivial", "review:prose-flagged"):
        assert f"github.event.label.name == '{label}'" in wf, label
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


def test_only_one_thing_writes_the_terminal_staging_status():
    """Two writers of one context is the noise the in-run job was deleted for.

    `staging-deploy.sh` still writes the PENDING status -- that has to happen
    at dispatch time -- but its watch path (held by `/deploy-staging` to keep
    the `staging-stack` concurrency group for the length of the deploy) must
    not race the listener with a terminal one.
    """
    script = (REPO_ROOT / "scripts" / "review-v3" / "staging-deploy.sh").read_text()
    assert script.count("-f state=pending") == 1
    assert "-f state=\"$STATE\"" not in script, \
        "the terminal status belongs to staging-status.yml"
    assert "gh run watch" in script, "the attended lane still holds the stack"


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

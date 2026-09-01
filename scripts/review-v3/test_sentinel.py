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
        "other": {"mechanical": "none", "substantive": "docs-guild"},
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
        permission="write",
        permission_error=False,
        memberships=None,
        membership_error_users=(),
        label_events=None,
    ):
        self.pr = pr or {}
        self.files = files or []
        self.comments = comments or []
        self.reviews = reviews or []
        self.statuses = statuses or []
        self.permission = permission
        self.permission_error = permission_error
        self.memberships = memberships or {}  # (slug, user) -> state
        self.membership_error_users = set(membership_error_users)
        self.label_events = label_events or []
        self.patched = []  # (comment_id, body)

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

    def get_permission(self, actor):
        if self.permission_error:
            raise sentinel.SentinelDataError("boom")
        return self.permission

    def get_team_membership(self, org, team_slug, user):
        if user in self.membership_error_users:
            raise sentinel.SentinelDataError(f"lookup failed for {user}")
        return self.memberships.get((team_slug, user), "none")

    def get_label_events(self):
        return self.label_events

    def patch_issue_comment(self, comment_id, body):
        self.patched.append((comment_id, body))


# ---- Fixture builders ----------------------------------------------------


def pr_meta(labels=(), draft=False, author="someone"):
    return {
        "head": {"sha": HEAD},
        "draft": draft,
        "user": {"login": author},
        "labels": [{"name": n} for n in labels],
    }


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
    return {
        "filename": "layouts/partials/foo.html",
        "status": "modified",
        "patch": "@@ -1,1 +1,1 @@\n-<b>a</b>\n+<b>b</b>",
    }


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
        "### 🚨 Must fix or refute",
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


def test_external_contributor_g1_g2_skipped_g3_governs():
    gh = StubGh(pr=pr_meta(author="drive-by"), files=[docs_file_substantive()],
                permission="read", reviews=[approval("guild-member")],
                memberships={("docs-guild", "guild-member"): "active"})
    v = sentinel.evaluate(gh, CONFIG)
    assert _gate(v, "G1").status == "skip"
    assert _gate(v, "G2").status == "skip"
    assert _gate(v, "G3").status == "ok"
    assert v.conclusion == "success"
    assert "external contribution" in v.summary.lower()


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


def test_waived_success_with_banner_and_actor():
    gh = StubGh(pr=pr_meta(labels=["review:waived"]), files=[docs_file_substantive()],
                label_events=[{"event": "labeled", "label": {"name": "review:waived"},
                               "actor": {"login": "cam"}}])
    v = sentinel.evaluate(gh, CONFIG)
    assert v.conclusion == "success"
    assert "WAIVED by @cam" in v.summary


def test_waive_never_covers_infra_evidence():
    gh = StubGh(pr=pr_meta(labels=["review:waived"]), files=[infra_file()],
                label_events=[{"event": "labeled", "label": {"name": "review:waived"},
                               "actor": {"login": "cam"}}])
    v = sentinel.evaluate(gh, CONFIG)
    assert v.conclusion == "failure"
    assert "no waiver" in v.title.lower() or "NOT waivable" in v.summary


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


def test_workflow_never_checks_out_pr_code():
    wf = (REPO_ROOT / ".github" / "workflows" / "review-sentinel.yml").read_text()
    assert "pull_request_target" in wf
    for forbidden in ("github.event.pull_request.head.ref",
                      "github.event.pull_request.head.sha",
                      "refs/pull/", "merge_commit_sha"):
        assert forbidden not in wf, f"workflow must never reference PR code: {forbidden}"
    assert "default_branch" in wf  # checkout pinned to base default branch


# ---- Standalone harness --------------------------------------------------

ALL_TESTS = [v for k, v in sorted(globals().items()) if k.startswith("test_")]


def run_standalone() -> int:
    failures = 0
    for t in ALL_TESTS:
        try:
            t()
            print(f"  ok: {t.__name__}")
        except AssertionError as exc:
            failures += 1
            print(f"  FAIL: {t.__name__}: {exc}", file=sys.stderr)
    if failures:
        print(f"{failures} sentinel test(s) failed", file=sys.stderr)
        return 1
    print("all sentinel self-tests passed")
    return 0


if __name__ == "__main__":
    sys.exit(run_standalone())

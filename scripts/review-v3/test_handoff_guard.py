#!/usr/bin/env python3
"""handoff_guard.py truth table plus the claude-code-review.yml invariants
the superseded-publish path depends on (the test_sentinel.py pattern: read
the workflow text, assert the guards that must not silently regress).

Background: PR #21642, 2026-09-16. A review ran on head A, the author pushed
during it, the publish job's freshness guard correctly refused to publish —
and exited 0 leaving review:in-progress on the PR with no run behind it and
nothing scheduled to replace it. These tests pin both halves of the fix.
"""

from __future__ import annotations

import importlib.util
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent.parent
WF_PATH = REPO_ROOT / ".github" / "workflows" / "claude-code-review.yml"
RECONCILE_PATH = REPO_ROOT / ".github" / "workflows" / "review-label-reconcile.yml"


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


guard = _load("handoff_guard_under_test", HERE / "handoff_guard.py")

A, B = "a" * 40, "b" * 40


# ---- decide() -------------------------------------------------------------

def test_current_handoff_publishes():
    assert guard.decide(A, A, 0) == ("publish", "handoff is current")


def test_sha_compare_is_case_insensitive():
    assert guard.decide(A, A.upper(), 0)[0] == "publish"


def test_unreadable_live_head_fails_toward_publishing():
    # A refusal with no evidence of staleness would drop a review on the floor.
    assert guard.decide(A, None, 0)[0] == "publish"
    assert guard.decide(A, "", guard.MAX_DEPTH)[0] == "publish"


def test_moved_head_redispatches_below_the_cap():
    for depth in range(guard.MAX_DEPTH):
        action, reason = guard.decide(A, B, depth)
        assert action == "redispatch", depth
        assert f"depth {depth + 1}" in reason


def test_moved_head_rests_at_the_cap():
    action, reason = guard.decide(A, B, guard.MAX_DEPTH)
    assert action == "rest"
    assert "review:stale" in reason
    assert guard.decide(A, B, guard.MAX_DEPTH + 5)[0] == "rest"


def test_cap_is_two_chained_retries():
    # Worst case per ready-transition is 1 + MAX_DEPTH full reviews. Bumping
    # this is a cost decision, not a code change — make it deliberately.
    assert guard.MAX_DEPTH == 2


def test_self_test_passes():
    assert guard._self_test() == 0


# ---- settle_wait() --------------------------------------------------------

NOW = datetime(2026, 9, 16, 22, 30, tzinfo=timezone.utc)


def test_settle_unknown_push_time_never_blocks():
    assert guard.settle_wait(NOW, None) == 0


def test_settle_waits_the_remainder_of_the_quiet_window():
    just_now = NOW
    assert guard.settle_wait(NOW, just_now) == guard.SETTLE_S
    one_min_ago = guard._parse_iso("2026-09-16T22:29:00Z")
    assert guard.settle_wait(NOW, one_min_ago) == guard.SETTLE_S - 60


def test_settle_quiet_head_dispatches_immediately():
    assert guard.settle_wait(NOW, guard._parse_iso("2026-09-16T22:00:00Z")) == 0


# ---- workflow invariants --------------------------------------------------

def _wf():
    return yaml.safe_load(WF_PATH.read_text())


def _job(name):
    return _wf()["jobs"][name]


def _step(job, name):
    for s in job["steps"]:
        if s.get("name") == name:
            return s
    raise AssertionError(f"no step named {name!r}")


def test_publish_guard_resets_the_label_and_uses_the_script():
    run = _step(_job("publish"), "Verify handoff is still current")["run"]
    assert "handoff_guard.py decide" in run
    assert "--label review:stale" in run, "a superseded publish must not leave review:in-progress"
    assert "dispatcher_comment_id" in run, "a superseded #new-review must clean up its confirmation comment"
    # The rest path rewrites the spinner rather than deleting it.
    assert "gh api --method PATCH" in run and "#new-review" in run


def test_publish_guard_is_not_weakened():
    # Every publishing step still gates on the guard's verdict; only the
    # guard itself and the error trap may run without it.
    job = _job("publish")
    ungated = [
        s.get("name") or s.get("uses")
        for s in job["steps"]
        if "superseded == 'false'" not in str(s.get("if", ""))
    ]
    assert set(ungated) == {
        "Checkout repository (default branch)",
        "Download v3 handoff artifact",
        "Verify handoff is still current",
        "Publish error trap",
    }, ungated
    assert _step(job, "Publish error trap")["if"].strip() == \
        "failure() && steps.current.outputs.superseded != 'true'"


def test_handoff_sha_is_the_checked_out_sha():
    run = _step(_job("claude-review"), "Resolve PR context")["run"]
    assert 'HEAD_SHA="${{ github.event.workflow_run.head_sha || github.event.inputs.head_sha }}"' in run
    checkout = _step(_job("claude-review"), "Checkout repository")
    assert checkout["with"]["ref"] == "${{ github.event.workflow_run.head_sha || github.event.inputs.head_sha }}"


def test_redispatch_job_shape():
    wf = _wf()
    job = wf["jobs"]["redispatch"]
    assert job["needs"] == "publish"
    assert job["if"].strip() == "needs.publish.outputs.action == 'redispatch'"
    assert "concurrency" not in job, "must sit outside claude-review-<pr>: the dispatched run would cancel it"
    assert job["permissions"]["actions"] == "write"
    assert job["permissions"]["contents"] == "read"
    checkout = job["steps"][0]
    assert checkout["with"]["ref"] == "${{ github.event.repository.default_branch }}"
    for forbidden in ("head.ref", "head.sha", "refs/pull/", "needs.claude-review.outputs.head_sha"):
        assert forbidden not in str(job), forbidden
    run = job["steps"][-1]["run"]
    assert "handoff_guard.py settle" in run
    assert "gh workflow run claude-code-review.yml" in run
    for flag in ("-f pr_number=", "-f head_sha=", "-f supersede_depth=", "-f force=", "-f mention_author="):
        assert flag in run, flag
    assert "dispatcher_comment_id" not in run.split("gh workflow run")[1]
    assert 'IS_DRAFT" = "true"' in run and '"$STATE" != "OPEN"' in run


def test_depth_is_carried_through_dispatch_inputs():
    wf = _wf()
    inp = wf[True]["workflow_dispatch"]["inputs"]["supersede_depth"]
    assert inp["default"] == "0" and inp["required"] is False
    publish = _job("publish")
    assert publish["outputs"]["next_depth"] == "${{ steps.current.outputs.next_depth }}"
    assert publish["outputs"]["action"] == "${{ steps.current.outputs.action }}"
    guard_env = _step(publish, "Verify handoff is still current")["env"]
    assert guard_env["DEPTH"] == "${{ github.event.inputs.supersede_depth || '0' }}"


def test_claude_review_concurrency_group_is_unchanged():
    job = _job("claude-review")
    assert job["concurrency"]["cancel-in-progress"] is True
    assert job["concurrency"]["group"].startswith("claude-review-${{ github.event.workflow_run.pull_requests[0].number")
    assert _job("publish")["concurrency"]["group"] == "claude-review-${{ needs.claude-review.outputs.pr_number }}"
    assert "cancel-in-progress" not in _job("publish")["concurrency"]


def test_new_review_dispatcher_still_matches_the_inputs():
    # claude-new.yml passes an explicit input set; a required input added
    # here would 422 that dispatch. Every input it passes must exist and
    # every input it does not pass must have a default.
    inputs = _wf()[True]["workflow_dispatch"]["inputs"]
    new = (REPO_ROOT / ".github" / "workflows" / "claude-new.yml").read_text()
    passed = {tok.split("=")[0] for tok in new.split("-f ")[1:] if "=" in tok.split()[0]}
    for name, spec in inputs.items():
        assert name in passed or "default" in spec, name


def test_reconcile_sweeps_orphaned_in_progress():
    wf = RECONCILE_PATH.read_text()
    assert "--label review:in-progress" in wf
    assert 'label.name == "review:in-progress"' in wf
    assert "CLAUDE_PROGRESS" in wf
    assert '--add-label "review:stale" --remove-label "review:in-progress"' in wf
    assert "-lt 1800" in wf  # 30-minute minimum age

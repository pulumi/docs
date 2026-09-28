"""Structural sanity for every workflow file GitHub will try to parse.

GitHub rejects a workflow whose job reuses a step `id`, and it does so at
trigger time, not at merge time: the file merges fine, then every run of
that workflow fails to start and every `gh workflow run` of it returns
HTTP 422. #21557 shipped a second `id: mention` into claude-update.yml and
took the update lane down until the rename landed. `yaml.safe_load` alone
would not have caught it -- duplicate ids are valid YAML.
"""

from __future__ import annotations

import collections
import pathlib

import pytest
import yaml

REPO_ROOT = pathlib.Path(__file__).resolve().parents[4]
_WF_DIR = REPO_ROOT / ".github" / "workflows"
WORKFLOWS = sorted([*_WF_DIR.glob("*.yml"), *_WF_DIR.glob("*.yaml")])


@pytest.mark.parametrize("wf", WORKFLOWS, ids=lambda p: p.name)
def test_workflow_parses_and_step_ids_are_unique_per_job(wf):
    data = yaml.safe_load(wf.read_text())
    assert isinstance(data, dict) and "jobs" in data, f"{wf.name}: no jobs block"
    for job_name, job in (data["jobs"] or {}).items():
        ids = [s.get("id") for s in (job.get("steps") or []) if isinstance(s, dict) and s.get("id")]
        dupes = [k for k, n in collections.Counter(ids).items() if n > 1]
        assert not dupes, (
            f"{wf.name} job {job_name!r} reuses step id(s) {dupes}; GitHub refuses to run "
            "the workflow (\"identifier may not be used more than once within the same scope\")"
        )


def _upload_steps(wf):
    data = yaml.safe_load(wf.read_text())
    for job_name, job in (data.get("jobs") or {}).items():
        for step in job.get("steps") or []:
            if isinstance(step, dict) and str(step.get("uses", "")).startswith("actions/upload-artifact@"):
                yield job_name, step


def _hidden_paths(step) -> list[str]:
    """Upload paths with a dot-prefixed segment (`.foo.json`, `.snap/`)."""
    paths = str((step.get("with") or {}).get("path", "")).split()
    return [p for p in paths
            if any(seg.startswith(".") and seg not in (".", "..") for seg in p.lstrip("!").split("/"))]


@pytest.mark.parametrize("wf", WORKFLOWS, ids=lambda p: p.name)
def test_dotfile_uploads_include_hidden_files(wf):
    """upload-artifact skips hidden files unless told otherwise, and says
    nothing when it does: with `if-no-files-found: ignore` the step goes green
    over an empty bundle. Every pre-step artifact in the review pipeline is a
    dotfile, so an upload that forgets the flag preserves nothing."""
    for job_name, step in _upload_steps(wf):
        hidden = _hidden_paths(step)
        if hidden:
            assert (step.get("with") or {}).get("include-hidden-files") is True, (
                f"{wf.name} job {job_name!r} step {step.get('name')!r} uploads {hidden} "
                "without `include-hidden-files: true`; upload-artifact will silently skip them"
            )


def test_review_uploads_raw_claim_artifacts():
    """The pre-model claim records are the only place a verdict's routing
    inputs (`type`, `source_hint`, `found_by`) survive the run."""
    wf = _WF_DIR / "claude-code-review.yml"
    steps = [s for _, s in _upload_steps(wf) if s.get("name") == "Upload claim artifacts"]
    assert len(steps) == 1
    step = steps[0]
    assert set(_hidden_paths(step)) == {
        ".candidate-claims.json", ".verified-claims.json", ".fetched-urls.json"}
    assert step["with"]["include-hidden-files"] is True
    assert step["with"]["if-no-files-found"] == "ignore"
    # Must survive a failed or timed-out model step, and must never be the
    # reason a review fails.
    assert str(step.get("if", "")).startswith("always()")
    assert step.get("continue-on-error") is True


def test_update_lane_trigger_leaves_new_review_to_the_mention_gate():
    """A job-level `if:` is a substring match and can't see quoting. When the
    update lane's excluded `#new-review` there, a comment that only quoted
    that hashtag ran neither lane: claude-new.yml's gate declined it as a
    quote, and this one never reached its own gate (#21909). The exclusion
    belongs to mention-gate.py's `--exclude new-review`, which reads only
    live text."""
    wf = _WF_DIR / "claude-update.yml"
    gate = yaml.safe_load(wf.read_text())["jobs"]["gate"]
    assert "#new-review" not in gate["if"], "the trigger must not screen #new-review by substring"
    runs = "\n".join(s.get("run") or "" for s in gate.get("steps") or [])
    assert "--hashtag update-review --exclude new-review" in runs, "the mention gate must still apply the exclusion"


_BOT_ALLOWLIST_RE = __import__("re").compile(r'"\$AUTHOR" == "([^"]+)"')
_ACCESS_CHECKERS = ("claude-new.yml", "claude-update.yml", "claude-code-review.yml", "claude-triage.yml")


def test_trusted_bot_allowlist_is_identical_in_every_access_check():
    """The collaborator-permission API says `none` for a GitHub App, so each
    lane that gates on write access carries a list of trusted bots. The four
    copies said "keep in sync" and claude-new.yml had none at all: every
    workprentice `#new-review` was silently dropped (#21936)."""
    lists = {}
    for name in _ACCESS_CHECKERS:
        text = (_WF_DIR / name).read_text()
        blocks = __import__("re").findall(
            r'if \[\[ "\$AUTHOR" == "github-copilot\[bot\]".*?\]\]; then', text, __import__("re").S)
        assert len(blocks) == 1, f"{name}: expected one trusted-bot block, found {len(blocks)}"
        lists[name] = frozenset(_BOT_ALLOWLIST_RE.findall(blocks[0]))
    reference = lists["claude-update.yml"]
    assert "workprentice[bot]" in reference and "app/workprentice" in reference
    for name, bots in lists.items():
        assert bots == reference, f"{name} trusts {sorted(bots)}, claude-update.yml trusts {sorted(reference)}"


def _job_run_text(wf_name: str, job: str) -> str:
    data = yaml.safe_load((_WF_DIR / wf_name).read_text())
    return "\n".join(str(s.get("run", "")) for s in data["jobs"][job].get("steps") or [])


def test_redispatch_forwards_every_new_review_input():
    """Adversarial review of #21948: the redispatch forwarded force /
    mention_author / ack_target but not prior_high_water, so a #new-review
    superseded after `clear` re-ran with no card and restarted at F1."""
    data = yaml.safe_load((_WF_DIR / "claude-code-review.yml").read_text())
    trigger = data.get("on") or data.get(True)
    inputs = set((trigger["workflow_dispatch"].get("inputs") or {}))
    run = _job_run_text("claude-code-review.yml", "redispatch")
    # dispatcher_comment_id is deliberately dropped (the guard deleted it);
    # the rest are the re-run's own bookkeeping or its resolved head.
    carried = inputs - {"dispatcher_comment_id", "supersede_depth", "head_sha", "pr_number"}
    missing = sorted(i for i in carried if f"-f {i}=" not in run)
    assert not missing, f"redispatch drops {missing}"


def test_failure_notices_carry_the_prior_high_water():
    """An errored forced run's card is already gone; its notice keeps the
    mark, and both readers look for it."""
    text = (_WF_DIR / "claude-code-review.yml").read_text()
    assert text.count("<!-- REVIEW_HIGH_WATER $PRIOR_HW_IN -->") == 2
    assert text.count("PRIOR_HW_IN: ${{ github.event.inputs.prior_high_water }}") == 2
    assert "review_state.py high-water-marker" in text
    assert "review_state.py high-water-marker" in (_WF_DIR / "claude-new.yml").read_text()
    # Only failure notices: a card or triage prose can quote PR text, and a
    # quoted marker would inflate the next review's ids.
    for wf in ("claude-code-review.yml", "claude-new.yml"):
        reader = next(l for l in (_WF_DIR / wf).read_text().splitlines()
                      if "select(.user.login == \"github-actions[bot]\")" in l and ".body' 2>/dev/null" in l)
        assert 'startswith("<!-- CLAUDE_PROGRESS -->")' in reader, wf


def test_reconcile_re_evaluates_the_sentinel_after_it_repairs_a_card():
    """Adversarial review of #21948: the cron restamped cards and un-staled
    labels, but GITHUB_TOKEN writes fire no event, so G1 stayed red."""
    wf = _WF_DIR / "review-label-reconcile.yml"
    data = yaml.safe_load(wf.read_text())
    assert data["permissions"].get("actions") == "write"
    run = _job_run_text("review-label-reconcile.yml", "reconcile")
    assert "gh workflow run review-sentinel.yml" in run
    # After the loop-1 restamp and after the loop-3 label write.
    restamp_branch = run.split("review carried across", 1)[1].split("continue", 1)[0]
    assert 'sentinel "$pr"' in restamp_branch
    unstale = run.split("review:stale → $label", 1)[1].split("done", 1)[0]
    assert 'sentinel "$pr"' in unstale


def test_triage_re_evaluates_the_sentinel_when_it_moves_a_label_the_gate_reads():
    """The Sentinel decides oversized/trivial from the label alone, and a
    GITHUB_TOKEN label write fires no `labeled` event (#21936's G5 race)."""
    data = yaml.safe_load((_WF_DIR / "claude-triage.yml").read_text())
    job = next(iter(data["jobs"].values()))
    assert job["permissions"].get("actions") == "write"
    text = (_WF_DIR / "claude-triage.yml").read_text()
    apply_at = text.index('gh pr edit "$PR" --repo "$REPO" "${ARGS[@]}"')
    dispatch_at = text.index("gh workflow run review-sentinel.yml")
    assert dispatch_at > apply_at, "dispatch after the labels land"

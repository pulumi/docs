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

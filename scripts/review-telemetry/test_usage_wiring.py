"""The usage telemetry is only as good as its wiring: a Claude job that stops
uploading its rows, or a record job that stops running on failure, goes dark
without a single red check. These tests pin the contract README.md describes."""

from __future__ import annotations

import pathlib

import pytest
import yaml

REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
WF = REPO_ROOT / ".github" / "workflows"
RECORDER = "scripts/review-telemetry/record-usage.py"

# workflow file → the job that calls Claude and builds the rows
INSTRUMENTED = {
    "claude-code-review.yml": "claude-review",
    "claude-update.yml": "claude-update",
    "claude-triage.yml": "triage",
}
# workflow file → the run that records its rows to S3 (triage's rows ride the
# review run it triggers)
RECORDED_BY = {
    "claude-code-review.yml": "claude-code-review.yml",
    "claude-update.yml": "claude-update.yml",
    "claude-triage.yml": "claude-code-review.yml",
}


def _load(name: str) -> dict:
    return yaml.safe_load((WF / name).read_text())


def _steps(name: str, job: str) -> list[dict]:
    return [s for s in _load(name)["jobs"][job].get("steps") or [] if isinstance(s, dict)]


@pytest.mark.parametrize("wf,job", INSTRUMENTED.items())
def test_claude_job_builds_and_uploads_usage_rows_even_on_failure(wf, job):
    steps = _steps(wf, job)
    build = [s for s in steps if RECORDER in str(s.get("run", ""))]
    assert build, f"{wf} job {job!r} never runs {RECORDER}"
    upload = [s for s in steps
              if str(s.get("uses", "")).startswith("actions/upload-artifact@")
              and str((s.get("with") or {}).get("name", "")).startswith("docs-agent-usage-")]
    assert upload, f"{wf} job {job!r} uploads no docs-agent-usage-* artifact"
    for s in build + upload:
        assert "always()" in str(s.get("if", "")), (
            f"{wf} step {s.get('name')!r} must run with always(): failed and timed-out runs were billed too")
        assert s.get("continue-on-error") is True, (
            f"{wf} step {s.get('name')!r} is telemetry and must never fail the job")


@pytest.mark.parametrize("wf,job", INSTRUMENTED.items())
def test_recorder_comes_from_the_default_branch(wf, job):
    checkouts = [s for s in _steps(wf, job)
                 if str(s.get("uses", "")).startswith("actions/checkout@")
                 and "review-telemetry" in str((s.get("with") or {}).get("sparse-checkout", ""))]
    assert checkouts, f"{wf} job {job!r} doesn't check out the recorder separately from the PR head"
    for s in checkouts:
        assert "default_branch" in str((s.get("with") or {}).get("ref", "")), (
            f"{wf}: the recorder must come from the default branch, never the PR head")


@pytest.mark.parametrize("wf", sorted(set(RECORDED_BY.values())))
def test_record_job_runs_after_failures(wf):
    jobs = _load(wf)["jobs"]
    rec = [j for j in jobs.values()
           if str(j.get("uses", "")).endswith("record-docs-agent-usage.yml")]
    assert rec, f"{wf} never calls record-docs-agent-usage.yml"
    for j in rec:
        assert "always()" in str(j.get("if", "")), f"{wf}: the record-usage job must run with always()"
        perms = j.get("permissions") or {}
        assert perms.get("actions") == "read" and perms.get("id-token") == "write", (
            f"{wf}: the called workflow needs actions: read (artifacts) and id-token: write (AWS)")


def test_review_records_the_triage_run_that_triggered_it():
    rec = _load("claude-code-review.yml")["jobs"]["record-usage"]
    assert "workflow_run.id" in str((rec.get("with") or {}).get("extra-run-id", ""))


def test_collected_bundle_is_not_itself_collected_on_a_rerun():
    reusable = (WF / "record-docs-agent-usage.yml").read_text()
    data = yaml.safe_load(reusable)
    names = [str((s.get("with") or {}).get("name", ""))
             for s in data["jobs"]["collect"]["steps"]
             if str(s.get("uses", "")).startswith("actions/upload-artifact@")]
    assert names and not any(n.startswith("docs-agent-usage-") for n in names)


def test_pr_close_records_review_outcomes_from_the_default_branch():
    job = _load("pr-closed.yml")["jobs"]["record-review-outcome"]
    steps = [s for s in job["steps"] if isinstance(s, dict)]
    assert any("record-outcome.py" in str(s.get("run", "")) for s in steps)
    checkout = next(s for s in steps if str(s.get("uses", "")).startswith("actions/checkout@"))
    assert "default_branch" in str(checkout["with"]["ref"])

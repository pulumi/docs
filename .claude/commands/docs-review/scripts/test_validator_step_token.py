"""Every workflow step that runs `validate-pinned.py check --pr` must carry a
GitHub token in its env.

The validator fetches the PR diff with `gh pr diff` for the rules that exempt
content the review merely echoes (`internal-link-existence` and friends). A
step without `GH_TOKEN`/`GITHUB_TOKEN` makes that fetch fail silently, the
exemptions go dead, and on the v3 surface (no splicer, no model fallback) the
first review that quotes a dead link from the PR errors out -- #21560.
"""

from __future__ import annotations

import pathlib

import pytest
import yaml

REPO_ROOT = pathlib.Path(__file__).resolve().parents[4]
WORKFLOWS = sorted((REPO_ROOT / ".github" / "workflows").glob("*.yml"))


def _validator_steps():
    for wf in WORKFLOWS:
        data = yaml.safe_load(wf.read_text())
        for job_name, job in (data.get("jobs") or {}).items():
            for step in job.get("steps") or []:
                run = step.get("run") or ""
                if "validate-pinned.py check" in run and "--pr" in run:
                    yield wf.name, job_name, step


def test_validator_steps_exist():
    assert list(_validator_steps()), "no workflow step invokes validate-pinned.py check --pr"


@pytest.mark.parametrize("wf, job, step", list(_validator_steps()), ids=lambda v: v if isinstance(v, str) else v.get("name", "?"))
def test_validator_step_has_a_token(wf, job, step):
    env = step.get("env") or {}
    assert "GH_TOKEN" in env or "GITHUB_TOKEN" in env, (
        f"{wf} job {job!r} step {step.get('name')!r} runs validate-pinned.py check --pr "
        "without GH_TOKEN/GITHUB_TOKEN; `gh pr diff` inside the validator fails silently "
        "and every diff-based exemption goes dead"
    )

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

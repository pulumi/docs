#!/usr/bin/env python3
"""Tests for the `/deploy-staging` comment command: deploy-staging-command.py's
decisions (its --self-test is the broader table) and the shape of
.github/workflows/staging-deploy-command.yml that makes the command safe."""

from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
REPO_ROOT = HERE.parent.parent
SCRIPT = HERE / "deploy-staging-command.py"
WORKFLOW = REPO_ROOT / ".github" / "workflows" / "staging-deploy-command.yml"

_spec = importlib.util.spec_from_file_location("deploy_staging_command", SCRIPT)
dsc = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
sys.modules[_spec.name] = dsc  # @dataclass looks its module up by name
_spec.loader.exec_module(dsc)

REPO = "pulumi/docs"
SHA = "c0ffee" + "0" * 34
PR = {"state": "open", "merged": False,
      "head": {"sha": SHA, "ref": "me/infra", "repo": {"full_name": REPO}}}
WRITER = {"role_name": "write", "permission": "write"}


def _decide(**kw):
    args = dict(repo=REPO, commenter="alice", pr=PR, permission=WRITER,
                workflow_state="active", statuses=[], runs=[])
    args.update(kw)
    return dsc.decide(**args)


def test_self_test_passes():
    assert dsc._self_test() == 0


def test_deploys_the_api_head_for_a_writer():
    d = _decide()
    assert (d.action, d.head_sha, d.head_ref) == ("deploy", SHA, "me/infra")


def test_permitted_roles_and_refused_roles():
    for role in ("admin", "maintain", "write"):
        assert _decide(permission={"role_name": role}).action == "deploy", role
    for role in ("triage", "read", "none"):
        d = _decide(permission={"role_name": role})
        assert (d.action, d.reason) == ("reply", "no_write_access"), role


def test_fork_and_closed_prs_get_a_reply_not_a_deploy():
    fork = dict(PR, head=dict(PR["head"], repo={"full_name": "mallory/docs"}))
    assert _decide(pr=fork).reason == "fork"
    assert _decide(pr=dict(PR, state="closed")).reason == "closed"
    assert _decide(pr=None, pr_error="not_found").reason == "not_a_pr"


def test_existing_or_running_evidence_skips_and_a_failure_retries():
    run = {"id": 42, "head_sha": SHA, "status": "completed", "conclusion": "success",
           "html_url": "https://github.com/pulumi/docs/actions/runs/42"}
    done = _decide(runs=[run])
    assert done.reason == "already_deployed" and "runs/42" in done.reply and "`c0ffee0`" in done.reply
    assert _decide(runs=[dict(run, status="queued", conclusion=None)]).reason == "already_running"
    assert _decide(runs=[dict(run, conclusion="failure")]).action == "deploy"
    assert _decide(workflow_state="disabled_manually").reason == "disabled"


def test_started_reply_text():
    url = "https://github.com/pulumi/docs/actions/runs/9"
    reply = dsc.render_started(REPO, SHA, "alice", url)
    assert reply.splitlines()[1] == f"🤖 @alice — Staging deploy started for `c0ffee0`: {url}"
    assert dsc.runs_page(REPO) in dsc.render_started(REPO, SHA, "alice", "")


def test_constants_match_the_sentinel():
    import sentinel  # noqa: PLC0415
    assert dsc.STAGING_WORKFLOW_FILE == sentinel.STAGING_WORKFLOW_FILE
    assert dsc.STAGING_STATUS_CONTEXT == sentinel.STAGING_STATUS_CONTEXT
    assert dsc.STAGING_STATUS_WRITERS == sentinel.STAGING_STATUS_WRITERS


def _dispatch_targets(text: str) -> set[str]:
    return set(re.findall(r"^\s*(?:if\s+)?gh workflow run\s+(\S+)", text, re.M))


def test_the_command_can_only_dispatch_staging_and_the_sentinel():
    """`/deploy-staging` exists so nobody dispatches production by hand. The
    one script it runs must dispatch the staging workflow and nothing else,
    and the workflow's own dispatches are the Sentinel re-score only."""
    script = (HERE / "staging-deploy.sh").read_text()
    assert _dispatch_targets(script) == {"testing-build-and-deploy.yml"}
    wf_text = WORKFLOW.read_text()
    runs = "\n".join(s.get("run") or "" for j in yaml.safe_load(wf_text)["jobs"].values()
                     for s in j.get("steps") or [])
    assert _dispatch_targets(runs) == {"review-sentinel.yml"}
    assert "staging-deploy.sh" in runs
    # The runtime guard must compare against the staging file by name.
    assert '"gh workflow run testing-build-and-deploy.yml"' in runs
    assert not re.search(r"(?<!testing-)build-and-deploy\.yml", runs.replace(
        "never build-and-deploy.yml", "")), "the job must not name the production workflow"


def test_workflow_shape():
    data = yaml.safe_load(WORKFLOW.read_text())
    trigger = data.get("on") or data.get(True)
    assert trigger == {"issue_comment": {"types": ["created"]}}, "comment-created only"
    jobs = data["jobs"]
    gate_if = jobs["gate"]["if"]
    assert "github.event.issue.pull_request" in gate_if
    assert "'/deploy-staging'" in gate_if and "@claude" not in gate_if
    gate_runs = "\n".join(s.get("run") or "" for s in jobs["gate"]["steps"])
    assert "command-gate.py check" in gate_runs and "--command deploy-staging" in gate_runs
    assert jobs["deploy"]["if"] == "needs.gate.outputs.fire == 'true'"
    for job in jobs.values():
        for step in job.get("steps") or []:
            if str(step.get("uses", "")).startswith("actions/checkout@"):
                assert step["with"]["ref"] == "${{ github.event.repository.default_branch }}", \
                    "no PR code is ever checked out"
            run = step.get("run") or ""
            # Comment- and PR-controlled values reach bash only through env.
            assert "${{" not in run, f"{step.get('name')}: ${{{{ }}}} inside run:"
    assert "concurrency" not in jobs["gate"], "a declined comment must not displace a real one"
    assert jobs["deploy"]["concurrency"]["cancel-in-progress"] is False


def test_a_started_deploy_posts_no_comment_and_a_refusal_does():
    """The reply is for refusals: a started deploy is 🚀 on the command and the
    staging gate's status links the run, so a comment would only repeat it."""
    steps = {st.get("name"): st for st in yaml.safe_load(WORKFLOW.read_text())["jobs"]["deploy"]["steps"]}
    assert "steps.dispatch.outputs.dispatched != 'true'" in steps["Reply"]["if"]
    react = steps["React with the outcome"]
    assert "rocket" in react["run"] and "confused" in react["run"]
    gate = {st.get("name"): st for st in yaml.safe_load(WORKFLOW.read_text())["jobs"]["gate"]["steps"]}
    assert "content=eyes" in gate["Acknowledge the command"]["run"]

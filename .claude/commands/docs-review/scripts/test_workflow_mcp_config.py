"""Every claude-code-action workflow must wire the brand MCP identically.

The `--mcp-config` JSON is repeated verbatim in each workflow that runs
anthropics/claude-code-action, because the action takes it through `claude_args`
and there is no shared include. That is real drift surface: a URL change or an
added header is an N-file edit, and a missed file fails at runtime, not at lint
time -- this repo has no actionlint or any other workflow validator.

Lives here because `make test-review-pipeline` runs pytest over this directory.
"""

import json
import shlex
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parents[4]
WORKFLOWS = REPO / ".github/workflows"

EXPECTED_MCP = {
    "mcpServers": {
        "pulumi-brand": {"type": "http", "url": "https://brand.pulumi.com/mcp"}
    }
}
BRAND_TOOLS = {
    "mcp__pulumi-brand__get_guidelines",
    "mcp__pulumi-brand__search_guidelines",
}


def _claude_args(path: Path):
    """Yield each claude_args string from a workflow that uses the action."""
    data = yaml.safe_load(path.read_text())
    if not isinstance(data, dict):
        return
    for job in (data.get("jobs") or {}).values():
        for step in (job or {}).get("steps") or []:
            uses = (step or {}).get("uses") or ""
            if not uses.startswith("anthropics/claude-code-action"):
                continue
            args = ((step.get("with") or {}).get("claude_args")) or ""
            yield args


def _action_workflows():
    out = []
    for p in sorted(WORKFLOWS.glob("*.yml")):
        if "anthropics/claude-code-action" in p.read_text():
            for args in _claude_args(p):
                out.append((p.name, args))
    return out


ACTION_WORKFLOWS = _action_workflows()


def test_every_action_workflow_was_discovered():
    assert len(ACTION_WORKFLOWS) >= 8, (
        "expected at least 8 claude-code-action steps; found "
        f"{len(ACTION_WORKFLOWS)} -- did a workflow stop parsing?"
    )


@pytest.mark.parametrize("name,args", ACTION_WORKFLOWS, ids=lambda v: v if isinstance(v, str) and v.endswith(".yml") else "")
def test_claude_args_parse_as_a_shell_argv(name, args):
    """The block-scalar form must still tokenize; a broken quote splits silently."""
    tokens = shlex.split(args)
    assert tokens, f"{name}: claude_args is empty"
    assert "--mcp-config" in tokens, f"{name}: no --mcp-config"


@pytest.mark.parametrize("name,args", ACTION_WORKFLOWS, ids=lambda v: v if isinstance(v, str) and v.endswith(".yml") else "")
def test_mcp_config_json_is_identical_everywhere(name, args):
    tokens = shlex.split(args)
    payload = tokens[tokens.index("--mcp-config") + 1]
    assert json.loads(payload) == EXPECTED_MCP, (
        f"{name}: brand MCP config drifted from the other workflows. "
        "Update every claude-code-action workflow together."
    )


@pytest.mark.parametrize("name,args", ACTION_WORKFLOWS, ids=lambda v: v if isinstance(v, str) and v.endswith(".yml") else "")
def test_brand_tools_are_allowlisted(name, args):
    """Wiring the server without allowlisting its tools makes it inert."""
    tokens = shlex.split(args)
    assert "--allowed-tools" in tokens, f"{name}: no --allowed-tools"
    allowed = set(tokens[tokens.index("--allowed-tools") + 1].split(","))
    missing = BRAND_TOOLS - allowed
    assert not missing, f"{name}: brand MCP wired but tools not allowed: {missing}"

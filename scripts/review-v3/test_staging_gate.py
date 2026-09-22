"""The `/deploy-staging` permission gate, executed rather than read.

`staging-deploy-pr.yml`'s gate step is inline bash, and it has to stay
inline: it runs BEFORE the workflow's one checkout, deliberately, so there
is no script file on disk for it to call. That is the right ordering and
the wrong shape for testing, so these tests extract the step's `run:` block
out of the workflow YAML by step name and run it against a fake `gh`.

Extraction beats a transcribed copy. A copy is a second source of truth
that passes forever after the workflow it mirrors has changed; pulling the
real string means an edit to the step is an edit to what these tests run.

Why this file exists at all: as of the commit that added it, this workflow
had ~990 runs and every one of them short-circuited on the `if:` — nobody
had ever typed `/deploy-staging`. Its own header records the class of bug
that lay in wait (a missing `pull-requests: write`, found only because the
same mistake surfaced in PR #21642). The membership gate decides who can
spend a slot on the shared staging stack, and it had never once been
executed. These tests execute it.
"""

import os
import shutil
import subprocess
import textwrap
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
WORKFLOW = REPO_ROOT / ".github/workflows/staging-deploy-pr.yml"
ROUTING = REPO_ROOT / ".github/review-routing.yml"
STEP_NAME = "Gate and gather PR facts"

pytestmark = pytest.mark.skipif(
    shutil.which("bash") is None or shutil.which("jq") is None,
    reason="gate script needs bash and jq",
)


def gate_script() -> str:
    """The real `run:` body of the gate step, by step name."""
    workflow = yaml.safe_load(WORKFLOW.read_text(encoding="utf-8"))
    steps = workflow["jobs"]["deploy"]["steps"]
    for step in steps:
        if step.get("name") == STEP_NAME:
            return step["run"]
    raise AssertionError(
        f"no step named {STEP_NAME!r} in {WORKFLOW} — did the step get renamed?"
    )


def routing_teams() -> list[str]:
    """Every team slug the gate should accept, in the gate's own order."""
    teams = yaml.safe_load(ROUTING.read_text(encoding="utf-8"))["teams"]
    return [teams[role] for role in sorted(teams)]


# A fake `gh`. Each membership lookup answers from MEMBERSHIPS, written by
# the test as "<org>/<slug>/<login>=<state>" lines; a slug listed in
# ERRORING_TEAMS fails the way a token or network problem does (not a 404),
# which is the branch that must refuse differently. Everything the fake
# refuses is recorded, so a test can assert on the comment body a real
# reviewer would have read.
FAKE_GH = r"""#!/usr/bin/env bash
set -uo pipefail

# `gh api --method POST repos/<r>/issues/<n>/comments -f body=<text>`
if [ "${1:-}" = "api" ] && [ "${2:-}" = "--method" ] && [ "${3:-}" = "POST" ]; then
  for arg in "$@"; do
    case "$arg" in
      body=*) printf '%s' "${arg#body=}" > "$REFUSAL_FILE" ;;
    esac
  done
  echo '{}'
  exit 0
fi

# Honor `--jq <expr>` the way the real gh does — the gate pipes
# `--jq .content` straight into base64, so a fake that ignored it would
# hand base64 a JSON object and fail for a reason the gate never could.
ENDPOINT=""
JQ_EXPR=""
shift                     # drop `api`
while [ "$#" -gt 0 ]; do
  case "$1" in
    --jq) JQ_EXPR="$2"; shift 2 ;;
    -*)   shift ;;
    *)    [ -n "$ENDPOINT" ] || ENDPOINT="$1"; shift ;;
  esac
done

emit() {
  if [ -n "$JQ_EXPR" ]; then
    printf '%s' "$1" | jq -r "$JQ_EXPR"
  else
    printf '%s\n' "$1"
  fi
}

case "$ENDPOINT" in
  repos/*/contents/.github/review-routing.yml)
    emit "$(base64 < "$ROUTING_FILE" | tr -d '\n' | jq -R '{content: .}')"
    exit 0
    ;;
  orgs/*/teams/*/memberships/*)
    REST="${ENDPOINT#orgs/}"
    ORG="${REST%%/*}"
    REST="${REST#*/teams/}"
    SLUG="${REST%%/*}"
    LOGIN="${REST##*/}"
    case " $ERRORING_TEAMS " in
      *" $SLUG "*)
        echo "gh: Bad credentials (HTTP 401)" >&2
        exit 1
        ;;
    esac
    STATE=$(printf '%s\n' "$MEMBERSHIPS" | sed -n "s|^$ORG/$SLUG/$LOGIN=||p")
    if [ -z "$STATE" ]; then
      echo "gh: Not Found (HTTP 404)" >&2
      exit 1
    fi
    emit "$(jq -n --arg s "$STATE" '{state: $s}')"
    exit 0
    ;;
  repos/*/pulls/*)
    emit "$(jq -n --arg repo "$PR_HEAD_REPO" \
      '{head: {sha: "b621df57cd96166c6e8597108e310e70e8c08665",
               ref: "camsoper/loving-brown-wsse8v",
               repo: {full_name: $repo}}}')"
    exit 0
    ;;
esac

echo "fake gh: unexpected call: $ENDPOINT" >&2
exit 90
"""


class GateResult:
    def __init__(self, proc, refusal, outputs, log):
        self.proc = proc
        self.refusal = refusal
        self.outputs = outputs
        self.log = log

    @property
    def refused(self) -> bool:
        return self.outputs.get("refused") == "true"


def run_gate(tmp_path, *, actor="someone", memberships=None,
             erroring_teams=(), head_repo="pulumi/docs") -> GateResult:
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    fake = bin_dir / "gh"
    fake.write_text(FAKE_GH, encoding="utf-8")
    fake.chmod(0o755)

    refusal_file = tmp_path / "refusal.txt"
    output_file = tmp_path / "github_output"
    output_file.touch()

    env = {
        **os.environ,
        "PATH": f"{bin_dir}{os.pathsep}{os.environ['PATH']}",
        "GITHUB_OUTPUT": str(output_file),
        "REFUSAL_FILE": str(refusal_file),
        "ROUTING_FILE": str(ROUTING),
        "MEMBERSHIPS": "\n".join(memberships or []),
        "ERRORING_TEAMS": " ".join(erroring_teams),
        "PR_HEAD_REPO": head_repo,
        # The step's own `env:` block.
        "GH_TOKEN": "fake-github-token",
        "TEAM_TOKEN": "fake-team-token",
        "ACTOR": actor,
        "PR": "21789",
        "REPO": "pulumi/docs",
    }

    proc = subprocess.run(
        ["bash", "-c", gate_script()],
        env=env, capture_output=True, text=True, timeout=120,
    )
    outputs = {}
    for line in output_file.read_text(encoding="utf-8").splitlines():
        if "=" in line:
            key, _, value = line.partition("=")
            outputs[key] = value
    refusal = (refusal_file.read_text(encoding="utf-8")
               if refusal_file.exists() else "")
    return GateResult(proc, refusal, outputs,
                      proc.stdout + proc.stderr)


def member_of(team_ref, login="someone", state="active"):
    return [f"{team_ref}/{login}={state}"]


# --- the widening itself ------------------------------------------------

@pytest.mark.parametrize("team_ref", routing_teams())
def test_any_review_team_may_deploy(tmp_path, team_ref):
    """Every team under `teams:` clears the gate, not just tools.

    Parametrized over the routing config rather than a hardcoded list, so
    adding a review team extends this test by itself — and so a team added
    to `teams:` that the gate somehow cannot see fails here rather than in
    a reviewer's confused comment thread.
    """
    result = run_gate(tmp_path, memberships=member_of(team_ref))
    assert not result.refused, result.log
    assert result.outputs["head_sha"].startswith("b621df57"), result.outputs
    assert result.refusal == ""


def test_non_member_is_refused_and_told_who_can(tmp_path):
    result = run_gate(tmp_path, memberships=[])
    assert result.refused, result.log
    assert "limited to members of a review team" in result.refusal
    # The refusal has to name somebody reachable, or it is a dead end.
    for team_ref in routing_teams():
        assert team_ref in result.refusal, result.refusal


def test_pending_invitation_is_not_membership(tmp_path):
    """`pending` means invited, not joined. Only `active` counts."""
    result = run_gate(
        tmp_path,
        memberships=member_of(routing_teams()[0], state="pending"),
    )
    assert result.refused, result.log
    assert "limited to members of a review team" in result.refusal


# --- fail-closed, and saying which kind of closed -----------------------

def test_lookup_failure_refuses_rather_than_guessing(tmp_path):
    """A token or API problem must never be read as permission.

    This is the branch that decides whether a broken credential silently
    opens the gate. It refuses, and says so in different words than a
    non-member gets, because "we could not check" and "you are not on the
    list" call for different next actions.
    """
    result = run_gate(tmp_path, erroring_teams=[
        ref.split("/", 1)[1] for ref in routing_teams()
    ])
    assert result.refused, result.log
    assert "could not verify your team membership" in result.refusal
    assert "limited to members of a review team" not in result.refusal


def test_one_broken_team_does_not_block_a_member_of_another(tmp_path):
    """A partial outage degrades to the teams that did answer.

    The loop breaks on the first `active`, so a team that errors earlier in
    the order must not strand a member of a later one.
    """
    teams = routing_teams()
    assert len(teams) > 1, "this test needs at least two review teams"
    result = run_gate(
        tmp_path,
        memberships=member_of(teams[-1]),
        erroring_teams=[teams[0].split("/", 1)[1]],
    )
    assert not result.refused, result.log


def test_non_member_during_partial_outage_gets_the_cautious_refusal(tmp_path):
    """Unverifiable beats not-a-member when both are true.

    Someone who is on no team that answered, while another team errored,
    cannot be told they are not a member — nobody knows that.
    """
    teams = routing_teams()
    result = run_gate(
        tmp_path,
        memberships=[],
        erroring_teams=[teams[0].split("/", 1)[1]],
    )
    assert result.refused, result.log
    assert "could not verify your team membership" in result.refusal


# --- guards the widening must not have loosened -------------------------

def test_fork_head_is_still_refused_for_a_review_team_member(tmp_path):
    """The fork guard is what bounds the blast radius of the widening.

    Widening the gate is only safe because this refusal keeps it to
    branches in this repo. A member clearing the membership check must
    still be stopped by a fork head.
    """
    result = run_gate(
        tmp_path,
        memberships=member_of(routing_teams()[0]),
        head_repo="someone-else/docs",
    )
    assert result.refused, result.log
    assert "lives on a fork" in result.refusal


def test_gate_reports_each_team_it_consulted(tmp_path):
    """The run log has to show why a refusal happened.

    A gate that refuses without saying which lookups it made, and what they
    said, is a gate nobody can debug from the Actions tab.
    """
    result = run_gate(tmp_path, memberships=[])
    for team_ref in routing_teams():
        assert f"{team_ref}: not-a-member" in result.log, result.log


def test_extraction_is_pointed_at_a_real_step():
    """If the step is renamed, fail here rather than silently testing nothing."""
    script = gate_script()
    assert "refuse()" in script
    assert "review-routing.yml" in script


def test_g4_remedy_text_matches_who_the_gate_accepts():
    """The Sentinel's advice and the gate's rule are one fact, stated twice.

    G4's message tells a blocked author who can retry. If it still says
    tools-team while the gate accepts any review team, the PR sits waiting
    on one person for no reason.
    """
    sentinel_src = (REPO_ROOT / "scripts/review-v3/sentinel.py").read_text(
        encoding="utf-8")
    start = sentinel_src.index('"G4 infra-evidence", "red"')
    message = sentinel_src[start:start + 800]
    assert "any review team" in message, textwrap.shorten(message, 400)
    assert "tools-team" not in message, textwrap.shorten(message, 400)

#!/usr/bin/env python3
"""Tests for ack-request.sh — success acknowledgment by reaction, with the
timeline comment as the fallback. `gh` is stubbed on PATH; the stub logs
each call and fails the reactions endpoint when told to."""

from __future__ import annotations

import os
import stat
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPT = HERE / "ack-request.sh"

STUB = """#!/usr/bin/env bash
ARGS="$*"; printf '%s\\n' "${ARGS//$'\\n'/\\\\n}" >> "$GH_LOG"
case "$*" in
  *reactions*) [ -n "${GH_FAIL_REACTION:-}" ] && exit 1 ;;
esac
exit 0
"""


def run(tmp_path: Path, *args: str, fail_reaction: bool = False) -> tuple[int, list[str]]:
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir(exist_ok=True)
    gh = bin_dir / "gh"
    gh.write_text(STUB)
    gh.chmod(gh.stat().st_mode | stat.S_IEXEC)
    log = tmp_path / "gh.log"
    log.write_text("")
    env = dict(os.environ, PATH=f"{bin_dir}:{os.environ['PATH']}", GH_LOG=str(log))
    env.pop("GITHUB_REPOSITORY", None)
    if fail_reaction:
        env["GH_FAIL_REACTION"] = "1"
    proc = subprocess.run(["bash", str(SCRIPT), *args], env=env, capture_output=True, text=True)
    return proc.returncode, [ln for ln in log.read_text().splitlines() if ln]


def test_issue_comment_target_gets_a_reaction_and_no_comment(tmp_path):
    rc, calls = run(tmp_path, "--pr", "7", "--repo", "o/r", "--target", "issues/comments/42", "--message", "m")
    assert rc == 0
    assert calls == ["api -X POST repos/o/r/issues/comments/42/reactions -f content=rocket"]


def test_review_comment_target_uses_the_pulls_endpoint(tmp_path):
    rc, calls = run(tmp_path, "--pr", "7", "--repo", "o/r", "--target", "pulls/comments/9", "--message", "m")
    assert rc == 0 and calls == ["api -X POST repos/o/r/pulls/comments/9/reactions -f content=rocket"]


def test_no_target_falls_back_to_the_progress_comment(tmp_path):
    rc, calls = run(tmp_path, "--pr", "7", "--repo", "o/r", "--target", "", "--message", "🤖 done")
    assert rc == 0 and len(calls) == 1
    assert calls[0].startswith("api repos/o/r/issues/7/comments -f body=<!-- CLAUDE_PROGRESS -->")
    assert "🤖 done" in calls[0]


def test_failed_reaction_falls_back_so_the_requester_still_hears_back(tmp_path):
    rc, calls = run(tmp_path, "--pr", "7", "--repo", "o/r", "--target", "issues/comments/42",
                    "--message", "m", fail_reaction=True)
    assert rc == 0 and len(calls) == 2 and "issues/7/comments" in calls[1]


def test_malformed_target_is_ignored_not_interpolated(tmp_path):
    rc, calls = run(tmp_path, "--pr", "7", "--repo", "o/r", "--target", "../../orgs/x", "--message", "m")
    assert rc == 0 and len(calls) == 1 and "reactions" not in calls[0]


def test_nothing_to_do_is_a_no_op(tmp_path):
    rc, calls = run(tmp_path, "--pr", "7", "--repo", "o/r", "--target", "", "--message", "")
    assert rc == 0 and calls == []


def test_missing_repo_is_a_usage_error(tmp_path):
    rc, _ = run(tmp_path, "--pr", "7", "--target", "issues/comments/1")
    assert rc == 2

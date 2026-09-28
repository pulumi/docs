"""with-pr-files.sh: the paginated PR file list must survive a PR of any size.

Adversarial review of #21948: triage merged the REST file list into the PR
JSON with `jq --argjson f "$ALL_FILES"`. One argv string is capped at 128 KiB
on Linux (MAX_ARG_STRLEN), so a ~1,000-file PR failed with "Argument list too
long" -- and under `set -e` + `continue-on-error` triage went green without
the `review:oversized` label, sending the PR to a full model review.
"""

from __future__ import annotations

import json
import os
import pathlib
import subprocess
import sys

import pytest

HERE = pathlib.Path(__file__).resolve().parent
SCRIPT = HERE / "with-pr-files.sh"
REPO_ROOT = HERE.parents[3]
TRIAGE = REPO_ROOT / ".github" / "workflows" / "claude-triage.yml"

N_FILES = 1200


def _fake_gh(tmp_path: pathlib.Path, n: int, fail: bool = False) -> dict:
    """A `gh` on PATH whose `api --paginate … --jq` prints one file object per
    line, as the real one does across pages."""
    bindir = tmp_path / "bin"
    bindir.mkdir()
    gh = bindir / "gh"
    if fail:
        gh.write_text("#!/usr/bin/env bash\nexit 1\n")
    else:
        lines = tmp_path / "files.jsonl"
        with lines.open("w") as fh:
            for i in range(n):
                path = f"content/docs/iac/guides/migration/migrating-to-pulumi/generated/page-{i:05d}-with-a-long-slug.md"
                fh.write(json.dumps({"path": path, "additions": 1, "deletions": 0}) + "\n")
        gh.write_text(f"#!/usr/bin/env bash\ncat {lines}\n")
    gh.chmod(0o755)
    return {**os.environ, "PATH": f"{bindir}:{os.environ['PATH']}"}


def _run(env: dict, pr_json: dict) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["bash", str(SCRIPT), "--repo", "pulumi/docs", "--pr", "21936"],
        input=json.dumps(pr_json), capture_output=True, text=True, env=env, check=False)


def test_twelve_hundred_files_merge_without_touching_argv(tmp_path):
    env = _fake_gh(tmp_path, N_FILES)
    listing = (tmp_path / "files.jsonl").read_text()
    assert len(listing.encode()) > 128 * 1024, "fixture must exceed MAX_ARG_STRLEN to prove anything"
    pr = {"additions": 1200, "deletions": 0, "changedFiles": N_FILES,
          "files": [{"path": "first-page-only.md", "additions": 1, "deletions": 0}]}
    r = _run(env, pr)
    assert r.returncode == 0, r.stderr
    out = json.loads(r.stdout)
    assert len(out["files"]) == N_FILES
    assert out["changedFiles"] == N_FILES and out["additions"] == 1200


@pytest.mark.skipif(not sys.platform.startswith("linux"), reason="MAX_ARG_STRLEN is Linux-specific")
def test_the_old_argv_path_overflows_at_this_size(tmp_path):
    """Reproduces the bug the script exists to avoid."""
    _fake_gh(tmp_path, N_FILES)
    files = json.dumps([json.loads(l) for l in (tmp_path / "files.jsonl").read_text().splitlines()])
    with pytest.raises(OSError) as exc:
        subprocess.run(["jq", "-n", "--argjson", "f", files, "$f | length"],
                       capture_output=True, text=True, check=False)
    assert "too long" in str(exc.value).lower()


def test_a_failed_listing_keeps_the_input(tmp_path):
    env = _fake_gh(tmp_path, 0, fail=True)
    pr = {"files": [{"path": "a.md", "additions": 1, "deletions": 0}], "additions": 1}
    r = _run(env, pr)
    assert r.returncode == 0 and json.loads(r.stdout) == pr


def test_triage_never_passes_the_file_list_through_argv():
    text = TRIAGE.read_text()
    assert "--argjson f" not in text
    assert text.count("docs-review/scripts/with-pr-files.sh --repo") == 2, "classification and routing both use the helper"


def test_the_merged_list_classifies_as_oversized(tmp_path):
    """End to end: the helper's output is what triage-classify.py reads."""
    env = _fake_gh(tmp_path, N_FILES)
    pr = {"title": "t", "body": "", "labels": [], "additions": 1200, "deletions": 0,
          "changedFiles": N_FILES, "files": []}
    r = _run(env, pr)
    data = tmp_path / "pr.json"
    data.write_text(r.stdout)
    c = subprocess.run([sys.executable, str(HERE / "triage-classify.py"), str(data)],
                       input="", capture_output=True, text=True, check=False)
    assert c.returncode == 0, c.stderr
    assert json.loads(c.stdout)["oversized"] is True

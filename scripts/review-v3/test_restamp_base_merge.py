#!/usr/bin/env python3
"""Tests for restamp-base-merge.py — carrying a v3 review across a base-only
merge (#21673) and refusing to whenever the diff the review read changed."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


rb = _load("restamp_base_merge", HERE / "restamp-base-merge.py")
sentinel = rb.sentinel

REVIEWED = "1" * 40
MERGE = "2" * 40
HEAD = "3" * 40


def card(head=REVIEWED) -> str:
    return (
        "<!-- CLAUDE_REVIEW 1/1 -->\n"
        f"{sentinel.AUTHOR_MARKER}\n"
        f"<!-- CLAUDE_REVIEW_HEAD {head} -->\n"
        "## Author action guide v2 — nothing blocks merge\n\n"
        '<!-- REVIEW_STATE {"findings":{},"high_water":0,"schema":1} -->\n\n'
        f"<sub>Review v2 · updated 2026-09-17T00:00:00Z · head commit {head[:7]}</sub>\n"
    )


def commit(sha, parents=1):
    return {"sha": sha, "parents": [{"sha": "p"}] * parents}


FILES = [{"filename": "content/docs/x.md", "patch": "@@ -1,2 +1,2 @@\n-old\n+new\n ctx"}]
# The base moved: hunk header and context differ, the PR's own lines don't.
FILES_AFTER_MERGE = [{"filename": "content/docs/x.md", "patch": "@@ -9,2 +9,2 @@\n-old\n+new\n other ctx"}]


class FakeGh:
    repo = "pulumi/docs"

    def __init__(self, body, commits, files_then, files_now, head=HEAD):
        self.body, self.commits = body, commits
        self.files_then, self.files_now, self.head = files_then, files_now, head
        self.patched = []

    def pr(self, _n):
        return {"head": {"sha": self.head}, "base": {"ref": "master"}}

    def issue_comments(self, _n):
        return [{"id": 7, "user": {"login": "github-actions[bot]"}, "body": self.body}]

    def pr_commits(self, _n):
        return self.commits

    def pr_files(self, _n):
        return self.files_now

    def compare_files(self, base, sha):
        assert (base, sha) == ("master", REVIEWED)
        return self.files_then

    def get(self, path):
        assert path.endswith("/issues/comments/7")
        return {"id": 7, "body": getattr(self, "body_at_write", self.body)}

    def patch(self, path, body):
        self.patched.append((path, body["body"]))


def test_a_base_only_merge_moves_the_head_carriers_and_nothing_else():
    gh = FakeGh(card(), [commit(REVIEWED), commit(MERGE, 2), commit(HEAD, 2)], FILES, FILES_AFTER_MERGE)
    out = rb.run(gh, 21673)
    assert out["restamped"] is True
    (path, body), = gh.patched
    assert path.endswith("/issues/comments/7")
    assert f"<!-- CLAUDE_REVIEW_HEAD {HEAD} -->" in body and REVIEWED not in body
    assert f"head commit {HEAD[:7]}</sub>" in body
    assert "updated 2026-09-17T00:00:00Z" in body, "composition stamp untouched (stale-publish guard)"
    assert sentinel._body_matches_head(body, HEAD)


def test_a_real_commit_since_the_review_is_not_restamped():
    gh = FakeGh(card(), [commit(REVIEWED), commit(MERGE, 2), commit(HEAD, 1)], FILES, FILES_AFTER_MERGE)
    assert rb.run(gh, 1)["restamped"] is False and not gh.patched


def test_a_conflict_resolution_that_edits_the_prs_lines_is_not_restamped():
    changed = [{"filename": "content/docs/x.md", "patch": "@@ -1,2 +1,2 @@\n-old\n+newer\n ctx"}]
    gh = FakeGh(card(), [commit(REVIEWED), commit(HEAD, 2)], FILES, changed)
    out = rb.run(gh, 1)
    assert out["restamped"] is False and "conflict" in out["reason"] and not gh.patched


def test_unknown_reviewed_head_or_legacy_review_fails_closed():
    gh = FakeGh(card(head="9" * 40), [commit(REVIEWED), commit(HEAD, 2)], FILES, FILES)
    assert rb.run(gh, 1)["restamped"] is False
    legacy = FakeGh("<!-- CLAUDE_REVIEW 1/1 -->\nv2\n", [commit(HEAD, 2)], FILES, FILES)
    assert rb.run(legacy, 1) == {"restamped": False, "reason": "no v3 author card", "head": HEAD}


def test_a_current_card_is_left_alone():
    gh = FakeGh(card(head=HEAD), [commit(HEAD)], FILES, FILES)
    assert rb.run(gh, 1)["restamped"] is False and not gh.patched


def test_dry_run_decides_without_writing():
    gh = FakeGh(card(), [commit(REVIEWED), commit(HEAD, 2)], FILES, FILES_AFTER_MERGE)
    assert rb.run(gh, 1, dry_run=True)["restamped"] is True and not gh.patched


def test_a_card_republished_mid_decision_is_not_overwritten():
    """Adversarial review of #21948: the restamp read the card, made several
    API calls, then PATCHed the whole stale body over a refresh that landed
    in between."""
    gh = FakeGh(card(), [commit(REVIEWED), commit(HEAD, 2)], FILES, FILES_AFTER_MERGE)
    gh.body_at_write = card().replace("nothing blocks merge", "1 item needs your answer")
    out = rb.run(gh, 1)
    assert out["restamped"] is False and "changed" in out["reason"] and not gh.patched


def test_a_patchless_file_must_keep_its_blob_to_count_as_unchanged():
    """Adversarial review of #21948: GitHub omits `patch` for large and
    binary files, and two empty patches compared equal whatever changed."""
    big_then = [{"filename": "static/big.json", "sha": "a" * 40}]
    big_now = [{"filename": "static/big.json", "sha": "b" * 40}]
    gh = FakeGh(card(), [commit(REVIEWED), commit(HEAD, 2)], big_then, big_now)
    out = rb.run(gh, 1)
    assert out["restamped"] is False and "patch" in out["reason"] and not gh.patched
    same = FakeGh(card(), [commit(REVIEWED), commit(HEAD, 2)], big_then, list(big_then))
    assert rb.run(same, 1)["restamped"] is True
    no_sha = FakeGh(card(), [commit(REVIEWED), commit(HEAD, 2)],
                    [{"filename": "static/big.json"}], [{"filename": "static/big.json"}])
    assert rb.run(no_sha, 1)["restamped"] is False, "no blob sha → fail closed"

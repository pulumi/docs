#!/usr/bin/env python3
"""Tests for cleanup-review-leftovers.py — the one-time sweep. Every action
kind is planned from a fake PR, and nothing is written without --apply."""

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


cl = _load("cleanup_review_leftovers", HERE / "cleanup-review-leftovers.py")
sentinel = cl.sentinel
HEAD = "d" * 40
BOT = {"login": "github-actions[bot]"}


def card(head=HEAD, open_row=False):
    rows = ("| ID | Where | Finding |\n|---|---|---|\n| **F1** | `x.md` L1 | bad |\n"
            if open_row else "_Nothing to fix — this section is empty._\n")
    return ("<!-- CLAUDE_REVIEW 1/1 -->\n" + sentinel.AUTHOR_MARKER + "\n"
            f"<!-- CLAUDE_REVIEW_HEAD {head} -->\n## Author action guide v2 — x\n\n"
            "### 🚨 Fix or disagree\n\n" + rows + "\n"
            '<!-- REVIEW_STATE {"findings":{},"high_water":1,"schema":1} -->\n')


class FakeGh:
    repo = "pulumi/docs"

    def __init__(self, comments, labels=("review:stale",), state="open"):
        self.comments, self.labels, self.state = comments, labels, state
        self.writes = []

    def pr(self, _n):
        return {"state": self.state, "head": {"sha": HEAD}, "base": {"ref": "master"},
                "labels": [{"name": l} for l in self.labels]}

    def issue_comments(self, _n):
        return self.comments

    def pr_commits(self, _n):
        return [{"sha": HEAD, "parents": [{}]}]

    def pr_files(self, _n):
        return []

    def compare_files(self, *_a):
        return []

    def delete(self, path):
        self.writes.append(("DELETE", path))

    def post(self, path, body):
        self.writes.append(("POST", path, body))

    def patch(self, path, body):
        self.writes.append(("PATCH", path))


def test_every_leftover_kind_is_planned():
    comments = [
        {"id": 1, "user": {"login": "pulumi-bot"}, "body": "<!-- CLAUDE_REVIEW 1/1 -->\n## Pre-merge Review\n"},
        {"id": 2, "user": BOT, "created_at": "2026-09-20T00:00:00Z",
         "body": "<!-- CLAUDE_PROGRESS -->\n🤖 Review errored. Flip to draft…"},
        {"id": 3, "user": BOT, "created_at": "2026-09-21T00:00:00Z", "updated_at": "2026-09-22T00:00:00Z",
         "body": card()},
        {"id": 4, "user": BOT, "created_at": "2026-09-23T00:00:00Z",
         "body": "<!-- CLAUDE_PROGRESS -->\n🤖 Review errored. (after the card: still news)"},
        {"id": 5, "user": {"login": "someone"}, "body": "<!-- CLAUDE_REVIEW 1/1 -->\nquoting"},
    ]
    gh = FakeGh(comments)
    kinds = {(a["kind"], a.get("delete_comment"), a.get("set_label")) for a in cl.plan_pr(gh, 7)}
    assert kinds == {("legacy-page", 1, None), ("errored-notice", 2, None),
                     ("stale-label", None, "review:no-blockers")}
    assert gh.writes == [], "planning never writes"


def test_stale_label_only_when_the_card_is_actually_current():
    gh = FakeGh([{"id": 3, "user": BOT, "body": card(head="e" * 40)}])
    assert [a for a in cl.plan_pr(gh, 7) if a["kind"] == "stale-label"] == []
    gh = FakeGh([{"id": 3, "user": BOT, "body": card(open_row=True)}])
    (a,) = cl.plan_pr(gh, 7)
    assert a["set_label"] == "review:outstanding-issues"


def test_apply_sets_one_state_label_and_deletes():
    gh = FakeGh([])
    cl.apply_action(gh, {"pr": 7, "kind": "stale-label", "restamp": False,
                         "set_label": "review:no-blockers"})
    assert ("POST", "repos/pulumi/docs/issues/7/labels", {"labels": ["review:no-blockers"]}) in gh.writes
    assert ("DELETE", "repos/pulumi/docs/issues/7/labels/review:stale") in gh.writes
    cl.apply_action(gh, {"pr": 7, "kind": "errored-notice", "delete_comment": 9})
    assert ("DELETE", "repos/pulumi/docs/issues/comments/9") in gh.writes


def test_a_closed_pr_only_loses_the_stray_status_comment():
    gh = FakeGh([{"id": 8, "user": BOT, "body": sentinel.STATUS_MARKER + "\n## Sentinel"},
                 {"id": 9, "user": BOT, "body": card()}], state="closed")
    assert cl.plan_pr(gh, 2) == [{"pr": 2, "kind": "stray-status", "delete_comment": 8}]

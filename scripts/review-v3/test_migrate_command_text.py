#!/usr/bin/env python3
"""Tests for migrate-command-text.py — rewriting the retired review-command
text on live bot comments after pulumi/docs#22277 (the --self-test is the
broader table of shapes)."""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


mct = _load("migrate_command_text", HERE / "migrate-command-text.py")
from gh_client import GhClient  # noqa: E402

FIXTURES = HERE / "testdata" / "migrate-command-text"
REPO = "pulumi/docs"
BOT = {"login": "github-actions[bot]"}


def test_old_cards_become_the_cards_the_composer_renders_now():
    """The fixtures are the composer's goldens from just before and just after
    #22277, so this is the whole contract: an old card, migrated, is byte for
    byte the card a fresh review would post."""
    for name in ("v3-fixture-author", "v3-fixture-brief", "golden-v2"):
        old = (FIXTURES / f"old-{name}.md.txt").read_text()
        new = (FIXTURES / f"new-{name}.md.txt").read_text()
        got, fired = mct.migrate(old)
        assert got == new, name
        assert fired, name
        assert mct.residue(got) == [], name
        assert mct.migrate(new)[0] == new, f"{name}: a migrated card must be left alone"


def test_review_state_and_markers_are_untouched():
    old = (FIXTURES / "old-v3-fixture-author.md.txt").read_text()
    got, _ = mct.migrate(old)
    keep = [ln for ln in old.splitlines() if ln.startswith("<!--") or "REVIEW_STATE" in ln or "<sub>" in ln]
    assert keep and all(ln in got.splitlines() for ln in keep)


def _snapshot(tmp_path: Path, comments_by_pr: dict[int, list[dict]], fresh: dict[int, str] | None = None) -> Path:
    root = tmp_path / "snap"
    d = root / "GET" / "repos" / REPO / "pulls__state=open.json"
    d.parent.mkdir(parents=True, exist_ok=True)
    d.write_text(json.dumps([{"number": n} for n in comments_by_pr]))
    for n, comments in comments_by_pr.items():
        f = root / "GET" / "repos" / REPO / "issues" / str(n) / "comments.json"
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(json.dumps(comments))
        for c in comments:
            body = (fresh or {}).get(c["id"], c["body"])
            g = root / "GET" / "repos" / REPO / "issues" / "comments" / f"{c['id']}.json"
            g.parent.mkdir(parents=True, exist_ok=True)
            g.write_text(json.dumps({**c, "body": body}))
    return root


def _comments():
    card = (FIXTURES / "old-v3-fixture-author.md.txt").read_text()
    return {
        101: [
            {"id": 1, "user": BOT, "body": card},
            {"id": 2, "user": {"login": "alice"}, "body": "@claude F1: sourced it #update-review"},
            {"id": 3, "user": BOT, "body": "<!-- REVIEW_COMMAND_REDIRECT -->\n`@claude … #update-review` is retired"},
            {"id": 4, "user": {"login": "pulumi-bot"},
             "body": "<!-- glowup-autofix pass=1 -->\n@claude answering for the glow-up automation:\n\n#update-review"},
        ],
        102: [
            {"id": 5, "user": BOT, "body": "<!-- SENTINEL_STATUS -->\n| 🔴 | **G1 review-ran** | comment "
                                           "`@claude <what changed> #update-review` to refresh it, or `@claude #new-review` for a fresh one. |"},
            {"id": 6, "user": BOT, "body": "<!-- SENTINEL_STATUS -->\nalready `/update-review`"},
        ],
    }


def test_dry_run_plans_only_our_comments_and_writes_nothing(tmp_path):
    root = _snapshot(tmp_path, _comments())
    rc = mct.main(["--repo", REPO, "--snapshot-dir", str(root), "--report", str(tmp_path / "r.md")])
    assert rc == 0
    assert not (root / "writes.jsonl").exists()
    p = mct.plan(GhClient(REPO, backend="snapshot", snapshot_dir=root))
    assert sorted(e["id"] for e in p["edits"]) == [1, 5]
    assert p["residue"] == [] and p["errors"] == []
    report = (tmp_path / "r.md").read_text()
    assert "dry run" in report and "**2** to edit" in report and "+| 🔴 | **G1 review-ran** | comment `/update-review <what changed>`" in report


def test_apply_rereads_each_comment_and_patches_only_what_still_needs_it(tmp_path):
    comments = _comments()
    migrated_card, _ = mct.migrate(comments[101][0]["body"])
    # Comment 1 was republished (already new text) between plan and write.
    root = _snapshot(tmp_path, comments, fresh={1: migrated_card})
    rc = mct.main(["--repo", REPO, "--snapshot-dir", str(root), "--apply"])
    assert rc == 0
    writes = [json.loads(ln) for ln in (root / "writes.jsonl").read_text().splitlines()]
    assert [w["path"] for w in writes] == [f"repos/{REPO}/issues/comments/5"]
    assert writes[0]["method"] == "PATCH"
    assert "`/update-review <what changed>`" in writes[0]["body"]["body"]
    assert "`/new-review` for a fresh one" in writes[0]["body"]["body"]


def test_the_workflow_is_a_dry_run_unless_told_otherwise():
    wf = yaml.safe_load((REPO_ROOT / ".github" / "workflows" / "review-command-text-migration.yml").read_text())
    on = wf.get("on") or wf.get(True)
    assert list(on) == ["workflow_dispatch"], "one-off: dispatch only"
    assert on["workflow_dispatch"]["inputs"]["apply"]["default"] is False
    run = "\n".join(s.get("run") or "" for s in wf["jobs"]["migrate"]["steps"])
    assert "migrate-command-text.py" in run and '"$APPLY" = "true"' in run

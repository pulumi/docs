#!/usr/bin/env python3
"""Tests for apply-update.py — the v3 update lane's deterministic renderer.

The heavy truth-table lives in the script's own `--self-test` (every action,
the /resolve race, auto-mode drops, demotion/unknown-id rejection, evidence
carry-forward + degraded path); this file makes pytest collection run it and
adds the cases that read better as separate tests.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod  # before exec — @dataclass needs the module registered
    spec.loader.exec_module(mod)
    return mod


au = _load("apply_update", HERE / "apply-update.py")

AUTHOR = (HERE / "testdata" / "v3-fixture-author.md").read_text()
BRIEF = (HERE / "testdata" / "v3-fixture-brief.md").read_text()
SHA = "c" * 40


def _update(findings, case="mixed"):
    return {"schema": 1, "case": case, "history_summary": "test", "findings": findings}


def test_self_test_suite():
    assert au._self_test() == 0


def test_retext_preserves_id_and_anchor():
    up = _update([{"id": "F3", "action": "retext", "text": "sharper question for the author"}])
    a_out, _, state, _ = au.apply(AUTHOR, BRIEF, up, head_sha=SHA, actor="cam", auto=False)
    assert "sharper question for the author" in a_out
    assert "| **F3** | `content/docs/iac/x.md` L61 |" in a_out
    assert "F3" not in state["findings"], "retext writes no disposition"


def test_resolve_without_annotation_rejected():
    up = _update([{"id": "F1", "action": "resolve"}])
    try:
        au.apply(AUTHOR, BRIEF, up, head_sha=SHA, actor="cam", auto=False)
    except au.UpdateError as exc:
        assert "annotation" in str(exc)
    else:
        raise AssertionError("resolve without annotation must be rejected")


def test_emptied_section_gets_placeholder():
    up = _update([
        {"id": "F1", "action": "resolve", "annotation": "fixed in d4d5d6"},
        {"id": "F2", "action": "resolve", "annotation": "fixed in d4d5d6"},
    ])
    a_out, _, _, report = au.apply(AUTHOR, BRIEF, up, head_sha=SHA, actor="cam", auto=False)
    assert au.SECTION_EMPTY["outstanding"] in a_out
    assert report["blocking"] == 1  # F3 still open in ❓


def test_assembled_evidence_passes_validator():
    base = json.loads((HERE / "testdata" / "v3-fixture-evidence-base.json").read_text())
    up = _update([{"id": "F1", "action": "resolve", "annotation": "fixed in e7e8e9"}])
    a_out, b_out, state, report = au.apply(AUTHOR, BRIEF, up, head_sha=SHA, actor="cam", auto=False)
    ev = au.assemble_evidence(base, a_out, b_out, state, up,
                              repo="pulumi/docs", pr=999, head_sha=SHA, run_id="t",
                              timestamp=report["timestamp"])
    assert au.validate_evidence_mod.validate_evidence(ev) == []


def test_malformed_update_json_is_exit_2_shape():
    up = {"schema": 2, "case": "nope", "findings": "not-a-list"}
    try:
        au.apply(AUTHOR, BRIEF, up, head_sha=SHA, actor="cam", auto=False)
    except au.UpdateError as exc:
        msg = str(exc)
        assert "schema" in msg and "case" in msg and "findings" in msg
    else:
        raise AssertionError("malformed update must be rejected")


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            print(f"  ok: {name}")
    print("test_apply_update: all passed")

#!/usr/bin/env python3
"""Tests for readthrough.py — the coherence lane's producer side, and the
contract that its `.readthrough-findings.json` is consumable by compose-review's
`_readthrough_synthetic_verdicts()` (the merged spine from PR #19756).

Self-contained: `python3 test_readthrough.py`. Imports the hyphenated scripts by
path (their entrypoints are guarded under __main__, so importing is side-effect
free). No network — exercises the dry-run and no-key paths only.
"""

from __future__ import annotations

import importlib.util
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[3]  # .claude/commands/docs-review/scripts -> repo root


def _load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


rt = _load("readthrough", "readthrough.py")
cr = _load("compose_review", "compose-review.py")

_fails: list[str] = []


def check(cond: bool, msg: str) -> None:
    print(("ok   " if cond else "FAIL ") + msg)
    if not cond:
        _fails.append(msg)


def _synthetic_patch(tmp: Path) -> Path:
    """A minimal whole-file `git diff --no-index` patch for a planted page."""
    page = tmp / "content" / "docs" / "x.md"
    page.parent.mkdir(parents=True, exist_ok=True)
    page.write_text(
        "---\ntitle: Configure Access\n---\n\n"
        "Run `pulumi up` to deploy the stack.\n\n"
        "## Background\n\nA stack is an isolated instance of your program.\n"
    )
    patch = tmp / ".synthetic.patch"
    proc = subprocess.run(
        ["git", "diff", "--no-index", "/dev/null", str(page)],
        capture_output=True, text=True,
    )
    # git diff --no-index exits 1 when files differ; that's expected.
    patch.write_text(proc.stdout)
    return patch


def main() -> int:
    # --- registry constants line up with the rubric + composer expectations ---
    check("local_repair" in rt.FIX_CLASSES and "reconception" in rt.FIX_CLASSES,
          "FIX_CLASSES = {local_repair, reconception}")
    check("prerequisite-inversion" in rt.FAILURE_MODES and len(rt.FAILURE_MODES) == 6,
          "FAILURE_MODES is the closed 6-item list")
    tool = rt.RECORD_FINDINGS_TOOL
    item = tool["input_schema"]["properties"]["findings"]["items"]
    check(set(item["required"]) == {"line_range", "anchor_quote", "failure_mode", "fix_class", "proposed_fix"},
          "tool requires the anchoring fields")
    check(item["properties"]["fix_class"]["enum"] == rt.FIX_CLASSES, "tool fix_class enum matches")
    check(item["properties"]["failure_mode"]["enum"] == rt.FAILURE_MODES, "tool failure_mode enum matches")

    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        patch = _synthetic_patch(tmp)
        out = tmp / "rt.json"

        # --- dry-run: ran=True, one schema-valid finding, file stamped ---
        rc = subprocess.run(
            [sys.executable, str(HERE / "readthrough.py"), "--dry-run",
             "--patch-file", str(patch), "--changed-files", "content/docs/x.md",
             "--out", str(out)],
            capture_output=True, text=True,
        ).returncode
        check(rc == 0, "dry-run exits 0")
        art = json.loads(out.read_text())
        check(art["ran"] is True, "dry-run ran=True")
        check(len(art["findings"]) == 1, "dry-run one finding")
        f0 = art["findings"][0]
        check(f0["file"] == "content/docs/x.md", "dry-run finding stamped with file")
        check(f0["fix_class"] in rt.FIX_CLASSES, "dry-run finding has a valid fix_class")

        # --- no ANTHROPIC_API_KEY: ran=False, exit 0, error recorded ---
        env = {k: v for k, v in os.environ.items() if k != "ANTHROPIC_API_KEY"}
        nokey = tmp / "rt-nokey.json"
        rc = subprocess.run(
            [sys.executable, str(HERE / "readthrough.py"),
             "--patch-file", str(patch), "--changed-files", "content/docs/x.md",
             "--repo-root", str(REPO_ROOT), "--out", str(nokey)],
            capture_output=True, text=True, env=env,
        ).returncode
        check(rc == 0, "no-key exits 0 (graceful)")
        nk = json.loads(nokey.read_text())
        check(nk["ran"] is False and nk["findings"] == [], "no-key ran=False, no findings")
        check(any("ANTHROPIC_API_KEY" in e for e in nk["errors"]), "no-key records the reason")

    # --- process_file drops findings missing required anchoring fields ---
    bad = {"line_range": "L1", "text": "no anchor_quote/failure_mode/fix_class here"}
    good = {"line_range": "L2", "anchor_quote": "x", "failure_mode": "missing-step",
            "fix_class": "local_repair", "proposed_fix": "y"}

    class _Resp:
        @staticmethod
        def call(*a, **k):
            return [bad, good], {}

    orig = rt.call_anthropic
    rt.call_anthropic = _Resp.call
    try:
        res = rt.process_file("key", REPO_ROOT, "", "content/docs/x.md", "m", "sys", False)
    finally:
        rt.call_anthropic = orig
    check(len(res["findings"]) == 1 and res["findings"][0]["line_range"] == "L2",
          "process_file drops the unanchored finding, keeps the valid one")

    # --- cross-module contract: a readthrough artifact feeds the composer ---
    art = {"ran": True, "findings": [
        {"file": "content/docs/x.md", "line_range": "L40-58",
         "anchor_quote": "Run `pulumi up`", "failure_mode": "missing-step",
         "fix_class": "local_repair", "severity_hint": "blocker",
         "proposed_fix": "add pulumi login", "rationale": "no backend"},
        {"file": "content/docs/x.md", "line_range": "L1-200",
         "anchor_quote": "## Background", "failure_mode": "purpose-mismatch",
         "fix_class": "reconception", "severity_hint": "recommended",
         "proposed_fix": "flag for split", "rationale": "two pages in one"},
    ]}
    sv = cr._readthrough_synthetic_verdicts(art)
    check(len(sv) == 2, "composer synthesizes two verdicts from the artifact")
    check(all(v["verdict"] == "flagged" and v["route"] == "preflight" for v in sv),
          "verdicts are flagged + preflight")
    check([v["type"] for v in sv] == ["readthrough-missing-step", "readthrough-purpose-mismatch"],
          "type carries the failure mode")
    check([v["fix_class"] for v in sv] == ["local_repair", "reconception"],
          "fix_class carried through to the composer")

    print(f"\n{len(_fails)} failure(s)")
    return 1 if _fails else 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Tests for triage-classify.py — the deterministic PR triage classifier.

Self-contained — run with `python3 test_triage_classify.py` (no pytest dep).
Shells out to the script the same way claude-triage.yml does (PR JSON on
argv[1], unified diff on stdin) and asserts on the JSON it emits.
"""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
CLASSIFY = HERE / "triage-classify.py"

_failures: list[str] = []
_passes = 0


def check(cond: bool, msg: str) -> None:
    global _passes
    if cond:
        _passes += 1
    else:
        _failures.append(msg)
        print(f"  FAIL: {msg}", file=sys.stderr)


def run_classify(pr_data: dict, diff: str = "") -> dict:
    with tempfile.TemporaryDirectory() as td:
        pf = Path(td) / "pr.json"
        pf.write_text(json.dumps(pr_data))
        r = subprocess.run([sys.executable, str(CLASSIFY), str(pf)],
                           input=diff, capture_output=True, text=True)
        assert r.returncode == 0, f"triage-classify.py exited {r.returncode}: {r.stderr}"
        return json.loads(r.stdout)


def _pr(additions: int, deletions: int, paths: list[str]) -> dict:
    return {
        "additions": additions,
        "deletions": deletions,
        "files": [{"path": p, "additions": additions // max(len(paths), 1), "deletions": 0}
                  for p in paths],
        "labels": [],
    }


def test_oversized_threshold() -> None:
    print("test_oversized_threshold")
    # A generated-corpus monster (the PR #20274 shape) is oversized.
    big = run_classify(_pr(99_664, 1_759, ["data/policy_pack_policies/cis.yaml",
                                           "content/docs/reference/x/_index.md",
                                           "scripts/gen-policy-docs.ts"]))
    check(big["oversized"] is True, f"99K-line PR classifies oversized; got {big['oversized']}")

    # Exactly at the threshold: not oversized (strict >).
    at = run_classify(_pr(10_000, 5_000, ["content/docs/a.md"]))
    check(at["oversized"] is False, f"15,000 changed lines is NOT oversized (strict >); got {at['oversized']}")

    # Just over: oversized. Deletions count toward the total.
    over = run_classify(_pr(1, 15_000, ["content/docs/a.md"]))
    check(over["oversized"] is True, f"15,001 changed lines (deletion-heavy) IS oversized; got {over['oversized']}")

    # A normal hand-written PR is nowhere near it.
    normal = run_classify(_pr(406, 1, ["content/blog/post/index.md"]))
    check(normal["oversized"] is False, "a 407-line PR is not oversized")
    check("oversized" in normal, "oversized field always present")


def main() -> int:
    tests = [test_oversized_threshold]
    for t in tests:
        try:
            t()
        except AssertionError as e:
            _failures.append(f"{t.__name__}: assertion error: {e}")
            print(f"  FAIL: {t.__name__}: {e}", file=sys.stderr)
        except Exception as e:  # noqa: BLE001
            _failures.append(f"{t.__name__}: {type(e).__name__}: {e}")
            print(f"  FAIL: {t.__name__}: {type(e).__name__}: {e}", file=sys.stderr)

    print(f"\n{_passes} check(s) passed, {len(_failures)} failed.")
    return 1 if _failures else 0


if __name__ == "__main__":
    sys.exit(main())

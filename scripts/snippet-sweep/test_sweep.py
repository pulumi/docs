#!/usr/bin/env python3
"""Integration tests for sweep.py.

Self-contained — run with `python3 test_sweep.py`. Builds a throwaway
content/docs tree with a fixture tiers file, shells out to sweep.py with
`--root`, and asserts on the signal JSON: tier filtering, draft skip,
suppression by content hash, pre-skip rules, and the schema contract the
selector's `--signal-file` loader will depend on.
"""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPT = HERE / "sweep.py"

_failures: list[str] = []
_passes = 0


def check(cond: bool, msg: str) -> None:
    global _passes
    if cond:
        _passes += 1
    else:
        _failures.append(msg)
        print(f"  FAIL: {msg}", file=sys.stderr)


BROKEN_PY = "---\ntitle: T\n---\n\n```python\nx = (1\n```\n"
CLEAN_TS = '---\ntitle: T\n---\n\n```typescript\nconst a = 1;\n```\n'
DRAFT_BROKEN = "---\ntitle: T\ndraft: true\n---\n\n```python\nx = (1\n```\n"
SHORTCODE = (
    "---\ntitle: T\n---\n\n```python\n"
    '{{< example-program-snippet path="x" >}}\n```\n'
)

TIERS = """\
tiers:
  - prefix: content/docs/generated/
    tier: 0
  - prefix: content/docs/concepts/
    tier: 1
  - prefix: content/docs/other/
    tier: 3
"""


def run(root: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(SCRIPT), "--root", str(root),
         "--tiers", str(root / "tiers.yaml"), *args],
        capture_output=True, text=True, cwd=root,
    )


with tempfile.TemporaryDirectory() as td:
    root = Path(td)
    (root / "tiers.yaml").write_text(TIERS)
    docs = root / "content/docs"
    for rel, body in {
        "concepts/broken.md": BROKEN_PY,
        "concepts/clean.md": CLEAN_TS,
        "concepts/draft.md": DRAFT_BROKEN,
        "concepts/shortcode.md": SHORTCODE,
        "generated/broken.md": BROKEN_PY,
        "other/broken.md": BROKEN_PY,
    }.items():
        p = docs / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(body)
    # sweep.py resolves the selector from the real repo, not --root, so no
    # scripts/ tree is needed in the fixture.

    print("== default scope (tier 1-2)")
    out = root / "signal.json"
    proc = run(root, "--out", str(out), "--ignore-file", str(root / "no-ignores.txt"))
    check(proc.returncode == 0, f"exit 0 with findings: {proc.stderr}")
    signal = json.loads(out.read_text())
    check(signal["schema_version"] == 1, "schema_version")
    check(signal["tier_scope"] == [1, 2], "tier_scope")
    check("content/docs/generated/broken.md" not in signal["pages"],
          "tier-0 page excluded")
    check("content/docs/other/broken.md" not in signal["pages"],
          "tier-3 page excluded by default")
    check("content/docs/concepts/draft.md" not in signal["pages"],
          "draft page excluded")
    check(list(signal["pages"]) == ["content/docs/concepts/broken.md"],
          f"exactly the broken tier-1 page flags: {list(signal['pages'])}")
    page = signal["pages"]["content/docs/concepts/broken.md"]
    sample = page["samples"][0]
    check(page["errors"] == 1, "error count")
    check(sample["lang"] == "python" and sample["check"] == "syntax",
          "sample lang/check")
    check(sample["line"] == 6, f"sample line is source-anchored: {sample['line']}")
    check(len(sample["hash"]) == 12, "sample carries suppression hash")
    check(signal["stats"]["blocks_skipped"] >= 1, "shortcode block counted as skipped")
    check("generated" in signal, "generated timestamp present")

    print("== --all-tiers")
    proc = run(root, "--out", str(out), "--all-tiers",
               "--ignore-file", str(root / "no-ignores.txt"))
    signal = json.loads(out.read_text())
    check("content/docs/other/broken.md" in signal["pages"],
          "tier-3 page included with --all-tiers")
    check("content/docs/generated/broken.md" not in signal["pages"],
          "tier-0 still excluded with --all-tiers")

    print("== suppression by content hash")
    h = sample["hash"]
    ignores = root / "ignores.txt"
    ignores.write_text(
        f"# test\ncontent/docs/concepts/broken.md\t{h}   # fixture\n"
    )
    proc = run(root, "--out", str(out), "--ignore-file", str(ignores))
    signal = json.loads(out.read_text())
    check(signal["pages"] == {}, "hash suppression removes the finding")
    check(signal["stats"]["suppressed"] == 1, "suppressed counted")

    print("== suppression expires on edit")
    (docs / "concepts/broken.md").write_text(
        "---\ntitle: T\n---\n\n```python\nx = (1  # edited\n```\n"
    )
    proc = run(root, "--out", str(out), "--ignore-file", str(ignores))
    signal = json.loads(out.read_text())
    check("content/docs/concepts/broken.md" in signal["pages"],
          "edited block re-exposed")

    print("== path-regex suppression + --explain-ignores")
    ignores.write_text("content/docs/concepts/.*   # whole subtree\n"
                       f"content/docs/concepts/broken.md\t{h}   # now dead\n")
    proc = run(root, "--out", str(out), "--ignore-file", str(ignores))
    signal = json.loads(out.read_text())
    check(signal["pages"] == {}, "regex suppression")
    proc = run(root, "--explain-ignores", "--ignore-file", str(ignores))
    check("broken.md" in proc.stdout and h in proc.stdout,
          f"--explain-ignores lists the dead hash entry: {proc.stdout!r}")

    print("== --paths subset")
    proc = run(root, "--out", str(out), "--paths",
               "content/docs/concepts/clean.md",
               "--ignore-file", str(root / "no-ignores.txt"))
    signal = json.loads(out.read_text())
    check(signal["pages"] == {} and signal["stats"]["pages_scanned"] == 1,
          "subset run scans only the named page")

    print("== infra error exits non-zero")
    proc = subprocess.run(
        [sys.executable, str(SCRIPT), "--root", str(root),
         "--tiers", str(root / "missing.yaml")],
        capture_output=True, text=True,
    )
    check(proc.returncode == 2, "unreadable tiers file -> exit 2")

if _failures:
    print(f"\n{len(_failures)} failure(s), {_passes} passed", file=sys.stderr)
    sys.exit(1)
print(f"\nall {_passes} checks passed")

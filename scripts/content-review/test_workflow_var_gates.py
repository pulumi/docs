#!/usr/bin/env python3
"""Guard against the null-coercion kill-switch bug in workflow expressions.

An unset repo variable is null, and GitHub coerces a null-vs-string
comparison to numbers (null -> 0, '0' -> 0). So a bare
`vars.X != '0'` is FALSE when X is unset: a kill switch meant to default ON
silently defaults OFF. The fix the repo uses everywhere is
`format('{0}', vars.X) != '0'`. A fork smoke run of the glow-up pre-verify
gates (pulumi/docs#21949) caught every round being skipped this way.

This scans every workflow's non-comment lines for a bare `vars.X != '0'` or
`vars.X == '0'` and fails on any hit. Run directly: exits non-zero on failure.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BARE = re.compile(r"\bvars\.[A-Za-z_][A-Za-z0-9_]*\s*(?:!=|==)\s*'0'")
WRAPPED = re.compile(r"format\('\{0\}',\s*vars\.[A-Za-z_][A-Za-z0-9_]*\)\s*(?:!=|==)\s*'0'")

failures: list[str] = []


def check(name: str, cond: bool) -> None:
    print(("ok: " if cond else "FAIL: ") + name)
    if not cond:
        failures.append(name)


def bare_hits(text: str) -> list[tuple[int, str]]:
    hits = []
    for n, line in enumerate(text.splitlines(), 1):
        if line.lstrip().startswith("#"):
            continue
        if BARE.search(WRAPPED.sub("", line)):
            hits.append((n, line.strip()))
    return hits


# The detector itself.
check("detects a bare != '0'", bool(bare_hits("    if: vars.FOO != '0'")))
check("detects a bare == '0'", bool(bare_hits("    if: a && vars.FOO == '0'")))
check("accepts the format() wrapper",
      not bare_hits("    if: format('{0}', vars.FOO) != '0'"))
check("ignores comments", not bare_hits("  # a bare `vars.FOO != '0'` is wrong"))
check("ignores comparisons against other literals", not bare_hits("    if: vars.FOO == '1'"))

wf_dir = ROOT / ".github" / "workflows"
found = sorted(wf_dir.glob("*.yml")) + sorted(wf_dir.glob("*.yaml"))
check("found workflows to scan", bool(found))
for wf in found:
    hits = bare_hits(wf.read_text())
    check(f"{wf.name}: no bare vars.X ==/!= '0' "
          + ("; ".join(f"L{n}: {t}" for n, t in hits) if hits else ""), not hits)

if failures:
    print(f"\n{len(failures)} failure(s)", file=sys.stderr)
    sys.exit(1)
print("\nall workflow var-gate checks passed")

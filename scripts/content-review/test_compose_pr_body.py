#!/usr/bin/env python3
"""Tests for compose-pr-body.py (assemble-then-judge PR-body draft)."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    "compose_pr_body", Path(__file__).resolve().parent / "compose-pr-body.py"
)
c = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(c)

failures: list[str] = []


def check(name: str, cond: bool) -> None:
    if cond:
        print(f"ok: {name}")
    else:
        failures.append(name)
        print(f"FAIL: {name}", file=sys.stderr)


QUEUE = {
    "traffic": {"available": True, "period": "2026-06", "source": "CLICKSTREAM.FCT_PAGEVIEWS"},
    "articles": [{
        "path": "content/docs/iac/concepts/functions/resource-methods.md",
        "url": "/docs/iac/concepts/functions/resource-methods/",
        "lane": "priority", "tier": 1, "no_retire": True,
        "monthly_visits": 384, "last_reviewed": None, "attempts": 0, "score": 278.3,
    }],
}

# A contradicted high-confidence claim (-> fix), an unverifiable claim (-> defer).
VERIFIED = {
    "verdicts": [
        {"claim_id": "c3", "line_range": "L34", "text": "C# signature GetKubeconfig(Cluster.GetKubeconfigArgs? args)",
         "verdict": "contradicted", "confidence": "high",
         "evidence": "dotnet SDK defines flat ClusterGetKubeconfigArgs", "source": "pulumi/pulumi-eks: sdk/dotnet/Cluster.cs"},
        {"claim_id": "c5", "line_range": "L52", "text": "Python signature includes profile_name",
         "verdict": "unverifiable", "confidence": "low",
         "evidence": "verifier did not converge", "source": "(no source pointer)"},
        {"claim_id": "c2", "text": "TS signature", "verdict": "verified", "confidence": "high",
         "evidence": "matches", "source": "sdk/nodejs/cluster.ts"},
    ],
}
# One mechanical Vale (difficulty qualifier -> fix), one style (passive -> defer).
VALE = [
    {"file": "x.md", "line": 67, "rule": "Pulumi.Difficulty", "category": "difficulty qualifier",
     "severity": "warning", "message": "'Simple' judges difficulty for the reader"},
    {"file": "x.md", "line": 12, "rule": "Google.Passive", "category": "passive voice",
     "severity": "suggestion", "message": "consider active voice"},
]
# One local_repair (-> fix), one reconception (-> defer).
READTHROUGH = {
    "ran": True,
    "findings": [
        {"line_range": "L40", "failure_mode": "missing-step", "anchor_quote": "run pulumi up",
         "fix_class": "local_repair", "proposed_fix": "add a login step before L40"},
        {"line_range": "L1-90", "failure_mode": "purpose-mismatch", "anchor_quote": "Configure access",
         "fix_class": "reconception", "proposed_fix": "split architecture half into its own page"},
    ],
}
FRONTMATTER = {"files": [{"path": "x.md",
    "alias_collisions": [{"alias": "/docs/dupe/"}],
    "menu_parents": [{"menu_name": "concepts", "parent": "functions", "parent_exists_in_menu": False}]}]}

out = c.compose(QUEUE, VERIFIED, VALE, READTHROUGH, FRONTMATTER)

# All six required sections present (record-review's check_pr_body expects these).
for sec in ["Why this page", "Fixes applied", "Findings not applied",
            "Screenshot check", "Rendered content", "Verification"]:
    check(f"section present: {sec}", f"## {sec}" in out)

# Provenance composed (real visits, not narrated).
check("provenance shows real visits", "384 monthly visits" in out)

# High-confidence findings land as fix stubs.
check("contradicted high-confidence claim -> fix row", "c3" in out.split("## Findings not applied")[0])
check("mechanical Vale -> fix row", "difficulty qualifier" in out.split("## Findings not applied")[0])
check("local_repair readthrough -> fix row", "missing-step" in out.split("## Findings not applied")[0])
check("alias collision -> fix row", "alias collision" in out.split("## Findings not applied")[0])

# Judgment-level findings land as deferral stubs.
deferral_block = out.split("## Findings not applied")[1].split("## Screenshot")[0]
check("unverifiable claim -> deferral", "c5" in deferral_block)
check("style Vale -> deferral", "passive voice" in deferral_block)
check("reconception readthrough -> deferral", "purpose-mismatch" in deferral_block)
check("legacy menu parent -> deferral", "menu parent" in deferral_block)

# TODO markers for the model to fill; lint placeholder for the gate to stamp.
check("fix rows carry <TODO>", "<TODO: correction" in out)
check("deferrals carry <TODO>", "<TODO: why judgment-level>" in deferral_block)
check("screenshot/rendered are <TODO>", out.count("<TODO") >= 4)
check("lint result is a stamped placeholder", c.LINT_PLACEHOLDER in out)
# The "do not edit" hint must live in an HTML comment, not leak to readers, and
# the label is `make lint` only (build isn't stamped here).
check("no reader-facing 'do not edit' instruction", "do not edit this line" not in out)
lint_line = next(l for l in out.splitlines() if c.LINT_PLACEHOLDER in l)
check("lint hint rides in an HTML comment", "<!--" in lint_line.split(c.LINT_PLACEHOLDER, 1)[1])
check("lint label is make-lint-only (no make build)", "make build`:" not in lint_line)

# Verification inventory is deterministic.
check("inventory counts verdicts", "3 verdict(s); 1 contradicted/mismatch, 1 unverifiable" in out)

# Graceful degradation: all artifacts missing still yields a valid full draft.
bare = c.compose(QUEUE, None, None, None, None)
for sec in ["Why this page", "Fixes applied", "Findings not applied",
            "Screenshot check", "Rendered content", "Verification"]:
    check(f"degraded draft still has {sec}", f"## {sec}" in bare)
check("degraded fixes section notes no stubs", "No high-confidence fix candidates" in bare)
check("degraded inventory marks missing", ".verified-claims.json`: missing" in bare)

# Errored artifact is surfaced in Verification.
errd = c.compose(QUEUE, {"verdicts": [], "errors": ["verify-claims failed"]}, [], {"ran": False, "findings": []}, {})
check("errored artifact surfaced", "Artifacts that failed" in errd and "verified-claims" in errd)

if failures:
    print(f"\n{len(failures)} failure(s)", file=sys.stderr)
    sys.exit(1)
print("\nall compose-pr-body tests passed")

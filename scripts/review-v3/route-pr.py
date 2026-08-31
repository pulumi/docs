#!/usr/bin/env python3
"""Glue for the triage routing step: PR data + diff → required reviewer teams.

Runs inside claude-triage.yml after classification, and only there — the
Sentinel does its own resolution from live API state. This script exists so
the workflow doesn't inline a fragile python heredoc: it wires the mechanical
bar and claims signal (triage-classify.py) into the lane matrix
(routing.py) and prints one JSON object the workflow can consume with jq:

    {
      "mechanical": bool, "mechanical_reasons": [...],
      "claims": bool,
      "roles": [...], "teams": [...],          # teams = org/slug to request
      "staging_evidence_required": bool,
      "reasons": [...]
    }

Deterministic, no network. Inputs are the files the triage step already has
on disk: the `gh pr view --json ...` payload and the (possibly truncated)
unified diff.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_REPO_ROOT = _HERE.parent.parent


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def route(pr_data: dict, diff_text: str, config_path: Path, repo_root: Path) -> dict:
    tc = _load("route_pr_triage_classify",
               repo_root / ".claude/commands/docs-review/scripts/triage-classify.py")
    routing = _load("route_pr_routing", _HERE / "routing.py")

    file_flags = [tc.classify_file(path, file_diff)
                  for path, file_diff in tc.split_files(diff_text)]
    mechanical, mech_reasons = tc.classify_mechanical(pr_data, file_flags, diff_text, repo_root)
    claims = bool(tc.claims_signal_reasons(pr_data.get("files") or [], diff_text))

    config = routing.load_config(config_path)
    paths = [f.get("path", "") for f in pr_data.get("files") or []]
    resolution = routing.resolve_lanes(paths, mechanical, claims, config)

    roles = sorted(resolution.roles)
    return {
        "mechanical": mechanical,
        "mechanical_reasons": mech_reasons,
        "claims": claims,
        "roles": roles,
        "teams": [config.teams[r] for r in roles],
        "staging_evidence_required": resolution.staging_evidence_required,
        "reasons": resolution.reasons,
    }


def _self_test() -> int:
    docs_diff = (
        "diff --git a/content/docs/foo.md b/content/docs/foo.md\n"
        "--- a/content/docs/foo.md\n"
        "+++ b/content/docs/foo.md\n"
        "@@ -40,1 +40,1 @@\n"
        "-teh stack\n"
        "+the stack\n"
    )
    pr = {"additions": 1, "deletions": 1, "files": [{"path": "content/docs/foo.md"}]}
    out = route(pr, docs_diff, _REPO_ROOT / ".github/review-routing.yml", _REPO_ROOT)
    assert out["mechanical"] is True, out
    assert out["roles"] == [] and out["teams"] == [], "mechanical docs PR needs no human"
    assert out["staging_evidence_required"] is False

    infra_pr = {"additions": 3, "deletions": 0, "files": [{"path": "layouts/partials/foo.html"}]}
    infra_diff = (
        "diff --git a/layouts/partials/foo.html b/layouts/partials/foo.html\n"
        "--- a/layouts/partials/foo.html\n"
        "+++ b/layouts/partials/foo.html\n"
        "@@ -1,0 +1,1 @@\n"
        "+<div></div>\n"
    )
    out2 = route(infra_pr, infra_diff, _REPO_ROOT / ".github/review-routing.yml", _REPO_ROOT)
    assert out2["mechanical"] is False
    assert "tools" in out2["roles"] and out2["staging_evidence_required"] is True

    pricing_pr = {"additions": 1, "deletions": 0, "files": [{"path": "data/pulumi_pricing.yaml"}]}
    pricing_diff = (
        "diff --git a/data/pulumi_pricing.yaml b/data/pulumi_pricing.yaml\n"
        "--- a/data/pulumi_pricing.yaml\n"
        "+++ b/data/pulumi_pricing.yaml\n"
        "@@ -1,0 +1,1 @@\n"
        "+price: 50\n"
    )
    out3 = route(pricing_pr, pricing_diff, _REPO_ROOT / ".github/review-routing.yml", _REPO_ROOT)
    assert out3["claims"] is True
    assert "marketing" in out3["roles"], "claims overlay stacks the marketing lane"

    print("route-pr self-test passed")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--pr-data", help="path to the gh pr view --json payload")
    parser.add_argument("--diff", help="path to the unified diff")
    parser.add_argument("--config", default=str(_REPO_ROOT / ".github/review-routing.yml"))
    parser.add_argument("--repo-root", default=str(_REPO_ROOT))
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        return _self_test()
    if not args.pr_data or not args.diff:
        parser.error("--pr-data and --diff are required")
    pr_data = json.loads(Path(args.pr_data).read_text())
    diff_text = Path(args.diff).read_text()
    out = route(pr_data, diff_text, Path(args.config), Path(args.repo_root))
    print(json.dumps(out, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

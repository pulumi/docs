#!/usr/bin/env python3
"""cross-sibling-discover.py — pre-step for cross-sibling discovery.

Architectural mirror of `editorial-balance-detect.py` and `extract-urls-and-fetch.py`:
a workflow pre-step that pre-computes cross-sibling discovery deterministically
so the model uses a structurally-guaranteed sibling list instead of computing
"is this in a templated section?" inline (where the decision is skippable).

S38 motivation: pr18568 r1+r2 both classified the changed file as "not in a
templated section" because the changed file's directory (`content/docs/iac/
clouds/azure/guides/`) had zero peers. The model didn't broaden the search to
the parallel `content/docs/iac/guides/clouds/` tree where the actual canonical
sibling lives. Result: structural-bug triplet (file-location, alias collision,
menu-parent) silently dropped.

Ship F (S38) added a "zero-peer check" inline rule. This pre-step encodes the
same logic deterministically — the artifact is the structural guarantee that
discovery runs.

Usage:
    cross-sibling-discover.py --pr <PR_NUMBER> --out <out.json>

Output schema (JSON, one entry per changed `*.md` under `content/docs/`):

    {
      "files": [
        {
          "file": "content/docs/iac/clouds/azure/guides/_index.md",
          "in_templated_section": false,
          "directory_peers": [],
          "parallel_path_check": {
            "checked_patterns": [...],
            "found": [...],
            "structural_warning": "file at non-canonical path; ..."
          },
          "siblings_for_dispatch": [...]
        },
        ...
      ]
    }

Empty input (no PR-changed `content/docs/**/*.md`) produces `{"files": []}`.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

# Templated-section threshold (mirrors `references/fact-check.md` §Cross-sibling
# consistency: "directory with ≥3 parallel pages on the same subject").
TEMPLATED_PEER_THRESHOLD = 3

# Parallel-path patterns. Each entry: when a changed file matches `from_glob`
# but has zero/few peers in its own directory, check `to_glob` and any
# `to_alt_files` for the canonical templated set.
#
# {x} is the variable segment captured from the matching path.
PARALLEL_PATTERNS = [
    {
        "name": "iac-clouds-layout-swap",
        "from_pattern": r"^content/docs/iac/clouds/(?P<x>[^/]+)/guides/.*\.md$",
        "to_dir": "content/docs/iac/guides/clouds/{x}/",
        "to_alt_files": ["content/docs/iac/guides/clouds/{x}.md"],
        "warning_template": (
            "file at non-canonical path; existing canonical guide(s) at {found_paths} "
            "(PR-base content tree). The pulumi/docs convention places per-cloud guides "
            "under `content/docs/iac/guides/clouds/<cloud>/` (or as a single `<cloud>.md` "
            "file), not under `content/docs/iac/clouds/<cloud>/guides/`."
        ),
    },
]


def get_changed_files(pr: str | None) -> list[str]:
    """Return list of changed `*.md` paths under `content/docs/` from the PR."""
    if not pr:
        return []
    try:
        result = subprocess.run(
            ["gh", "pr", "diff", pr, "--name-only"],
            capture_output=True, text=True, check=True, timeout=30,
        )
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
        return []
    return [
        line.strip() for line in result.stdout.splitlines()
        if line.strip().startswith("content/docs/") and line.strip().endswith(".md")
    ]


def list_directory_peers(repo_root: Path, dir_path: str, exclude: str) -> list[str]:
    """List `*.md` files in `dir_path` under `repo_root`, excluding `exclude` and `_index.md`.

    Returns relative paths (e.g., `auth0.md`, not full paths). Result is sorted.
    """
    full_dir = repo_root / dir_path
    if not full_dir.is_dir():
        return []
    out = []
    for child in sorted(full_dir.iterdir()):
        if child.name == "_index.md":
            continue
        if not child.name.endswith(".md"):
            continue
        rel = (Path(dir_path) / child.name).as_posix()
        if rel == exclude:
            continue
        out.append(child.name)
    return out


def list_directory_files(repo_root: Path, dir_path: str) -> list[str]:
    """List `*.md` filenames under `dir_path` (no exclusions, includes `_index.md`)."""
    full_dir = repo_root / dir_path
    if not full_dir.is_dir():
        return []
    return sorted([
        c.name for c in full_dir.iterdir()
        if c.is_file() and c.name.endswith(".md")
    ])


def check_parallel_paths(repo_root: Path, file_path: str) -> dict | None:
    """Check whether the changed file has parallel-path canonical siblings.

    Returns a dict with `checked_patterns`, `found`, and (optionally) a
    `structural_warning` if a parallel canonical set was located. Returns
    None when no patterns match the changed file.
    """
    checked = []
    found = []
    for pattern in PARALLEL_PATTERNS:
        m = re.match(pattern["from_pattern"], file_path)
        if not m:
            continue
        x = m.group("x")
        to_dir = pattern["to_dir"].format(x=x)
        alt_files = [f.format(x=x) for f in pattern.get("to_alt_files", [])]
        checked.append({
            "name": pattern["name"],
            "x": x,
            "to_dir": to_dir,
            "to_alt_files": alt_files,
        })
        # Check the parallel directory.
        dir_files = list_directory_files(repo_root, to_dir)
        if dir_files:
            found.append({
                "path": to_dir,
                "type": "templated_directory",
                "files": dir_files,
            })
        # Check the alternate-file form (e.g., `azure.md` instead of `azure/`).
        for alt in alt_files:
            if (repo_root / alt).is_file():
                found.append({
                    "path": alt,
                    "type": "canonical_file",
                })
    if not checked:
        return None
    result = {"checked_patterns": checked, "found": found}
    if found:
        # Apply the warning template from the FIRST matched pattern that produced findings.
        for pattern in PARALLEL_PATTERNS:
            if re.match(pattern["from_pattern"], file_path):
                result["structural_warning"] = pattern["warning_template"].format(
                    found_paths=", ".join(f["path"] for f in found)
                )
                break
    return result


def discover_for_file(repo_root: Path, file_path: str) -> dict:
    """Compute the cross-sibling discovery record for a single changed file."""
    file_dir = str(Path(file_path).parent) + "/"
    peers_in_dir = list_directory_peers(repo_root, file_dir, exclude=file_path)
    in_templated = len(peers_in_dir) >= (TEMPLATED_PEER_THRESHOLD - 1)
    record = {
        "file": file_path,
        "in_templated_section": in_templated,
        "directory_peers": peers_in_dir,
        "parallel_path_check": None,
        "siblings_for_dispatch": [],
    }
    # Always run the parallel-path check (Ship F: don't trust the local-dir signal alone).
    parallel = check_parallel_paths(repo_root, file_path)
    if parallel is not None:
        record["parallel_path_check"] = parallel
    # Build the dispatch list: in-dir peers (if templated) ∪ parallel-found paths.
    dispatch = []
    if in_templated:
        for peer in peers_in_dir:
            dispatch.append(str(Path(file_dir) / peer))
    if parallel and parallel.get("found"):
        for entry in parallel["found"]:
            if entry["type"] == "canonical_file":
                dispatch.append(entry["path"])
            elif entry["type"] == "templated_directory":
                for fname in entry["files"]:
                    dispatch.append(entry["path"] + fname)
    # De-dupe while preserving order.
    seen = set()
    unique_dispatch = []
    for d in dispatch:
        if d not in seen:
            seen.add(d)
            unique_dispatch.append(d)
    record["siblings_for_dispatch"] = unique_dispatch
    return record


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--pr", help="PR number (for `gh pr diff`)")
    p.add_argument("--changed-files", help="Comma-separated list of changed files (overrides --pr; for testing)")
    p.add_argument("--repo-root", default=".", help="Repo root (default: cwd)")
    p.add_argument("--out", required=True, help="Output JSON path")
    args = p.parse_args()

    repo_root = Path(args.repo_root).resolve()
    if args.changed_files:
        changed = [f.strip() for f in args.changed_files.split(",") if f.strip()]
    else:
        changed = get_changed_files(args.pr)

    files = [discover_for_file(repo_root, f) for f in changed]
    out = {"files": files}

    Path(args.out).write_text(json.dumps(out, indent=2) + "\n")
    print(f"cross-sibling-discover: {len(files)} file(s) processed → {args.out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())

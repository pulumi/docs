#!/usr/bin/env python3
"""cross-sibling-discover.py — pre-step for cross-sibling discovery.

Architectural mirror of `editorial-balance-detect.py`, `extract-urls-and-fetch.py`,
and `frontmatter-validate.py`: a workflow pre-step that pre-computes the
"is this file in a templated section?" decision deterministically, so the
model uses a structurally-guaranteed sibling list instead of computing the
classification inline (where the decision is skippable under attention pressure).

Scope: just the local-directory peer-counting check. The parallel-path /
wrong-layout detection that originally lived here as the hardcoded
`PARALLEL_PATTERNS` table is removed — its responsibility moved to
`frontmatter-validate.py`'s URL-ownership check, which uses Hugo aliases +
S3 redirects (data the codebase already curates) instead of hardcoded layout
patterns. See `references/pre-computation.md` and `references/fact-check.md`
§Cross-sibling consistency for the unified model.

History: an earlier version bundled the parallel-path check here using a
hardcoded `PARALLEL_PATTERNS` table. The table caught the pr18568 case but
was brittle — it only handled the one observed layout swap. A later refactor
(S38) replaced the hardcoded approach with a data-driven URL-ownership lookup
in frontmatter-validate; this script now does only what its name says.

Usage:
    cross-sibling-discover.py --pr <PR_NUMBER> --out <out.json>

Output schema (JSON, one entry per changed `*.md` under `content/docs/`):

    {
      "files": [
        {
          "file": "content/docs/administration/access-identity/saml/jumpcloud.md",
          "in_templated_section": true,
          "directory_peers": ["auth0.md", "entra.md", "gsuite.md", ...],
          "siblings_for_dispatch": [
            "content/docs/administration/access-identity/saml/auth0.md",
            ...
          ]
        }
      ]
    }

Empty input (no PR-changed `content/docs/**/*.md`) produces `{"files": []}`.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

# Templated-section threshold (mirrors `references/fact-check.md` §Cross-sibling
# consistency: "directory with ≥3 parallel pages on the same subject").
TEMPLATED_PEER_THRESHOLD = 3


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

    Returns filenames (e.g., `auth0.md`, not full paths). Result is sorted.
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


def discover_for_file(repo_root: Path, file_path: str) -> dict:
    """Compute the cross-sibling discovery record for a single changed file."""
    file_dir = str(Path(file_path).parent) + "/"
    peers_in_dir = list_directory_peers(repo_root, file_dir, exclude=file_path)
    in_templated = len(peers_in_dir) >= (TEMPLATED_PEER_THRESHOLD - 1)
    dispatch = []
    if in_templated:
        for peer in peers_in_dir:
            dispatch.append(str(Path(file_dir) / peer))
    return {
        "file": file_path,
        "in_templated_section": in_templated,
        "directory_peers": peers_in_dir,
        "siblings_for_dispatch": dispatch,
    }


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

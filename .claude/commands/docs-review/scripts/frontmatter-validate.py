#!/usr/bin/env python3
"""frontmatter-validate.py — pre-step for frontmatter validation (Bundle 1).

Architectural mirror of `cross-sibling-discover.py`, `editorial-balance-detect.py`,
and `extract-urls-and-fetch.py`: a workflow pre-step that pre-computes deterministic
frontmatter checks so the model receives a structurally-guaranteed result instead
of computing them inline (where they get skipped under attention pressure).

S38 motivation: Ship G's cross-sibling pre-step caught the file-location and alias
collision findings on pr18568, but missed the L11 menu-parent finding. The
menu-parent identifier check is fully deterministic: parse the changed file's
frontmatter, walk content/**/*.md to build a global menu-identifier map, check
that each declared parent exists in the same named menu. Same atomization pattern,
different layer.

Two checks bundled (both walk frontmatter, single tree walk):

1. **Menu-parent validation.** For each `menu.<name>.parent: <X>` in a changed
   file's frontmatter, verify `(name, X)` exists somewhere in the global
   identifier map. The S37/S38 pr18568 case: `menu.iac.parent: azure-clouds`
   resolves only against `menu.integrations.identifier: azure-clouds` —
   wrong-named-menu.

2. **Alias collision detection.** Two sub-checks:
   - PR-internal: any alias appearing in 2+ PR-changed files.
   - Repo-wide: any alias on a PR-changed file that already exists as an alias
     on a different (non-PR-changed) canonical file.

Usage:
    frontmatter-validate.py --pr <PR_NUMBER> --out <out.json>

Output schema (JSON):

    {
      "files": [
        {
          "file": "content/docs/iac/clouds/azure/guides/_index.md",
          "frontmatter_parse_ok": true,
          "menu_parents": [
            {
              "menu_name": "iac",
              "parent_identifier": "azure-clouds",
              "parent_exists_in_menu": false,
              "found_in_other_menus": ["integrations"]
            }
          ],
          "aliases_declared": ["/docs/iac/clouds/azure/"],
          "alias_collisions": [
            {
              "alias": "/docs/iac/clouds/azure/guides/",
              "collides_with": "content/docs/iac/guides/clouds/azure.md",
              "scope": "repo-wide"
            }
          ]
        }
      ],
      "global_identifier_map_size": 0,
      "global_alias_map_size": 0
    }

Empty input (no PR-changed `content/**/*.md`) produces a valid empty artifact.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

# Frontmatter delimiters for the YAML block at the top of a Hugo content file.
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def get_changed_files(pr: str | None) -> list[str]:
    """Return list of changed `*.md` paths under `content/` from the PR."""
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
        if line.strip().startswith("content/") and line.strip().endswith(".md")
    ]


def read_frontmatter(path: Path) -> dict | None:
    """Read and parse the YAML frontmatter block of a Hugo content file.

    Returns None if the file doesn't have a parseable frontmatter block.
    Uses a minimal manual parser to avoid pulling in PyYAML — the frontmatter
    schema we care about (menu.<name>.{parent,identifier} + aliases list) is
    simple enough to parse line-by-line.
    """
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except (OSError, UnicodeError):
        return None
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    block = m.group(1)
    return parse_minimal_yaml(block)


def parse_minimal_yaml(block: str) -> dict:
    """Manually parse the limited YAML shape we care about.

    Handles:
    - Top-level scalars (`title: foo`)
    - Top-level lists (`aliases:\\n  - /a/\\n  - /b/`)
    - Two-level nested maps (`menu:\\n  iac:\\n    parent: foo`)
    - Three-level nested maps not needed for our checks.

    Returns a dict. Values are strings, lists of strings, or dicts.
    Doesn't attempt to handle anchors, multi-line scalars, or quoted edge cases.
    """
    out: dict = {}
    lines = block.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.lstrip().startswith("#"):
            i += 1
            continue
        # Top-level: no leading whitespace.
        if not line.startswith((" ", "\t")):
            if ":" not in line:
                i += 1
                continue
            key, _, rest = line.partition(":")
            key = key.strip()
            rest = rest.strip()
            if rest == "" or rest == "|" or rest == ">":
                # Could be a nested map or a list. Look ahead.
                # Accept indented lines AND column-0 list items (`- foo`) as
                # children — Hugo frontmatter often writes top-level lists
                # without indentation.
                j = i + 1
                child_lines = []
                while j < len(lines):
                    nxt = lines[j]
                    if not nxt.strip():
                        child_lines.append(nxt)
                        j += 1
                        continue
                    if nxt.startswith((" ", "\t")) or nxt.lstrip().startswith("- "):
                        child_lines.append(nxt)
                        j += 1
                        continue
                    break
                # Decide list vs map.
                first_nonblank = next((cl for cl in child_lines if cl.strip()), "")
                if first_nonblank.lstrip().startswith("- "):
                    out[key] = [
                        cl.lstrip()[2:].strip().strip('"').strip("'")
                        for cl in child_lines
                        if cl.lstrip().startswith("- ")
                    ]
                else:
                    out[key] = parse_minimal_yaml("\n".join(
                        # Strip the common leading indentation.
                        cl[_min_indent(child_lines):] if cl.strip() else cl
                        for cl in child_lines
                    ))
                i = j
                continue
            # Scalar value on the same line.
            out[key] = rest.strip().strip('"').strip("'")
            i += 1
            continue
        # Indented line at top of loop = stray; skip.
        i += 1
    return out


def _min_indent(lines: list[str]) -> int:
    """Return the minimum leading-space count across non-blank lines, or 0."""
    indents = []
    for line in lines:
        if not line.strip():
            continue
        stripped = line.lstrip(" ")
        indents.append(len(line) - len(stripped))
    return min(indents) if indents else 0


def extract_menu_parents(fm: dict) -> list[tuple[str, str]]:
    """Return list of (menu_name, parent_identifier) tuples from `menu.<name>.parent`."""
    menu = fm.get("menu")
    if not isinstance(menu, dict):
        return []
    out = []
    for menu_name, sub in menu.items():
        if isinstance(sub, dict) and isinstance(sub.get("parent"), str):
            out.append((menu_name, sub["parent"]))
    return out


def extract_menu_identifiers(fm: dict) -> list[tuple[str, str]]:
    """Return list of (menu_name, identifier) tuples from `menu.<name>.identifier`."""
    menu = fm.get("menu")
    if not isinstance(menu, dict):
        return []
    out = []
    for menu_name, sub in menu.items():
        if isinstance(sub, dict) and isinstance(sub.get("identifier"), str):
            out.append((menu_name, sub["identifier"]))
    return out


def extract_aliases(fm: dict) -> list[str]:
    """Return list of alias paths from `aliases:` frontmatter field."""
    aliases = fm.get("aliases", [])
    if isinstance(aliases, list):
        return [a for a in aliases if isinstance(a, str)]
    if isinstance(aliases, str):
        return [aliases]
    return []


def build_global_maps(repo_root: Path) -> tuple[dict, dict]:
    """Walk content/**/*.md and build:

    - identifier_map: {(menu_name, identifier): [file, ...]}
    - alias_map: {alias: [file, ...]}

    Files indexed by repo-relative path. Multiple files with the same identifier
    or alias are recorded (collision detection happens at check time).
    """
    identifier_map: dict[tuple[str, str], list[str]] = {}
    alias_map: dict[str, list[str]] = {}
    content_root = repo_root / "content"
    if not content_root.is_dir():
        return identifier_map, alias_map
    for md_path in content_root.rglob("*.md"):
        rel = md_path.relative_to(repo_root).as_posix()
        fm = read_frontmatter(md_path)
        if fm is None:
            continue
        for name, ident in extract_menu_identifiers(fm):
            identifier_map.setdefault((name, ident), []).append(rel)
        for alias in extract_aliases(fm):
            alias_map.setdefault(alias, []).append(rel)
    return identifier_map, alias_map


def check_menu_parents(
    file_rel: str,
    fm: dict,
    identifier_map: dict[tuple[str, str], list[str]],
) -> list[dict]:
    """Validate each menu.<name>.parent against the global identifier map."""
    out = []
    for menu_name, parent_ident in extract_menu_parents(fm):
        # Does (menu_name, parent_ident) exist anywhere?
        same_menu_files = identifier_map.get((menu_name, parent_ident), [])
        # Strip the file itself from the same-menu list (a file can declare its
        # own identifier and use it as a parent — unusual but valid).
        same_menu_files = [f for f in same_menu_files if f != file_rel]
        # Find this identifier in OTHER menus (the diagnostic case from S37/S38).
        found_in_other_menus = [
            other_name
            for (other_name, ident), files in identifier_map.items()
            if ident == parent_ident and other_name != menu_name
        ]
        out.append({
            "menu_name": menu_name,
            "parent_identifier": parent_ident,
            "parent_exists_in_menu": bool(same_menu_files),
            "found_in_other_menus": sorted(set(found_in_other_menus)),
        })
    return out


def check_alias_collisions(
    file_rel: str,
    aliases: list[str],
    alias_map: dict[str, list[str]],
    pr_files: set[str],
) -> list[dict]:
    """Detect alias collisions: PR-internal (across changed files) and repo-wide."""
    out = []
    for alias in aliases:
        # All files claiming this alias except `file_rel` itself.
        claimants = [f for f in alias_map.get(alias, []) if f != file_rel]
        if not claimants:
            continue
        for other in claimants:
            scope = "pr-internal" if other in pr_files else "repo-wide"
            out.append({
                "alias": alias,
                "collides_with": other,
                "scope": scope,
            })
    return out


def discover_for_file(
    repo_root: Path,
    file_rel: str,
    identifier_map: dict,
    alias_map: dict,
    pr_files: set[str],
) -> dict:
    """Compute the frontmatter-validation record for a single PR-changed file."""
    full_path = repo_root / file_rel
    if not full_path.is_file():
        return {
            "file": file_rel,
            "frontmatter_parse_ok": False,
            "menu_parents": [],
            "aliases_declared": [],
            "alias_collisions": [],
        }
    fm = read_frontmatter(full_path)
    if fm is None:
        return {
            "file": file_rel,
            "frontmatter_parse_ok": False,
            "menu_parents": [],
            "aliases_declared": [],
            "alias_collisions": [],
        }
    aliases = extract_aliases(fm)
    return {
        "file": file_rel,
        "frontmatter_parse_ok": True,
        "menu_parents": check_menu_parents(file_rel, fm, identifier_map),
        "aliases_declared": aliases,
        "alias_collisions": check_alias_collisions(file_rel, aliases, alias_map, pr_files),
    }


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--pr", help="PR number (for `gh pr diff`)")
    p.add_argument("--changed-files", help="Comma-separated changed files (overrides --pr; for testing)")
    p.add_argument("--repo-root", default=".", help="Repo root (default: cwd)")
    p.add_argument("--out", required=True, help="Output JSON path")
    args = p.parse_args()

    repo_root = Path(args.repo_root).resolve()
    if args.changed_files:
        changed = [f.strip() for f in args.changed_files.split(",") if f.strip()]
    else:
        changed = get_changed_files(args.pr)

    # Build global maps via single content tree walk.
    identifier_map, alias_map = build_global_maps(repo_root)
    pr_files = set(changed)

    files = [
        discover_for_file(repo_root, f, identifier_map, alias_map, pr_files)
        for f in changed
    ]
    out = {
        "files": files,
        "global_identifier_map_size": sum(len(v) for v in identifier_map.values()),
        "global_alias_map_size": sum(len(v) for v in alias_map.values()),
    }

    Path(args.out).write_text(json.dumps(out, indent=2) + "\n")
    print(
        f"frontmatter-validate: {len(files)} file(s); "
        f"{out['global_identifier_map_size']} identifiers, "
        f"{out['global_alias_map_size']} aliases mapped → {args.out}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

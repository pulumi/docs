#!/usr/bin/env python3
"""frontmatter-validate.py — pre-step for frontmatter validation.

Architectural mirror of `cross-sibling-discover.py`, `editorial-balance-detect.py`,
and `extract-urls-and-fetch.py`: a workflow pre-step that pre-computes deterministic
frontmatter checks so the model receives a structurally-guaranteed result instead
of computing them inline (where they get skipped under attention pressure).

S38 motivation: the cross-sibling pre-step caught the file-location and alias
collision findings on pr18568, but missed the L11 menu-parent finding. The
menu-parent identifier check is fully deterministic: parse the changed file's
frontmatter, walk content/**/*.md to build a global menu-identifier map, check
that each declared parent exists in the same named menu. Same atomization pattern,
different layer.

Three checks bundled (single content-tree walk + redirects scan):

1. **Menu-parent validation.** For each `menu.<name>.parent: <X>` in a changed
   file's frontmatter, verify `(name, X)` exists somewhere in the global
   identifier map. The S37/S38 pr18568 case: `menu.iac.parent: azure-clouds`
   resolves only against `menu.integrations.identifier: azure-clouds` —
   wrong-named-menu.

2. **Alias collision detection.** Two sub-checks:
   - PR-internal: any alias appearing in 2+ PR-changed files.
   - Repo-wide: any alias on a PR-changed file that already exists as an alias
     on a different (non-PR-changed) canonical file.

3. **URL-ownership check.** Build a global URL-ownership map that
   unifies Hugo `aliases:` (from all `content/**/*.md` frontmatter) and S3
   redirects (from `scripts/redirects/*.txt`), each entry tagged with `scope:
   hugo-alias` or `scope: s3-redirect`. For each PR-changed file, compute its
   rendered URL and look it up in the map. If another file or redirect entry
   claims that URL, surface as 🚨 — the PR is dropping content at a URL
   someone else already owns. Replaces the brittle hardcoded `PARALLEL_PATTERNS`
   table that lived in `cross-sibling-discover.py`; uses Hugo's own routing
   model + the S3 layer the move-doc skill maintains.

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


def build_global_maps(repo_root: Path) -> tuple[dict, dict, dict]:
    """Walk content/**/*.md + scripts/redirects/*.txt and build:

    - identifier_map: {(menu_name, identifier): [file, ...]}
    - alias_map: {alias: [file, ...]}  -- Hugo aliases only, used by alias-collision
    - url_ownership_map: {url: [{file, scope}, ...]}  -- unified Hugo aliases + S3 redirects

    Files indexed by repo-relative path. The url_ownership_map is the broader
    "who claims this URL" view; alias_map remains as the narrower "who's declared
    it as a Hugo alias" view that alias-collision uses.
    """
    identifier_map: dict[tuple[str, str], list[str]] = {}
    alias_map: dict[str, list[str]] = {}
    url_ownership_map: dict[str, list[dict]] = {}
    content_root = repo_root / "content"
    if content_root.is_dir():
        for md_path in content_root.rglob("*.md"):
            rel = md_path.relative_to(repo_root).as_posix()
            fm = read_frontmatter(md_path)
            if fm is None:
                continue
            for name, ident in extract_menu_identifiers(fm):
                identifier_map.setdefault((name, ident), []).append(rel)
            for alias in extract_aliases(fm):
                normalized = normalize_url(alias)
                alias_map.setdefault(alias, []).append(rel)
                url_ownership_map.setdefault(normalized, []).append({
                    "file": rel, "scope": "hugo-alias",
                })
    # Add S3 redirect sources to the url_ownership_map.
    redirects_root = repo_root / "scripts" / "redirects"
    if redirects_root.is_dir():
        for txt_path in sorted(redirects_root.glob("*.txt")):
            try:
                lines = txt_path.read_text(encoding="utf-8", errors="replace").splitlines()
            except OSError:
                continue
            rel_redirect = txt_path.relative_to(repo_root).as_posix()
            for ln_num, line in enumerate(lines, start=1):
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if "|" not in line:
                    continue
                source, _, _ = line.partition("|")
                source = source.strip()
                if not source:
                    continue
                normalized = normalize_url(source)
                url_ownership_map.setdefault(normalized, []).append({
                    "file": f"{rel_redirect}:{ln_num}", "scope": "s3-redirect",
                })
    return identifier_map, alias_map, url_ownership_map


def normalize_url(raw: str) -> str:
    """Normalize a URL for comparison across Hugo aliases, S3 redirect sources,
    and PR-file-derived URLs.

    - Ensure leading slash.
    - Strip trailing `index.html`; replace other `.html` with trailing slash.
    - Ensure trailing slash (unless the path is a file with extension).
    - Lowercase the path (Hugo URLs are case-sensitive in theory, but the
      Pulumi docs convention is lowercase; lower-casing prevents trivial
      case-mismatch misses).
    """
    s = raw.strip()
    if not s:
        return s
    if not s.startswith("/"):
        s = "/" + s
    if s.endswith("index.html"):
        s = s[: -len("index.html")]
    elif s.endswith(".html"):
        s = s[: -len(".html")] + "/"
    if not s.endswith("/"):
        # Has some other extension, probably an asset; leave as-is.
        if "." in s.rsplit("/", 1)[-1]:
            return s.lower()
        s = s + "/"
    return s.lower()


def derive_url_from_path(file_rel: str) -> str:
    """Convert a `content/<...>/<name>.md` path to its rendered Hugo URL.

    Examples:
    - content/docs/iac/clouds/azure/guides/_index.md → /docs/iac/clouds/azure/guides/
    - content/docs/iac/clouds/azure/guides/providers.md → /docs/iac/clouds/azure/guides/providers/
    - content/blog/foo/index.md → /blog/foo/
    """
    p = file_rel
    if p.startswith("content/"):
        p = p[len("content/"):]
    if p.endswith("/_index.md") or p.endswith("/index.md"):
        p = p.rsplit("/", 1)[0] + "/"
    elif p.endswith(".md"):
        p = p[: -len(".md")] + "/"
    return normalize_url(p)


def check_url_ownership(
    file_rel: str,
    url_ownership_map: dict[str, list[dict]],
) -> tuple[str, list[dict]]:
    """Compute PR file's rendered URL and find any claimants in the global map.

    Returns (rendered_url, claimants). Excludes the file itself (a Hugo file
    legitimately claims its own URL via its own existence; we want claimants
    that are OTHER files or S3 redirects).
    """
    rendered = derive_url_from_path(file_rel)
    raw_claimants = url_ownership_map.get(rendered, [])
    claimants = [c for c in raw_claimants if c.get("file") != file_rel]
    return rendered, claimants


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
    url_ownership_map: dict,
    pr_files: set[str],
) -> dict:
    """Compute the frontmatter-validation record for a single PR-changed file."""
    rendered_url, url_claimants = check_url_ownership(file_rel, url_ownership_map)
    full_path = repo_root / file_rel
    if not full_path.is_file():
        return {
            "file": file_rel,
            "frontmatter_parse_ok": False,
            "menu_parents": [],
            "aliases_declared": [],
            "alias_collisions": [],
            "rendered_url": rendered_url,
            "url_collisions": url_claimants,
        }
    fm = read_frontmatter(full_path)
    if fm is None:
        return {
            "file": file_rel,
            "frontmatter_parse_ok": False,
            "menu_parents": [],
            "aliases_declared": [],
            "alias_collisions": [],
            "rendered_url": rendered_url,
            "url_collisions": url_claimants,
        }
    aliases = extract_aliases(fm)
    return {
        "file": file_rel,
        "frontmatter_parse_ok": True,
        "menu_parents": check_menu_parents(file_rel, fm, identifier_map),
        "aliases_declared": aliases,
        "alias_collisions": check_alias_collisions(file_rel, aliases, alias_map, pr_files),
        "rendered_url": rendered_url,
        "url_collisions": url_claimants,
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

    # Build global maps via single content tree walk + redirect-table scan.
    identifier_map, alias_map, url_ownership_map = build_global_maps(repo_root)
    pr_files = set(changed)

    files = [
        discover_for_file(repo_root, f, identifier_map, alias_map, url_ownership_map, pr_files)
        for f in changed
    ]
    url_owner_total = sum(len(v) for v in url_ownership_map.values())
    out = {
        "files": files,
        "global_identifier_map_size": sum(len(v) for v in identifier_map.values()),
        "global_alias_map_size": sum(len(v) for v in alias_map.values()),
        "global_url_ownership_map_size": url_owner_total,
    }

    Path(args.out).write_text(json.dumps(out, indent=2) + "\n")
    print(
        f"frontmatter-validate: {len(files)} file(s); "
        f"{out['global_identifier_map_size']} identifiers, "
        f"{out['global_alias_map_size']} aliases, "
        f"{url_owner_total} URL-ownership entries (Hugo+S3) → {args.out}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

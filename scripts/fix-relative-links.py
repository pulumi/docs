#!/usr/bin/env python3
"""Convert page-relative links to root-relative links in Hugo content files.

Hugo renders regular .md files at /path/to/stem/ (a virtual directory), so
a relative link like ../thing resolves differently in a browser than it does
on the filesystem. This script converts all relative links (./  and ../) to
unambiguous root-relative links (/path/to/target).
"""

import os
import posixpath
import re
import sys
from pathlib import Path

CONTENT_DIR = Path("content")

# Regex to match markdown links and images with relative paths.
# Captures: prefix ([text]( or ![alt](), rel_path, suffix (rest of parens)
# Matches both ./path and ../path patterns.
RELATIVE_LINK_RE = re.compile(
    r'(\[(?:[^\[\]]*(?:\[[^\[\]]*\])?[^\[\]]*)\]|!\[[^\]]*\])'  # link text or image alt
    r'\((\.\.?/[^)#\s]*(?:#[^)]*)?)\)'  # relative URL in parens
)


def get_hugo_url(filepath: Path) -> str:
    """Return the Hugo URL for a content file (e.g. /docs/foo/bar/)."""
    rel = filepath.relative_to(CONTENT_DIR)
    parts = rel.parts
    dirs = list(parts[:-1])
    filename = parts[-1]

    if filename in ("_index.md", "index.md"):
        if dirs:
            return "/" + "/".join(dirs) + "/"
        return "/"
    else:
        stem = Path(filename).stem
        return "/" + "/".join(dirs + [stem]) + "/"


def resolve_relative_link(base_url: str, rel_path: str) -> str:
    """Resolve a relative path against a Hugo page's base URL.

    Uses URL-based resolution (not filesystem-based), because Hugo renders
    each .md file as a virtual directory at its URL path. The browser resolves
    relative links against that URL, not the file's directory on disk.
    """
    # Separate anchor fragment from path
    anchor = ""
    if "#" in rel_path:
        idx = rel_path.index("#")
        anchor = rel_path[idx:]
        rel_path = rel_path[:idx]

    had_trailing_slash = rel_path.endswith("/")

    # posixpath.join then normpath resolves ./  and ../ correctly
    joined = posixpath.join(base_url, rel_path) if rel_path else base_url
    resolved = posixpath.normpath(joined)

    # normpath strips trailing slashes; restore if the original had one
    # or if the path was empty (pure anchor on current page)
    if had_trailing_slash and not resolved.endswith("/"):
        resolved += "/"

    return resolved + anchor


def fix_file(filepath: Path) -> int:
    """Fix relative links in a single file. Returns number of replacements."""
    with open(filepath, encoding="utf-8") as f:
        original = f.read()

    base_url = get_hugo_url(filepath)
    replacements = 0

    def replace_match(m: re.Match) -> str:
        nonlocal replacements
        link_text = m.group(1)
        rel_path = m.group(2)
        root_rel = resolve_relative_link(base_url, rel_path)
        if root_rel == rel_path:
            return m.group(0)  # no change
        replacements += 1
        return f"{link_text}({root_rel})"

    updated = RELATIVE_LINK_RE.sub(replace_match, original)

    if updated != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(updated)

    return replacements


def main():
    total_files = 0
    total_replacements = 0

    for root, _dirs, files in os.walk(CONTENT_DIR):
        for name in files:
            if not name.endswith(".md"):
                continue
            filepath = Path(root) / name
            count = fix_file(filepath)
            if count:
                total_files += 1
                total_replacements += count
                print(f"  {filepath}: {count} replacement(s)")

    print(f"\nDone: {total_replacements} link(s) fixed across {total_files} file(s).")


if __name__ == "__main__":
    main()

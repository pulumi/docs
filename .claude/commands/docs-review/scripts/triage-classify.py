#!/usr/bin/env python3
"""Deterministic PR triage classification.

Reads the PR JSON (from `gh pr view --json title,body,author,files,labels,additions,deletions,commits,isDraft`)
on argv[1] and the unified diff (from `gh pr diff`) on stdin. Emits a single
JSON object on stdout with the classification fields the workflow consumes.

This script does not call any APIs and has no side effects. The model is only
invoked downstream when `prose_check_needed` is true (trivial or
frontmatter-only PRs); everything else is path matching and grep-on-diff.
"""

from __future__ import annotations

import json
import re
import sys
from collections.abc import Iterable

# ---- Path-precedence domain classification --------------------------------

WEBPACK_RE = re.compile(r"^webpack\.[^/]+\.js$")


def classify_path(path: str) -> str | None:
    # Programs first — both static/programs/** AND scripts/programs/** are
    # programs territory (the latter would otherwise fall to infra).
    if path.startswith("static/programs/") or path.startswith("scripts/programs/"):
        return "domain:programs"
    if path.startswith("content/blog/") or path.startswith("content/case-studies/"):
        return "domain:blog"
    for prefix in ("content/docs/", "content/learn/", "content/tutorials/", "content/what-is/"):
        if path.startswith(prefix):
            return "domain:docs"
    if path.startswith(".github/workflows/"):
        return "domain:infra"
    if path.startswith("scripts/") or path.startswith("infrastructure/"):
        return "domain:infra"
    if path in ("Makefile", "package.json", "webpack.config.js"):
        return "domain:infra"
    if WEBPACK_RE.match(path):
        return "domain:infra"
    return None


# ---- Per-file diff inspection ---------------------------------------------

HUNK_HEADER_RE = re.compile(r"^@@ -(\d+)(?:,\d+)? \+(\d+)(?:,\d+)? @@")
LINK_RE = re.compile(r"\[[^\]]*\]\([^)]+\)")


def split_files(diff_text: str) -> list[tuple[str, str]]:
    """Split the unified diff into [(path, file_diff_text), ...]."""
    if not diff_text.strip():
        return []
    chunks = re.split(r"^diff --git ", diff_text, flags=re.MULTILINE)
    out: list[tuple[str, str]] = []
    for chunk in chunks[1:]:  # chunks[0] is empty preamble
        first_line, _, _ = chunk.partition("\n")
        m = re.match(r"a/(\S+) b/(\S+)", first_line)
        if not m:
            continue
        path = m.group(2)  # 'b' path is the new path (handles renames)
        out.append((path, "diff --git " + chunk))
    return out


def iter_hunks(file_diff: str) -> Iterable[tuple[str, list[str]]]:
    """Yield (header_line, body_lines) per hunk."""
    header: str | None = None
    body: list[str] = []
    in_hunk = False
    for line in file_diff.split("\n"):
        if line.startswith("@@"):
            if header is not None:
                yield header, body
            header = line
            body = []
            in_hunk = True
        elif in_hunk:
            body.append(line)
    if header is not None:
        yield header, body


def detect_starting_state(body_lines: list[str], old_start: int) -> str:
    """For an .md file hunk, decide whether the hunk starts in frontmatter
    or body. Uses `---` context lines as ground truth when present;
    falls back to content-shape heuristics."""
    dashdash_positions = [
        i for i, line in enumerate(body_lines)
        if line.startswith(" ") and line[1:].strip() == "---"
    ]
    # Two or more `---` context lines: hunk started before the opening
    # delimiter (only happens when old_start == 1).
    if len(dashdash_positions) >= 2:
        return "pre-frontmatter"
    # Single `---` context line: opening if old_start == 1, otherwise
    # closing (the more common case for aliases / meta_desc edits).
    if len(dashdash_positions) == 1:
        return "pre-frontmatter" if old_start == 1 else "frontmatter"
    # No `---` context. Hugo content frontmatter sits in the first ~30
    # lines of every file; a hunk past that is body, full stop. The
    # YAML-key heuristic below is unreliable past frontmatter because
    # markdown YAML code blocks (e.g., `description: A minimal program.`
    # inside a Pulumi.yaml example) match the same shape and cause body
    # changes to be misclassified as frontmatter changes.
    if old_start > 30:
        return "body"
    # No `---` context. Look at the surrounding content to guess.
    for line in body_lines:
        if not line:
            continue
        if line[0] not in " +-":
            continue
        stripped = line[1:].strip()
        if not stripped:
            continue
        # Markdown-shaped content → body.
        if stripped.startswith(("#", "```", "{{<", "{{%")):
            return "body"
        # YAML-shaped content (key:value at root, no leading whitespace) →
        # frontmatter.
        if re.match(r"^[a-z_][a-zA-Z0-9_-]*:", stripped):
            return "frontmatter"
        # Long prose-looking line → body.
        if len(stripped) > 60 and " " in stripped:
            return "body"
    # Fall back: small line numbers default to frontmatter.
    return "frontmatter" if old_start <= 30 else "body"


def classify_file(path: str, file_diff: str) -> dict:
    """Walk a single file's diff and return its classification flags."""
    head300 = file_diff[:300]
    is_rename = "rename from" in head300 or "rename to" in head300
    is_delete = "+++ /dev/null" in head300
    is_new = "--- /dev/null" in head300
    is_binary = "GIT binary patch" in file_diff or "\nBinary files " in file_diff
    is_md = path.endswith(".md")

    flags = {
        "path": path,
        "is_md": is_md,
        "is_rename": is_rename,
        "is_delete": is_delete,
        "is_new": is_new,
        "is_binary": is_binary,
        "has_frontmatter_change": False,
        "has_body_change": False,
        "has_code_block_change": False,
        "has_shortcode_change": False,
        "has_link_change": False,
    }

    # Per-file link-set comparison: detect link change by comparing the
    # union of (text, url) tuples on `+` lines vs `-` lines. A typo fix in
    # a paragraph that contains unchanged links produces matching sets =>
    # no link change.
    plus_links: set[tuple[str, str]] = set()
    minus_links: set[tuple[str, str]] = set()

    for header, body_lines in iter_hunks(file_diff):
        m = HUNK_HEADER_RE.match(header)
        if not m:
            continue
        old_start = int(m.group(1))

        if is_md:
            state = detect_starting_state(body_lines, old_start)
        else:
            state = "body"

        for line in body_lines:
            if not line:
                continue
            marker = line[0]
            content = line[1:]
            stripped = content.strip()

            # Frontmatter boundary toggling — both context and changed
            # lines can be `---`. If a `---` line is added or removed,
            # that's itself a frontmatter change.
            if is_md and stripped == "---" and marker in " +-":
                if state == "pre-frontmatter":
                    state = "frontmatter"
                elif state == "frontmatter":
                    state = "body"
                if marker in "+-":
                    flags["has_frontmatter_change"] = True
                continue

            if marker == " ":
                continue  # plain context line, no signal

            if marker not in "+-":
                continue

            if is_md and state in ("pre-frontmatter", "frontmatter"):
                flags["has_frontmatter_change"] = True
                continue

            # Body-side change
            flags["has_body_change"] = True
            if stripped.startswith("```"):
                flags["has_code_block_change"] = True
            if "{{<" in stripped or "{{%" in stripped:
                flags["has_shortcode_change"] = True
            line_links = set(re.findall(r"\[([^\]]*)\]\(([^)]+)\)", stripped))
            if marker == "+":
                plus_links |= line_links
            else:
                minus_links |= line_links

    flags["has_link_change"] = plus_links != minus_links
    return flags


# ---- PR-level aggregation --------------------------------------------------


def classify_pr(pr_data: dict, file_flags: list[dict]) -> dict:
    additions = int(pr_data.get("additions") or 0)
    deletions = int(pr_data.get("deletions") or 0)
    files = pr_data.get("files") or []
    file_count = len(files)
    total_lines = additions + deletions

    domains: set[str] = set()
    for f in files:
        d = classify_path(f.get("path", ""))
        if d:
            domains.add(d)

    has_any_frontmatter = any(f["has_frontmatter_change"] for f in file_flags)
    has_any_body = any(f["has_body_change"] for f in file_flags)
    has_any_link = any(f["has_link_change"] for f in file_flags)
    has_any_code = any(f["has_code_block_change"] or f["has_shortcode_change"] for f in file_flags)
    has_any_rename_or_delete = any(f["is_rename"] or f["is_delete"] for f in file_flags)
    has_any_new_file = any(f["is_new"] for f in file_flags)
    has_any_binary = any(f["is_binary"] for f in file_flags)

    # Trivial and frontmatter-only short-circuits only apply to Hugo content
    # markdown — never to programs, scripts, layouts, or other code paths.
    # A 5-line .ts change shouldn't escape review just because it has no
    # fenced code blocks.
    all_files_content_md = file_count > 0 and all(
        f.get("path", "").startswith("content/") and f.get("path", "").endswith(".md")
        for f in files
    )

    trivial = (
        additions <= 10
        and file_count <= 2
        and all_files_content_md
        and not has_any_frontmatter
        and not has_any_link
        and not has_any_code
        and not has_any_rename_or_delete
        and not has_any_new_file
        and not has_any_binary
    )

    # Frontmatter-only: any number of content/*.md files, but every file's
    # changes are entirely within the frontmatter block. Mutually exclusive
    # with trivial.
    frontmatter_only = (
        not trivial
        and all_files_content_md
        and has_any_frontmatter
        and not has_any_body
        and not has_any_rename_or_delete
        and not has_any_new_file
        and not has_any_binary
    )

    return {
        "target_domains": sorted(domains),
        "mixed": len(domains) > 1,
        "trivial": trivial,
        "frontmatter_only": frontmatter_only,
        "prose_check_needed": trivial or frontmatter_only,
        "summary": {
            "lines": total_lines,
            "files": file_count,
            "frontmatter_changed": has_any_frontmatter,
            "body_changed": has_any_body,
            "rename_or_delete": has_any_rename_or_delete,
        },
    }


# ---- Entry point -----------------------------------------------------------


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: triage-classify.py <pr-data.json>  (diff on stdin)", file=sys.stderr)
        return 2
    with open(sys.argv[1], encoding="utf-8") as fh:
        pr_data = json.load(fh)
    diff_text = sys.stdin.read()
    files = split_files(diff_text)
    file_flags = [classify_file(p, d) for p, d in files]
    result = classify_pr(pr_data, file_flags)
    json.dump(result, sys.stdout, separators=(",", ":"))
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

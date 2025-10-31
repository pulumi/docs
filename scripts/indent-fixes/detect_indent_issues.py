#!/usr/bin/env python3
"""
Detect incorrectly indented bullet points in markdown files.
This script finds bullet lists with 4-space indentation that should be unindented.
It distinguishes between YAML frontmatter (where indentation is correct) and
markdown content (where 4-space indentation creates code blocks).
"""

import re
from pathlib import Path
from typing import List, Tuple

def detect_indent_issues(file_path: str) -> List[Tuple[int, str]]:
    """
    Detect lines with problematic 4-space indentation before bullet points.
    Returns a list of (line_number, line_content) tuples.
    """
    issues = []

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    in_frontmatter = False
    frontmatter_count = 0
    in_code_block = False

    for i, line in enumerate(lines, 1):
        # Track frontmatter boundaries (YAML between --- markers)
        if line.strip() == '---':
            frontmatter_count += 1
            if frontmatter_count == 1:
                in_frontmatter = True
            elif frontmatter_count == 2:
                in_frontmatter = False
            continue

        # Track code blocks (```)
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            continue

        # Skip if we're in frontmatter or code block
        if in_frontmatter or in_code_block:
            continue

        # Check for 4-space indented bullet points
        # Pattern: exactly 4 spaces, then dash, then space or content
        if re.match(r'^    - ', line):
            # Check if this might be a legitimate nested list item
            # Look at previous lines to see if there's a parent list item
            is_nested = False
            if i > 1:
                # Check previous non-empty lines
                for j in range(i-2, max(0, i-10), -1):
                    prev_line = lines[j].rstrip()
                    if not prev_line:
                        continue
                    # If previous line is a list item without indent, this might be nested
                    if re.match(r'^  - ', prev_line):
                        is_nested = True
                        break
                    # If we hit another non-list line, assume not nested
                    if prev_line and not prev_line.startswith(' '):
                        break

            # Also check for YAML-like context (key: value patterns nearby)
            is_yaml_context = False
            if i > 1 and i < len(lines):
                # Check surrounding lines for YAML patterns
                for j in range(max(0, i-5), min(len(lines), i+5)):
                    if re.search(r'^\w+:', lines[j]):
                        # Could be YAML or markdown heading
                        # If it's followed by indented content, likely YAML
                        if j < len(lines) - 1 and lines[j+1].startswith('  '):
                            is_yaml_context = True
                            break

            if not is_nested and not is_yaml_context:
                issues.append((i, line.rstrip()))

    return issues

def main():
    # Search in content/docs directory (relative to repo root)
    # Script can be run from repo root or from scripts/indent-fixes/
    repo_root = Path(__file__).parent.parent.parent
    content_dir = repo_root / 'content' / 'docs'

    all_issues = {}

    for md_file in content_dir.rglob('*.md'):
        issues = detect_indent_issues(str(md_file))
        if issues:
            all_issues[str(md_file)] = issues

    # Print results
    if all_issues:
        print(f"Found {len(all_issues)} files with potential indentation issues:\n")
        total_issues = 0
        for file_path in sorted(all_issues.keys()):
            issues = all_issues[file_path]
            total_issues += len(issues)
            print(f"\n{file_path}: {len(issues)} issue(s)")
            for line_num, line_content in issues:
                print(f"  Line {line_num}: {line_content}")

        print(f"\n\nTotal: {total_issues} potential issues across {len(all_issues)} files")
    else:
        print("No indentation issues found.")

if __name__ == '__main__':
    main()

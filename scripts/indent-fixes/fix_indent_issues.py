#!/usr/bin/env python3
"""
Fix incorrectly indented bullet points in markdown files.
This script removes the 4-space indentation from bullet lists that should be unindented.
"""

import re
from pathlib import Path

def detect_indent_issues(file_path: str) -> list[int]:
    """
    Detect line numbers with problematic 4-space indentation before bullet points.
    Returns a list of line numbers (1-indexed).
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
        if re.match(r'^    - ', line):
            # Check if this might be a legitimate nested list item
            is_nested = False
            if i > 1:
                for j in range(i-2, max(0, i-10), -1):
                    prev_line = lines[j].rstrip()
                    if not prev_line:
                        continue
                    if re.match(r'^  - ', prev_line):
                        is_nested = True
                        break
                    if prev_line and not prev_line.startswith(' '):
                        break

            # Check for YAML-like context
            is_yaml_context = False
            if i > 1 and i < len(lines):
                for j in range(max(0, i-5), min(len(lines), i+5)):
                    if re.search(r'^\w+:', lines[j]):
                        if j < len(lines) - 1 and lines[j+1].startswith('  '):
                            is_yaml_context = True
                            break

            if not is_nested and not is_yaml_context:
                issues.append(i)

    return issues

def fix_file(file_path: str) -> int:
    """
    Fix indentation issues in a file by removing the 4-space indent from bullet points.
    Returns the number of lines fixed.
    """
    issue_line_numbers = detect_indent_issues(file_path)
    if not issue_line_numbers:
        return 0

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    fixed_count = 0
    for line_num in issue_line_numbers:
        # Convert to 0-indexed
        idx = line_num - 1
        if idx < len(lines):
            # Remove exactly 4 spaces from the beginning
            if lines[idx].startswith('    - '):
                lines[idx] = lines[idx][4:]  # Remove first 4 characters
                fixed_count += 1

    # Write the fixed content back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)

    return fixed_count

def main():
    # Search in content/docs directory (relative to repo root)
    # Script can be run from repo root or from scripts/indent-fixes/
    repo_root = Path(__file__).parent.parent.parent
    content_dir = repo_root / 'content' / 'docs'

    all_files = {}
    total_fixed = 0

    for md_file in content_dir.rglob('*.md'):
        fixed_count = fix_file(str(md_file))
        if fixed_count > 0:
            all_files[str(md_file)] = fixed_count
            total_fixed += fixed_count

    # Print results
    if all_files:
        print(f"Fixed {total_fixed} lines across {len(all_files)} files:\n")
        for file_path in sorted(all_files.keys()):
            count = all_files[file_path]
            print(f"  {file_path}: {count} line(s) fixed")
    else:
        print("No files needed fixing.")

if __name__ == '__main__':
    main()

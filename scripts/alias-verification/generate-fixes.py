#!/usr/bin/env python3
"""
Generate Alias Fixes Script
Generates Edit commands to add missing aliases to renamed files.
"""

import sys
from pathlib import Path

def path_to_url(filepath):
    """Convert file path to Hugo URL path."""
    url = filepath.replace('content', '', 1)
    url = url.replace('.md', '')
    url = url.replace('/_index', '')
    if not url.endswith('/'):
        url += '/'
    return url

def extract_frontmatter_and_aliases(filepath):
    """Extract full frontmatter and aliases list from file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return None, None, None

    # Find frontmatter boundaries
    lines = content.split('\n')
    if not lines or lines[0].strip() != '---':
        return None, None, None

    frontmatter_end = -1
    for i in range(1, len(lines)):
        if lines[i].strip() == '---':
            frontmatter_end = i
            break

    if frontmatter_end == -1:
        return None, None, None

    frontmatter_lines = lines[1:frontmatter_end]

    # Extract aliases
    aliases = []
    in_aliases = False

    for line in frontmatter_lines:
        if line.startswith('aliases:'):
            in_aliases = True
            continue

        if in_aliases and line and not line.startswith((' ', '\t', '-')):
            in_aliases = False

        if in_aliases and line.strip().startswith('-'):
            alias = line.strip()[1:].strip()
            aliases.append(alias)

    return content, frontmatter_lines, aliases

def main():
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent.parent
    missing_log = script_dir / 'aliases-missing.txt'
    suspicious_log = script_dir / 'aliases-suspicious.txt'
    fixes_script = script_dir / 'apply-fixes.sh'

    if not missing_log.exists() or not suspicious_log.exists():
        print("ERROR: Log files not found. Run verify-aliases.py first", file=sys.stderr)
        sys.exit(1)

    fixes = []

    # Process MISSING files (only .md files)
    print("Processing MISSING files...")
    with open(missing_log, 'r') as f:
        lines = f.readlines()

    i = 0
    missing_count = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith('❌ MISSING:'):
            new_path = line.split(':', 1)[1].strip()

            # Only process .md files
            if not new_path.endswith('.md'):
                i += 2  # Skip the OLD line and blank line
                continue

            # Next line has OLD path
            i += 1
            old_line = lines[i].strip()
            if old_line.startswith('OLD:'):
                parts = old_line.split('→')
                old_path = parts[0].replace('OLD:', '').strip()
                expected_alias = parts[1].replace('EXPECTED ALIAS:', '').strip()

                new_file = repo_root / new_path
                content, frontmatter_lines, aliases = extract_frontmatter_and_aliases(new_file)

                if content and not aliases:
                    # Find where to insert aliases (after title/meta_desc, before menu)
                    insert_after = -1
                    for idx, fm_line in enumerate(frontmatter_lines):
                        if fm_line.startswith(('title:', 'meta_desc:', 'h1:', 'meta_image:')):
                            insert_after = idx

                    # Build new frontmatter with aliases
                    new_frontmatter_lines = frontmatter_lines.copy()
                    new_frontmatter_lines.insert(insert_after + 1, f"aliases:")
                    new_frontmatter_lines.insert(insert_after + 2, f"  - {expected_alias}")

                    # Reconstruct full content
                    content_lines = content.split('\n')
                    frontmatter_end = content_lines.index('---', 1)
                    new_content_lines = ['---'] + new_frontmatter_lines + ['---'] + content_lines[frontmatter_end+1:]

                    fixes.append({
                        'file': str(new_file),
                        'type': 'MISSING',
                        'old_content': content,
                        'new_content': '\n'.join(new_content_lines)
                    })
                    missing_count += 1

        i += 1

    print(f"  Found {missing_count} MISSING .md files to fix")

    # Process SUSPICIOUS files
    print("Processing SUSPICIOUS files...")
    with open(suspicious_log, 'r') as f:
        lines = f.readlines()

    i = 0
    suspicious_count = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith('⚠️  SUSPICIOUS:'):
            new_path = line.split(':', 1)[1].strip()

            # Next line has OLD path
            i += 1
            old_line = lines[i].strip()
            if old_line.startswith('OLD:'):
                parts = old_line.split('→')
                old_path = parts[0].replace('OLD:', '').strip()
                expected_alias = parts[1].replace('EXPECTED ALIAS:', '').strip()

                new_file = repo_root / new_path
                content, frontmatter_lines, aliases = extract_frontmatter_and_aliases(new_file)

                if content and aliases and expected_alias not in aliases:
                    # Find last alias line and its indentation
                    last_alias_idx = -1
                    alias_indent = '  '
                    for idx, fm_line in enumerate(frontmatter_lines):
                        if fm_line.strip().startswith('-') and any(alias in fm_line for alias in aliases):
                            last_alias_idx = idx
                            # Extract the indentation from this line
                            alias_indent = fm_line[:len(fm_line) - len(fm_line.lstrip())]

                    # Build new frontmatter with added alias
                    new_frontmatter_lines = frontmatter_lines.copy()
                    new_frontmatter_lines.insert(last_alias_idx + 1, f"{alias_indent}- {expected_alias}")

                    # Reconstruct full content
                    content_lines = content.split('\n')
                    frontmatter_end = content_lines.index('---', 1)
                    new_content_lines = ['---'] + new_frontmatter_lines + ['---'] + content_lines[frontmatter_end+1:]

                    fixes.append({
                        'file': str(new_file),
                        'type': 'SUSPICIOUS',
                        'old_content': content,
                        'new_content': '\n'.join(new_content_lines)
                    })
                    suspicious_count += 1

        i += 1

    print(f"  Found {suspicious_count} SUSPICIOUS files to fix")
    print()
    print(f"Total fixes to apply: {len(fixes)}")

    # Write fixes to a data file
    fixes_data = script_dir / 'fixes-data.txt'
    with open(fixes_data, 'w') as f:
        for fix in fixes:
            f.write(f"FILE:{fix['file']}\n")
            f.write(f"TYPE:{fix['type']}\n")
            f.write("===OLD===\n")
            f.write(fix['old_content'])
            f.write("\n===NEW===\n")
            f.write(fix['new_content'])
            f.write("\n===END===\n\n")

    print(f"Fixes written to: {fixes_data}")

    # Show samples
    print("\n=== SAMPLE FIXES ===\n")

    # Show 2 MISSING samples
    missing_samples = [f for f in fixes if f['type'] == 'MISSING'][:2]
    for sample in missing_samples:
        print(f"MISSING: {Path(sample['file']).relative_to(repo_root)}")
        # Show just the frontmatter diff
        old_lines = sample['old_content'].split('\n')
        new_lines = sample['new_content'].split('\n')
        fm_end_old = old_lines.index('---', 1)
        fm_end_new = new_lines.index('---', 1)
        print("OLD frontmatter:")
        for line in old_lines[:fm_end_old+1]:
            print(f"  {line}")
        print("\nNEW frontmatter:")
        for line in new_lines[:fm_end_new+1]:
            print(f"  {line}")
        print()

    # Show 2 SUSPICIOUS samples
    suspicious_samples = [f for f in fixes if f['type'] == 'SUSPICIOUS'][:2]
    for sample in suspicious_samples:
        print(f"SUSPICIOUS: {Path(sample['file']).relative_to(repo_root)}")
        # Show just the aliases section
        new_lines = sample['new_content'].split('\n')
        in_aliases = False
        for line in new_lines:
            if line.strip().startswith('aliases:'):
                in_aliases = True
            if in_aliases:
                print(f"  {line}")
                if line.strip() and not line.startswith((' ', '\t')) and not line.strip().startswith('aliases:') and not line.strip().startswith('-'):
                    break
        print()

if __name__ == '__main__':
    main()

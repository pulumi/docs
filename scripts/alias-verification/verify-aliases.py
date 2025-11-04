#!/usr/bin/env python3
"""
Alias Verification Script
Checks if renamed and deleted files have proper aliases pointing to their old locations.
"""

import sys
from pathlib import Path

def path_to_url(filepath):
    """Convert file path to Hugo URL path."""
    # Remove content/ prefix
    url = filepath.replace('content', '', 1)
    # Remove .md extension
    url = url.replace('.md', '')
    # For _index.md files, remove _index
    url = url.replace('/_index', '')
    # Ensure trailing slash
    if not url.endswith('/'):
        url += '/'
    return url

def extract_aliases(filepath):
    """Extract aliases list from frontmatter."""
    aliases = []
    in_frontmatter = False
    in_aliases = False
    frontmatter_count = 0

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.rstrip()

                # Track frontmatter boundaries
                if line == '---':
                    frontmatter_count += 1
                    if frontmatter_count == 1:
                        in_frontmatter = True
                    elif frontmatter_count == 2:
                        break
                    continue

                if not in_frontmatter:
                    continue

                # Check for aliases field
                if line.startswith('aliases:'):
                    in_aliases = True
                    continue

                # End of aliases section
                if in_aliases and line and not line.startswith((' ', '\t', '-')):
                    in_aliases = False

                # Extract alias entries
                if in_aliases and line.strip().startswith('-'):
                    alias = line.strip()[1:].strip()
                    aliases.append(alias)

    except Exception as e:
        print(f"Warning: Could not read {filepath}: {e}", file=sys.stderr)

    return aliases

def find_alias_in_content(repo_root, expected_alias):
    """Search all content/docs files for a specific alias."""
    content_dir = repo_root / 'content' / 'docs'
    if not content_dir.exists():
        return None

    for md_file in content_dir.rglob('*.md'):
        aliases = extract_aliases(md_file)
        if expected_alias in aliases:
            return md_file.relative_to(repo_root)

    return None

def main():
    script_dir = Path(__file__).parent
    renames_file = script_dir / 'renames.txt'
    repo_root = script_dir.parent.parent

    if not renames_file.exists():
        print(f"ERROR: Renames file not found: {renames_file}", file=sys.stderr)
        print("Run ./extract-renames.sh first", file=sys.stderr)
        sys.exit(1)

    # Counters
    correct_renames = 0
    missing_renames = 0
    suspicious_renames = 0
    total_renames = 0

    correct_deletes = 0
    missing_deletes = 0
    total_deletes = 0

    # Output files
    correct_log = script_dir / 'aliases-correct.txt'
    missing_log = script_dir / 'aliases-missing.txt'
    suspicious_log = script_dir / 'aliases-suspicious.txt'

    correct_log.write_text('')
    missing_log.write_text('')
    suspicious_log.write_text('')

    print("Verifying aliases for renamed and deleted content files...")
    print()

    # Process renames and deletes
    with open(renames_file, 'r') as f:
        for line in f:
            line = line.strip()

            # Handle renames (R status)
            if line.startswith('R'):
                parts = line.split('\t')
                if len(parts) != 3:
                    continue

                _, old_path, new_path = parts

                # Skip non-content files
                if not old_path.startswith('content/docs/'):
                    continue

                total_renames += 1

                # Convert old path to expected URL
                expected_alias = path_to_url(old_path)

                # Check if new file exists
                new_file = repo_root / new_path
                if not new_file.exists():
                    print(f"Warning: New file doesn't exist: {new_file}", file=sys.stderr)
                    continue

                # Extract aliases from frontmatter
                aliases = extract_aliases(new_file)

                # Check if expected alias is present
                if not aliases:
                    missing_renames += 1
                    with open(missing_log, 'a') as log:
                        log.write(f"❌ MISSING (RENAME): {new_path}\n")
                        log.write(f"   OLD: {old_path} → EXPECTED ALIAS: {expected_alias}\n\n")
                elif expected_alias in aliases:
                    correct_renames += 1
                    with open(correct_log, 'a') as log:
                        log.write(f"✓ RENAME: {new_path}\n")
                else:
                    suspicious_renames += 1
                    with open(suspicious_log, 'a') as log:
                        log.write(f"⚠️  SUSPICIOUS (RENAME): {new_path}\n")
                        log.write(f"   OLD: {old_path} → EXPECTED ALIAS: {expected_alias}\n")
                        log.write(f"   HAS: {', '.join(aliases)}\n\n")

            # Handle deletes (D status)
            elif line.startswith('D'):
                parts = line.split('\t')
                if len(parts) != 2:
                    continue

                _, old_path = parts

                # Skip non-content files
                if not old_path.startswith('content/docs/'):
                    continue

                total_deletes += 1

                # Convert old path to expected URL
                expected_alias = path_to_url(old_path)

                # Search for this alias in all current content files
                found_in = find_alias_in_content(repo_root, expected_alias)

                if found_in:
                    correct_deletes += 1
                    with open(correct_log, 'a') as log:
                        log.write(f"✓ DELETE: {old_path}\n")
                        log.write(f"   ALIAS FOUND IN: {found_in}\n")
                else:
                    missing_deletes += 1
                    with open(missing_log, 'a') as log:
                        log.write(f"❌ MISSING (DELETE): {old_path}\n")
                        log.write(f"   EXPECTED ALIAS: {expected_alias}\n")
                        log.write(f"   Not found in any current content file\n\n")

            # Progress indicator
            total = total_renames + total_deletes
            if total % 50 == 0 and total > 0:
                print(f"Processed {total} files...", file=sys.stderr)

    # Print summary
    print("=== VERIFICATION SUMMARY ===")
    print(f"Renamed files: {total_renames}")
    print(f"Deleted files: {total_deletes}")
    print(f"Total files:   {total_renames + total_deletes}")
    print()
    print(f"✓ CORRECT:    {correct_renames + correct_deletes} (Renames: {correct_renames}, Deletes: {correct_deletes})")
    print(f"❌ MISSING:    {missing_renames + missing_deletes} (Renames: {missing_renames}, Deletes: {missing_deletes})")
    print(f"⚠️  SUSPICIOUS: {suspicious_renames} (Renames only)")
    print()

    total_missing = missing_renames + missing_deletes
    total_correct = correct_renames + correct_deletes

    if total_missing == 0 and suspicious_renames == 0:
        print(f"🎉 ALL ALIASES VERIFIED! All {total_correct} files have correct aliases.")
        sys.exit(0)
    else:
        print("❌ ISSUES FOUND - Details in:")
        if total_correct > 0:
            print(f"  ✓ {correct_log}")
        if total_missing > 0:
            print(f"  ❌ {missing_log}")
        if suspicious_renames > 0:
            print(f"  ⚠️  {suspicious_log}")
        sys.exit(1)

if __name__ == '__main__':
    main()

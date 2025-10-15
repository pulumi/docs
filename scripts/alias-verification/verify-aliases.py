#!/usr/bin/env python3
"""
Alias Verification Script
Checks if renamed files have proper aliases pointing to their old locations.
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

def main():
    script_dir = Path(__file__).parent
    renames_file = script_dir / 'renames.txt'
    repo_root = script_dir.parent.parent

    if not renames_file.exists():
        print(f"ERROR: Renames file not found: {renames_file}", file=sys.stderr)
        print("Run ./extract-renames.sh first", file=sys.stderr)
        sys.exit(1)

    # Counters
    correct = 0
    missing = 0
    suspicious = 0
    total_content = 0

    # Output files
    correct_log = script_dir / 'aliases-correct.txt'
    missing_log = script_dir / 'aliases-missing.txt'
    suspicious_log = script_dir / 'aliases-suspicious.txt'

    correct_log.write_text('')
    missing_log.write_text('')
    suspicious_log.write_text('')

    print("Verifying aliases for renamed content files...")
    print()

    # Process each rename
    with open(renames_file, 'r') as f:
        for line in f:
            line = line.strip()
            if not line.startswith('R'):
                continue

            parts = line.split('\t')
            if len(parts) != 3:
                continue

            _similarity, old_path, new_path = parts

            # Skip non-content files
            if not old_path.startswith('content/docs/'):
                continue

            total_content += 1

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
                missing += 1
                with open(missing_log, 'a') as log:
                    log.write(f"❌ MISSING: {new_path}\n")
                    log.write(f"   OLD: {old_path} → EXPECTED ALIAS: {expected_alias}\n\n")
            elif expected_alias in aliases:
                correct += 1
                with open(correct_log, 'a') as log:
                    log.write(f"✓ {new_path}\n")
            else:
                suspicious += 1
                with open(suspicious_log, 'a') as log:
                    log.write(f"⚠️  SUSPICIOUS: {new_path}\n")
                    log.write(f"   OLD: {old_path} → EXPECTED ALIAS: {expected_alias}\n")
                    log.write(f"   HAS: {', '.join(aliases)}\n\n")

            # Progress indicator
            if total_content % 50 == 0:
                print(f"Processed {total_content} files...", file=sys.stderr)

    # Print summary
    print("=== VERIFICATION SUMMARY ===")
    print(f"Total content files renamed: {total_content}")
    print()
    print(f"✓ CORRECT:    {correct}")
    print(f"❌ MISSING:    {missing}")
    print(f"⚠️  SUSPICIOUS: {suspicious}")
    print()

    if missing == 0 and suspicious == 0:
        print(f"🎉 ALL ALIASES VERIFIED! All {correct} files have correct aliases.")
        sys.exit(0)
    else:
        print("❌ ISSUES FOUND - Details in:")
        if correct > 0:
            print(f"  ✓ {correct_log}")
        if missing > 0:
            print(f"  ❌ {missing_log}")
        if suspicious > 0:
            print(f"  ⚠️  {suspicious_log}")
        sys.exit(1)

if __name__ == '__main__':
    main()

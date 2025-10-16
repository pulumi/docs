#!/usr/bin/env python3
"""
Generate Historical Alias Fixes

Reads the output from verify-all-historical-aliases.py and generates
a structured fixes file that can be applied by apply-historical-fixes.py
"""

import sys
import json
from pathlib import Path
from typing import Set, List, Dict

def extract_aliases(filepath: Path) -> Set[str]:
    """Extract aliases set from frontmatter."""
    aliases = set()
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
                    aliases.add(alias)

    except Exception as e:
        print(f"Warning: Could not read {filepath}: {e}", file=sys.stderr)

    return aliases

def parse_missing_log(missing_log: Path, repo_root: Path) -> List[Dict]:
    """
    Parse the historical-aliases-missing.txt file.
    Returns a list of dicts with file_path and missing_aliases.
    """
    fixes = []
    current_file = None
    current_missing = []
    in_missing_section = False

    with open(missing_log, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip()

            # New file entry
            if line.startswith('❌ MISSING ALIASES:'):
                # Save previous entry if exists
                if current_file and current_missing:
                    fixes.append({
                        'file_path': current_file,
                        'missing_aliases': sorted(current_missing)
                    })

                # Start new entry
                current_file = line.split('❌ MISSING ALIASES:')[1].strip()
                current_missing = []
                in_missing_section = False

            # Start of missing aliases list
            elif 'Missing aliases' in line and line.strip().endswith(':'):
                in_missing_section = True

            # Alias entry
            elif in_missing_section and line.strip().startswith('-'):
                alias = line.strip()[1:].strip()
                current_missing.append(alias)

            # Empty line ends the current file entry
            elif not line.strip() and current_file and current_missing:
                fixes.append({
                    'file_path': current_file,
                    'missing_aliases': sorted(current_missing)
                })
                current_file = None
                current_missing = []
                in_missing_section = False

        # Don't forget the last entry
        if current_file and current_missing:
            fixes.append({
                'file_path': current_file,
                'missing_aliases': sorted(current_missing)
            })

    return fixes

def main():
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent.parent
    missing_log = script_dir / 'historical-aliases-missing.txt'
    output_file = script_dir / 'historical-fixes.json'

    if not missing_log.exists():
        print(f"ERROR: Missing log file not found: {missing_log}", file=sys.stderr)
        print("Run verify-all-historical-aliases.py first", file=sys.stderr)
        sys.exit(1)

    print("Parsing historical-aliases-missing.txt...")
    fixes_data = parse_missing_log(missing_log, repo_root)

    if not fixes_data:
        print("No missing aliases found in log file!")
        sys.exit(0)

    print(f"Found {len(fixes_data)} files with missing aliases")
    print("\nGenerating fixes with current alias information...")

    # Enhance each fix with current aliases
    enhanced_fixes = []
    for fix in fixes_data:
        file_path = repo_root / fix['file_path']

        if not file_path.exists():
            print(f"Warning: File not found: {file_path}", file=sys.stderr)
            continue

        # Get current aliases
        current_aliases = extract_aliases(file_path)

        # Combine current + missing aliases (deduplicated and sorted)
        all_aliases = sorted(set(current_aliases) | set(fix['missing_aliases']))

        enhanced_fixes.append({
            'file_path': str(fix['file_path']),
            'current_aliases': sorted(current_aliases),
            'missing_aliases': fix['missing_aliases'],
            'new_aliases': all_aliases,
            'aliases_to_add': len(fix['missing_aliases'])
        })

    # Write output
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(enhanced_fixes, f, indent=2)

    # Print summary
    print("\n" + "="*80)
    print("=== FIX GENERATION SUMMARY ===")
    print("="*80)
    print(f"Files to fix:              {len(enhanced_fixes)}")
    print(f"Total aliases to add:      {sum(f['aliases_to_add'] for f in enhanced_fixes)}")
    print()
    print(f"📄 Fixes written to: {output_file}")
    print()
    print("💡 Next steps:")
    print("   1. Review the generated fixes in historical-fixes.json")
    print("   2. Run apply-historical-fixes.py to apply the fixes")
    print("   3. Re-run verify-all-historical-aliases.py to verify")
    print()

    # Show a few examples
    print("📋 Example fixes (first 5 files):")
    for i, fix in enumerate(enhanced_fixes[:5], 1):
        print(f"\n{i}. {fix['file_path']}")
        print(f"   Current aliases: {len(fix['current_aliases'])}")
        print(f"   Adding {len(fix['missing_aliases'])} missing aliases:")
        for alias in fix['missing_aliases']:
            print(f"     + {alias}")

    if len(enhanced_fixes) > 5:
        print(f"\n   ... and {len(enhanced_fixes) - 5} more files")

if __name__ == '__main__':
    main()

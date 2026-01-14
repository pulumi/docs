#!/usr/bin/env python3
"""
Apply Alias Fixes Script
Applies the generated fixes to add missing aliases to renamed files.
"""

import sys
from pathlib import Path

def main():
    script_dir = Path(__file__).parent
    fixes_data = script_dir / 'fixes-data.txt'

    if not fixes_data.exists():
        print("ERROR: fixes-data.txt not found. Run generate-fixes.py first", file=sys.stderr)
        sys.exit(1)

    # Parse fixes
    fixes = []
    current_fix = {}
    current_section = None
    section_content = []

    with open(fixes_data, 'r') as f:
        for line in f:
            if line.startswith('FILE:'):
                if current_fix and 'file' in current_fix:
                    fixes.append(current_fix)
                current_fix = {'file': line[5:].strip()}
                current_section = None
                section_content = []
            elif line.startswith('TYPE:'):
                current_fix['type'] = line[5:].strip()
            elif line.startswith('===OLD==='):
                if current_section and section_content:
                    current_fix[current_section] = ''.join(section_content)
                current_section = 'old_content'
                section_content = []
            elif line.startswith('===NEW==='):
                if current_section and section_content:
                    current_fix[current_section] = ''.join(section_content)
                current_section = 'new_content'
                section_content = []
            elif line.startswith('===END==='):
                if current_section and section_content:
                    current_fix[current_section] = ''.join(section_content)
                current_section = None
                section_content = []
            elif current_section:
                section_content.append(line)

    if current_fix and 'file' in current_fix:
        fixes.append(current_fix)

    print(f"Loaded {len(fixes)} fixes")
    print()

    # Apply fixes in batches
    batch_size = 50
    total = len(fixes)
    applied = 0
    failed = 0

    for i in range(0, total, batch_size):
        batch = fixes[i:i+batch_size]
        batch_num = (i // batch_size) + 1
        total_batches = (total + batch_size - 1) // batch_size

        print(f"=== Batch {batch_num}/{total_batches} ({len(batch)} files) ===")

        for fix in batch:
            filepath = Path(fix['file'])

            try:
                # Write the new content, ensuring exactly one trailing newline
                content = fix['new_content'].rstrip() + '\n'
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)

                applied += 1
                print(f"  ✓ {filepath.relative_to(Path.cwd())}")

            except Exception as e:
                failed += 1
                print(f"  ✗ {filepath.relative_to(Path.cwd())}: {e}", file=sys.stderr)

        print()

    print(f"=== SUMMARY ===")
    print(f"Applied: {applied}")
    print(f"Failed: {failed}")
    print(f"Total: {total}")

    if failed > 0:
        sys.exit(1)

if __name__ == '__main__':
    main()

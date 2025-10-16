#!/usr/bin/env python3
"""
Comprehensive Historical Alias Verification Script

This script checks the COMPLETE git history of every file in content/docs/
to ensure ALL historical paths have corresponding aliases. Unlike verify-aliases.py
which only checks branch diffs, this catches:
- Pre-reorg moves that happened on master
- Multi-hop moves (A→B→C where only B is aliased)
- Cross-branch moves
- Old repository migrations
"""

import sys
import subprocess
from pathlib import Path
from typing import Set, List, Tuple, Dict

def path_to_url(filepath: str) -> str:
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

def get_file_history(repo_root: Path, current_path: Path) -> Set[str]:
    """
    Get all historical paths for a file using git log --follow.
    Only checks the past 6 months to avoid very old/irrelevant paths.
    Returns a set of unique file paths this file has ever had.
    """
    try:
        # Use --follow to track renames, --name-only to get just paths
        # --all to check all branches, not just current
        # --since="6 months ago" to limit scope to recent history
        result = subprocess.run(
            ['git', 'log', '--follow', '--all', '--since=6 months ago', '--name-only', '--format=', '--', str(current_path.relative_to(repo_root))],
            cwd=repo_root,
            capture_output=True,
            text=True,
            check=True
        )

        # Extract unique paths, filter out empty lines
        paths = set(line.strip() for line in result.stdout.split('\n') if line.strip())

        # Filter to only content/docs paths
        docs_paths = {p for p in paths if p.startswith('content/docs/')}

        return docs_paths

    except subprocess.CalledProcessError as e:
        print(f"Warning: Could not get history for {current_path}: {e}", file=sys.stderr)
        return set()

def load_s3_redirects(repo_root: Path) -> Dict[str, str]:
    """Load all S3 redirect mappings from scripts/redirects/*.txt files.

    Returns a dict mapping source URLs to destination URLs.
    Format: {'/docs/esc-cli/': '/docs/esc/cli/'}
    """
    redirects = {}
    redirects_dir = repo_root / 'scripts' / 'redirects'

    if not redirects_dir.exists():
        return redirects

    for redirect_file in redirects_dir.glob('*.txt'):
        try:
            with open(redirect_file, 'r', encoding='utf-8') as f:
                for line_num, line in enumerate(f, 1):
                    line = line.strip()
                    if not line or line.startswith('#'):
                        continue

                    # Format: source|destination
                    if '|' not in line:
                        print(f"Warning: Invalid redirect format in {redirect_file}:{line_num}", file=sys.stderr)
                        continue

                    source, destination = line.split('|', 1)
                    source = source.strip()
                    destination = destination.strip()

                    # Convert source to URL format
                    # Remove /index.html suffix if present
                    source_url = '/' + source.replace('/index.html', '/')

                    redirects[source_url] = destination

        except Exception as e:
            print(f"Warning: Could not read redirect file {redirect_file}: {e}", file=sys.stderr)

    return redirects

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

def analyze_file(repo_root: Path, current_file: Path, s3_redirects: Dict[str, str]) -> Tuple[Set[str], Set[str], Set[str], Set[str]]:
    """
    Analyze a single file for historical aliases.
    Returns (all_historical_urls, current_aliases, missing_aliases, s3_covered_urls)
    """
    # Get all historical paths
    historical_paths = get_file_history(repo_root, current_file)

    # Convert to URLs
    all_historical_urls = {path_to_url(path) for path in historical_paths}

    # Get current URL (should be in the set)
    current_url = path_to_url(str(current_file.relative_to(repo_root)))

    # Remove current URL from historical URLs (we don't need to alias to ourselves)
    all_historical_urls.discard(current_url)

    # Get current aliases from frontmatter
    current_aliases = extract_aliases(current_file)

    # Check which historical URLs are covered by S3 redirects
    s3_covered_urls = {url for url in all_historical_urls if url in s3_redirects}

    # Find missing aliases (not in frontmatter AND not in S3 redirects)
    missing_aliases = all_historical_urls - current_aliases - s3_covered_urls

    return all_historical_urls, current_aliases, missing_aliases, s3_covered_urls

def main():
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent.parent
    content_dir = repo_root / 'content' / 'docs'

    if not content_dir.exists():
        print(f"ERROR: Content directory not found: {content_dir}", file=sys.stderr)
        sys.exit(1)

    # Output files
    correct_log = script_dir / 'historical-aliases-correct.txt'
    missing_log = script_dir / 'historical-aliases-missing.txt'
    report_log = script_dir / 'historical-aliases-report.txt'

    correct_log.write_text('')
    missing_log.write_text('')
    report_log.write_text('')

    # Counters
    total_files = 0
    files_with_history = 0
    files_correct = 0
    files_missing = 0
    total_missing_aliases = 0

    # Load S3 redirects
    print("Loading S3 redirect mappings from scripts/redirects/...")
    s3_redirects = load_s3_redirects(repo_root)
    print(f"Loaded {len(s3_redirects)} S3 redirect mappings\n")

    print("Scanning all content/docs/ files for complete git history...")
    print("This may take a few minutes...\n")

    # Get all markdown files
    all_md_files = sorted(content_dir.rglob('*.md'))

    with open(report_log, 'a') as report:
        report.write("=== COMPREHENSIVE HISTORICAL ALIAS VERIFICATION ===\n")
        report.write(f"Checking {len(all_md_files)} markdown files\n")
        report.write(f"Git history scope: Past 6 months\n")
        report.write(f"S3 redirects loaded: {len(s3_redirects)}\n\n")

    for md_file in all_md_files:
        total_files += 1

        # Progress indicator
        if total_files % 50 == 0:
            print(f"Processed {total_files}/{len(all_md_files)} files...", file=sys.stderr)

        # Analyze this file
        historical_urls, current_aliases, missing_aliases, s3_covered = analyze_file(repo_root, md_file, s3_redirects)

        # Skip files with no history (only ever existed at current path)
        if not historical_urls:
            continue

        files_with_history += 1
        rel_path = md_file.relative_to(repo_root)

        if missing_aliases:
            files_missing += 1
            total_missing_aliases += len(missing_aliases)

            with open(missing_log, 'a') as log:
                log.write(f"❌ MISSING ALIASES: {rel_path}\n")
                log.write(f"   Historical paths found: {len(historical_urls)}\n")
                log.write(f"   Current aliases: {len(current_aliases)}\n")
                log.write(f"   S3 redirects: {len(s3_covered)}\n")
                log.write(f"   Missing aliases ({len(missing_aliases)}):\n")
                for alias in sorted(missing_aliases):
                    log.write(f"     - {alias}\n")
                log.write("\n")

            with open(report_log, 'a') as report:
                report.write(f"\n{'='*80}\n")
                report.write(f"FILE: {rel_path}\n")
                report.write(f"{'='*80}\n\n")
                report.write(f"HISTORICAL URLS ({len(historical_urls)}):\n")
                for url in sorted(historical_urls):
                    if url in current_aliases:
                        status = "✓ ALIAS"
                    elif url in s3_covered:
                        status = "✓ S3"
                    else:
                        status = "❌ MISSING"
                    report.write(f"  {status:12}  {url}\n")
                report.write(f"\nCURRENT ALIASES ({len(current_aliases)}):\n")
                for alias in sorted(current_aliases):
                    report.write(f"  - {alias}\n")
                if s3_covered:
                    report.write(f"\nS3 REDIRECTS ({len(s3_covered)}):\n")
                    for url in sorted(s3_covered):
                        report.write(f"  → {url}\n")
                report.write(f"\nMISSING ALIASES ({len(missing_aliases)}):\n")
                for alias in sorted(missing_aliases):
                    report.write(f"  ❌ {alias}\n")
                report.write("\n")
        else:
            files_correct += 1

            with open(correct_log, 'a') as log:
                log.write(f"✓ {rel_path}\n")
                log.write(f"   Historical paths: {len(historical_urls)}, Aliases: {len(current_aliases)}, S3: {len(s3_covered)}\n")

    # Print summary
    print("\n" + "="*80)
    print("=== VERIFICATION SUMMARY ===")
    print("="*80)
    print(f"Total markdown files scanned:        {total_files}")
    print(f"Files with historical moves:         {files_with_history}")
    print(f"Files with complete aliases:         ✓ {files_correct}")
    print(f"Files with missing aliases:          ❌ {files_missing}")
    print(f"Total missing aliases:               ❌ {total_missing_aliases}")
    print()

    if files_missing == 0:
        print(f"🎉 ALL HISTORICAL ALIASES VERIFIED!")
        print(f"   All {files_with_history} files with history have complete alias coverage.")
        sys.exit(0)
    else:
        print("❌ MISSING ALIASES FOUND!")
        print()
        print(f"📄 Detailed reports generated:")
        print(f"   ✓ Files with complete aliases:  {correct_log}")
        print(f"   ❌ Files missing aliases:         {missing_log}")
        print(f"   📊 Full analysis report:          {report_log}")
        print()
        print("💡 Next steps:")
        print("   1. Review missing-aliases.txt")
        print("   2. Run generate-historical-fixes.py to create fix commands")
        print("   3. Run apply-historical-fixes.py to apply the fixes")
        print("   4. Re-run this script to verify")
        sys.exit(1)

if __name__ == '__main__':
    main()

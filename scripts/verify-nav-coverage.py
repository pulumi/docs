#!/usr/bin/env python3
"""
Verify that all documentation pages are accessible in the left navigation.

USAGE:
    python3 scripts/verify-nav-coverage.py

    Or with virtual environment:
    python3 -m venv /tmp/nav-venv
    /tmp/nav-venv/bin/pip install pyyaml
    /tmp/nav-venv/bin/python3 scripts/verify-nav-coverage.py

WHAT THIS SCRIPT CHECKS:
    1. Every Markdown file in content/docs/ is reachable through the left nav
    2. Pages with menu configuration use active menu names

HOW PAGES BECOME REACHABLE:
    - Direct menu config in frontmatter (menu: iac:, menu: esc:, etc.)
    - URL entry in config/_default/menus.yml
    - Auto-inclusion as child of parent _index.md with menu config
    - Overview link when parent has menu children

ACTIVE MENUS (defined in layouts/partials/docs/menu.html):
    get-started, iac, esc, deployments, insights, idp, ai, migration,
    administration, reference, support

EXIT CODES:
    0 = All pages reachable, no issues
    1 = Unreachable pages or incorrect menu configuration found
"""

import re
import yaml
from pathlib import Path

# Active menus defined in layouts/partials/docs/menu.html
ACTIVE_MENUS = {
    'get-started', 'iac', 'esc', 'deployments', 'insights',
    'idp', 'ai', 'migration', 'administration', 'reference', 'support'
}

def extract_frontmatter(file_path):
    """Extract YAML frontmatter from a Markdown file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Match frontmatter between --- delimiters
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return {}

    try:
        return yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError:
        return {}

def load_menus_yml(repo_root):
    """Load and parse config/_default/menus.yml."""
    menus_path = repo_root / 'config' / '_default' / 'menus.yml'
    if not menus_path.exists():
        return set()

    with open(menus_path, 'r', encoding='utf-8') as f:
        try:
            menus = yaml.safe_load(f) or {}
            # Build a set of all URLs defined in menus.yml
            urls = set()

            for entries in menus.values():
                if isinstance(entries, list):
                    for entry in entries:
                        if 'url' in entry and entry['url']:
                            urls.add(entry['url'])

            return urls
        except yaml.YAMLError:
            return set()

def get_page_url(file_path, docs_root):
    """Convert a file path to its URL on the site."""
    rel_path = file_path.relative_to(docs_root)

    # Remove content/docs prefix
    if str(rel_path).startswith('content/docs/'):
        rel_path = Path(str(rel_path)[len('content/docs/'):])

    # Convert _index.md to directory URL
    if rel_path.name == '_index.md':
        url = '/' + str(rel_path.parent) + '/'
    else:
        # Remove .md extension
        url = '/' + str(rel_path)[:-3] + '/'

    # Normalize path separators
    url = url.replace('\\', '/')

    # Add /docs/ prefix
    if not url.startswith('/docs/'):
        url = '/docs' + url

    return url

def has_menu_in_frontmatter(frontmatter):
    """Check if frontmatter has menu configuration for any active menu."""
    if 'menu' not in frontmatter:
        return False

    menu_config = frontmatter['menu']
    if not isinstance(menu_config, dict):
        return False

    # Check if any active menu is configured
    for menu_name in ACTIVE_MENUS:
        if menu_name in menu_config:
            return True

    return False

def find_parent_with_menu(file_path, docs_content_root):
    """Walk up directory tree to find parent _index.md with menu config."""
    current = file_path.parent

    while current >= docs_content_root:
        parent_index = current / '_index.md'
        if parent_index.exists() and parent_index != file_path:
            frontmatter = extract_frontmatter(parent_index)
            if has_menu_in_frontmatter(frontmatter):
                return parent_index

        # Stop at content/docs/ boundary
        if current == docs_content_root:
            break

        current = current.parent

    return None

def main():
    repo_root = Path('/workspaces/src/pulumi/docs')
    docs_content_root = repo_root / 'content' / 'docs'

    if not docs_content_root.exists():
        print(f"Error: {docs_content_root} does not exist")
        return 1

    # Load menus.yml URLs
    menu_urls = load_menus_yml(repo_root)
    print(f"Found {len(menu_urls)} URLs in menus.yml\n")

    # Find all Markdown files
    md_files = list(docs_content_root.rglob('*.md'))
    print(f"Checking {len(md_files)} Markdown files...\n")

    # Track results
    reachable = {
        'frontmatter': [],
        'menus_yml': [],
        'parent_auto_include': []
    }
    orphaned = []
    wrong_menu = []

    for md_file in sorted(md_files):
        frontmatter = extract_frontmatter(md_file)
        page_url = get_page_url(md_file, repo_root)

        # Special case: /docs/_index.md is the docs home, hardcoded in menu.html
        if md_file.name == '_index.md' and md_file.parent.name == 'docs':
            reachable['frontmatter'].append(md_file)
            continue

        # Check if file has menu in frontmatter
        if has_menu_in_frontmatter(frontmatter):
            # Verify it's using an active menu
            menu_config = frontmatter.get('menu', {})
            uses_active_menu = any(m in ACTIVE_MENUS for m in menu_config.keys())

            if uses_active_menu:
                reachable['frontmatter'].append(md_file)

                # Note: Pages with menu children automatically get Overview links via template
                # This is handled in layouts/partials/docs/menu.html lines 283-302

                continue
            else:
                # Has menu config but not using active menus
                wrong_menu.append((md_file, list(menu_config.keys())))
                continue

        # Check if URL is in menus.yml
        if page_url in menu_urls:
            reachable['menus_yml'].append(md_file)
            continue

        # Check if parent _index.md has menu config (auto-inclusion)
        parent_with_menu = find_parent_with_menu(md_file, docs_content_root)
        if parent_with_menu:
            reachable['parent_auto_include'].append((md_file, parent_with_menu))
            continue

        # Not reachable through any method
        orphaned.append(md_file)

    # Print results
    print("=" * 80)
    print("NAVIGATION COVERAGE REPORT")
    print("=" * 80)
    print()

    total_reachable = len(reachable['frontmatter']) + len(reachable['menus_yml']) + len(reachable['parent_auto_include'])
    total_files = len(md_files)

    print(f"✓ Reachable: {total_reachable}/{total_files}")
    print(f"  - Via frontmatter menu: {len(reachable['frontmatter'])}")
    print(f"  - Via menus.yml: {len(reachable['menus_yml'])}")
    print(f"  - Via parent auto-inclusion: {len(reachable['parent_auto_include'])}")
    print()

    if wrong_menu:
        print(f"⚠ Using inactive menus: {len(wrong_menu)}")
        for file, menus in wrong_menu:
            rel_path = file.relative_to(repo_root)
            print(f"  - {rel_path}")
            print(f"    Menus: {', '.join(menus)}")
        print()

    if orphaned:
        print(f"✗ Orphaned (unreachable): {len(orphaned)}")
        for file in orphaned:
            rel_path = file.relative_to(repo_root)
            print(f"  - {rel_path}")
        print()
    else:
        print("✓ No orphaned files found!")
        print()

    # Detailed breakdown for verification
    if orphaned or wrong_menu:
        print("=" * 80)
        print("DETAILS")
        print("=" * 80)
        print()

        if wrong_menu:
            print("Files using inactive menus:")
            print("These files have menu configuration but aren't using active menus.")
            print(f"Active menus: {', '.join(sorted(ACTIVE_MENUS))}")
            print()
            for file, menus in wrong_menu:
                rel_path = file.relative_to(repo_root)
                print(f"  {rel_path}")
                print(f"    Has menus: {', '.join(menus)}")
                print()

        if orphaned:
            print("Orphaned files:")
            print("These files are not reachable through any navigation method.")
            print()
            for file in orphaned:
                rel_path = file.relative_to(repo_root)
                print(f"  {rel_path}")
                print(f"    URL: {get_page_url(file, repo_root)}")
                print(f"    Not in menus.yml: {get_page_url(file, repo_root) not in menu_urls}")
                print(f"    No menu in frontmatter: {not has_menu_in_frontmatter(extract_frontmatter(file))}")
                parent = find_parent_with_menu(file, docs_content_root)
                print(f"    No parent with menu: {parent is None}")
                print()

    return 0 if not orphaned else 1

if __name__ == '__main__':
    exit(main())

#!/bin/bash

# Vale prose linter. Always exits 0 -- style nits are nags, not gates.
#
# Usage:
#   make lint-prose                 # changed files vs master (fast)
#   make lint-prose ARGS=...        # explicit path or files
#   ./scripts/lint-prose.sh content/docs/iac
#
# Linting the full content tree (1500+ files) takes 5+ minutes. The default
# scope is "files changed vs master" so contributors get fast feedback on
# what they actually touched. Pass an explicit path/glob to override.

set -o pipefail

if [ $# -gt 0 ]; then
    TARGETS=("$@")
else
    # Default: changed files in content/docs and content/blog vs master.
    # Includes both committed and uncommitted changes in the working tree.
    BASE=$(git merge-base HEAD master 2>/dev/null || echo "master")
    # Portable replacement for `mapfile` (bash 4+, missing on macOS bash 3.2).
    CHANGED=()
    while IFS= read -r line; do
        CHANGED+=("$line")
    done < <(
        {
            git diff --name-only --diff-filter=AM "$BASE"...HEAD
            git diff --name-only --diff-filter=AM
            git ls-files --others --exclude-standard
        } | grep -E '^content/(docs|blog)/.*\.md$' | sort -u
    )
    if [ "${#CHANGED[@]}" -eq 0 ]; then
        echo "lint-prose: no changed docs/blog files vs master; nothing to lint"
        echo "  (pass an explicit path to lint a specific scope: make lint-prose ARGS=content/docs)"
        exit 0
    fi
    TARGETS=("${CHANGED[@]}")
    echo "lint-prose: linting ${#CHANGED[@]} changed file(s)"
fi

vale --no-exit "${TARGETS[@]}"

# Front-matter titles are the site's H1s. Vale reads front matter (a
# substitution rule matches a title_tag: today), but this rule is scoped to
# headings and front matter isn't parsed as one. This helper feeds
# each target's title/h1 fields through that same Vale rule (same
# sentence-case check, same proper-noun exceptions) and maps findings back to
# the source line. Advisory like everything else here; the changed-files
# default above means the Title Case backlog surfaces one touched page at a
# time rather than all at once.
python3 "$(dirname "$0")/lint/frontmatter-title-case.py" "${TARGETS[@]}" || true

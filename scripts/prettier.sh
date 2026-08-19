#!/bin/bash

# Runs prettier over the repository with an ignore list that unions
# .prettierignore with .gitignore.
#
# Prettier does not read .gitignore, and --ignore-path takes a single file on
# prettier 2.x, so every scratch file a workflow drops in the working tree has
# had to be listed in BOTH files. Miss the second one and `prettier --check .`
# reports an untracked artifact as a formatting error -- which is how the
# content-review re-gate fails lint on a PR whose content is clean, stranding it
# in draft. Unioning the two lists makes .gitignore sufficient on its own: if
# git ignores a file, prettier ignores it too, and a new runtime artifact needs
# exactly one entry rather than two.
#
# The union file has to live in the repo root: prettier resolves the patterns in
# --ignore-path relative to that file's directory, so a temp file elsewhere
# silently mismatches every path.
#
# Usage: ./scripts/prettier.sh --check . --cache

set -o errexit -o pipefail

cd "$(dirname "$0")/.."

ignore_file=".prettierignore.union"
trap 'rm -f "$ignore_file"' EXIT

{
    cat .prettierignore
    echo
    cat .gitignore
} >"$ignore_file"

yarn prettier "$@" --ignore-path "$ignore_file"

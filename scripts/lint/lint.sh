#!/bin/bash

set -o errexit -o pipefail

DEBUG=0

# Debug logging function
debug() {
    if [ -n "$DEBUG" ]; then
        echo "[DEBUG] $1"
    fi
}

# Determine mode based on environment
if [ -n "$BASE_BRANCH" ]; then
    MODE="gha"
    debug "Using base branch: $BASE_BRANCH"
else
    MODE="git"
    debug "Using git mode (no base branch)"
fi

# If in debug mode, show what files would be considered new
# if [ -n "$DEBUG" ]; then
#     debug "Preview of new files:"
#     yarn ts-node "./scripts/lint/find-markdown.ts" "$MODE" --show-all
# fi

# Function to run a command and store its exit code
run_step() {
    echo -e "\n=== Running: $1 ==="
    eval "$1"
    return $?
}

# Initialize error collection
markdownlint_exit=0
frontmatter_exit=0
prettier_exit=0

# Run all steps and collect exit codes
run_step "DEBUG=$DEBUG yarn ts-node './scripts/lint/markdownlint-runner.ts' '$MODE'" || markdownlint_exit=$?
run_step "DEBUG=$DEBUG yarn ts-node './scripts/lint/validate-frontmatter.ts' '$MODE'" || frontmatter_exit=$?
run_step "yarn prettier --check ." || prettier_exit=$?

# Report all failures at the end
failed=0
if [ $markdownlint_exit -ne 0 ]; then
    echo -e "\n❌ Markdown linting failed"
    failed=1
fi
if [ $frontmatter_exit -ne 0 ]; then
    echo -e "\n❌ Front matter validation failed"
    failed=1
fi
if [ $prettier_exit -ne 0 ]; then
    echo -e "\n❌ Prettier check failed"
    failed=1
fi

# Exit with failure if any step failed
if [ $failed -eq 1 ]; then
    exit 1
fi

echo -e "\n✅ All checks passed"

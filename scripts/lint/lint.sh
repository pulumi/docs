#!/bin/bash

set -o errexit -o pipefail

# Get script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

DEBUG=0

# Determine mode based on environment
if [ -n "$GITHUB_ACTIONS" ]; then
    MODE="gha"
else
    MODE="git"
fi

# Run markdown linting with debug flag
DEBUG=$DEBUG ts-node "$SCRIPT_DIR/markdownlint-runner.ts" "$MODE"

# Run front matter validation
DEBUG=$DEBUG ts-node "$SCRIPT_DIR/validate-frontmatter.ts" "$MODE"

# Run prettier
yarn prettier --check .

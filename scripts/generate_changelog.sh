#!/bin/bash
# Usage: generate-changelog <from-git-tag> <to-git-tag> [--all-prs] [--tab-output]
# Writes changelog to standard output

# Prerequisites: Set environment variable GITHUB_TOKEN
# For now, globally install https://github.com/lindydonna/github-pr-changelog 
# by cloning the repo and running `npm i -g`
# In the future, will publish the tool to NPM, so that this script can use a local version

set -o nounset -o errexit -o pipefail

LAUNCH_DIR="${PWD}"

TOOLS_REPOS="pulumi,pulumi-cloud,pulumi-aws,pulumi-terraform,pulumi-azure"

echo -e "\033[0;95m+++ Generating changelog for repos pulumi/{${TOOLS_REPOS}} +++\033[0m" 

gh-changelog \
    --owner pulumi --repos "${TOOLS_REPOS}" \
    --git-directory "${LAUNCH_DIR}/../" \
    --from "${1}" --to "${2}" \
    "${3:-}" "${4:-}" 

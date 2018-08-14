#!/bin/bash
# Usage: generate-changelog <from-git-tag> <to-git-tag> [--all-prs] [--tab-output]
# Writes changelog to standard output

# Prerequisites: Set environment variable GITHUB_TOKEN
# For now, globally install https://github.com/lindydonna/github-pr-changelog 
# by cloning the repo and running `npm i -g`
# In the future, will publish the tool to NPM, so that this script can use a local version

set -o nounset -o errexit -o pipefail

if [ -z "${1:-}" ] || [ -z "${2:-}" ]; then
    echo "Missing required arguments."
    echo "Usage: generate-changelog <from-git-tag> <to-git-tag> [--all-prs] [--tab-output]"
    exit 1
fi

# not currently used, will add back when gh-changelog is moved to a locally installed package
SCRIPT_DIR="$( cd "$( dirname "$0" )" && pwd )"

TOOLS_REPOS="pulumi,pulumi-cloud,pulumi-aws,pulumi-terraform,pulumi-azure,pulumi-kubernetes,pulumi-aws-serverless,pulumi-aws-infra,pulumi-gcp,pulumi-azure-serverless,pulumi-docker"

gh-changelog \
    --owner pulumi --repos "${TOOLS_REPOS}" \
    --git-directory "../" \
    --from "${1}" --to "${2}" \
    "${3:-}" "${4:-}" 

#!/bin/bash
# Usage: generate-changelog <from-git-tag> <to-git-tag> [--all-prs] [--tab-output]

# Prerequisites: Set environment variable GITHUB_TOKEN

set -o nounset -o errexit -o pipefail

LAUNCH_DIR="${PWD}"

# Change to the directory of the bash script (so this can be run from any directory)
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "${SCRIPT_DIR}"

# Create temp directory for changelogs
# PULUMI_CHANGELOGS=`mktemp -d`

TOOLS_REPOS=(
    "pulumi"
    "pulumi-aws"
    "pulumi-azure"
    "pulumi-cloud"
    "pulumi-terraform"
    # # "terraform"
    # # "terraform-provider-aws"
    # # "terraform-provider-azurerm"
    # # "terraform-provider-github"
    # # "terraform-provider-kubernetes"
)

# SERVICE_REPOS=(
#     "pulumi-ppc"
#     "pulumi-service"
# )

for repo in "${TOOLS_REPOS[@]}"
do
    echo -e "\033[0;95m--- Updating repo pulumi/${repo} ---\033[0m" 
    pushd "${LAUNCH_DIR}"
    cd "../${repo}"
    git checkout master; git pull origin master
    popd
done

CHANGELOG_FILE="${LAUNCH_DIR}/${2}.changelog"
rm -f -- "${CHANGELOG_FILE}"  # -f is used in case the file doesn't exist

for repo in "${TOOLS_REPOS[@]}"
do
    echo -e "\033[0;95m+++ Generating changelog for repo pulumi/${repo} +++\033[0m" 
    cd "${SCRIPT_DIR}"
    node bin/cli.js \
        --owner pulumi --repo "${repo}" \
        --git-directory "${LAUNCH_DIR}/../${repo}" \
        --from "${1}" --to "${2}" \
        "${3:-}" "${4:-}" >> "${CHANGELOG_FILE}"
done

echo "Changelog written to ${CHANGELOG_FILE}"

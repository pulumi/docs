#!/bin/bash
# Usage: update_repos

set -o nounset -o errexit -o pipefail

TOOLS_REPOS=(
    "pulumi"
    "pulumi-aws"
    "pulumi-aws-infra"
    "pulumi-aws-serverless"
    "pulumi-azure"
    "pulumi-cloud"
    "pulumi-docker"
    "pulumi-eks"
    "pulumi-gcp"
    "pulumi-kubernetes"
    "pulumi-openstack"
    "pulumi-random"
    "pulumi-terraform"
    "pulumi-vsphere"
)

for repo in "${TOOLS_REPOS[@]}"
do
    echo -e "\033[0;95m--- Updating repo pulumi/${repo} ---\033[0m"
    pushd . >/dev/null 2>&1
    cd "../${repo}"
    echo -e "\033[0;93mPulling changes\033[0m"
    git checkout master >/dev/null
    git pull origin master >/dev/null
    git fetch --tags >/dev/null
    echo -e "\033[0;93mChecking out latest release\033[0m"
    LATEST_RELEASE=$(git describe --tags `git rev-list --max-count=1 --tags --not --tags='*-dev'`)
    git -c advice.detachedHead=false checkout $LATEST_RELEASE >/dev/null
    echo -e "\033[0;96m$LATEST_RELEASE\033[0m"
    popd . >/dev/null 2>&1
done

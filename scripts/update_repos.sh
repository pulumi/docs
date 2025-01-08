#!/bin/bash
# Usage: update_repos

set -o nounset -o errexit -o pipefail

REPO_OVERRIDE=${1:-}

TOOLS_REPOS=(
    "pulumi"
    "pulumi-awsx"
    "pulumi-cloud"
    "pulumi-kubernetesx"
    "pulumi-policy"
    "pulumi-terraform"
    "esc-sdk"
)

update_repo() {
    repo=$1
    echo -e "\033[0;95m--- Updating repo pulumi/${repo} ---\033[0m"
    pushd . >/dev/null 2>&1
    mkdir -p "../${repo}" && cd "../${repo}"
    git remote -v || git clone "git@github.com:pulumi/${repo}.git" .
    echo -e "\033[0;93mPulling changes\033[0m"
    default_branch=$(git symbolic-ref refs/remotes/origin/HEAD | cut -d'/' -f4)
    git checkout ${default_branch} >/dev/null
    git pull origin ${default_branch} >/dev/null
    git fetch --tags >/dev/null
    echo -e "\033[0;93mChecking out latest release\033[0m"
    LATEST_RELEASE=$(git describe --tags `git rev-list --max-count=1 --tags --not --tags='*-dev'`)
    git -c advice.detachedHead=false checkout $LATEST_RELEASE >/dev/null
    echo -e "\033[0;96m$LATEST_RELEASE\033[0m"
    popd >/dev/null 2>&1
}

if [ -z "${REPO_OVERRIDE:-}" ]; then
    for repo in "${TOOLS_REPOS[@]}"
    do
        update_repo ${repo}
    done
else
    update_repo ${REPO_OVERRIDE}
fi

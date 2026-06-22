#!/bin/bash
# Usage: update_repos

set -o nounset -o errexit -o pipefail

# Usage:
#   update_repos.sh                      # update all repos, checkout latest release
#   update_repos.sh <repo>               # update one repo, checkout latest release
#   update_repos.sh <repo> <tag>         # update one repo, checkout a specific tag
#                                        # (used by versioned-docs backfill to rebuild
#                                        #  docs at a historical version)
REPO_OVERRIDE=${1:-}
TAG_OVERRIDE=${2:-}

TOOLS_REPOS=(
    "pulumi"
    "pulumi-policy"
    "esc-sdk"
)

update_repo() {
    repo=$1
    requested_tag=${2:-}
    echo -e "\033[0;95m--- Updating repo pulumi/${repo} ---\033[0m"
    pushd . >/dev/null 2>&1
    mkdir -p "../${repo}" && cd "../${repo}"
    git remote -v || git clone "git@github.com:pulumi/${repo}.git" .
    echo -e "\033[0;93mPulling changes\033[0m"
    default_branch=$(git symbolic-ref refs/remotes/origin/HEAD | cut -d'/' -f4)
    git checkout ${default_branch} >/dev/null
    git pull origin ${default_branch} >/dev/null
    git fetch --tags >/dev/null
    if [ -n "${requested_tag}" ]; then
        echo -e "\033[0;93mChecking out requested tag ${requested_tag}\033[0m"
        CHECKOUT_REF="${requested_tag}"
    else
        echo -e "\033[0;93mChecking out latest release\033[0m"
        CHECKOUT_REF=$(git describe --tags `git rev-list --max-count=1 --tags --not --tags='*-dev'`)
    fi
    git -c advice.detachedHead=false checkout "${CHECKOUT_REF}" >/dev/null
    echo -e "\033[0;96m${CHECKOUT_REF}\033[0m"
    popd >/dev/null 2>&1
}

if [ -z "${REPO_OVERRIDE:-}" ]; then
    for repo in "${TOOLS_REPOS[@]}"
    do
        update_repo ${repo}
    done
else
    update_repo "${REPO_OVERRIDE}" "${TAG_OVERRIDE}"
fi

#!/bin/bash
# Usage: update_repos

set -o nounset -o errexit -o pipefail

# Usage:
#   update_repos.sh                      # update all repos, checkout latest release
#   update_repos.sh <repo>               # update one repo, checkout latest release
#   update_repos.sh <repo> <tag>         # update one repo, checkout a specific tag
#                                        # (used by versioned-docs backfill to rebuild
#                                        #  docs at a historical version)
#   update_repos.sh pulumi-service       # clone or update pulumi-service on its default
#                                        # branch, for make generate-feature-parity
REPO_OVERRIDE=${1:-}
TAG_OVERRIDE=${2:-}

TOOLS_REPOS=(
    "pulumi"
    "pulumi-policy"
    "esc-sdk"
    "pulumi-cloud-sdk"
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

# pulumi-service is private, and often a clone someone works in, so it's only
# updated when asked for by name. It tracks its default branch, not a release,
# and a clone that's dirty or on another branch is left alone.
update_pulumi_service() {
    echo -e "\033[0;95m--- Updating repo pulumi/pulumi-service ---\033[0m"
    pushd . >/dev/null 2>&1
    if [ ! -d ../pulumi-service/.git ]; then
        echo -e "\033[0;93mCloning repository (needs access to the private repo)...\033[0m"
        git clone "git@github.com:pulumi/pulumi-service.git" ../pulumi-service
        cd ../pulumi-service
    else
        cd ../pulumi-service
        default_branch=$(git symbolic-ref refs/remotes/origin/HEAD | cut -d'/' -f4)
        if [ -n "$(git status --porcelain)" ] || [ "$(git branch --show-current)" != "${default_branch}" ]; then
            echo -e "\033[0;93mSkipping: ../pulumi-service has local changes or isn't on ${default_branch}. Set PULUMI_SERVICE_REPO to use another clone.\033[0m"
            popd >/dev/null 2>&1
            return 0
        fi
        git pull origin "${default_branch}" >/dev/null
    fi
    echo -e "\033[0;96m$(git branch --show-current) @ $(git rev-parse --short HEAD)\033[0m"
    popd >/dev/null 2>&1
}

if [ "${REPO_OVERRIDE:-}" = "pulumi-service" ]; then
    update_pulumi_service
elif [ -z "${REPO_OVERRIDE:-}" ]; then
    for repo in "${TOOLS_REPOS[@]}"
    do
        update_repo ${repo}
    done
else
    update_repo "${REPO_OVERRIDE}" "${TAG_OVERRIDE}"
fi

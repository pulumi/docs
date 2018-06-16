#!/bin/bash
# Usage: update_repos 

set -o nounset -o errexit -o pipefail

TOOLS_REPOS=(
    "pulumi"
    "pulumi-aws"
    "pulumi-azure"
    "pulumi-cloud"
    "pulumi-terraform"
    "pulumi-kubernetes"
    "pulumi-aws-serverless"
    "pulumi-aws-infra"
    "pulumi-gcp"
)

for repo in "${TOOLS_REPOS[@]}"
do
    echo -e "\033[0;95m--- Updating repo pulumi/${repo} ---\033[0m" 
    pushd .
    cd "../${repo}"
    git checkout master; git pull origin master; git fetch --tags
    popd
done

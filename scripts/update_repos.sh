#!/bin/bash
# Usage: update_repos 

set -o nounset -o errexit -o pipefail

TOOLS_REPOS=(
    "eks"
    "pulumi"
    "pulumi-aws"
    "pulumi-aws-infra"
    "pulumi-aws-serverless"
    "pulumi-azure"
    "pulumi-cloud"
    "pulumi-docker"
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
    pushd .
    cd "../${repo}"
    git checkout master; git pull origin master; git fetch --tags
    popd
done

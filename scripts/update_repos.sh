#!/bin/bash
# Usage: update_repos

set -o nounset -o errexit -o pipefail

REPO_OVERRIDE=${1:-}

TOOLS_REPOS=(
    "pulumi"
    "pulumi-aiven"
    "pulumi-alicloud"
    "pulumi-aws"
    "pulumi-awsx"
    "pulumi-azure"
    "pulumi-azuread"
    "pulumi-cloud"
    "pulumi-cloudamqp"
    "pulumi-cloudflare"
    "pulumi-consul"
    "pulumi-datadog"
    "pulumi-digitalocean"
    "pulumi-dnsimple"
    "pulumi-docker"
    "pulumi-eks"
    "pulumi-fastly"
    "pulumi-f5bigip"
    "pulumi-gcp"
    "pulumi-github"
    "pulumi-gitlab"
    "pulumi-kafka"
    "pulumi-keycloak"
    "pulumi-kubernetes"
    "pulumi-kubernetesx"
    "pulumi-linode"
    "pulumi-mailgun"
    "pulumi-mongodbatlas"
    "pulumi-mysql"
    "pulumi-newrelic"
    "pulumi-okta"
    "pulumi-openstack"
    "pulumi-packet"
    "pulumi-policy"
    "pulumi-postgresql"
    "pulumi-rabbitmq"
    "pulumi-rancher2"
    "pulumi-random"
    "pulumi-signalfx"
    "pulumi-spotinst"
    "pulumi-terraform"
    "pulumi-tls"
    "pulumi-vault"
    "pulumi-vsphere"
)

update_repo() {
    repo=$1
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

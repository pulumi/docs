#!/usr/bin/env bash

set -o errexit -o pipefail
set -x

# Optional argument to generate docs for just a single provider.
REPO_OVERRIDE="${1:-}"

PACKAGES=(
  "pulumi"
  "pulumi_aiven"
  "pulumi_alicloud"
  "pulumi_aws"
  "pulumi_azure"
  "pulumi_azuread"
  "pulumi_cloudamqp"
  "pulumi_cloudflare"
  "pulumi_consul"
  "pulumi_datadog"
  "pulumi_digitalocean"
  "pulumi_dnsimple"
  "pulumi_docker"
  "pulumi_fastly"
  "pulumi_f5bigip"
  "pulumi_gcp"
  "pulumi_github"
  "pulumi_gitlab"
  "pulumi_kafka"
  "pulumi_keycloak"
  "pulumi_kong"
  "pulumi_kubernetes"
  "pulumi_linode"
  "pulumi_mailgun"
  "pulumi_mongodbatlas"
  "pulumi_mysql"
  "pulumi_newrelic"
  "pulumi_okta"
  "pulumi_openstack"
  "pulumi_packet"
  "pulumi_policy"
  "pulumi_postgresql"
  "pulumi_rabbitmq"
  "pulumi_rancher2"
  "pulumi_random"
  "pulumi_signalfx"
  "pulumi_spotinst"
  "pulumi_terraform"
  "pulumi_tls"
  "pulumi_vault"
  "pulumi_vsphere"
)

pushd "tools/pydocgen"
pipenv --python 3
pipenv install

if [ -z "${REPO_OVERRIDE:-}" ]; then
    echo "Building all Python docs..."
    # Install the Python package for all the providers.
    for PACKAGE in "${PACKAGES[@]}" ; do \
        pipenv run pip install "${PACKAGE}"
    done

    # Run the pydocgen to generate the docs for all the packages.
    pipenv run python -m pydocgen "../../content/docs/reference/pkg"
else
    # Install the Python package and run the pydocgen tool for just the provider that
    # was requested.
    echo "Building Python docs for ${REPO_OVERRIDE}..."
    if [ "${REPO_OVERRIDE}" = "pulumi" ]; then
      PACKAGE="${REPO_OVERRIDE}"
    else
      PACKAGE="pulumi_${REPO_OVERRIDE}"
    fi
    pipenv run pip install "${PACKAGE}"
    pipenv run python -m pydocgen "../../content/docs/reference/pkg" "${PACKAGE}"
fi

popd

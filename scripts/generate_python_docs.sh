#!/usr/bin/env bash

set -o errexit -o pipefail
set -x

PACKAGES=(
  "pulumi"
  "pulumi_aws"
  "pulumi_azure"
  "pulumi_azuread"
  "pulumi_cloudflare"
  "pulumi_datadog"
  "pulumi_digitalocean"
  "pulumi_dnsimple"
  "pulumi_docker"
  "pulumi_f5bigip"
  "pulumi_gcp"
  "pulumi_gitlab"
  "pulumi_kafka"
  "pulumi_kubernetes"
  "pulumi_linode"
  "pulumi_mysql"
  "pulumi_newrelic"
  "pulumi_openstack"
  "pulumi_packet"
  "pulumi_postgresql"
  "pulumi_random"
  "pulumi_terraform"
  "pulumi_tls"
  "pulumi_vault"
  "pulumi_vsphere"
)

run_pydocgen() {
  pushd "tools/pydocgen"
  pipenv --python 3
  pipenv install
  for pkg in "${PACKAGES[@]}"; do
    pipenv run pip install "${pkg}"
  done
  pipenv run python -m pydocgen "../../content/docs/reference/pkg"
  popd
}

run_pydocgen

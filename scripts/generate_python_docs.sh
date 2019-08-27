#!/usr/bin/env bash

set -o errexit -o pipefail
set -x

PACKAGES=(
  "pulumi==1.0.0b4"
  "pulumi_aws==1.0.0b3"
  "pulumi_azure==1.0.0b2"
  "pulumi_azuread==1.0.0b2"
  "pulumi_cloudflare"
  "pulumi_datadog"
  "pulumi_digitalocean"
  "pulumi_dnsimple"
  "pulumi_f5bigip"
  "pulumi_gcp"
  "pulumi_gitlab"
  "pulumi_kubernetes==1.0.0b2"
  "pulumi_linode"
  "pulumi_mysql"
  "pulumi_newrelic"
  "pulumi_openstack"
  "pulumi_packet"
  "pulumi_postgresql"
  "pulumi_random==1.0.0b2"
  "pulumi_tls"
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

#!/usr/bin/env bash

set -o errexit -o pipefail
set -x

PACKAGES=(
  "pulumi"
  "pulumi_aws"
  "pulumi_azure"
  "pulumi_azuread"
  "pulumi_cloudflare"
  "pulumi_digitalocean"
  "pulumi_f5bigip"
  "pulumi_gcp"
  "pulumi_kubernetes"
  "pulumi_linode"
  "pulumi_mysql"
  "pulumi_newrelic"
  "pulumi_openstack"
  "pulumi_packet"
  "pulumi_random"
  "pulumi_vsphere"
)

run_pydocgen() {
  pushd "tools/pydocgen"
  pipenv --python 3
  pipenv install
  for pkg in "${PACKAGES[@]}"; do
    pipenv run pip install --pre "${pkg}"
  done
  pipenv run python -m pydocgen "../../content/reference/pkg"
  popd
}

run_pydocgen

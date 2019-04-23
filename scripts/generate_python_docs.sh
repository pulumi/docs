#!/usr/bin/env bash

set -o errexit -o pipefail
set -x

PACKAGES=(
  "pulumi"
  "pulumi_aws"
  "pulumi_azure"
  "pulumi_cloudflare"
  "pulumi_gcp"
  "pulumi_random"
  "pulumi_vsphere"
  "pulumi_openstack"
  "pulumi_f5bigip"
  "pulumi_packet"
  "pulumi_kubernetes"
)

run_pydocgen() {
  pushd "tools/pydocgen"
  pipenv --python 3
  pipenv install
  for pkg in "${PACKAGES[@]}"; do
    pipenv run pip install --pre "${pkg}"
  done
  pipenv run python -m pydocgen "../../reference/pkg"
  popd
}

run_pydocgen

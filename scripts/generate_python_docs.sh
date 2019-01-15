#!/bin/bash

set -o errexit -o pipefail
set -x

PACKAGES=(
  "pulumi_aws"
  "pulumi_azure"
  "pulumi_gcp"
  "pulumi_random"
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

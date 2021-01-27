#!/usr/bin/env bash

set -o errexit -o pipefail
set -x

# Optional argument to generate docs for just a single provider.
REPO_OVERRIDE="${1:-}"

PACKAGES=(
  "pulumi"
  "pulumi_policy"
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
    PACKAGE="pulumi"
    if [ "${REPO_OVERRIDE}" != "pulumi" ]; then
        PACKAGE="pulumi_${REPO_OVERRIDE}"
    fi
    pipenv run pip install "${PACKAGE}"
    pipenv run python -m pydocgen "../../content/docs/reference/pkg" "${PACKAGE}"
fi

popd

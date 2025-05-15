#!/usr/bin/env bash

set -o errexit -o pipefail
set -x

PACKAGES=(
  "pulumi"
  "pulumi_policy"
  "pulumi_terraform"
  "pulumi_esc_sdk"
)

OUTDIR="../../static-prebuilt/docs/reference/pkg/python"

pushd "tools/pydocgen"

pipenv --python 3
pipenv install
pipenv run pip install sphinx-rtd-theme

echo "Building all Python docs..."
# Install each package.
for PACKAGE in "${PACKAGES[@]}" ; do \
    pipenv run pip install --upgrade "${PACKAGE}"
done

rm -rf "$OUTDIR"
pipenv run sphinx-build -j auto -b dirhtml ./source "$OUTDIR"

popd

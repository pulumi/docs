#!/usr/bin/env bash

# Builds Sphinx HTML docs for a single Pulumi Python SDK package as an
# independent docset and writes the output to
# static-prebuilt/docs/reference/pkg/python/${PACKAGE}/.
#
# Each package has its own sphinx source dir under tools/pydocgen/source/<pkg>/
# with its own conf.py and index.rst, so per-package builds don't affect each
# other's output.
#
# Required env:
#   PACKAGE  one of: pulumi, pulumi_policy, pulumi_esc_sdk
#
# Optional env:
#   VERSION  pin the primary package ($PACKAGE) to this exact version instead of
#            installing the latest. Used by versioned-docs backfill to rebuild docs at
#            a historical release. Dependencies (e.g. pulumi for pulumi_policy) still
#            install latest. Unset = current behavior (install latest of everything).

set -o errexit -o pipefail
set -x

PACKAGE="${PACKAGE:?Set PACKAGE to one of: pulumi, pulumi_policy, pulumi_esc_sdk}"

case "$PACKAGE" in
  pulumi)         INSTALL=("pulumi") ;;
  pulumi_policy)  INSTALL=("pulumi" "pulumi_policy") ;;
  pulumi_esc_sdk) INSTALL=("pulumi_esc_sdk") ;;
  *)
    echo "Unknown PACKAGE: $PACKAGE (expected: pulumi, pulumi_policy, pulumi_esc_sdk)" >&2
    exit 1
    ;;
esac

SOURCE_DIR="./source/${PACKAGE}"
OUTDIR="../../static-prebuilt/docs/reference/pkg/python/${PACKAGE}"

pushd "tools/pydocgen"

pipenv --python 3
pipenv install
pipenv run pip install sphinx-rtd-theme

echo "Installing packages for ${PACKAGE} docs build: ${INSTALL[*]}"
for p in "${INSTALL[@]}" ; do
    if [ -n "${VERSION:-}" ] && [ "${p}" = "${PACKAGE}" ]; then
        echo "Pinning primary package ${p}==${VERSION}"
        pipenv run pip install "${p}==${VERSION}"
    else
        pipenv run pip install --upgrade "${p}"
    fi
done

mkdir -p "$(dirname "$OUTDIR")"
rm -rf "${OUTDIR}"
pipenv run sphinx-build -j auto -b dirhtml "$SOURCE_DIR" "$OUTDIR"

popd

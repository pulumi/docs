#!/usr/bin/env bash

# Builds Sphinx HTML docs for a single Pulumi Python SDK package and atomically
# replaces only that package's subdirectory under
# static-prebuilt/docs/reference/pkg/python/<package>.
#
# Required env:
#   PACKAGE  one of: pulumi, pulumi_policy, pulumi_esc_sdk
#
# Output:
#   ../../static-prebuilt/docs/reference/pkg/python/${PACKAGE}/

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

OUTDIR="../../static-prebuilt/docs/reference/pkg/python"

pushd "tools/pydocgen"

pipenv --python 3
pipenv install
pipenv run pip install sphinx-rtd-theme

echo "Installing packages for ${PACKAGE} docs build: ${INSTALL[*]}"
for p in "${INSTALL[@]}" ; do
    pipenv run pip install --upgrade "${p}"
done

TMP_SRC=$(mktemp -d)
TMP_OUT=$(mktemp -d)
trap 'rm -rf "$TMP_SRC" "$TMP_OUT"' EXIT

cp source/conf.py "$TMP_SRC/"
cp "source/${PACKAGE}.rst" "$TMP_SRC/"

underline=$(printf '=%.0s' $(seq 1 ${#PACKAGE}))
cat > "$TMP_SRC/index.rst" <<EOF
${PACKAGE}
${underline}

.. toctree::
    ${PACKAGE}
EOF

pipenv run sphinx-build -j auto -b dirhtml "$TMP_SRC" "$TMP_OUT"

mkdir -p "$OUTDIR"
rm -rf "${OUTDIR:?}/${PACKAGE}"
cp -r "$TMP_OUT/${PACKAGE}" "$OUTDIR/${PACKAGE}"

popd

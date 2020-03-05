#!/bin/bash
set -o nounset -o errexit -o pipefail

PACKDIR="./content/docs/reference/providers"
ABSOLUTEPACKDIR="$(pwd)/content/docs/reference/providers"

echo "Generating docs templates bundle in pulumi/pulumi"
pushd ../pulumi
make generate
popd

for PROVIDER in "aws" ; do \
    echo "Removing the ${PACKDIR}/${PROVIDER} dir..."
    rm -rf "${PACKDIR}/${PROVIDER}"

    TFGEN=pulumi-tfgen-${PROVIDER}
    pushd ../pulumi-${PROVIDER}
    make provider && make tfgen && make install_plugins

    echo "Running ${TFGEN}... for docs"
    ${TFGEN} docs --overlays overlays/docs --out ${ABSOLUTEPACKDIR}/${PROVIDER} || exit 3
    popd

    echo "Done generating resource docs for ${PROVIDER}"
    echo ""
done
#!/bin/bash
set -o nounset -o errexit -o pipefail

PACKDIR="./content/docs/reference/providers"
ABSOLUTEPACKDIR="$(pwd)/content/docs/reference/providers"
TOOL_APIDOCGEN="go run ./tools/resourcedocsgen/*.go"

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

    echo "Running ${TFGEN} to generate provider schema..."
    ${TFGEN} schema --out ${ABSOLUTEPACKDIR}/${PROVIDER}/schema.json || exit 3

    popd

    echo "Running docs generator from schema..."
    ${TOOL_APIDOCGEN} ${ABSOLUTEPACKDIR}/${PROVIDER} ${ABSOLUTEPACKDIR}/${PROVIDER}/schema.json || exit 3

    rm ${ABSOLUTEPACKDIR}/${PROVIDER}/schema.json

    echo "Done generating resource docs for ${PROVIDER}\n"
done

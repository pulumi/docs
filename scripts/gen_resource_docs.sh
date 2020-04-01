#!/bin/bash
# A script that facilitates generating resource docs using the tools/resourcedocsgen Go-based
# tool. This script optionally allows passing the provider name (without the "pulumi-" prefix.)

set -o nounset -o errexit -o pipefail

REPO_OVERRIDE=${1:-}

PACKDIR="./content/docs/reference/pkg"
ABSOLUTEPACKDIR="$(pwd)/content/docs/reference/pkg"
TOOL_RESDOCGEN="go run ./tools/resourcedocsgen/*.go -logtostderr"

PROVIDERS=(
    "aws"
    "azure"
    "azuread"
    "gcp"
)

echo "Generating docs templates bundle in pulumi/pulumi"
pushd ../pulumi
make generate
popd

generate_docs() {
    provider=$1
    ./scripts/update_repos.sh "pulumi-${provider}"

    echo "Removing the ${PACKDIR}/${provider} dir..."
    rm -rf "${PACKDIR}/${provider}"

    TFGEN=pulumi-tfgen-${provider}

    pushd ../pulumi-${provider}
    echo "Running pulumi-tfgen-${TFGEN} to generate provider schema..."
    make generate_schema
    popd

    if [ $provider = "kubernetes" ]; then
        SCHEMA_FILE="../pulumi-${provider}/sdk/schema/schema.json"
    else
        SCHEMA_FILE="../pulumi-${provider}/provider/cmd/pulumi-resource-${provider}/schema.json"
    fi

    echo "Running docs generator from schema for ${provider}..."
    ${TOOL_RESDOCGEN} ${ABSOLUTEPACKDIR}/${provider} ${SCHEMA_FILE} || exit 3

    echo "Done generating resource docs for ${provider}"
    echo ""
}

if [ -z "${REPO_OVERRIDE:-}" ]; then
    for PROVIDER in "${PROVIDERS[@]}" ; do \
        generate_docs $PROVIDER
    done
else
    generate_docs ${REPO_OVERRIDE}
fi
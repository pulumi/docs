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

    # Checkout the latest branch of the provider repo, rather than
    # using the update_repos script. This is only temporary until
    # 2.0 is GA.
    # ./scripts/update_repos.sh "pulumi-${provider}"

    echo -e "\033[0;95m--- Updating repo pulumi/pulumi-${provider} ---\033[0m"
    pushd "../pulumi-${provider}"
    echo -e "\033[0;93mPulling changes\033[0m"
    git checkout master >/dev/null
    git pull origin master >/dev/null
    popd

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
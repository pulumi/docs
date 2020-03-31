#!/bin/bash
set -o nounset -o errexit -o pipefail

PACKDIR="./content/docs/reference/pkg"
ABSOLUTEPACKDIR="$(pwd)/content/docs/reference/pkg"
TOOL_RESDOCGEN="go run ./tools/resourcedocsgen/*.go -v=3 -logtostderr"

PROVIDERS=(
    "kubernetes"
)

echo "Generating docs templates bundle in pulumi/pulumi"
pushd ../pulumi
make generate
popd

for PROVIDER in "${PROVIDERS[@]}" ; do \
    # ./scripts/update_repos.sh "pulumi-${PROVIDER}"

    echo "Removing the ${PACKDIR}/${PROVIDER} dir..."
    rm -rf "${PACKDIR}/${PROVIDER}"

    TFGEN=pulumi-tfgen-${PROVIDER}

    #pushd ../pulumi-${PROVIDER}
    #echo "Running pulumi-tfgen-${TFGEN} to generate provider schema..."
    #make generate_schema
    #popd

    if [ $PROVIDER = "kubernetes" ]; then
        SCHEMA_FILE="../pulumi-${PROVIDER}/sdk/schema/schema.json"
    else
        SCHEMA_FILE="../pulumi-${PROVIDER}/provider/cmd/pulumi-resource-${PROVIDER}/schema.json"
    fi

    echo "Running docs generator from schema for ${PROVIDER}..."
    ${TOOL_RESDOCGEN} ${ABSOLUTEPACKDIR}/${PROVIDER} ${SCHEMA_FILE} || exit 3

    echo "Done generating resource docs for ${PROVIDER}"
    echo ""
done

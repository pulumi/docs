#!/bin/bash
set -o nounset -o errexit -o pipefail

PACKDIR="./content/docs/reference/pkg"
ABSOLUTEPACKDIR="$(pwd)/content/docs/reference/pkg"
TOOL_APIDOCGEN="go run ./tools/resourcedocsgen/*.go"

TOOLS_REPOS=(
    "pulumi-aws"
    "pulumi-azure"
    "pulumi-azuread"
    "pulumi-gcp"
)

for repo in "${TOOLS_REPOS[@]}"
do
    ./scripts/update_repos.sh ${repo}
done

echo "Generating docs templates bundle in pulumi/pulumi"
pushd ../pulumi
make generate
popd

for PROVIDER in "aws" "azure" "azuread" "gcp" ; do \
    echo "Removing the ${PACKDIR}/${PROVIDER} dir..."
    rm -rf "${PACKDIR}/${PROVIDER}"

    echo "Running docs generator from schema for ${PROVIDER}..."
    ${TOOL_APIDOCGEN} ${ABSOLUTEPACKDIR}/${PROVIDER} ../pulumi-${PROVIDER}/cmd/pulumi-resource-${PROVIDER}/schema.json || exit 3

    echo "Done generating resource docs for ${PROVIDER}"
    echo ""
done

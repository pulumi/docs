#!/bin/bash
# A script that facilitates generating resource docs using the tools/resourcedocsgen Go-based
# tool. This script optionally allows passing the provider name (without the "pulumi-" prefix.)

set -o nounset -o errexit -o pipefail

# The first argument is the override for the repo for which this script will generate the resource docs. 
REPO_OVERRIDE=${1:-}
# Pass a 2nd argument (value does not matter) to indicate that the resource plugin must be installed.
# The latest release tag (not beta or dev) is used as the version to install the plugin. 
INSTALL_RESOURCE_PLUGIN=${2:-}
# Pass a 3rd argument to override the resource plugin version installed by this script.
INSTALL_RESOURCE_PLUGIN_VERSION=${3:-}

PACKDIR="./content/docs/reference/pkg"
ABSOLUTEPACKDIR="$(pwd)/content/docs/reference/pkg"
TOOL_RESDOCGEN="./tools/resourcedocsgen/"

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

    echo -e "\033[0;95m--- Updating repo pulumi/pulumi-${provider} ---\033[0m"
    pushd "../pulumi-${provider}"
    git fetch --tags

    plugin_version=$(git describe --tags "$(git rev-list --max-count=1 --tags --not --tags='*-dev')")
    # If a plugin version was passed, then use that.
    # The provider repo will also be checked out at that version below.
    if [ -n "${INSTALL_RESOURCE_PLUGIN_VERSION:-}" ]; then
        plugin_version=${INSTALL_RESOURCE_PLUGIN_VERSION}
    elif [[ ${plugin_version} = sdk* ]]; then
        plugin_version=${plugin_version:4}
    elif [[ ${plugin_version} = provider* ]]; then
        plugin_version=${plugin_version:9}
    fi

    echo -e "\033[0;93mCheckout pulumi/pulumi-${provider} at tag $plugin_version\033[0m"
    git -c advice.detachedHead=false checkout "$plugin_version" >/dev/null

    # Go back to the docs repo.
    popd

    EXISTING_SCHEMA_FILE="../pulumi-${provider}/provider/cmd/pulumi-resource-${provider}/schema.json"
    if [ "$provider" = "kubernetes" ]; then
        EXISTING_SCHEMA_FILE="../pulumi-kubernetes/sdk/schema/schema.json"
    fi

    # Use a previously generated schema.json file if it exists.
    if [ -f "${EXISTING_SCHEMA_FILE}" ]; then
        echo "Will use the previously generated schema.json for generating resource docs..."
    else
        echo "Could not find a previously generated schema.json file. Will generate schema..."

        if [ -n "${INSTALL_RESOURCE_PLUGIN:-}" ]; then
            echo "Installing resource plugin for ${provider}. Version: ${plugin_version}"
            pulumi plugin install resource "${provider}" "${plugin_version}"
        fi

        pushd "../pulumi-${provider}"
        make generate_schema
        popd
    fi

    if [ "$provider" = "kubernetes" ]; then
        SCHEMA_FILE="../../../pulumi-kubernetes/sdk/schema/schema.json"
    else
        SCHEMA_FILE="../../../pulumi-${provider}/provider/cmd/pulumi-resource-${provider}/schema.json"
    fi

    OVERLAY_SCHEMA_FILE=""
    if [ -d "${TOOL_RESDOCGEN}/overlays/${provider}" ] && [ -f "${TOOL_RESDOCGEN}/overlays/${provider}/overlays.json" ]; then
        echo "Found an overlay file for ${provider}..."
        OVERLAY_SCHEMA_FILE="./overlays/${provider}/overlays.json"
    fi

    echo "Running docs generator from schema for ${provider}..."
    pushd ${TOOL_RESDOCGEN}
    go run . -logtostderr "${ABSOLUTEPACKDIR}/${provider}" "${SCHEMA_FILE}" "${plugin_version}" "${OVERLAY_SCHEMA_FILE}" || exit 3
    popd

    echo "Done generating resource docs for ${provider}"
    echo ""
}

if [ -z "${REPO_OVERRIDE:-}" ]; then
    for PROVIDER in "${PROVIDERS[@]}" ; do \
        generate_docs "$PROVIDER"
    done
else
    generate_docs "${REPO_OVERRIDE}"
fi

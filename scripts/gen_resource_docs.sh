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

    # Checkout the master branch of the provider repo, rather than
    # using the update_repos script. This is only temporary until
    # 2.0 is GA.
    # ./scripts/update_repos.sh "pulumi-${provider}"

    echo -e "\033[0;95m--- Updating repo pulumi/pulumi-${provider} ---\033[0m"
    pushd "../pulumi-${provider}"
    git fetch --tags

    if [ -n "${INSTALL_RESOURCE_PLUGIN:-}" ]; then
        # For the moment, choose only v1 tags, by default unless an override was provided.
        plugin_version=$(git describe --tags `git rev-list --max-count=1 --tags='v1*'`)
        if [ -n "${INSTALL_RESOURCE_PLUGIN_VERSION:-}" ]; then
            plugin_version=${INSTALL_RESOURCE_PLUGIN_VERSION}
        elif [[ ${plugin_version} = sdk* ]]; then
            plugin_version=${plugin_version:4}
        fi

        echo -e "\033[0;93mCheckout repo at tag $plugin_version\033[0m"
        git -c advice.detachedHead=false checkout $plugin_version >/dev/null

        echo "Installing resource plugin for ${provider}. Version: ${plugin_version}"
        pulumi plugin install resource ${provider} ${plugin_version}
    fi

    TFGEN=pulumi-tfgen-${provider}
    echo "Running pulumi-tfgen-${TFGEN} to generate provider schema..."
    make generate_schema
    popd

    if [ $provider = "kubernetes" ]; then
        SCHEMA_FILE="../../../pulumi-kubernetes/sdk/schema/schema.json"
        OVERLAY_SCHEMA_FILE="./overlays/kubernetes/overlays.json"
    else
        SCHEMA_FILE="../../../pulumi-${provider}/provider/cmd/pulumi-resource-${provider}/schema.json"
    fi

    echo "Removing the ${PACKDIR}/${provider} dir..."
    rm -rf "${PACKDIR}/${provider}"

    echo "Running docs generator from schema for ${provider}..."
    pushd ${TOOL_RESDOCGEN}
    go run . -logtostderr "${ABSOLUTEPACKDIR}/${provider}" "${SCHEMA_FILE}" "${OVERLAY_SCHEMA_FILE}" || exit 3
    popd

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

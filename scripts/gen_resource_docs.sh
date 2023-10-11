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
# Pass a non-empty string as the 4th arg to override the path to the Pulumi schema file.
# The path must start from the root of the package's repository.
# For example, if the schema is in the root of the package repo, then
# this value should be set to `/schema.json` (if using a JSON schema, .yaml otherwise)
# And if the schema is in a folder called provider, then this would be set to
# `/provider/schema.json` (or .yaml).
#
# If not set, the default location for the schema will be used which is
# /provider/cmd/pulumi-resource-${provider}/schema.[json|yaml].
SCHEMA_FILE_PATH=${4:-}

PACKDIR="content/registry/packages/"
ABSOLUTEPACKDIR="$(pwd)/$PACKDIR"
PACKAGE_TREE_OUT_DIR="../../static/registry/packages/navs"
TOOL_RESDOCGEN="./tools/resourcedocsgen/"

PROVIDERS=(
    "aws"
    "aws-native"
    "azure"
    "azure-native"
    "azuread"
    "gcp"
    "google-native"
)

echo "Generating docs templates bundle in pulumi/pulumi"
pushd ../pulumi
make generate
popd

source ./scripts/resource_docs_common.sh

generate_docs() {
    provider=$1
    repository="pulumi-${provider}"

    echo -e "\033[0;95m--- Updating repo pulumi/${repository} ---\033[0m"
    pushd "../${repository}"
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

    echo -e "\033[0;93mCheckout pulumi/${repository} at tag $plugin_version\033[0m"
    git -c advice.detachedHead=false checkout "$plugin_version" >/dev/null

    # Go back to the docs repo.
    popd

    EXISTING_SCHEMA_FILE=""
    # If the schema file path was overridden, then just use that.
    if [ -n "${SCHEMA_FILE_PATH:-}" ]; then
        EXISTING_SCHEMA_FILE="../${repository}${SCHEMA_FILE_PATH}"
        if [ ! -f "${EXISTING_SCHEMA_FILE}" ]; then
            echo "Pulumi schema file at path ${SCHEMA_FILE_PATH} does not exist."
            exit 1
        fi
    else
        EXISTING_SCHEMA_FILE=$(get_schema_file_path "${repository}" "${provider}")
    fi

    # This path should be relative to the tools/resourcedocsgen tool.
    SCHEMA_FILE="../../${EXISTING_SCHEMA_FILE}"

    echo "Running docs generator from schema for ${provider}..."

    resourcedocsgen docs \
      --docsOutDir "${ABSOLUTEPACKDIR}/${provider}/api-docs" \
      --schemaFile "${SCHEMA_FILE}" \
      --version "${plugin_version}" \
      --logtostderr \
      --packageTreeJSONOutDir "${PACKAGE_TREE_OUT_DIR}" || exit 3

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

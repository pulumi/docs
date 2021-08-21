#!/bin/bash

# A script that facilitates generating package metadata files using the tools/resourcedocsgen Go-based
# tool. This script optionally allows passing the provider name (without the "pulumi-" prefix.)

set -o nounset -o errexit -o pipefail

# The first argument is for the output dir (required).
METADATA_OUT_DIR=${1:-}
# The second argument is the override for the package for which this script will generate the metadata.
# Must not be passed without the "pulumi-" prefix.
REPO_OVERRIDE=${2:-}
# Pass a 3rd argument to override the package version used by this script.
VERSION=${3:-}

TOOL_RESDOCGEN="./tools/resourcedocsgen/"

# If the script is invoked without any arguments, then the script
# will generate metadata for these packages.
DEFAULT_PKGS=(
    "aws"
    "azure"
    "azure-native"
    "azuread"
    "gcp"
    "google-native"
)

featured_packages=(
  "aws"
  "azure-native"
  "google-native"
  "kubernetes"
)

generate_metadata() {
    provider=$1
    repository="pulumi-${provider}"

    echo -e "\033[0;95m--- Updating repo pulumi/${repository} ---\033[0m"
    pushd "../${repository}"
    git fetch --tags

    plugin_version=$(git describe --tags "$(git rev-list --max-count=1 --tags --not --tags='*-dev')")
    # If a plugin version was passed, then use that.
    # The provider repo will also be checked out at that version below.
    if [ -n "${VERSION:-}" ]; then
        plugin_version=${VERSION}
    elif [[ ${plugin_version} = sdk* ]]; then
        plugin_version=${plugin_version:4}
    elif [[ ${plugin_version} = provider* ]]; then
        plugin_version=${plugin_version:9}
    fi

    echo -e "\033[0;93mCheckout pulumi/${repository} at tag $plugin_version\033[0m"
    git -c advice.detachedHead=false checkout "$plugin_version" >/dev/null

    # Go back to the docs repo.
    popd

    EXISTING_SCHEMA_FILE="../${repository}/provider/cmd/pulumi-resource-${provider}/schema.json"

    # Use a previously generated schema.json file if it exists.
    if [ -f "${EXISTING_SCHEMA_FILE}" ]; then
        echo "Will use the previously generated schema.json for generating resource docs..."
    else
        echo "Could not find a previously generated schema.json file. Will generate schema..."

        echo "Installing resource plugin for ${provider}. Version: ${plugin_version}"
        pulumi plugin install resource "${provider}" "${plugin_version}"

        pushd "../${repository}"
        make generate_schema
        popd
    fi

    SCHEMA_FILE="../../../${repository}/provider/cmd/pulumi-resource-${provider}/schema.json"

    echo "Running package metadata generator from schema for ${provider}..."
    pushd ${TOOL_RESDOCGEN}

    go mod tidy
    go build -o "${HOME}/go/bin/resourcedocsgen" .

    featured=""
    if [[ "${featured_packages[*]}" =~ ${provider} ]]; then
        featured="--featured"
    fi

    resourcedocsgen metadata \
      --metadataOutDir "${METADATA_OUT_DIR}" \
      --schemaFile "${SCHEMA_FILE}" \
      --version "${plugin_version}" \
      --logtostderr ${featured} || exit 3

    popd

    echo "Done generating package metadata for ${provider}"
    echo ""
}

if [ -z "${REPO_OVERRIDE:-}" ]; then
    for PKG in "${DEFAULT_PKGS[@]}" ; do \
        generate_metadata "${PKG}"
    done
else
    generate_metadata "${REPO_OVERRIDE}"
fi

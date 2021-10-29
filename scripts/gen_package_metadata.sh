#!/bin/bash

# A script that facilitates generating package metadata files using the tools/resourcedocsgen Go-based
# tool. This script optionally allows passing the provider name (without the "pulumi-" prefix.)

set -o nounset -o errexit -o pipefail

# The first argument is the override for the package for which this script will generate the metadata.
# Must not be passed without the "pulumi-" prefix.
REPO_OVERRIDE=${1:-}
# Pass a non-empty string as the 2nd arg to override the path to the Pulumi schema file.
# The path must start from the root of the package's repository.
# For example, if the schema is in the root of the package repo, then
# this value should be set to `/schema.json` (if using a JSON schema, .yaml otherwise)
# And if the schema is in a folder called provider, then this would be set to
# `/provider/schema.json` (or .yaml).
#
# If not set, the default location for the schema will be used which is
# /provider/cmd/pulumi-resource-${provider}/schema.[json|yaml].
SCHEMA_FILE_PATH=${2:-}
# Pass a non-empty string as the 3rd arg to override the package version used by this script.
VERSION=${3:-}
# Pass a non-empty string as the 4th arg to override the publisher name for the package.
# Default is Pulumi.
PUBLISHER=${4:-Pulumi}
# Pass a non-empty string as the 5th arg to override the display name of the package.
TITLE=${5:-}
# Pass a non-empty string as the 6th arg to override the category of the package.
CATEGORY=${6:-}
# Pass true as the 7th arg if the package is a component.
COMPONENT=${7:-}

# The path relative to the resourcedocsgen tool where the metadata file should be
# written.
METADATA_OUT_DIR=../../../registry/themes/default/data/registry/packages
TOOL_RESDOCGEN="./tools/resourcedocsgen/"

if [ -z "${REPO_OVERRIDE:-}" ]; then
  echo "Specify the repo name. Usage is gen_package_metadata.sh <METADATA_OUT_DIR> <REPO_OVERRIDE> <VERSION> [PUBLISHER] [TITLE] [CATEGORY]."
  exit 1
fi

# If the script is invoked without any arguments, then the script
# will generate metadata for these packages.
DEFAULT_PKGS=(
    "aws"
    "aws-native"
    "azure"
    "azure-native"
    "azuread"
    "gcp"
    "google-native"
)

featured_packages=(
    "aws"
    "azure-native"
    "gcp"
    "kubernetes"
)

component_packages=(
    "eks"
)

source ./scripts/resource_docs_common.sh

generate_metadata() {
    provider=$1
    repository="pulumi-${provider}"

    echo -e "\033[0;95m--- Updating repo ${repository} ---\033[0m"
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

    # Use the tag's creatordate as the timestamp for when the package was updated.
    # See https://git-scm.com/docs/git-for-each-ref#_field_names (search for `creatordate`).
    PKG_UPDATED_ON=$(git for-each-ref --format="%(creatordate:unix)" "refs/tags/${plugin_version}")

    echo -e "\033[0;93mCheckout ${repository} at tag $plugin_version\033[0m"
    git -c advice.detachedHead=false checkout "$plugin_version" >/dev/null

    # Go back to the docs repo.
    popd

    EXISTING_SCHEMA_FILE=""
    # If the schema file path was overridden, then just use that.
    if [ -n "${SCHEMA_FILE_PATH:-}" ]; then
        EXISTING_SCHEMA_FILE="../${repository}${SCHEMA_FILE_PATH}"
        if [ ! -f "${EXISTING_SCHEMA_FILE}" ]; then
            echo "Error: Pulumi schema file at path ${SCHEMA_FILE_PATH} does not exist."
            exit 1
        fi
    else
        EXISTING_SCHEMA_FILE=$(get_schema_file_path "${repository}" "${provider}")
    fi

    # This path should be relative to the tools/resourcedocsgen tool.
    SCHEMA_FILE="../../${EXISTING_SCHEMA_FILE}"

    echo "Running package metadata generator from schema for ${provider}..."
    pushd ${TOOL_RESDOCGEN}

    go mod tidy

    if [ -z "${GOPATH:-}" ]; then
        echo "GOPATH is empty. Defaulting to ${HOME}/go"
        GOPATH="${HOME}/go"
    fi

    go build -o "${GOPATH}/bin/resourcedocsgen" .

    featured_flag=""
    # The surrounding white-space is needed to ensure that we match the whole word.
    # Disabling shellcheck for the right-side quotation since we want the surrounding
    # white-spaces there too.
    # shellcheck disable=SC2076
    if [[ " ${featured_packages[*]} " =~ " ${provider} " ]]; then
        featured_flag="--featured"
    fi

    component_flag=""
    # If the current package is one of the known component packages
    # then mark it as such. Otherwise, check if COMPONENT is true
    # in order to mark the current package as a component.
    #
    # Same as above, the surrounding white-space is needed here for
    # the regex match.
    # shellcheck disable=SC2076
    if [[ " ${component_packages[*]} " =~ " ${provider} " ]]; then
        component_flag="--component"
    elif [ "${COMPONENT:-}" == "true" ]; then
        component_flag="--component"
    fi

    resourcedocsgen metadata \
      --metadataOutDir "${METADATA_OUT_DIR}" \
      --schemaFile "${SCHEMA_FILE}" \
      --version "${plugin_version}" \
      --publisher "${PUBLISHER}" \
      --updatedOn "${PKG_UPDATED_ON}" \
      --title "${TITLE}" \
      --category "${CATEGORY}" \
      --logtostderr ${featured_flag} ${component_flag} || exit 3

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

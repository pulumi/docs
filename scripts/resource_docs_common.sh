#!/bin/bash

# This script contains common functions used in the scripts for API docs generation.

set -o nounset -o errexit -o pipefail

# Returns the relative path to the schema file for a package.
# Requires the repository name and the package name as the first
# and second arguments respectively.
function get_schema_file_path() {
    local repository=$1
    local pkg=$2

    # This path is related to the root of the docs repo.
    SCHEMA_FILE_ROOT_REL_PATH="../${repository}/provider/cmd/pulumi-resource-${pkg}"
    EXISTING_SCHEMA_JSON_FILE="${SCHEMA_FILE_ROOT_REL_PATH}/schema.json"
    EXISTING_SCHEMA_YAML_FILE="${SCHEMA_FILE_ROOT_REL_PATH}/schema.yaml"
    EXISTING_SCHEMA_FILE=""

    # Use a previously generated schema.json file if it exists.
    if [ -f "${EXISTING_SCHEMA_JSON_FILE}" ]; then
        EXISTING_SCHEMA_FILE=${EXISTING_SCHEMA_JSON_FILE}
    elif [ -f "${EXISTING_SCHEMA_YAML_FILE}" ]; then
        EXISTING_SCHEMA_FILE=${EXISTING_SCHEMA_YAML_FILE}
    else
        echo "Error: A schema file was not found in the package's repo. Cannot generate resource docs."
        exit 1
    fi

    echo "${EXISTING_SCHEMA_FILE}"
}

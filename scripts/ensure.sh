#!/bin/bash

set -o errexit -o pipefail

check_version() {
    tool_name="$1"
    executable="$2"
    version_string="$(eval $3)"
    required_version="$4"
    level="$5"

    color_red=$(echo -e "\033[0;31m")
    color_yellow=$(echo -e "\033[0;33m")
    color_end=$(echo -e "\033[0m")

    details="See the README at https://github.com/pulumi/docs for a list of required tools and versions."

    if ! command -v "$executable" &> /dev/null; then
        echo -e "${color_red}error${color_end} This project requires $1, but the '$2' executable is either not installed or not on your PATH."
        echo $details
        exit 1
    fi

    if [ ! $(echo ${version_string} | grep ${required_version}) ]; then
        printf "${color_yellow}warning${color_end} It looks like you're running %s %s, but this project uses version %s.\n" ${tool_name} ${version_string} ${required_version}
        echo $details
    fi
}
check_version "Node.js"  "node"  "node -v | sed 's/v\([0-9\.]*\).*$/\1/'"            "18"
check_version "Hugo"     "hugo"  "hugo version | sed 's/hugo v\([0-9\.]*\).*$/\1/'"  "0.126.0"
check_version "Yarn"     "yarn"  "yarn -v | sed 's/v\([0-9\.]*\).*$/\1/'"            "1.22"

# Install the Node dependencies for the website and the infrastructure.
yarn install
yarn --cwd infrastructure install
yarn --cwd theme install
yarn --cwd theme/stencil install

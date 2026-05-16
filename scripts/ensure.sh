#!/bin/bash

set -o errexit -o pipefail

color_red=$(echo -e "\033[0;31m")
color_yellow=$(echo -e "\033[0;33m")
color_blue=$(echo -e "\033[0;34m")
color_end=$(echo -e "\033[0m")

# If mise is installed locally, install the tool versions pinned in
# mise.toml (Node, Yarn, Go, Vale) and put them on PATH for the remainder
# of this script. This block is a no-op in CI, which installs tools via
# its own actions (setup-node, peaceiris/actions-hugo, etc.).
if command -v mise &> /dev/null; then
    echo "${color_blue}Installing pinned tool versions via mise...${color_end}"
    mise install
fi

source ./scripts/mise-env.sh

check_version() {
    tool_name="$1"
    executable="$2"
    version_string="$(eval $3)"
    required_version="$4"

    details="See the README at https://github.com/pulumi/docs for installation instructions."

    if ! command -v "$executable" &> /dev/null; then
        echo "${color_red}error${color_end} This project requires $1, but the '$2' executable is either not installed or not on your PATH."
        echo "$details"
        exit 1
    fi

    if [ ! $(echo ${version_string} | grep ${required_version}) ]; then
        printf "${color_yellow}warning${color_end} It looks like you're running %s %s, but this project uses version %s.\n" ${tool_name} ${version_string} ${required_version}
        echo "$details"
    fi
}
check_version "Node.js"  "node"  "node -v | sed 's/v\([0-9\.]*\).*$/\1/'"            "24"
check_version "Hugo"     "hugo"  "hugo version | sed 's/hugo v\([0-9\.]*\).*$/\1/'"  "0.157.0"
check_version "Yarn"     "yarn"  "yarn -v | sed 's/v\([0-9\.]*\).*$/\1/'"            "1.22"

# Install the Node dependencies for the website and the infrastructure.
yarn install --ignore-engines
yarn --cwd infrastructure install
yarn --cwd theme install
yarn --cwd theme/stencil install

# Warm up prettier cache for faster linting
echo ""
echo "${color_blue}Note:${color_end} Warming prettier cache (this will make 'make lint' faster)..."
yarn prettier --check . --cache --loglevel warn

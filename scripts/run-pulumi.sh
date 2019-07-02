#!/bin/bash
#
# Run Pulumi to update the stack targeted by the given branch.

set -o errexit -o pipefail
cd "$(dirname "${BASH_SOURCE}")/.."

if [ -z ${2:-} ]; then
    echo "Usage: $0 [ preview | update ] stack-name"
    exit 1
fi

export PULUMI_ACTION=${1}
export STACK_NAME=${2}

cd ./infrastructure

# Sync dependencies and build the Pulumi program.
yarn install
yarn build

pulumi login
pulumi stack select "pulumi/${STACK_NAME}"

case ${PULUMI_ACTION} in
    preview)
        assume-role pulumi-ci pulumi preview
        ;;
    update)
        assume-role pulumi-ci pulumi up --yes
        ;;
    *)
        echo "Unknown action '${PULUMI_ACTION}'"
        exit 1
        ;;
esac

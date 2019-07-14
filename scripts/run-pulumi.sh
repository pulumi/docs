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

# Double check we have the right credentials. If CI/CD is running from a repo's fork,
# they won't be available. In which case, skip the preview step and just rely on
# make build/validate.
if [ -z ${PULUMI_ACCESS_TOKEN:-} ]; then
    echo "PULUMI_ACCESS_TOKEN not set. Skipping ${PULUMI_ACTION} on pulumi/${STACK_NAME}."
    exit 0
fi

cd ./infrastructure

# Sync dependencies and build the Pulumi program.
yarn install
yarn build

pulumi login
pulumi stack select "pulumi/${STACK_NAME}"

ROLE_ARN="arn:aws:iam::058607598222:role/ContinuousIntegrationRole"

case ${PULUMI_ACTION} in
    preview)
        assume-role "${ROLE_ARN}" pulumi preview
        ;;
    update)
        assume-role "${ROLE_ARN}" pulumi up --yes --parallel 10
        ;;
    *)
        echo "Unknown action '${PULUMI_ACTION}'"
        exit 1
        ;;
esac

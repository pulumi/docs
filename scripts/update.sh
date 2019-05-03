#!/bin/bash

set -o errexit -o pipefail
cd "$(dirname "${BASH_SOURCE}")/.."

if [ -z ${1:-} ]; then
    echo "Usage: $0 [ staging | production ]"
    exit 1
fi

# Environment being updated (production, staging, etc.)
export ENVIRONMENT=${1}

# Each environment is running in a different AWS account, so we determine the
# credentials to use based on environment. Set in the Travis UI:
# https://travis-ci.com/pulumi/docs/settings
export ACCESS_KEY_ENV_VAR="AWS_ACCESS_KEY_ID_${ENVIRONMENT}"
export SECRET_KEY_ENV_VAR="AWS_SECRET_ACCESS_KEY_${ENVIRONMENT}"

export AWS_ACCESS_KEY_ID="${!ACCESS_KEY_ENV_VAR}"
export AWS_SECRET_ACCESS_KEY="${!SECRET_KEY_ENV_VAR}"

if [ -z "${AWS_ACCESS_KEY_ID:-}" ] || [ -z "${AWS_SECRET_ACCESS_KEY:-}" ]; then
    echo "Skipping update, no AWS credentials found."
    exit 0
fi
echo "Using AWS Access KEY ID ${AWS_ACCESS_KEY_ID}"

cd ./infrastructure

# Sync dependencies and build the Pulumi program.
yarn install
yarn build

# Login, select the stack, and update.
pulumi stack select "pulumi/pulumi.io-${ENVIRONMENT}"
pulumi up --yes --skip-preview

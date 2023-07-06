#!/bin/bash

set -o errexit -o pipefail

echo "Selecting the ${PULUMI_STACK_NAME} stack"
pulumi login
pulumi -C infrastructure stack select "${PULUMI_STACK_NAME}"


#!/bin/bash

set -o errexit -o pipefail

if [ -n "${CI_ASSUME_ROLE_ARN:-}" ]; then
  echo "Assuming the production CI role..."
  eval "$(assume-role "${CI_ASSUME_ROLE_ARN}")"
fi

if [ -n "${PULUMI_STACK_NAME:-}" ]; then
  pulumi login
  echo "Selecting the ${PULUMI_STACK_NAME} stack"
  pulumi -C infrastructure stack select "${PULUMI_STACK_NAME}"
else
  echo "Could not select a stack. PULUMI_STACK_NAME is empty."
fi

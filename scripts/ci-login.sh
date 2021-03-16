#!/bin/bash

set -o errexit -o pipefail

echo "Selecting the pulumi/production stack"
pulumi login
pulumi -C infrastructure stack select pulumi/production

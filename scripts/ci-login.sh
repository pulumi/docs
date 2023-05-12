#!/bin/bash

set -o errexit -o pipefail

echo "Selecting the pulumi/www-production stack"
pulumi login
pulumi -C infrastructure stack select pulumi/www-production


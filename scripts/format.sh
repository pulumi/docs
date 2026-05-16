#!/bin/bash

set -o errexit -o pipefail

source ./scripts/mise-env.sh

yarn prettier --write . --cache

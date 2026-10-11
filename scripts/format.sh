#!/bin/bash

set -o errexit -o pipefail

./scripts/prettier.sh --write . --cache

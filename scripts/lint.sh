#!/bin/bash

set -o errexit -o pipefail

yarn run lint-markdown
yarn prettier --check .

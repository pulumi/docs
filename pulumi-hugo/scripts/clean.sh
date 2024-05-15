#!/bin/bash

set -o errexit -o pipefail

yarn cache clean
hugo mod clean
git clean -fdX

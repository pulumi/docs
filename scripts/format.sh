#!/bin/bash

set -o errexit -o pipefail

yarn prettier --write .

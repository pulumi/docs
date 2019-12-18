#!/bin/bash
# Usage: run_docfx

set -o nounset -o errexit -o pipefail

cd docfx
docfx

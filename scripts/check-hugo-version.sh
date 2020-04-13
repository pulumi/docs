#!/bin/bash
#
# Check the currently installed version of Hugo is the specific
# one required.
#
# Recent versions of Hugo have bugs in the markdown renderer (Blackfriday) that prevents fenced
# code from rendering correctly in lists when a language is specified. See README.md for more
# details.

set -o nounset -o errexit -o pipefail

>/dev/null 2>/dev/null which hugo || {
    echo "ERROR: Can't find hugo. Do you have hugo installed?"
    exit 1
}

readonly REQUIRED_HUGO_VERSION="v0.55.4"

HUGO_VERSION=$(hugo version)
if [[ ${HUGO_VERSION} != *"${REQUIRED_HUGO_VERSION}"* ]]; then
    echo "ERROR: Running incorrect version of hugo detected. See README.md for more information."
    echo "    Installed: ${HUGO_VERSION}"
    echo "    Required : ${REQUIRED_HUGO_VERSION}"
    exit 1
fi

#!/usr/bin/env bash
#
# Create shortened URL targets (shortlinks) for links on the doc site.
#
# Shortlink definitions are created as markdown files in the /shortlinks directory.
# Each of these files contains a reference to the target link, and the desired
# shortlink that will redirect to the target. In the common case, the shortlink
# is a randomly generated string, but a specific shortlink can also be specified.
# Note that the shortlink must include a trailing / for the redirection to work correctly.

set -o errexit -o pipefail
cd "$(dirname "${BASH_SOURCE}")/.."

if [[ $# -ne 2 && $# -ne 3 ]]; then
    cat << EOF
Usage: $(basename $0) <target_link> <filename> [shortlink]

Example: $(basename $0) /reference/troubleshooting.html#ingress-status-loadbalancer k8s-ingress-lbstatus

/shortlinks/k8s-ingress-lbstatus.md
---
redirect_to: /reference/troubleshooting.html#ingress-status-loadbalancer
permalink: <random-6-char-string>/
---
EOF
    exit 1
fi

TARGET_LINK=$1
FILENAME=$2
SHORTLINK=$3

# If shortlink not provided, generate a random 6-character alphanumeric link
if [[ ! ${SHORTLINK} ]]; then
    PERMALINK="$(LC_ALL=C tr -dc 'a-z0-9' </dev/urandom | head -c6 ; echo)"
else
    PERMALINK="${SHORTLINK}"
fi

RELATIVEPATH="./shortlinks/${FILENAME}.md"
FILEPATH=$(echo "$(cd "$(dirname "${RELATIVEPATH}")"; pwd -P)/$(basename "${RELATIVEPATH}")")

cat << EOF > "${FILEPATH}"
---
redirect_to: ${TARGET_LINK}
permalink: ${PERMALINK}/
---
EOF

cat << EOF
Created shortlink definition at ${FILEPATH}
https://pulumi.io/${PERMALINK} --> https://pulumi.io${TARGET_LINK}
EOF

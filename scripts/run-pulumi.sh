#!/bin/bash
#
# Run Pulumi to update the stack targeted by the given branch.

set -o errexit -o pipefail
cd "$(dirname "${BASH_SOURCE}")/.."

if [ -z ${1:-} ]; then
    echo "Usage: $0 [ preview | update ]"
    exit 1
fi

source ./scripts/common.sh

export PULUMI_ACTION=${1}

case ${PULUMI_ACTION} in
    preview)
        pulumi -C infrastructure preview
        ;;
    update)
        # Given how frequently we update the CloudFront distribution, and how easy it can
        # be for our checkpointed CloudFront Etag to fall out of sync with what's current,
        # we refresh the distribution on every update -- but we consider any other
        # difference in stack state an error to be examined and corrected manually.
        pulumi -C infrastructure refresh -t "urn:pulumi:production::www.pulumi.com::aws:cloudfront/distribution:Distribution::cdn" --yes
        pulumi -C infrastructure refresh --expect-no-changes --yes

        pulumi -C infrastructure up --yes
        ;;
    *)
        echo "Unknown action '${PULUMI_ACTION}'"
        exit 1
        ;;
esac

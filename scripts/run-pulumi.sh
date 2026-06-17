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
        # Run previews against the production stack. On PR workflows we provision the bucket in the testing account,
        # but infrastructure previews should always run against the production stack because that is where they are
        # deployed when merged (not the www-testing stack).
        pulumi -C infrastructure preview --stack pulumi/www-production
        ;;
    update)
        # Given how frequently we update the CloudFront distribution, and how easy it can
        # be for our checkpointed CloudFront Etag to fall out of sync with what's current,
        # we refresh the distribution on every update.
        pulumi -C infrastructure refresh -t "${CDN_PULUMI_URN}" --yes

        pulumi -C infrastructure up --yes

        # Invalidate CloudFront cache after deploy so updated content is served immediately.
        # Only invalidate HTML and non-fingerprinted paths. Fingerprinted assets (css, js,
        # images under /fingerprinted/) use content-hash URLs and don't need invalidation.
        DISTRIBUTION_ID=$(pulumi -C infrastructure stack output cloudFrontDistributionId 2>/dev/null || true)
        if [ -n "${DISTRIBUTION_ID}" ]; then
            echo "Invalidating CloudFront cache for distribution ${DISTRIBUTION_ID}..."
            if aws cloudfront create-invalidation \
                --distribution-id "${DISTRIBUTION_ID}" \
                --paths "/docs/*" "/registry/*" "/blog/*" "/tutorials/*" "/guides/*" "/product/*" "/pricing/*" "/contact/*" "/index.html" "/"; then
                echo "CloudFront cache invalidation submitted successfully."
            else
                echo "WARNING: CloudFront cache invalidation failed. Content will refresh within 30 minutes."
            fi
        fi
        ;;
    *)
        echo "Unknown action '${PULUMI_ACTION}'"
        exit 1
        ;;
esac

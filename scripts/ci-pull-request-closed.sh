#!/bin/bash

set -o errexit -o pipefail

# This script handles closed pull requests. For PRs that are closed unmerged, it deletes
# their associated buckets and posts a message back to the PR to that effect.

source ./scripts/ci-login.sh
source ./scripts/common.sh

if [[ "$GITHUB_EVENT_NAME" == "pull_request" && ! -z "$GITHUB_EVENT_PATH" ]]; then
    event="$(cat "$GITHUB_EVENT_PATH")"
    pr_number="$(echo $event | jq -r ".number")"
    pr_action="$(echo $event | jq -r ".action")"
    pr_merged="$(echo $event | jq -r ".pull_request.merged")"

    if [[ "$pr_action" == "closed" && "$pr_merged" == "false" ]]; then
        pr_bucket_name="$(origin_bucket_prefix)-pr-${pr_number}"
        pr_comment_api_url="$(echo $event | jq -r ".pull_request._links.comments.href")"

        if [ -z "$(aws s3api head-bucket --bucket $pr_bucket_name || echo '')" ]; then
            echo "Bucket ${pr_bucket_name} wasn't found. Exiting."
            exit 0
        fi

        echo "Found bucket ${pr_bucket_name}."
        prod_bucket_name="$(pulumi -C infrastructure stack output originBucketName)"

        if [ "$pr_bucket_name" == "$prod_bucket_name" ]; then
            echo "PR bucket name (${pr_bucket_name}) matches production bucket name (${prod_bucket_name}). Skipping delete."
            exit 0
        else
            echo "Removing the bucket."

            # Deliberately logging this at first just to make sure it works as designed.
            echo "aws s3 rb s3://${pr_bucket_name} --force"

            post_github_pr_comment \
                "The site preview for this pull request was removed. ✨" \
                $pr_comment_api_url
        fi
    fi

    echo "PR action was ${pr_action}, merged ${merged}, so skipping."
fi

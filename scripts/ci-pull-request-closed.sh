#!/bin/bash

set -o errexit -o pipefail

# This script handles closed pull requests by finding all of their associated site-preview
# buckets and deleting them.

# See if we have the requisite credentials. If not, we might be in a fork, so exit.
if [ -z "${AWS_ACCESS_KEY_ID:-}" ] || [ -z "${AWS_SECRET_ACCESS_KEY:-}" ] || [ -z "${PULUMI_ACCESS_TOKEN:-}" ]; then
    echo "Missing secret tokens, possibly due to a forked PR. Exiting."
    exit
fi

source ./scripts/common.sh
source ./scripts/ci-login.sh


if [[ "$GITHUB_EVENT_NAME" == "pull_request" && ! -z "$GITHUB_EVENT_PATH" ]]; then
    event="$(cat "$GITHUB_EVENT_PATH")"
    pr_number="$(echo $event | jq -r ".number")"
    pr_action="$(echo $event | jq -r ".action")"

    if [[ "$pr_action" == "closed" ]]; then
        pr_comment_api_url="$(echo $event | jq -r ".pull_request._links.comments.href")"

        # List s3 buckets and filter all buckets associated with this PR. 
        buckets=$(aws s3 ls | grep "$(origin_bucket_prefix)-pr-${pr_number}-" | awk '{print $3}')

        if [ ! -z "$buckets" ]; then
            for bucket in $buckets; do
                echo "removing s3://${bucket}..."
                aws s3 rb "s3://${bucket}" --force --region "$(aws_region)"
            done
        else
            echo "No buckets found for PR: 'https://github.com/pulumi/docs/pulls/${pr_number}'"
        fi

        # Post a PR comment that any links to previously built previews will no longer work.
        post_github_pr_comment \
            "Site previews for this pull request have been removed. ✨" \
            $pr_comment_api_url
    else
        echo "PR action was ${pr_action}. Skipping."
    fi
fi

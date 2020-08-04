#!/bin/bash

set -o errexit -o pipefail

# This script handles closed pull requests by finding all of their associated site-preview
# buckets and deleting them.

source ./scripts/ci-login.sh
source ./scripts/common.sh

if [[ "$GITHUB_EVENT_NAME" == "pull_request" && ! -z "$GITHUB_EVENT_PATH" ]]; then
    event="$(cat "$GITHUB_EVENT_PATH")"
    pr_number="$(echo $event | jq -r ".number")"
    pr_action="$(echo $event | jq -r ".action")"

    if [[ "$pr_action" == "closed" ]]; then
        pr_comment_api_url="$(echo $event | jq -r ".pull_request._links.comments.href")"

        # Find all commits associated with the PR.
        pr_commits="$(curl \
            -s \
            -H "Accept: application/vnd.github.v3+json" \
            "https://api.github.com/repos/${GITHUB_REPOSITORY}/pulls/${pr_number}/commits")"

        # For each PR commit, if a bucket exists for it, delete it.
        for commit in $(echo $pr_commits | jq -r ".[].sha"); do
            pr_bucket_name="$(get_bucket_for_commit $commit)"

            if [ ! -z "$pr_bucket_name" ]; then
                echo "Found bucket ${pr_bucket_name} associated with commit ${commit}."
                echo "Attempting to delete..."

                # aws s3api head-bucket is a quick way to determine whether the bucket exists
                # and we have access to it.
                if aws s3api head-bucket --bucket "$pr_bucket_name" 2>/dev/null; then

                    # Deliberately logging this at first just to make sure it works as designed.
                    echo "aws s3 rb s3://${pr_bucket_name} --force"
                else
                    echo "Unable to delete ${pr_bucket_name}. Skipping."
                fi
            else
                echo "No bucket found for commit ${commit}. Skipping."
            fi
        done

        # Post a PR comment that any links to previously built previews will no longer work.
        post_github_pr_comment \
            "Site previews for this pull request have been removed. ✨" \
            $pr_comment_api_url
    fi

    echo "PR action was ${pr_action}. Skipping."
fi

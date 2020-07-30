#!/bin/bash

# Posts a message to Slack. Requires a valid access token is available in $SLACK_ACCESS_TOKEN.
# Usage: post_to_slack <channel> <message>
post_to_slack() {
    local channel=$1
    local message=$2

    local escaped=$(echo ${message} | sed 's/"/\"/g' | sed "s/'/\'/g" )
    local json="{\"channel\": \"#${channel}\", \"text\": \"${escaped}\", \"as_user\": true}"

    curl -s \
         -X POST \
         -H "Content-type: application/json" \
         -H "Authorization: Bearer ${SLACK_ACCESS_TOKEN}" \
         -d  "${json}" \
         https://slack.com/api/chat.postMessage > /dev/null
}

# Posts a comment to a GitHub PR. Requires a GitHub token is available in $GITHUB_TOKEN.
# Usage: post_github_pr_comment "Hi!" "https://api.github.com/repos/<org>/<repo>/issues/<pr-number>/comments"
post_github_pr_comment() {
    local pr_comment=$1
    local pr_comment_api_url=$2
    local pr_comment_body=$(printf '{ "body": "%s" }' "$pr_comment")

    curl -s \
         -X POST \
         -H "Authorization: token ${GITHUB_TOKEN}" \
         -d "$pr_comment_body" \
         $pr_comment_api_url > /dev/null
}

# Returns the Git SHA of the HEAD commit. For pull requests, we take this from GitHub event metadata, since in that case, the HEAD commit will contain the SHA of the merge commit with the base branch.
git_sha() {
    if [[ "$GITHUB_EVENT_NAME" == "pull_request" && ! -z "$GITHUB_EVENT_PATH" ]]; then
        echo "$(cat "$GITHUB_EVENT_PATH" | jq -r ".pull_request.head.sha")"
    else
        echo "$(git rev-parse HEAD)"
    fi
}

# Returns the shortened version of either the GITHUB_SHA, if present, or that of the most
# recent commit.
git_sha_short() {
    echo "$(git_sha)" | cut -c1-8
}

origin_bucket_prefix() {
    echo "pulumi-docs-origin"
}

# Returns the name of the metadata file we expect to exist locally before running Pulumi.
origin_bucket_metadata_filepath() {
    echo "./origin-bucket-metadata.json"
}

# pr_number_or_git_sha returns either the PR number of the current GitHub Actions run or
# the Git SHA of the current branch, for purposes of naming the destination bucket and
# bundled build assets.
pr_number_or_git_sha() {
    if [[ "$GITHUB_EVENT_NAME" == "pull_request" && ! -z "$GITHUB_EVENT_PATH" ]]; then
        echo "pr-$(cat "$GITHUB_EVENT_PATH" | jq -r ".number")"
    else
        echo "push-$(git_sha_short)"
    fi
}

# Get the AWS SSM Parameter Store key for the specified commit SHA. Used for mapping a
# commit to a previously created bucket.
ssm_parameter_key_for_commit() {
    echo "/docs/commits/$1/bucket"
}

# Retry the given command some number of times, with a delay of some number of seconds between calls.
# Usage: retry some_command <retry-count> <delay-in-seconds>
retry() {
    local n=1
    local max=$2
    local delay=$3
    while true; do
    "$@" && break || {
        if [[ $n -lt $max ]]; then
            ((n++))
            echo "Command failed. Attempt $n/$max:"
            sleep $delay;
        else
            echo "The command has failed after $n attempts." >&2
            return 1
        fi
    }
    done
}

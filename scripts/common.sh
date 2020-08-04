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

# current_time_in_ms returns the epoch time in milliseconds.
current_time_in_ms() {
    echo "$(node -e 'console.log(Date.now())')"
}

origin_bucket_prefix() {
    echo "pulumi-docs-origin"
}

# Returns the name of the metadata file we expect to exist locally before running Pulumi.
origin_bucket_metadata_filepath() {
    echo "./origin-bucket-metadata.json"
}

# build_identifier returns a string that is used to identify the current build for naming
# S3 buckets and asset bundles.
build_identifier() {
    local identifier

    # For CI builds, we use the GitHub Actions event to generate more readable identifiers.
    # - For pull_request actions, return "pr-<number>-<git-sha>"
    # - For others, return "<event-name>-<git-sha>".
    if [[ ! -z "$GITHUB_EVENT_NAME" && ! -z "$GITHUB_EVENT_PATH" ]]; then
        identifier="$GITHUB_EVENT_NAME"

        if [ "$GITHUB_EVENT_NAME" == "pull_request" ]; then
            identifier="pr-$(cat "$GITHUB_EVENT_PATH" | jq -r ".number")"
        fi

        identifier="${identifier}-$(git_sha_short)"
    else
        # For on-demand builds, if an identifier's been set, use it.
        identifier="$BUILD_IDENTIFIER"

        # Otherwise, just use the current Git SHA.
        if [ -z "$BUILD_IDENTIFIER" ]; then
            identifier="$(git_sha_short)"
        fi
    fi

    echo "$identifier"
}

# Get the AWS SSM Parameter Store key for the specified commit SHA. Used for mapping a
# commit to a previously created bucket.
ssm_parameter_key_for_commit() {
    echo "/docs/commits/$1/bucket"
}

get_bucket_for_commit() {
    aws ssm get-parameter \
        --name "$(ssm_parameter_key_for_commit $1)" \
        --query Parameter.Value \
        --region us-west-2 \
        --output text || echo ""
}

set_bucket_for_commit() {
    aws ssm put-parameter \
        --name "$(ssm_parameter_key_for_commit $1)" \
        --value "$2" \
        --type String \
        --region $3 \
        --overwrite
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

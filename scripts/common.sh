#!/bin/bash

# Posts a message to Slack. Requires a valid access token is available in $SLACK_ACCESS_TOKEN.
# Usage: post_to_slack <channel> <message>
post_to_slack() {
    local channel=$1
    local message=$2

    local escaped=$(echo ${message} | sed 's/"/\"/g' | sed "s/'/\'/g" )
    local json="{\"channel\": \"#${channel}\", \"text\": \"${escaped}\", \"as_user\": true}"

    curl \
        -X POST \
        -H "Content-type: application/json" \
        -H "Authorization: Bearer ${SLACK_ACCESS_TOKEN}" \
        -d  "${json}" \
        https://slack.com/api/chat.postMessage > /dev/null
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

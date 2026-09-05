#!/bin/bash

aws_region() {
    echo "$(pulumi -C infrastructure config get 'aws:region')"
}

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
         -H "Authorization: token ${PULUMI_BOT_TOKEN}" \
         -d "$pr_comment_body" \
         $pr_comment_api_url > /dev/null
}

# Converts a Hugo content file path to its published, root-relative URL, following
# the same rules the site uses: strip the leading "content/", strip the ".md"
# extension, collapse section landing pages ("/_index") and leaf-bundle pages
# ("/index") to their directory, and guarantee a leading and trailing slash.
# Usage:
#   content_path_to_url content/docs/foo/bar.md          # => /docs/foo/bar/
#   content_path_to_url content/blog/my-post/index.md    # => /blog/my-post/
#   content_path_to_url content/_index.md                # => /
content_path_to_url() {
    local path=$1

    path="${path#content/}"     # Strip the leading content/ prefix.
    path="${path%.md}"          # Strip the trailing .md extension.

    if [[ "$path" == "_index" || "$path" == "index" ]]; then
        path=""                 # Site root (content/_index.md).
    else
        path="${path%/_index}"  # Collapse section landing pages (_index.md).
        path="${path%/index}"   # Collapse leaf-bundle pages (index.md).
    fi

    echo "/${path}/" | sed 's#//*#/#g'
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
    # This function returns the bucket name prefix to be used when naming the
    # S3 buckets. We are adding a `www` prefix to the buckets being deployed
    # to the new account, in order to account for collisions in the global
    # bucket namespace.
    echo "www-${DEPLOYMENT_ENVIRONMENT}-pulumi-docs-origin"
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
        event_name_sanitized="${GITHUB_EVENT_NAME//_/-}"
        identifier="$event_name_sanitized"

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

# to_base36 converts a non-negative integer to a lowercase base-36 string. Used to keep
# the deploy-run uniquifier (see deploy_run_uniquifier below) as compact as possible, since
# it has to fit inside S3's 63-character bucket-name limit alongside the bucket prefix, the
# event name, and the commit SHA.
to_base36() {
    local n=$1
    local chars="0123456789abcdefghijklmnopqrstuvwxyz"
    local result=""

    if [ "$n" -eq 0 ]; then
        echo "0"
        return
    fi

    while [ "$n" -gt 0 ]; do
        result="${chars:$((n % 36)):1}${result}"
        n=$((n / 36))
    done

    echo "$result"
}

# deploy_run_uniquifier returns a short token that's different across separate script
# invocations that would otherwise compute the same build_identifier -- most importantly,
# two scheduled rebuilds of the same commit (no new push in between). In CI, this is the
# GitHub Actions run ID (plus the run attempt, if this is a re-run), base36-encoded to stay
# compact. Outside CI, it falls back to the current epoch second, also base36-encoded.
deploy_run_uniquifier() {
    if [[ ! -z "$GITHUB_RUN_ID" ]]; then
        local run_attempt="${GITHUB_RUN_ATTEMPT:-1}"
        local encoded="$(to_base36 "$GITHUB_RUN_ID")"

        if [ "$run_attempt" != "1" ]; then
            encoded="${encoded}${run_attempt}"
        fi

        echo "$encoded"
    else
        to_base36 "$(date +%s)"
    fi
}

# deploy_bucket_name returns the name of the S3 bucket to use for a deploy-path (i.e.,
# non-preview) build: pushes to master and the scheduled/manual rebuilds in
# build-and-deploy.yml. Unlike build_identifier(), which is also used to fingerprint asset
# bundle paths and therefore MUST stay identical for a given commit, this appends a short
# per-run token (deploy_run_uniquifier) so that two deploy runs at the same commit never
# collide on the same bucket name.
#
# Why this matters: sync-and-test-bucket.sh treats "bucket already exists" as an expected,
# swallowed condition (aws s3 mb ... || true) covering the case where a previous run of
# *this same build* failed partway through. Without a uniquifier, an unrelated later run
# that happens to share a commit -- e.g. a scheduled rebuild with no intervening push --
# hits that same swallowed condition and then runs a destructive `s5cmd sync --delete` in
# place against the pre-existing bucket, which may be the one CloudFront is actively
# serving. Preview (PR) builds are intentionally excluded: they're named directly by the
# caller from build_identifier() so a PR keeps reusing the same bucket across pushes, and
# they're never a CloudFront origin, so they carry none of this risk.
#
# The result is clamped to S3's 63-character bucket-name limit by trimming the event-name
# segment of build_identifier() only -- never the commit SHA (needed for traceability) and
# never the uniquifier (needed for collision-freedom). If build_identifier() has no
# trimmable event segment (e.g. a caller-supplied $BUILD_IDENTIFIER with no embedded event)
# and the name still doesn't fit, this fails loudly rather than silently truncating the SHA
# or the uniquifier.
deploy_bucket_name() {
    local prefix identifier uniq name max_len overflow event_part rest_part

    prefix="$(origin_bucket_prefix)"
    identifier="$(build_identifier)"
    uniq="$(deploy_run_uniquifier)"
    name="${prefix}-${identifier}-${uniq}"
    max_len=63

    if [ "${#name}" -gt "$max_len" ]; then
        overflow=$(( ${#name} - max_len ))

        if [[ "$identifier" != *-* ]]; then
            echo "ERROR: deploy bucket name '${name}' is ${#name} chars (max ${max_len}) and build_identifier ('${identifier}') has no event segment to trim; refusing to silently truncate the SHA or the uniquifier." >&2
            return 1
        fi

        event_part="${identifier%-*}"
        rest_part="${identifier##*-}"

        if [ "$overflow" -ge "${#event_part}" ]; then
            echo "ERROR: deploy bucket name '${name}' is ${#name} chars (max ${max_len}) and trimming the event segment ('${event_part}') isn't enough to fit; refusing to silently truncate the SHA or the uniquifier." >&2
            return 1
        fi

        event_part="${event_part:0:$(( ${#event_part} - overflow ))}"
        name="${prefix}-${event_part}-${rest_part}-${uniq}"
    fi

    echo "$name"
}

# List the 100 most recent bucket in the current account, sorted descendingly by
# CreationDate, matching the prefix we use to name website buckets. Supports an optional
# suffix to filter by (e.g., "pr" or "push").
get_recent_buckets() {
    # The starts_with() filter already scopes results to the per-deploy atomic origin
    # buckets (www-{env}-pulumi-docs-origin-*), so the permanent versioned-docs archive
    # bucket (pulumi-docs-versioned-{env}) can never appear here. The select(...) below
    # is a belt-and-braces guard: it guarantees the permanent bucket is never returned
    # for deletion even if the naming scheme ever changes. NEVER remove this.
    aws s3api list-buckets \
        --query "reverse(sort_by(Buckets,&CreationDate))[:100].{id:Name,date:CreationDate}|[?starts_with(id,'$(origin_bucket_prefix)-${1}')]" \
        --region "$(aws_region)" \
        --output json | jq -r '.[].id | select(test("pulumi-docs-versioned") | not)'
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

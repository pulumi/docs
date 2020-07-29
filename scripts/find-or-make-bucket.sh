#!/bin/bash

set -o errexit -o pipefail

source ./scripts/common.sh

# This script examines the current environment and determines whether to check for an
# existing, previously tested bucket or to make a new one. It expects to be run on GitHub
# Actions push events only.

build_and_sync_bucket() {
    echo "Making a new bucket..."
    ./scripts/build-site.sh
    ./scripts/bucketize.sh
}

get_bucket_for_commit() {
    aws ssm get-parameter \
        --name "$(ssm_parameter_key_for_commit $1)" \
        --query Parameter.Value \
        --region us-west-2 \
        --output text || echo ""
}

get_associated_pr_commit_for_commit() {
    # Note that this uses a GitHub preview API.
    # https://docs.github.com/en/rest/reference/repos#list-pull-requests-associated-with-a-commit
    curl -H "Accept: application/vnd.github.groot-preview+json" \
        "https://api.github.com/repos/${GITHUB_REPOSITORY}/commits/$1/pulls" | jq -r '.[0].head.sha' || echo ""
}

# Examine GitHub event metadata. If it's a push, and there's a referenced commit, find the
# bucket that goes with that commit.
if [[ "$GITHUB_EVENT_NAME" == "push" && ! -z "$GITHUB_EVENT_PATH" ]]; then
    merged_commit="$(cat "$GITHUB_EVENT_PATH" | jq -r ".before")"

    if [ "$merged_commit" != "null" ]; then

        # All merged commits *should* have an associated bucket, but some may not -- for
        # example, if a commit merges before its build completes, or if someone pushes
        # directly to master. In these cases, we build and test a new bucket before
        # deploying it in a later step. Otherwise, if we do find a bucket associated with
        # the merged commit, we run a few checks, and if things look good, we exit.

        # Query AWS Parameter Store for a bucket associated with the referenced commit.
        candidate_bucket="$(get_bucket_for_commit $merged_commit)"

        # If a matching bucket wasn't found, check to see whether the merged commit
        # relates to a PR, and if it does (e.g., when a PR is squashed-and-merged), check
        # to see whether the PR's HEAD commit has an associated bucket.
        if [ -z "$candidate_bucket" ]; then
            pr_commit="$(get_associated_pr_commit_for_commit $merged_commit)"

            if [ ! -z "$pr_commit" ]; then
                candidate_bucket="$(get_bucket_for_commit $pr_commit)"
            fi
        fi

        # Otherwise, if a matching bucket wasn't found, just make one.
        if [ -z "$candidate_bucket" ]; then
            echo "Push event detected, but there doesn't seem to be a bucket associated with the referenced commit ${merged_commit}."
            build_and_sync_bucket
            exit 0
        fi

        # Validate that the bucket has a metadata file, and download that file to the
        # local path that Pulumi will be expecting. We'll use this file to run the Pulumi
        # update if it passes all of our checks.
        aws s3 cp s3://${candidate_bucket}/metadata.json $(origin_bucket_metadata_filepath)

        # Pull some values out of that file.
        bucket_metadata="$(cat $(origin_bucket_metadata_filepath))"
        bucket_commit="$(echo $bucket_metadata | jq -r '.commit')"
        bucket_url="$(echo $bucket_metadata | jq -r '.url')"

        # Make sure the merged commit and the commit referenced in the bucket actually
        # match. If they don't, it's an error.
        if [ "$bucket_commit" != "$merged_commit" ]; then
            printf \
                "Merged commit %s doesn't match the commit referenced in the associated bucket's metadata file (%s). This may be the wrong bucket. Exiting.\n" \
                "$merged_commit" \
                "$bucket_commit"
            exit 1
        fi

        # Make sure the bucket URL is accessible and seems like a Pulumi website.
        if [[ ! $(curl -I "${bucket_url}/" --fail) || ! $(curl -I "${bucket_url}/start/" --fail) ]]; then
            printf "The bucket at %s doesn't seem to contain a working Pulumi website. Exiting.\n" "$bucket_url"
            exit 1
        fi

        # Ok, everything looks good -- let's roll with this bucket.
        echo "Found bucket ${candidate_bucket} and it looks good. Continuing."
        exit 0
    else
        echo "Push event detected, but the event metadata either didn't exist or didn't reference a merged commit."
        build_and_sync_bucket
        exit 0
    fi
fi

echo "Not a push event. Exiting."
exit 1

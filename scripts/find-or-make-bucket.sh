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
    # Note that this GitHub API is still in preview.
    # https://docs.github.com/en/rest/reference/repos#list-pull-requests-associated-with-a-commit
    curl -s \
         -H "Accept: application/vnd.github.groot-preview+json" \
         "https://api.github.com/repos/${GITHUB_REPOSITORY}/commits/$1/pulls" | jq -r '.[0].head.sha' || echo ""
}

# For push events, the GITHUB_SHA is the HEAD of the base branch (e.g., master).
# https://docs.github.com/en/actions/configuring-and-managing-workflows/using-environment-variables#default-environment-variables
if [[ "$GITHUB_EVENT_NAME" == "push" && ! -z "$GITHUB_REPOSITORY" &&  ! -z "$GITHUB_SHA" ]]; then

    # Attempt to find the most recent PR commit associated with the commit that triggered this workflow.
    associated_pr_commit="$(get_associated_pr_commit_for_commit $GITHUB_SHA)"

    # If there's an associated PR commit, attempt to find the bucket that goes with it.
    if [ "$associated_pr_commit" != "null" ]; then

        # All commits originating from PRs *should* have an associated bucket, but some
        # may not -- for example, if a merge occurred before the PR build completed, or if
        # the commit is was the result of a direct push to master. In these cases, we
        # build and test a new bucket before deploying it in a later step. If we do find a
        # bucket associated with the commit, however, we run a few checks, and if things
        # look good, we exit, leaving its metadata file in place for the Pulumi update.

        # Query AWS Parameter Store for a bucket associated with the referenced commit.
        candidate_bucket="$(get_bucket_for_commit $associated_pr_commit)"

        # If a matching bucket wasn't found, just make one. Otherwise, continue.
        if [ -z "$candidate_bucket" ]; then
            echo "Push event detected, but there doesn't seem to be a bucket associated with the referenced commit ${associated_pr_commit}."
            build_and_sync_bucket
            exit 0
        fi

        # Validate that the bucket exists and has a metadata file, then download that file
        # to the local path that Pulumi will be expecting. We'll use this file to run the
        # Pulumi update if it passes all of our checks.
        aws s3 cp s3://${candidate_bucket}/metadata.json $(origin_bucket_metadata_filepath)

        # Pull some values out of that file.
        bucket_metadata="$(cat $(origin_bucket_metadata_filepath))"
        bucket_commit="$(echo $bucket_metadata | jq -r '.commit')"
        bucket_url="$(echo $bucket_metadata | jq -r '.url')"

        # Make sure the associated commit and the commit referenced in the bucket actually
        # match. If they don't, it's an error.
        if [ "$bucket_commit" != "$associated_pr_commit" ]; then
            printf \
                "Associated PR commit %s doesn't match the commit referenced in the bucket's metadata file (%s). This may be the wrong bucket. Exiting.\n" \
                "$associated_pr_commit" \
                "$bucket_commit"
            exit 1
        fi

        # Make sure the bucket works as it should.
        ./scripts/check-links.sh "url" "$bucket_url"
        ./scripts/run-browser-tests.sh "$bucket_url"

        # Ok, everything looks good -- let's roll with this bucket.
        echo "Found bucket ${candidate_bucket} and it looks good. Continuing."
        exit 0
    else
        echo "Push event detected, but an associated PR commit was not found."
        build_and_sync_bucket
        exit 0
    fi
fi

echo "Not a push event. Exiting."
exit 1

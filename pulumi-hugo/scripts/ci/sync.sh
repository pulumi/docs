#!/bin/bash

set -o errexit -o pipefail

# This script takes the built Hugo site and:
#   - creates a new S3 bucket named according to whether the action is a push or pull_request.
#   - creates a list of all Hugo-generated client-side ("meta-refresh") redirects that
#   - we'll use to produce proper 301s later.
#   - pushes the content of the website into the new S3 bucket.
#   - tests the built website, first for broken links, then with Cypress to ensure pages
#   - render and behave properly.
#   - emits a metadata file containing information about the commit and bucket, which
#   - Pulumi will use to process its update.
#   - writes a record to AWS Parameter Store relating the generated bucket to the commit
#   - responsible for producing it.
#   - Posts a PR comment back to GitHub, if applicable.

source ./scripts/ci/common.sh

# The docroot of the built website.
build_dir="public"

# The text file we'll write as an output result.
metadata_file="$(origin_bucket_metadata_filepath)"

# Verify we have at least 1000 index.html files in total across the site.
if [ ! "$(find $build_dir -type f | grep index.html | wc -l)" -ge 1000 ]; then
    echo "Page-count check failed. Exiting."
    exit 1
fi

# For previews, name the destination bucket with the PR number, to reduce the number of
# buckets we create and to facilitate shorter sync times.
destination_bucket="$(origin_bucket_prefix)-$(build_identifier)"
destination_bucket_uri="s3://${destination_bucket}"

# Make the bucket. If this fails, there are two explanations, given the way we're naming
# our buckets: either a previous run failed at some point after creating the bucket, in
# which case we should simply proceed (to repopulate it), or the bucket was somehow
# created in another account, in which case subsequent operations on the bucket will also
# fail, causing this script to exit nonzero. In either case, it's okay to continue.
aws s3 mb $destination_bucket_uri --region "$(aws_region)" || true
aws s3api put-bucket-tagging --bucket $destination_bucket --tagging "TagSet=[{$(aws_owner_tag)}]" --region "$(aws_region)"

# Make the bucket an S3 website.
aws s3 website $destination_bucket_uri --index-document index.html --error-document 404.html --region "$(aws_region)"

# Sync the local build directory to the bucket. Note that we do pass the --delete option
# here, since in most cases, we'll be continually updating a bucket associated with a PR;
# passing this option keeps the destination bucket clean.
echo "Synchronizing to $destination_bucket_uri..."
aws s3 sync "$build_dir" "$destination_bucket_uri" --acl public-read --delete --quiet --region "$(aws_region)"

echo "Sync complete."
s3_website_url="http://${destination_bucket}.s3-website.$(aws_region).amazonaws.com"
echo "$s3_website_url"

# Set the content-type of latest-version explicitly. (Otherwise, it'll be set as binary/octet-stream.)
aws s3 cp "$build_dir/latest-version" "${destination_bucket_uri}/latest-version" \
    --content-type "text/plain" --acl public-read --region "$(aws_region)" --metadata-directive REPLACE

# At this point, we have a bucket that's suitable for deployment. As a result of this run,
# we leave a file in the project root indicating the name of the bucket that was generated
# and the associated commit SHA, and then we upload that file into the bucket as well, for
# reference. The Pulumi program will expect this file to exist, and will use the bucket
# name to set the CloudFront origin on the next Pulumi run.
#
# Why use a local file and not `pulumi config`, or some other persistence store? Because
# we need ensure that every CI job deploys only what it was responsible for building.
# Coupled with the locking we get from the Pulumi Service, using a local file is a safe
# way to ensure we're deploying what we just finished building and testing.
echo "Writing result metadata."
metadata='{
    "timestamp": %s,
    "commit": "%s",
    "bucket": "%s",
    "url": "%s"
}'
printf "$metadata" "$(current_time_in_ms)" "$(git_sha)" "$destination_bucket" "$s3_website_url" > "$metadata_file"

# Copy the file to the destination bucket, for future reference.
aws s3 cp "$metadata_file" "${destination_bucket_uri}/metadata.json" --region "$(aws_region)" --acl public-read

# Persist an association between the current commit and the bucket we just deployed to.
set_bucket_for_commit "$(git_sha)" "$destination_bucket" "$(aws_region)"

# Finally, post a comment to the PR that directs the user to the resulting bucket URL.
pr_comment_api_url="$(cat "$GITHUB_EVENT_PATH" | jq -r ".pull_request._links.comments.href")"
post_github_pr_comment \
    "Your site preview for commit $(git_sha_short) is ready! :tada:\n\n${s3_website_url}." \
    $pr_comment_api_url

echo "Done! The bucket website is now built and available at ${s3_website_url}."

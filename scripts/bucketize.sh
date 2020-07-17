#!/bin/bash

# Exit on any non-zero status or unbound variable, and print all commands to the terminal.
set -euo pipefail

source ./scripts/common.sh

# This script takes the built Hugo site and:
#   * creates a new S3 bucket named with the current Git SHA and a timestamp (of now)
#   * creates a list of all Hugo-generated client-side ("meta-refresh") redirects
#   * pushes the content of the website into the new S3 bucket
#   * converts all client-side redirects into HTTP 301s
#   * tests the built website with a headless browser to ensure pages are rendering and
#     behaving properly
#   * sets a Pulumi stack-configuration item marking the new, tested bucket as the one to
#     be used on the next Pulumi update

# The docroot of the built website.
build_dir="public"

# The text file we'll write as an output result.
metadata_file="origin-bucket-metadata.json"

# Verify we have at least 1000 index.html files in total across the site.
if [ ! "$(find $build_dir -type f | grep index.html | wc -l)" -ge 1000 ]; then
    echo "Page-count check failed. See the archive extraction log above for details."
    exit 1
fi

# The S3 bucket to publish to. We name this using both Git SHA and timestamp to
# be sure every run produces its own bucket.
now="$(date '+%Y%m%d%H%M%S')"
git_sha="$(git rev-parse HEAD)"
git_sha_short="$(git rev-parse --short HEAD)"
destination_bucket="pulumi-docs-origin-${git_sha_short}-${now}"
destination_bucket_uri="s3://${destination_bucket}"

# Log in and select the target stack.
run_pulumi_login
run_pulumi_stack_select

# Translate Hugo redirects into 301s. Note that we do this before syncing the site, as
# having the redirects available for reference can be helpful for debugging purposes.
node scripts/translate-redirects.js "$build_dir" "$(run_pulumi_config get redirectDomain || echo '')"

# Read the region from the stack's config -- we use it below.
aws_region="$(run_pulumi_config get 'aws:region')"

# Push site content to the bucket.
echo "Synchronizing to $destination_bucket_uri..."
aws s3 mb $destination_bucket_uri --region $aws_region
aws s3 website $destination_bucket_uri --index-document index.html --error-document 404.html
aws s3 sync "$build_dir" "$destination_bucket_uri" --acl public-read

echo "Sync complete."
s3_website_url="http://${destination_bucket}.s3-website.${aws_region}.amazonaws.com"
echo "$s3_website_url"

# Create an S3 object for each of the items in the redirect list so it returns a 301
# redirect (instead of serving the HTML with a meta-redirect). This ensures the right HTTP
# response code is returned for search engines and enables better support for URL anchors.
echo "Processing S3 redirects..."
IFS="|"
while read key location; do
    echo "Redirecting $key to $location (${destination_bucket})"
    aws s3api put-object --key "$key" --website-redirect-location "$location" --bucket "$destination_bucket" --acl public-read
done < $build_dir/redirects.txt

# Set the content-type of latest-version explicitly. (Otherwise, it'll be set as binary/octet-stream.)
aws s3 cp "$build_dir/latest-version" "${destination_bucket_uri}/latest-version" \
    --content-type "text/plain" --acl public-read --metadata-directive REPLACE

echo "Done! The bucket website is now built and available at ${s3_website_url}."

# Smoke test the deployed website. Specs are in ../cypress/integration.
echo "Running tests..."
CYPRESS_BASE_URL="$s3_website_url" yarn run cypress run --headless

# At this point, we have a bucket that's suitable for deployment. As a result of this run,
# we leave a file in the project root indicating the name of the bucket that was generated
# and the associated commit SHA, and then we upload that file into the bucket as well, for
# reference. The Pulumi program will expect this file to exist, and will use the bucket
# name to set the CloudFront origin on the next Pulumi run.
#
# Why use a local file and not `pulumi config`, or some other persistence store? Because
# we need ensure that every CI job deploys only what it was responsible for building. If
# we wrote to an async store in this step, and read from that store in the follow-on
# Pulumi job, it'd be easy for anothe Pulumi run to pick up and deploy this job's
# artifact, or vice-versa. Coupled with the locking we get from the Pulumi Service, using
# a local file is the safest way to ensure we're always deploying what we think we are.
echo "Writing result metadata."
metadata='{
    "bucket": "%s",
    "commit": "%s"
}'
printf "$metadata" "$destination_bucket" "$git_sha" > "$result_file"

# Copy the file to the destination bucket, for future reference.
aws s3 cp "$result_file" "${destination_bucket_uri}/metadata.json" --region $aws_region --acl public-read

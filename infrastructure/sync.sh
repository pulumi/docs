#!/bin/sh

# S3 URL of the website tarball.
site_archive="$1"

# S3 URL of the destination website bucket (e.g., the one hosting www.pulumi.com).
site_bucket="$2"

if [ -z "$site_archive" ]; then
    echo "Missing argument: site_archive"
    exit 1
fi

if [ -z "$site_bucket" ]; then
    echo "Missing argument: site_bucket"
    exit 1
fi

# Download the archive from the archive bucket and unpack it into a local folder.
echo "Downloading $site_archive..."
aws s3 cp $site_archive .
mkdir site_contents
tar -xzvf $(basename "$site_archive") -C site_contents

# Verify index.html exists in the root.
if [ ! -f "site_contents/index.html" ]; then
    echo "Missing root index.html. See the archive extraction log above for details."
    exit 1
fi

# Verify we have at least 1000 index.html files in total across the site.
if [ ! "$(find site_contents -type f | grep index.html | wc -l)" -ge 1000 ]; then
    echo "Page-count check failed. See the archive extraction log above for details."
    exit 1
fi

# Upload the JS and CSS bundles first.
cd site_contents

for file in $(find css -name "styles.*.css") ; do
    aws s3 cp "$file" "$site_bucket/$file" --acl public-read
done

for file in $(find js -name "bundle.min.*.js") ; do
    aws s3 cp "$file" "$site_bucket/$file"  --acl public-read
done

cd ..

# Synchronize the remaining contents of the local folder and site bucket, deleting
# whatever files exist remotely but not locally.
echo "Synchronizing to $site_bucket..."
aws s3 sync site_contents "$site_bucket" --acl public-read --delete

# Create an S3 object for each of the items in the redirect list so it returns a 301
# redirect (instead of serving the HTML with a meta-redirect). This ensures the right HTTP
# code response is returned for search engines and enables better support for URL anchors.
IFS="|"
while read key location; do
    echo "Redirect $key to $location (${site_bucket:5})"
    aws s3api put-object --key "$key" --website-redirect-location "$location" --bucket "${site_bucket:5}" --acl public-read
done < site_contents/redirects.txt

# Set the content-type of latest-version explicitly. (Otherwise, it'll be set as binary/octet-stream.)
aws s3 cp "site_contents/latest-version" "$site_bucket/latest-version" \
    --content-type "text/plain" --acl public-read --metadata-directive REPLACE

echo "Done!"

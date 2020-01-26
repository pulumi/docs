#!/bin/sh

site_archive=$1
site_bucket=$2

# Download the archive from the archive bucket and unpack it into a local folder.
echo "Downloading $site_archive..."
aws s3 cp $site_archive .
mkdir site_contents
tar -xzvf $(basename $site_archive) -C site_contents

# Upload the JS and CSS bundles first.
cd site_contents

for file in $(find css -name "styles.*.css") ; do
    aws s3 cp "$file" "$site_bucket/$file"
done

for file in $(find js -name "bundle.min.*.js") ; do
    aws s3 cp "$file" "$site_bucket/$file"
done

cd ..

# Synchronize the contents of the local folder and site bucket, deleting whatever files
# exist remotely but not locally.
echo "Synchronizing to $site_bucket..."
aws s3 sync site_contents $site_bucket --acl public-read --delete

echo "Done!"

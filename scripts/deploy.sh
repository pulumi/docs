#!/bin/bash

# Deploy the built website to an S3 bucket. The newly updated files will be
# picked up by the docs website backend.

set -o nounset -o errexit -o pipefail

CURRENT_COMMIT=$(git rev-parse HEAD)
ENVIRONMENT=${1:-}

if [ -z ${ENVIRONMENT} ]; then
    echo "Usage: $0 <environment>"
    exit 1
fi

if [[ -z ${AWS_ACCESS_KEY_ID:-} || -z ${AWS_SECRET_ACCESS_KEY:-} || -z ${AWS_REGION:-} ]]; then
    echo "Error: Missing AWS credentials. Unable to deploy built website."
    exit 1
fi

# AWS credentials are expected to be provided to the Travis job, and that
# account should be able to assume role to get the access needed for S3.
aws configure set aws_access_key_id ${AWS_ACCESS_KEY_ID}
aws configure set aws_secret_access_key ${AWS_SECRET_ACCESS_KEY}
aws configure set region ${AWS_REGION}

echo "Assuming the role of UploadPulumiReleases, uploading ${ENVIRONMENT} at ${CURRENT_COMMIT:0:6}..."
CREDS_JSON=$(aws sts assume-role \
    --role-arn "arn:aws:iam::058607598222:role/UploadPulumiReleases" \
    --role-session-name "docs-release_${ENVIRONMENT}_${CURRENT_COMMIT:0:6}" \
    --external-id "upload-docs-release")

export AWS_ACCESS_KEY_ID=$(echo ${CREDS_JSON}     | jq ".Credentials.AccessKeyId" --raw-output)
export AWS_SECRET_ACCESS_KEY=$(echo ${CREDS_JSON} | jq ".Credentials.SecretAccessKey" --raw-output)
export AWS_SECURITY_TOKEN=$(echo ${CREDS_JSON}    | jq ".Credentials.SessionToken" --raw-output)

aws s3 sync ./_site/ s3://rel.pulumi.com/docs/${ENVIRONMENT}

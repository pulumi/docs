import pulumi
import pulumi_aws as aws

# Get the account ID of the current user as a Pulumi output.
account_id = aws.get_caller_identity_output().apply(
    lambda identity: identity.account_id
)

# Create an S3 bucket.
bucket = aws.s3.Bucket("my-bucket")

# Create an S3 bucket policy allowing anyone in the account to list the contents of the bucket.
policy = aws.s3.BucketPolicy(
    "my-bucket-policy",
    bucket=bucket.id,
    policy=pulumi.Output.json_dumps(
        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {
                        "AWS": pulumi.Output.format("arn:aws:iam::{0}:root", account_id)
                    },
                    "Action": "s3:ListBucket",
                    "Resource": bucket.arn,
                }
            ],
        }
    ),
)

# Export the name of the bucket
pulumi.export("bucketName", bucket.id)

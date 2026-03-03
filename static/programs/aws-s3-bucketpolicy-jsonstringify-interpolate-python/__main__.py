import pulumi
import pulumi_aws as aws

# Create an S3 bucket.
bucket = aws.s3.Bucket("my-bucket")

# Create an S3 bucket policy that grants read access to all objects in the bucket.
# The Resource field uses pulumi.Output.concat to append "/*" to the bucket ARN,
# targeting individual objects rather than the bucket itself.
policy = aws.s3.BucketPolicy(
    "my-bucket-policy",
    bucket=bucket.id,
    policy=pulumi.Output.json_dumps(
        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": "*",
                    "Action": "s3:GetObject",
                    "Resource": pulumi.Output.concat(bucket.arn, "/*"),
                }
            ],
        }
    ),
)

# Export the name of the bucket.
pulumi.export("bucketName", bucket.id)

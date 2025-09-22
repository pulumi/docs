import json
import pulumi
import pulumi_aws as aws

bucket = aws.s3.Bucket("my-bucket")

ownership_controls = aws.s3.BucketOwnershipControls(
    "ownership-controls",
    bucket=bucket.id,
    rule=aws.s3.BucketOwnershipControlsRuleArgs(
        object_ownership="ObjectWriter",
    ),
)

public_access_block = aws.s3.BucketPublicAccessBlock(
    "public-access-block",
    bucket=bucket.id,
    block_public_acls=False,
)

bucket_metric = aws.s3.BucketMetric(
    "my-bucket-metric",
    bucket=bucket.id,
)

bucket_notification = aws.s3.BucketNotification(
    "my-bucket-notification",
    bucket=bucket.id,
)

bucket_object = aws.s3.BucketObject(
    "my-bucket-object",
    bucket=bucket.id,
    content="hello world",
    opts=pulumi.ResourceOptions(depends_on=[public_access_block, ownership_controls]),
)


def public_read_policy_for_bucket(bucket_name):
    return pulumi.Output.all(bucket_name).apply(
        lambda args: json.dumps(
            {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Effect": "Allow",
                        "Principal": "*",
                        "Action": "s3:GetObject",
                        "Resource": f"arn:aws:s3:::{args[0]}/*",
                    }
                ],
            }
        )
    )


bucket_policy = aws.s3.BucketPolicy(
    "my-bucket-policy",
    bucket=bucket.id,
    policy=bucket.id.apply(public_read_policy_for_bucket),
    opts=pulumi.ResourceOptions(depends_on=[public_access_block, ownership_controls]),
)

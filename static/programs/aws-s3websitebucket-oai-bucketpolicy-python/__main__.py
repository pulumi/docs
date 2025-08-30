import pulumi
import pulumi_aws as aws
import json

bucket = aws.s3.Bucket("content-bucket")

bucket_ownership = aws.s3.BucketOwnershipControls(
    "content-bucket",
    bucket=bucket.bucket,
    rule={"objectOwnership": "BucketOwnerPreferred"}
)

bucket_acl = aws.s3.BucketAcl("content-bucket",
    bucket=bucket.bucket,
    acl="private",
    opts=pulumi.ResourceOptions(depends_on=[bucket_ownership]),
)

bucket_website = aws.s3.BucketWebsiteConfiguration(
    "content-bucket",
    bucket=bucket.id,
    index_document={"suffix": "index.html"},
    error_document={"key": "404.html"},
)

origin_access_identity = aws.cloudfront.OriginAccessIdentity(
    "cloudfront",
    comment=pulumi.Output.concat("OAI-", bucket.id),
)

bucket_policy = aws.s3.BucketPolicy(
    "cloudfront-bucket-policy",
    bucket=bucket.bucket,
    policy=pulumi.Output.all(
        cloudfront_iam_arn=origin_access_identity.iam_arn,
        bucket_arn=bucket.arn
    ).apply(
        lambda args: json.dumps(
            {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Sid": "CloudfrontAllow",
                        "Effect": "Allow",
                        "Principal": {
                            "AWS": args["cloudfront_iam_arn"],
                        },
                        "Action": "s3:GetObject",
                        "Resource": f"{args['bucket_arn']}/*",
                    }
                ],
            }
        )
    ),
    opts=pulumi.ResourceOptions(parent=bucket)
)

import pulumi
import pulumi_aws as aws

bucket = aws.s3.Bucket("bucket")

file = aws.s3.BucketObject("bucket-object",
    bucket=bucket.id,
    key="some-file.txt",
    content="some-content",
)

# concat takes a list of args and concatenates all of them into a single output:
s3Url1 = pulumi.Output.concat("s3://", bucket.bucket, "/", file.key)

# format takes a template string and a list of args or keyword args and formats the string, expanding outputs correctly:
s3Url2 = pulumi.Output.format("s3://{0}/{1}", bucket.bucket, file.key)

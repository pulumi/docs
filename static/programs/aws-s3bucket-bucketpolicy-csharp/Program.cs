using Pulumi;
using Pulumi.Aws.Iam;
using Pulumi.Aws.S3;
using System.Collections.Generic;
using System.Text.Json;

return await Deployment.RunAsync(() =>
{
    var bucket = new Bucket("myBucket");

    var s3BucketPolicyDocument = bucket.Arn.Apply(arn => JsonSerializer.Serialize(new
    {
        Version = "2012-10-17",
        Statement = new[]
        {
            new
            {
                Effect = "Allow",
                Principal = new { Service = "lambda.amazonaws.com" },
                Action = new[] { "s3:PutObject", "s3:PutObjectAcl" },
                Resource = $"{arn}/*"
            }
        }
    }));

    var bucketPolicy = new BucketPolicy("myBucketPolicy", new BucketPolicyArgs
    {
        Bucket = bucket.Id,
        Policy = s3BucketPolicyDocument
    });

    return new Dictionary<string, object?>
    {
        ["bucketName"] = bucket.Id,
        ["bucketArn"] = bucket.Arn
    };
});

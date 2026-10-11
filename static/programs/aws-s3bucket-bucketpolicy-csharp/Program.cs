using System.Collections.Generic;
using Pulumi;
using Pulumi.Aws.S3;

return await Deployment.RunAsync(() =>
{
    var bucket = new Bucket("myBucket");

    var bucketPolicy = new BucketPolicy("myBucketPolicy", new BucketPolicyArgs
    {
        Bucket = bucket.Id,
        Policy = Output.JsonSerialize(Output.Create(
            new
            {
                Version = "2012-10-17",
                Statement = new[]
                {
                    new
                    {
                        Effect = "Allow",
                        Principal = new { Service = "lambda.amazonaws.com" },
                        Action = new[] { "s3:PutObject", "s3:PutObjectAcl" },
                        Resource = Output.Format($"{bucket.Arn}/*"),
                    }
                }
            }
        ))
    });

    return new Dictionary<string, object?>
    {
        ["bucketName"] = bucket.Id,
        ["bucketArn"] = bucket.Arn
    };
});

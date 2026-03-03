using System.Collections.Generic;
using Pulumi;
using Pulumi.Aws.S3;

return await Deployment.RunAsync(() =>
{
    // Create an S3 bucket.
    var bucket = new Bucket("my-bucket");

    // Create an S3 bucket policy that grants read access to all objects in the bucket.
    // The Resource field uses Output.Format to append "/*" to the bucket ARN,
    // targeting individual objects rather than the bucket itself.
    var policy = new BucketPolicy("my-bucket-policy", new BucketPolicyArgs
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
                            Principal = "*",
                            Action = "s3:GetObject",
                            Resource = Output.Format($"{bucket.Arn}/*"),
                        }
                    }
                }
            ))
        }
    );

    // Export the name of the bucket.
    return new Dictionary<string, object?> { ["bucketName"] = bucket.Id };
});

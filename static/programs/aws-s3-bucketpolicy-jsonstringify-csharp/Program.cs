using System.Collections.Generic;
using Pulumi;
using Pulumi.Aws.S3;

return await Deployment.RunAsync(() =>
{
    // Get the account ID of the current user as a Pulumi output.
    var accountID = Pulumi.Aws.GetCallerIdentity.Invoke().Apply(identity => identity.AccountId);

    // Create an S3 bucket.
    var bucket = new Bucket("my-bucket");

    // Create an S3 bucket policy allowing anyone in the account to list the contents of the bucket.
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
                            Principal = new
                            {
                                AWS = Output.Format($"arn:aws:iam::{accountID}:root")
                            },
                            Action = "s3:ListBucket",
                            Resource = bucket.Arn,
                        }
                    }
                }
            ))
        }
    );

    // Export the name of the bucket.
    return new Dictionary<string, object?> { ["bucketName"] = bucket.Id };
});

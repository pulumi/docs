using System.Collections.Generic;
using System.Text.Json;
using Pulumi;
using Aws = Pulumi.Aws;

return await Deployment.RunAsync(() =>
{
    var bucket = new Aws.S3.Bucket("my-bucket");

    var ownershipControls = new Aws.S3.BucketOwnershipControls(
        "ownership-controls",
        new()
        {
            Bucket = bucket.Id,
            Rule = new Aws.S3.Inputs.BucketOwnershipControlsRuleArgs
            {
                ObjectOwnership = "ObjectWriter"
            }
        }
    );

    var publicAccessBlock = new Aws.S3.BucketPublicAccessBlock(
        "public-access-block",
        new() { Bucket = bucket.Id, BlockPublicAcls = false }
    );

    var bucketMetric = new Aws.S3.BucketMetric("my-bucket-metric", new() { Bucket = bucket.Id });

    var bucketNotification = new Aws.S3.BucketNotification(
        "my-bucket-notification",
        new() { Bucket = bucket.Id }
    );

    var bucketObject = new Aws.S3.BucketObject(
        "my-bucket-object",
        new Aws.S3.BucketObjectArgs { Bucket = bucket.Id, Content = "hello world" },
        new CustomResourceOptions
        {
            DependsOn = new List<Resource> { publicAccessBlock, ownershipControls }
        }
    );

    var bucketPolicy = new Aws.S3.BucketPolicy(
        "my-bucket-policy",
        new() { Bucket = bucket.Id, Policy = bucket.Id.Apply(id => PublicReadPolicyForBucket(id)) },
        new CustomResourceOptions
        {
            DependsOn = new List<Resource> { publicAccessBlock, ownershipControls }
        }
    );

    return new Dictionary<string, object?> { { "bucketName", bucket.Id } };
});

static string PublicReadPolicyForBucket(string bucketName)
{
    return JsonSerializer.Serialize(
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
                    Resource = $"arn:aws:s3:::{bucketName}/*"
                }
            }
        }
    );
}

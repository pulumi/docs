using Pulumi;
using Pulumi.Aws.S3;
using Pulumi.Aws.S3.Inputs;
using Pulumi.Aws.Iam;
using Pulumi.Aws.CloudFront;
using System.Collections.Generic;
using System.Text.Json;

return await Deployment.RunAsync(() =>
{
    var bucket = new Bucket("content-bucket");

    var bucketAcl = new BucketAcl("content-bucket", new() {
        Bucket = bucket.Id,
        Acl = "private",
    });

    var bucketOwnership = new BucketOwnershipControls("content-bucket", new() {
        Bucket = bucket.Id,
        Rule = new BucketOwnershipControlsRuleArgs
        {
            ObjectOwnership = "BucketOwnerPreferred",
        },
    }, new CustomResourceOptions { DependsOn = { bucketAcl }});

    var bucketWebsite = new BucketWebsiteConfiguration("content-bucket", new() {
        Bucket = bucket.Id,
        IndexDocument = new BucketWebsiteConfigurationIndexDocumentArgs
        {
            Suffix = "index.html"
        },
        ErrorDocument = new BucketWebsiteConfigurationErrorDocumentArgs
        {
            Key = "404.html"
        },
    });

    var originAccessIdentity = new OriginAccessIdentity("cloudfront", new OriginAccessIdentityArgs
    {
        Comment = Output.Format($"OAI-{bucket.Id}"),
    });

    var bucketPolicy = new BucketPolicy("cloudfront-bucket-policy", new BucketPolicyArgs
    {
        Bucket = bucket.Id,
        Policy = Output.Tuple(bucket.Arn, originAccessIdentity.IamArn)
        .Apply(t =>
        {
            string bucketArn = t.Item1;
            string cloudfrontIamArn = t.Item2;

            var policy = new
            {
                Version = "2012-10-17",
                Statement = new object[]
                {
                    new
                    {
                        Sid = "CloudfrontAllow",
                        Effect = "Allow",
                        Principal = new { AWS = cloudfrontIamArn },
                        Action = "s3:GetObject",
                        Resource = $"{bucketArn}/*",
                    },
                },
            };

            return JsonSerializer.Serialize(policy);
        }),
    }, new CustomResourceOptions { Parent = bucket });
});

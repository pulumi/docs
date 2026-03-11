using System;
using System.Collections.Generic;

using Pulumi;
using Pulumi.Aws.S3;
using Pulumi.Aws.S3.Inputs;

using Newtonsoft.Json;

public sealed class StaticPageArgs : ResourceArgs {
    [Input("indexContent")]
    public Input<string> IndexContent { get; set; } = null!;
}

class StaticPage : ComponentResource {
    [Output("endpoint")]
    public Output<string> Endpoint { get; set; }

    public StaticPage(string name, StaticPageArgs args, ComponentResourceOptions? opts = null)
        : base("sample-components:index:StaticPage", name, args, opts)
    {
        var bucket = new Bucket($"{name}-bucket", new() { }, new() { Parent = this });

        var bucketWebsite = new BucketWebsiteConfiguration($"{name}-website", new() {
            Bucket = bucket.BucketName,
            IndexDocument = new BucketWebsiteConfigurationIndexDocumentArgs { Suffix = "index.html" },
        }, new() { Parent = this });

        var bucketObject = new BucketObject($"{name}-index-object", new BucketObjectArgs {
            Bucket = bucket.BucketName,
            Key = "index.html",
            Content = args.IndexContent,
            ContentType = "text/html",
        }, new() { Parent = this });

        var publicAccessBlock = new BucketPublicAccessBlock($"{name}-public-access-block", new() {
            Bucket = bucket.BucketName,
            BlockPublicAcls = false,
        }, new() { Parent = this });

        var bucketPolicy = new BucketPolicy($"{name}-bucket-policy", new() {
            Bucket = bucket.BucketName,
            Policy = bucket.Id.Apply(this.AllowGetObjectPolicy),
        }, new() { Parent = this, DependsOn = publicAccessBlock });

        this.Endpoint = bucketWebsite.WebsiteEndpoint;

        this.RegisterOutputs(new Dictionary<string, object?> {
            ["endpoint"] = bucketWebsite.WebsiteEndpoint
        });
    }

    private string AllowGetObjectPolicy(string bucketName) {
        return JsonConvert.SerializeObject(new {
            Version = "2012-10-17",
            Statement = new[] { new {
                Effect = "Allow",
                Principal = "*",
                Action = new[] {
                    "s3:GetObject"
                },
                Resource = new[] {
                    $"arn:aws:s3:::{bucketName}/*"
                }
            }}
        });
    }
}

---
title: "How to Serve S3 Content Through CloudFront CDN with Pulumi"
meta_desc: "Distribute static website content globally with low latency using AWS CloudFront CDN and S3 bucket as origin with Pulumi in TypeScript, Python, Go, C#, or Java."
canonical_url: "https://www.pulumi.com/recipes/aws/s3-cloudfront-cdn"
date: 2025-10-08
category: "Storage"
tags: ["aws", "s3", "cloudfront", "cdn", "static-website"]
faq:
  - question: What is the difference between Origin Access Control and Origin Access Identity?
    answer: Origin Access Control (OAC) is the newer, recommended method to secure S3 origins. OAC supports all S3 buckets, SSE-KMS encryption, and more AWS Regions compared to the legacy Origin Access Identity (OAI). AWS recommends migrating from OAI to OAC for new distributions.
  - question: How long does it take for CloudFront to deploy?
    answer: CloudFront distributions typically take 15-20 minutes to fully deploy and propagate to all edge locations worldwide. During this time, the distribution status will show as 'InProgress'. You can access your content once the status changes to 'Deployed'.
  - question: How do I update content that's already cached?
    answer: You can create a CloudFront invalidation to immediately remove content from edge caches. Use the aws.cloudfront.Invalidation resource in Pulumi. Note that the first 1,000 invalidation paths per month are free, with $0.005 per path after that.
  - question: Can I use my custom domain with CloudFront?
    answer: Yes, you can add custom domain names (CNAMEs) to your CloudFront distribution. You'll need to create an ACM certificate in us-east-1 region for your domain and configure DNS records to point to the CloudFront distribution domain name.
  - question: How much does CloudFront cost compared to serving directly from S3?
    answer: CloudFront costs approximately $0.085/GB for the first 10TB in the US (cheaper for higher volumes), compared to S3's $0.09/GB for data transfer out to the internet. CloudFront is usually cost-effective for frequently accessed content due to caching, and provides better performance globally.
---

## How do I serve S3 content through CloudFront CDN?

**To distribute S3 content globally with low latency**, create a CloudFront distribution with your S3 bucket as the origin. CloudFront caches your content at edge locations worldwide, reducing latency for users and offloading traffic from your S3 bucket. The following example shows how to configure this in TypeScript, Python, Go, C#, and Java.

{{< chooser language "typescript,python,go,csharp,java" >}}
{{% choosable language typescript %}}
```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const s3OriginId = "myS3Origin";

const s3Distribution = new aws.cloudfront.Distribution("s3_distribution", {
    origins: [{
        domainName: b.bucketRegionalDomainName,
        originAccessControlId: _default.id,
        originId: s3OriginId,
    }],
    enabled: true,
    isIpv6Enabled: true,
    comment: "Some comment",
    defaultRootObject: "index.html",
    defaultCacheBehavior: {
        allowedMethods: [
            "DELETE", "GET", "HEAD", "OPTIONS",
            "PATCH", "POST", "PUT"
        ],
        cachedMethods: ["GET", "HEAD"],
        targetOriginId: s3OriginId,
        forwardedValues: {
            queryString: false,
            cookies: { forward: "none" },
        },
        viewerProtocolPolicy: "allow-all",
        minTtl: 0,
        defaultTtl: 3600,
        maxTtl: 86400,
    },
});
```
{{% /choosable %}}

{{% choosable language python %}}
```python
import pulumi
import pulumi_aws as aws

s3_origin_id = "myS3Origin"

s3_distribution = aws.cloudfront.Distribution("s3_distribution",
    origins=[aws.cloudfront.DistributionOriginArgs(
        domain_name=b.bucket_regional_domain_name,
        origin_access_control_id=default.id,
        origin_id=s3_origin_id,
    )],
    enabled=True,
    is_ipv6_enabled=True,
    comment="Some comment",
    default_root_object="index.html",
    default_cache_behavior=aws.cloudfront.DistributionDefaultCacheBehaviorArgs(
        allowed_methods=[
            "DELETE", "GET", "HEAD", "OPTIONS",
            "PATCH", "POST", "PUT"
        ],
        cached_methods=["GET", "HEAD"],
        target_origin_id=s3_origin_id,
        forwarded_values=aws.cloudfront.DistributionDefaultCacheBehaviorForwardedValuesArgs(
            query_string=False,
            cookies=aws.cloudfront.DistributionDefaultCacheBehaviorForwardedValuesCookiesArgs(
                forward="none",
            ),
        ),
        viewer_protocol_policy="allow-all",
        min_ttl=0,
        default_ttl=3600,
        max_ttl=86400,
    ))
```
{{% /choosable %}}

{{% choosable language go %}}
```go
package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v7/go/aws/cloudfront"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		s3OriginId := "myS3Origin"

		_, err := cloudfront.NewDistribution(ctx, "s3_distribution", &cloudfront.DistributionArgs{
			Origins: cloudfront.DistributionOriginArray{
				&cloudfront.DistributionOriginArgs{
					DomainName:            b.BucketRegionalDomainName,
					OriginAccessControlId: _default.Id,
					OriginId:              pulumi.String(s3OriginId),
				},
			},
			Enabled:           pulumi.Bool(true),
			IsIpv6Enabled:     pulumi.Bool(true),
			Comment:           pulumi.String("Some comment"),
			DefaultRootObject: pulumi.String("index.html"),
			DefaultCacheBehavior: &cloudfront.DistributionDefaultCacheBehaviorArgs{
				AllowedMethods: pulumi.StringArray{
					pulumi.String("DELETE"), pulumi.String("GET"), pulumi.String("HEAD"),
					pulumi.String("OPTIONS"), pulumi.String("PATCH"), pulumi.String("POST"),
					pulumi.String("PUT"),
				},
				CachedMethods: pulumi.StringArray{
					pulumi.String("GET"),
					pulumi.String("HEAD"),
				},
				TargetOriginId: pulumi.String(s3OriginId),
				ForwardedValues: &cloudfront.DistributionDefaultCacheBehaviorForwardedValuesArgs{
					QueryString: pulumi.Bool(false),
					Cookies: &cloudfront.DistributionDefaultCacheBehaviorForwardedValuesCookiesArgs{
						Forward: pulumi.String("none"),
					},
				},
				ViewerProtocolPolicy: pulumi.String("allow-all"),
				MinTtl:               pulumi.Int(0),
				DefaultTtl:           pulumi.Int(3600),
				MaxTtl:               pulumi.Int(86400),
			},
		})
		if err != nil {
			return err
		}
		return nil
	})
}
```
{{% /choosable %}}

{{% choosable language csharp %}}
```csharp
using System.Collections.Generic;
using Pulumi;
using Aws = Pulumi.Aws;

return await Deployment.RunAsync(() =>
{
    var s3OriginId = "myS3Origin";

    var s3Distribution = new Aws.CloudFront.Distribution("s3_distribution", new()
    {
        Origins = new[]
        {
            new Aws.CloudFront.Inputs.DistributionOriginArgs
            {
                DomainName = b.BucketRegionalDomainName,
                OriginAccessControlId = @default.Id,
                OriginId = s3OriginId,
            },
        },
        Enabled = true,
        IsIpv6Enabled = true,
        Comment = "Some comment",
        DefaultRootObject = "index.html",
        DefaultCacheBehavior = new Aws.CloudFront.Inputs.DistributionDefaultCacheBehaviorArgs
        {
            AllowedMethods = new[]
            {
                "DELETE", "GET", "HEAD", "OPTIONS",
                "PATCH", "POST", "PUT",
            },
            CachedMethods = new[]
            {
                "GET", "HEAD",
            },
            TargetOriginId = s3OriginId,
            ForwardedValues = new Aws.CloudFront.Inputs.DistributionDefaultCacheBehaviorForwardedValuesArgs
            {
                QueryString = false,
                Cookies = new Aws.CloudFront.Inputs.DistributionDefaultCacheBehaviorForwardedValuesCookiesArgs
                {
                    Forward = "none",
                },
            },
            ViewerProtocolPolicy = "allow-all",
            MinTtl = 0,
            DefaultTtl = 3600,
            MaxTtl = 86400,
        },
    });
});
```
{{% /choosable %}}

{{% choosable language java %}}
```java
package generated_program;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.aws.cloudfront.Distribution;
import com.pulumi.aws.cloudfront.DistributionArgs;
import com.pulumi.aws.cloudfront.inputs.DistributionOriginArgs;
import com.pulumi.aws.cloudfront.inputs.DistributionDefaultCacheBehaviorArgs;
import com.pulumi.aws.cloudfront.inputs.DistributionDefaultCacheBehaviorForwardedValuesArgs;
import com.pulumi.aws.cloudfront.inputs.DistributionDefaultCacheBehaviorForwardedValuesCookiesArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        var s3OriginId = "myS3Origin";

        var s3Distribution = new Distribution("s3_distribution", DistributionArgs.builder()
            .origins(DistributionOriginArgs.builder()
                .domainName(b.bucketRegionalDomainName())
                .originAccessControlId(default_.id())
                .originId(s3OriginId)
                .build())
            .enabled(true)
            .isIpv6Enabled(true)
            .comment("Some comment")
            .defaultRootObject("index.html")
            .defaultCacheBehavior(DistributionDefaultCacheBehaviorArgs.builder()
                .allowedMethods(
                    "DELETE", "GET", "HEAD", "OPTIONS",
                    "PATCH", "POST", "PUT")
                .cachedMethods("GET", "HEAD")
                .targetOriginId(s3OriginId)
                .forwardedValues(DistributionDefaultCacheBehaviorForwardedValuesArgs.builder()
                    .queryString(false)
                    .cookies(DistributionDefaultCacheBehaviorForwardedValuesCookiesArgs.builder()
                        .forward("none")
                        .build())
                    .build())
                .viewerProtocolPolicy("allow-all")
                .minTtl(0)
                .defaultTtl(3600)
                .maxTtl(86400)
                .build())
            .build());
    }
}
```
{{% /choosable %}}
{{< /chooser >}}

## Key configuration details

**Origins configuration**: The `origins` array specifies your S3 bucket as the content source. Use `bucketRegionalDomainName` instead of `bucketDomainName` to avoid redirect issues in certain regions.

**Origin Access Control**: The `originAccessControlId` secures your S3 bucket by allowing only CloudFront to access it. Create an Origin Access Control resource separately and reference its ID here. This replaces the legacy Origin Access Identity.

**Cache behavior**: The `defaultCacheBehavior` defines how CloudFront caches and serves content. The example caches GET and HEAD requests for 1 hour (3600 seconds) by default.

**TTL settings**: Time-to-Live values control cache duration. `minTtl` (0), `defaultTtl` (3600), and `maxTtl` (86400) set the minimum, default, and maximum cache durations in seconds.

**IPv6 support**: Setting `isIpv6Enabled: true` allows CloudFront to serve content over IPv6, improving accessibility for IPv6-only clients.

**Viewer protocol policy**: The `allow-all` policy permits both HTTP and HTTPS. For production, consider using `redirect-to-https` or `https-only` for better security.

**Default root object**: Specifies the file (e.g., `index.html`) to serve when users request the root URL of your distribution.

## Frequently asked questions

**What is the difference between Origin Access Control and Origin Access Identity?**
Origin Access Control (OAC) is the newer, recommended method to secure S3 origins. OAC supports all S3 buckets, SSE-KMS encryption, and more AWS Regions compared to the legacy Origin Access Identity (OAI). AWS recommends migrating from OAI to OAC for new distributions.

**How long does it take for CloudFront to deploy?**
CloudFront distributions typically take 15-20 minutes to fully deploy and propagate to all edge locations worldwide. During this time, the distribution status will show as 'InProgress'. You can access your content once the status changes to 'Deployed'.

**How do I update content that's already cached?**
You can create a CloudFront invalidation to immediately remove content from edge caches. Use the aws.cloudfront.Invalidation resource in Pulumi. Note that the first 1,000 invalidation paths per month are free, with $0.005 per path after that.

**Can I use my custom domain with CloudFront?**
Yes, you can add custom domain names (CNAMEs) to your CloudFront distribution. You'll need to create an ACM certificate in us-east-1 region for your domain and configure DNS records to point to the CloudFront distribution domain name.

**How much does CloudFront cost compared to serving directly from S3?**
CloudFront costs approximately $0.085/GB for the first 10TB in the US (cheaper for higher volumes), compared to S3's $0.09/GB for data transfer out to the internet. CloudFront is usually cost-effective for frequently accessed content due to caching, and provides better performance globally.


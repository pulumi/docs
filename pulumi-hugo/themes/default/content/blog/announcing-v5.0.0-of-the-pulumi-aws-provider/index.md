---
title: "Announcing v5.0.0 of the Pulumi AWS Provider"
date: 2022-03-28
meta_desc: "v5.0.0 of the Pulumi AWS Provider is now available"
meta_image: meta.png
authors:
- paul-stack
tags:
- aws
---

We are excited to announce v5.0.0 of the Pulumi [AWS Classic](https://www.pulumi.com/registry/packages/aws/) provider. The AWS Classic provider is one of the most heavily used providers across the Pulumi ecosystem, and offers access to the full surface area of the upstream Terraform AWS Provider from within Pulumi projects in all supported Pulumi languages. The v5.0.0 release brings a substantial set of [fixes and improvements](https://github.com/hashicorp/terraform-provider-aws/blob/main/CHANGELOG.md#400-february-10-2022) to the provider, including a number of breaking
changes as part of the major version release.

<!--more-->

At Pulumi, we take compatibility seriously, and are concious of the impact that major version updates can have on developer adoption. To that end, it is always our goal to minimize the extent of breaking changes where possible, and to provide easy paths for adoption of new versions. Among the breaking changes that come along with the upstream provider update, one in particular has potential to be disruptive to common usage of the Pulumi AWS Classic provider - a change to the API for the AWS S3 Bucket resource which removes many features from the Bucket resource and introduces new resources to represent these capabilities.

In order to ensure that Pulumi AWS Classic users are not adversely impacted by this breaking change, we have extended the Pulumi AWS Classic provider to offer both the old implementation and the new implementation of the S3 Bucket resource. This means that all existing usages of S3 Bucket will continue to work as normal. We also now offer the ability to create a v2 variants of the S3 Bucket supported in the new upstream AWS provider.

Let's consider an existing implemention of an S3 Bucket that is used to create a static website:

{{< chooser language "typescript,python,csharp,go" >}}

{{% choosable language typescript %}}

```typescript
import * as aws from "@pulumi/aws";

const siteBucket = new aws.s3.Bucket("s3-website-bucket", {
    website: {
        indexDocument: "index.html",
    },
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
from pulumi_aws import s3

web_bucket = s3.Bucket('s3-website-bucket',
                       website=s3.BucketWebsiteArgs(
                       index_document="index.html",
                       ))
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using Pulumi;
using Pulumi.Aws.S3;
using Pulumi.Aws.S3.Inputs;

class WebsiteStack : Stack
{
    public WebsiteStack()
    {
        var bucket = new Bucket("my-bucket", new BucketArgs
        {
            Website = new BucketWebsiteArgs
            {
                IndexDocument = "index.html"
            }
        });
    }
}
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v4/go/aws/s3"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		_, err := s3.NewBucket(ctx, "s3-website-bucket", &s3.BucketArgs{
			Website: s3.BucketWebsiteArgs{
				IndexDocument: pulumi.String("index.html"),
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

{{% /chooser %}}

In the upstream provider, the S3 Bucket resource has been broken into multiple pieces meaning that you would need to move the website
part of the bucket out to be it's own resource. *We have ensured that this will continue to work in Pulumi.*

## What if I want to migrate to use the new implementation of an S3 Bucket?

The Pulumi AWS Provider, has introduced a new resource, `aws.s3.BucketV2` that users can use to create new variants of
how an S3 bucket resource would look. To create a static website using `BucketV2`, we can see that the code gets more
targetted toward the resource that we are writing:

{{< chooser language "typescript,python,csharp,go" >}}

{{% choosable language typescript %}}

```typescript
import * as aws from "@pulumi/aws";

const siteBucket = new aws.s3.BucketV2("s3-website-bucket");

const bucketWebsiteConfig = new aws.s3.BucketWebsiteConfigurationV2("website-config", {
   bucket: siteBucket.bucket,
   indexDocument: {
       suffix: "index.html"
   },
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
from pulumi_aws import s3

site_bucket = s3.BucketV2('s3-website-bucket')

website_config = aws.s3.BucketWebsiteConfigurationV2("website-config",
                                                     bucket=site_bucket.bucket,
                                                     index_document=aws.s3.BucketWebsiteConfigurationV2IndexDocumentArgs(
                                                        prefix="index.html",
                                                     ))
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using Pulumi;
using Pulumi.Aws.S3;
using Pulumi.Aws.S3.Inputs;

class WebsiteStack : Stack
{
    public WebsiteStack()
    {
        var siteBucket = new Bucket("s3-website-bucket", new BucketArgs{});

        var websiteConfig = new Aws.S3.BucketWebsiteConfigurationV2("website-config", new Aws.S3.BucketWebsiteConfigurationV2Args
        {
            Bucket = siteBucket.Bucket,
            IndexDocument = new Aws.S3.Inputs.BucketWebsiteConfigurationV2IndexDocumentArgs
            {
                Suffix = "index.html",
            },
        });
    }
}
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v4/go/aws/s3"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		siteBucket, err := s3.NewBucket(ctx, "s3-website-bucket", nil)
		if err != nil {
			return err
		}

		_, err := s3.NewBucketWebsiteConfigurationV2(ctx, "website-config", &s3.BucketWebsiteConfigurationV2Args{
			Bucket: siteBucket.bucket,
			IndexDocument: &s3.BucketWebsiteConfigurationV2IndexDocumentArgs{
				Suffix: pulumi.String("index.html"),
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

{{% /chooser %}}

## Can I migrate from `aws.s3.Bucket` to `aws.s3.BucketV2`?

Yes! As part of this major version, we have taken advantage of using [aliases]({{< relref "/docs/intro/concepts/resources/options/aliases" >}}) in Pulumi to be able to allow users to
change to `aws.s3.BucketV2` easily. An alias was added to the new `aws.s3.BucketV2` resource as follows:

```go
    "aws_s3_bucket": {
        Tok: awsResource(s3Mod, "BucketV2"),
        Aliases: []tfbridge.AliasInfo{
            {
                Type: stringRef("aws:s3/bucket:Bucket"),
            },
        },
    },
```

This ensures that when a user changes from `aws.s3.Bucket` to `aws.s3.BucketV2` that the Pulumi engine understands that
the bucket is not a new bucket but is an existing bucket that has changed. Therefore, the Pulumi engine will not destroy
the bucket and recreate it. This means that to change from 1 codebase to the other, we just need to keep the names of the
resources the same (e.g `s3-website-bucket` in the code above) and then continue to add the new code to satisfy the way the
resources need to be handed (e.g. `BucketWebsiteConfigurationV2` in the code above).

You can see the steps on how this works as follows:

{{< asciicast id="YMgxBRkaBv95iegpkgMjBy7Zt" >}}

Notice that the bucket is not recreate - the only change is the addition of the new aws s3 resource for the website configuration.
Your existing infrastructure is not going to change and thus we can easily migrate between the different resource types.

## Get Started Today!

You can browse our [API reference docs](https://www.pulumi.com/registry/packages/aws/) with inline examples or explore
the [Pulumi AWS SDKs](https://github.com/pulumi/pulumi-aws) repository to get started today!

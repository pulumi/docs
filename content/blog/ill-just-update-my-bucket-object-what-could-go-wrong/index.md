---
title: "I'll just update the bucket object. What could go wrong?"

# The date represents the post's publish date, and by default corresponds with
# the date this file was generated. Posts with future dates are visible in development,
# but excluded from production builds. Use the time and timezone-offset portions of
# of this value to schedule posts for publishing later.
date: 2022-09-12T08:33:30-07:00

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or social-media
# previews. This field is required or the build will fail the linter test.
# Max length is 160 characters.
meta_desc: The AWS Static Website Package makes it easy for you to update the content
  on your website by enabling atomic deployments and cache key customizations.

# The meta_image appears in social-media previews and on the blog home page.
# A placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: meta.png

# At least one author is required. The values in this list correspond with the `id`
# properties of the team member files at /data/team/team. Create a file for yourself
# if you don't already have one.
authors:
  - zack-chase

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
  - aws
  - static-website

# See the blogging docs at https://github.com/pulumi/docs/blob/master/BLOGGING.md.
# for additional details, and please remove these comments before submitting for review.
search:
  keywords:
    - website
    - wrong
    - bucket
    - atomic
    - update
    - websiteurl
    - object
---

Creating a website on AWS with an S3 bucket is a fairly straightforward task. You just need to create an S3 bucket, configure it to be a website, and add your content, right?

Unfortunately getting your content into a bucket is only a part of the story. To get your website ready to handle traffic, you will want to associate a domain name and likely want to use a CDN, like Cloudfront, to help with performance. The [AWS Static Website Package](/registry/packages/aws-static-website/) makes it easy for you to associate a domain and stand up a CDN with only a few arguments.

{{% chooser language "yaml,typescript,python,go,csharp" / %}}

{{% choosable language yaml %}}

```yaml
name: atomic-bucket-blog-yaml
description: An AWS Pulumi YAML program for provisioning a static website.
runtime: yaml
resources:
  web:
    type: "aws-static-website:index:Website"
    properties:
      sitePath: "./build"
outputs:
  websiteURL: ${web.websiteURL}
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as awsStaticWebsite from "@pulumi/aws-static-website";

const web = new awsStaticWebsite.Website("web", {
    sitePath: "./build"
});

export const websiteURL = web.websiteURL;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_aws_static_website as aws_static_website

web = aws_static_website.Website("web", site_path="./build")

pulumi.export("websiteURL", web.website_url)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	website "github.com/pulumi/pulumi-aws-static-website/sdk/go/aws-static-website"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		web, err := website.NewWebsite(ctx, "web", &website.WebsiteArgs{
			SitePath: pulumi.String("./build"),
		})
		if err != nil {
			return err
		}
		ctx.Export("websiteURL", web.WebsiteURL)
		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using Pulumi;
using AwsStaticWebsite = Pulumi.AwsStaticWebsite;

return await Deployment.RunAsync(() =>
{
    var web = new AwsStaticWebsite.Website("web", new()
    {
        SitePath = "./build",
    });

    return new Dictionary<string, object?>
    {
        ["websiteURL"] = web.WebsiteURL,
    };
});
```

{{% /choosable %}}

The only problem? Now you have to deal with keeping your content up to date without interrupting your website’s user experience.

## So what’s the problem?

When your website is still fairly small in size, updating the bucket objects in place probably seems like a decent strategy for updating your static website. Unfortunately updating the objects in place has a few rough edges that could lead to a degraded user experience.

First and foremost (in my opinion) is that you are introducing a chance for assets to not be available when the page needs them. For example, if an HTML page is updated with new CSS classes before the CSS itself is updated, then the website could have bad styling until the new CSS file is available.

Having a CDN to cache your content is helpful in mitigating deploy time issues, but it doesn’t eliminate them entirely. Different objects can have different expiration times, so you still risk an asset not being available if a cached paged is requesting an object that has expired.

## Versioning your website

To eliminate all the potential issues that could go wrong with an in-place update, you can version your website to ensure all your assets and dependencies are present and the cache behaves in the way you intend. While that may seem complicated, the AWS Static Website Package makes it simple for you to enable website versioning.

### Atomic Deployments

The first step for versioning is that you are going to need to build a new S3 Bucket on every deployment. You want to do this because it ensures all the assets and dependencies are present in the bucket before you associate it with your Cloudfront CDN.

To accomplish this with the AWS Static Website Package all you need to do is set the Atomic Deployment argument to `true`.

{{% chooser language "yaml,typescript,python,go,csharp" / %}}

{{% choosable language yaml %}}

```yaml
name: atomic-bucket-blog-yaml
description: An AWS Pulumi YAML program for provisioning a static website.
runtime: yaml
resources:
  web:
    type: "aws-static-website:index:Website"
    properties:
      sitePath: "./build"
      atomicDeployments: true
outputs:
  websiteURL: ${web.websiteURL}
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as awsStaticWebsite from "@pulumi/aws-static-website";

const web = new awsStaticWebsite.Website("web", {
    sitePath: "./build",
    atomicDeployments: true,
});

export const websiteURL = web.websiteURL;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_aws_static_website as aws_static_website

web = aws_static_website.Website("web",
    site_path="./build",
    atomic_deployments=True)

pulumi.export("websiteURL", web.website_url)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	website "github.com/pulumi/pulumi-aws-static-website/sdk/go/aws-static-website"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		web, err := website.NewWebsite(ctx, "web", &website.WebsiteArgs{
			SitePath:          pulumi.String("./build"),
			AtomicDeployments: pulumi.Bool(true),
		})
		if err != nil {
			return err
		}
		ctx.Export("websiteURL", web.WebsiteURL)
		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using Pulumi;
using AwsStaticWebsite = Pulumi.AwsStaticWebsite;

return await Deployment.RunAsync(() =>
{
    var web = new AwsStaticWebsite.Website("web", new()
    {
        SitePath = "./build",
        AtomicDeployments = true,
    });

    return new Dictionary<string, object?>
    {
        ["websiteURL"] = web.WebsiteURL,
    };
});
```

{{% /choosable %}}

With atomic deployments enabled a new bucket will be provisioned, your content is added via a sync command, and finally once your new bucket is built the old bucket is deleted.

![Gif of creating and updating a atomically deployed website](atomic-deployment.gif)

#### Rollback

The AWS Static Website Package currently does not support rollbacks but if you export the name of the bucket on your stack then the Package will keep the previous bucket provision until the next update. This allows manual rollbacks to previous bucket versions if you encounter a post-deployment error. See the example code below for how to enable this feature exactly.

{{% chooser language "yaml,typescript,python,go,csharp" / %}}

{{% choosable language yaml %}}

```yaml
name: atomic-bucket-blog-yaml
description: An AWS Pulumi YAML program for provisioning a static website.
runtime: yaml
resources:
  web:
    type: "aws-static-website:index:Website"
    properties:
      sitePath: "./build"
      atomicDeployments: true
outputs:
  websiteURL: ${web.websiteURL}
  bucketName: ${web.bucketName}
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws_static_website from "@pulumi/aws-static-website";

const web = new aws_static_website.Website("web", {
    sitePath: "./build",
    atomicDeployments: true,
});

export const websiteURL = web.websiteURL;
export const bucketName = web.bucketName;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_aws_static_website as aws_static_website

web = aws_static_website.Website("web",
    site_path="./build",
    atomic_deployments=True)

pulumi.export("websiteURL", web.website_url)
pulumi.export("bucketName", web.bucket_name)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	website "github.com/pulumi/pulumi-aws-static-website/sdk/go/aws-static-website"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		web, err := website.NewWebsite(ctx, "web", &website.WebsiteArgs{
			SitePath:          pulumi.String("./build"),
			AtomicDeployments: pulumi.Bool(true),
		})
		if err != nil {
			return err
		}
		ctx.Export("websiteURL", web.WebsiteURL)
		ctx.Export("bucketName", web.BucketName)
		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using Pulumi;
using AwsStaticWebsite = Pulumi.AwsStaticWebsite;

return await Deployment.RunAsync(() =>
{
    var web = new AwsStaticWebsite.Website("web", new()
    {
        SitePath = "./build",
        AtomicDeployments = true,
    });

    return new Dictionary<string, object?>
    {
        ["websiteURL"] = web.WebsiteURL,
        ["bucketName"] = web.BucketName,
    };
});
```

{{% /choosable %}}

### Cache Control

Now that your website has atomic deployments enabled and you have solved the issue where your assets and dependencies might not be available, you still have to tackle the beast that is your CDN cache. You will need a way to tell the CDN that there is new content and to stop serving the old content.

You could just rely on the cached content expiring but as stated earlier that can still lead in some cases to missing assets. The AWS Static Website Package handles communicating to the CDN that there is new content by provisioning a [Cloudfront Function](/registry/packages/aws/api-docs/cloudfront/function/) that adds a unique build identifier to the CDN’s cache key.

```js
function handler(event){
    var request = event.request;
    request.headers["website-version"] = {
        value: "${buildIdentifier}",
    };
    return request;
}
```

To enable this behavior you simply need to set the cache control header argument to `true`.

{{% chooser language "yaml,typescript,python,go,csharp" / %}}

{{% choosable language yaml %}}

```yaml
name: atomic-bucket-blog-yaml
description: An AWS Pulumi YAML program for provisioning a static website.
runtime: yaml
resources:
  web:
    type: "aws-static-website:index:Website"
    properties:
      sitePath: "./build"
      withCDN: true
      addWebsiteVersionHeader: true
outputs:
  websiteURL: ${web.websiteURL}

```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws_static_website from "@pulumi/aws-static-website";

const web = new aws_static_website.Website("web", {
    sitePath: "./build",
    withCDN: true,
    addWebsiteVersionHeader: true,
});

export const websiteURL = web.websiteURL;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_aws_static_website as aws_static_website

web = aws_static_website.Website("web",
    site_path="./build",
    with_cdn=True,
    add_website_version_header=True)

pulumi.export("websiteURL", web.website_url)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	website "github.com/pulumi/pulumi-aws-static-website/sdk/go/aws-static-website"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		web, err := website.NewWebsite(ctx, "web", &website.WebsiteArgs{
			SitePath:                pulumi.String("./build"),
            WithCDN:                 pulumi.Bool(true),
			AddWebsiteVersionHeader: pulumi.Bool(true),
		})
		if err != nil {
			return err
		}
		ctx.Export("websiteURL", web.WebsiteURL)
		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using Pulumi;
using AwsStaticWebsite = Pulumi.AwsStaticWebsite;

return await Deployment.RunAsync(() =>
{
    var web = new AwsStaticWebsite.Website("web", new()
    {
        SitePath = "./build",
        WithCDN = true,
        AddWebsiteVersionHeader = true,
    });

    return new Dictionary<string, object?>
    {
        ["websiteURL"] = web.WebsiteURL,
    };
});
```

{{% /choosable %}}

## Putting it all together

Below you will find a full Pulumi program that atomically deploys your website, keeps the cache up to date, and allows for you to do manual rollbacks.

{{% chooser language "yaml,typescript,python,go,csharp" / %}}

{{% choosable language yaml %}}

```yaml
name: atomic-bucket-blog-yaml
description: An AWS Pulumi YAML program for provisioning a static website.
runtime: yaml
resources:
  web:
    type: "aws-static-website:index:Website"
    properties:
      sitePath: "./build"
      withCDN: true
      atomicDeployments: true
      addWebsiteVersionHeader: true
outputs:
  websiteURL: ${web.websiteURL}
  bucketName: ${web.bucketName}
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws_static_website from "@pulumi/aws-static-website";

const web = new aws_static_website.Website("web", {
    sitePath: "./build",
    withCDN: true,
    atomicDeployments: true,
    addWebsiteVersionHeader: true,
});

export const websiteURL = web.websiteURL;
export const bucketName = web.bucketName;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_aws_static_website as aws_static_website

web = aws_static_website.Website("web",
    site_path="./build",
    with_cdn=True,
    atomic_deployments=True,
    add_website_version_header=True)

pulumi.export("websiteURL", web.website_url)
pulumi.export("bucketName", web.bucket_name)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	website "github.com/pulumi/pulumi-aws-static-website/sdk/go/aws-static-website"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		web, err := website.NewWebsite(ctx, "web", &website.WebsiteArgs{
			SitePath:                pulumi.String("./build"),
            WithCDN:                 pulumi.bool(true),
			AtomicDeployments:       pulumi.Bool(true),
			AddWebsiteVersionHeader: pulumi.Bool(true),
		})
		if err != nil {
			return err
		}
		ctx.Export("websiteURL", web.WebsiteURL)
		ctx.Export("bucketName", web.BucketName)
		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using Pulumi;
using AwsStaticWebsite = Pulumi.AwsStaticWebsite;

return await Deployment.RunAsync(() =>
{
    var web = new AwsStaticWebsite.Website("web", new()
    {
        SitePath = "./build",
        WithCDN = true,
        AtomicDeployments = true,
        AddWebsiteVersionHeader = true,
    });

    return new Dictionary<string, object?>
    {
        ["websiteURL"] = web.WebsiteURL,
        ["bucketName"] = web.BucketName,
    };
});
```

{{% /choosable %}}

Now when you run a `pulumi up` you will provision a new bucket, sync your content, associate the bucket to your CDN, update the Cloudfront Function so the CDN knows to fetch new content, and lastly keep your previous bucket around in case you need to rollback.

Deploying and managing a static website should be easy and the AWS Static Website Package makes it so you can focus more time on generating great content and less time on the internals on your website. For more information on the AWS Static Website Package you can visit the [documentation](/registry/packages/aws-static-website/) or via the code directly on [Github](https://github.com/pulumi/pulumi-aws-static-website).

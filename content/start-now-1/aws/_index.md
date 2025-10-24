---
title: Get Started with Pulumi and AWS
meta_desc: Deploy your first AWS resources with Pulumi in under 5 minutes
type: page
layout: cloud-unified
no_on_this_page: true

cloud_name: AWS
subtitle: Deploy your first AWS resources in under 5 minutes
---

## Quick Setup

### 1. Sign up for Pulumi (Free)

Get started with Pulumi Cloud for free. Includes state management, secrets, and more.

<a href="https://app.pulumi.com/signup" class="btn-primary">Create Free Account</a>

### 2. Install Pulumi CLI

{{< chooser os "macos,linux,windows" >}}

{{% choosable os macos %}}

```bash
brew install pulumi/tap/pulumi
```

{{% /choosable %}}

{{% choosable os linux %}}

```bash
curl -fsSL https://get.pulumi.com | sh
```

{{% /choosable %}}

{{% choosable os windows %}}

```powershell
choco install pulumi
```

{{% /choosable %}}

{{< /chooser >}}

### 3. Configure AWS Credentials

```bash
aws configure
```

Or set environment variables:

```bash
export AWS_ACCESS_KEY_ID=<YOUR_ACCESS_KEY_ID>
export AWS_SECRET_ACCESS_KEY=<YOUR_SECRET_ACCESS_KEY>
```

### 4. Deploy Your First Resource

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language typescript %}}

Create a new project:

```bash
mkdir my-aws-app && cd my-aws-app
pulumi new aws-typescript
```

Example: Create an S3 bucket

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

// Create an S3 bucket
const bucket = new aws.s3.Bucket("my-bucket", {
    website: {
        indexDocument: "index.html",
    },
});

// Export the bucket name and URL
export const bucketName = bucket.id;
export const bucketUrl = pulumi.interpolate`http://${bucket.websiteEndpoint}`;
```

Deploy your infrastructure:

```bash
pulumi up
```

{{% /choosable %}}

{{% choosable language python %}}

Create a new project:

```bash
mkdir my-aws-app && cd my-aws-app
pulumi new aws-python
```

Example: Create an S3 bucket

```python
import pulumi
import pulumi_aws as aws

# Create an S3 bucket
bucket = aws.s3.Bucket("my-bucket",
    website=aws.s3.BucketWebsiteArgs(
        index_document="index.html"
    ))

# Export the bucket name and URL
pulumi.export("bucket_name", bucket.id)
pulumi.export("bucket_url", pulumi.Output.concat("http://", bucket.website_endpoint))
```

Deploy your infrastructure:

```bash
pulumi up
```

{{% /choosable %}}

{{% choosable language go %}}

Create a new project:

```bash
mkdir my-aws-app && cd my-aws-app
pulumi new aws-go
```

Example: Create an S3 bucket

```go
package main

import (
    "github.com/pulumi/pulumi-aws/sdk/v6/go/aws/s3"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        // Create an S3 bucket
        bucket, err := s3.NewBucket(ctx, "my-bucket", &s3.BucketArgs{
            Website: &s3.BucketWebsiteArgs{
                IndexDocument: pulumi.String("index.html"),
            },
        })
        if err != nil {
            return err
        }

        // Export the bucket name and URL
        ctx.Export("bucketName", bucket.ID())
        ctx.Export("bucketUrl", pulumi.Sprintf("http://%s", bucket.WebsiteEndpoint))
        return nil
    })
}
```

Deploy your infrastructure:

```bash
pulumi up
```

{{% /choosable %}}

{{% choosable language csharp %}}

Create a new project:

```bash
mkdir my-aws-app && cd my-aws-app
pulumi new aws-csharp
```

Example: Create an S3 bucket

```csharp
using Pulumi;
using Pulumi.Aws.S3;

class MyStack : Stack
{
    public MyStack()
    {
        // Create an S3 bucket
        var bucket = new Bucket("my-bucket", new BucketArgs
        {
            Website = new BucketWebsiteArgs
            {
                IndexDocument = "index.html"
            }
        });

        // Export the bucket name and URL
        this.BucketName = bucket.Id;
        this.BucketUrl = Output.Format($"http://{bucket.WebsiteEndpoint}");
    }

    [Output]
    public Output<string> BucketName { get; set; }

    [Output]
    public Output<string> BucketUrl { get; set; }
}
```

Deploy your infrastructure:

```bash
pulumi up
```

{{% /choosable %}}

{{% choosable language java %}}

Create a new project:

```bash
mkdir my-aws-app && cd my-aws-app
pulumi new aws-java
```

Example: Create an S3 bucket

```java
package myproject;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.aws.s3.Bucket;
import com.pulumi.aws.s3.BucketArgs;
import com.pulumi.aws.s3.inputs.BucketWebsiteArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        // Create an S3 bucket
        var bucket = new Bucket("my-bucket", BucketArgs.builder()
            .website(BucketWebsiteArgs.builder()
                .indexDocument("index.html")
                .build())
            .build());

        // Export the bucket name and URL
        ctx.export("bucketName", bucket.id());
        ctx.export("bucketUrl", bucket.websiteEndpoint()
            .applyValue(endpoint -> String.format("http://%s", endpoint)));
    }
}
```

Deploy your infrastructure:

```bash
pulumi up
```

{{% /choosable %}}

{{% choosable language yaml %}}

Create a new project:

```bash
mkdir my-aws-app && cd my-aws-app
pulumi new aws-yaml
```

Example: Create an S3 bucket

```yaml
name: my-aws-app
runtime: yaml

resources:
  # Create an S3 bucket
  my-bucket:
    type: aws:s3:Bucket
    properties:
      website:
        indexDocument: index.html

outputs:
  # Export the bucket name and URL
  bucketName: ${my-bucket.id}
  bucketUrl: http://${my-bucket.websiteEndpoint}
```

Deploy your infrastructure:

```bash
pulumi up
```

{{% /choosable %}}

## What's next?

- [**View your stack in Pulumi Cloud →**](https://app.pulumi.com/stacks)
  Explore resource details, deployment history, and manage your infrastructure

- [**Follow the complete AWS tutorial →**](/docs/iac/get-started/aws/)
  Learn how to build a static website on AWS with S3 and CloudFront

- [**Explore AWS examples →**](https://github.com/pulumi/examples#aws)
  Browse production-ready examples for common AWS architectures

- [**Learn Pulumi concepts →**](/docs/iac/concepts/)
  Understand stacks, state, configuration, and more

- [**Join the community →**](https://slack.pulumi.com)
  Get help and share knowledge with other Pulumi users

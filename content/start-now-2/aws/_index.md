---
title: Get Started with Pulumi and AWS
meta_desc: Deploy AWS infrastructure with Pulumi using your favorite programming language
type: page
layout: cloud-progressive
no_on_this_page: true

cloud_name: AWS
subtitle: Choose your language and deploy AWS infrastructure in minutes
---

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language typescript %}}

## Get Started with TypeScript

Build AWS infrastructure using TypeScript's type safety and modern JavaScript features.

### Prerequisites

- [Node.js](https://nodejs.org/) version 14 or later
- [AWS Account](https://aws.amazon.com/free/)
- AWS credentials configured

### Quick Start

#### 1. Sign up for Pulumi Cloud (Free)

<a href="https://app.pulumi.com/signup" class="btn-primary">Create Free Account</a>

Pulumi Cloud provides free state management, secrets encryption, and deployment history.

#### 2. Install Pulumi

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

#### 3. Create Your First Project

```bash
mkdir aws-quickstart && cd aws-quickstart
pulumi new aws-typescript
```

This creates a new Pulumi project with TypeScript configured for AWS.

#### 4. Deploy Infrastructure

Your project includes example code to create an S3 bucket:

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

Deploy it:

```bash
pulumi up
```

### Next Steps

- [**View your stack in Pulumi Cloud →**](https://app.pulumi.com/stacks)
  Explore resource details, deployment history, and manage your infrastructure
- [Complete AWS TypeScript Tutorial →](/docs/iac/get-started/aws/)
- [Browse AWS TypeScript Examples →](https://github.com/pulumi/examples#typescript)
- [Learn Pulumi TypeScript Concepts →](/docs/iac/concepts/languages/javascript/)

{{% /choosable %}}

{{% choosable language python %}}

## Get Started with Python

Build AWS infrastructure using Python's simplicity and extensive ecosystem.

### Prerequisites

- [Python](https://www.python.org/) 3.8 or later
- [AWS Account](https://aws.amazon.com/free/)
- AWS credentials configured

### Quick Start

#### 1. Sign up for Pulumi Cloud (Free)

<a href="https://app.pulumi.com/signup" class="btn-primary">Create Free Account</a>

Pulumi Cloud provides free state management, secrets encryption, and deployment history.

#### 2. Install Pulumi

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

#### 3. Create Your First Project

```bash
mkdir aws-quickstart && cd aws-quickstart
pulumi new aws-python
```

This creates a new Pulumi project with Python configured for AWS.

#### 4. Deploy Infrastructure

Your project includes example code to create an S3 bucket:

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

Deploy it:

```bash
pulumi up
```

### Next Steps

- [**View your stack in Pulumi Cloud →**](https://app.pulumi.com/stacks)
  Explore resource details, deployment history, and manage your infrastructure
- [Complete AWS Python Tutorial →](/docs/iac/get-started/aws/)
- [Browse AWS Python Examples →](https://github.com/pulumi/examples#python)
- [Learn Pulumi Python Concepts →](/docs/iac/concepts/languages/python/)

{{% /choosable %}}

{{% choosable language go %}}

## Get Started with Go

Build AWS infrastructure using Go's performance and strong typing.

### Prerequisites

- [Go](https://golang.org/) 1.20 or later
- [AWS Account](https://aws.amazon.com/free/)
- AWS credentials configured

### Quick Start

#### 1. Sign up for Pulumi Cloud (Free)

<a href="https://app.pulumi.com/signup" class="btn-primary">Create Free Account</a>

Pulumi Cloud provides free state management, secrets encryption, and deployment history.

#### 2. Install Pulumi

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

#### 3. Create Your First Project

```bash
mkdir aws-quickstart && cd aws-quickstart
pulumi new aws-go
```

This creates a new Pulumi project with Go configured for AWS.

#### 4. Deploy Infrastructure

Your project includes example code to create an S3 bucket:

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

Deploy it:

```bash
pulumi up
```

### Next Steps

- [**View your stack in Pulumi Cloud →**](https://app.pulumi.com/stacks)
  Explore resource details, deployment history, and manage your infrastructure
- [Complete AWS Go Tutorial →](/docs/iac/get-started/aws/)
- [Browse AWS Go Examples →](https://github.com/pulumi/examples#go)
- [Learn Pulumi Go Concepts →](/docs/iac/concepts/languages/go/)

{{% /choosable %}}

{{% choosable language csharp %}}

## Get Started with C\#

Build AWS infrastructure using C# and the .NET ecosystem.

### Prerequisites

- [.NET](https://dotnet.microsoft.com/) 6.0 or later
- [AWS Account](https://aws.amazon.com/free/)
- AWS credentials configured

### Quick Start

#### 1. Sign up for Pulumi Cloud (Free)

<a href="https://app.pulumi.com/signup" class="btn-primary">Create Free Account</a>

Pulumi Cloud provides free state management, secrets encryption, and deployment history.

#### 2. Install Pulumi

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

#### 3. Create Your First Project

```bash
mkdir aws-quickstart && cd aws-quickstart
pulumi new aws-csharp
```

This creates a new Pulumi project with C# configured for AWS.

#### 4. Deploy Infrastructure

Your project includes example code to create an S3 bucket:

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

Deploy it:

```bash
pulumi up
```

### Next Steps

- [**View your stack in Pulumi Cloud →**](https://app.pulumi.com/stacks)
  Explore resource details, deployment history, and manage your infrastructure
- [Complete AWS C# Tutorial →](/docs/iac/get-started/aws/)
- [Browse AWS C# Examples →](https://github.com/pulumi/examples#dotnet)
- [Learn Pulumi C# Concepts →](/docs/iac/concepts/languages/dotnet/)

{{% /choosable %}}

{{% choosable language java %}}

## Get Started with Java

Build AWS infrastructure using Java's maturity and enterprise ecosystem.

### Prerequisites

- [Java](https://www.oracle.com/java/) 11 or later
- [Maven](https://maven.apache.org/) 3.6.1 or later
- [AWS Account](https://aws.amazon.com/free/)
- AWS credentials configured

### Quick Start

#### 1. Sign up for Pulumi Cloud (Free)

<a href="https://app.pulumi.com/signup" class="btn-primary">Create Free Account</a>

Pulumi Cloud provides free state management, secrets encryption, and deployment history.

#### 2. Install Pulumi

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

#### 3. Create Your First Project

```bash
mkdir aws-quickstart && cd aws-quickstart
pulumi new aws-java
```

This creates a new Pulumi project with Java configured for AWS.

#### 4. Deploy Infrastructure

Your project includes example code to create an S3 bucket:

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

Deploy it:

```bash
pulumi up
```

### Next Steps

- [**View your stack in Pulumi Cloud →**](https://app.pulumi.com/stacks)
  Explore resource details, deployment history, and manage your infrastructure
- [Complete AWS Java Tutorial →](/docs/iac/get-started/aws/)
- [Browse AWS Java Examples →](https://github.com/pulumi/examples#java)
- [Learn Pulumi Java Concepts →](/docs/iac/concepts/languages/java/)

{{% /choosable %}}

{{% choosable language yaml %}}

## Get Started with YAML

Build AWS infrastructure using simple, declarative YAML configuration.

### Prerequisites

- [AWS Account](https://aws.amazon.com/free/)
- AWS credentials configured

### Quick Start

#### 1. Sign up for Pulumi Cloud (Free)

<a href="https://app.pulumi.com/signup" class="btn-primary">Create Free Account</a>

Pulumi Cloud provides free state management, secrets encryption, and deployment history.

#### 2. Install Pulumi

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

#### 3. Create Your First Project

```bash
mkdir aws-quickstart && cd aws-quickstart
pulumi new aws-yaml
```

This creates a new Pulumi project with YAML configured for AWS.

#### 4. Deploy Infrastructure

Your project includes example YAML to create an S3 bucket:

```yaml
name: aws-quickstart
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

Deploy it:

```bash
pulumi up
```

### Next Steps

- [**View your stack in Pulumi Cloud →**](https://app.pulumi.com/stacks)
  Explore resource details, deployment history, and manage your infrastructure
- [Complete AWS YAML Tutorial →](/docs/iac/get-started/aws/)
- [Browse AWS YAML Examples →](https://github.com/pulumi/examples#yaml)
- [Learn Pulumi YAML Concepts →](/docs/iac/concepts/languages/yaml/)

{{% /choosable %}}

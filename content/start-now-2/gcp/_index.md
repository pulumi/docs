---
title: Get Started with Pulumi and Google Cloud
meta_desc: Deploy Google Cloud infrastructure with Pulumi using your favorite programming language
type: page
layout: cloud-progressive
no_on_this_page: true

cloud_name: Google Cloud
subtitle: Choose your language and deploy Google Cloud infrastructure in minutes
---

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language typescript %}}

## Get Started with TypeScript

Build Google Cloud infrastructure using TypeScript's type safety and modern JavaScript features.

### Prerequisites

- [Node.js](https://nodejs.org/) version 14 or later
- [GCP Account](https://cloud.google.com/free/)
- Google Cloud CLI configured (`gcloud auth login`)

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
mkdir gcp-quickstart && cd gcp-quickstart
pulumi new gcp-typescript
```

This creates a new Pulumi project with TypeScript configured for Google Cloud.

#### 4. Deploy Infrastructure

Your project includes example code to create a Storage bucket:

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as gcp from "@pulumi/gcp";

// Create a GCP Storage bucket
const bucket = new gcp.storage.Bucket("my-bucket", {
    location: "US",
    website: {
        mainPageSuffix: "index.html",
    },
});

// Export the bucket name and URL
export const bucketName = bucket.name;
export const bucketUrl = pulumi.interpolate`gs://${bucket.name}`;
```

Deploy it:

```bash
pulumi up
```

### Next steps

- [**View your stack in Pulumi Cloud →**](https://app.pulumi.com/stacks)
  Explore resource details, deployment history, and manage your infrastructure
- [Complete Google Cloud TypeScript Tutorial →](/docs/iac/get-started/gcp/)
- [Browse Google Cloud TypeScript Examples →](https://github.com/pulumi/examples#typescript)
- [Learn Pulumi TypeScript Concepts →](/docs/iac/concepts/languages/javascript/)

{{% /choosable %}}

{{% choosable language python %}}

## Get Started with Python

Build Google Cloud infrastructure using Python's simplicity and extensive ecosystem.

### Prerequisites

- [Python](https://www.python.org/) 3.8 or later
- [GCP Account](https://cloud.google.com/free/)
- Google Cloud CLI configured (`gcloud auth login`)

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
mkdir gcp-quickstart && cd gcp-quickstart
pulumi new gcp-python
```

This creates a new Pulumi project with Python configured for Google Cloud.

#### 4. Deploy Infrastructure

Your project includes example code to create a Storage bucket:

```python
import pulumi
import pulumi_gcp as gcp

# Create a GCP Storage bucket
bucket = gcp.storage.Bucket("my-bucket",
    location="US",
    website=gcp.storage.BucketWebsiteArgs(
        main_page_suffix="index.html"
    ))

# Export the bucket name and URL
pulumi.export("bucket_name", bucket.name)
pulumi.export("bucket_url", pulumi.Output.concat("gs://", bucket.name))
```

Deploy it:

```bash
pulumi up
```

### Next steps

- [**View your stack in Pulumi Cloud →**](https://app.pulumi.com/stacks)
  Explore resource details, deployment history, and manage your infrastructure
- [Complete Google Cloud Python Tutorial →](/docs/iac/get-started/gcp/)
- [Browse Google Cloud Python Examples →](https://github.com/pulumi/examples#python)
- [Learn Pulumi Python Concepts →](/docs/iac/concepts/languages/python/)

{{% /choosable %}}

{{% choosable language go %}}

## Get Started with Go

Build Google Cloud infrastructure using Go's performance and strong typing.

### Prerequisites

- [Go](https://golang.org/) 1.20 or later
- [GCP Account](https://cloud.google.com/free/)
- Google Cloud CLI configured (`gcloud auth login`)

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
mkdir gcp-quickstart && cd gcp-quickstart
pulumi new gcp-go
```

This creates a new Pulumi project with Go configured for Google Cloud.

#### 4. Deploy Infrastructure

Your project includes example code to create a Storage bucket:

```go
package main

import (
    "github.com/pulumi/pulumi-gcp/sdk/v7/go/gcp/storage"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        // Create a GCP Storage bucket
        bucket, err := storage.NewBucket(ctx, "my-bucket", &storage.BucketArgs{
            Location: pulumi.String("US"),
            Website: &storage.BucketWebsiteArgs{
                MainPageSuffix: pulumi.String("index.html"),
            },
        })
        if err != nil {
            return err
        }

        // Export the bucket name and URL
        ctx.Export("bucketName", bucket.Name)
        ctx.Export("bucketUrl", pulumi.Sprintf("gs://%s", bucket.Name))
        return nil
    })
}
```

Deploy it:

```bash
pulumi up
```

### Next steps

- [**View your stack in Pulumi Cloud →**](https://app.pulumi.com/stacks)
  Explore resource details, deployment history, and manage your infrastructure
- [Complete Google Cloud Go Tutorial →](/docs/iac/get-started/gcp/)
- [Browse Google Cloud Go Examples →](https://github.com/pulumi/examples#go)
- [Learn Pulumi Go Concepts →](/docs/iac/concepts/languages/go/)

{{% /choosable %}}

{{% choosable language csharp %}}

## Get Started with C\#

Build Google Cloud infrastructure using C# and the .NET ecosystem.

### Prerequisites

- [.NET](https://dotnet.microsoft.com/) 6.0 or later
- [GCP Account](https://cloud.google.com/free/)
- Google Cloud CLI configured (`gcloud auth login`)

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
mkdir gcp-quickstart && cd gcp-quickstart
pulumi new gcp-csharp
```

This creates a new Pulumi project with C# configured for Google Cloud.

#### 4. Deploy Infrastructure

Your project includes example code to create a Storage bucket:

```csharp
using Pulumi;
using Pulumi.Gcp.Storage;

class MyStack : Stack
{
    public MyStack()
    {
        // Create a GCP Storage bucket
        var bucket = new Bucket("my-bucket", new BucketArgs
        {
            Location = "US",
            Website = new BucketWebsiteArgs
            {
                MainPageSuffix = "index.html"
            }
        });

        // Export the bucket name and URL
        this.BucketName = bucket.Name;
        this.BucketUrl = Output.Format($"gs://{bucket.Name}");
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

### Next steps

- [**View your stack in Pulumi Cloud →**](https://app.pulumi.com/stacks)
  Explore resource details, deployment history, and manage your infrastructure
- [Complete Google Cloud C# Tutorial →](/docs/iac/get-started/gcp/)
- [Browse Google Cloud C# Examples →](https://github.com/pulumi/examples#dotnet)
- [Learn Pulumi C# Concepts →](/docs/iac/concepts/languages/dotnet/)

{{% /choosable %}}

{{% choosable language java %}}

## Get Started with Java

Build Google Cloud infrastructure using Java's maturity and enterprise ecosystem.

### Prerequisites

- [Java](https://www.oracle.com/java/) 11 or later
- [Maven](https://maven.apache.org/) 3.6.1 or later
- [GCP Account](https://cloud.google.com/free/)
- Google Cloud CLI configured (`gcloud auth login`)

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
mkdir gcp-quickstart && cd gcp-quickstart
pulumi new gcp-java
```

This creates a new Pulumi project with Java configured for Google Cloud.

#### 4. Deploy Infrastructure

Your project includes example code to create a Storage bucket:

```java
package myproject;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.gcp.storage.Bucket;
import com.pulumi.gcp.storage.BucketArgs;
import com.pulumi.gcp.storage.inputs.BucketWebsiteArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        // Create a GCP Storage bucket
        var bucket = new Bucket("my-bucket", BucketArgs.builder()
            .location("US")
            .website(BucketWebsiteArgs.builder()
                .mainPageSuffix("index.html")
                .build())
            .build());

        // Export the bucket name and URL
        ctx.export("bucketName", bucket.name());
        ctx.export("bucketUrl", bucket.name()
            .applyValue(name -> String.format("gs://%s", name)));
    }
}
```

Deploy it:

```bash
pulumi up
```

### Next steps

- [**View your stack in Pulumi Cloud →**](https://app.pulumi.com/stacks)
  Explore resource details, deployment history, and manage your infrastructure
- [Complete Google Cloud Java Tutorial →](/docs/iac/get-started/gcp/)
- [Browse Google Cloud Java Examples →](https://github.com/pulumi/examples#java)
- [Learn Pulumi Java Concepts →](/docs/iac/concepts/languages/java/)

{{% /choosable %}}

{{% choosable language yaml %}}

## Get Started with YAML

Build Google Cloud infrastructure using simple, declarative YAML configuration.

### Prerequisites

- [GCP Account](https://cloud.google.com/free/)
- Google Cloud CLI configured (`gcloud auth login`)

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
mkdir gcp-quickstart && cd gcp-quickstart
pulumi new gcp-yaml
```

This creates a new Pulumi project with YAML configured for Google Cloud.

#### 4. Deploy Infrastructure

Your project includes example YAML to create a Storage bucket:

```yaml
name: gcp-quickstart
runtime: yaml

resources:
  # Create a GCP Storage bucket
  my-bucket:
    type: gcp:storage:Bucket
    properties:
      location: US
      website:
        mainPageSuffix: index.html

outputs:
  # Export the bucket name and URL
  bucketName: ${my-bucket.name}
  bucketUrl: gs://${my-bucket.name}
```

Deploy it:

```bash
pulumi up
```

### Next steps

- [**View your stack in Pulumi Cloud →**](https://app.pulumi.com/stacks)
  Explore resource details, deployment history, and manage your infrastructure
- [Complete Google Cloud YAML Tutorial →](/docs/iac/get-started/gcp/)
- [Browse Google Cloud YAML Examples →](https://github.com/pulumi/examples#yaml)
- [Learn Pulumi YAML Concepts →](/docs/iac/concepts/languages/yaml/)

{{% /choosable %}}

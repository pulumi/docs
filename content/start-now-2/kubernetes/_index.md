---
title: Get Started with Pulumi and Kubernetes
meta_desc: Deploy Kubernetes infrastructure with Pulumi using your favorite programming language
type: page
layout: cloud-progressive
no_on_this_page: true

cloud_name: Kubernetes
subtitle: Choose your language and deploy Kubernetes infrastructure in minutes
---

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language typescript %}}

## Get Started with TypeScript

Deploy to Kubernetes using TypeScript's type safety and modern JavaScript features.

### Prerequisites

- [Node.js](https://nodejs.org/) version 14 or later
- [Kubernetes cluster](https://kubernetes.io/docs/tasks/tools/)
- kubectl configured (`kubectl cluster-info`)

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
mkdir kubernetes-quickstart && cd kubernetes-quickstart
pulumi new kubernetes-typescript
```

This creates a new Pulumi project with TypeScript configured for Kubernetes.

#### 4. Deploy Infrastructure

Your project includes example code to create an S3 bucket:

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as kubernetes from "@pulumi/kubernetes";

// Create an S3 bucket
const bucket = new kubernetes.s3.Bucket("my-bucket", {
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
- [Complete Kubernetes TypeScript Tutorial →](/docs/iac/get-started/kubernetes/)
- [Browse Kubernetes TypeScript Examples →](https://github.com/pulumi/examples#typescript)
- [Learn Pulumi TypeScript Concepts →](/docs/iac/concepts/languages/javascript/)

{{% /choosable %}}

{{% choosable language python %}}

## Get Started with Python

Deploy to Kubernetes using Python's simplicity and extensive ecosystem.

### Prerequisites

- [Python](https://www.python.org/) 3.8 or later
- [Kubernetes cluster](https://kubernetes.io/docs/tasks/tools/)
- kubectl configured (`kubectl cluster-info`)

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
mkdir kubernetes-quickstart && cd kubernetes-quickstart
pulumi new kubernetes-python
```

This creates a new Pulumi project with Python configured for Kubernetes.

#### 4. Deploy Infrastructure

Your project includes example code to create an S3 bucket:

```python
import pulumi
import pulumi_kubernetes as kubernetes

# Create an S3 bucket
bucket = kubernetes.s3.Bucket("my-bucket",
    website=kubernetes.s3.BucketWebsiteArgs(
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
- [Complete Kubernetes Python Tutorial →](/docs/iac/get-started/kubernetes/)
- [Browse Kubernetes Python Examples →](https://github.com/pulumi/examples#python)
- [Learn Pulumi Python Concepts →](/docs/iac/concepts/languages/python/)

{{% /choosable %}}

{{% choosable language go %}}

## Get Started with Go

Deploy to Kubernetes using Go's performance and strong typing.

### Prerequisites

- [Go](https://golang.org/) 1.20 or later
- [Kubernetes cluster](https://kubernetes.io/docs/tasks/tools/)
- kubectl configured (`kubectl cluster-info`)

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
mkdir kubernetes-quickstart && cd kubernetes-quickstart
pulumi new kubernetes-go
```

This creates a new Pulumi project with Go configured for Kubernetes.

#### 4. Deploy Infrastructure

Your project includes example code to create an S3 bucket:

```go
package main

import (
    "github.com/pulumi/pulumi-kubernetes/sdk/v6/go/kubernetes/s3"
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
- [Complete Kubernetes Go Tutorial →](/docs/iac/get-started/kubernetes/)
- [Browse Kubernetes Go Examples →](https://github.com/pulumi/examples#go)
- [Learn Pulumi Go Concepts →](/docs/iac/concepts/languages/go/)

{{% /choosable %}}

{{% choosable language csharp %}}

## Get Started with C\#

Deploy to Kubernetes using C# and the .NET ecosystem.

### Prerequisites

- [.NET](https://dotnet.microsoft.com/) 6.0 or later
- [Kubernetes cluster](https://kubernetes.io/docs/tasks/tools/)
- kubectl configured (`kubectl cluster-info`)

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
mkdir kubernetes-quickstart && cd kubernetes-quickstart
pulumi new kubernetes-csharp
```

This creates a new Pulumi project with C# configured for Kubernetes.

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
- [Complete Kubernetes C# Tutorial →](/docs/iac/get-started/kubernetes/)
- [Browse Kubernetes C# Examples →](https://github.com/pulumi/examples#dotnet)
- [Learn Pulumi C# Concepts →](/docs/iac/concepts/languages/dotnet/)

{{% /choosable %}}

{{% choosable language java %}}

## Get Started with Java

Deploy to Kubernetes using Java's maturity and enterprise ecosystem.

### Prerequisites

- [Java](https://www.oracle.com/java/) 11 or later
- [Maven](https://maven.apache.org/) 3.6.1 or later
- [Kubernetes cluster](https://kubernetes.io/docs/tasks/tools/)
- kubectl configured (`kubectl cluster-info`)

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
mkdir kubernetes-quickstart && cd kubernetes-quickstart
pulumi new kubernetes-java
```

This creates a new Pulumi project with Java configured for Kubernetes.

#### 4. Deploy Infrastructure

Your project includes example code to create an S3 bucket:

```java
package myproject;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.kubernetes.s3.Bucket;
import com.pulumi.kubernetes.s3.BucketArgs;
import com.pulumi.kubernetes.s3.inputs.BucketWebsiteArgs;

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
- [Complete Kubernetes Java Tutorial →](/docs/iac/get-started/kubernetes/)
- [Browse Kubernetes Java Examples →](https://github.com/pulumi/examples#java)
- [Learn Pulumi Java Concepts →](/docs/iac/concepts/languages/java/)

{{% /choosable %}}

{{% choosable language yaml %}}

## Get Started with YAML

Deploy to Kubernetes using simple, declarative YAML configuration.

### Prerequisites

- [Kubernetes cluster](https://kubernetes.io/docs/tasks/tools/)
- kubectl configured (`kubectl cluster-info`)

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
mkdir kubernetes-quickstart && cd kubernetes-quickstart
pulumi new kubernetes-yaml
```

This creates a new Pulumi project with YAML configured for Kubernetes.

#### 4. Deploy Infrastructure

Your project includes example YAML to deploy an application:

```yaml
name: kubernetes-quickstart
runtime: yaml

resources:
  # Create a Kubernetes Deployment
  nginx-deployment:
    type: kubernetes:apps/v1:Deployment
    properties:
      spec:
        selector:
          matchLabels:
            app: nginx
        replicas: 2
        template:
          metadata:
            labels:
              app: nginx
          spec:
            containers:
              - name: nginx
                image: nginx:latest
                ports:
                  - containerPort: 80

  # Create a Service
  nginx-service:
    type: kubernetes:core/v1:Service
    properties:
      spec:
        selector:
          app: nginx
        ports:
          - port: 80
        type: LoadBalancer

outputs:
  serviceName: ${nginx-service.metadata.name}
```

Deploy it:

```bash
pulumi up
```

### Next Steps

- [**View your stack in Pulumi Cloud →**](https://app.pulumi.com/stacks)
  Explore resource details, deployment history, and manage your infrastructure
- [Complete Kubernetes YAML Tutorial →](/docs/iac/get-started/kubernetes/)
- [Browse Kubernetes YAML Examples →](https://github.com/pulumi/examples#yaml)
- [Learn Pulumi YAML Concepts →](/docs/iac/concepts/languages/yaml/)

{{% /choosable %}}

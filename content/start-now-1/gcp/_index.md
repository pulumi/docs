---
title: Get Started with Pulumi and Google Cloud
meta_desc: Deploy your first Google Cloud resources with Pulumi in under 5 minutes
type: page
layout: cloud-unified
no_on_this_page: true

cloud_name: Google Cloud
subtitle: Deploy your first Google Cloud resources in under 5 minutes
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

### 3. Configure Google Cloud Credentials

```bash
gcloud auth application-default login
```

Or use a service account:

```bash
export GOOGLE_CREDENTIALS=/path/to/service-account-key.json
```

### 4. Deploy Your First Resource

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language typescript %}}

Create a new project:

```bash
mkdir my-gcp-app && cd my-gcp-app
pulumi new gcp-typescript
```

Example: Create a Storage Bucket

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

// Export the bucket URL
export const bucketName = bucket.name;
export const bucketUrl = pulumi.interpolate`gs://${bucket.name}`;
```

Deploy your infrastructure:

```bash
pulumi up
```

{{% /choosable %}}

{{% choosable language python %}}

Create a new project:

```bash
mkdir my-gcp-app && cd my-gcp-app
pulumi new gcp-python
```

Example: Create a Storage Bucket

```python
import pulumi
import pulumi_gcp as gcp

# Create a GCP Storage bucket
bucket = gcp.storage.Bucket("my-bucket",
    location="US",
    website=gcp.storage.BucketWebsiteArgs(
        main_page_suffix="index.html"
    ))

# Export the bucket URL
pulumi.export("bucket_name", bucket.name)
pulumi.export("bucket_url", pulumi.Output.concat("gs://", bucket.name))
```

Deploy your infrastructure:

```bash
pulumi up
```

{{% /choosable %}}

{{% choosable language go %}}

Create a new project:

```bash
mkdir my-gcp-app && cd my-gcp-app
pulumi new gcp-go
```

Example: Create a Storage Bucket

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

        // Export the bucket URL
        ctx.Export("bucketName", bucket.Name)
        ctx.Export("bucketUrl", pulumi.Sprintf("gs://%s", bucket.Name))
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
mkdir my-gcp-app && cd my-gcp-app
pulumi new gcp-csharp
```

Example: Create a Storage Bucket

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

        // Export the bucket URL
        this.BucketName = bucket.Name;
        this.BucketUrl = Output.Format($"gs://{bucket.Name}");
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
mkdir my-gcp-app && cd my-gcp-app
pulumi new gcp-java
```

Example: Create a Storage Bucket

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

        // Export the bucket URL
        ctx.export("bucketName", bucket.name());
        ctx.export("bucketUrl", bucket.name()
            .applyValue(name -> String.format("gs://%s", name)));
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
mkdir my-gcp-app && cd my-gcp-app
pulumi new gcp-yaml
```

Example: Create a Storage Bucket

```yaml
name: my-gcp-app
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
  # Export the bucket URL
  bucketName: ${my-bucket.name}
  bucketUrl: gs://${my-bucket.name}
```

Deploy your infrastructure:

```bash
pulumi up
```

{{% /choosable %}}

## What's Next?

- [**Follow the complete GCP tutorial →**](/docs/iac/get-started/gcp/)
  Learn how to build and deploy applications on Google Cloud

- [**Explore GCP examples →**](https://github.com/pulumi/examples#gcp)
  Browse production-ready examples for common GCP architectures

- [**Learn Pulumi concepts →**](/docs/iac/concepts/)
  Understand stacks, state, configuration, and more

- [**Join the community →**](https://slack.pulumi.com)
  Get help and share knowledge with other Pulumi users

---
title: Review the New Project | GCP
h1: Review the New Project
linktitle: Review the New Project
meta_desc: This page provides an overview on how to a review a new GCP project.
weight: 6
menu:
  getstarted:
    parent: gcp
    identifier: gcp-review-project

aliases: ["/docs/quickstart/gcp/review-project/"]
---

Let's review some of the generated project files:

- `Pulumi.yaml` defines the [project]({{< relref "/docs/intro/concepts/project" >}}).
- `Pulumi.dev.yaml` contains [configuration]({{< relref "/docs/intro/concepts/config" >}}) values for the [stack]({{< relref "/docs/intro/concepts/stack" >}}) we initialized.
{{% choosable language csharp %}}

- `Program.cs` with a simple entry point.

{{% /choosable %}}
- {{< langfile >}} is the Pulumi program that defines our stack resources. Let's examine it.

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language javascript %}}

```javascript
"use strict";
const pulumi = require("@pulumi/pulumi");
const gcp = require("@pulumi/gcp");

// Create a GCP resource (Storage Bucket)
const bucket = new gcp.storage.Bucket("my-bucket");

// Export the DNS name of the bucket
exports.bucketName = bucket.url;
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as gcp from "@pulumi/gcp";

// Create a GCP resource (Storage Bucket)
const bucket = new gcp.storage.Bucket("my-bucket");

// Export the DNS name of the bucket
export const bucketName = bucket.url;
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
from pulumi_gcp import storage

# Create a GCP resource (Storage Bucket)
bucket = storage.Bucket('my-bucket')

# Export the DNS name of the bucket
pulumi.export('bucket_name',  bucket.url)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-gcp/sdk/v2/go/gcp/storage"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Create a GCP resource (Storage Bucket)
		bucket, err := storage.NewBucket(ctx, "my-bucket", nil)
		if err != nil {
			return err
		}

		// Export the DNS name of the bucket
		ctx.Export("bucketName", bucket.Url)
		return nil
	})
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using Pulumi;
using Pulumi.Gcp.Storage;

class MyStack : Stack
{
    public MyStack()
    {
        // Create a GCP resource (Storage Bucket)
        var bucket = new Bucket("my-bucket");

        // Export the DNS name of the bucket
        this.BucketName = bucket.Url;
    }

    [Output]
    public Output<string> BucketName { get; set; }
}
```

{{% /choosable %}}

This Pulumi program creates a storage bucket and exports the bucket URL.

{{% choosable language python %}}

{{< python-venv >}}

{{% /choosable %}}

Next, we'll deploy the stack.

{{< get-started-stepper >}}

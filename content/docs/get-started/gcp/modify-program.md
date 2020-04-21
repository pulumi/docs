---
title: Modify the Program | GCP
h1: Modify the Program
linktitle: Modify the Program
meta_desc: This page provides an overview on how to update Google Cloud (GCP) project from a Pulumi program.
weight: 8
menu:
  getstarted:
    parent: gcp
    identifier: gcp-modify-program

aliases: ["/docs/quickstart/gcp/modify-program/"]
---

Now that we have an instance of our Pulumi program deployed, let's add some labels to it.

Replace the entire contents of {{< langfile >}} with the following:

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language javascript %}}

```javascript
"use strict";
const pulumi = require("@pulumi/pulumi");
const gcp = require("@pulumi/gcp");

// Create a GCP resource (Storage Bucket)
const bucket = new gcp.storage.Bucket("my-bucket", {
    labels: { "environment": "dev" }
});

// Export the DNS name of the bucket
exports.bucketName = bucket.url;
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as gcp from "@pulumi/gcp";

// Create a GCP resource (Storage Bucket)
const bucket = new gcp.storage.Bucket("my-bucket", {
    labels: { "environment": "dev" } 
});

// Export the DNS name of the bucket
export const bucketName = bucket.url;
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
from pulumi_gcp import storage

# Create a GCP resource (Storage Bucket)
bucket = storage.Bucket('my-bucket',
    labels={'environemnt': "dev"})

# Export the DNS name of the bucket
pulumi.export('bucket_name',  bucket.url)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
    "github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/storage"
    "github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        // Create a GCP resource (Storage Bucket)
        bucket, err := storage.NewBucket(ctx, "my-bucket", &storage.BucketArgs{
            Labels: pulumi.StringMap{
                "environment": pulumi.String("dev"),
            },
        })
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
        var bucket = new Bucket("my-bucket", new BucketArgs{
            Labels =
            {
                { "environment", "dev" }
            }
        });

        // Export the DNS name of the bucket
        this.BucketName = bucket.Url;
    }

    [Output]
    public Output<string> BucketName { get; set; }
}
```

{{% /choosable %}}

Next, we'll deploy the changes.

{{< get-started-stepper >}}

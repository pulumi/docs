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
- {{< langfile >}} is the Pulumi program that defines our stack resources. Let's examine it.

{{< langchoose csharp >}}

```javascript
"use strict";
const pulumi = require("@pulumi/pulumi");
const gcp = require("@pulumi/gcp");

// Create a GCP resource (Storage Bucket)
const bucket = new gcp.storage.Bucket("my-bucket");

// Export the DNS name of the bucket
exports.bucketName = bucket.url;
```

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as gcp from "@pulumi/gcp";

// Create a GCP resource (Storage Bucket)
const bucket = new gcp.storage.Bucket("my-bucket");

// Export the DNS name of the bucket
export const bucketName = bucket.url;
```

```python
import pulumi
from pulumi_gcp import storage

# Create a GCP resource (Storage Bucket)
bucket = storage.Bucket('my-bucket')

# Export the DNS name of the bucket
pulumi.export('bucket_name',  bucket.url)
```

```go
package main

import (
    "github.com/pulumi/pulumi-gcp/sdk/go/gcp/storage"
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
        ctx.Export("bucketName", bucket.Url())
        return nil
    })
}
```

```csharp
using System.Collections.Generic;
using System.Threading.Tasks;
using Pulumi;
using Pulumi.Gcp.Storage;

class Program
{
    static Task Main()
    {
        return Deployment.RunAsync(() =>
        {
            // Create a GCP resource (Storage Bucket)
            var bucket = new Storage.Bucket("my-bucket");

            // Export the DNS name of the bucket
            return new Dictionary<string, object> {
                { "bucket_name", bucket.Url },
            };
        });
    }
}
```

This Pulumi program creates a storage bucket and exports the bucket URL.

{{% lang python %}}
For Python, before we deploy the stack, the following commands need to be run to create a virtual environment, activate it, and install dependencies:

```bash
$ virtualenv -p python3 venv
```

```bash
$ source venv/bin/activate
```

```bash
$ pip3 install -r requirements.txt
```

{{% /lang %}}

{{% lang go %}}
For Go, before we can deploy the stack, you will need to initialize your project's dependencies. Any dependency manager can be used, including Go's built-in module system:

```bash
$ go mod init
```

{{% /lang %}}

Next, we'll deploy the stack.

{{< get-started-stepper >}}

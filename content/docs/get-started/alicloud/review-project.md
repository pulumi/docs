---
title: Review the New Project | Alibaba Cloud
h1: Review the New Project
linktitle: Review the New Project
meta_desc: This page provides an overview on how to a review a new Alibaba Cloud project.
weight: 6
menu:
  getstarted:
    parent: alicloud
    identifier: alicloud-review-project

---

Let's review some of the generated project files:

- `Pulumi.yaml` defines the [project]({{< relref "/docs/intro/concepts/project" >}}).
- `Pulumi.dev.yaml` contains [configuration]({{< relref "/docs/intro/concepts/config" >}}) values for the [stack]({{< relref "/docs/intro/concepts/stack" >}}) we initialized.
- {{< langfile >}} is the Pulumi program that defines our stack resources. Let's examine it.

{{< langchoose csharp >}}

```javascript
"use strict";
const pulumi = require("@pulumi/pulumi");
const alicloud = require("@pulumi/alicloud");

// Create an AliCloud resource (OSS Bucket)
const bucket = new alicloud.oss.Bucket("my-bucket");

// Export the name of the bucket
exports.bucketName = bucket.id;
```

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as alicloud from "@pulumi/alicloud";

// Create an AliCloud resource (OSS Bucket)
const bucket = new alicloud.oss.Bucket("my-bucket");

// Export the name of the bucket
export const bucketName = bucket.id;
```

```python
import pulumi
from pulumi_alicloud import oss

# Create an AliCloud resource (OSS Bucket)
bucket = oss.Bucket('my-bucket')

# Export the name of the bucket
pulumi.export('bucket_name',  bucket.id)
```

```go
package main

import (
    "github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/oss"
    "github.com/pulumi/pulumi/sdk/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        // Create an AliCloud resource (OSS Bucket)
        bucket, err := oss.NewBucket(ctx, "my-bucket", nil)
        if err != nil {
            return err
        }

        // Export the name of the bucket
        ctx.Export("bucketName", bucket.ID())
        return nil
    })
}
```

```csharp
using System.Collections.Generic;
using System.Threading.Tasks;
using Pulumi;
using Pulumi.Alicloud.Oss;

class Program
{
    static Task Main()
    {
        return Deployment.RunAsync(() => {
            // Create an AliCloud resource (OSS Bucket)
            var bucket = new Bucket("my-bucket");

            // Export the name of the bucket
            return new Dictionary<string, object> {
                { "bucket_name" , bucket.Id },
            };
        });
    }
}
```

This Pulumi program creates an OSS bucket and exports the name of the bucket.

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

Because Go is a compiled language, you also need to compile it:

```bash
$ go build $(basename $(pwd))
```

This instructs Go to create a binary whose name is the same as your directory. It needs to match your project name.
{{% /lang %}}

Next, we'll deploy the stack.

{{< get-started-stepper >}}

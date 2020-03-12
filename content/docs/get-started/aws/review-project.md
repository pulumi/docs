---
title: Review the New Project | AWS
h1: Review the New Project
linktitle: Review the New Project
meta_desc: This page provides an overview on how to a review a new AWS project.
weight: 6
menu:
  getstarted:
    parent: aws
    identifier: aws-review-project

aliases: ["/docs/quickstart/aws/review-project/"]
---

Let's review some of the generated project files:

- `Pulumi.yaml` defines the [project]({{< relref "/docs/intro/concepts/project" >}}).
- `Pulumi.dev.yaml` contains [configuration]({{< relref "/docs/intro/concepts/config" >}}) values for the [stack]({{< relref "/docs/intro/concepts/stack" >}}) we initialized.
- {{< langfile >}} is the Pulumi program that defines our stack resources. Let's examine it.

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language javascript %}}

```javascript
"use strict";
const pulumi = require("@pulumi/pulumi");
const aws = require("@pulumi/aws");
const awsx = require("@pulumi/awsx");

// Create an AWS resource (S3 Bucket)
const bucket = new aws.s3.Bucket("my-bucket");

// Export the name of the bucket
exports.bucketName = bucket.id;
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import * as awsx from "@pulumi/awsx";

// Create an AWS resource (S3 Bucket)
const bucket = new aws.s3.Bucket("my-bucket");

// Export the name of the bucket
export const bucketName = bucket.id;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
from pulumi_aws import s3

# Create an AWS resource (S3 Bucket)
bucket = s3.Bucket('my-bucket')

# Export the name of the bucket
pulumi.export('bucket_name',  bucket.id)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
    "github.com/pulumi/pulumi-aws/sdk/go/aws/s3"
    "github.com/pulumi/pulumi/sdk/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        // Create an AWS resource (S3 Bucket)
        bucket, err := s3.NewBucket(ctx, "my-bucket", nil)
        if err != nil {
            return err
        }

        // Export the name of the bucket
        ctx.Export("bucketName", bucket.ID())
        return nil
    })
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using System.Threading.Tasks;
using Pulumi;
using Pulumi.Aws.S3;

class Program
{
    static Task Main()
    {
        return Deployment.RunAsync(() => {
            // Create an AWS resource (S3 Bucket)
            var bucket = new Bucket("my-bucket");

            // Export the name of the bucket
            return new Dictionary<string, object> {
                { "bucket_name" , bucket.Id },
            };
        });
    }
}
```

{{% /choosable %}}

This Pulumi program creates an S3 bucket and exports the name of the bucket.

{{% choosable language python %}}

{{% python-venv %}}

{{% /choosable %}}

{{% choosable language go %}}

For Go, before we can deploy the stack, you will need to initialize your project's dependencies. Pulumi templates currently use `dep`:

```bash
$ dep ensure
```

{{% /choosable %}}

Next, we'll deploy the stack.

{{< get-started-stepper >}}

---
title: Review the New Project | AWS
h1: Review the New Project
linktitle: Review the New Project
meta_desc: This page provides an overview on how to a review a new AWS project.
weight: 4
menu:
  getstarted:
    parent: aws
    identifier: aws-review-project

aliases: ["/docs/quickstart/aws/review-project/"]
---

Let's review some of the generated project files:

{{% choosable language "javascript,typescript,python,go,csharp,java" %}}

- `Pulumi.yaml` defines the [project](/docs/intro/concepts/project/).

{{% /choosable %}}

{{% choosable language "yaml" %}}

- `Pulumi.yaml` defines both the [project](/docs/intro/concepts/project/) and the program that manages your stack resources.

{{% /choosable %}}

- `Pulumi.dev.yaml` contains [configuration](/docs/intro/concepts/config/) values for the [stack](/docs/intro/concepts/stack/) you just initialized.

{{% choosable language csharp %}}

- `Program.cs` is the Pulumi program that defines your stack resources.

{{% /choosable %}}

{{% choosable language java %}}

- `src/main/java/myproject` defines the project's Java package root.

{{% /choosable %}}

{{% choosable language "javascript,typescript,python,go,java" %}}

<!-- The wrapping spans are infortunately necessary here; without them, the renderer gets confused and generates invalid markup. -->
- <span>{{< langfile >}}</span> is the Pulumi program that defines your stack resources.

{{% /choosable %}}

Let's examine {{< langfile >}}.

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" / >}}

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
pulumi.export('bucket_name', bucket.id)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v5/go/aws/s3"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
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
using Pulumi;
using Pulumi.Aws.S3;
using System.Collections.Generic;

return await Deployment.RunAsync(() =>
{
   // Create an AWS resource (S3 Bucket)
   var bucket = new Bucket("my-bucket");

   // Export the name of the bucket
   return new Dictionary<string, object?>
   {
      ["bucketName"] = bucket.Id
   };
});
```

{{% /choosable %}}

{{% choosable language java %}}

```java
package myproject;

import com.pulumi.Pulumi;
import com.pulumi.aws.s3.Bucket;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {

            // Create an AWS resource (S3 Bucket)
            var bucket = new Bucket("my-bucket");

            // Export the name of the bucket
            ctx.export("bucketName", bucket.bucket());
        });
    }
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
name: quickstart
runtime: yaml
description: A minimal AWS Pulumi YAML program

resources:
  # Create an AWS resource (S3 Bucket)
  my-bucket:
    type: aws:s3:Bucket

outputs:
  # Export the name of the bucket
  bucketName: ${my-bucket.id}
```

{{% /choosable %}}

This Pulumi program creates a new S3 bucket and exports the name of the bucket.

{{% choosable language javascript %}}

```javascript
exports.bucketName = bucket.id;
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
export const bucketName = bucket.id;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
pulumi.export('bucket_name', bucket.id)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
ctx.Export("bucketName", bucket.ID())
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
return new Dictionary<string, object?>
{
   ["bucketName"] = bucket.Id
};
```

{{% /choosable %}}

{{% choosable language java %}}

```java
ctx.export("bucketName", bucket.bucket());
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
outputs:
  bucketName: ${my-bucket.id}
```

{{% /choosable %}}

Next, you'll deploy your stack, which will provision your S3 bucket.

{{< get-started-stepper >}}

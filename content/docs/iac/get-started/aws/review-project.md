---
title_tag: Review the Project | AWS
title: Review the project files
h1: "Review the project files"
meta_desc: This page walks through the files in a newly created AWS + Pulumi project.
weight: 5
menu:
    iac:
        name: Review the project
        parent: aws-get-started
        weight: 5

aliases:
    - /docs/get-started/aws/review-project/
    - /docs/quickstart/aws/review-project/
    - /docs/clouds/aws/get-started/review-project/
---

Your new project includes a few key files:

{{% choosable language "typescript,python,go,csharp" %}}

- <span>{{< langfile >}}</span> contains your program, which declares an S3 bucket
- `Pulumi.yaml` is the [project file](/docs/iac/concepts/projects/project-file) with metadata like your project's name
- `Pulumi.dev.yaml` holds configuration for the stack you just created

{{% /choosable %}}
{{% choosable language java %}}

- `src/main/java/myproject` is the project's Java package root
- <span>{{< langfile >}}</span> contains your program, which declares an S3 bucket
- `Pulumi.yaml` is the [project file](/docs/iac/concepts/projects/project-file) with metadata like your project's name
- `Pulumi.dev.yaml` holds configuration for the stack you just created

{{% /choosable %}}
{{% choosable language yaml %}}

- `Pulumi.yaml` is the [project file](/docs/iac/concepts/projects/project-file) with metadata like your project's name, as well as your program's resources
- `Pulumi.dev.yaml` holds configuration for the stack you just created

{{% /choosable %}}

Now open {{< langfile >}} and take a look:

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

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
	"github.com/pulumi/pulumi-aws/sdk/v7/go/aws/s3"
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

return await Pulumi.Deployment.RunAsync(() =>
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

This program declares an S3 [Bucket](/registry/packages/aws/api-docs/s3/bucket/) [resource](/docs/iac/concepts/resources) and exports its ID as a [stack output](/docs/iac/concepts/stacks/#outputs). Resources are just objects with [properties](/docs/iac/concepts/inputs-outputs) that capture their inputs and outputs. Exporting the bucket's ID makes it easy to reference later.

Now you're ready to deploy!

{{< get-started-stepper >}}

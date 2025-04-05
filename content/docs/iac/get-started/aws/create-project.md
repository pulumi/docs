---
title_tag: Create a New Project | AWS
title: Create project
h1: "Get started with Pulumi and AWS"
meta_desc: This page provides an overview of how to create a new AWS + Pulumi project.
weight: 4
menu:
    iac:
        name: Create project
        parent: aws-get-started
        weight: 4

aliases:
- /docs/quickstart/aws/create-project/
- /docs/get-started/aws/create-project/
- /docs/clouds/aws/get-started/create-project/
- /docs/quickstart/aws/review-project/
- /docs/get-started/aws/review-project/
- /docs/clouds/aws/get-started/review-project/
- /docs/iac/get-started/aws/review-project/
---

## Create a new project

A [**project**](/docs/iac/concepts/projects) is a program in your chosen language that defines a collection of related
cloud resources. In this step, you will create a new project.

### Initializing your project

Each project lives in its own directory. Create a new one:

{{% choosable os "linux,macos" %}}

```bash
$ mkdir pulumi-start-aws
```

{{% /choosable %}}
{{% choosable os "windows" %}}

```powershell
> mkdir pulumi-start-aws
```

{{% /choosable %}}

Change into the new directory:

{{% choosable os "linux,macos" %}}

```bash
$ cd pulumi-start-aws
```

{{% /choosable %}}
{{% choosable os "windows" %}}

```powershell
> cd pulumi-start-aws
```

{{% /choosable %}}

Now initialize a new Pulumi project for AWS using the `pulumi new` command:

{{% choosable language javascript %}}

{{% choosable os "linux,macos" %}}

```bash
$ pulumi new aws-javascript
```

{{% /choosable %}}
{{% choosable os "windows" %}}

```powershell
> pulumi new aws-javascript
```

{{% /choosable %}}

{{% /choosable %}}
{{% choosable language typescript %}}

{{% choosable os "linux,macos" %}}

```bash
$ pulumi new aws-typescript
```

{{% /choosable %}}
{{% choosable os "windows" %}}

```powershell
> pulumi new aws-typescript
```

{{% /choosable %}}

{{% /choosable %}}
{{% choosable language python %}}

{{% choosable os "linux,macos" %}}

```bash
$ pulumi new aws-python
```

{{% /choosable %}}
{{% choosable os "windows" %}}

```powershell
> pulumi new aws-python
```

{{% /choosable %}}

{{% /choosable %}}
{{% choosable language go %}}

{{% choosable os "linux,macos" %}}

```bash
$ pulumi new aws-go
```

{{% /choosable %}}
{{% choosable os "windows" %}}

```powershell
> pulumi new aws-go
```

{{% /choosable %}}

{{% /choosable %}}
{{% choosable language csharp %}}

{{% choosable os "linux,macos" %}}

```bash
$ pulumi new aws-csharp
```

{{% /choosable %}}
{{% choosable os "windows" %}}

```powershell
> pulumi new aws-csharp
```

{{% /choosable %}}

{{% /choosable %}}
{{% choosable language java %}}

{{% choosable os "linux,macos" %}}

```bash
$ pulumi new aws-java
```

{{% /choosable %}}
{{% choosable os "windows" %}}

```powershell
> pulumi new aws-java
```

{{% /choosable %}}

{{% /choosable %}}
{{% choosable language yaml %}}

{{% choosable os "linux,macos" %}}

```bash
$ pulumi new aws-yaml
```

{{% /choosable %}}
{{% choosable os "windows" %}}

```powershell
> pulumi new aws-yaml
```

{{% /choosable %}}

{{% /choosable %}}

The `pulumi new` command interactively walks through initializing a new project, as well as creating a
[**stack**](/docs/iac/concepts/stacks) and [**configuring**](/docs/iac/concepts/config) it. A stack is an instance of your
project and you may have many of them -- like `dev`, `staging`, and `prod` -- each with different configuration settings.

You will be prompted for configuration values such as an AWS region. You can hit ENTER to accept the default of `us-east-1`,
or can type in another value such as `us-west-2`:

```
The AWS region to deploy into (aws:region) (us-east-1): us-west-2
```

{{< cli-note >}}

{{% choosable language "javascript,typescript" %}}

After some dependency installations from `npm`, the project and stack will be ready.

{{% /choosable %}}

{{% choosable language python %}}

After the command completes, the project and stack will be ready.

{{% /choosable %}}

{{% choosable language go %}}

After the command completes, the project and stack will be ready.

{{% /choosable %}}

{{% choosable language "csharp,fsharp,visualbasic" %}}

After the command completes, the project and stack will be ready.

{{% /choosable %}}

### Review your new project's contents

If you list the contents of your directory, you'll see some key files:

{{% choosable language java %}}

- `src/main/java/myproject` is the project's Java package root

{{% /choosable %}}

{{% choosable language "javascript,typescript,python,go,csharp,java" %}}

- <span>{{< langfile >}}</span> contains your project's main code that declares a new S3 bucket
- `Pulumi.yaml` is a [project file](/docs/iac/concepts/projects/project-file) containing metadata about your project like its name

{{% /choosable %}}
{{% choosable language "yaml" %}}

- `Pulumi.yaml` is a [project file](/docs/iac/concepts/projects/project-file) containing metadata about your project, like its name,
  as well as declaring your project's resources

{{% /choosable %}}

- `Pulumi.dev.yaml` contains configuration values for the stack you just initialized

Now examine the code in {{< langfile >}}:

{{% choosable language javascript %}}

```javascript
"use strict";
const pulumi = require("@pulumi/pulumi");
const aws = require("@pulumi/aws");
const awsx = require("@pulumi/awsx");

// Create an AWS resource (S3 Bucket)
const bucket = new aws.s3.BucketV2("my-bucket");

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
const bucket = new aws.s3.BucketV2("my-bucket");

// Export the name of the bucket
export const bucketName = bucket.id;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
from pulumi_aws import s3

# Create an AWS resource (S3 Bucket)
bucket = s3.BucketV2('my-bucket')

# Export the name of the bucket
pulumi.export('bucket_name', bucket.id)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/s3"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        // Create an AWS resource (S3 Bucket)
        bucket, err := s3.NewBucketV2(ctx, "my-bucket", nil)
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
   var bucket = new BucketV2("my-bucket");

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
import com.pulumi.aws.s3.BucketV2;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            // Create an AWS resource (S3 Bucket)
            var bucket = new BucketV2("my-bucket");

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
    type: aws:s3:BucketV2

outputs:
  # Export the name of the bucket
  bucketName: ${my-bucket.id}
```

{{% /choosable %}}

The program declares an AWS S3 [BucketV2](/registry/packages/aws/api-docs/s3/bucketv2/)
[resource](/docs/iac/concepts/resources) and exports its ID as a [stack output](/docs/iac/concepts/stacks/#outputs).
Resources are just objects in our language of choice with [properties](/docs/iac/concepts/inputs-outputs) capturing
their inputs and outputs. Exporting the bucket's ID makes it convenient to use afterwards.

Now you're ready for your first deployment!

{{< get-started-stepper >}}

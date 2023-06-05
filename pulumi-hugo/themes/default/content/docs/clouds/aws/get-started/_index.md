---
title_tag: Get started with Pulumi & AWS
title: Get started
h1: Get started with Pulumi & AWS
meta_desc: This page provides a guide on how to get started with AWS & Pulumi.
menu:
  clouds:
    parent: aws
    identifier: aws-get-started
    weight: 1

aliases:
- /docs/quickstart/aws/
- /docs/get-started/aws/
- /docs/quickstart/aws/begin/
- /docs/quickstart/aws/install-pulumi/
- /docs/quickstart/aws/install-language-runtime/
- /docs/quickstart/aws/configure/
- /docs/get-started/aws/install-pulumi/
- /docs/get-started/aws/install-language-runtime/
- /docs/get-started/aws/configure/
- /docs/get-started/aws/begin/
- /docs/quickstart/aws/create-project/
- /docs/get-started/aws/create-project/
- /docs/quickstart/aws/deploy-changes/
- /docs/get-started/aws/deploy-changes/
- /docs/quickstart/aws/deploy-stack/
- /docs/get-started/aws/deploy-stack/
- /docs/quickstart/aws/destroy-stack/
- /docs/get-started/aws/destroy-stack/
- /docs/quickstart/aws/modify-program/
- /docs/get-started/aws/modify-program/
- /docs/quickstart/aws/next-steps/
- /docs/get-started/aws/next-steps/
- /docs/quickstart/aws/review-project/
- /docs/get-started/aws/review-project/
- /clouds/aws/get-started/destroy-stack/
---

Pulumi's infrastructure-as-code SDK helps you create, deploy, and manage AWS containers, serverless functions, and infrastructure using familiar programming languages.

This tutorial takes you through the steps to easily deploy a static website.

## Install Pulumi

{{< install-pulumi >}}
{{% notes "info" %}}
All Windows examples in this tutorial assume you are running in PowerShell.
{{% /notes %}}
{{< /install-pulumi >}}

### Install language runtime

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language "javascript,typescript" %}}
Install [Node.js](https://nodejs.org/en/download).
{{% /choosable %}}

{{% choosable language python %}}
{{< install-python >}}
{{% /choosable %}}

{{% choosable language go %}}
{{< install-go >}}
{{% /choosable %}}

{{% choosable language "csharp,fsharp,visualbasic" %}}
{{< install-dotnet >}}
{{% /choosable %}}

{{% choosable language "java" %}}
{{< install-java >}}
{{% /choosable %}}

{{% choosable language "yaml" %}}
{{< install-yaml >}}
{{% /choosable %}}

{{< /chooser >}}

### Configure Pulumi to access AWS

Pulumi requires cloud credentials to manage and provision resources. Use an IAM user account that has **programmatic access** with rights to deploy and manage resources.

If you have previously installed and configured the AWS CLI, Pulumi will respect and use your configuration settings.

If you do not have the AWS CLI installed or plan on using Pulumi from within a CI/CD pipeline, [retrieve your access key ID and secret access key](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys) and then set the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` environment variables on your workstation:

{{< chooser os "linux,macos,windows" >}}
{{% choosable os linux %}}

```bash
$ export AWS_ACCESS_KEY_ID=<YOUR_ACCESS_KEY_ID>
$ export AWS_SECRET_ACCESS_KEY=<YOUR_SECRET_ACCESS_KEY>
```

{{% /choosable %}}

{{% choosable os macos %}}

```bash
$ export AWS_ACCESS_KEY_ID=<YOUR_ACCESS_KEY_ID>
$ export AWS_SECRET_ACCESS_KEY=<YOUR_SECRET_ACCESS_KEY>
```

{{% /choosable %}}

{{% choosable os windows %}}

```powershell
> $env:AWS_ACCESS_KEY_ID = "<YOUR_ACCESS_KEY_ID>"
> $env:AWS_SECRET_ACCESS_KEY = "<YOUR_SECRET_ACCESS_KEY>"
```

{{% /choosable %}}
{{< /chooser >}}

## Create project

Let's create your first Pulumi project, stack, and program. Pulumi [projects](/docs/concepts/projects/) and [stacks](/docs/concepts/stack/) organize Pulumi code. Projects are similar to GitHub repos and stacks are an instance of code with separate configuration. Projects can have multiple stacks for different development environments or for different cloud configurations.

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

```bash
$ mkdir quickstart && cd quickstart
$ pulumi new aws-javascript
```

{{% /choosable %}}
{{% choosable language typescript %}}

```bash
$ mkdir quickstart && cd quickstart
$ pulumi new aws-typescript
```

{{% /choosable %}}
{{% choosable language python %}}

```bash
$ mkdir quickstart && cd quickstart
$ pulumi new aws-python
```

{{% /choosable %}}
{{% choosable language go %}}

```bash
$ mkdir quickstart && cd quickstart
$ pulumi new aws-go
```

{{% /choosable %}}
{{% choosable language csharp %}}

```bash
$ mkdir quickstart && cd quickstart
$ pulumi new aws-csharp
```

{{% /choosable %}}
{{% choosable language java %}}

```bash
$ mkdir quickstart && cd quickstart
$ pulumi new aws-java
```

{{% /choosable %}}
{{% choosable language yaml %}}

```bash
$ mkdir quickstart && cd quickstart
$ pulumi new aws-yaml
```

{{% /choosable %}}
{{< /chooser >}}

The [`pulumi new`](/docs/cli/commands/pulumi_new) command creates a Pulumi project with basic scaffolding.

You will be asked for a **project name** and **project description**.

```
This command will walk you through creating a Pulumi project.

Enter a value or leave blank to accept the (default), and press <ENTER>.
Press ^C at any time to quit.

project name: (quickstart)
project description: (A minimal AWS Pulumi program)
Created project 'quickstart'
```

Then you will be asked for a **stack name**.

```
Please enter your desired stack name.
To create a stack in an organization, use the format <org-name>/<stack-name> (e.g. `acmecorp/dev`).
stack name: (dev)
Created stack 'dev'
```

Finally, you will be prompted for a configuration value for the stack, specifically the AWS region.

```
aws:region: The AWS region to deploy into: (us-west-2)
Saved config
```

After the command completes, the project and stack will be ready.

## Review project

Let's review some of the generated project files:

{{% choosable language "javascript,typescript,python,go,csharp,java" %}}

- `Pulumi.yaml` defines the [project](/docs/concepts/projects/).

{{% /choosable %}}

{{% choosable language "yaml" %}}

- `Pulumi.yaml` defines both the [project](/docs/concepts/projects/) and the program that manages your stack resources.

{{% /choosable %}}

- `Pulumi.dev.yaml` contains [configuration](/docs/concepts/config/) values for the [stack](/docs/concepts/stack/) you just initialized.

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

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

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
{{< /chooser >}}

## Deploy stack

Let's deploy the stack:

```bash
$ pulumi up
```

This command evaluates the program and determines what resources need updates. A preview is shown that outlines the changes that will be made when you run the update:

```
Previewing update (dev):

     Type                 Name            Plan
 +   pulumi:pulumi:Stack  quickstart-dev  create
 +   └─ aws:s3:Bucket     my-bucket       create

Resources:
    + 2 to create

Do you want to perform this update?
> yes
  no
  details
```

Once the preview has finished choose `yes` to create your new S3 bucket in AWS.

```
Do you want to perform this update? yes
Updating (dev):

     Type                 Name            Status
 +   pulumi:pulumi:Stack  quickstart-dev  created (4s)
 +   └─ aws:s3:Bucket     my-bucket       created (2s)

Outputs:
    bucketName: "my-bucket-58ce361"

Resources:
    + 2 created

Duration: 5s
```

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

```bash
$ pulumi stack output bucketName
```

{{% /choosable %}}

{{% choosable language typescript %}}

```bash
$ pulumi stack output bucketName
```

{{% /choosable %}}

{{% choosable language python %}}

```bash
$ pulumi stack output bucket_name
```

{{% /choosable %}}

{{% choosable language go %}}

```bash
$ pulumi stack output bucketName
```

{{% /choosable %}}

{{% choosable language csharp %}}

```bash
$ pulumi stack output bucketName
```

{{% /choosable %}}

{{% choosable language java %}}

```bash
$ pulumi stack output bucketName
```

{{% /choosable %}}

{{% choosable language yaml %}}

```bash
$ pulumi stack output bucketName
```

{{% /choosable %}}
{{< /chooser >}}

## Modify program

Now that your S3 bucket is provisioned, let's add a file to it. In the project directory, create a new file called `index.html` along with some content:

{{< chooser os "macos,linux,windows" >}}

{{% choosable os macos %}}

```bash
echo '<html>
    <body>
        <h1>Hello, Pulumi!</h1>
    </body>
</html>' > index.html
```

{{% /choosable %}}

{{% choosable os linux %}}

```bash
echo '<html>
    <body>
        <h1>Hello, Pulumi!</h1>
    </body>
</html>' > index.html
```

{{% /choosable %}}

{{% choosable os windows %}}

```powershell
@"
<html>
  <body>
    <h1>Hello, Pulumi!</h1>
  </body>
</html>
"@ | Out-File -FilePath index.html
```

{{% /choosable %}}
{{< /chooser >}}

Open the program and add this file to the S3 bucket. This uses Pulumi's `FileAsset` resource to assign the content of the file to a new  `BucketObject`:

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

In `index.js`, create the `BucketObject` right after creating the bucket itself:

```javascript
// Create an S3 Bucket object
const bucketObject = new aws.s3.BucketObject("index.html", {
    bucket: bucket.id,
    source: new pulumi.asset.FileAsset("./index.html")
});
```

{{% /choosable %}}

{{% choosable language typescript %}}

In `index.ts`, create the `BucketObject` right after creating the bucket itself:

```typescript
// Create an S3 Bucket object
const bucketObject = new aws.s3.BucketObject("index.html", {
    bucket: bucket.id,
    source: new pulumi.asset.FileAsset("./index.html")
});
```

{{% /choosable %}}

{{% choosable language python %}}

In `__main__.py`, create a new bucket object by adding the following right after creating the bucket itself:

```python
# Create an S3 Bucket object
bucketObject = s3.BucketObject(
    'index.html',
    bucket=bucket.id,
    source=pulumi.FileAsset('./index.html')
)
```

{{% /choosable %}}

{{% choosable language go %}}

In `main.go`, create the `BucketObject` right after creating the bucket itself:

```go
// Create an S3 Bucket object
_, err = s3.NewBucketObject(ctx, "index.html", &s3.BucketObjectArgs{
    Bucket:  bucket.ID(),
    Source: pulumi.NewFileAsset("./index.html"),
})
if err != nil {
    return err
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

In `Program.cs`, create a new `BucketObject` right after creating the bucket itself.

```csharp
// Create an S3 Bucket object
var bucketObject = new BucketObject("index.html", new BucketObjectArgs
{
    Bucket = bucket.BucketName,
    Source = new FileAsset("./index.html")
});
```

{{% /choosable %}}

{{% choosable language java %}}

In {{< langfile >}}, import the `FileAsset`, `BucketObject`, and `BucketObjectArgs` classes, then create the `BucketObject` right after creating the bucket itself.

```java
package myproject;

import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.pulumi.aws.s3.Bucket;
import com.pulumi.aws.s3.BucketObject;
import com.pulumi.aws.s3.BucketObjectArgs;
import com.pulumi.asset.FileAsset;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {

            // Create an AWS resource (S3 Bucket)
            var bucket = new Bucket("my-bucket");

            // Create an S3 Bucket object
            new BucketObject("index.html", BucketObjectArgs.builder()
                .bucket(bucket.id())
                .source(new FileAsset("./index.html"))
                .build()
            );

            // Export the name of the bucket
            ctx.export("bucketName", bucket.bucket());
        });
    }
}
```

{{% /choosable %}}

{{% choosable language "yaml" %}}

In {{< langfile >}}, create the `BucketObject` right below the bucket itself.

```yaml
name: quickstart
runtime: yaml
description: A minimal AWS Pulumi YAML program

resources:
  # Create an AWS resource (S3 Bucket)
  my-bucket:
    type: aws:s3:Bucket

  # Create an S3 Bucket object
  index.html:
    type: aws:s3:BucketObject
    properties:
      bucket: ${my-bucket}
      source:
        fn::fileAsset: ./index.html

outputs:
  # Export the name of the bucket
  bucketName: ${my-bucket.id}
```

{{% /choosable %}}
{{< /chooser >}}

This bucket object is part of the `Bucket` that we deployed earlier because we _reference_ the bucket name in the properties of the bucket object.

We refer to this relationship as the `BucketObject` being a _child_ resource of the S3 `Bucket` that is the _parent_ resource.

## Deploy changes

Deploy the changes by running `pulumi up` again.

```bash
$ pulumi up
```

Pulumi will run the `preview` step of the update, which computes the minimally disruptive change to achieve the desired state described by the program.

```
Previewing update (dev):

     Type                    Name            Plan
     pulumi:pulumi:Stack     quickstart-dev
 +   └─ aws:s3:BucketObject  index.html      create

Resources:
    + 1 to create
    2 unchanged

Do you want to perform this update?
> yes
  no
  details
```

Choose `yes` to proceed with the update and upload the `index.html` file to your bucket:

```
Do you want to perform this update? yes
Updating (dev):

     Type                    Name            Status
     pulumi:pulumi:Stack     quickstart-dev
 +   └─ aws:s3:BucketObject  index.html      created (0.98s)


Outputs:
    bucketName: "my-bucket-58ce361"

Resources:
    + 1 created
    2 unchanged

Duration: 3s
```

Verify the object was created in your bucket by checking the AWS Console or by running the following AWS CLI command:

{{% choosable language javascript %}}

```bash
$ aws s3 ls $(pulumi stack output bucketName)
```

{{% /choosable %}}

{{% choosable language typescript %}}

```bash
$ aws s3 ls $(pulumi stack output bucketName)
```

{{% /choosable %}}

{{% choosable language python %}}

```bash
$ aws s3 ls $(pulumi stack output bucket_name)
```

{{% /choosable %}}

{{% choosable language go %}}

```bash
$ aws s3 ls $(pulumi stack output bucketName)
```

{{% /choosable %}}

{{% choosable language csharp %}}

```bash
$ aws s3 ls $(pulumi stack output bucketName)
```

{{% /choosable %}}

{{% choosable language java %}}

```bash
$ aws s3 ls $(pulumi stack output bucketName)
```

{{% /choosable %}}

{{% choosable language yaml %}}

```bash
$ aws s3 ls $(pulumi stack output bucketName)
```

{{% /choosable %}}

Notice that your `index.html` file has been added to the bucket:

```bash
2023-04-20 17:01:06        118 index.html
```

## Modify program again

Update the `Bucket` declaration to add a `website` property and make `index.html` the home page of the website:

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language "javascript,typescript" %}}

```typescript
const bucket = new aws.s3.Bucket("my-bucket", {
    website: {
        indexDocument: "index.html",
    },
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
bucket = s3.Bucket("my-bucket",
    website=s3.BucketWebsiteArgs(
        index_document="index.html",
    ),
)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
bucket, err := s3.NewBucket(ctx, "my-bucket", &s3.BucketArgs{
    Website: &s3.BucketWebsiteArgs{
        IndexDocument: pulumi.String("index.html"),
    },
})
if err != nil {
    return err
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using Pulumi.Aws.S3.Inputs;

var bucket = new Bucket("my-bucket", new()
{
    Website = new BucketWebsiteArgs
    {
        IndexDocument = "index.html",
    },
});
```

{{% /choosable %}}

{{% choosable language java %}}

```java
import com.pulumi.aws.s3.BucketArgs;
import com.pulumi.aws.s3.inputs.BucketWebsiteArgs;

var bucket = new Bucket("my-bucket", BucketArgs.builder()
    .website(BucketWebsiteArgs.builder()
        .indexDocument("index.html")
        .build())
    .build());
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
my-bucket:
  type: aws:s3:Bucket
  properties:
    website:
      indexDocument: index.html
```

{{% /choosable %}}
{{< /chooser >}}

Lastly, you'll make a few adjustments to make these resources accessible on the Internet.

For the bucket itself, you'll need two new resources: a `BucketOwnershipControls` resource, to define the bucket's file-ownership settings, and a `BucketPublicAccessBlock` resource to allow the bucket to be accessed publicly.

For the `BucketObject`, you'll need an access-control (ACL) setting of `public-read` to allow the page to be accessed anonymously (e.g., in a browser) and a content type of `text/html` to tell AWS to serve the file as a web page.

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language "javascript,typescript" %}}

```typescript
const ownershipControls = new aws.s3.BucketOwnershipControls("ownership-controls", {
    bucket: bucket.id,
    rule: {
        objectOwnership: "ObjectWriter"
    }
});

const publicAccessBlock = new aws.s3.BucketPublicAccessBlock("public-access-block", {
    bucket: bucket.id,
    blockPublicAcls: false,
});

const bucketObject = new aws.s3.BucketObject("index.html", {
    bucket: bucket.id,
    source: new pulumi.asset.FileAsset("./index.html"),
    contentType: "text/html",
    acl: "public-read",
}, { dependsOn: publicAccessBlock });
```

{{% /choosable %}}

{{% choosable language python %}}

```python
ownership_controls = s3.BucketOwnershipControls(
    'ownership-controls',
    bucket=bucket.id,
    rule=s3.BucketOwnershipControlsRuleArgs(
        object_ownership='ObjectWriter',
    ),
)

public_access_block = s3.BucketPublicAccessBlock(
    'public-access-block', bucket=bucket.id, block_public_acls=False
)

bucket_object = s3.BucketObject(
    'index.html',
    bucket=bucket.id,
    source=pulumi.FileAsset('index.html'),
    content_type='text/html',
    acl='public-read',
    opts=pulumi.ResourceOptions(depends_on=[public_access_block]),
)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
_, err = s3.NewBucketOwnershipControls(ctx, "ownership-controls", &s3.BucketOwnershipControlsArgs{
    Bucket: bucket.ID(),
    Rule: &s3.BucketOwnershipControlsRuleArgs{
        ObjectOwnership: pulumi.String("ObjectWriter"),
    },
})
if err != nil {
    return err
}

publicAccessBlock, err := s3.NewBucketPublicAccessBlock(ctx, "public-access-block", &s3.BucketPublicAccessBlockArgs{
    Bucket:          bucket.ID(),
    BlockPublicAcls: pulumi.Bool(false),
})
if err != nil {
    return err
}

_, err = s3.NewBucketObject(ctx, "index.html", &s3.BucketObjectArgs{
    Bucket:      bucket.ID(),
    Source:      pulumi.NewFileAsset("index.html"),
    ContentType: pulumi.String("text/html"),
    Acl:         pulumi.String("public-read"),
}, pulumi.DependsOn([]pulumi.Resource{
    publicAccessBlock,
}))
if err != nil {
    return err
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
var ownershipControls = new BucketOwnershipControls("ownership-controls", new()
{
    Bucket = bucket.Id,
    Rule = new BucketOwnershipControlsRuleArgs
    {
        ObjectOwnership = "ObjectWriter",
    },
});

var publicAccessBlock = new BucketPublicAccessBlock("public-access-block", new()
{
    Bucket = bucket.Id,
    BlockPublicAcls = false,
});

var indexHtml = new BucketObject("index.html", new()
{
    Bucket = bucket.Id,
    Source = new FileAsset("./index.html"),
    ContentType = "text/html",
    Acl = "public-read",
}, new CustomResourceOptions
{
    DependsOn = new[]
    {
        publicAccessBlock,
    },
});
```

{{% /choosable %}}

{{% choosable language java %}}

```java
import com.pulumi.aws.s3.BucketOwnershipControls;
import com.pulumi.aws.s3.BucketOwnershipControlsArgs;
import com.pulumi.aws.s3.inputs.BucketOwnershipControlsRuleArgs;
import com.pulumi.aws.s3.BucketPublicAccessBlock;
import com.pulumi.aws.s3.BucketPublicAccessBlockArgs;
import com.pulumi.resources.CustomResourceOptions;
import com.pulumi.asset.FileAsset;

var ownershipControls = new BucketOwnershipControls("ownershipControls", BucketOwnershipControlsArgs.builder()
    .bucket(bucket.id())
    .rule(BucketOwnershipControlsRuleArgs.builder()
        .objectOwnership("ObjectWriter")
        .build())
    .build());

var publicAccessBlock = new BucketPublicAccessBlock("publicAccessBlock", BucketPublicAccessBlockArgs.builder()
    .bucket(bucket.id())
    .blockPublicAcls(false)
    .build());

var indexHtml = new BucketObject("index.html", BucketObjectArgs.builder()
    .bucket(bucket.id())
    .source(new FileAsset("./index.html"))
    .contentType("text/html")
    .acl("public-read")
    .build(), CustomResourceOptions.builder()
        .dependsOn(publicAccessBlock)
        .build());
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
ownership-controls:
  type: aws:s3:BucketOwnershipControls
  properties:
    bucket: ${my-bucket.id}
    rule:
      objectOwnership: ObjectWriter

public-access-block:
  type: aws:s3:BucketPublicAccessBlock
  properties:
    bucket: ${my-bucket.id}
    blockPublicAcls: false

index.html:
  type: aws:s3:BucketObject
  properties:
    bucket: ${my-bucket.id}
    source: ${homepage}
    contentType: text/html
    acl: public-read
  options:
    dependsOn:
      - ${public-access-block}
```

{{% /choosable %}}
{{< /chooser >}}

The `BucketObject` includes the Pulumi resource _option_ [`dependsOn`](/docs/concepts/options/dependson/). This setting tells Pulumi that the `BucketObject` relies indirectly on the `BucketPublicAccessBlock`, which is responsible for enabling public access to its contents.

At the end of the program, export the bucket’s endpoint URL:

{{% choosable language javascript %}}

```javascript
exports.bucketEndpoint = pulumi.interpolate`http://${bucket.websiteEndpoint}`;
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
export const bucketEndpoint = pulumi.interpolate`http://${bucket.websiteEndpoint}`;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
pulumi.export('bucket_endpoint', pulumi.Output.concat('http://', bucket.website_endpoint))
```

{{% /choosable %}}

{{% choosable language go %}}

```go
ctx.Export("bucketEndpoint", bucket.WebsiteEndpoint.ApplyT(func(websiteEndpoint string) (string, error) {
    return fmt.Sprintf("http://%v", websiteEndpoint), nil
}).(pulumi.StringOutput))
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
return new Dictionary<string, object?>
{
    // ...
    ["bucketEndpoint"] = bucket.WebsiteEndpoint.Apply(websiteEndpoint => $"http://{websiteEndpoint}"),
};
```

{{% /choosable %}}

{{% choosable language java %}}

```java
// ...
ctx.export("bucketEndpoint", bucket.websiteEndpoint().applyValue(websiteEndpoint -> String.format("http://%s", websiteEndpoint)));
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
outputs:
  # ...
  bucketEndpoint: http://${my-bucket.websiteEndpoint}
```

{{% /choosable %}}

## Deploy website

Update your stack to deploy these changes to AWS:

```bash
$ pulumi up
```

Review the preview of the changes before deploying:

```
Previewing update (dev):

     Type                               Name                 Plan       Info
     pulumi:pulumi:Stack                quickstart-dev
 ~   ├─ aws:s3:Bucket                   my-bucket            update     [diff: +website]
 +   ├─ aws:s3:BucketOwnershipControls  ownership-controls   create
 +   ├─ aws:s3:BucketPublicAccessBlock  public-access-block  create
 ~   └─ aws:s3:BucketObject             index.html           update     [diff: ~acl,contentType]

Outputs:
  + bucketEndpoint: output<string>

Resources:
    + 2 to create
    ~ 2 to update
    4 changes. 1 unchanged

Do you want to perform this update?
> yes
  no
  details
```

Choose `yes` to perform the deployment:

```
Do you want to perform this update? yes
Updating (dev):

     Type                               Name                 Status              Info
     pulumi:pulumi:Stack                quickstart-dev
 ~   ├─ aws:s3:Bucket                   my-bucket            updated (3s)        [diff: +website]
 +   ├─ aws:s3:BucketOwnershipControls  ownership-controls   created (0.84s)
 +   ├─ aws:s3:BucketPublicAccessBlock  public-access-block  created (1s)
 ~   └─ aws:s3:BucketObject             index.html           updated (0.53s)     [diff: ~acl,contentType]

Outputs:
  + bucketEndpoint: "http://my-bucket-dfd6bd0.s3-website-us-east-1.amazonaws.com"
    bucketName    : "my-bucket-dfd6bd0"

Resources:
    + 2 created
    ~ 2 updated
    4 changes. 1 unchanged

Duration: 8s
```

Check out your new website at the URL or make a `curl` request:

{{% choosable language javascript %}}

```bash
$ curl $(pulumi stack output bucketEndpoint)
```

{{% /choosable %}}

{{% choosable language typescript %}}

```bash
$ curl $(pulumi stack output bucketEndpoint)
```

{{% /choosable %}}

{{% choosable language python %}}

```bash
$ curl $(pulumi stack output bucket_endpoint)
```

{{% /choosable %}}

{{% choosable language go %}}

```bash
$ curl $(pulumi stack output bucketEndpoint)
```

{{% /choosable %}}

{{% choosable language csharp %}}

```bash
$ curl $(pulumi stack output bucketEndpoint)
```

{{% /choosable %}}

{{% choosable language java %}}

```bash
$ curl $(pulumi stack output bucketEndpoint)
```

{{% /choosable %}}

{{% choosable language yaml %}}

```bash
$ curl $(pulumi stack output bucketEndpoint)
```

{{% /choosable %}}

```bash
<html>
    <body>
        <h1>Hello, Pulumi!</h1>
    </body>
</html>
```

## Destroy stack

Now that you've seen how to deploy changes to our program, let's clean up and tear down the resources that are part of your stack.

To destroy resources, run the following:

```bash
$ pulumi destroy
```

```
Previewing destroy (dev):

     Type                               Name                 Plan
 -   pulumi:pulumi:Stack                quickstart-dev       delete
 -   ├─ aws:s3:BucketObject             index.html           delete
 -   ├─ aws:s3:BucketOwnershipControls  ownership-controls   delete
 -   ├─ aws:s3:BucketPublicAccessBlock  public-access-block  delete
 -   └─ aws:s3:Bucket                   my-bucket            delete

Outputs:
  - bucketEndpoint: "http://my-bucket-dfd6bd0.s3-website-us-east-1.amazonaws.com"
  - bucketName    : "my-bucket-dfd6bd0"

Resources:
    - 5 to delete

Do you want to perform this destroy? yes
Destroying (dev):

     Type                               Name                 Status
 -   pulumi:pulumi:Stack                quickstart-dev       deleted
 -   ├─ aws:s3:BucketObject             index.html           deleted (1s)
 -   ├─ aws:s3:BucketPublicAccessBlock  public-access-block  deleted (0.28s)
 -   ├─ aws:s3:BucketOwnershipControls  ownership-controls   deleted (0.47s)
 -   └─ aws:s3:Bucket                   my-bucket            deleted (0.39s)

Outputs:
  - bucketEndpoint: "http://my-bucket-dfd6bd0.s3-website-us-east-1.amazonaws.com"
  - bucketName    : "my-bucket-dfd6bd0"

Resources:
    - 5 deleted

Duration: 4s
```

To delete the stack itself, run [`pulumi stack rm`](/docs/cli/commands/pulumi_stack_rm). This removes the stack and the update history from Pulumi Cloud.

## Next steps

Congrats! You've deployed your first project on AWS with Pulumi. Try a next step!

- Dive into [Learn Pulumi](/learn/pulumi-fundamentals) for a comprehensive walkthrough of key Pulumi concepts in the context of a real-life application.
- Explore how-to guides: [static websites](/registry/packages/aws-native/how-to-guides/aws-native-ts-s3-folder/), [EC2 virtual machines](/registry/packages/aws/how-to-guides/ec2-webserver/), [EKS clusters](/registry/packages/aws/how-to-guides/aws-ts-eks/), [Fargate containers](/registry/packages/aws/how-to-guides/ecs-fargate/), and [serverless applications](/registry/packages/aws/how-to-guides/rest-api/).
- Learn how Pulumi works from its architecture to key concepts, including [stacks](/docs/concepts/stack/), [state](/docs/concepts/state/), [configuration](/docs/concepts/config/), and [secrets](/docs/concepts/secrets/).
- Read through the [latest blog posts](/blog/tag/aws) about using Pulumi with AWS.

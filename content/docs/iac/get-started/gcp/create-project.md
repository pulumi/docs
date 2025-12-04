---
title_tag: Create a New Project | Google Cloud
title: Create project
h1: "Get started with Pulumi and Google Cloud"
meta_desc: This page provides an overview of how to create a new Google Cloud + Pulumi project.
weight: 4
menu:
    iac:
        name: Create project
        identifier: gcp-get-started.create-project
        parent: gcp-get-started
        weight: 4

aliases:
    - /docs/quickstart/gcp/create-project/
    - /docs/clouds/gcp/get-started/create-project/
    - /docs/quickstart/gcp/review-project/
    - /docs/get-started/gcp/review-project/
    - /docs/clouds/gcp/get-started/review-project/
---

## Create a new project

A [**project**](/docs/iac/concepts/projects) is a program in your chosen language that defines a collection of related
cloud resources. In this step, you will create a new project.

### Initializing your project

Each project lives in its own directory. Create a new one:

{{% choosable os "linux,macos" %}}

```bash
$ mkdir quickstart
```

{{% /choosable %}}
{{% choosable os "windows" %}}

```powershell
> mkdir quickstart
```

{{% /choosable %}}

Change into the new directory:

{{% choosable os "linux,macos" %}}

```bash
$ cd quickstart
```

{{% /choosable %}}
{{% choosable os "windows" %}}

```powershell
> cd quickstart
```

{{% /choosable %}}

Now initialize a new Pulumi project for Google Cloud using the `pulumi new` command:

{{% choosable language typescript %}}

{{% choosable os "linux,macos" %}}

```bash
$ pulumi new gcp-typescript
```

{{% /choosable %}}
{{% choosable os "windows" %}}

```powershell
> pulumi new gcp-typescript
```

{{% /choosable %}}

{{% /choosable %}}
{{% choosable language python %}}

{{% choosable os "linux,macos" %}}

```bash
$ pulumi new gcp-python
```

{{% /choosable %}}
{{% choosable os "windows" %}}

```powershell
> pulumi new gcp-python
```

{{% /choosable %}}

{{% /choosable %}}
{{% choosable language go %}}

{{% choosable os "linux,macos" %}}

```bash
$ pulumi new gcp-go
```

{{% /choosable %}}
{{% choosable os "windows" %}}

```powershell
> pulumi new gcp-go
```

{{% /choosable %}}

{{% /choosable %}}
{{% choosable language csharp %}}

{{% choosable os "linux,macos" %}}

```bash
$ pulumi new gcp-csharp
```

{{% /choosable %}}
{{% choosable os "windows" %}}

```powershell
> pulumi new gcp-csharp
```

{{% /choosable %}}

{{% /choosable %}}

{{% choosable language java %}}

{{% choosable os "linux,macos" %}}

```bash
$ pulumi new gcp-java
```

{{% /choosable %}}
{{% choosable os "windows" %}}

```powershell
> pulumi new gcp-java
```

{{% /choosable %}}

{{% /choosable %}}

{{% choosable language yaml %}}

{{% choosable os "linux,macos" %}}

```bash
$ pulumi new gcp-yaml
```

{{% /choosable %}}
{{% choosable os "windows" %}}

```powershell
> pulumi new gcp-yaml
```

{{% /choosable %}}

{{% /choosable %}}

The `pulumi new` command interactively walks through initializing a new project, as well as creating a
[**stack**](/docs/iac/concepts/stacks) and [**configuring**](/docs/iac/concepts/config) it. A stack is an instance of your
project and you may have many of them -- like `dev`, `staging`, and `prod` -- each with different configuration settings.

You will be prompted for configuration values such as a Google Cloud project ID. You can hit ENTER to accept the defaults,
or can type in your values:

```
gcp:project: The Google Cloud project to deploy into: my-gcp-project
```

{{< cli-note >}}

{{% choosable language "typescript" %}}

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

{{% choosable language java %}}

After the command completes, the project and stack will be ready.

{{% /choosable %}}

{{% choosable language yaml %}}

After the command completes, the project and stack will be ready.

{{% /choosable %}}

### Review your new project's contents

If you list the contents of your directory, you'll see some key files:

{{% choosable language java %}}

- `src/main/java/myproject` is the project's Java package root

{{% /choosable %}}

{{% choosable language "typescript,python,go,csharp,java" %}}

- <span>{{< langfile >}}</span> contains your project's main code that declares a Google Cloud Storage bucket
- `Pulumi.yaml` is a [project file](/docs/iac/concepts/projects/project-file) containing metadata about your project like its name

{{% /choosable %}}
{{% choosable language "yaml" %}}

- `Pulumi.yaml` is a [project file](/docs/iac/concepts/projects/project-file) containing metadata about your project, like its name, as well as declaring your project's resources

{{% /choosable %}}

- `Pulumi.dev.yaml` contains configuration values for the stack you just initialized

Now examine the code in {{< langfile >}}:

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as gcp from "@pulumi/gcp";

// Create a Google Cloud resource (Storage Bucket)
const bucket = new gcp.storage.Bucket("my-bucket", {
    location: "US",
});

// Export the DNS name of the bucket
export const bucketName = bucket.url;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
from pulumi_gcp import storage

# Create a Google Cloud resource (Storage Bucket)
bucket = storage.Bucket("my-bucket", location="US")

# Export the DNS name of the bucket
pulumi.export("bucket_name", bucket.url)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-gcp/sdk/v7/go/gcp/storage"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Create a Google Cloud resource (Storage Bucket)
		bucket, err := storage.NewBucket(ctx, "my-bucket", &storage.BucketArgs{
			Location: pulumi.String("US"),
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
using System.Collections.Generic;

return await Pulumi.Deployment.RunAsync(() =>
{
    // Create a Google Cloud resource (Storage Bucket).
    var bucket = new Bucket("my-bucket", new BucketArgs
    {
        Location = "US",
    });

    // Export the DNS name of the bucket.
    return new Dictionary<string, object?>
    {
        ["bucketName"] = bucket.Url,
    };
});
```

{{% /choosable %}}

{{% choosable language java %}}

```java
package myproject;

import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.pulumi.gcp.storage.Bucket;
import com.pulumi.gcp.storage.BucketArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            // Create a Google Cloud resource (Storage Bucket)
            var bucket = new Bucket("my-bucket", BucketArgs.builder()
                .location("US")
                .build());

            // Export the DNS name of the bucket
            ctx.export("bucketName", bucket.url());
        });
    }
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
name: quickstart
runtime: yaml
description: A minimal Google Cloud Pulumi YAML program

resources:
  # Create a Google Cloud resource (Storage Bucket)
  my-bucket:
    type: gcp:storage:Bucket
    properties:
      location: US

outputs:
  # Export the DNS name of the bucket
  bucketName: ${my-bucket.url}
```

{{% /choosable %}}

This Pulumi program creates a new storage bucket resource and exports the DNS name of the bucket as a [stack output](/docs/iac/concepts/stacks/#outputs). Resources are just objects in our language of choice with [properties](/docs/iac/concepts/inputs-outputs) capturing their inputs and outputs. Exporting the bucket's ID makes it convenient to use afterwards.

Next, you'll deploy your stack, which will provision your storage bucket.

{{< get-started-stepper >}}

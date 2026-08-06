---
title_tag: Import Terraform Modules | Pulumi for Terraform Users
title: Import Terraform Modules
h1: "Import Terraform Modules"
meta_desc: Learn how to use existing Terraform modules directly in Pulumi programs, leveraging the Terraform Registry ecosystem.
weight: 5
menu:
    iac:
        name: Import Terraform Modules
        parent: terraform-get-started
        weight: 5

aliases:
---

## Leverage the module ecosystem

Pulumi can directly use existing Terraform modules from the Terraform Registry, private registries, or local sources. This allows you to access thousands of existing modules without rewriting them in Pulumi.
It's powered by the [Any HCL Module](/registry/packages/hcl/) package, which turns any Terraform or OpenTofu module into a Pulumi component, either as a strongly typed SDK or loaded dynamically at runtime.

## Add Terraform modules

Use the `pulumi package add` command to add Terraform modules to your project:

```bash
# Add a module from the Terraform Registry
$ pulumi package add hcl module terraform-aws-modules/s3-bucket/aws 4.1.2

# Add a local module
$ pulumi package add hcl module ./path/to/module
```

## Example: AWS S3 bucket module

Let's use the popular AWS `s3-bucket` module to create an S3 bucket and export its outputs:

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language "typescript" %}}

First, create a new Pulumi program:

```bash
$ mkdir pulumi-terraform-modules-test && cd pulumi-terraform-modules-test
$ pulumi new aws-typescript --yes
```

Next, add the S3 bucket module:

```bash
$ pulumi package add hcl module terraform-aws-modules/s3-bucket/aws 4.1.2
```

Then use it in your Pulumi program:

```typescript
import * as s3Bucket from "@pulumi/s3-bucket";

// Create an S3 bucket using the Terraform module
const bucket = new s3Bucket.Module("my-bucket", {
    bucketPrefix: "my-example-bucket",
    tags: {
        Environment: "dev",
    },
});

// The module's outputs are strongly typed
export const bucketArn = bucket.s3BucketArn;
export const bucketId = bucket.s3BucketId;
```

{{% /choosable %}}

{{% choosable language "python" %}}

First, create a new Pulumi program:

```bash
$ mkdir pulumi-terraform-modules-test && cd pulumi-terraform-modules-test
$ pulumi new aws-python --yes
```

Next, add the S3 bucket module:

```bash
$ pulumi package add hcl module terraform-aws-modules/s3-bucket/aws 4.1.2
```

Then use it in your Pulumi program:

```python
import pulumi
import pulumi_s3_bucket as s3bucket

# Create an S3 bucket using the Terraform module
bucket = s3bucket.Module("my-bucket",
    bucket_prefix="my-example-bucket",
    tags={
        "Environment": "dev",
    })

# The module's outputs are strongly typed
pulumi.export("bucket_arn", bucket.s3_bucket_arn)
pulumi.export("bucket_id", bucket.s3_bucket_id)
```

{{% /choosable %}}

{{% choosable language "go" %}}

First, create a new Pulumi program:

```bash
$ mkdir pulumi-terraform-modules-test && cd pulumi-terraform-modules-test
$ pulumi new aws-go --yes
```

Next, add the S3 bucket module:

```bash
$ pulumi package add hcl module terraform-aws-modules/s3-bucket/aws 4.1.2
```

Then use it in your Pulumi program:

```go
package main

import (
	"example.com/pulumi-s3-bucket/sdk/go/s3bucket"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Create an S3 bucket using the Terraform module
		bucket, err := s3bucket.NewModule(ctx, "my-bucket", &s3bucket.ModuleArgs{
			BucketPrefix: pulumi.String("my-example-bucket"),
			Tags: pulumi.StringMap{
				"Environment": pulumi.String("dev"),
			},
		})
		if err != nil {
			return err
		}
		// The module's outputs are strongly typed
		ctx.Export("bucketArn", bucket.S3BucketArn)
		ctx.Export("bucketId", bucket.S3BucketId)
		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language "csharp" %}}

First, create a new Pulumi program:

```bash
$ mkdir pulumi-terraform-modules-test && cd pulumi-terraform-modules-test
$ pulumi new aws-csharp --yes
```

Next, add the S3 bucket module:

```bash
$ pulumi package add hcl module terraform-aws-modules/s3-bucket/aws 4.1.2
```

{{% notes type="tip" %}}
The `pulumi package add ...` command will add the required dependencies to the solution file, but you'll need to manually add the following directive:

```xml {hl_lines=[3]}
  <PropertyGroup>
    <!-- ... -->
    <DefaultItemExcludes>$(DefaultItemExcludes);sdks/**/*.cs</DefaultItemExcludes>
  </PropertyGroup>
```

{{% /notes %}}

Then use it in your Pulumi program:

```csharp
using System.Collections.Generic;
using Pulumi;
using Pulumi.S3Bucket;

return await Deployment.RunAsync(() =>
{
    // Create an S3 bucket using the Terraform module
    var bucket = new Module("my-bucket", new ModuleArgs
    {
        BucketPrefix = "my-example-bucket",
        Tags =
        {
            { "Environment", "dev" },
        },
    });

    // The module's outputs are strongly typed
    return new Dictionary<string, object?>
    {
        ["bucketArn"] = bucket.S3BucketArn,
        ["bucketId"] = bucket.S3BucketId,
    };
});
```

{{% /choosable %}}

{{% choosable language "java" %}}

First, create a new Pulumi program:

```bash
$ mkdir pulumi-terraform-modules-test && cd pulumi-terraform-modules-test
$ pulumi new aws-java --yes
```

Next, add the S3 bucket module:

```bash
$ pulumi package add hcl module terraform-aws-modules/s3-bucket/aws 4.1.2
```

{{% notes type="tip" %}}
The `pulumi package add ...` command will output some important instructions. There are two steps you must perform manually: copy the contents of the generated SDK to your Java project, and add the dependencies to `pom.xml`:

```xml {hl_lines=["3-12"]}
     <dependencies>
        <!-- ... -->
         <dependency>
             <groupId>com.google.code.findbugs</groupId>
             <artifactId>jsr305</artifactId>
             <version>3.0.2</version>
         </dependency>
         <dependency>
             <groupId>com.google.code.gson</groupId>
             <artifactId>gson</artifactId>
             <version>2.8.9</version>
         </dependency>
     </dependencies>
```

{{% /notes %}}

Then use it in your Pulumi program:

```java
package myproject;

import com.pulumi.Pulumi;
import com.pulumi.s3bucket.Module;
import com.pulumi.s3bucket.ModuleArgs;
import java.util.Map;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            // Create an S3 bucket using the Terraform module
            var bucket = new Module("my-bucket", ModuleArgs.builder()
                .bucketPrefix("my-example-bucket")
                .tags(Map.of("Environment", "dev"))
                .build());

            // The module's outputs are strongly typed
            ctx.export("bucketArn", bucket.s3BucketArn());
            ctx.export("bucketId", bucket.s3BucketId());
        });
    }
}
```

{{% /choosable %}}

{{% choosable language "yaml" %}}

First, create a new Pulumi program:

```bash
$ mkdir pulumi-terraform-modules-test && cd pulumi-terraform-modules-test
$ pulumi new aws-yaml --yes
```

Next, add the S3 bucket module:

```bash
$ pulumi package add hcl module terraform-aws-modules/s3-bucket/aws 4.1.2
```

Then use it in your Pulumi program:

```yaml
name: pulumi-terraform-modules-example
runtime: yaml
description: Use a Terraform module in Pulumi

resources:
  # Create an S3 bucket using the Terraform module
  my-bucket:
    type: s3-bucket:index:Module
    properties:
      bucketPrefix: my-example-bucket
      tags:
        Environment: dev

# The module's outputs are strongly typed
outputs:
  bucketArn: ${my-bucket.s3BucketArn}
  bucketId: ${my-bucket.s3BucketId}

packages:
  s3-bucket:
    source: hcl
    version: 0.13.0
    parameters:
      - module
      - terraform-aws-modules/s3-bucket/aws
      - 4.1.2
```

{{% /choosable %}}

## Load a module at runtime

Generating an SDK gives you strongly typed inputs and outputs, IDE completion, and a package you can pin and share across your team. When you'd rather trade that type safety for flexibility — for example, to load a module whose address isn't known until runtime — you can use the [Any HCL Module](/registry/packages/hcl/) package directly.

Add the Any HCL Module package to your project:

```bash
$ pulumi package add hcl
```

Then use its `Module` resource to load your desired module. The constructor takes a module `source`, an optional `version`, and a map of `inputs`, and exposes the module's outputs as an untyped map:

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language "typescript" %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as hcl from "@pulumi/hcl";

const bucket = new hcl.Module("bucket", {
    source: "terraform-aws-modules/s3-bucket/aws",
    version: "4.1.2",
    inputs: {
        bucket_prefix: "my-example-bucket",
    },
});

export const bucketArn = bucket.outputs.apply(o => o["s3_bucket_arn"]);
```

{{% /choosable %}}

{{% choosable language "python" %}}

```python
import pulumi
import pulumi_hcl as hcl

bucket = hcl.Module("bucket",
    source="terraform-aws-modules/s3-bucket/aws",
    version="4.1.2",
    inputs={
        "bucket_prefix": "my-example-bucket",
    })

pulumi.export("bucket_arn", bucket.outputs["s3_bucket_arn"])
```

{{% /choosable %}}

{{% choosable language "go" %}}

```go
package main

import (
	"github.com/pulumi/pulumi-hcl/sdk/go/hcl"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		bucket, err := hcl.NewModule(ctx, "bucket", &hcl.ModuleArgs{
			Source:  "terraform-aws-modules/s3-bucket/aws",
			Version: pulumi.StringRef("4.1.2"),
			Inputs: pulumi.Map{
				"bucket_prefix": pulumi.String("my-example-bucket"),
			},
		})
		if err != nil {
			return err
		}
		ctx.Export("bucketArn", bucket.Outputs.MapIndex(pulumi.String("s3_bucket_arn")))
		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language "csharp" %}}

```csharp
using System.Collections.Generic;
using Pulumi;
using Pulumi.Hcl;

return await Deployment.RunAsync(() =>
{
    var bucket = new Module("bucket", new ModuleArgs
    {
        Source = "terraform-aws-modules/s3-bucket/aws",
        Version = "4.1.2",
        Inputs =
        {
            { "bucket_prefix", "my-example-bucket" },
        },
    });

    return new Dictionary<string, object?>
    {
        ["bucketArn"] = bucket.Outputs.Apply(o => o["s3_bucket_arn"]),
    };
});
```

{{% /choosable %}}

{{% choosable language "java" %}}

```java
package myapp;

import com.pulumi.Pulumi;
import com.pulumi.hcl.Module;
import com.pulumi.hcl.ModuleArgs;
import java.util.Map;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            var bucket = new Module("bucket", ModuleArgs.builder()
                .source("terraform-aws-modules/s3-bucket/aws")
                .version("4.1.2")
                .inputs(Map.of(
                    "bucket_prefix", "my-example-bucket"))
                .build());

            ctx.export("bucketArn", bucket.outputs().applyValue(o -> o.get("s3_bucket_arn")));
        });
    }
}
```

{{% /choosable %}}

{{% choosable language "yaml" %}}

```yaml
name: example
runtime: yaml
resources:
  bucket:
    type: hcl:index:Module
    properties:
      source: terraform-aws-modules/s3-bucket/aws
      version: "4.1.2"
      inputs:
        bucket_prefix: my-example-bucket
outputs:
  bucketArn: ${bucket.outputs["s3_bucket_arn"]}
```

{{% /choosable %}}

## Compare with Terraform

The same functionality in Terraform would look like:

```hcl
# Terraform equivalent
module "s3_bucket" {
  source = "terraform-aws-modules/s3-bucket/aws"

  bucket_prefix = "my-example-bucket"

  tags = {
    Environment = "dev"
  }
}

output "bucket_arn" {
  value = module.s3_bucket.s3_bucket_arn
}

output "bucket_id" {
  value = module.s3_bucket.s3_bucket_id
}
```

## Best practices

1. **Pin module versions**: Always specify module versions in production
2. **Review module source**: Understand what the module does before using it
3. **Test module outputs**: Verify that module outputs work as expected
4. **Monitor module updates**: Keep track of module updates and breaking changes
5. **Use reputable sources**: Prefer well-maintained modules from trusted sources
6. **Document module usage**: Document why you chose specific modules and their configuration
7. **Use `pulumi install` for setup**: When cloning a project that uses Terraform modules, run [`pulumi install`](/docs/iac/cli/commands/pulumi_install/) to install all dependencies, including local SDKs defined in `Pulumi.yaml`

## Deploy and clean up

Test your deployment and clean up resources:

```bash
# Deploy the stack
$ pulumi up

# When done, destroy the resources
$ pulumi destroy
```

{{< get-started-stepper >}}

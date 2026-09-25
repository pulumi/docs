---
title_tag: Use Terraform modules in Pulumi | Pulumi
title: Use Terraform modules in Pulumi
h1: Use Terraform modules in Pulumi
meta_desc: Use existing Terraform and OpenTofu modules directly in your Pulumi programs, with generated, typed SDKs in any Pulumi language.
menu:
  integrations:
    name: Terraform modules
    parent: integrations-terraform
    identifier: integrations-terraform-modules
    weight: 4
aliases:
  - /docs/iac/using-pulumi/extending-pulumi/use-terraform-module/
  - /docs/iac/extending-pulumi/use-terraform-module/
  - /docs/iac/build-with-pulumi/use-terraform-module/
  - /docs/iac/guides/building-extending/using-existing-tools/use-terraform-module/
  - /docs/iac/get-started/terraform/terraform-modules/
---

This guide will walk you through the process of using existing Terraform modules directly in your Pulumi programs, allowing you to leverage the vast Terraform module ecosystem.

{{< notes type="info" >}}
**Prerequisites:**

- The [Pulumi CLI](/docs/install/)
- One of Pulumi's [supported language runtimes](/docs/iac/languages-sdks/) installed
- Access to a cloud provider account for deployment (e.g., AWS, Azure, Google Cloud)

{{< /notes >}}

## Why use Terraform modules in Pulumi?

Terraform has a mature ecosystem with thousands of modules available in the [Terraform Registry](https://registry.terraform.io/). These modules encapsulate well-tested infrastructure patterns that you might want to leverage in your Pulumi projects without having to rewrite them.

Also, many Terraform users have created their own custom modules and would like to avoid re-writing them in order to use Pulumi. Using Terraform modules directly within Pulumi allows you to use Terraform and Pulumi side-by-side, enabling the two technologies to coexist, taking a slower gentler migration path from Terraform to Pulumi. This is especially powerful in larger organizations, where some teams prefer Pulumi's workflows, and others prefer to continue using Terraform.

### Key benefits

- **Leverage Existing Modules**: Use the rich ecosystem of Terraform modules directly in Pulumi.
- **Migrate Gradually**: Incrementally migrate from Terraform to Pulumi without rewriting everything at once.
- **Consistency**: Maintain consistency across teams that may be using a mix of Terraform and Pulumi.

## How it works

The [Any HCL Module](/registry/packages/hcl/) package allows you to consume Terraform modules as if they were native Pulumi packages. It works by:

1. Automatically installing and managing [OpenTofu](https://opentofu.org/) (an open-source Terraform-compatible implementation) to execute the module.
2. Passing the inputs you provide to the module as Terraform variables.
3. Managing state through your standard Pulumi state backend.
4. Exposing module outputs as native Pulumi outputs.

## Get started

### Add a Terraform module to your Pulumi project

A [Pulumi HCL](/docs/iac/languages-sdks/hcl/) program can skip this step and declare the module inline with a `module` block, as the [example below](#example-aws-s3-bucket-module) shows. In every other language, first add the module to your project using the `pulumi package add` command:

```bash
pulumi package add hcl module <module-source> [<version>]
```

Where:

- `<module-source>` is either a registry module identifier (e.g. `terraform-aws-modules/rds/aws`) or a local path
- `<version>` is an optional version constraint (e.g. `3.5.0`)

For example, to add the AWS S3 bucket module from the Terraform Registry:

```bash
pulumi package add hcl module terraform-aws-modules/s3-bucket/aws 4.1.2
```

This will generate a local SDK in your programming language that you can import into your Pulumi program.

{{% notes type="tip" %}}
See [Local SDKs](/docs/iac/guides/building-extending/packages/local-sdks/) for details on generating and using SDKs from local or parameterized providers.
{{% /notes %}}

### Use a local Terraform module

You can also use local Terraform modules:

```bash
pulumi package add hcl module ./path/to/module
```

Any directory containing `.tf` files and optionally `variables.tf` and `outputs.tf` is considered a valid module.

### Use a module from Pulumi Cloud

If your organization publishes Terraform modules to the [Pulumi Cloud registry](/docs/integrations/terraform/module-registry/), every published version is converted into a Pulumi package for you. Install it by package name, which is the module's name and system joined with a hyphen. The system is the last segment of the module's address, naming what the module provisions, such as `aws` or `azurerm`:

```bash
pulumi package add <name>-<system>[@<version>]
```

A module published as `acme-corp/vpc/aws` installs as `vpc-aws`. This is the same as any other Pulumi package: you get a generated SDK in your language, an [API reference](/docs/idp/concepts/private-registry/#api-documentation) on the package's page, and [usage tracking](/docs/idp/concepts/private-registry/#usage-tracking) showing which of your stacks depend on it and which are behind the latest version. Installing a converted package requires Pulumi CLI 3.248.0 or newer; see [Download & Install Pulumi](/docs/install/) to upgrade.

The package's page in Pulumi Cloud shows whether a given version has converted.

See [Terraform Modules in the Pulumi Cloud Registry](/docs/integrations/terraform/module-registry/) for the publishing side and the broader module workflow.

## Example: AWS S3 bucket module

Here's an example of how to use the AWS S3 bucket module to create a bucket in your Pulumi program.

{{% choosable language "typescript,python,go,csharp,java,yaml" %}}

First, add the module to your project:

```bash
$ pulumi package add hcl module terraform-aws-modules/s3-bucket/aws 4.1.2
```

After adding the package, your `Pulumi.yaml` is updated with the module definition:

**Example:** Pulumi.yaml

```yaml
name: s3-bucket-example
runtime:
  name: nodejs
  options:
    packagemanager: npm
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

{{% choosable language "hcl" %}}

An HCL program declares the module inline, so there is no `pulumi package add` step and no generated SDK. The `Pulumi.yaml` only has to select the runtime:

**Example:** Pulumi.yaml

```yaml
name: s3-bucket-example
runtime: hcl
```

{{% /choosable %}}

{{% chooser language "typescript,python,go,csharp,java,yaml,hcl" %}}

{{% choosable language typescript %}}

Since this was a TypeScript project, Pulumi generated a TypeScript SDK for the module, making it available as `@pulumi/s3-bucket`. We can now use the Terraform module directly in our code:

**Example:** index.ts

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

{{% choosable language python %}}

Since this was a Python project, Pulumi generated a Python SDK for the module, making it available as `pulumi_s3_bucket`. We can now use the Terraform module directly in our code:

**Example:** `__main__.py`

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

{{% choosable language go %}}

Since this was a Go project, Pulumi generated a Go SDK for the module. We can now use the Terraform module directly in our code:

**Example:** `main.go`

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

{{% choosable language csharp %}}

Since this was a C# project, Pulumi generated a C# SDK for the module, making it available as `Pulumi.S3Bucket`. We can now use the Terraform module directly in our code:

**Example:** `Program.cs`

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

{{% choosable language java %}}

Since this was a Java project, Pulumi generated a Java SDK for the module, making it available as `com.pulumi.s3bucket`. We can now use the Terraform module directly in our code:

**Example:** `App.java`

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

{{% choosable language yaml %}}

When authoring in YAML, there's no SDK to generate — you reference the module by its schema token, which takes the format `<package-name>:index:Module`:

**Example:** `Pulumi.yaml`

```yaml
name: s3-bucket-example
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

{{% choosable language hcl %}}

Declare the module with a `module` block and read its outputs as `module.<name>.<output>`. HCL programs keep the module's original snake_case input and output names:

**Example:** main.tf

```hcl
# Create an S3 bucket using the Terraform module
module "s3_bucket" {
  source  = "terraform-aws-modules/s3-bucket/aws"
  version = "4.1.2"

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

Run `pulumi install` to fetch the module and the providers it uses. Besides registry addresses like this one, a `module` block accepts local paths, Git URLs, and HTTP archives; see [Module sources](/docs/iac/languages-sdks/hcl/hcl-language-reference/#module-sources).

{{% /choosable %}}

{{% /chooser %}}

In the above code, the imported Terraform module works the same as any other Pulumi code. Outputs are returned, and resource state is stored in your Pulumi state storage, alongside all your other Pulumi-native resources. This also means that resource dependencies work as expected between Pulumi-native resources and resources created by Terraform modules.

## Load a module at runtime

Generating an SDK gives you strongly typed inputs and outputs, IDE completion, and a package you can pin and share across your team. When you'd rather trade that type safety for flexibility — for example, to load a module whose address isn't known until runtime — you can use the [Any HCL Module](/registry/packages/hcl/) package directly.

{{% choosable language "typescript,python,go,csharp,java,yaml" %}}

Add the Any HCL Module package to your project:

```bash
$ pulumi package add hcl
```

Then use its `Module` resource to load the module you want. The constructor takes a module `source`, an optional `version`, and a map of `inputs`, and exposes the module's outputs as an untyped map:

{{% /choosable %}}

{{% choosable language "hcl" %}}

A Pulumi HCL `module` block can't do this, because its `source` must be a literal string. Use the package's `hcl_module` resource instead, whose `source` is an ordinary argument that can come from a variable. Declare the package in `required_providers` rather than running `pulumi package add`, then run `pulumi install`. The resource takes a module `source`, an optional `version`, and a map of `inputs`, and exposes the module's outputs as an untyped map:

{{% /choosable %}}

{{< chooser language "typescript,python,go,csharp,java,yaml,hcl" / >}}

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

{{% choosable language "hcl" %}}

```hcl
terraform {
  required_providers {
    hcl = {
      source = "pulumi/hcl"
    }
  }
}

resource "hcl_module" "bucket" {
  source  = "terraform-aws-modules/s3-bucket/aws"
  version = "4.1.2"

  inputs = {
    bucket_prefix = "my-example-bucket"
  }
}

output "bucket_arn" {
  value = hcl_module.bucket.outputs["s3_bucket_arn"]
}
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
1. **Review module source**: Understand what the module does before using it
1. **Test module outputs**: Verify that module outputs work as expected
1. **Monitor module updates**: Keep track of module updates and breaking changes
1. **Use reputable sources**: Prefer well-maintained modules from trusted sources
1. **Document module usage**: Document why you chose specific modules and their configuration
1. **Use `pulumi install` for setup**: When cloning a project that uses Terraform modules, run [`pulumi install`](/docs/iac/cli/commands/pulumi_install/) to install all dependencies, including local SDKs defined in `Pulumi.yaml`

## Configure Terraform providers

A Terraform module runs against your project's default provider configuration — the same configuration your Pulumi-native resources use — so it inherits whatever region, account, or credentials you've already set. To target a specific region, for example, set it the way you would for any Pulumi provider:

```bash
$ pulumi config set aws:region us-west-2
```

You can also supply provider settings, including short-lived credentials, through a [Pulumi ESC environment](/docs/esc/). See [Providers](/docs/iac/concepts/providers/) for the full range of configuration options.

## Troubleshooting

### Fix invalid relative paths

When a module accepts a file path, pass an absolute path instead of a relative one. For example, the [AWS Lambda module](https://registry.terraform.io/modules/terraform-aws-modules/lambda/aws) accepts a `source_path` that points to your function's code:

```typescript
import * as hcl from "@pulumi/hcl";

const lambdaModule = new hcl.Module("my-lambda", {
    source: "terraform-aws-modules/lambda/aws",
    inputs: {
        function_name: "my-function",
        handler: "index.handler",
        runtime: "nodejs20.x",
        source_path: `${process.cwd()}/src`,
    },
});
```

This is necessary because Terraform modules run from a different working directory than your Pulumi program, so a relative path would resolve incorrectly. The example above uses the Node.js built-in `process.cwd()` to anchor the path to the function code in `src` to your project's working directory.

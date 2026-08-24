---
title_tag: "Variables & Values | Language Essentials"
meta_desc: Learn how variables, types, and string interpolation work in Pulumi programs, translated from Pulumi YAML and Terraform HCL.
title: Variables
h1: Variables and Values
menu:
    iac:
        name: Variables & Values
        parent: iac-guides-language-essentials
        weight: 10
aliases:
    - /docs/iac/guides/language-essentials/variables/
---

A variable gives a name to a value so you can reuse it and refer to it later.
Every configuration language you already use has a version of this: a `locals`
block in HCL, a `variables:` section in Pulumi YAML. In a general-purpose
language, naming a value is the most basic thing you do, and it works the same
way whether the value is a string, a number, or the result of creating a
resource.

## Where you have seen this before

In Pulumi YAML, `variables` names a value once so you can reference it
elsewhere in the same file:

```yaml
variables:
  bucketName: my-app-data
resources:
  bucket:
    type: aws:s3:Bucket
    properties:
      bucket: ${bucketName}
```

In Terraform HCL, a `locals` block does the same thing, and `${...}`
interpolation substitutes it into a string:

```hcl
locals {
  bucket_name = "my-app-data"
}

resource "aws_s3_bucket" "bucket" {
  bucket = "${local.bucket_name}"
}
```

## The syntax

In a general-purpose language, you declare a variable and assign it a value in
one statement. Most Pulumi languages infer the type from the value, so you
rarely write the type out yourself.

{{< chooser language "typescript,python,go,csharp,java,yaml,hcl" >}}

{{% choosable language typescript %}}

```typescript
const bucketName = "my-app-data";
const replicaCount = 3;
```

{{% /choosable %}}
{{% choosable language python %}}

```python
bucket_name = "my-app-data"
replica_count = 3
```

{{% /choosable %}}
{{% choosable language go %}}

```go
bucketName := "my-app-data"
replicaCount := 3
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var bucketName = "my-app-data";
var replicaCount = 3;
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var bucketName = "my-app-data";
var replicaCount = 3;
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
variables:
  bucketName: my-app-data
  replicaCount: 3
```

{{% /choosable %}}
{{% choosable language hcl %}}

```hcl
locals {
  bucket_name   = "my-app-data"
  replica_count = 3
}
```

{{% /choosable %}}

{{< /chooser >}}

Building a string out of a variable works the way you'd expect from `${...}`
interpolation, just with each language's own syntax: template literals in
TypeScript, f-strings in Python, `fmt.Sprintf` in Go, `$"..."` in C#, and
`String.format` in Java.

{{< chooser language "typescript,python,go,csharp,java,yaml,hcl" >}}

{{% choosable language typescript %}}

```typescript
const label = `${bucketName}-${replicaCount}`;
```

{{% /choosable %}}
{{% choosable language python %}}

```python
label = f"{bucket_name}-{replica_count}"
```

{{% /choosable %}}
{{% choosable language go %}}

```go
label := fmt.Sprintf("%s-%d", bucketName, replicaCount)
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var label = $"{bucketName}-{replicaCount}";
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var label = String.format("%s-%d", bucketName, replicaCount);
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
variables:
  label: ${bucketName}-${replicaCount}
```

{{% /choosable %}}
{{% choosable language hcl %}}

```hcl
locals {
  label = "${local.bucket_name}-${local.replica_count}"
}
```

{{% /choosable %}}

{{< /chooser >}}

## In a Pulumi program

Stack configuration is the language equivalent of a `Pulumi.<stack>.yaml`
value you'd otherwise reference directly. You read it into a variable with
`pulumi.Config` and use it the same way you'd use any other variable. Set the
value first, since `config.require` fails if it isn't set:

```bash
pulumi config set environment production
```

{{< chooser language "typescript,python,go,csharp,java,yaml,hcl" >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const config = new pulumi.Config();
const environment = config.require("environment");

const bucket = new aws.s3.Bucket(`data-${environment}`);
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
import pulumi_aws as aws

config = pulumi.Config()
environment = config.require("environment")

bucket = aws.s3.Bucket(f"data-{environment}")
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
	"fmt"

	"github.com/pulumi/pulumi-aws/sdk/v7/go/aws/s3"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		cfg := config.New(ctx, "")
		environment := cfg.Require("environment")

		_, err := s3.NewBucket(ctx, fmt.Sprintf("data-%s", environment), nil)
		return err
	})
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using Pulumi;
using Pulumi.Aws.S3;

return await Deployment.RunAsync(() =>
{
    var config = new Config();
    var environment = config.Require("environment");

    var bucket = new Bucket($"data-{environment}");
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
import com.pulumi.Pulumi;
import com.pulumi.Config;
import com.pulumi.aws.s3.Bucket;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            var config = ctx.config();
            var environment = config.require("environment");

            var bucket = new Bucket("data-" + environment);
        });
    }
}
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
config:
  environment:
    type: string
resources:
  bucket:
    type: aws:s3:Bucket
    properties:
      bucket: data-${environment}
```

{{% /choosable %}}
{{% choosable language hcl %}}

```hcl
variable "environment" {
  type = string
}

resource "aws_s3_bucket" "bucket" {
  bucket = "data-${var.environment}"
}
```

{{% /choosable %}}

{{< /chooser >}}

## What to watch out for

Not every value on a resource is a plain string or number you can interpolate
directly. Many resource properties are outputs: values Pulumi doesn't know
until the resource is actually created, such as a generated ARN or a load
balancer's DNS name. Ordinary string interpolation doesn't work on an output,
because the value isn't available when your program runs. See
[inputs and outputs](/docs/iac/concepts/inputs-outputs/) for how that model
works, and each language's interpolation helper, such as `pulumi.interpolate`
in TypeScript or `pulumi.Output.format()` in Python, for building strings out
of them.

## Frequently asked questions

### What replaces Terraform locals and variables in Pulumi?

An ordinary variable in your programming language plays the role Terraform's `locals` and `variable` blocks play. Per-stack inputs that used to live in a `variable` block instead come from [stack configuration](/docs/iac/concepts/config/), which you read at the top of your program and assign to a regular variable.

### Why doesn't string interpolation work on a resource output?

Because an output value isn't known while your program runs; it only resolves once the resource is created or updated. Standard string interpolation needs a value in hand immediately, so each language SDK provides an [output](/docs/iac/concepts/inputs-outputs/)-aware helper instead: `pulumi.interpolate` in TypeScript, `Output.format()` in Python and Java, `pulumi.Sprintf()` in Go, and `Output.Format()` in C#.

### Do I have to declare a type for every variable?

No. Type inference handles most cases, so you can assign a value and let the compiler work out its type. Declaring a type explicitly still pays off for public function signatures and component inputs, where it gives you IDE completion and catches mismatches at compile time rather than at deployment time.

## Next steps

Continue to [conditionals](/docs/iac/guides/basics/language-essentials/conditionals/)
to see how `if` statements replace `count`-based conditionals.

## Learn more

- [Configuration](/docs/iac/concepts/config/) for the full set of options for
  reading and validating stack configuration.

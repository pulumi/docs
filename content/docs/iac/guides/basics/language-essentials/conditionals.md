---
title_tag: "Conditionals | Language Essentials"
meta_desc: Learn how if statements and conditional expressions replace count-based conditionals in Pulumi programs written in a general-purpose language.
title: Conditionals
h1: Conditionals
menu:
    iac:
        name: Conditionals
        parent: iac-guides-language-essentials
        weight: 20
aliases:
    - /docs/iac/guides/language-essentials/conditionals/
---

A conditional decides whether to do something, or which of two things to do,
based on a value you already know. You use this constantly in HCL, usually
without calling it a conditional: the `count = var.enabled ? 1 : 0` idiom is a
conditional wearing a resource-repetition costume. A general-purpose language
gives you the `if` statement directly, so you don't have to route the decision
through a resource count.

## Where you have seen this before

Pulumi YAML has no native conditional, so YAML programs work around the
absence with `fn::select` or by omitting a resource entirely from the file for
a given stack. Terraform HCL's idiom is the conditional `count`:

```hcl
resource "aws_s3_bucket" "backups" {
  count  = var.environment == "production" ? 1 : 0
  bucket = "app-backups"
}
```

Everything downstream that used to reference `aws_s3_bucket.backups` now has to
account for it being a list of zero or one items. That's the tell that HCL is
simulating a conditional with a loop, because it doesn't have a real one.

## The syntax

A general-purpose language has `if`/`else` directly, plus a conditional
(ternary) expression for picking between two values. Go doesn't have a ternary
operator, so an `if` is the idiom there for both cases.

{{< chooser language "typescript,python,go,csharp,java,yaml,hcl" >}}

{{% choosable language typescript %}}

```typescript
const instanceSize = environment === "production" ? "m5.large" : "t3.micro";

if (environment === "production") {
  // ...
}
```

{{% /choosable %}}
{{% choosable language python %}}

```python
instance_size = "m5.large" if environment == "production" else "t3.micro"

if environment == "production":
    ...
```

{{% /choosable %}}
{{% choosable language go %}}

```go
instanceSize := "t3.micro"
if environment == "production" {
	instanceSize = "m5.large"
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var instanceSize = environment == "production" ? "m5.large" : "t3.micro";

if (environment == "production")
{
    // ...
}
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var instanceSize = environment.equals("production") ? "m5.large" : "t3.micro";

if (environment.equals("production")) {
    // ...
}
```

{{% /choosable %}}
{{% choosable language yaml %}}

Pulumi YAML has no `if` or ternary expression. `fn::select` picks a value out
of a list by a 0-based integer index, which stands in for a two-way choice
when that index itself comes from config:

```yaml
config:
  isProduction:
    type: integer
variables:
  instanceSize:
    fn::select:
      - ${isProduction}
      - - t3.micro
        - m5.large
```

There's no way to skip creating a resource entirely from YAML; that requires a
general-purpose language or a component.

{{% /choosable %}}
{{% choosable language hcl %}}

HCL has a ternary expression but no `if` statement, so both branching on a
value and deciding whether to create a resource at all go through the
conditional expression, the second one via `count`:

```hcl
locals {
  instance_size = var.environment == "production" ? "m5.large" : "t3.micro"
}

resource "aws_s3_bucket" "backups" {
  count  = var.environment == "production" ? 1 : 0
  bucket = "app-backups"
}
```

{{% /choosable %}}

{{< /chooser >}}

## In a Pulumi program

Deciding whether to create a resource at all, such as a backup bucket that
only exists in production, is a plain `if` around the resource declaration.
`pulumi.getStack()` returns the current stack name, which is the language
equivalent of the stack-scoped variables you'd otherwise branch on in HCL:

{{< chooser language "typescript,python,go,csharp,java,yaml,hcl" >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

if (pulumi.getStack() === "production") {
  new aws.s3.Bucket("app-backups");
}
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
import pulumi_aws as aws

if pulumi.get_stack() == "production":
    aws.s3.Bucket("app-backups")
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
		if ctx.Stack() == "production" {
			if _, err := s3.NewBucket(ctx, "app-backups", nil); err != nil {
				return err
			}
		}
		return nil
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
    if (Deployment.Instance.StackName == "production")
    {
        var backups = new Bucket("app-backups");
    }
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
import com.pulumi.Pulumi;
import com.pulumi.aws.s3.Bucket;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            if (ctx.stackName().equals("production")) {
                var backups = new Bucket("app-backups");
            }
        });
    }
}
```

{{% /choosable %}}
{{% choosable language yaml %}}

Pulumi YAML has no way to skip declaring a resource based on a condition; every
resource in the file is always created. Reaching for a general-purpose
language, or a component someone already wrote in one, is the way to make
resource creation itself conditional.

{{% /choosable %}}
{{% choosable language hcl %}}

```hcl
resource "aws_s3_bucket" "backups" {
  count  = terraform.workspace == "production" ? 1 : 0
  bucket = "app-backups"
}
```

{{% /choosable %}}

{{< /chooser >}}

## What to watch out for

You can't branch an `if` statement on a resource output. An output's value
isn't known while your program is running, so a comparison like
`if (bucket.arn === "...")` doesn't do what it looks like it does. Branch on
values you actually know when the program runs: stack names, configuration,
and plain inputs. If a decision genuinely depends on a value that only exists
after a resource is created, that decision has to happen inside `apply`, not
in an `if` statement; see
[working with outputs](/docs/iac/concepts/inputs-outputs/apply/) for how that
works.

## Next steps

Continue to [loops and iteration](/docs/iac/guides/basics/language-essentials/loops/)
to see how a `for` loop replaces `count` and `for_each` for creating multiple
resources.

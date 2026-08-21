---
title_tag: "Functions | Language Essentials"
meta_desc: Learn how functions let you reuse and parameterize resource declarations in Pulumi programs, and when to reach for one.
title: Functions
h1: Functions
menu:
    iac:
        name: Functions
        parent: iac-guides-language-essentials
        weight: 40
aliases:
    - /docs/iac/guides/language-essentials/functions/
---

A function packages a piece of logic so you can call it with different inputs
instead of repeating the logic each time. This is the same job a Terraform
module does at a coarser grain: you parameterize a group of resources once,
then reuse it. In a general-purpose language, a function is the smallest unit
of that reuse, and it works the same whether it computes a plain value or
creates cloud resources.

## Where you have seen this before

A Terraform module is a coarser version of the same idea: you declare inputs
once, and every place that calls the module gets its own copy of the
resources inside it with those inputs applied.

```hcl
module "logging_bucket" {
  source = "./modules/logging-bucket"
  name   = "app-logs"
}

module "audit_logging_bucket" {
  source = "./modules/logging-bucket"
  name   = "audit-logs"
}
```

A function is the same reuse mechanism at a smaller grain: no separate
directory or source block, just a callable name in the same file.

## The syntax

A function takes parameters, does something with them, and optionally returns
a value.

{{< chooser language "typescript,python,go,csharp,java,yaml,hcl" >}}

{{% choosable language typescript %}}

```typescript
function taggedName(prefix: string, environment: string): string {
  return `${prefix}-${environment}`;
}

const name = taggedName("app", "production");
```

{{% /choosable %}}
{{% choosable language python %}}

```python
def tagged_name(prefix: str, environment: str) -> str:
    return f"{prefix}-{environment}"

name = tagged_name("app", "production")
```

{{% /choosable %}}
{{% choosable language go %}}

```go
func taggedName(prefix, environment string) string {
	return fmt.Sprintf("%s-%s", prefix, environment)
}

name := taggedName("app", "production")
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
string TaggedName(string prefix, string environment) => $"{prefix}-{environment}";

var name = TaggedName("app", "production");
```

{{% /choosable %}}
{{% choosable language java %}}

```java
static String taggedName(String prefix, String environment) {
    return prefix + "-" + environment;
}

var name = taggedName("app", "production");
```

{{% /choosable %}}
{{% choosable language yaml %}}

Pulumi YAML has no way to define your own function. Its built-in functions,
such as `fn::join` and `fn::toJSON`, cover common value transformations, but
you can't add to that set from within a YAML program.

{{% /choosable %}}
{{% choosable language hcl %}}

Terraform HCL doesn't support user-defined functions either; it ships a fixed
set of built-in functions instead. A module is the closest equivalent to
reuse, shown above, but it reuses a group of resources, not a single
computed value.

{{% /choosable %}}

{{< /chooser >}}

## In a Pulumi program

The same pattern applies when a function's job is to create resources rather
than compute a string. A function that creates a bucket with a standard set of
properties lets every call site stay short, and it keeps the tagging or
naming convention in one place:

{{< chooser language "typescript,python,go,csharp,java,yaml,hcl" >}}

{{% choosable language typescript %}}

```typescript
import * as aws from "@pulumi/aws";

function createLoggingBucket(name: string): aws.s3.Bucket {
  return new aws.s3.Bucket(name, {
    lifecycleRules: [{ enabled: true, expiration: { days: 90 } }],
  });
}

const appLogs = createLoggingBucket("app-logs");
const auditLogs = createLoggingBucket("audit-logs");
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_aws as aws

def create_logging_bucket(name: str) -> aws.s3.Bucket:
    return aws.s3.Bucket(
        name,
        lifecycle_rules=[aws.s3.BucketLifecycleRuleArgs(
            enabled=True,
            expiration=aws.s3.BucketLifecycleRuleExpirationArgs(days=90),
        )],
    )

app_logs = create_logging_bucket("app-logs")
audit_logs = create_logging_bucket("audit-logs")
```

{{% /choosable %}}
{{% choosable language go %}}

```go
func createLoggingBucket(ctx *pulumi.Context, name string) (*s3.Bucket, error) {
	return s3.NewBucket(ctx, name, &s3.BucketArgs{
		LifecycleRules: s3.BucketLifecycleRuleArray{
			&s3.BucketLifecycleRuleArgs{
				Enabled: pulumi.Bool(true),
				Expiration: &s3.BucketLifecycleRuleExpirationArgs{
					Days: pulumi.Int(90),
				},
			},
		},
	})
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using Pulumi.Aws.S3;
using Pulumi.Aws.S3.Inputs;

Bucket CreateLoggingBucket(string name) => new Bucket(name, new BucketArgs
{
    LifecycleRules = new[]
    {
        new BucketLifecycleRuleArgs
        {
            Enabled = true,
            Expiration = new BucketLifecycleRuleExpirationArgs { Days = 90 },
        },
    },
});

var appLogs = CreateLoggingBucket("app-logs");
var auditLogs = CreateLoggingBucket("audit-logs");
```

{{% /choosable %}}
{{% choosable language java %}}

```java
import com.pulumi.aws.s3.Bucket;
import com.pulumi.aws.s3.BucketArgs;
import com.pulumi.aws.s3.inputs.BucketLifecycleRuleArgs;
import com.pulumi.aws.s3.inputs.BucketLifecycleRuleExpirationArgs;

static Bucket createLoggingBucket(String name) {
    return new Bucket(name, BucketArgs.builder()
        .lifecycleRules(BucketLifecycleRuleArgs.builder()
            .enabled(true)
            .expiration(BucketLifecycleRuleExpirationArgs.builder().days(90).build())
            .build())
        .build());
}

var appLogs = createLoggingBucket("app-logs");
var auditLogs = createLoggingBucket("audit-logs");
```

{{% /choosable %}}
{{% choosable language yaml %}}

Pulumi YAML has to declare each bucket as its own resource; there's no way to
factor the shared properties into something callable from within the file:

```yaml
resources:
  appLogs:
    type: aws:s3:Bucket
    properties:
      lifecycleRules:
        - enabled: true
          expiration:
            days: 90
  auditLogs:
    type: aws:s3:Bucket
    properties:
      lifecycleRules:
        - enabled: true
          expiration:
            days: 90
```

{{% /choosable %}}
{{% choosable language hcl %}}

```hcl
module "logging_bucket" {
  source = "./modules/logging-bucket"
  name   = "app-logs"
}

module "audit_logging_bucket" {
  source = "./modules/logging-bucket"
  name   = "audit-logs"
}
```

{{% /choosable %}}

{{< /chooser >}}

## What to watch out for

Calling the same function twice creates two separate resources, so the name
you pass in has to be unique each time, the same requirement covered in
[loops](/docs/iac/guides/basics/language-essentials/loops/). A function is the right
tool as long as the group of resources it creates doesn't need its own
identity in Pulumi's state: no combined outputs, no shared configuration,
nothing another part of the program needs to reference as a unit. Once it
does, that's the signal to move to a class-based
[component](/docs/iac/guides/basics/language-essentials/classes/)
instead.

## Next steps

Continue to
[classes and components](/docs/iac/guides/basics/language-essentials/classes/)
to see how grouping resources into a class gives them a shared identity.

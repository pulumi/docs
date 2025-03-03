---
title: "Introducing Customizable Resource Auto-naming in Pulumi"
date: 2025-01-16
updated: 2025-03-03
meta_desc: "Discover how to customize Pulumi's resource naming to align with your organization's standards and naming conventions."
meta_image: meta.png
authors:
    - mikhail-shilkov
tags:
    - features
    - releases
social:
    twitter: |
        🎉 New in Pulumi: Flexible Resource Auto-naming!
        
        Finally, full control over your cloud resource names:
        ✨ Custom naming patterns
        🎯 Verbatim mode
        🔧 Flexible configuration

        No more compromises between naming standards and uniqueness.

        Read more ⬇️
    linkedin: >
        🚀 We're excited to announce Flexible Resource Auto-naming in Pulumi! 
        
        This highly anticipated feature gives you complete control over how your cloud resources are named across all cloud providers. Whether you want to enforce enterprise naming standards, ensure compliance, or maintain consistent naming patterns - we've got you covered.
        
        Key capabilities:
        - Custom naming patterns with static text, resource information, and random components
        - Verbatim mode for exact logical name matching
        - Option to disable auto-naming entirely
        - Support across all cloud providers
        
        Ready to try it out? Check out our latest blog post to learn more about this game-changing feature for infrastructure management.
---

I'm thrilled to announce that you can now customize how Pulumi names your cloud resources! Our default auto-naming feature has helped thousands of customers successfully manage cloud resources at scale by automatically ensuring unique, conflict-free resource names across their cloud deployments. This robust naming system has been particularly valuable for teams managing multiple environments, handling zero-downtime deployments, and maintaining clear resource organization. Today, we're taking it to the next level by giving you control over how these names are generated.

<!--more-->

Over the years, we've heard from many teams using Pulumi that while they love the power and convenience of our auto-naming system, they need it to work with their organization's naming standards - whether that's adding cost center identifiers, following compliance rules, or matching existing naming patterns. The [GitHub issue tracking this feature](https://github.com/pulumi/pulumi/issues/1518) has gathered quite some attention (50 thumbs up!) and lots of great input from the community.

Today, I'm excited to introduce resource auto-naming configuration. Now you can have the best of both worlds: keep the robustness of Pulumi's auto-naming while making it follow your team's naming conventions. Want your resources to include environment tags? Project prefixes? Random suffixes of specific length? Disable auto-naming entirely? It's all possible now, and it works across all major cloud providers.

## The Road to Better Resource Naming

The original [feature request](https://github.com/pulumi/pulumi/issues/1518) I opened in June 2018 when I was a Pulumi customer. It has generated extensive discussion, with users sharing various use cases and requirements. Today, I'm happy to finally close that issue with a solution that addresses the community's needs while maintaining Pulumi's robust resource management capabilities.

Check out the full story:

{{< youtube "Y7tedYSZly4?rel=0" >}}

## Introducing Auto-naming Configuration

With the new auto-naming configuration feature, you now have full control over how Pulumi generates resource names. Here are some common scenarios you can achieve:

### Disable Auto-naming

If you want complete control over your resource names, you can disable Pulumi auto-naming entirely:

```yaml
pulumi:autonaming:
  mode: disabled
```

In this mode, Pulumi will require you to provide explicit physical names for all resources.

### Use Logical Names As-Is

For scenarios where you want Pulumi to copy exactly the logical names to become the physical names, you can use the `verbatim` mode:

```yaml
pulumi:autonaming:
  mode: verbatim
```

No random suffixes will be added to the resource names.

Note, when an update requires replacing the resource, Pulumi's default behavior is to create the new resource and then delete the old resource. However, when using verbatim names or patterns without random components, resources that need to be replaced will be deleted before creating the new resource. This can lead to downtime.

### Custom Naming Patterns

Create your own naming patterns that combine static text, resource information, and random elements:

```yaml
pulumi:autonaming:
  pattern: ${project}-${stack}-${name}${alphanum(6)}
```

See the [auto-naming configuration documentation](/docs/concepts/resources/names/#auto-naming-configuration) to see the full list of available expressions.

## See It In Action

Let's look at a practical example. Say you're creating an S3 bucket and a DynamoDB table in your Pulumi program:

{{< chooser language "typescript,python,csharp,go,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
import * as aws from "@pulumi/aws";

// Create an S3 bucket
const bucket = new aws.s3.Bucket("uploads");

// Create a DynamoDB table
const table = new aws.dynamodb.Table("users", {
    hashKey: "id",
    attributes: [{
        name: "id",
        type: "S",
    }],
    billingMode: "PAY_PER_REQUEST",
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi_aws as aws

# Create an S3 bucket
bucket = aws.s3.Bucket("uploads")

# Create a DynamoDB table
table = aws.dynamodb.Table("users",
    hash_key="id",
    attributes=[aws.dynamodb.TableAttributeArgs(
        name="id",
        type="S"
    )],
    billing_mode="PAY_PER_REQUEST"
)
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using Pulumi;
using Pulumi.Aws.S3;
using Pulumi.Aws.DynamoDB;
using Pulumi.Aws.DynamoDB.Inputs;

return await Deployment.RunAsync(() =>
{
    // Create an S3 bucket
    var bucket = new Bucket("uploads");

    // Create a DynamoDB table
    var table = new Table("users", new TableArgs
    {
        HashKey = "id",
        Attributes = new[]
        {
            new TableAttributeArgs
            {
                Name = "id",
                Type = "S"
            }
        },
        BillingMode = "PAY_PER_REQUEST"
    });
});
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
    "github.com/pulumi/pulumi-aws/sdk/v5/go/aws/dynamodb"
    "github.com/pulumi/pulumi-aws/sdk/v5/go/aws/s3"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        // Create an S3 bucket
        bucket, err := s3.NewBucket(ctx, "uploads", nil)
        if err != nil {
            return err
        }

        // Create a DynamoDB table
        table, err := dynamodb.NewTable(ctx, "users", &dynamodb.TableArgs{
            HashKey: pulumi.String("id"),
            Attributes: dynamodb.TableAttributeArray{
                &dynamodb.TableAttributeArgs{
                    Name: pulumi.String("id"),
                    Type: pulumi.String("S"),
                },
            },
            BillingMode: pulumi.String("PAY_PER_REQUEST"),
        })
        if err != nil {
            return err
        }

        return nil
    })
}
```

{{% /choosable %}}

{{% choosable language java %}}

```java
package myproject;

import com.pulumi.Pulumi;
import com.pulumi.aws.s3.Bucket;
import com.pulumi.aws.dynamodb.Table;
import com.pulumi.aws.dynamodb.TableArgs;
import com.pulumi.aws.dynamodb.inputs.TableAttributeArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            // Create an S3 bucket
            var bucket = new Bucket("uploads");

            // Create a DynamoDB table
            var table = new Table("users", TableArgs.builder()
                .hashKey("id")
                .attributes(TableAttributeArgs.builder()
                    .name("id")
                    .type("S")
                    .build())
                .billingMode("PAY_PER_REQUEST")
                .build());
        });
    }
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
resources:
  # Create an S3 bucket
  uploads:
    type: aws:s3:Bucket

  # Create a DynamoDB table
  users:
    type: aws:dynamodb:Table
    properties:
      hashKey: id
      attributes:
        - name: id
          type: S
      billingMode: PAY_PER_REQUEST
```

{{% /choosable %}}

{{< /chooser >}}

By default, Pulumi would generate names like `uploads-ae26f3b` and `users-4c2dd09`. But let's say you want your resources to follow a pattern that includes your project and stack name. You can configure this in your stack configuration file (`Pulumi.<stack-name>.yaml`):

```yaml
config:
  pulumi:autonaming:
    pattern: ${project}-${stack}-${name}
```

Now when you run `pulumi up`, your resources will be created with predictable names:

- S3 bucket: `myproject-dev-uploads`
- DynamoDB table: `myproject-dev-users`

You can also set different patterns for specific providers or resource types:

```yaml
config:
  pulumi:autonaming:
    pattern: ${project}-${stack}-${name}
    providers:
      aws:
        resources:
          "aws:s3/bucket:Bucket":
            pattern: ${name}-${stack}-${alphanum(6)}
```

With this configuration, you'll get:

- S3 bucket: `uploads-dev-x7yz9n` (with a random suffix for global uniqueness)
- DynamoDB table: `myproject-dev-users` (following the default pattern)

### Configuration Syntax

The configuration syntax differs slightly depending on where you define it:

In your project file `Pulumi.yaml`:

```yaml
config:
  pulumi:autonaming:
    value:
      mode: verbatim
```

In your stack configuration file `Pulumi.<stack-name>.yaml`:

```yaml
config:
  pulumi:autonaming:
    mode: verbatim
```

The same applies to other configuration patterns shown above - use the `value:` key in project-level configuration, but omit it in stack-level configuration.

## Getting Started

To use the auto-naming configuration feature, you'll need:

1. Pulumi CLI 3.146.0 or later
2. The following minimum provider versions (as applicable):
   - AWS provider 6.66.0 or later
   - Azure Native provider 2.78.0 or later
   - Azure Classic provider 6.14.0 or later
   - Google Cloud Platform provider 8.11.0 or later
   - Kubernetes provider 4.20.0 or later
   - AWS Cloud Control provider 1.21.0 or later

Once you have the required versions installed, simply add your desired auto-naming configuration to your Pulumi configuration file.

For complete documentation and advanced usage scenarios, visit our [resource auto-naming documentation](/docs/intro/concepts/resources/names/#auto-naming-configuration).

## General Availability

We're excited to announce that the auto-naming feature is now generally available across our major cloud providers. This release marks an important milestone in Pulumi's evolution, delivering a robust and flexible solution for resource naming.

Thank you to everyone who participated in the [RFC discussion](https://github.com/pulumi/pulumi/discussions/17592) and the preview period and for providing valuable feedback. Your input has been invaluable in creating a solution that works for diverse use cases while maintaining Pulumi's core strengths.

If you have any questions or feedback about the resource auto-naming feature, please don't hesitate to reach out to us on GitHub or in the [Pulumi Community Slack](https://slack.pulumi.com).

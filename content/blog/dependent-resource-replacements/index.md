---
title: "New in Pulumi IaC: `replaceWith` Resource Option"
date: 2025-12-02
meta_desc: "You can now use the `replaceWith` resource option to inform Pulumi of extra dependencies"
meta_image: meta.png
authors:
    - tom-harding
tags:
    - features
    - iac
    - releases

social:
    twitter: "New in Pulumi IaC: Use the `replaceWith` resource option to declare custom resource dependencies and ensure coordinated replacements across your infrastructure."
    linkedin: "Pulumi introduces a powerful new feature for fine-grained infrastructure control: the `replaceWith` resource option. Now you can explicitly define dependencies between resources to ensure coordinated replacements—perfect for scenarios like restarting services when databases are updated or managing complex multi-resource dependencies."
---

The magic of Pulumi is that we rarely have to worry about the fine details of *how* our deployment and infrastructure management works, allowing us to focus instead on *what* we want. If our program declares an S3 bucket, Pulumi handles creation, updates, and deletion automatically.

Most of the time, this is exactly what we want. However, some use cases require finer-grained control over resource dependencies. Today, we're introducing the `replaceWith` resource option, a new feature that gives you explicit control over replacement dependencies between resources.

<!--more-->

## Custom resource dependencies

When replacing a resource, the Pulumi engine walks the dependency graph to determine what else needs replacement. However, the answer isn't always obvious:

* Some dependencies aren't obvious at the infrastructure level. For example, restarting a database server may require restarting its consumers to reconnect.

* Provider-specific challenges exist. You might not be able to update a subnet's properties while resources are using it, even without an observable dependency. Any subnet change must be accompanied by changes to all its consumers to avoid errors.

* Application-level dependencies may exist beyond infrastructure. If two services maintain open connections in the application layer, replacing one should trigger replacement of the other.

## Declaring our own dependencies

The `replaceWith` resource option makes these dependencies explicit in your code. Similar to `deletedWith`, passing references to other resources via `replaceWith` defines a relationship: when any target resource is replaced, the source is also replaced. This has some interesting implications:

* We can define a number of resources that all `replaceWith` each other, and so any change to any member of the group will trigger an update to all the others.

* Relationships are transitive: organizing resources hierarchically where children `replaceWith` their parents means any ancestor change triggers replacement of all descendants.

## In code

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const database = new aws.rds.Instance("app-db", { /* ... */ });

// The database location is provided to this instance
// by other means, so there is not an explicit dependency
// linking the two.
const app = new aws.ec2.Instance("app-service", { /* ... */ }, {
    // Here, we explicitly tie the two together: if the
    // database is upgraded, for example, we will need to
    // restart the application instance to ensure that
    // a connection is re-established.
    replaceWith: [database],
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
import pulumi_aws as aws

database = aws.rds.Instance('app-db', {})

# The database location is provided to this instance
# by other means, so there is not an explicit dependency
# linking the two.
application = aws.ec2.Instance('app-service', {},
    # Here, we explicitly tie the two together: if the
    # database is upgraded, for example, we will need to
    # restart the application instance to ensure that
    # a connection is re-established.
    opts=pulumi.ResourceOptions(replace_with=[database])
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
import (
    "github.com/pulumi/pulumi-aws/sdk/v6/go/aws/ec2"
    "github.com/pulumi/pulumi-aws/sdk/v6/go/aws/rds"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

database, err := rds.NewInstance(ctx, "app-db", &rds.InstanceArgs{ ... })
if err != nil {
    return err
}

// The database location is provided to this instance
// by other means, so there is not an explicit dependency
// linking the two.
application, err := ec2.NewInstance(ctx, "app-service", &ec2.InstanceArgs{ ... },
    // Here, we explicitly tie the two together; if the
    // database is upgraded, for example, we will need to
    // restart the application instance to ensure that
    // a connection is re-established.
    pulumi.ReplaceWith([]pulumi.Resource{database}))
if err != nil {
    return err
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using Pulumi;
using Aws = Pulumi.Aws;

var database = new Aws.Rds.Instance("app-db", new() { ... });

// The database location is provided to this instance
// by other means, so there is not an explicit dependency
// linking the two.
var application = new Aws.Ec2.Instance("app-service", new() { ... }, new CustomResourceOptions
{
    // Here, we explicitly tie the two together; if the
    // database is upgraded, for example, we will need to
    // restart the application instance to ensure that
    // a connection is re-established.
    ReplaceWith = new[]
    {
        database,
    },
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
import com.pulumi.aws.ec2.Instance;
import com.pulumi.aws.ec2.InstanceArgs;
import com.pulumi.resources.CustomResourceOptions;

var database = new com.pulumi.aws.rds.Instance("app-db",
    com.pulumi.aws.rds.InstanceArgs.builder()
        .build());

// The database location is provided to this instance
// by other means, so there is not an explicit dependency
// linking the two.
var application = new Instance("app-service",
    InstanceArgs.builder()
        .build(),
    // Here, we explicitly tie the two together; if the
    // database is upgraded, for example, we will need to
    // restart the application instance to ensure that
    // a connection is re-established.
    CustomResourceOptions.builder()
        .replaceWith(database)
        .build());
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  database:
    type: aws:rds:Instance
    properties:
      # ...
  # The database location is provided to this instance
  # by other means, so there is not an explicit dependency
  # linking the two.
  application:
    type: aws:ec2:Instance
    properties:
      # ...
    options:
      # Here, we explicitly tie the two together: if the
      # database is upgraded, for example, we will need to
      # restart the application instance to ensure that
      # a connection is re-established.
      replaceWith:
        - ${database}
```

{{% /choosable %}}

{{< /chooser >}}

Of course, this is a simple example, but hopefully it illustrates the point: we now have a way to make implicit dependencies between resources more explicit within our programs, and provide hints to Pulumi as to which services depend on others.

## Next steps

This feature is supported as of [Pulumi `v3.207.0`](https://github.com/pulumi/pulumi/releases/tag/v3.207.0), and is now available within the Go, Python, NodeJS, and Java SDKs, with C# and YAML coming soon. Thanks for reading, and feel free to reach out with any questions via [GitHub](https://github.com/pulumi/pulumi), [X](https://x.com/pulumicorp), or our [Community Slack](https://slack.pulumi.com/).

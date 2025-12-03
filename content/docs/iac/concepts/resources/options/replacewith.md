---
title_tag: "replacewith | Resource Options"
meta_desc: The replacewith resource option allows for explicit replace dependencies to be declared between resources.
title: "replacewith"
h1: "Resource option: replaceWith"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  iac:
    identifier: replaceWith
    parent: options-concepts
    weight: 5
aliases:
  - /docs/intro/concepts/resources/options/replacewith/
  - /docs/concepts/options/replacewith/
  - /docs/iac/concepts/options/replacewith/
---

The `replaceWith` resource option allows you to force a replace operation on the current resource every time one of the given resources is replaced.

However, not all relationships are visible to Pulumi: perhaps there are differences in behavior between providers, or your application introduces its own specific relationships, such as two services that depend on one another and thus must always be replaced together.

In these cases, you can use `replaceWith` to make these relationships explicit to the Pulumi engine. In the following example, an explicit dependency is declared: whenever the database is replaced, we must also replace the server.

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const database = new aws.rds.Instance('app-db', { /* ... */ });
const application = new aws.ec2.Instance('app-service', { /* ... */ }, {
  replaceWith: [database]
})
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
import pulumi_aws as aws

database = aws.rds.Instance('app-db', {})
application = aws.ec2.Instance('app-service', {},
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

application, err := ec2.NewInstance(ctx, "app-service", &ec2.InstanceArgs{ ... },
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
var application = new Aws.Ec2.Instance("app-service", new() { ... }, new CustomResourceOptions
{
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

var application = new Instance("app-service",
    InstanceArgs.builder()
        .build(),
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
  application:
    type: aws:ec2:Instance
    properties:
      # ...
    options:
      replaceWith:
        - ${database}
```

{{% /choosable %}}

{{< /chooser >}}
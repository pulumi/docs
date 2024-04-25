---
title_tag: "Get Functions"
meta_desc: Each Pulumi resource has a `get` function to get a reference to an existing instance of the resource. Learn more about these `get` functions in this guide.
title: Get functions
h1: Get functions
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  concepts:
    parent: resources
    weight: 7
aliases:
- /docs/intro/concepts/resources/get/
---

You can use the static `get` function, which is available on all resource types, to look up an existing resource that is not managed by Pulumi. The `get` function is different from the [`import` CLI command](/docs/cli/commands/pulumi_import): `pulumi import` is used to bring an existing resource under management by Pulumi. `get` is used to allow the attributes of an existing resource to be used within a Pulumi program. A resource read with the `get` function will never be updated or deleted by Pulumi during an update.

Two values are passed to the `get` function:

1. The **logical name** Pulumi will use to refer to the resource.
1. The **physical ID** that the resource has in the target cloud.

You can use the `get` function to consume properties from a resource that was provisioned elsewhere. For example, this program reads an existing EC2 Security Group whose ID is `sg-0dfd33cdac25b1ec9` and uses the result as input to create an EC2 Instance that Pulumi will manage:

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

```javascript
let aws = require("@pulumi/aws");

let group = aws.ec2.SecurityGroup.get("group", "sg-0dfd33cdac25b1ec9");

let server = new aws.ec2.Instance("web-server", {
    ami: "ami-6869aa05",
    instanceType: "t2.micro",
    securityGroups: [ group.name ], // reference the security group resource above
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as aws from "@pulumi/aws";

let group = aws.ec2.SecurityGroup.get("group", "sg-0dfd33cdac25b1ec9");

let server = new aws.ec2.Instance("web-server", {
    ami: "ami-6869aa05",
    instanceType: "t2.micro",
    securityGroups: [ group.name ], // reference the security group resource above
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_aws as aws

group = aws.ec2.SecurityGroup.get('group', 'sg-0dfd33cdac25b1ec9')

server = aws.ec2.Instance('web-server',
    ami='ami-6869aa05',
    instance_type='t2.micro',
    security_groups=[group.name]) # reference the security group resource above
```

{{% /choosable %}}
{{% choosable language go %}}

```go
import (
    "github.com/pulumi/pulumi-aws/sdk/v4/go/aws/ec2"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        group, err := ec2.GetSecurityGroup(ctx, "group", pulumi.ID("sg-0dfd33cdac25b1ec9"), nil)
        if err != nil {
            return err
        }
        server, err := ec2.NewInstance(ctx, "web-server", &ec2.InstanceArgs{
            Ami:            pulumi.String("ami-6869aa05"),
            InstanceType:   pulumi.String("t2.micro"),
            SecurityGroups: pulumi.StringArray{group.Name},
        })
        if err != nil {
            return err
        }
        return nil
    })
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using Pulumi;
using Pulumi.Aws.Ec2;
using Pulumi.Aws.Ec2.Inputs;

class MyStack : Stack
{
    public MyStack()
    {
        var group = SecurityGroup.Get("group", "sg-0dfd33cdac25b1ec9");

        var server = new Instance("web-server", new InstanceArgs {
            Ami = "ami-6869aa05",
            InstanceType = "t2.micro",
            SecurityGroups = { group.Name }
        });
    }
}
```

{{% /choosable %}}
{{% choosable language java %}}

```java
public static void stack(Context ctx) {
    var group = SecurityGroup.get("group", Output.of("sg-0dfd33cdac25b1ec9"), null, null);

    var server = new Instance("web-server", InstanceArgs.builder()
        .ami("ami-6869aa05")
        .instanceType("t2.micro")
        .securityGroups(
            group.name().applyValue(v -> List.of(v)))
        .build());
}
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  group:
    type: aws:ec2:SecurityGroup
    get:
      id: sg-0dfd33cdac25b1ec9
  web-server:
    type: aws:ec2:Instance
    properties:
      ami: ami-6869aa05
      instanceType: t2.micro
      securityGroups:
        - ${group.name}
```

{{% /choosable %}}

{{< /chooser >}}

Note that Pulumi will never attempt to modify the security group in this example. It queries the attributes of the security group from your cloud account and then uses its name as an input for the new EC2 Instance.

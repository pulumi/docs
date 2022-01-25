---
title: "Import"
meta_desc: The import resource option brings an existing cloud resource into Pulumi.
menu:
  intro:
    identifier: import
    parent: options
    weight: 7
---

The `import` resource option imports an existing cloud resource so that Pulumi can manage it. Imported resources can have been provisioned by any other method, including manually in the cloud console or with the cloud CLI.

To import a resource, first specify the `import` option with the resource’s ID. This ID is the same as would be returned by the id property for any resource created by Pulumi; the ID is resource-specific. Pulumi reads the current state of the resource with the given ID from the cloud provider. Next, you must specify all required arguments to the resource constructor so that it exactly matches the state to import. By doing this, you end up with a Pulumi program that will accurately generate a matching desired state.

This example imports an existing EC2 security group with ID `sg-04aeda9a214730248` and an EC2 instance with ID `i-06a1073de86f4adef`:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
let aws = require("@pulumi/aws");

let group = new aws.ec2.SecurityGroup("web-sg", {
    name: "web-sg-62a569b",
    ingress: [{ protocol: "tcp", fromPort: 80, toPort: 80, cidrBlocks: ["0.0.0.0/0"] }],
}, { import: "sg-04aeda9a214730248" });

let server = new aws.ec2.Instance("web-server", {
    ami: "ami-6869aa05",
    instanceType: "t2.micro",
    securityGroups: [ group.name ],
}, { import: "i-06a1073de86f4adef" });
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as aws from "@pulumi/aws";

let group = new aws.ec2.SecurityGroup("web-sg", {
    name: "web-sg-62a569b",
    ingress: [{ protocol: "tcp", fromPort: 80, toPort: 80, cidrBlocks: ["0.0.0.0/0"] }],
}, { import: "sg-04aeda9a214730248" });

let server = new aws.ec2.Instance("web-server", {
    ami: "ami-6869aa05",
    instanceType: "t2.micro",
    securityGroups: [ group.name ],
}, { import: "i-06a1073de86f4adef" });
```

{{% /choosable %}}
{{% choosable language python %}}

```python
# IMPORTANT: Python appends an underscore (`import_`) to avoid conflicting with the keyword.

import pulumi_aws as aws

group = aws.ec2.SecurityGroup('web-sg',
    name='web-sg-62a569b',
    description='Enable HTTP access',
    ingress=[
        { 'protocol': 'tcp', 'from_port': 80, 'to_port': 80, 'cidr_blocks': ['0.0.0.0/0'] }
    ],
    opts=ResourceOptions(import_='sg-04aeda9a214730248'))

server = aws.ec2.Instance('web-server',
    ami='ami-6869aa05',
    instance_type='t2.micro',
    security_groups=[group.name],
    opts=ResourceOptions(import_='i-06a1073de86f4adef'))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
group, err := ec2.NewSecurityGroup(ctx, "web-sg",
    &ec2.SecurityGroupArgs{
        Name:        pulumi.String("web-sg-62a569b"),
        Description: pulumi.String("Enable HTTP access"),
        Ingress: ec2.SecurityGroupIngressArray{
            ec2.SecurityGroupIngressArgs{
                Protocol:   pulumi.String("tcp"),
                FromPort:   pulumi.Int(80),
                ToPort:     pulumi.Int(80),
                CidrBlocks: pulumi.StringArray{pulumi.String("0.0.0.0/0")},
            },
        },
    },
    pulumi.Import(pulumi.ID("sg-04aeda9a214730248")),
)
if err != nil {
    return err
}
server, err := ec2.NewInstance(ctx, "web-server",
    &ec2.InstanceArgs{
        Ami:            pulumi.String("ami-6869aa05"),
        InstanceType:   pulumi.String("t2.micro"),
        SecurityGroups: pulumi.StringArray{group.Name},
    },
    pulumi.Import(pulumi.ID("i-06a1073de86f4adef")),
)
if err != nil {
    return err
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var group = new SecurityGroup("web-sg",
    new SecurityGroupArgs {
        Name = "web-sg-62a569b",
        Description = "Enable HTTP access",
        Ingress = {
            new SecurityGroupIngressArgs {
                Protocol = "tcp",
                FromPort = 80,
                ToPort = 80,
                CidrBlocks = { "0.0.0.0/0" }
            }
        }
    },
    new CustomResourceOptions {
        ImportId = "sg-04aeda9a214730248"
    }
);
var server = new Instance("web-server",
    new InstanceArgs {
        Ami = "ami-6869aa05",
        InstanceType = "t2.micro",
        SecurityGroups = { group.Name }
    },
    new CustomResourceOptions {
        ImportId = "i-06a1073de86f4adef"
    }
);
```

{{% /choosable %}}

{{< /chooser >}}

For this to work, your Pulumi stack must be configured correctly. In this example, it’s important that the AWS region is correct.

If the resource’s arguments differ from the imported state, the import will fail. You will receive this message: `warning: inputs to import do not match the existing resource; importing this resource will fail`. Select “details” in the `pulumi up` preview to learn what the differences are. If you try to proceed without correcting the inconsistencies, you will see this message: `error: inputs to import do not match the existing resource`. To fix these errors, make sure that your program computes a state that completely matches the resource to be imported.

Because of auto-naming, it is common to run into this error when you import a resource’s name property. Unless you explicitly specify a name, Pulumi will auto-generate one, which is guaranteed not to match, because it will have a random hex suffix. To fix this problem, explicitly specify the resource’s name [as described here]({{< relref "../#autonaming" >}}). Note that, in the example for the EC2 security group, the name was specified by passing `web-sg-62a569b` as the resource’s name property.

Once a resource is successfully imported, remove the `import` option because Pulumi is now managing the resource.

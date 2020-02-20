---
title: "Importing Infrastructure"
meta_desc: Learn how to import existing cloud infrastructure into Pulumi no matter how it was provisioned.
menu:
  userguides:
    parent: adopting
    weight: 1
---

Most infrastructure projects require working with existing cloud resources, either by building on top of existing resources or adopting existing resources under management with a new and more robust infrastructure provisioning solution.

No matter how you've provisioned these resources &mdash; manually in your cloud provider's console or CLI, using an infrastructure as code tool like Terraform or AWS CloudFormation &mdash; Pulumi enables you to adopt and manage your resources.

<!--more-->

When working with existing resources, there are two primary scenarios:

* You need to reference existing resources to use as inputs to new resources in Pulumi
* You need to adopt existing resources under management so they can be managed by Pulumi

We'll review referencing existing resources and then dive deeper to see how to adopt existing resources to be entirely under the control of Pulumi.

## Referencing Existing Resources

For referencing existing resources, Pulumi offers several options:

* [**Resource getter functions**]({{< relref "/docs/intro/concepts/programming-model#resource-get" >}}) available on every resource let you read all the details for a resource from the cloud provider based just on its ID.

* [**Stack references**]({{< relref "/docs/intro/concepts/organizing-stacks-projects#inter-stack-dependencies" >}}) let you reference outputs of another Pulumi stack for use as inputs to a stack, which is very useful for [organizing projects and stacks]({{< relref "/docs/intro/concepts/organizing-stacks-projects" >}}).

* **State references** let you reference outputs from a non-Pulumi stack for use as inputs to a Pulumi stack, including [Terraform workspaces]({{< relref "terraform" >}}), [AWS CloudFormation stacks]({{< relref "aws" >}}), and [Azure Resource Manager (ARM) deployments]({{< relref "azure" >}}).

Together, these make it easy to reference existing infrastructure regardless of how it was provisioned, without Pulumi taking over control of its ongoing management.

## Adopting Existing Resources

To adopt existing resources so that Pulumi is able to manage subsequent updates to them, Pulumi offers the [`import`]({{< relref "/docs/intro/concepts/programming-model#import" >}}) resource option. This option request that a resource defined in your Pulumi program adopts an existing resource in the cloud provider instead of creating a new one as would normally occur. In keeping with its focus on infrastructure as _code_, Pulumi lets you specify this `import` behavior inside the Pulumi code for your infrastructure deployment, instead of outside of it in a manual workflow.

This example imports an existing AWS EC2 security group with ID `sg-04aeda9a214730248`:

{{< langchoose csharp >}}

```javascript
let aws = require("@pulumi/aws");

let group = new aws.ec2.SecurityGroup("my-sg", {
    name: "my-sg-62a569b",
    ingress: [{ protocol: "tcp", fromPort: 80, toPort: 80, cidrBlocks: ["0.0.0.0/0"] }],
}, { import: "sg-04aeda9a214730248" });
```

```typescript
import * as aws from "@pulumi/aws";

let group = new aws.ec2.SecurityGroup("my-sg", {
    name: "my-sg-62a569b",
    ingress: [{ protocol: "tcp", fromPort: 80, toPort: 80, cidrBlocks: ["0.0.0.0/0"] }],
}, { import: "sg-04aeda9a214730248" });
```

```python
# IMPORTANT: Python appends an underscore (`import_`) to avoid conflicting with the keyword.

import pulumi_aws as aws
from pulumi import ResourceOptions

group = aws.ec2.SecurityGroup('my-sg',
    name='my-sg-62a569b',
    description='Enable HTTP access',
    ingress=[
        { 'protocol': 'tcp', 'from_port': 80, 'to_port': 80, 'cidr_blocks': ['0.0.0.0/0'] }
    ],
    opts=ResourceOptions(import_='sg-04aeda9a214730248'))
```

```go
group, err := ec2.NewSecurityGroup(ctx, "my-sg",
    &ec2.SecurityGroupArgs{
        Name: "my-sg-62a569b",
        Description: "Enable HTTP access",
        Ingress: []map[string]interface{}{
            {
                "protocol":   "tcp",
                "fromPort":   80,
                "toPort":     80,
                "cidrBlocks": []string{"0.0.0.0/0"},
            },
        },
    },
    pulumi.ResourceOpt{Import: "sg-04aeda9a214730248"},
)
if err != nil {
    return err
}
```

```csharp
var group = new SecurityGroup("my-sg",
    new SecurityGroupArgs {
        Name = "my-sg-62a569b",
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
```

> **Note:** Import IDs are resource specific. The ID to use is the same as the ID that gets assigned when Pulumi has provisioned a resource of that type from scratch.

When Pulumi first sees a resource with an `import` option set (in this case `my-sg`), it will adopt the existing resource by querying the target cloud provider for a resource of that type with the given ID, instead of creating a new resource as usual.

To perform the import, run `pulumi up` as usual, and you will see `=` instead of the usual `+`, indicating an import operation:

```
$ pulumi up
Previewing update (dev):

     Type                       Name              Plan
     pulumi:pulumi:Stack        import-dev
 =   └─ aws:ec2:SecurityGroup   my-sg             import

Resources:
    = 1 to import
    1 unchanged
```

If the resource is not found, an error will occur:

```
error: Preview failed: importing sg-04aeda9a214730248: security group not found
```

> Your Pulumi stack must be configured correctly---e.g., in this case, the correct AWS region---otherwise the resource will not be found.

After successfully importing a resource, you can delete the `import` statement, rerun `pulumi up`, and all subsequent operations will behave as though Pulumi provisioned the resource from the outset. Be careful, as this applies to `destroy` operations also.

### Mismatched State

An important part of importing resources is that the resulting Pulumi program, after the import is complete, will faithfully generate the same desired state as your existing infrastructure's actual state. After the import, of course, you may edit your program to generate and apply new desired states to update your infrastructure.

Because of this, all properties need to be fully specified. If you forget to specify a property, or that property's value is incorrect, you'll first receive a warning during preview, and then an error during the actual import update.

For instance, keeping with the example above, let's say we specified the wrong `ingress` rule by choosing port 22 instead of port 80. We'll see a warning:

```
$ pulumi preview
Previewing update (dev):
     Type                      Name        Plan       Info
     pulumi:pulumi:Stack       import-dev
 =   └─ aws:ec2:SecurityGroup  my-sg       import     [diff: ~ingress]; 1 warning

Diagnostics:
  aws:ec2:SecurityGroup (my-sg):
    warning: imported resource sg-04aeda9a214730248's property 'ingress' does not match the existing value;
             importing this resource will fail
```

If we'd like to see details on what specifically did not match, select the `details` option:

```
+ pulumi:pulumi:Stack: (create)
    [urn=urn:pulumi:dev::import::pulumi:pulumi:Stack::import-dev]
    = aws:ec2/securityGroup:SecurityGroup: (import)
        [id=sg-0d188488272df7df8]
        [urn=urn:pulumi:dev::import::aws:ec2/securityGroup:SecurityGroup::my-sg]
        [provider=urn:pulumi:dev::import::pulumi:providers:aws::default_1_22_0::04da6b54-80e4-46f7-96ec-b56ff0331ba9]
      ~ ingress: [
          ~ [0]: {
                  ~ cidrBlocks : [
                      ~ [0]: "0.0.0.0/0" => "0.0.0.0/0"
                    ]
                  - description: ""
                  ~ fromPort   : 80 => 22
                  ~ protocol   : "tcp" => "tcp"
                  ~ self       : false => false
                  ~ toPort     : 80 => 22
                }
        ]
```

Attempting to proceed will fail completely with an error:

```
Diagnostics:
  pulumi:pulumi:Stack (import-dev):
    error: update failed

  aws:ec2:SecurityGroup (my-sg):
    error: imported resource sg-04aeda9a214730248's property 'ingress' does not match the existing value
```

> **Note:** Because of [auto-naming]({{< relref "/docs/intro/concepts/programming-model#autonaming" >}}), it's common to accidentally get in a situation where names don't match. For example, if we left off the security group's name, `"my-sg-62a569b"`, in the earlier example, Pulumi would still auto-name the resource, leading to an error `imported resource sg-04aeda9a214730248's property 'name' does not match the existing value`. To fix this problem, make sure to specify names for all resources explicitly.

### More Complex ID Mappings

Import can be used for a wide variety of adoption scenarios, from importing a single resource to migrating an entire stack from an existing tool like Terraform. You can even automate an entire migration process across dozens of instances of infrastructure deployment.

Because a resource's `import` ID is provided in code, it can be configured in many different ways. Often times mapping from existing infrastructure to the corresponding infrastructure as code definitions can get complicated and so this capability can enable you to specify IDs by looking them up or generating them dynamically. For example, you can:

* Read import IDs from Pulumi config instead of hard-coding them
* Look up import IDs from a JSON or CSV file
* Programmatically construct IDs from predictable names using project and stack names
* Conditionally add the import ID property, enabling you to have some stacks that import, and others that provision new infrastructure
* Use the [`transformations`]({{< relref "/docs/intro/concepts/programming-model#transformations" >}}) capability to inject resource IDs at runtime

For small numbers of resources, you can just paste in individual resource IDs. For larger conversions, you will likely want to automate the mapping of IDs to resources (such as with an external file and using `import: idMapping[name]`). If you are importing or migrating dozens of stacks, you can even select between which of these mappings to use via a Pulumi config setting.

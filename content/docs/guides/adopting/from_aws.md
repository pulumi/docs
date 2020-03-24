---
title: "From AWS CloudFormation"
meta_desc: Migrate your existing AWS CloudFormation JSON/YAML and/or coexist with existing stacks.
menu:
  userguides:
    parent: adopting
    weight: 3
---

<img src="/logos/tech/aws_cloudformation.png" align="right" class="h-32 px-8 pb-4">

If your team has already provisioned infrastructure using AWS CloudFormation, and you'd like to adopt Pulumi, you have three primary strategies you can take:

* [**Coexist**](#referencing-stack-outputs) with resources provisioned by CloudFormation by referencing stack outputs.
* [**Import**]({{< relref "import" >}}) existing resources into Pulumi [in the usual way]({{< relref "import" >}}).
* [**Convert**](#converting-stacks-and-resources) your deployments to use Pulumi and then incrementally migrate resources.

## Referencing Stack Outputs

It is possible to reference existing AWS CloudFormation stacks from your program. It doesn't matter how these stacks were created. This lets you read properties of that CloudFormation stack for use within your Pulumi program. This includes output values computed from resources provisioned that stack.

For instance, let's say your infrastructure team has provisioned your network infrastructure using CloudFormation and you need to use the Subnet ID to provision something new from your Pulumi program. One approach is to hardcode that ID but this is brittle and, if it ever changes, you'd need to go and manually update the hardcoded value.

Instead, you can look up that stack by name and use one of its output values. The following example reads an AWS CloudFormation stack named `my-network-stack` and then uses the exported `SubnetId` value to provision a brand new EC2 instance that runs in that subnet:

{{< langchoose csharp >}}

```javascript
let aws = require("@pulumi/aws");

let network = aws.cloudformation.getStack({
    name: "my-network-stack",
}, { async: true });

let subnetId = network.then(n => n.outputs["SubnetId"]);

let web = new aws.ec2.Instance("web", {
    ami: "ami-0adc0e3ef2558cb1f", // us-west-2 AMI
    instanceType: "t3.micro",
    subnetId: subnetId,
});
```

```typescript
import * as aws from "@pulumi/aws";

const network = aws.cloudformation.getStack({
    name: "my-network-stack",
}, { async: true });

const subnetId = network.then(n => n.outputs["SubnetId"]);

const web = new aws.ec2.Instance("web", {
    ami: "ami-0adc0e3ef2558cb1f", // us-west-2 AMI
    instanceType: "t3.micro",
    subnetId: subnetId,
});
```

```python
import pulumi_aws as aws

network = aws.cloudformation.get_stack(
    name='my-network-stack'
)

subnet_id = network.outputs['SubnetId']

web = aws.ec2.Instance('web',
    ami='ami-0adc0e3ef2558cb1f', # us-west-2 AMI
    instance_type='t2.micro',
    subnet_id=subnet_id
)
```

```go
package main

import (
    "github.com/pulumi/pulumi-aws/sdk/go/aws/cloudformation"
    "github.com/pulumi/pulumi-aws/sdk/go/aws/ec2"
    "github.com/pulumi/pulumi/sdk/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        network, err := cloudformation.LookupStack(ctx, &cloudformation.LookupStackArgs{
            Name: "my-network-stack",
        })
        if err != nil {
            return nil
        }

        subnetID := network.Outputs["SubnetId"].(string)

        web, err := ec2.NewInstance(ctx, "web", &ec2.InstanceArgs{
            Ami:          pulumi.String("ami-0adc0e3ef2558cb1f"), // us-west-2 AMI
            InstanceType: pulumi.String("t2.micro"),
            SubnetId:     pulumi.StringPtr(subnetID),
        })
        if err != nil {
            return err
        }

        ctx.Export("publicIp", web.PublicIp)
        return nil
    })
}
```

```csharp
using System.Collections.Generic;
using System.Threading.Tasks;

using Pulumi;
using CloudFormation = Pulumi.Aws.CloudFormation;
using Ec2 = Pulumi.Aws.Ec2;

class Program
{
    static Task<int> Main()
    {
        return Deployment.RunAsync(async () =>
        {
            var network = await CloudFormation.Invokes.GetStack(new CloudFormation.GetStackArgs
            {
                Name = "my-network-stack",
            });

            var subnetId = (string)network.Outputs["SubnetId"];

            var web = new Ec2.Instance("web", new Ec2.InstanceArgs
            {
                Ami = "ami-0adc0e3ef2558cb1f", // us-west-2 AMI
                InstanceType = "t3.micro",
                SubnetId = subnetId,
            });

            return new Dictionary<string, object?>();
        });
    }
}
```

All we need to do is run `pulumi up` and the Pulumi runtime will know how to query the CloudFormation stack and retrieve its output values. In this case, the CloudFormation stack is treated entirely as read-only, and Pulumi will never attempt to modify it or any resources managed by it.

> Although we've hard-coded the AWS CloudFormation stack name here &mdash; `"my-network-stack"` &mdash; it's common to dynamically compute a name using unique per-stack information, like the stack name, AWS region, or other configuration variables.

## Converting Stacks and Resources

Let's say you want to migrate from AWS CloudFormation to Pulumi and that simply co-existing side-by-side as shown above isn't sufficient. There are two approaches:

1. Deploy your CloudFormation stack using Pulumi.
2. Migrate resources from your CloudFormation stack to Pulumi code.

Depending on what you're trying to accomplish, you may prefer to start with (1) and move to (2) incrementally, or simply jump straight to (2) directly.

### Deploy Stacks Using Pulumi

The Pulumi AWS package [provides a CloudFormation Stack]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/cloudformation#Stack" >}}) resource type. Using this type, you can deploy an existing AWS CloudFormation template written in YAML or JSON.

For instance, this code deploys a simple CloudFormation template using the given parameters, and exports the resulting VPC ID:

{{< langchoose csharp >}}

```javascript
let aws = require("@pulumi/aws");

let template = `{
    "Parameters" : {
        "VPCCidr" : {
            "Type" : "String",
            "Default" : "10.0.0.0/16",
            "Description" : "Enter the CIDR block for the VPC. Default is 10.0.0.0/16."
        }
    },
    "Resources": {
        "myVpc": {
            "Type" : "AWS::EC2::VPC",
            "Properties" : {
                "CidrBlock" : { "Ref" : "VPCCidr" },
                "Tags" : [
                    {"Key": "Name", "Value": "Primary_CF_VPC"}
                ]
            }
        }
    },
    "Outputs": {
        "VpcId": {
            "Value": { "Ref": "myVpc" }
        }
    }
}
`;

let network = new aws.cloudformation.Stack("network", {
    templateBody: template,
    parameters: {
        VPCCidr: "10.0.0.0/16",
    },
});

module.exports = {
    vpcId: network.outputs["VpcId"],
};
```

```typescript
import * as aws from "@pulumi/aws";

const template = `{
    "Parameters" : {
        "VPCCidr" : {
            "Type" : "String",
            "Default" : "10.0.0.0/16",
            "Description" : "Enter the CIDR block for the VPC. Default is 10.0.0.0/16."
        }
    },
    "Resources": {
        "myVpc": {
            "Type" : "AWS::EC2::VPC",
            "Properties" : {
                "CidrBlock" : { "Ref" : "VPCCidr" },
                "Tags" : [
                    {"Key": "Name", "Value": "Primary_CF_VPC"}
                ]
            }
        }
    },
    "Outputs": {
        "VpcId": {
            "Value": { "Ref": "myVpc" }
        }
    }
}
`;

const network = new aws.cloudformation.Stack("network", {
    templateBody: template,
    parameters: {
        VPCCidr: "10.0.0.0/16",
    },
});

export const vpcId = network.outputs["VpcId"];
```

```python
import pulumi
import pulumi_aws as aws

template = """{
    "Parameters" : {
        "VPCCidr" : {
            "Type" : "String",
            "Default" : "10.0.0.0/16",
            "Description" : "Enter the CIDR block for the VPC. Default is 10.0.0.0/16."
        }
    },
    "Resources": {
        "myVpc": {
            "Type" : "AWS::EC2::VPC",
            "Properties" : {
                "CidrBlock" : { "Ref" : "VPCCidr" },
                "Tags" : [
                    {"Key": "Name", "Value": "Primary_CF_VPC"}
                ]
            }
        }
    },
    "Outputs": {
        "VpcId": {
            "Value": { "Ref": "myVpc" }
        }
    }
}
"""

network = aws.cloudformation.Stack('network',
    template_body=template,
    parameters={
        'VPCCidr': '10.0.0.0/16',
    },
)

pulumi.export('vpc_id', network.outputs["VpcId"])
```

```go
package main

import (
    "github.com/pulumi/pulumi-aws/sdk/go/aws/cloudformation"
    "github.com/pulumi/pulumi/sdk/go/pulumi"
)

const (
    template = `{
    "Parameters" : {
        "VPCCidr" : {
            "Type" : "String",
            "Default" : "10.0.0.0/16",
            "Description" : "Enter the CIDR block for the VPC. Default is 10.0.0.0/16."
        }
    },
    "Resources": {
        "myVpc": {
            "Type" : "AWS::EC2::VPC",
            "Properties" : {
                "CidrBlock" : { "Ref" : "VPCCidr" },
                "Tags" : [
                    {"Key": "Name", "Value": "Primary_CF_VPC"}
                ]
            }
        }
    },
    "Outputs": {
        "VpcId": {
            "Value": { "Ref": "myVpc" }
        }
    }
}
`
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        network, err := cloudformation.NewStack(ctx, "network", &cloudformation.StackArgs{
            TemplateBody: pulumi.String(template),
            Parameters: pulumi.Map{
                "VPCCidr": pulumi.String("10.0.0.0/16"),
            },
        })
        if err != nil {
            return err
        }

        ctx.Export("vpcId", network.Outputs.MapIndex(pulumi.String("VpcId")))
        return nil
    })
}
```

```csharp
using System.Collections.Generic;
using System.Threading.Tasks;

using Pulumi;
using CloudFormation = Pulumi.Aws.CloudFormation;

class Program
{
    static Task<int> Main()
    {
        return Deployment.RunAsync(() => {
            var template = @"{
    ""Parameters"" : {
        ""VPCCidr"" : {
            ""Type"" : ""String"",
            ""Default"" : ""10.0.0.0/16"",
            ""Description"" : ""Enter the CIDR block for the VPC. Default is 10.0.0.0/16.""
        }
    },
    ""Resources"": {
        ""myVpc"": {
            ""Type"" : ""AWS::EC2::VPC"",
            ""Properties"" : {
                ""CidrBlock"" : { ""Ref"" : ""VPCCidr"" },
                ""Tags"" : [
                    {""Key"": ""Name"", ""Value"": ""Primary_CF_VPC""}
                ]
            }
        }
    },
    ""Outputs"": {
        ""VpcId"": {
            ""Value"": { ""Ref"": ""myVpc"" }
        }
    }
}";

            var network = new CloudFormation.Stack("network", new CloudFormation.StackArgs
            {
                TemplateBody = template,
                Parameters = new Dictionary<string, object?>
                {
                    { "VPCCidr", "10.0.0.0/16" },
                },
            });

            return new Dictionary<string, object?>
            {
                { "vpcId", network.Outputs.Apply(nw => nw["VpcId"]) },
            };
        });
    }
}
```

> We could have just as well read the template off disk, instead of putting it right in the source code.

After deploying this, Pulumi will see the CloudFormation stack as an opaque single resource. That is, it won't assume control of individual resources inside of the stack. For that, you will need to migrate and/or import individual resources, per the following section:

```bash
$ pulumi up
Updating (dev):
     Type                         Name            Status
 +   pulumi:pulumi:Stack          aws-cfn-dev
 +   └─ aws:cloudformation:Stack  network         created

Outputs:
 + vpcId: "vpc-0e1a74859af1da17f"

Resources:
 + 2 created
```

From here, you can change the template body and/or surrounding code, rerun `pulumi up`, and the right incremental changes will take place.

### Migrate Resources into Code

Now let's see how to actually migrate your CloudFormation resources fully to Pulumi. This requires rewriting the CloudFormation JSON or YAML as real code, either entirely, or one resource at a time. Because you can query stack outputs and provide stack parameters in code, you can more easily intermingle CloudFormation-managed resources alongside Pulumi ones. Cyclic dependencies, of course, cannot be expressed, since the CloudFormation stack is seen as one opaque resource to Pulumi.

> Because Pulumi's AWS resource model doesn't match CloudFormation's resource projections exactly, there is no tool currently available to automate this translation. A good apraoch is to copy the CloudFormation template definition into your code and then rewrite it to your language of choice, translating resource and property names as appropriate.

Note that you can always skip the intermediate step of deploying your CloudFormation stack using Pulumi and go straight to migrating your resources. For large stacks, however, doing this in multiple incremental steps can help minimize disruption and allow you to do this migration more slowly over time.

Our example below will result in a Pulumi program that creates a VPC definition identical to the above CloudFormation stack example. The example will also use [import]({{< relref "import" >}}) in conjunction with CloudFormation's ["retain" deletion policy](https://aws.amazon.com/premiumsupport/knowledge-center/delete-cf-stack-retain-resources/) to adopt resources on-the-fly from CloudFormation to Pulumi rather than recreating them.

Before replacing the CloudFormation stack, we must first update the stack definition so that the VPC's set to "retain" upon deletion. Since we'll be replacing its definition with our Pulumi equivalent, we need to set this to ensure CloudFormation doesn't delete the VPC during the adoption process:

```diff
{
    "Parameters" : {
        "VPCCidr" : {
            "Type" : "String",
            "Default" : "10.0.0.0/16",
            "Description" : "Enter the CIDR block for the VPC. Default is 10.0.0.0/16."
        }
    },
    "Resources": {
        "myVpc": {
            "Type" : "AWS::EC2::VPC",
+           "DeletionPolicy": "Retain",
            "Properties" : {
                "CidrBlock" : { "Ref" : "VPCCidr" },
                "Tags" : [
                    {"Key": "Name", "Value": "Primary_CF_VPC"}
                ]
            }
        }
    },
    "Outputs": {
        "VpcId": {
            "Value": { "Ref": "myVpc" }
        }
    }
}
```

Remember to run `pulumi up` so that your changes are applied before moving on.

Next, we can adopt the resources under Pulumi's control, by using `import` IDs. For this example, recall that our VPC ID from above was `"vpc-0e1a74859af1da17f"`, which is what we will use for illustration purposes. Also, in this example, there is just one resource, so we can simply delete the CloudFormation stack in its entirety and replace it with a Pulumi definition of the VPC. In cases where multiple resources exist, you can delete them one by one, until the stack is eventually empty.

{{< langchoose csharp >}}

```javascript
let aws = require("@pulumi/aws");

let vpc = new aws.ec2.Vpc("myVpc", {
    cidrBlock: "10.0.0.0/16",
    tags: { Name: "Primary_CF_VPC" },
}, { import: "vpc-0e1a74859af1da17f" });

module.exports = {
    vpcId: vpc.id,
};
```

```typescript
import * as aws from "@pulumi/aws";

const vpc = new aws.ec2.Vpc("myVpc", {
    cidrBlock: "10.0.0.0/16",
    tags: { Name: "Primary_CF_VPC" },
}, { import: "vpc-0e1a74859af1da17f" });

export const vpcId = vpc.id;
```

```python
import pulumi_aws as aws

vpc = aws.ec2.Vpc('myVpc',
    cidr_block='10.0.0.0/16',
    tags={ 'Name': 'Primary_CF_VPC' },
    opts=ResourceOptions(import_='vpc-0e1a74859af1da17f')
)

pulumi.export('vpc_id', vpc.id)
```

```go
package main

import (
    "github.com/pulumi/pulumi-aws/sdk/go/aws/ec2"
    "github.com/pulumi/pulumi/sdk/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        vpc, err := ec2.NewVpc(ctx, "myVpc",
            &ec2.VpcArgs{
                CidrBlock: pulumi.String("10.0.0.0/16"),
                Tags: pulumi.Map{
                    "Name": pulumi.String("Primary_CF_VPC"),
                },
            },
            pulumi.Import(pulumi.ID("vpc-0e1a74859af1da17f")),
        })
        if err != nil {
            return err
        }

        ctx.Export("vpcId", vpc.ID())
        return nil
    })
}
```

```csharp
using System.Collections.Generic;
using System.Threading.Tasks;

using Pulumi;
using Ec2 = Pulumi.Aws.Ec2;

class Program
{
    static Task<int> Main()
    {
        return Deployment.RunAsync(() => {
            var vpc = new Ec2.Vpc("myVpc",
                new Ec2.VpcArgs
                {
                    CidrBlock = "10.0.0.0/16",
                    Tags = new Dictionary<string, object?>
                    {
                        { "Name", "Primary_CF_VPC" },
                    },
                },
                new CustomResourceOptions {
                    ImportId = "vpc-0e1a74859af1da17f",
                },
            );

            return new Dictionary<string, object?>
            {
                { "vpcId", vpc.Id },
            };
        });
    }
}
```

After running `pulumi up`, your VPC will become under the control of Pulumi without any disruption, and you can then delete the import directives from your code. All subsequent infrastructure changes you'd like to be made can happen within Pulumi instead of AWS CloudFormation.

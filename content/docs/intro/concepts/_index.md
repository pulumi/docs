---
title: Architecture & Concepts
meta_desc: This page describes the primary concepts behind the Pulumi infrastructure as code platform.
menu:
  intro:
    identifier: concepts
    weight: 2

aliases: ["/docs/reference/concepts/"]
---

Pulumi is a modern infrastructure as code platform. It includes a CLI, runtime, libraries, and a hosted service working together to deliver a robust way of provisioning, updating, and managing cloud infrastructure.

Instead of YAML or a domain-specific language (DSL), Pulumi leverages existing programming languages---TypeScript, JavaScript, Python, Go, and .NET---and their native tools, libraries, and package managers to interact with cloud resources through the Pulumi SDK.

> If this is your first time using Pulumi, you likely want to begin with [the Getting Started guide]({{< relref "/docs/get-started" >}}) for your cloud of choice. It will walk you through an [AWS]({{< relref "/docs/get-started/aws" >}}), [Azure]({{< relref "/docs/get-started/azure" >}}), [GCP]({{< relref "/docs/get-started/gcp" >}}), or [Kubernetes]({{< relref "/docs/get-started/kubernetes" >}}) deployment from start to finish.

## Pulumi Overview {#overview}

This diagram illustrates the structure and major components of Pulumi.

![Pulumi programming model diagram.](/images/docs/pulumi-programming-model-diagram.svg)

*Programs* use existing [programming languages]({{< relref "/docs/intro/languages/" >}}) to define how your cloud infrastructure should be deployed. After writing a program, you run the [Pulumi CLI]({{< relref "/docs/reference/cli/)" >}}) command `pulumi up`, which executes the program and determines the desired infrastructure state for all resources declared.

*Resources* represent a type of infrastructure that you declare in your program. Resources have properties that correspond to the desired state of your infrastructure and can be used as *inputs and outputs* that represent dependencies between resources.

_Stacks_ are isolated, configurable instances of a Pulumi program. Because of their isolated nature, you can think of stacks are similar to deployment environments where your Pulumi program runs.

The program, stacks, and other metadata reside in a *Project* directory.

To illustrate these concepts, the following program shows how to create an AWS EC2 security group and an EC2 instance that uses it:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
let pulumi = require("@pulumi/pulumi");
let aws = require("@pulumi/aws");

let group = new aws.ec2.SecurityGroup("web-sg", {
    description: "Enable HTTP access",
    ingress: [{ protocol: "tcp", fromPort: 80, toPort: 80, cidrBlocks: ["0.0.0.0/0"] }],
});

let server = new aws.ec2.Instance("web-server", {
    ami: "ami-6869aa05",
    instanceType: "t2.micro",
    securityGroups: [ group.name ], // reference the security group resource above
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

let group = new aws.ec2.SecurityGroup("web-sg", {
    description: "Enable HTTP access",
    ingress: [{ protocol: "tcp", fromPort: 80, toPort: 80, cidrBlocks: ["0.0.0.0/0"] }],
});

let server = new aws.ec2.Instance("web-server", {
    ami: "ami-6869aa05",
    instanceType: "t2.micro",
    securityGroups: [ group.name ], // reference the security group resource above
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
import pulumi_aws as aws

group = aws.ec2.SecurityGroup('web-sg',
    description='Enable HTTP access',
    ingress=[
        { 'protocol': 'tcp', 'from_port': 80, 'to_port': 80, 'cidr_blocks': ['0.0.0.0/0'] }
    ])

server = aws.ec2.Instance('web-server',
    ami='ami-6869aa05',
    instance_type='t2.micro',
    security_groups=[group.name]) # reference the security group resource above
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
    "github.com/pulumi/pulumi-aws/sdk/v4/go/aws/ec2"
    "github.com/pulumi/pulumi/sdk/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        group, err := ec2.NewSecurityGroup(ctx, "web-sg", &ec2.SecurityGroupArgs{
            Description: pulumi.String("Enable HTTP access"),
            Ingress: ec2.SecurityGroupIngressArray{
                ec2.SecurityGroupIngressArgs{
                    Protocol:   pulumi.String("tcp"),
                    FromPort:   pulumi.Int(80),
                    ToPort:     pulumi.Int(80),
                    CidrBlocks: pulumi.StringArray{pulumi.String("0.0.0.0/0")},
                },
            },
        })
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
using System.Threading.Tasks;
using Pulumi;
using Pulumi.Aws.Ec2;
using Pulumi.Aws.Ec2.Inputs;

class Program
{
    static Task<int> Main() => Deployment.RunAsync<MyStack>();
}


class MyStack : Stack
{
    public MyStack()
    {
        var group = new SecurityGroup("web-sg", new SecurityGroupArgs {
            Description = "Enable HTTP access",
            Ingress = {
                new SecurityGroupIngressArgs {
                    Protocol = "tcp",
                    FromPort = 80,
                    ToPort = 80,
                    CidrBlocks = { "0.0.0.0/0" }
                }
            }
        });
        var server = new Instance("web-server", new InstanceArgs {
            Ami = "ami-6869aa05",
            InstanceType = "t2.micro",
            SecurityGroups = { group.Name }
        });
    }
}
```

{{% /choosable %}}

{{< /chooser >}}

The two resource objects, and their properties, are used by Pulumi to perform the appropriate actions on your infrastructure. For example, Pulumi understands that you would like an EC2 security group named `web-sg`, with a single ingress rule and a `t2.micro`-sized EC2 instance running AMI `ami-8689aa05` using that security group. And because of the output properties, Pulumi also understands the dependencies between resources, which maximizes parallelism and ensures correct ordering.

When you update your cloud project with Pulumi, Pulumi will compute the desired state, compare it to the current infrastructure you already have (if any), show you the delta, and let you confirm and carry out the changes.

If needed, you can also export resulting infrastructure values to access outside your application. For example, adding the following code to the example above exports the server's resulting IP address and DNS name to either stdout or for use by another stack:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
// ...
module.exports = {
    publicIp: server.publicIp,
    publicDns: server.publicDns,
};
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
// ...
export let publicIp = server.publicIp;
export let publicDns = server.publicDns;
```

{{% /choosable %}}
{{% choosable language python %}}

```python
# ...
pulumi.export('public_ip', server.public_ip)
pulumi.export('public_dns', server.public_dns)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
// ...
        ctx.Export("publicIp", server.PublicIp)
        ctx.Export("publicHostName", server.PublicDns)
        return nil
    })
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
// ...
        this.PublicIp = server.PublicIp;
        this.PublicDns = server.PublicDns;
    }

    [Output] Output<string> PublicIp { get; set; }
    [Output] Output<string> PublicDns { get; set; }
}
```

{{% /choosable %}}

{{< /chooser >}}

## Concept Details

The following topics provide more details on the core concepts of Pulumi and how to use it:

<div class="md:flex flex-row mt-6 mb-6">
    <div class="w-1/2 border-solid border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="{{< relref "/docs/intro/concepts/project" >}}"><i class="fas fa-folder-open pr-2"></i>Projects</a></h3>
        <p>Learn how Pulumi projects are organized and configured.</p>
    </div>
    <div class="w-1/2 border-solid ml-4 border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="{{< relref "/docs/intro/concepts/resources" >}}"><i class="fas fa-server pr-2"></i>Resources</a></h3>
        <p>Learn more about how to use and manage resources in your program.</p>
    </div>
</div>
<div class="md:flex flex-row mt-6 mb-6">
    <div class="w-1/2 border-solid border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="{{< relref "/docs/intro/concepts/inputs-outputs" >}}"><i class="fas fa-hdd pr-2"></i>Inputs and Outputs</a></h3>
        <p>Learn how to use resource properties to handle dependencies between resources.</p>
    </div>
    <div class="w-1/2 border-solid ml-4 border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="{{< relref "/docs/intro/concepts/stack" >}}"><i class="fas fa-cloud pr-2"></i>Stacks</a></h3>
        <p>Learn how to create and deploy stacks.</p>
    </div>
</div>
<div class="md:flex flex-row mt-6 mb-6">
    <div class="w-1/2 border-solid border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="{{< relref "/docs/intro/concepts/state" >}}"><i class="fas fa-file-alt pr-2"></i>State and Backends</a></h3>
        <p>Learn how Pulumi stores state and manages concurrency.</p>
    </div>
    <div class="w-1/2 border-solid ml-4 border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="{{< relref "/docs/intro/concepts/how-pulumi-works" >}}"><i class="fas fa-upload pr-2"></i>How Pulumi Deploys Infrastructure</a></h3>
        <p>Learn how Pulumi performs deployments.</p>
    </div>
</div>
<div class="md:flex flex-row mt-6 mb-6">
    <div class="w-1/2 border-solid border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="{{< relref "/docs/intro/concepts/config" >}}"><i class="fas fa-check-square pr-2"></i>Configuring Stacks</a></h3>
        <p>Learn how to configure stacks for different deployment scenarios.</p>
    </div>
    <div class="w-1/2 border-solid ml-4 border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="{{< relref "/docs/intro/concepts/secrets" >}}"><i class="fas fa-key pr-2"></i>Handling Secrets</a></h3>
        <p>Learn how to handle sensitive data and how to store secret encrypted settings in Pulumi.</p>
    </div>
</div>
<div class="md:flex flex-row mt-6 mb-6">
    <div class="w-1/2 border-solid border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="{{< relref "/docs/intro/concepts/organizing-stacks-projects" >}}"><i class="fas fa-laptop-code pr-2"></i>Organizing Projects</a></h3>
        <p>Learn some best practices for organizing your Pulumi programs.</p>
    </div>
    <div class="w-1/2 border-solid ml-4 border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="{{< relref "/docs/intro/concepts/runtime-functions" >}}"><i class="fas fa-terminal pr-2"></i>Utilizing Helper Functions</a></h3>
        <p>Learn about some runtime functions to help you when creating Pulumi programs.</p>
    </div>
</div>
<div class="md:flex flex-row mt-6 mb-6">
    <div class="w-1/2 border-solid border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="{{< relref "/docs/intro/concepts/assets-archives" >}}"><i class="fas fa-stream pr-2"></i>Assets and Archives</a></h3>
        <p>Learn about to use local or remote files with your Pulumi program.</p>
    </div>
</div>

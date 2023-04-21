---
title_tag: "Using AWS VPC | Crosswalk"
title: Using AWS VPC
meta_desc: Pulumi Crosswalk for AWS provides simple, out of the box VPC functionality that follows widely accepted best
           practices.
linktitle: Virtual Private Cloud (VPC)
menu:
  userguides:
    parent: crosswalk-aws
    weight: 10

aliases: ["/docs/reference/crosswalk/aws/vpc/"]
---

<a href="./">
    <img src="/images/docs/reference/crosswalk/aws/logo.svg" align="right" width="280" style="margin: 0 0 32px 16px;">
</a>

[Amazon Virtual Private Cloud (Amazon VPC)](https://aws.amazon.com/vpc) lets you provision a logically isolated section
of the AWS Cloud where you can launch AWS resources in a virtual network that you define. You have complete control
over your virtual networking environment, including selection of your own IP address range, creation of subnets, and
configuration of route tables and network gateways. You can use both IPv4 and IPv6 in your VPC for secure and easy
access to resources and applications, and use multiple layers of security, including security groups and network
access control lists, to limit network access to and from resources.

## Overview

Pulumi Crosswalk for AWS provides simple, out of the box VPC functionality that follows widely accepted best
practices. This ensures you can provision and evolve your VPCs across many environments productively and safely,
without needing to recreate the same VPC templates for every new project you tackle.

Using these capabilities, you can control the entire virtual network and restrict access to just those network
endpoints that require it. These network resources are essential to configuring many of the other Crosswalk AWS
components, including ECS and EKS clusters, API gateways, and various network load balancing options.

Each account has a default regional network and VPC to make it easy to get up and running. Most production
circumstances call for dedicated VPCs and network isolation. This includes multi-tenanted scenarios where VPCs can be
used for strong network isolation between endpoints and resources that are otherwise sharing an AWS account.

## Managing VPCs

The [VPC resource](/registry/packages/aws/api-docs/ec2/vpc/) class provides full access to the
AWS VPC API, and [aws.ec2](/registry/packages/aws/api-docs/ec2/) the entire AWS EC2 API. Using
these packages, you can configure all aspects of AWS networks for your applications and infrastructure.

The [awsx.ec2.Vpc](/docs/reference/pkg/nodejs/pulumi/awsx/ec2#Vpc) class encapsulates a complete
configuration of an AWS network, including the actual VPC itself, in addition to public and/or private subnets, route
tables, and gateways, across multiple availability zones. It is designed to be easier to use, with reasonable defaults,
and follows AWS's own best practices, with configurability for advanced scenarios. The two can be used together.

Below are some of the most common infrastructure as code tasks with VPCs.

## Getting the Default VPC

Often resources like clusters, API gateways, lambdas, and more, will request a VPC object or ID. This ensures
such resources inside of your VPC so network traffic are isolated from other VPCs in your account.

So where do you get such a VPC from? One way is that each AWS account has a default VPC per region. Using the default
VPC is often the easiest path when you're just getting up and running or don't yet understand your specific networking
requirements. Most resources will use this default VPC automatically if you leave it unspecified. In other cases,
you may be required to pass it explicitly, in which case you'll need to get it programmatically.

To get the default VPC, just call the `awsx.vpc.DefaultVpc("default-vpc");` function:

{{< chooser language "typescript,python,csharp" / >}}

{{% choosable language typescript %}}

```typescript
import * as awsx from "@pulumi/awsx";

// Fetch the default VPC information from your AWS account:
const vpc = new awsx.ec2.DefaultVpc("default-vpc");

// Export a few interesting fields to make them easy to use:
export const vpcId = vpc.vpcId;
export const vpcPrivateSubnetIds = vpc.privateSubnetIds;
export const vpcPublicSubnetIds = vpc.publicSubnetIds;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_awsx as awsx

vpc = awsx.ec2.DefaultVpc("default-vpc")

pulumi.export("vpcId", vpc.vpc_id)
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using System.Threading.Tasks;
using Pulumi;
using Ec2 = Pulumi.Awsx.Ec2;

class MyStack : Stack
{
    public MyStack()
    {
        var vpc = new DefaultVpc("default-vpc");
        this.VpcId = vpc.vpcId;
    }
    [Output] public Output<string> VpcId { get; set; }
}

class Program
{
    static Task<int> Main(string[] args) => Deployment.RunAsync<MyStack>();
}
```

{{% /choosable %}}

This example reads the default VPC and exports some of its properties for easy consumption. `pulumi up` will show:

```bash
$ pulumi up
Updating (dev):

     Type                     Name                  Status
 +   pulumi:pulumi:Stack      crosswalk-aws-dev     created
 +   └─ awsx:ec2:DefaultVpc   default-vpc           created

Outputs:
    publicSubnetIds : [
        [0]: "subnet-03711d3b9b21b3a8e"
        [1]: "subnet-06e8296c053e2b952"
        [2]: "subnet-0fc2dc8f8ba906919"
        [3]: "subnet-037f366816336db85"
    ]
    privateSubnetIds : [
        [0]: "subnet-03711d3b9b21b3a8e"
        [1]: "subnet-06e8296c053e2b952"
        [2]: "subnet-0fc2dc8f8ba906919"
        [3]: "subnet-037f366816336db85"
    ]

Resources:
    + 2 created

Duration: 9s
```

In this case, the VPC is not created and managed by Pulumi. Instead `DefaultVpc` reads from your AWS account
and returns the VPC metadata. This object can be introspected or passed anywhere a `VpcID` or `SubnetIds` are expected.

## Setting Up a New VPC

Although using the default VPC is easy, it's often not suitable for production. By setting up a dedicated VPC,
we can isolate workloads from existing ones, and have more control over subnet configuration, routing, and
controlling ingress and egress security rules.

To set up a new VPC, allocate a new `awsx.ec2.Vpc` object. This class offers a number of options, ranging from
simple defaults that many will want to start with, to complete control over everything VPC has to offer.

The following code creates a new VPC using all default settings:

{{< chooser language "typescript,python,csharp" / >}}

{{% choosable language typescript %}}

```typescript
import * as awsx from "@pulumi/awsx";

// Allocate a new VPC with the default settings:
const vpc = new awsx.ec2.Vpc("custom");

// Export a few resulting fields to make them easy to use:
export const vpcId = vpc.vpcId;
export const privateSubnetIds = vpc.privateSubnetIds;
export const publicSubnetIds = vpc.publicSubnetIds;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_awsx as awsx

vpc = awsx.ec2.Vpc("custom")

pulumi.export("vpcId", vpc.vpc_id)
pulumi.export("publicSubnetIds", vpc.public_subnet_ids)
pulumi.export("privateSubnetIds", vpc.private_subnet_ids)
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using Pulumi;
using Ec2 = Pulumi.Awsx.Ec2;

class MyStack : Stack
{
    public MyStack()
    {
        var vpc = new Ec2.Vpc("custom");

        this.VpcId = vpc.VpcId;
        this.PublicSubnetIds = vpc.PublicSubnetIds;
        this.PrivateSubnetIds = vpc.PrivateSubnetIds;
    }


    [Output] public Output<ImmutableArray<string>> PrivateSubnetIds { get; private set; }
    [Output] public Output<ImmutableArray<string>> PublicSubnetIds { get; private set; }
    [Output] public Output<string> VpcId { get; set; }
}

class Program
{
    static Task<int> Main(string[] args) => Deployment.RunAsync<MyStack>();
}
```

{{% /choosable %}}

If we run `pulumi up`, the VPC and its supporting resources will be provisioned:

```bash
$ pulumi up
Updating (dev):

     Type                                          Name                Status
 +   pulumi:pulumi:Stack                           crosswalk-aws-dev   created
 +   └─ awsx:ec2:Vpc                               custom              created
 +      └─ aws:ec2:Vpc                             custom              created
 +         ├─ aws:ec2:InternetGateway              custom              created
 +         ├─ aws:ec2:Subnet                       custom-private-3    created
 +         │  └─ aws:ec2:RouteTable                custom-private-3    created
 +         │     ├─ aws:ec2:RouteTableAssociation  custom-private-3    created
 +         │     └─ aws:ec2:Route                  custom-private-3    created
 +         ├─ aws:ec2:Subnet                       custom-public-1     created
 +         │  ├─ aws:ec2:RouteTable                custom-public-1     created
 +         │  │  ├─ aws:ec2:RouteTableAssociation  custom-public-1     created
 +         │  │  └─ aws:ec2:Route                  custom-public-1     created
 +         │  ├─ aws:ec2:Eip                       custom-1            created
 +         │  └─ aws:ec2:NatGateway                custom-1            created
 +         ├─ aws:ec2:Subnet                       custom-public-3     created
 +         │  ├─ aws:ec2:RouteTable                custom-public-3     created
 +         │  │  ├─ aws:ec2:RouteTableAssociation  custom-public-3     created
 +         │  │  └─ aws:ec2:Route                  custom-public-3     created
 +         │  ├─ aws:ec2:Eip                       custom-3            created
 +         │  └─ aws:ec2:NatGateway                custom-3            created
 +         ├─ aws:ec2:Subnet                       custom-private-1    created
 +         │  └─ aws:ec2:RouteTable                custom-private-1    created
 +         │     ├─ aws:ec2:RouteTableAssociation  custom-private-1    created
 +         │     └─ aws:ec2:Route                  custom-private-1    created
 +         ├─ aws:ec2:Subnet                       custom-private-2    created
 +         │  └─ aws:ec2:RouteTable                custom-private-2    created
 +         │     ├─ aws:ec2:RouteTableAssociation  custom-private-2    created
 +         │     └─ aws:ec2:Route                  custom-private-2    created
 +         └─ aws:ec2:Subnet                       custom-public-2     created
 +            ├─ aws:ec2:Eip                       custom-2            created
 +            ├─ aws:ec2:RouteTable                custom-public-2     created
 +            │  ├─ aws:ec2:Route                  custom-public-2     created
 +            │  └─ aws:ec2:RouteTableAssociation  custom-public-2     created
 +            └─ aws:ec2:NatGateway                custom-2            created

Outputs:
  + privateSubnetIds: [
  +     [0]: "subnet-0dd701be10146604d"
  +     [1]: "subnet-0cb44ff5ad9916c8b"
  +     [2]: "subnet-0a71e13e0f7cb1072"
    ]
  + publicSubnetIds : [
  +     [0]: "subnet-07aeb839d421ec509"
  +     [1]: "subnet-0f3ddf15e83b09a51"
  +     [2]: "subnet-0ea5745eb5d7d5353"
    ]
  + vpcId           : "vpc-06d9c2a16345db520"

Resources:
    + 34 created

Duration: 2m42s
```

If unspecified, this VPC will use the following defaults:

* An IPv4 CIDR block of `10.0.0.0/16`.
* The first `3` availability zones inside of your region.
* A public and private subnet per availability zone.
* Equally partitioned CIDR address spaces per subnet (per availability zone).
* A NAT Gateway and EIP per private subnet.
* A single Internet Gateway for all public subnets to use.

The following sections show how to explicitly manage any or all of these settings.

## Configuring CIDR Blocks for a VPC

Although the default CIDR block of `10.0.0.0/16` is reasonable most of the time, it is easy to override.

> Classless Inter-Domain Routing (CIDR) is an Internet standard for specifying ranges of
> IP addresses. See [RFC 4632](https://tools.ietf.org/html/rfc4632) for more details.

To set our VPC's CIDR block, pass a custom `cidrBlock` argument to `awsx.ec2.Vpc`'s constructor:

{{< chooser language "typescript,python,csharp" / >}}

{{% choosable language typescript %}}

```typescript
import * as awsx from "@pulumi/awsx";

// Allocate a new VPC with the default settings:
const vpc = new awsx.ec2.Vpc("custom", {
  cidrBlock: "172.16.8.0/24",
});

// Export a few resulting fields to make them easy to use:
export const vpcId = vpc.vpcId;
export const privateSubnetIds = vpc.privateSubnetIds;
export const publicSubnetIds = vpc.publicSubnetIds;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_awsx as awsx

vpc = awsx.ec2.Vpc("custom", cidr_block="172.16.8.0/24")

pulumi.export("vpcId", vpc.vpc_id)
pulumi.export("publicSubnetIds", vpc.public_subnet_ids)
pulumi.export("privateSubnetIds", vpc.private_subnet_ids)
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using Pulumi;
using Ec2 = Pulumi.Awsx.Ec2;

class MyStack : Stack
{
    public MyStack()
    {
        var vpc = new Ec2.Vpc("custom", new Ec2.VpcArgs
        {
            CidrBlock = "172.16.8.0/24",
        });

        this.VpcId = vpc.VpcId;
        this.PublicSubnetIds = vpc.PublicSubnetIds;
        this.PrivateSubnetIds = vpc.PrivateSubnetIds;
    }

    [Output] public Output<ImmutableArray<string>> PrivateSubnetIds { get; private set; }
    [Output] public Output<ImmutableArray<string>> PublicSubnetIds { get; private set; }
    [Output] public Output<string> VpcId { get; set; }
}

class Program
{
    static Task<int> Main(string[] args) => Deployment.RunAsync<MyStack>();
}
```

{{% /choosable %}}

This decreases the number of available IP addresses in our VPC from the default of 65,536 addresses (`/16` netmask) to
256 addresses (`/24` netmask), in addition to changing the IP address prefix from `10.0.0.0` to `172.16.8.0`.

> A VPC can have a minimum of 16 addresses, using the CIDR netmask `/28`, and a maximum of 65,536 addresses, using
> the netmask `/16`. The addresses are allocated across availability zones which may incur additional constraints.

In addition to configuring the CIDR block for your entire VPC, you can optionally assign a CIDR block to your
VPC's subnets. These must reside entirely within your VPC's CIDR block. If you do not explicitly specify ranges,
traffic will be evenly partitioned between availability zones within the VPC CIDR block range provided.

See [IP Addressing in Your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-ip-addressing.html)
for information about the full range of IP address and CIDR configuration available for your VPC.

## Configuring Availability Zones for an AWS VPC

A VPC spans all of the availability zones in your region. By default, however, the `awsx.ec2.Vpc` resource will
only use 2 of them when allocating subnets and the associated gateways. This provides fault tolerance between
two zones at a reasonable cost.

All regions support at least 3 availability zones, but many of them support more. If you'd like to improve the
fault tolerance of your configuration, override this with the `numberOfAvailabilityZones` argument:

{{< chooser language "typescript,python,csharp" / >}}

{{% choosable language typescript %}}

```typescript
import * as awsx from "@pulumi/awsx";

// Allocate a new VPC with the default settings:
const vpc = new awsx.ec2.Vpc("custom", {
  numberOfAvailabilityZones: 4,
});

// Export a few resulting fields to make them easy to use:
export const vpcId = vpc.vpcId;
export const privateSubnetIds = vpc.privateSubnetIds;
export const publicSubnetIds = vpc.publicSubnetIds;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_awsx as awsx

vpc = awsx.ec2.Vpc("custom", number_of_availability_zones=4)

pulumi.export("vpcId", vpc.vpc_id)
pulumi.export("publicSubnetIds", vpc.public_subnet_ids)
pulumi.export("privateSubnetIds", vpc.private_subnet_ids)
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using Pulumi;
using Ec2 = Pulumi.Awsx.Ec2;

class MyStack : Stack
{
    public MyStack()
    {
        var vpc = new Ec2.Vpc("custom", new Ec2.VpcArgs
        {
            NumberOfAvailabilityZones = 4,
        });

        this.VpcId = vpc.VpcId;
        this.PublicSubnetIds = vpc.PublicSubnetIds;
        this.PrivateSubnetIds = vpc.PrivateSubnetIds;
    }

    [Output] public Output<ImmutableArray<string>> PrivateSubnetIds { get; private set; }
    [Output] public Output<ImmutableArray<string>> PublicSubnetIds { get; private set; }
    [Output] public Output<string> VpcId { get; set; }
}

class Program
{
    static Task<int> Main(string[] args) => Deployment.RunAsync<MyStack>();
}
```

{{% /choosable %}}

The VPC resource will internally adjust to fully consume 4 availability zones and split traffic accordingly.

For information about regional support for availability zones, refer to AWS's
[Global Infrastructures Regions and AZs](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/) help page.

## Configuring Subnets for a VPC

A VPC spans all of the availability zones in a region. You can additionally create one or more subnets in each
availability zone, to increase your fault tolerance within a region and control routing.

By default, the `awsx.ec2.Vpc` class will allocate a public and a private subnet for each availability zone and evenly
partition traffic amongst each of them. In the event that you do not wish to keep this default, you can override
the behavior using its constructor's `subnets` argument.

For example, this program replicates the default behavior but with an explicit specification:

{{< chooser language "typescript,python,csharp" / >}}

{{% choosable language typescript %}}

```typescript
import * as awsx from "@pulumi/awsx";

// Allocate a new VPC with public and private subnets per AZ:
const vpc = new awsx.ec2.Vpc("custom", {
  subnetSpecs:[
    {
      type: awsx.ec2.SubnetType.Public,
      cidrMask: 22,
    },
    {
      type: awsx.ec2.SubnetType.Private,
      cidrMask: 20,
    },
  ],
});

// Export a few resulting fields to make them easy to use:
export const vpcId = vpc.vpcId;
export const vpcPrivateSubnetIds = vpc.privateSubnetIds;
export const vpcPublicSubnetIds = vpc.publicSubnetIds;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_awsx as awsx

vpc = awsx.ec2.Vpc("custom", subnet_specs=[
  awsx.ec2.SubnetSpecArgs(
    type=awsx.ec2.SubnetType.PRIVATE,
    cidr_mask=20,
  ),
  awsx.ec2.SubnetSpecArgs(
    type=awsx.ec2.SubnetType.PUBLIC,
    cidr_mask=22,
  )
])

pulumi.export("vpcId", vpc.vpc_id)
pulumi.export("publicSubnetIds", vpc.public_subnet_ids)
pulumi.export("privateSubnetIds", vpc.private_subnet_ids)
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using System.Collections.Immutable;
using Pulumi;
using Pulumi.Awsx.Ec2.Inputs;
using Ec2 = Pulumi.Awsx.Ec2;

class MyStack : Stack
{
    public MyStack()
    {
        var vpc = new Ec2.Vpc("custom", new Ec2.VpcArgs
        {
            SubnetSpecs =
            {
                new SubnetSpecArgs
                {
                    Type = Ec2.SubnetType.Public,
                    CidrMask = 22,
                },
                new SubnetSpecArgs
                {
                    Type = Ec2.SubnetType.Private,
                    CidrMask = 20,
                }
            }
        });

        this.VpcId = vpc.VpcId;
        this.PublicSubnetIds = vpc.PublicSubnetIds;
        this.PrivateSubnetIds = vpc.PrivateSubnetIds;
    }

    [Output] public Output<ImmutableArray<string>> PrivateSubnetIds { get; private set; }
    [Output] public Output<ImmutableArray<string>> PublicSubnetIds { get; private set; }
    [Output] public Output<string> VpcId { get; set; }
}

class Program
{
    static Task<int> Main(string[] args) => Deployment.RunAsync<MyStack>();
}
```

{{% /choosable %}}

The `subnetSpecs` argument takes an array of subnet specifications. Each one can include this information:

* `type`: A required type of subnet to create. There are three kinds available:
    * A `Public` subnet is one whose traffic is routed to an
    [Internet Gateway (IGW)](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html).
    * A `Private` subnet is one that is configured to use a
    [NAT Gateway (NAT)](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat.html) so that it can reach the internet,
    but which prevents the internet from initiating connections to it.
    * An `Isolated` subnet is one that cannot reach the internet either through an IGW or with NAT.

* `cidrMask`: The number of leading bits in the VPC's CIDR block to use to define the CIDR for this specific
  subnet. By providing masking bits, this ensures each subnet has a distinct block.

* `name`: An optional name to use as part of the subnet name. If not provided, the type of the subnet will be
  used. As a result, this is required when making multiple subnets of the same type.

Refer to [VPCs and Subnets](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html) for complete
information about how VPCs and subnets relate in AWS and the configuration options available to you.

## Configuring Internet and NAT Gateways for Subnets in a VPC

By default, any VPC with public subnets will have a single Internet Gateway created for it. All public subnets will be
routable for all IPv4 addresses connections through this gateway.

To allow connections from private subnets to the internet, NAT gateways will also be created. If not specified, one
NAT Gateway will be created for each availability zone, to maximize fault tolerance. Because the NAT gateway must be
in a public subnet, NAT gateways will only be created if there is at least one public subnet.

Fewer NAT gateways can be requested (e.g., to save on costs) using the `natGateways` property:

{{< chooser language "typescript,python,csharp" / >}}

{{% choosable language typescript %}}

```typescript
import * as awsx from "@pulumi/awsx";

// Allocate a new VPC with public and private subnets per AZ:
const vpc = new awsx.ec2.Vpc("custom", {
  natGateways: {
    strategy: awsx.ec2.NatGatewayStrategy.Single,
  }
});

// Export a few resulting fields to make them easy to use:
export const vpcId = vpc.vpcId;
export const vpcPrivateSubnetIds = vpc.privateSubnetIds;
export const vpcPublicSubnetIds = vpc.publicSubnetIds;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_awsx as awsx

vpc = awsx.ec2.Vpc("custom", nat_gateways=awsx.ec2.NatGatewayConfigurationArgs(
    strategy=awsx.ec2.NatGatewayStrategy.SINGLE))

pulumi.export("vpcId", vpc.vpc_id)
pulumi.export("publicSubnetIds", vpc.public_subnet_ids)
pulumi.export("privateSubnetIds", vpc.private_subnet_ids)
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using System.Collections.Immutable;
using Pulumi;
using Pulumi.Awsx.Ec2.Inputs;
using Ec2 = Pulumi.Awsx.Ec2;

class MyStack : Stack
{
    public MyStack()
    {
        var vpc = new Ec2.Vpc("custom", new Ec2.VpcArgs
        {
            NatGateways = new NatGatewayConfigurationArgs
            {
                Strategy = Ec2.NatGatewayStrategy.Single
            }
        });

        this.VpcId = vpc.VpcId;
        this.PublicSubnetIds = vpc.PublicSubnetIds;
        this.PrivateSubnetIds = vpc.PrivateSubnetIds;
    }

    [Output] public Output<ImmutableArray<string>> PrivateSubnetIds { get; private set; }
    [Output] public Output<ImmutableArray<string>> PublicSubnetIds { get; private set; }
    [Output] public Output<string> VpcId { get; set; }
}

class Program
{
    static Task<int> Main(string[] args) => Deployment.RunAsync<MyStack>();
}
```

{{% /choosable %}}

In the case where there is one NAT gateway per availability zone, then routing is very simple. Each private subnet
will have have connections routed through gateway in that availability zone.

In the case where there are fewer NAT gateways than availability zones, however, routing works differently. If there
are _N_ NAT gateways requested, then the first _N_ availability zones will get a NAT gateway. Routing to private subnets
in those availability zones works as above. However, all remaining availability zones will have their private subnets
routed to in a round-robin fashion from the availability zones with NAT gateways.

> Warning: While reducing the number of NAT gateways will save money, it also introduces risk as failure of one
> availability zone may impact others.

## Configuring Security Groups for a VPC

A [security group](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html) acts as a virtual firewall for your instance (e.g EC2) to control inbound and outbound traffic. Security groups act at the instance level, not the subnet level. Therefore, each instance in a subnet in your VPC can be assigned to a different set of security groups.

For security groups, you add _rules_ that control traffic what traffic is permitted in the form of _ingress rules_ (for
inbound traffic) and _egress rules_ (outbound traffic). In addition to specifying what network protocol and ports
these rules apply to, you can also specify source and destination locations using CIDR blocks and other notations.

Each VPC has a default Security Group that disallows all ingress from any external source, and permits all outbound
traffic. This will be used by default, however you may allocate and assign resources to different groups explicitly.

Here is a program that allocates a new group with a few rules:

{{< chooser language "typescript,python,csharp" / >}}

{{% choosable language typescript %}}

```typescript
import * as aws from "@pulumi/aws";
import * as awsx from "@pulumi/awsx";

// Allocate a new VPC with the default settings:
const vpc = new awsx.ec2.Vpc("custom");

// Allocate a security group and then a series of rules:
const sg = new aws.ec2.SecurityGroup("webserver-sg", {
  vpcId: vpc.vpcId,
  ingress: [{
    description: "allow SSH access from 203.0.113.25",
    fromPort: 22,
    toPort: 22,
    protocol: "tcp",
    cidrBlocks: ["203.0.113.25/32"],
  }, {
    description: "allow HTTPS access from anywhere",
    fromPort: 443,
    toPort: 443,
    protocol: "tcp",
    cidrBlocks: ["0.0.0.0/0"],
  }],
  egress: [{
    fromPort: 0,
    toPort: 0,
    protocol: "-1",
    cidrBlocks: ["0.0.0.0/0"],
  }],
});

// Export a few resulting fields to make them easy to use:
export const vpcId = vpc.vpcId;
export const privateSubnetIds = vpc.privateSubnetIds;
export const publicSubnetIds = vpc.publicSubnetIds;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_aws as aws
import pulumi_awsx as awsx

vpc = awsx.ec2.Vpc("custom")

allow_tls = aws.ec2.SecurityGroup("allowTls",
                                  description="Allow TLS inbound traffic",
                                  vpc_id=vpc.vpc_id,
                                  ingress=[aws.ec2.SecurityGroupIngressArgs(
                                    description="allow SSH access from 203.0.113.25",
                                    from_port=22,
                                    to_port=22,
                                    protocol="tcp",
                                    cidr_blocks=["203.0.113.25/32"],
                                  ), aws.ec2.SecurityGroupIngressArgs(
                                    description="allow HTTPS access from anywhere",
                                    from_port=443,
                                    to_port=443,
                                    protocol="tcp",
                                    cidr_blocks=["0.0.0.0/0"],
                                  )],
                                  egress=[aws.ec2.SecurityGroupEgressArgs(
                                    from_port=0,
                                    to_port=0,
                                    protocol="-1",
                                    cidr_blocks=["0.0.0.0/0"],
                                  )])

pulumi.export("vpcId", vpc.vpc_id)
pulumi.export("publicSubnetIds", vpc.public_subnet_ids)
pulumi.export("privateSubnetIds", vpc.private_subnet_ids)
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using Pulumi;
using Aws = Pulumi.Aws;
using Ec2 = Pulumi.Awsx.Ec2;

class MyStack : Stack
{
    public MyStack()
    {
        var vpc = new Ec2.Vpc("custom");

        var allowTls = new Aws.Ec2.SecurityGroup("allowTls", new Aws.Ec2.SecurityGroupArgs
        {
            Description = "Allow TLS inbound traffic",
            VpcId = vpc.VpcId,
            Ingress =
            {
                new Aws.Ec2.Inputs.SecurityGroupIngressArgs
                {
                    Description = "allow SSH access from 203.0.113.25",
                    FromPort = 22,
                    ToPort = 22,
                    Protocol = "tcp",
                    CidrBlocks =
                    {
                        "203.0.113.25/32"
                    },
                },
                new Aws.Ec2.Inputs.SecurityGroupIngressArgs
                {
                    Description = "allow HTTPS access from anywhere",
                    FromPort = 443,
                    ToPort = 443,
                    Protocol = "tcp",
                    CidrBlocks =
                    {
                        "0.0.0.0"
                    },
                },
            },
            Egress =
            {
                new Aws.Ec2.Inputs.SecurityGroupEgressArgs
                {
                    FromPort = 0,
                    ToPort = 0,
                    Protocol = "-1",
                    CidrBlocks =
                    {
                        "0.0.0.0/0",
                    },
                },
            },
        });

        this.VpcId = vpc.VpcId;
        this.PublicSubnetIds = vpc.PublicSubnetIds;
        this.PrivateSubnetIds = vpc.PrivateSubnetIds;
    }

    [Output] public Output<ImmutableArray<string>> PrivateSubnetIds { get; private set; }
    [Output] public Output<ImmutableArray<string>> PublicSubnetIds { get; private set; }
    [Output] public Output<string> VpcId { get; set; }
}

class Program
{
    static Task<int> Main(string[] args) => Deployment.RunAsync<MyStack>();
}
```

{{% /choosable %}}

For additional details about configuring security group rules, See the
[Security Groups for Your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html) documentation.

## How to use your VPC, Security Group, and EC2 instance

This example shows how to deploy an EC2 instance using a VPC and Security Group provisioned with the Crosswalk AWS component:

{{< chooser language "typescript,python,csharp" / >}}

{{% choosable language typescript %}}

```typescript
import * as aws from "@pulumi/aws";
import * as awsx from "@pulumi/awsx";

// Allocate a new VPC with the default settings:
const vpc = new awsx.ec2.Vpc("custom");

// Allocate a security group using the above techniques:
const sg = new aws.ec2.SecurityGroup("webserver-sg", {
  vpcId: vpc.vpcId,
})

// t2.micro is available in the AWS free tier
const size = "t2.micro";

// Get the most recent Amazon linux ami:
const ami = aws.ec2.getAmiOutput({
  filters: [{
    name: "name",
    values: ["amzn-ami-hvm-*"],
  }],
  owners: ["137112412989"], // This owner ID is Amazon
  mostRecent: true,
});

const server = new aws.ec2.Instance("webserver-www", {
  instanceType: size,
  vpcSecurityGroupIds: [ sg.id ], // reference the security group resource above
  subnetId: vpc.publicSubnetIds.apply(x => x![0]),  // reference the public subnet from the custom vpc above
  ami: ami.id,
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_aws as aws
import pulumi_awsx as awsx

vpc = awsx.ec2.Vpc("custom")

sg = aws.ec2.SecurityGroup("webserver-sg",
                                  vpc_id=vpc.vpc_id)

ami = aws.ec2.get_ami(filters=[
                            aws.ec2.GetAmiFilterArgs(
                              name="name",
                              values=["amzn-ami-hvm-*"],
                            )],
                          most_recent=True,
                          owners=["137112412989"])

server = aws.ec2.Instance("webserver-www",
                          instance_type="t2.micro",
                          vpc_security_group_ids=[sg.id],
                          ami=ami.id,
                          subnet_id=vpc.public_subnet_ids.apply(lambda id: id[0]))

pulumi.export("vpcId", vpc.vpc_id)
pulumi.export("publicSubnetIds", vpc.public_subnet_ids)
pulumi.export("privateSubnetIds", vpc.private_subnet_ids)
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using Pulumi;
using Aws = Pulumi.Aws;
using Ec2 = Pulumi.Awsx.Ec2;

class MyStack : Stack
{
    public MyStack()
    {
        var vpc = new Ec2.Vpc("custom");

        var sg = new Aws.Ec2.SecurityGroup("webserver-sg", new Aws.Ec2.SecurityGroupArgs
        {
            VpcId = vpc.VpcId,
        });

        var ami = Output.Create(Aws.Ec2.GetAmi.InvokeAsync(new Aws.Ec2.GetAmiArgs
        {
            Filters =
            {
                new Aws.Ec2.Inputs.GetAmiFilterArgs
                {
                    Name = "name",
                    Values =
                    {
                        "amzn-ami-hvm-*",
                    },
                },
            },
            MostRecent = true,
            Owners =
            {
                "137112412989",
            },
        }));

        var web = new Aws.Ec2.Instance("web", new Aws.Ec2.InstanceArgs
        {
            Ami = ami.Apply(ami => ami.Id),
            InstanceType = "t2.micro",
            VpcSecurityGroupIds =
            {
                sg.Id,
            },
            SubnetId = vpc.PublicSubnetIds.Apply(subnet => subnet[0]),
        });

        this.VpcId = vpc.VpcId;
        this.PublicSubnetIds = vpc.PublicSubnetIds;
        this.PrivateSubnetIds = vpc.PrivateSubnetIds;
    }

    [Output] public Output<ImmutableArray<string>> PrivateSubnetIds { get; private set; }
    [Output] public Output<ImmutableArray<string>> PublicSubnetIds { get; private set; }
    [Output] public Output<string> VpcId { get; set; }
}

class Program
{
    static Task<int> Main(string[] args) => Deployment.RunAsync<MyStack>();
}
```

{{% /choosable %}}

If we run `pulumi up`, the `aws.ec2.Instance` will be provisioned using the _first_ public subnet from the `awsx.ec2.Vpc` component and the security group provisioned with the `awsx.ec2.SecurityGroup` component:

```bash
$ pulumi up
Updating (dev):
     Type                                          Name                   Status
 +   pulumi:pulumi:Stack                           crosswalk-dev          created
 +   ├─ awsx:ec2:Vpc                               custom                 created
 +   │  └─ aws:ec2:Vpc                             custom                 created
 +   │     ├─ aws:ec2:InternetGateway              custom                 created
 +   │     ├─ aws:ec2:Subnet                       custom-public-2        created
 +   │     │  ├─ aws:ec2:Eip                       custom-2               created
 +   │     │  ├─ aws:ec2:RouteTable                custom-public-2        created
 +   │     │  │  ├─ aws:ec2:Route                  custom-public-2        created
 +   │     │  │  └─ aws:ec2:RouteTableAssociation  custom-public-2        created
 +   │     │  └─ aws:ec2:NatGateway                custom-2               created
 +   │     ├─ aws:ec2:Subnet                       custom-public-1        created
 +   │     │  ├─ aws:ec2:RouteTable                custom-public-1        created
 +   │     │  │  ├─ aws:ec2:RouteTableAssociation  custom-public-1        created
 +   │     │  │  └─ aws:ec2:Route                  custom-public-1        created
 +   │     │  ├─ aws:ec2:Eip                       custom-1               created
 +   │     │  └─ aws:ec2:NatGateway                custom-1               created
 +   │     ├─ aws:ec2:Subnet                       custom-public-3        created
 +   │     │  ├─ aws:ec2:Eip                       custom-3               created
 +   │     │  ├─ aws:ec2:RouteTable                custom-public-3        created
 +   │     │  │  ├─ aws:ec2:Route                  custom-public-3        created
 +   │     │  │  └─ aws:ec2:RouteTableAssociation  custom-public-3        created
 +   │     │  └─ aws:ec2:NatGateway                custom-3               created
 +   │     ├─ aws:ec2:Subnet                       custom-private-1       created
 +   │     │  └─ aws:ec2:RouteTable                custom-private-1       created
 +   │     │     ├─ aws:ec2:RouteTableAssociation  custom-private-1       created
 +   │     │     └─ aws:ec2:Route                  custom-private-1       created
 +   │     ├─ aws:ec2:Subnet                       custom-private-3       created
 +   │     │  └─ aws:ec2:RouteTable                custom-private-3       created
 +   │     │     ├─ aws:ec2:RouteTableAssociation  custom-private-3       created
 +   │     │     └─ aws:ec2:Route                  custom-private-3       created
 +   │     └─ aws:ec2:Subnet                       custom-private-2       created
 +   │        └─ aws:ec2:RouteTable                custom-private-2       created
 +   │           ├─ aws:ec2:RouteTableAssociation  custom-private-2       created
 +   │           └─ aws:ec2:Route                  custom-private-2       created
 +   ├─ aws:ec2:SecurityGroup                      webserver-sg           created
 +   └─ aws:ec2:Instance                           web                    created

Outputs:
    PrivateSubnetIds: [
        [0]: "subnet-0f494849172af77b6"
        [1]: "subnet-024b4e3ff6a4cf859"
        [2]: "subnet-0c50551a11e563fc7"
    ]
    PublicSubnetIds : [
        [0]: "subnet-00a260ee8643426dc"
        [1]: "subnet-0bd4649d712d67c17"
        [2]: "subnet-08ffd5328715d39c7"
    ]
    VpcId           : "vpc-0c5e0fd20533e9e6f"

Resources:
    + 36 created

Duration: 3m23s
```

## Setting Up a New VPC the Hard Way

The `awsx.ec2.Vpc` component encapsulates a lot of details, including subnets, route tables, gateways, in addition to
the VPC resource itself. The `aws.ec2` package, on the other hand, out of which `Vpc` is built, provides all of these
raw resource so that you can code directly to the underlying AWS resource types, exposing every underlying capability.

For information about configuring each of these resources, refer to each type's API documentation:

* [Vpc](/registry/packages/aws/api-docs/ec2/vpc/)
* [Subnet](/registry/packages/aws/api-docs/ec2/subnet/)
* [InternetGateway](/registry/packages/aws/api-docs/ec2/internetgateway/)
* [NatGateway](/registry/packages/aws/api-docs/ec2/natgateway/)
* [SecurityGroup](/registry/packages/aws/api-docs/ec2/securitygroup/)

These resources can be independently allocated, just as with the `Vpc` class shown above. They will need to be
connected together manually, however, which can provide greater flexibility but at a greater implementation cost.

Note that the constituent parts, in the form of these raw resources, are available as properties on the
resulting `Vpc` class. For instance, `internetGateway` will return the Internet Gateway object for a VPC.

## Additional VPC Resources

For more information about VPCs, read the following:

* [Amazon Virtual Private Cloud homepage](https://aws.amazon.com/vpc/)

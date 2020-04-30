---
title: "AWS Virtual Private Cloud (VPC)"
meta_desc: Pulumi Crosswalk for AWS provides simple, out of the box VPC functionality that follows widely accepted best
           practices.
linktitle: Virtual Private Cloud (VPC)
menu:
  userguides:
    parent: crosswalk-aws
    weight: 10

aliases: ["/docs/reference/crosswalk/aws/vpc/"]
---

<a href="{{< prelref "./" >}}">
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

The [VPC resource]({{< prelref "/docs/reference/pkg/aws/ec2/vpc" >}}) class provides full access to the
AWS VPC API, and [aws.ec2]({{< prelref "/docs/reference/pkg/aws/ec2" >}}) the entire AWS EC2 API. Using
these packages, you can configure all aspects of AWS networks for your applications and infrastructure.

The [awsx.ec2.Vpc]({{< prelref "/docs/reference/pkg/nodejs/pulumi/awsx/ec2#Vpc" >}}) class encapsulates a complete
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

To get the default VPC, just call the `awsx.ec2.Vpc.getDefault()` function:

```typescript
import * as awsx from "@pulumi/awsx";

// Fetch the default VPC information from your AWS account:
const vpc = awsx.ec2.Vpc.getDefault();

// Export a few interesting fields to make them easy to use:
export const vpcId = vpc.id;
export const vpcPrivateSubnetIds = vpc.privateSubnetIds;
export const vpcPublicSubnetIds = vpc.publicSubnetIds;
```

This example reads the default VPC and exports some of its properties for easy consumption. `pulumi up` will show:

```bash
$ pulumi up
Updating (dev):

     Type                     Name                  Status
 +   pulumi:pulumi:Stack      crosswalk-aws-dev     created
 +   ├─ awsx:x:ec2:Vpc        default-vpc           created
 +   │  ├─ awsx:x:ec2:Subnet  default-vpc-public-0  created
 +   │  ├─ awsx:x:ec2:Subnet  default-vpc-public-1  created
 >   │  ├─ aws:ec2:Subnet     default-vpc-public-0  read
 >   │  └─ aws:ec2:Subnet     default-vpc-public-1  read
 >   └─ aws:ec2:Vpc           default-vpc           read

Outputs:
    vpcId              : "vpc-c93b06ae"
    vpcPublicSubnetIds : [
        [0]: "subnet-00412149"
        [1]: "subnet-fd19eaa6"
    ]

Resources:
    + 4 created

Duration: 6s
```

In this case, the VPC is not created and managed by Pulumi. Instead `getDefault` reads from your AWS account
and returns the VPC metadata. This object can be introspected or passed anywhere an `awsx.ec2.Vpc` is expected.

## Setting Up a New VPC

Although using the default VPC is easy, it's often not suitable for production. By setting up a dedicated VPC,
we can isolate workloads from existing ones, and have more control over subnet configuration, routing, and
controlling ingress and egress security rules.

To set up a new VPC, allocate a new `awsx.ec2.Vpc` object. This class offers a number of options, ranging from
simple defaults that many will want to start with, to complete control over everything VPC has to offer.

The following code creates a new VPC using all default settings:

```typescript
import * as awsx from "@pulumi/awsx";

// Allocate a new VPC with the default settings:
const vpc = new awsx.ec2.Vpc("custom");

// Export a few resulting fields to make them easy to use:
export const vpcId = vpc.id;
export const vpcPrivateSubnetIds = vpc.privateSubnetIds;
export const vpcPublicSubnetIds = vpc.publicSubnetIds;
```

If we run `pulumi up`, the VPC and its supporting resources will be provisioned:

```bash
$ pulumi up
Updating (dev):

     Type                                    Name                    Status
 +   pulumi:pulumi:Stack                     crosswalk-aws-dev       created
 +   ├─ awsx:x:ec2:Vpc                       custom                  created
 +   │  ├─ awsx:x:ec2:Subnet                 custom-public-0         created
 +   │  │  ├─ aws:ec2:RouteTable             custom-public-0         created
 +   │  │  ├─ aws:ec2:Subnet                 custom-public-0         created
 +   │  │  ├─ aws:ec2:Route                  custom-public-0-ig      created
 +   │  │  └─ aws:ec2:RouteTableAssociation  custom-public-0         created
 +   │  ├─ awsx:x:ec2:Subnet                 custom-public-1         created
 +   │  │  ├─ aws:ec2:RouteTable             custom-public-1         created
 +   │  │  ├─ aws:ec2:Subnet                 custom-public-1         created
 +   │  │  ├─ aws:ec2:Route                  custom-public-1-ig      created
 +   │  │  └─ aws:ec2:RouteTableAssociation  custom-public-1         created
 +   │  ├─ awsx:x:ec2:Subnet                 custom-private-0        created
 +   │  │  ├─ aws:ec2:RouteTable             custom-private-0        created
 +   │  │  ├─ aws:ec2:Subnet                 custom-private-0        created
 +   │  │  ├─ aws:ec2:RouteTableAssociation  custom-private-0        created
 +   │  │  └─ aws:ec2:Route                  custom-private-0-nat-0  created
 +   │  ├─ awsx:x:ec2:Subnet                 custom-private-1        created
 +   │  │  ├─ aws:ec2:RouteTable             custom-private-1        created
 +   │  │  ├─ aws:ec2:Subnet                 custom-private-1        created
 +   │  │  ├─ aws:ec2:RouteTableAssociation  custom-private-1        created
 +   │  │  └─ aws:ec2:Route                  custom-private-1-nat-1  created
 +   │  ├─ awsx:x:ec2:NatGateway             custom-1                created
 +   │  │  ├─ aws:ec2:Eip                    custom-1                created
 +   │  │  └─ aws:ec2:NatGateway             custom-1                created
 +   │  ├─ awsx:x:ec2:InternetGateway        custom                  created
 +   │  │  └─ aws:ec2:InternetGateway        custom                  created
 +   │  └─ awsx:x:ec2:NatGateway             custom-0                created
 +   │     ├─ aws:ec2:Eip                    custom-0                created
 +   │     └─ aws:ec2:NatGateway             custom-0                created
 +   └─ aws:ec2:Vpc                          custom                  created

Outputs:
    vpcId              : "vpc-0db13470ea4417118"
    vpcPrivateSubnetIds: [
        [0]: "subnet-046a7b24ce8c72997"
        [1]: "subnet-0cd37676da1738dcc"
    ]
    vpcPublicSubnetIds : [
        [0]: "subnet-022b9acda1e440d69"
        [1]: "subnet-0cdb12f9c04eafa68"
    ]

Resources:
    + 31 created

Duration: 1m56s
```

If unspecified, this VPC will use the following defaults:

* An IPv4 CIDR block of `10.0.0.0/16`.
* The first `2` availability zones inside of your region.
* A public and private subnet per availability zone.
* Equally partitioned CIDR address spaces per subnet (per availability zone).
* A NAT Gateway and EIP per private subnet.
* A single Internet Gateway for all public subnets to use.

The following sections show how to explicitly manage any or all of these settings.

## Configuring CIDR Blocks for a VPC

Although the default CIDR block of `10.0.0.0/16` is reasonable most of the time, it is easy to override.

> Classless Inter-Domain Routing (CIDR) is an Internet standard for specifying ranges of
> IP addresses. Please see [RFC 4632](https://tools.ietf.org/html/rfc4632) for more details.

To set our VPC's CIDR block, pass a custom `cidrBlock` argument to `awsx.ec2.Vpc`'s constructor:

```typescript
import * as awsx from "@pulumi/awsx";

// Allocate a new VPC with a smaller CIDR range:
const vpc = new awsx.ec2.Vpc("custom", {
    cidrBlock: "172.16.8.0/28",
});

// Export a few resulting fields to make them easy to use:
export const vpcId = vpc.id;
export const vpcPrivateSubnetIds = vpc.privateSubnetIds;
export const vpcPublicSubnetIds = vpc.publicSubnetIds;
```

This decreases the number of available IP addresses in our VPC from the default of 65,536 addresses (`/16` netmask) to
256 addresses (`/24` netmask), in addition to changing the IP address prefix from `10.0.0.0` to `172.16.8.0`.

> A VPC can have a minimum of 16 addresses, using the CIDR netmask `/28`, and a maximum of 65,536 addresses, using
> the netmask `/16`. The addresses are allocated across availability zones which may incur additional constraints.

In addition to configuring the CIDR block for your entire VPC, you can optionally assign a CIDR block to your
VPC's subnets. These must reside entirely within your VPC's CIDR block. If you do not explicitly specify ranges,
traffic will be evenly partitioned between availability zones within the VPC CIDR block range provided.

Please see [IP Addressing in Your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-ip-addressing.html)
for information about the full range of IP address and CIDR configuration available for your VPC.

## Configuring Availability Zones for an AWS VPC

A VPC spans all of the availability zones in your region. By default, however, the `awsx.ec2.Vpc` resource will
only use 2 of them when allocating subnets and the associated gateways. This provides fault tolerance between
two zones at a reasonable cost.

All regions support at least 2 availability zones, but many of them support more. If you'd like to improve the
fault tolerance of your configuration, simply override this with the `numberOfAvailabilityZones` argument:

```typescript
import * as awsx from "@pulumi/awsx";

// Allocate a new VPC that uses 3 availability zones, instead of 2:
const vpc = new awsx.ec2.Vpc("custom", {
    numberOfAvailabilityZones: 3,
});

// Export a few resulting fields to make them easy to use:
export const vpcId = vpc.id;
export const vpcPrivateSubnetIds = vpc.privateSubnetIds;
export const vpcPublicSubnetIds = vpc.publicSubnetIds;
```

The VPC resource will internally adjust to fully consume 3 availability zones and split traffic accordingly.

For information about regional support for availability zones, refer to AWS's
[Global Infrastructures Regions and AZs](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/) help page.

## Using All of a Region's Availability Zones for a VPC

To use all availability zones within a region, simply pass `"all"` for `numberOfAvailabilityZones`:

```typescript
import * as awsx from "@pulumi/awsx";

// Allocate a new VPC that uses all of the current region's availability zones:
const vpc = new awsx.ec2.Vpc("custom", {
    numberOfAvailabilityZones: "all",
});

// Export a few resulting fields to make them easy to use:
export const vpcId = vpc.id;
export const vpcPrivateSubnetIds = vpc.privateSubnetIds;
export const vpcPublicSubnetIds = vpc.publicSubnetIds;
```

This approach keeps your code flexibly deployable across different regions, where the number of zones may vary.

## Configuring Subnets for a VPC

A VPC spans all of the availability zones in a region. You can additionally create one or more subnets in each
availability zone, to increase your fault tolerance within a region and control routing.

By default, the `awsx.ec2.Vpc` class will allocate a public and a private subnet for each availability zone and evenly
partition traffic amongst each of them. In the event that you do not wish to keep this default, you can override
the behavior using its constructor's `subnets` argument.

For example, this program replicates the default behavior but with an explicit specification:

```typescript
import * as awsx from "@pulumi/awsx";

// Allocate a new VPC with public and private subnets per AZ:
const vpc = new awsx.ec2.Vpc("custom", {
    subnets: [{ type: "public" }, { type: "private" }],
});

// Export a few resulting fields to make them easy to use:
export const vpcId = vpc.id;
export const vpcPrivateSubnetIds = vpc.privateSubnetIds;
export const vpcPublicSubnetIds = vpc.publicSubnetIds;
```

The `subnets` argument simply takes an array of subnet specifications. Each one can include this information:

* `type`: A required type of subnet to create. There are three kinds available:
    * A `public` subnet is is one whose traffic is routed to an
    [Internet Gateway (IGW)](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html).
    * A `private` subnet is one that is configured to use a
    [NAT Gateway (NAT)](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat.html) so that it can reach the internet,
    but which prevents the internet from initiating connections to it.
    * An `isolated` subnet is one that cannot reach the internet either through an IGW or with NAT.

* `name`: An optional name to use as part of the subnet name. If not provided, the type of the subnet will be
  used. As a result, this is required when making multiple subnets of the same type.

* `cidrMask`: The number of leading bits in the VPC's CIDR block to use to define the CIDR for this specific
  subnet. By providing masking bits, this ensures each subnet has a distinct block.

* `tags`: A map of name/value pairs to tag the resulting subnet resource with.

There is no restriction on the number of subnets in an availability zone. For example, it might be useful to
have multiple isolated subnets, one for DB instances, and another for Redis instances. To facilitate this sort
of arrangements, we can use the `name` property mentioned above:

```typescript
import * as awsx from "@pulumi/awsx";

// Allocate a new VPC with a public and private subnet per AZ, plus two isolated subnets
// without Internet access, one for our DB instances and another for our Redis instances.
const vpc = new awsx.ec2.Vpc("custom", {
    subnets: [
        { type: "public" },
        { type: "private" },
        { type: "isolated", name: "db" },
        { type: "isolated", name: "redis" },
    ],
});

// Export a few resulting fields to make them easy to use:
export const vpcId = vpc.id;
export const vpcPrivateSubnetIds = vpc.privateSubnetIds;
export const vpcPublicSubnetIds = vpc.publicSubnetIds;
```

By default, the subnet CIDR ranges will be divided as evenly as possible within the VPC. If this isn't desired,
a particular size for each zone can be requested by passing in an appropriate `cidrMask` value between 16 and 28.
This value can be provided for specific subnets you know the number of instances you want IP addresses for. The
remaining IP addresses in the availability zone, if any, will be split over the subnets without a defined size.

Please refer to [VPCs and Subnets](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html) for complete
information about how VPCs and subnets relate in AWS and the configuration options available to you.

## Configuring Internet and NAT Gateways for Subnets in a VPC

By default, any VPC with public subnets will have a single Internet Gateway created for it. All public subnets will be
routable for all IPv4 addresses connections through this gateway.

To allow connections from private subnets to the internet, NAT gateways will also be created. If not specified, one
NAT Gateway will be created for each availability zone, to maximize fault tolerance. Because the NAT gateway must be
in a public subnet, NAT gateways will only be created if there is at least one public subnet.

Fewer NAT gateways can be requested (e.g., to save on costs) using the `numberOfNatGateways` property:

```typescript
import * as aws from "@pulumi/aws";
import * as awsx from "@pulumi/awsx";

// Allocate a VPC that routes all traffic through a single NAT Gateway:
const vpc = new awsx.ec2.Vpc("custom", {
   numberOfNatGateways: 1,
});

// Export a few resulting fields to make them easy to use:
export const vpcId = vpc.id;
export const vpcPrivateSubnetIds = vpc.privateSubnetIds;
export const vpcPublicSubnetIds = vpc.publicSubnetIds;
```

In the case where there is one NAT gateway per availability zone, then routing is very simple. Each private subnet
will have have connections routed through gateway in that availability zone.

In the case where there are fewer NAT gateways than availability zones, however, routing works differently. If there
are _N_ NAT gateways requested, then the first _N_ availability zones will get a NAT gateway. Routing to private subnets
in those availability zones works as above. However, all remaining availability zones will have their private subnets
routed to in a round-robin fashion from the availability zones with NAT gateways.

> Warning: While reducing the number of NAT gateways will save money, it also introduces risk as failure of one
> availability zone may impact others.

## Configuring Security Groups for a VPC

All traffic in and out of a VPC is controlled by
[Security Groups](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html), which act as virtual
firewalls that limit inbound traffic to and outbound traffic from your VPC.

For security groups, you add _rules_ that control traffic what traffic is permitted in the form of _ingress rules_ (for
inbound traffic) and _egress rules_ (outbound traffic). In addition to specifying what network protocol and ports
these rules apply to, you can also specify source and destination locations using CIDR blocks and other notations.

Each VPC has a default Security Group that disallows all ingress from any external source, and permits all outbound
traffic. This will be used by default, however you may allocate and assign resources to different groups explicitly.

Here is a program that allocates a new group with a few rules:

```typescript
import * as aws from "@pulumi/aws";
import * as awsx from "@pulumi/awsx";

// Allocate a new VPC using any of the above techniques.
const vpc = new awsx.ec2.Vpc("custom", { /*...*/ });

// Allocate a security group and then a series of rules:
const sg = new awsx.ec2.SecurityGroup("sg", { vpc });

// 1) inbound SSH traffic on port 22 from a specific IP address
sg.createIngressRule("ssh-access", {
    location: { cidrBlocks: [ "203.0.113.25/32" ] },
    ports: new awsx.ec2.TcpPorts(22),
    description: "allow SSH access to 203.0.113.25",
});

// 2) inbound HTTPS traffic on port 443 from anywhere
sg.createIngressRule("https-access", {
    location: new awsx.ec2.AnyIPv4Location(),
    ports: new awsx.ec2.TcpPorts(443),
    description: "allow HTTPS access from anywhere",
});

// 3) outbound TCP traffic on any port to anywhere
sg.createEgressRule("outbound-access", {
    location: new awsx.ec2.AnyIPv4Location(),
    ports: new awsx.ec2.AllTcpPorts(),
    description: "allow outbound access to anywhere",
});
```

This program allows all ingress traffic on port 443, only ingress from a certain IP address over SSH, and explicitly
allows all egress to any TCP destination. This code uses helpers like `AnyIPv4Location` and `TcpPorts` to cut down
on boilerplate we'd otherwise have to state by hand. We can write it out by hand if we prefer:

```typescript
import * as aws from "@pulumi/aws";
import * as awsx from "@pulumi/awsx";

// Allocate a new VPC using any of the above techniques.
const vpc = new awsx.ec2.Vpc("custom", { /*...*/ });

// Allocate a security group and then a series of rules:
const sg = new awsx.ec2.SecurityGroup("sg", { vpc });

// 1) inbound SSH traffic on port 22 from a specific IP address
sg.createIngressRule("ssh-access", {
    location: { cidrBlocks: [ "203.0.113.25/32" ] },
    ports: { protocol: "tcp", fromPort: 22 },
    description: "allow SSH access to 203.0.113.25",
});

// 2) inbound HTTPS traffic on port 443 from anywhere
sg.createIngressRule("https-access", {
    location: { cidrBlocks: [ "0.0.0.0/0" ] },
    ports: { protocol: "tcp", fromPort: 443 },
    description: "allow HTTPS access from anywhere",
});

// 3) outbound TCP traffic on any port to anywhere
sg.createEgressRule("outbound-access", {
    location: { cidrBlocks: [ "0.0.0.0/0" ] },
    ports: { protocol: "tcp", fromPort: 65535 },
    description: "allow outbound access to anywhere",
});
```

For additional details about configuring security group rules, please see the
[Security Groups for Your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html) documentation.

## Setting Up a New VPC the Hard Way

The `awsx.ec2.Vpc` component encapsulates a lot of details, including subnets, route tables, gateways, in addition to
the VPC resource itself. The `aws.ec2` package, on the other hand, out of which `Vpc` is built, provides all of these
raw resource so that you can code directly to the underlying AWS resource types, exposing every underlying capability.

For information about configuring each of these resources, please refer to each type's API documentation:

* [Vpc]({{< prelref "/docs/reference/pkg/aws/ec2/vpc" >}})
* [Subnet]({{< prelref "/docs/reference/pkg/aws/ec2/subnet" >}})
* [InternetGateway]({{< prelref "/docs/reference/pkg/aws/ec2/internetgateway" >}})
* [NatGateway]({{< prelref "/docs/reference/pkg/aws/ec2/natgateway" >}})
* [SecurityGroup]({{< prelref "/docs/reference/pkg/aws/ec2/securitygroup" >}})

These resources can be independently allocated, just as with the `Vpc` class shown above. They will need to be
connected together manually, however, which can provide greater flexibility but at a greater implementation cost.

Please note that the constituent parts, in the form of these raw resources, are available as properties on the
resulting `Vpc` class. For instance, `internetGateway` will return the Internet Gateway object for a VPC.

## Additional VPC Resources

For more information about VPCs, please read the following:

* [Amazon Virtual Private Cloud homepage](https://aws.amazon.com/vpc/)

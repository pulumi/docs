---
title_tag: "Using AWS VPC | Crosswalk"
title: VPC
h1: AWS Virtual Private Cloud (VPC)
meta_desc: Pulumi Crosswalk for AWS provides simple, out of the box VPC functionality that follows widely accepted best
           practices.
meta_image: /images/docs/meta-images/docs-clouds-aws-meta-image.png
menu:
  clouds:
    parent: aws-guides
    identifier: aws-guides-vpc
    weight: 10

aliases:
- /docs/reference/crosswalk/aws/vpc/
- /docs/guides/crosswalk/aws/vpc/
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

The [awsx.ec2.Vpc](/registry/packages/awsx/api-docs/ec2/vpc/) class encapsulates a complete
configuration of an AWS network, including the actual VPC itself, in addition to public and/or private subnets, route
tables, and gateways, across multiple availability zones. It is designed to be easier to use, with reasonable defaults,
and follows AWS's own best practices, with configurability for advanced scenarios. The two can be used together.

Below are some of the most common infrastructure as code tasks with VPCs.

## Getting the Default VPC

Often resources like clusters, API gateways, lambdas, and more, will request a VPC object or ID. This ensures
such resources inside of your VPC so network traffic are isolated from other VPCs in your account.

Each AWS account has a default VPC per region. Using the default VPC is often the easiest path when you're just getting up and running or don't yet understand your specific networking requirements. Most resources will use this default VPC automatically if you leave it unspecified. In other cases, you may be required to pass it explicitly, in which case you'll need to get it programmatically.

The following example will [read the default VPC](https://www.pulumi.com/registry/packages/awsx/api-docs/ec2/defaultvpc/) and export some of its properties for easy consumption.

{{< example-program path="awsx-vpc-default" >}}

Once you have defined this function, running `pulumi up` will show:

```bash
$ pulumi up

Updating (dev)

     Type                    Name          Status
 +   pulumi:pulumi:Stack     awsx-vpc-dev  created (2s)
 +   └─ awsx:ec2:DefaultVpc  default-vpc   created (0.49s)

Outputs:
    privateSubnetIds: [
        [0]: "subnet-0b4f9fb1df1543b07"
    ]
    publicSubnetIds : [
        [0]: "subnet-43f43a1e"
        [1]: "subnet-c7d926bf"
        [2]: "subnet-d7e7fe9c"
    ]
    vpcId           : "vpc-4b82e033"

Resources:
    + 2 created

Duration: 3s
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

{{< example-program path="awsx-vpc" >}}

If we run `pulumi up`, the VPC and its supporting resources will be provisioned:

```bash
$ pulumi up

Updating (dev)

     Type                                          Name           Status
 +   pulumi:pulumi:Stack                           awsx-vpc-dev   created (146s)
 +   └─ awsx:ec2:Vpc                               vpc            created (0.79s)
 +      └─ aws:ec2:Vpc                             vpc            created (1s)
 +         ├─ aws:ec2:Subnet                       vpc-private-3  created (0.95s)
 +         │  └─ aws:ec2:RouteTable                vpc-private-3  created (0.72s)
 +         │     ├─ aws:ec2:RouteTableAssociation  vpc-private-3  created (0.75s)
 +         │     └─ aws:ec2:Route                  vpc-private-3  created (1s)
 +         ├─ aws:ec2:Subnet                       vpc-public-1   created (11s)
 +         │  ├─ aws:ec2:Eip                       vpc-1          created (0.93s)
 +         │  ├─ aws:ec2:RouteTable                vpc-public-1   created (1s)
 +         │  │  ├─ aws:ec2:RouteTableAssociation  vpc-public-1   created (1s)
 +         │  │  └─ aws:ec2:Route                  vpc-public-1   created (1s)
 +         │  └─ aws:ec2:NatGateway                vpc-1          created (95s)
 +         ├─ aws:ec2:Subnet                       vpc-public-3   created (11s)
 +         │  ├─ aws:ec2:RouteTable                vpc-public-3   created (1s)
 +         │  │  ├─ aws:ec2:Route                  vpc-public-3   created (1s)
 +         │  │  └─ aws:ec2:RouteTableAssociation  vpc-public-3   created (1s)
 +         │  ├─ aws:ec2:Eip                       vpc-3          created (1s)
 +         │  └─ aws:ec2:NatGateway                vpc-3          created (125s)
 +         ├─ aws:ec2:Subnet                       vpc-public-2   created (11s)
 +         │  ├─ aws:ec2:Eip                       vpc-2          created (1s)
 +         │  ├─ aws:ec2:RouteTable                vpc-public-2   created (1s)
 +         │  │  ├─ aws:ec2:Route                  vpc-public-2   created (1s)
 +         │  │  └─ aws:ec2:RouteTableAssociation  vpc-public-2   created (1s)
 +         │  └─ aws:ec2:NatGateway                vpc-2          created (95s)
 +         ├─ aws:ec2:Subnet                       vpc-private-1  created (1s)
 +         │  └─ aws:ec2:RouteTable                vpc-private-1  created (1s)
 +         │     ├─ aws:ec2:RouteTableAssociation  vpc-private-1  created (0.51s)
 +         │     └─ aws:ec2:Route                  vpc-private-1  created (1s)
 +         ├─ aws:ec2:Subnet                       vpc-private-2  created (2s)
 +         │  └─ aws:ec2:RouteTable                vpc-private-2  created (1s)
 +         │     ├─ aws:ec2:RouteTableAssociation  vpc-private-2  created (0.72s)
 +         │     └─ aws:ec2:Route                  vpc-private-2  created (1s)
 +         └─ aws:ec2:InternetGateway              vpc            created (2s)

Outputs:
    privateSubnetIds: [
        [0]: "subnet-0b5f7a7f8a4a88d51"
        [1]: "subnet-03dac3c6561fe7140"
        [2]: "subnet-089ba98ecf74614c0"
    ]
    publicSubnetIds : [
        [0]: "subnet-02783beae211c9bab"
        [1]: "subnet-0460f52b1c1786dee"
        [2]: "subnet-0afa4ac06444be3c5"
    ]
    vpcId           : "vpc-0bba07367def55a87"

Resources:
    + 34 created

Duration: 2m27s
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

{{< example-program path="awsx-vpc-cidr" >}}

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
only use 3 of them when allocating subnets and the associated gateways. This provides fault tolerance between
three zones at a reasonable cost.

All regions support at least 3 availability zones, but many of them support more. If you'd like to improve the fault tolerance of your configuration, override this with the `numberOfAvailabilityZones` argument:

{{< example-program path="awsx-vpc-azs" >}}

The VPC resource will internally adjust to fully consume 4 availability zones and split traffic accordingly.

{{% notes type="info" %}}

If creating a VPC with the availability zone configuration set to 4 or higher, please ensure you are deploying in a region that supports more than 3 availability zones.

{{% /notes %}}

For information about regional support for availability zones, refer to AWS's
[Global Infrastructures Regions and AZs](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/) help page.

## Configuring Subnets for a VPC

A VPC spans all of the availability zones in a region. You can additionally create one or more subnets in each
availability zone, to increase your fault tolerance within a region and control routing.

By default, the `awsx.ec2.Vpc` class will allocate a public and a private subnet for each availability zone and evenly
partition traffic amongst each of them. In the event that you do not wish to keep this default, you can override
the behavior using its constructor's `subnets` argument.

For example, this program replicates the default behavior but with an explicit specification:

{{< example-program path="awsx-vpc-subnets" >}}

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

{{< example-program path="awsx-vpc-nat-gateways" >}}

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

For security groups, you add _rules_ that control how traffic is permitted in the form of _ingress rules_ (for
inbound traffic) and _egress rules_ (outbound traffic). In addition to specifying what network protocol and ports
these rules apply to, you can also specify source and destination locations using CIDR blocks and other notations.

Each VPC has a default security group that disallows all ingress from any external source, and permits all outbound
traffic. This will be used by default, however you may allocate and assign resources to different groups explicitly.

Here is a program that allocates a new group with a few rules:

{{< example-program path="awsx-vpc-security-groups" >}}

For additional details about configuring security group rules, See the
[Security Groups for Your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html) documentation.

## How to use your VPC, Security Group, and EC2 instance

This example shows how to deploy an EC2 instance using a VPC and security group provisioned with the Crosswalk for AWS component:

{{< example-program path="awsx-vpc-sg-ec2" >}}

If we run `pulumi up`, the `aws.ec2.Instance` will be provisioned using the _first_ public subnet from the `awsx.ec2.Vpc` component and the security group provisioned with the `awsx.ec2.SecurityGroup` component:

```bash
$ pulumi up

Updating (dev)

     Type                                          Name           Status
 +   pulumi:pulumi:Stack                           awsx-vpc-dev   created (166s)
 +   ├─ awsx:ec2:Vpc                               vpc            created (0.66s)
 +   │  └─ aws:ec2:Vpc                             vpc            created (1s)
 +   │     ├─ aws:ec2:Subnet                       vpc-private-2  created (0.97s)
 +   │     │  └─ aws:ec2:RouteTable                vpc-private-2  created (0.81s)
 +   │     │     ├─ aws:ec2:RouteTableAssociation  vpc-private-2  created (0.77s)
 +   │     │     └─ aws:ec2:Route                  vpc-private-2  created (1s)
 +   │     ├─ aws:ec2:InternetGateway              vpc            created (0.94s)
 +   │     ├─ aws:ec2:Subnet                       vpc-public-1   created (11s)
 +   │     │  ├─ aws:ec2:RouteTable                vpc-public-1   created (0.85s)
 +   │     │  │  ├─ aws:ec2:RouteTableAssociation  vpc-public-1   created (1s)
 +   │     │  │  └─ aws:ec2:Route                  vpc-public-1   created (2s)
 +   │     │  ├─ aws:ec2:Eip                       vpc-1          created (1s)
 +   │     │  └─ aws:ec2:NatGateway                vpc-1          created (85s)
 +   │     ├─ aws:ec2:Subnet                       vpc-private-1  created (1s)
 +   │     │  └─ aws:ec2:RouteTable                vpc-private-1  created (0.97s)
 +   │     │     ├─ aws:ec2:RouteTableAssociation  vpc-private-1  created (0.94s)
 +   │     │     └─ aws:ec2:Route                  vpc-private-1  created (1s)
 +   │     ├─ aws:ec2:Subnet                       vpc-public-2   created (11s)
 +   │     │  ├─ aws:ec2:RouteTable                vpc-public-2   created (1s)
 +   │     │  │  ├─ aws:ec2:RouteTableAssociation  vpc-public-2   created (1s)
 +   │     │  │  └─ aws:ec2:Route                  vpc-public-2   created (1s)
 +   │     │  ├─ aws:ec2:Eip                       vpc-2          created (1s)
 +   │     │  └─ aws:ec2:NatGateway                vpc-2          created (146s)
 +   │     ├─ aws:ec2:Subnet                       vpc-public-3   created (12s)
 +   │     │  ├─ aws:ec2:Eip                       vpc-3          created (1s)
 +   │     │  ├─ aws:ec2:RouteTable                vpc-public-3   created (1s)
 +   │     │  │  ├─ aws:ec2:RouteTableAssociation  vpc-public-3   created (1s)
 +   │     │  │  └─ aws:ec2:Route                  vpc-public-3   created (1s)
 +   │     │  └─ aws:ec2:NatGateway                vpc-3          created (95s)
 +   │     └─ aws:ec2:Subnet                       vpc-private-3  created (2s)
 +   │        └─ aws:ec2:RouteTable                vpc-private-3  created (0.70s)
 +   │           ├─ aws:ec2:RouteTableAssociation  vpc-private-3  created (13s)
 +   │           └─ aws:ec2:Route                  vpc-private-3  created (1s)
 +   ├─ aws:ec2:SecurityGroup                      group          created (2s)
 +   └─ aws:ec2:Instance                           instance       created (32s)

Outputs:
    vpcId: "vpc-02d379aaaa281f99d"

Resources:
    + 36 created
```

## Setting Up a New VPC the Hard Way

The `awsx.ec2.Vpc` component encapsulates a lot of details, including subnets, route tables, gateways, in addition to
the VPC resource itself. The `aws.ec2` package, on the other hand, out of which `Vpc` is built, provides all of these
raw resources so that you can code directly to the underlying AWS resource types, exposing every supported capability.

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

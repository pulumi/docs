---

title: Managed Infrastructure

aliases: ["/docs/guides/crosswalk/kubernetes/aws/managed-infra/"]
---

AWS has a catalog of [managed infrastructure][aws-managed-svcs] services that
support and complement Kubernetes clusters and their workloads.

At a minimum, networking must be configured for deployment of an EKS cluster.

AWS exposes a [Virtual Private Cloud][aws-vpc] API which can be used to create
resources into a virtual network. With the VPC you can define the region's [Availability
Zones][aws-azs] to use, alongwith [Route Tables][aws-rts], [Subnets][aws-subnets], [Internet Gateways][aws-igw],
[NAT Gateways][aws-ngw] and [Security Groups][aws-sgs].

In [Crosswalk for AWS][crosswalk-aws] we showcase how to define networking:

  - [VPCs][vpc]
  - [Availability Zones][vpc-azs]
  - [Subnets][vpc-subnets]
  - [Internet & NAT Gateways][vpc-gw]
  - [Security Groups][vpc-sg]

The full code for this stack is on [GitHub][gh-repo-stack].

## Creating a New VPC for Kubernetes

Create a new VPC to use with the cluster that uses custom settings and best-practice
defaults.

```typescript
import * as awsx from "@pulumi/awsx";

// Create a new VPC with custom settings.
const vpcName = "eksVpc";
const vpc = new awsx.ec2.Vpc(vpcName, {
    cidrBlock: "172.16.0.0/16",
    numberOfAvailabilityZones: "all",
    tags: { "Name": vpcName },
});

// Export the VPC resource IDs.
export const vpcId = vpc.id;
export const publicSubnetIds = vpc.publicSubnetIds;
export const privateSubnetIds = vpc.privateSubnetIds;
```

## Using the Default VPC with Kubernetes

Use the AWS account's default VPC.

Ensure the network is [properly configured](#network-configuration).

```typescript
import * as awsx from "@pulumi/awsx";

// Use the default VPC.
const defaultVpc = awsx.ec2.Vpc.getDefault();

// Export the VPC resource IDs.
export const defaultVpcId = defaultVpc.id;
export const defaultPublicSubnetIds = defaultVpc.publicSubnetIds;
export const defaultPrivateSubnetIds = defaultVpc.privateSubnetIds;
```

## Using an Existing VPC with Kubernetes

To use an existing VPC with EKS, provide the IDs of the VPC and its resources.

Ensure the network is [properly configured](#network-configuration).

```typescript
import * as awsx from "@pulumi/awsx";

// Use an existing VPC, subnets, and gateways.
const existingVpc = awsx.ec2.Vpc.fromExistingIds("existingVpc", {
    vpcId: "vpc-00000000000000000",
    publicSubnetIds: ["subnet-00000000000000000", "subnet-11111111111111111"],
    privateSubnetIds: ["subnet-22222222222222222", "subnet-33333333333333333"],
    internetGatewayId: "igw-00000000000000000",
    natGatewayIds: ["nat-00000000000000000", "nat-11111111111111111"],
})

// Export the VPC resource IDs.
export const existingVpcId = existingVpc.id;
export const existingPublicSubnetIds = existingVpc.publicSubnetIds;
export const existingPrivateSubnetIds = existingVpc.privateSubnetIds;
```

## Network Configuration

[Requirements](https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html)

  * Must have DNS hostname enabled.
  * Must have DNS resolution enabled.
  * Subnets in at least 2 Availability Zones of the region (use of all region AZs is strongly recommended).

[Recommendations](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Scenario2.html)

  * Subnets
    * Workers use private subnets (strongly recommended).
    * Public subnets exist for NAT gateways.
    * Public subnets exist and are [tagged][eks-tagging] for use with public load balancers in Kubernetes.
    * Private subnets exist and are [tagged](https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html#vpc-subnet-tagging ) for use with private load balancers in Kubernetes.
  * Attach an Internet Gateway to the VPC for Internet access.
  * Attach a NAT Gateway to a public subnet such that private subnet instances
    can route to the Internet.


[crosswalk-aws]: /docs/guides/crosswalk/aws

[aws-managed-svcs]: https://aws.amazon.com/products/
[aws-vpc]: https://aws.amazon.com/vpc/
[aws-azs]: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html
[aws-rts]: https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html
[aws-subnets]: https://docs.aws.amazon.com/vpc/latest/userguide/working-with-vpcs.html
[aws-igw]: https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html
[aws-ngw]: https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html
[aws-sgs]: https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html

[vpc]: /docs/guides/crosswalk/aws/vpc/#setting-up-a-new-vpc
[vpc-azs]: /docs/guides/crosswalk/aws/vpc/#configuring-availability-zones-for-an-aws-vpc
[vpc-subnets]: /docs/guides/crosswalk/aws/vpc/#configuring-subnets-for-a-vpc
[vpc-gw]: /docs/guides/crosswalk/aws/vpc/#configuring-internet-and-nat-gateways-for-subnets-in-a-vpc
[vpc-sg]: /docs/guides/crosswalk/aws/vpc/#configuring-security-groups-for-a-vpc

[eks-tagging]: https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html#vpc-subnet-tagging
[gh-repo-stack]: https://github.com/metral/kubernetes-the-prod-way/tree/metral/crosswalk/aws/02-networking

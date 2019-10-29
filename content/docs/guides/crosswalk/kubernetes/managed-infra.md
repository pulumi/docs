---
title: Managed Infrastructure
linktitle: Managed Infrastructure
---

{{< cloudchoose >}}

<div class="cloud-prologue-aws"></div>
<div class="mt">
{{% md %}}

AWS has a catalog of [managed infrastructure][aws-managed-svcs] services that
support and complement Kubernetes clusters and their workloads.

At a minimum, networking must be configured for deployment of an EKS cluster.

AWS exposes a [Virtual Private Cloud][aws-vpc] API which can be used to create
resources into a virtual network. With the VPC you can define the region's [Availability
Zones][aws-azs] to use, alongwith [Route Tables][aws-rts], [Subnets][aws-subnets], [Internet Gateways][aws-igw],
[NAT Gateways][aws-ngw] and [Security Groups][aws-sgs].

The full code for this stack is on [GitHub][gh-repo-stack].

[gh-repo-stack]: https://github.com/pulumi/kubernetes-the-prod-way/tree/crosswalk/aws/02-managed-infra
[crosswalk-aws]: {{< relref "/docs/guides/crosswalk/aws" >}}
[aws-managed-svcs]: https://aws.amazon.com/products/
[aws-vpc]: https://aws.amazon.com/vpc/
[aws-azs]: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html
[aws-rts]: https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html
[aws-subnets]: https://docs.aws.amazon.com/vpc/latest/userguide/working-with-vpcs.html
[aws-igw]: https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html
[aws-ngw]: https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html
[aws-sgs]: https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html
{{% /md %}}
</div>

<div class="cloud-prologue-azure"></div>
<div class="mt">
{{% md %}}

Azure has a catalog of [managed infrastructure][azure-managed-svcs] services that
support and complement Kubernetes clusters and their workloads.

At a minimum, networking must be configured for deployment of an AKS cluster.

AWS exposes a [Virtual Network][azure-vpc] API which can be used to create
resources into a virtual network. With the VPC you can define
use, alongwith [Route Tables][azure-rts], [Subnets][azure-subnets],
[Security Groups][azure-sgs] and [VPN Gateways][azure-vpn-gw].

The full code for this stack is on [GitHub][gh-repo-stack].

[azure-managed-svcs]: https://azure.microsoft.com/en-us/services/
[azure-vpc]: https://azure.microsoft.com/en-us/services/
[azure-subnets]: https://docs.microsoft.com/en-us/azure/virtual-network/virtual-network-vnet-plan-design-arm#subnets
[azure-rts]: https://docs.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview#user-defined
[azure-sgs]: https://docs.microsoft.com/en-us/azure/virtual-network/virtual-network-vnet-plan-design-arm#security
[azure-vpn-gw]: https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-vnet-vnet-rm-ps
[gh-repo-stack]: https://github.com/pulumi/kubernetes-the-prod-way/tree/crosswalk/azure/02-managed-infra
{{% /md %}}
</div>

<div class="cloud-prologue-gcp"></div>
<div class="mt">
{{% md %}}

TODO

The full code for this stack is on [GitHub][gh-repo-stack].

[gh-repo-stack]: https://github.com/pulumi/kubernetes-the-prod-way/tree/crosswalk/gcp/02-managed-infra
{{% /md %}}
</div>

## Overview

We'll configure and deploy:

  * [Networking](#networking): To provide a virtual network for the cluster to
    use.
  cluster users, and worker nodes.
  * [Storage](#storage): To provide data stores for the cluster.

## Networking

<div class="cloud-prologue-aws"></div>
<div class="mt">
{{% md %}}

In [Crosswalk for AWS][crosswalk-aws] we showcase how to define networking:

  - [VPCs][vpc]
  - [Availability Zones][vpc-azs]
  - [Subnets][vpc-subnets]
  - [Internet & NAT Gateways][vpc-gw]
  - [Security Groups][vpc-sg]

### Create a New VPC for Kubernetes

Create a new VPC to use with the cluster that uses custom settings and
best-practice defaults.

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
[crosswalk-aws]: {{< relref "/docs/guides/crosswalk/aws" >}}
[vpc]: {{< relref "/docs/guides/crosswalk/aws/vpc#setting-up-a-new-vpc" >}}
[vpc-azs]: {{< relref "/docs/guides/crosswalk/aws/vpc#configuring-availability-zones-for-an-aws-vpc" >}}
[vpc-subnets]: {{< relref "/docs/guides/crosswalk/aws/vpc#configuring-subnets-for-a-vpc" >}}
[vpc-gw]: {{< relref "/docs/guides/crosswalk/aws/vpc#configuring-internet-and-nat-gateways-for-subnets-in-a-vpc" >}}
[vpc-sg]: {{< relref "/docs/guides/crosswalk/aws/vpc#configuring-security-groups-for-a-vpc" >}}
{{% /md %}}
</div>

<div class="cloud-prologue-azure"></div>
<div class="mt">
{{% md %}}

### Create a New Virtual Network for Kubernetes

Create a new Virtual Network to use with the cluster that uses custom settings and
best-practice defaults.

```typescript
// Create a Virtual Network for the cluster.
const vnet = new azure.network.VirtualNetwork(name, {
    resourceGroupName: config.resourceGroupName,
    addressSpaces: ["10.2.0.0/16"],
});

// Create a Subnet for the cluster.
const subnet = new azure.network.Subnet(name, {
    resourceGroupName: config.resourceGroupName,
    virtualNetworkName: vnet.name,
    addressPrefix: "10.2.1.0/24",
});
```

{{% /md %}}
</div>

<div class="cloud-prologue-gcp"></div>
<div class="mt">
{{% md %}}

TODO

### Create a New VPC for Kubernetes

Create a new VPC to use with the cluster that uses custom settings and
best-practice defaults.

```typescript
// TODO
```

{{% /md %}}
</div>

### Use the Default VPC with Kubernetes

<div class="cloud-prologue-aws"></div>
<div class="mt">
{{% md %}}

Use the account's default VPC.

```typescript
import * as awsx from "@pulumi/awsx";

// Use the default VPC.
const defaultVpc = awsx.ec2.Vpc.getDefault();

// Export the VPC resource IDs.
export const defaultVpcId = defaultVpc.id;
export const defaultPublicSubnetIds = defaultVpc.publicSubnetIds;
export const defaultPrivateSubnetIds = defaultVpc.privateSubnetIds;
```

{{% /md %}}
</div>

<div class="cloud-prologue-azure"></div>
<div class="mt">
{{% md %}}

Use the account's default VPC.

```typescript
// TODO
```

{{% /md %}}
</div>

<div class="cloud-prologue-gcp"></div>
<div class="mt">
{{% md %}}

Use the account's default VPC.

```typescript
// TODO
```

{{% /md %}}
</div>

### Use an Existing VPC with Kubernetes

<div class="cloud-prologue-aws"></div>
<div class="mt">
{{% md %}}

To use an existing VPC, provide the IDs of the VPC and its resources.

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
{{% /md %}}
</div>

<div class="cloud-prologue-azure"></div>
<div class="mt">
{{% md %}}

To use an existing VPC, provide the IDs of the VPC and its resources.

```typescript
// TODO
```

{{% /md %}}
</div>

<div class="cloud-prologue-gcp"></div>
<div class="mt">
{{% md %}}

To use an existing VPC, provide the IDs of the VPC and its resources.

```typescript
// TODO
```

{{% /md %}}
</div>

### Requirements & Recommendations

<div class="cloud-prologue-aws"></div>
<div class="mt">
{{% md %}}

See the official docs [EKS Network Requirements](https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html)
and [AWS VPC Recommendations](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Scenario2.html) for more details.

[eks-tagging]: https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html#vpc-subnet-tagging
{{% /md %}}
</div>

<div class="cloud-prologue-azure"></div>
<div class="mt">
{{% md %}}

See the official Networking [docs][azure-net-docs] for more details.

[azure-net-docs]: https://docs.microsoft.com/en-us/azure/aks/concepts-network
{{% /md %}}
</div>

<div class="cloud-prologue-gcp"></div>
<div class="mt">
{{% md %}}

TODO

{{% /md %}}
</div>

## Storage

Cloud storage persists data in many forms, from data warehouses to analytics,
and is presented as object, file, block storage, and migration capabilities.

Generally, the storage services in this stack tend to be foundational for
teams, and is typically shared across clusters and orgs.

In the managed clusters, the worker node groups by default will use block devices,
and Kubernetes itself could manage [PersistentVolumes][k8s-pvs].

Often times, this layer may be conflated with storage services managed in stacks
closer to the apps, such as the Kubernetes [Cluster Services][crosswalk-cluster-svcs]
or [App Services][crosswalk-app-svcs]. Those higher layers tend to primarily focus on
the direct needs of a **given** Kubernetes cluster and its apps, rather than the
needs of your complete architecture.

<div class="cloud-prologue-aws"></div>
<div class="mt">
{{% md %}}

## Amazon Simple Storage Service (S3)

See [Crosswalk AWS S3][pulumi-s3] and the [AWS S3 docs][aws-s3] for more details.

## Elastic Container Registry (ECR)

See [Crosswalk AWS ECR][crosswalk-ecr] and the [AWS ECR docs][aws-ecr] for more details.

## Amazon Elastic File System (EFS)

See [Persisting Kubernetes Workloads with Amazon EFS][pulumi-efs] and the
[AWS EFS docs][aws-efs] for more details.

[pulumi-efs]: {{< relref "/blog/persisting-kubernetes-workloads-with-amazon-efscsi-volumes-using-pulumi-sdks" >}}
[aws-efs]: https://aws.amazon.com/efs/
[pulumi-s3]: {{< relref "/docs/aws/s3" >}}
[crosswalk-ecr]: {{< relref "/docs/guides/crosswalk/aws/ecr" >}}
[aws-ecr]: https://aws.amazon.com/ecr/
[aws-s3]: https://aws.amazon.com/s3
{{% /md %}}
</div>

<div class="cloud-prologue-azure"></div>
<div class="mt">
{{% md %}}

## Azure Object Storage

```typescript
import * as azure from "@pulumi/azure";

// Create an Azure Resource Group.
const resourceGroup = new azure.core.ResourceGroup("website-rg", {
    location: azure.Locations.WestUS,
});

// Create a Storage Account.
const storageAccount = new azure.storage.Account("websitesa", {
    resourceGroupName: resourceGroup.name,
    accountReplicationType: "LRS",
    accountTier: "Standard",
    accountKind: "StorageV2",
});

// Upload the following files from a local directory.
["index.html", "404.html"].map(name =>
    new azure.storage.Blob(name, {
        name,
        resourceGroupName: resourceGroup.name,
        storageAccountName: storageAccount.name,
        storageContainerName: "wwwroot",
        type: "block",
        source: `./wwwroot/${name}`,
        contentType: "text/html",
    }),
);
```
## Azure Container Registry (ACR)

```typescript
import * as azure from "@pulumi/azure";

// Create an Azure Resource Group.
const resourceGroup = new azure.core.ResourceGroup("rg", {
    location: "West US",
    name: "resourceGroup1",
});

// Create an ACR.
const acr = new azure.containerservice.Registry("acr", {
    adminEnabled: false,
    georeplicationLocations: [
        "East US",
        "West Europe",
    ],
    location: resourceGroup.location,
    name: "containerRegistry1",
    resourceGroupName: resourceGroup.name,
    sku: "Premium",
});
```

{{% /md %}}
</div>

<div class="cloud-prologue-gcp"></div>
<div class="mt">
{{% md %}}

TODO

```typescript
TODO
```

{{% /md %}}
</div>

[crosswalk-cluster-svcs]: {{< relref "/docs/guides/crosswalk/kubernetes/cluster-services" >}}
[crosswalk-app-svcs]: {{< relref "/docs/guides/crosswalk/kubernetes/app-services" >}}
[k8s-pvs]: https://kubernetes.io/docs/concepts/storage/persistent-volumes/

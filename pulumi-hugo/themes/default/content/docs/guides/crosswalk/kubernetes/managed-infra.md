---
title_tag: Managed Infrastructure Services for Kubernetes | Crosswalk
title: Managed Infrastructure Services for Kubernetes
meta_desc: This page provides an overview of Managed Infrastructure services that
           support and complement Kubernetes clusters and workloads.
linktitle: Managed Infrastructure
---

{{< chooser cloud "aws,azure,gcp" / >}}

{{% choosable cloud aws %}}

AWS has a catalog of [managed infrastructure][aws-managed-svcs] services that
support and complement Kubernetes clusters and their workloads.

At a minimum, networking must be configured for deployment of an EKS cluster.

AWS exposes a [Virtual Private Cloud][aws-vpc] API which can be used to create
resources into a virtual network. With the VPC you can define the region's [Availability
Zones][aws-azs] to use, alongwith [Route Tables][aws-rts], [Subnets][aws-subnets], [Internet Gateways][aws-igw],
[NAT Gateways][aws-ngw] and [Security Groups][aws-sgs].

The full code for this stack is on [GitHub][gh-repo-stack].

<!-- markdownlint-disable url -->
[gh-repo-stack]: https://github.com/pulumi/kubernetes-guides/tree/master/aws/02-managed-infra
[crosswalk-aws]: /docs/guides/crosswalk/aws/
[aws-managed-svcs]: https://aws.amazon.com/products/
[aws-vpc]: https://aws.amazon.com/vpc/
[aws-azs]: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html
[aws-rts]: https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html
[aws-subnets]: https://docs.aws.amazon.com/vpc/latest/userguide/working-with-vpcs.html
[aws-igw]: https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html
[aws-ngw]: https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html
[aws-sgs]: https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html
<!-- markdownlint-enable url -->

{{% /choosable %}}

{{% choosable cloud azure %}}

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
[gh-repo-stack]: https://github.com/pulumi/kubernetes-guides/tree/master/azure/02-managed-infra

{{% /choosable %}}

{{% choosable cloud gcp %}}

GCP has a catalog of [managed infrastructure][gcp-managed-svcs] services that
support and complement Kubernetes clusters and their workloads.

At a minimum, networking must be configured for deployment of an EKS cluster.

GCP exposes a [Virtual Private Cloud][gcp-vpc] API which can be used to create
resources into a virtual network. With the VPC you can define the region to use,
alongwith [Routes][gcp-rts], [Subnets][gcp-subnets], [Forwarding Rules][gcp-fwd-rules],
and [Firewall Rules][gcp-fw-rules].

The full code for this stack is on [GitHub][gh-repo-stack].

<!-- markdownlint-disable url -->
[gcp-managed-svcs]: https://cloud.google.com/products/
[gcp-subnets]: https://cloud.google.com/vpc/docs/vpc#vpc_networks_and_subnets
[gcp-fwd-rules]: https://cloud.google.com/compute/docs/protocol-forwarding
[gcp-vpc]: https://cloud.google.com/vpc/docs/overview
[gcp-rts]: https://cloud.google.com/vpc/docs/routes
[gcp-fw-rules]: https://cloud.google.com/vpc/docs/firewalls
[gh-repo-stack]: https://github.com/pulumi/kubernetes-guides/tree/master/gcp/02-managed-infra
<!-- markdownlint-enable url -->

{{% /choosable %}}

## Overview

We'll configure and deploy:

* [Networking](#networking): To provide a virtual network for the cluster.
* [Storage](#storage): To provide data stores for the cluster.

## Networking

{{% choosable cloud aws %}}

In [Crosswalk for AWS][crosswalk-aws] we showcase how to define networking:

* [VPCs][vpc]
* [Availability Zones][vpc-azs]
* [Subnets][vpc-subnets]
* [Internet & NAT Gateways][vpc-gw]
* [Security Groups][vpc-sg]

### Create a New VPC for Kubernetes

Create a new VPC to use with the cluster with custom settings and
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

[crosswalk-aws]: /docs/guides/crosswalk/aws/
[vpc]: /docs/guides/crosswalk/aws/vpc/#setting-up-a-new-vpc
[vpc-azs]: /docs/guides/crosswalk/aws/vpc/#configuring-availability-zones-for-an-aws-vpc
[vpc-subnets]: /docs/guides/crosswalk/aws/vpc/#configuring-subnets-for-a-vpc
[vpc-gw]: /docs/guides/crosswalk/aws/vpc/#configuring-internet-and-nat-gateways-for-subnets-in-a-vpc
[vpc-sg]: /docs/guides/crosswalk/aws/vpc/#configuring-security-groups-for-a-vpc

{{% /choosable %}}

{{% choosable cloud azure %}}

### Create a New Virtual Network for Kubernetes

Create a new Virtual Network to use with the cluster with custom settings and
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

{{% /choosable %}}

{{% choosable cloud gcp %}}

<!-- markdownlint-disable no-duplicate-heading -->
### Create a New VPC for Kubernetes
<!-- markdownlint-enable no-duplicate-heading -->

Create a new network to use with the cluster with custom settings and
best-practice defaults.

```typescript
import * as gcp from "@pulumi/gcp";

const network = new gcp.compute.Network(name, {
    project: config.project,
    autoCreateSubnetworks: false,
});
export const networkName = network.name;

const subnet = new gcp.compute.Subnetwork(name, {
    project: config.project,
    region: pulumi.output(config.zone).apply(zone =>
        (<string>zone)
            .split("-")
            .slice(0, 2)
            .join("-"),
    ),
    ipCidrRange: "10.0.0.0/24",
    network: network.name,
    secondaryIpRanges: [{ rangeName: "pods", ipCidrRange: "10.1.0.0/16" }],
});
export const subnetworkName = subnet.name;
```

{{% /choosable %}}

{{% choosable cloud aws %}}

#### Use the Default VPC with Kubernetes

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

{{% /choosable %}}

{{% choosable cloud aws %}}

#### Use an Existing VPC with Kubernetes

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

{{% /choosable %}}

### Requirements & Recommendations

{{% choosable cloud aws %}}

See the official docs [EKS Network Requirements](https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html)
and [AWS VPC Recommendations](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Scenario2.html) for more details.

[eks-tagging]: https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html#vpc-subnet-tagging

{{% /choosable %}}

{{% choosable cloud azure %}}

See the official Networking [docs][azure-net-docs] for more details.

[azure-net-docs]: https://docs.microsoft.com/en-us/azure/aks/concepts-network
{{% /choosable %}}

{{% choosable cloud gcp %}}

See the official Networking [docs][gke-net-docs] for more details.

[gke-net-docs]: https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-admin-overview

{{% /choosable %}}

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

{{% choosable cloud aws %}}

### Amazon Simple Storage Service (S3)

See [Crosswalk AWS S3][pulumi-s3] and the [AWS S3 docs][aws-s3] for more details.

### Elastic Container Registry (ECR)

See [Crosswalk AWS ECR][crosswalk-ecr] and the [AWS ECR docs][aws-ecr] for more details.

### Amazon Elastic File System (EFS)

See [Persisting Kubernetes Workloads with Amazon EFS][pulumi-efs] and the
[AWS EFS docs][aws-efs] for more details.

<!-- markdownlint-disable url -->
[pulumi-efs]: /blog/persisting-kubernetes-workloads-with-amazon-efscsi-volumes-using-pulumi-sdks/
[aws-efs]: https://aws.amazon.com/efs/
[pulumi-s3]: /docs/aws/s3/
[crosswalk-ecr]: /docs/guides/crosswalk/aws/ecr/
[aws-ecr]: https://aws.amazon.com/ecr/
[aws-s3]: https://aws.amazon.com/s3
<!-- markdownlint-enable url -->

{{% /choosable %}}

{{% choosable cloud azure %}}

### Azure Blob Storage

Create a new blob storage with a data source of a local directory and files.

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

### Azure Container Registry (ACR)

Create a new registry, build a local Docker image, and push it to the registry.

```typescript
import * as azure from "@pulumi/azure";

// Create an Azure Resource Group.
const resourceGroup = new azure.core.ResourceGroup("rg", {
    location: "West US",
    name: "resourceGroup1",
});

// Create an ACR.
const registry = new azure.containerservice.Registry("acr", {
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

// Build a local Docker image with a given Dockerfile context, and push it
// to the registry.
const customImage = "node-app";
const appImage = new docker.Image(customImage, {
    imageName: pulumi.interpolate`${registry.loginServer}/${customImage}:v1.0.0`,
    build: {
        context: `./${customImage}`,
    },
    registry: {
        server: registry.loginServer,
        username: registry.adminUsername,
        password: registry.adminPassword,
    },
});
```

{{% /choosable %}}

{{% choosable cloud gcp %}}

### Google Container Registry (GCR)

Fetch the URL to use for the Debian container image.

```typescript
import * as gcp from "@pulumi/gcp";

const debian = gcp.container.getRegistryImage({
    name: "debian",
});

export const gcrLocation = debian.imageUrl;
```

Fetch the project's registry and display its GCR location.

```ts
import * as gcp from "@pulumi/gcp";

const registry = gcp.container.getRegistryRepository();
export const gcrLocation = registry.repositoryUrl;
```

Build a local Docker image with a given Dockerfile context, and push it to the registry.

```ts
import * as docker from "@pulumi/docker";

const customImage = "node-app";
const appImage = new docker.Image(customImage, {
    imageName: pulumi.interpolate`${registry.repositoryUrl}/${customImage}:v1.0.0`,
    build: {
        context: `./${customImage}`,
    },
});
```

### GCP Object Storage

Create a new bucket with a data source of a local file.

```typescript
import * as gcp from "@pulumi/gcp";

const picture = new gcp.storage.BucketObject("picture", {
    bucket: "image-store",
    source: new pulumi.asset.FileAsset("/images/nature/garden-tiger-moth.jpg"),
});
```

{{% /choosable %}}

<!-- markdownlint-disable url -->
[crosswalk-cluster-svcs]: /docs/guides/crosswalk/kubernetes/cluster-services/
[crosswalk-app-svcs]: /docs/guides/crosswalk/kubernetes/app-services/
[k8s-pvs]: https://kubernetes.io/docs/concepts/storage/persistent-volumes/
<!-- markdownlint-enable url -->

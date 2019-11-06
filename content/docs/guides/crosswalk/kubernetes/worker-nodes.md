---
title: Create the Worker Nodes
menu:
  userguides:
    parent: crosswalk-kubernetes
    identifier: crosswalk-kubernetes-worker-nodes
    weight: 2
---

{{< cloudchoose >}}

The [worker nodes][k8s-concepts] are hosts that are responsible for
running the apps and workloads of the cluster after the control plane has
scheduled its work. It also typically facilitates virtual networking using an
overlay or integrated network depending on setup.

See the [official Kubernetes docs][k8s-docs] for more details.

<div class="cloud-prologue-aws"></div>
<div class="mt">
{{% md %}}

The full code for this stack is on [GitHub][gh-repo-stack].

[gh-repo-stack]: https://github.com/metral/kubernetes-the-prod-way/tree/metral/crosswalk/aws/03-cluster-configuration
{{% /md %}}
</div>

<div class="cloud-prologue-azure"></div>
<div class="mt">
{{% md %}}

The full code for this stack is on [GitHub][gh-repo-stack].

[gh-repo-stack]: https://github.com/metral/kubernetes-the-prod-way/tree/metral/crosswalk/azure/03-cluster-configuration
{{% /md %}}
</div>

<div class="cloud-prologue-gcp"></div>
<div class="mt">
{{% md %}}

The full code for this stack is on [GitHub][gh-repo-stack].

[gh-repo-stack]: https://github.com/metral/kubernetes-the-prod-way/tree/metral/crosswalk/gcp/03-cluster-configuration

{{% /md %}}
</div>

## Overview

Given that apps and workloads will vary in quantity, and in the resources they
require, it's wise to offer differing pools of nodes for Pods to use.

Pools, also known as Node Groups, can vary by machine instance type for specific
hardware profiles. Or in sizing and capacity of nodes in a scaling group.
As well as other properties like the version of the [Kubelet][k8s-kubelet] to run.

How you segment and configure your node groups will vary by preferences and
requirements. Generally, there are at least a few classes of worker node
groups for starters: a standard pool of nodes that offers a base for
medium-sized use, and a performant pool of nodes with higher capacity and capability.

<div class="cloud-prologue-aws"></div>
<div class="mt">
{{% md %}}

We'll configure and deploy:

  * [Node Identity](#node-identity): For authentication and authorization of the worker nodes.
  * [Node Group Networking](#node-group-networking): To provide a virtual network for the
    nodes and the Pods it runs.
  * [Node Sizing](#node-sizing): To size our node scaling groups
  * [Pod Scheduling](#pod-scheduling): To schedule Pods on nodes using predicates.
  * [Recommended Worker Settings](#recommended-worker-settings): To apply helpful features
  and best-practices, such as version pinning, and resource tags.

### Node Identity

When creating node groups, it is recommended to use separate identities between
node groups, as separation of roles creates many functions: it can be used to
limit the blast radius if a given group is compromised, can regulate the number
of API requests originating from a certain group, and can also help scope
privileges to specific node types and related workloads.

We'll create [AWS instance profiles][aws-instance-profile] from the roles we
created in [AWS Identity][crosswalk-aws-identity], and used earlier when [configuring node identity](#worker-node-groups) in the cluster.

```typescript
// Create a Standard node group of t2.medium workers with an IAM instance profile.
const ngStandard = new eks.NodeGroup(`${projectName}-ng-standard`, {
    cluster: cluster,
    instanceType: "t2.medium",
    instanceProfile: new aws.iam.InstanceProfile("ng-standard", {role: stdNodegroupIamRoleName}),
    ...
}, {
    providers: { kubernetes: cluster.provider},
});

// Create a 2xlarge node group of t3.2xlarge workers with an IAM instance profile.
const ng2xlarge = new eks.NodeGroup(`${projectName}-ng-2xlarge`, {
    cluster: cluster,
    instanceType: "t3.2xlarge",
    instanceProfile: new aws.iam.InstanceProfile("ng-2xlarge", {role: perfNodegroupIamRoleName}),
    ...
}, {
    providers: { kubernetes: cluster.provider},
});
```

[aws-instance-profile]: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html
[crosswalk-aws-identity]: {{< relref "/docs/guides/crosswalk/kubernetes/identity" >}}
{{% /md %}}
</div>

<div class="cloud-prologue-azure"></div>
<div class="mt">
{{% md %}}

We'll configure and deploy:

  * [Node Pool Sizing](#node-pool-sizing): To properly size our nodes.
  * [Pod Scheduling](#pod-scheduling): To schedule Pods on nodes using predicates.
  * [Recommended Worker Settings](#recommended-worker-settings): To apply helpful features
  and best-practices.

{{% /md %}}
</div>

<div class="cloud-prologue-gcp"></div>
<div class="mt">
{{% md %}}

We'll configure and deploy:

  * [Node Sizing](#node-sizing): To properly size our nodes.
  * [Pod Scheduling](#pod-scheduling): To schedule Pods on nodes using predicates.
  * [Recommended Worker Settings](#recommended-worker-settings): To apply helpful features
  and best-practices.

{{% /md %}}
</div>

<div class="cloud-prologue-aws"></div>
<div class="mt">
{{% md %}}

### Node Group Networking

Node groups in EKS can also have their node security group be configured to a
new or existing security group.

To [create a custom security group][crosswalk-sgs], grab the cluster's ingress
rule to correctly configure the ingress and egress rules.

```typescript
// Create a Standard node group of t2.medium workers with an IAM instance profile.
const ngStandard = new eks.NodeGroup(`${projectName}-ng-standard`, {
    cluster: cluster,
    instanceType: "t2.medium",
    nodeAssociatePublicIpAddress: false,
    nodeSecurityGroup: cluster.nodeSecurityGroup,
    clusterIngressRule: cluster.eksClusterIngressRule,
    ...
}, {
    providers: { kubernetes: cluster.provider},
});

// Create a 2xlarge node group of t3.2xlarge workers with an IAM instance profile.
const ng2xlarge = new eks.NodeGroup(`${projectName}-ng-2xlarge`, {
    cluster: cluster,
    instanceType: "t3.2xlarge",
    nodeAssociatePublicIpAddress: false,
    nodeSecurityGroup: cluster.nodeSecurityGroup,
    clusterIngressRule: cluster.eksClusterIngressRule,
    ...
}, {
    providers: { kubernetes: cluster.provider},
});
```

[crosswalk-sgs]: {{< relref "/docs/guides/crosswalk/aws/vpc#configuring-security-groups-for-a-vpc" >}}
{{% /md %}}
</div>

<div class="cloud-prologue-azure"></div>
<div class="mt">
{{% md %}}

### Node Pool Networking

Network profiles can be configured in Azure to work within the virtual network
created, allowing you to specify the Kubernetes Service and Docker network properties.

```typescript
import * as azure from "@pulumi/azure";

// Create the AKS cluster within the network created.
const cluster = new azure.containerservice.KubernetesCluster(`${name}`, {
    resourceGroupName: config.resourceGroupName,
    networkProfile: {
        networkPlugin: "azure",
        dnsServiceIp: "10.2.2.254",
        serviceCidr: "10.2.2.0/24",
        dockerBridgeCidr: "172.17.0.1/16",
    },
    ...
}
```

{{% /md %}}
</div>

### Node Sizing

<div class="cloud-prologue-aws"></div>
<div class="mt">
{{% md %}}

In EKS, worker node groups are backed by auto scaling groups.
These groups provide automatic scaling and management of a logical
collection of hosts through health checks and policies, and are an effective
means of ensuring node groups are adequately provisioned as intended.

We can configure the scaling group to run a specific quantity of nodes.

Size the node groups accordingly to known or approximate usage and bursting
expectations.

```typescript
// Create a Standard node group of t2.medium workers with an IAM instance profile.
const ngStandard = new eks.NodeGroup(`${projectName}-ng-standard`, {
    cluster: cluster,
    instanceType: "t2.medium",
    desiredCapacity: 3,
    minSize: 3,
    maxSize: 10,
    ...
}, {
    providers: { kubernetes: cluster.provider},
});

// Create a 2xlarge node group of t3.2xlarge workers with an IAM instance profile.
const ng2xlarge = new eks.NodeGroup(`${projectName}-ng-2xlarge`, {
    cluster: cluster,
    instanceType: "t3.2xlarge",
    desiredCapacity: 5,
    minSize: 5,
    maxSize: 10,
    ...
}, {
    providers: { kubernetes: cluster.provider},
});
```

{{% /md %}}
</div>

<div class="cloud-prologue-azure"></div>
<div class="mt">
{{% md %}}

In AKS, worker node pools are backed by [VM Scale Sets][azure-scalesets].
These pools provide automatic scaling and management of a logical
collection of hosts through health checks and policies, and are an effective
means of ensuring node pools are adequately provisioned as intended.

We can configure the agent pool profile to run a specific quantity and type of nodes.

Size the node pools accordingly to known or approximate usage and bursting
expectations.

```typescript
const cluster = new azure.containerservice.KubernetesCluster(`${name}`, {
    agentPoolProfiles: [{
        name: "performant",
        count: 3,
        vmSize: "Standard_DS4_v2",
        osType: "Linux",
        osDiskSizeGb: 30,
        vnetSubnetId: config.subnetId,
    }, {
        name: "standard",
        count: 2,
        vmSize: "Standard_B2s",
        osType: "Linux",
        osDiskSizeGb: 30,
        vnetSubnetId: config.subnetId,
    }],
    // ...
});
```

[azure-scalesets]: https://azure.microsoft.com/en-us/services/virtual-machine-scale-sets/
{{% /md %}}
</div>

<div class="cloud-prologue-gcp"></div>
<div class="mt">
{{% md %}}

In GKE, worker node pools provide automatic scaling and management of a logical
collection of hosts through health checks and policies, and are an effective
means of ensuring node pools are adequately provisioned as intended.

We can configure the node config to run a specific quantity of nodes, alongwith
the min and max capacity the pool should have.

Size the node pools accordingly to known or approximate usage and bursting
expectations.

```typescript
const standardNodes = new gcp.container.NodePool("standard-nodes", {
    cluster: cluster.name,
    version: "1.14.7-gke.10",
    autoscaling: {minNodeCount: 0, maxNodeCount: 3},
    initialNodeCount: 2,
    ...
});

const performantNodes = new gcp.container.NodePool("performant-nodes", {
    cluster: cluster.name,
    version: "1.14.7-gke.10",
    autoscaling: {minNodeCount: 0, maxNodeCount: 3},
    initialNodeCount: 2,
    ...
});
```

{{% /md %}}
</div>

If necessary, consider installing the [Kubernetes Cluster
Autoscaler][k8s-cluster-autoscaler] to automatically adjust the size of the
cluster when there are either insufficient resources for Pods, or if nodes are
underutilized. You'll need to set up the appropriate tags on the node groups for
the `cluster-autoscaler` to run properly. See the [Recommended Worker
Settings](#recommended-worker-settings) below to configure the tags of
a node group accordingly for the `cluster-autoscaler`.

### Pod Scheduling

We can logically organize node groups in Kubernetes to use with configurable scheduling
predicates on Pods. Node [Labels][k8s-labels] are used to identify nodes by attributes,
and [Taints][k8s-taints] repel a set of Pods to ensure that only a given
class of workload that can tolerate the taint is allowed to run on the nodes.

Both configurations can be set in the `PodSpec` using a
[`nodeSelector`][k8s-node-selector] or [`tolerations`][k8s-taints]
respectively.

<div class="cloud-prologue-aws"></div>
<div class="mt">
{{% md %}}

```typescript
// Create a Standard node group of t2.medium workers with an IAM instance profile.
const ngStandard = new eks.NodeGroup(`${projectName}-ng-standard`, {
    cluster: cluster,
    instanceType: "t2.medium",
    labels: {"amiId": "ami-0ca5998dc2c88e64b"},
    ...
}, {
    providers: { kubernetes: cluster.provider},
});

// Create a 2xlarge node group of t3.2xlarge workers with an IAM instance profile.
const ng2xlarge = new eks.NodeGroup(`${projectName}-ng-2xlarge`, {
    cluster: cluster,
    instanceType: "t3.2xlarge",
    labels: {"amiId": "ami-0ca5998dc2c88e64b"},
    taints: { "special": { value: "true", effect: "NoSchedule"}},
    ...
}, {
    providers: { kubernetes: cluster.provider},
});
```

{{% /md %}}
</div>

<div class="cloud-prologue-azure"></div>
<div class="mt">
{{% md %}}

Set labels on nodes.

```typescript
$ kubectl label nodes <NODE_NAME> disktype=ssd
```

Set taints on nodes.
```typescript
$ kubectl taint nodes <NODE_NAME> special=true:NoSchedule
```

{{% /md %}}
</div>

<div class="cloud-prologue-gcp"></div>
<div class="mt">
{{% md %}}

```typescript
import * as gcp from "@pulumi/gcp";

const standardNodes = new gcp.container.NodePool("standard-nodes", {
    cluster: cluster.name,
    version: "1.14.7-gke.10",
    autoscaling: {minNodeCount: 0, maxNodeCount: 3},
    initialNodeCount: 2,
    nodeConfig: {
        machineType: "n1-standard-1",
        oauthScopes: [
            "https://www.googleapis.com/auth/compute",
            "https://www.googleapis.com/auth/devstorage.read_only",
            "https://www.googleapis.com/auth/logging.write",
            "https://www.googleapis.com/auth/monitoring",
        ],
        labels: {"instanceType": "n1-standard-1"},
    },
});

const performantNodes = new gcp.container.NodePool("performant-nodes", {
    cluster: cluster.name,
    version: "1.14.7-gke.10",
    autoscaling: {minNodeCount: 0, maxNodeCount: 3},
    initialNodeCount: 2,
    nodeConfig: {
        machineType: "n1-standard-16",
        oauthScopes: [
            "https://www.googleapis.com/auth/compute",
            "https://www.googleapis.com/auth/devstorage.read_only",
            "https://www.googleapis.com/auth/logging.write",
            "https://www.googleapis.com/auth/monitoring",
        ],
        labels: {"instanceType": "n1-standard-16"},
        taints: [{key: "special", value: "true", effect: "NO_SCHEDULE"}],
    },
});

```

{{% /md %}}
</div>

### Recommended Worker Settings

<div class="cloud-prologue-aws"></div>
<div class="mt">
{{% md %}}

  * Use a specific version of Kubernetes for node group. This pins the nodes
  to a particular release in a declarative manner, instead of implicitly
  using the latest available version, or using a smart default where both
  can be updated at any moment.
  * Tag resources under management to provide the ability to assign
  metadata to resources to make it easier to manage, search, and filter them.

```typescript
// Create a Standard node group of t2.medium workers with an IAM instance profile.
const ngStandard = new eks.NodeGroup(`${projectName}-ng-standard`, {
    cluster: cluster,
    instanceType: "t2.medium",
    amiId: "ami-0ca5998dc2c88e64b", // k8s v1.14.7 in us-west-2
    cloudFormationTags: clusterName.apply(clusterName => ({
        "CloudFormationGroupTag": "true",
        "k8s.io/cluster-autoscaler/enabled": "true",
        [`k8s.io/cluster-autoscaler/${clusterName}`]: "true",
    })),
    ...
}, {
    providers: { kubernetes: cluster.provider},
});

// Create a 2xlarge node group of t3.2xlarge workers with an IAM instance profile.
const ng2xlarge = new eks.NodeGroup(`${projectName}-ng-2xlarge`, {
    cluster: cluster,
    instanceType: "t3.2xlarge",
    amiId: "ami-0ca5998dc2c88e64b", // k8s v1.14.7 in us-west-2
    cloudFormationTags: clusterName.apply(clusterName => ({
        "CloudFormationGroupTag": "true",
        "k8s.io/cluster-autoscaler/enabled": "true",
        [`k8s.io/cluster-autoscaler/${clusterName}`]: "true",
    })),
    ...
}, {
    providers: { kubernetes: cluster.provider},
});
```

{{% /md %}}
</div>

<div class="cloud-prologue-azure"></div>
<div class="mt">
{{% md %}}

  * Use a specific version of Kubernetes for node group. This pins the nodes
  to a particular release in a declarative manner, instead of implicitly
  using the latest available version, or using a smart default where both
  can be updated at any moment.

{{% /md %}}
</div>

<div class="cloud-prologue-gcp"></div>
<div class="mt">
{{% md %}}

  * Use a specific version of Kubernetes for node group. This pins the nodes
    to a particular release in a declarative manner, instead of implicitly
    using the latest available version, or using a smart default where both
    can be updated at any moment.
  * Set [OAuth Scopes][gcp-oauth-scopes] for Google APIs to limit the capabilities of the node
    pool.
  * Tag resources under management to provide the ability to assign
    metadata to resources to make it easier to manage, search, and filter them.

```typescript
import * as gcp from "@pulumi/gcp";

const standardNodes = new gcp.container.NodePool("standard-nodes", {
        ...
        version: "1.14.7-gke.10",
        nodeConfig: {
            machineType: "n1-standard-1",
            oauthScopes: [
                "https://www.googleapis.com/auth/compute",
                "https://www.googleapis.com/auth/devstorage.read_only",
                "https://www.googleapis.com/auth/logging.write",
                "https://www.googleapis.com/auth/monitoring",
            ],
            tags: ["org-pulumi"],
        },
});
```

[gcp-oauth-scopes]: https://developers.google.com/identity/protocols/googlescopes
[k8s-labels]: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/
{{% /md %}}
</div>

[k8s-concepts]: https://kubernetes.io/docs/concepts
[k8s-kubelet]: https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/
[k8s-labels]: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/
[k8s-taints]: https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/
[k8s-cluster-autoscaler]: https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler
[k8s-node-selector]: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/
[k8s-docs]: https://kubernetes.io/docs/reference/

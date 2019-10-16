---
title: Create the Worker Nodes
menu:
  userguides:
    parent: crosswalk-kubernetes
    identifier: crosswalk-kubernetes-worker-nodes
    weight: 2
---

The [worker nodes][k8s-concepts] are hosts that are responsible for
running the apps and workloads of the cluster after the control plane has 
scheduled it work. It also typically faciliates virtual networking using an
overlay or integrated network depending on setup.

The full code for this stack is on [GitHub][gh-repo-stack].

See the [official Kubernetes docs][k8s-docs] for more details.

## Overview

Given that apps and workloads will vary in quantity, and in the resources they
require, it's wise to offer differing pools of nodes for Pods to use.

Pools, also known as Node Groups, can vary by machine `instanceType` for specific
hardware profiles. Or in `minSize`, `maxSize` and `desiredCapacity` of nodes
in a scaling group. As well as other properties like the `version` of the [Kubelet][k8s-kubelet] to run.

How you segment and configure your node groups will vary by preferences and
requirements. Generally, there are at least a few classes of worker node
groups for starters: a standard pool of nodes that
offers a base for medium-sized use, and a performant pool of nodes with higher
capacity and capability.

We'll configure and deploy:

  * [Worker Identity](#worker-identity): For authentication and authorization of the worker nodes.
  * [Worker Networking](#worker-networking): To provide a virtual network for the
    nodes and the Pods it runs.
  * [Scheduling](#scheduling): To properly tune our scaling node groups, and to
    schedule Pods on nodes using predicates.
  * [Recommended Worker Settings](#recommended-worker-settings): To apply helpful features
  and best-practices, such as version pinning, and resource tags.

### Worker Identity

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

### Worker Networking

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

### Scheduling

Scheduling in Kubernetes takes on many forms depending on the context. It
generally revolves around the capacity of the worker nodes, or where to place
the Pods at runtime depending on preferences or requirements.

#### Node Scheduling

In managed Kubernetes offerings, worker node groups are backed by auto scaling
groups. These groups provide automatic scaling and management of a logical
collection of hosts through health checks and policies, and are an effective
means of ensuring node groups are adequately provisioned as intended.

We can configure the `desiredCapacity` of the scaling group to run a specific
quantity of nodes that falls between our `minSize` and `maxSize`.

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

If necessary, consider installing the [Kubernetes Cluster
Autoscaler][k8s-cluster-autoscaler] to automatically adjust the size of the
cluster when there are either insufficient resources for Pods, or if nodes are
underutilized. You'll need to set up the appropriate tags on the node groups for
the `cluster-autoscaler` to run properly. See the [Recommended Worker
Settings](#recommended-worker-settings) below to configure the tags of
a node group accordingly for the `cluster-autoscaler`.

#### Pod Scheduling

We can logically organize node groups in Kubernetes to use with configurable scheduling
predicates on Pods. Node [Labels][k8s-labels] are used to identify nodes by attributes,
and [Taints][k8s-taints] repel a set of Pods to ensure that only a given
class of workload that can tolerate the taint is allowed to run on the nodes.

Both configurations can be set in the `PodSpec` using a
[`nodeSelector`][k8s-node-selector] or [`tolerations`][k8s-taints]
respectively.

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

### Recommended Worker Settings

  * Use a specific version of Kubernetes for node group by specifing the AMI
    for the region. This pins the nodes to a particular release in a declarative
    manner, instead of implicitly using the latest available version, or using a smart default
    where both can be updated at any moment.
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

### Aggregated Node Groups Example

Below is an aggregated example of the recommended EKS node groups configuration.

The full code for this stack is also available on [GitHub][gh-repo-stack].

```typescript
// Create a Standard node group of t2.medium workers.
const ngStandard = new eks.NodeGroup(`${projectName}-ng-standard`, {
    cluster: cluster,
    instanceProfile: new aws.iam.InstanceProfile("ng-standard", {role: stdNodegroupIamRoleName}),
    nodeAssociatePublicIpAddress: false,
    nodeSecurityGroup: cluster.nodeSecurityGroup,
    clusterIngressRule: cluster.eksClusterIngressRule,
    amiId: "ami-0ca5998dc2c88e64b", // k8s v1.14.7 in us-west-2
    instanceType: "t2.medium",
    desiredCapacity: 3,
    minSize: 3,
    maxSize: 10,
    labels: {"amiId": "ami-0ca5998dc2c88e64b"},
    cloudFormationTags: clusterName.apply(clusterName => ({
        "CloudFormationGroupTag": "true",
        "k8s.io/cluster-autoscaler/enabled": "true",
        [`k8s.io/cluster-autoscaler/${clusterName}`]: "true",
    })),
}, {
    providers: { kubernetes: cluster.provider},
});

// Create a 2xlarge node group of t3.2xlarge workers with taints for special workloads.
const ng2xlarge = new eks.NodeGroup(`${projectName}-ng-2xlarge`, {
    cluster: cluster,
    instanceProfile: new aws.iam.InstanceProfile("ng-2xlarge", {role: perfNodegroupIamRoleName}),
    nodeAssociatePublicIpAddress: false,
    nodeSecurityGroup: cluster.nodeSecurityGroup,
    clusterIngressRule: cluster.eksClusterIngressRule,
    amiId: "ami-0ca5998dc2c88e64b", // k8s v1.14.7 in us-west-2
    instanceType: "t3.2xlarge",
    desiredCapacity: 5,
    minSize: 5,
    maxSize: 10,
    labels: {"amiId": "ami-0ca5998dc2c88e64b"},
    taints: { "special": { value: "true", effect: "NoSchedule"}},
    cloudFormationTags: clusterName.apply(clusterName => ({
        "CloudFormationGroupTag": "true",
        "k8s.io/cluster-autoscaler/enabled": "true",
        [`k8s.io/cluster-autoscaler/${clusterName}`]: "true",
    })),
}, {
    providers: { kubernetes: cluster.provider},
});
```

[k8s-concepts]: https://kubernetes.io/docs/concepts
[k8s-kubelet]: https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/
[aws-instance-profile]: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html
[crosswalk-aws-identity]: {{< relref "/docs/guides/crosswalk/kubernetes/identity" >}}
[crosswalk-sgs]: {{< relref "/docs/guides/crosswalk/aws/vpc#configuring-security-groups-for-a-vpc" >}}
[k8s-labels]: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/
[k8s-taints]: https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/
[k8s-cluster-autoscaler]: https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler
[gh-repo-stack]: https://github.com/metral/kubernetes-the-prod-way/tree/metral/crosswalk/aws/03-cluster-configuration
[k8s-node-selector]: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/
[k8s-docs]: https://kubernetes.io/docs/reference/

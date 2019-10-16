---
title: Create the Control Plane
menu:
  userguides:
    parent: crosswalk-kubernetes
    identifier: crosswalk-kubernetes-control-plane
    weight: 1
---

In order to run container workloads, you will need a Kubernetes cluster.
It is possible to provision and manage a cluster manually on AWS,
however the managed offering, [Elastic Kubernetes Service (EKS)][eks], offers an
easier way to get up and running.

The full code for this stack is on [GitHub][gh-repo-stack].

See the [official Kubernetes docs][k8s-docs] for more details.

## Overview

The [control plane][k8s-concepts] is a collection of processes that coordinate and
manage the cluster's state, segmented by responsibilities. It also makes
scheduling decisions to facilitate the applications and cloud workflows that
the worker nodes will be responsible for running.

Kubernetes clusters require a certain architecture of cloud resources in order
to successfully run.

We'll configure and deploy:

  * [Identity](#identity): For authentication and authorization of
  cluster users, and worker nodes.
  * [Networking](#networking): To provide a virtual network for the cluster
  and workloads to operate within.
  * [Storage](#storage): To provide data persistence for the cluster and its
    workloads.
  * [Recommended Settings](#recommended-settings): To apply helpful features
  and best-practices, such as version pinning, resource tags, and control plane logging.

### Identity

In [AWS Identity][crosswalk-aws-identity] we create various IAM roles for
use in Kubernetes.

For **users**, we create an `admins` role for cluster administrators with
root privileges, and a limited scope `devs` role for general purpose
execution of workloads. Both roles will be tied into Kubernetes RBAC.

For **worker nodes**, we create separate roles for a few typical
classes of worker node groups: a standard pool of nodes, and a performant
pool of nodes that differ by instance type. 

Separation of roles creates many functions: it can be used to
limit the blast radius if a given group is compromised, can regulate the number 
of API requests originating from a certain group, and can also help scope
privileges to specific node types and workloads.

#### Users 

We configure the user identities using `roleMappings` in the cluster since
we created roles for the users, and map it into Kubernetes RBAC as defined in the [docs][k8s-rbac-docs].

The following interfaces are available in Pulumi to map IAM into Kubernetes: [`RoleMapping`][role-mapping] and
[`UserMapping`][user-mapping]. Below we demonstrate using a `RoleMapping`.

```typescript
import * as eks from "@pulumi/eks";

// Create an EKS cluster with user IAM.
const cluster = new eks.Cluster(`${projectName}`, {
    roleMappings: [
        {
            roleArn: config.adminsIamRoleArn,
            groups: ["system:masters"],
            username: "pulumi:admins",
        },
        {
            roleArn: config.devsIamRoleArn,
            groups: ["pulumi:devs"],
            username: "pulumi:alice",
        },
    ]
    ...
}
```

#### Worker Node Groups

We configure the worker identities using `instanceRoles` in the cluster.
Later on, when we [define the node groups][nodegroups], we'll use an [instance
profile][aws-instance-profile] of each group's role to allow them to join the
cluster per the configuration below.

```typescript
import * as eks from "@pulumi/eks";

// Create an EKS cluster with worker node group IAM.
const cluster = new eks.Cluster(`${projectName}`, {
    instanceRoles: [
        aws.iam.Role.get("adminsIamRole", stdNodegroupIamRoleName),
        aws.iam.Role.get("devsIamRole", perfNodegroupIamRoleName),
    ],
    ...
}
```

### Networking

In [AWS Managed Infrastructure][crosswalk-aws-infra] we install any desired
managed services, and demonstrate how to 
create or use an existing a virtual network for use with Kubernetes.

How you create the network will vary on your permissions and preferences.

Typical setups will want to provide Kubernetes with the following resources
to use for the cluster.

  * Public subnets for use with provisioning public load balancers.
  * Private subnets for use with provisioning private load balancers.
  * Private subnets for use as the default subnets for workers to run in.
  * Managed [Pod networking][k8s-pod-networking].

By default, [`pulumi/eks`][pulumi-eks] will deploy workers into the private subnets, if
specified, if not into the public subnets provided. Using private subnets for
workers without associating a public IP address is highly recommended - it 
creates workers that will not be publicly accessible from the Internet,
and they'll typically be shielded within your VPC.

Kubernetes requires that all subnets you intend to use be [properly tagged][eks-subnet-tagging],
in order to know which subnets it can provision load balancers within. To
ensure proper functionality, pass in **any** public and/or private subnets you
intend to use into the cluster definition. If these need to be updated to include more subnets, or
if some need to be removed, the change is straightforward with a Pulumi update.

Lastly, EKS will automatically manage Kubernetes Pod networking for us through
the use of the [AWS CNI Plugin][aws-k8s-cni]. This plugin is deployed by
default on worker nodes as a [DeamonSet][k8s-ds] named `aws-node` in all clusters
provisioned with `pulumi/eks`, and is capable of being [configured][configure-cni].

```typescript
import * as eks from "@pulumi/eks";

// Create an EKS cluster in a given VPC and set of subnets.
const cluster = new eks.Cluster(`${projectName}`, {
    vpcId: config.vpcId,
    publicSubnetIds: config.publicSubnetIds,
    privateSubnetIds: config.privateSubnetIds,
    nodeAssociatePublicIpAddress: false,
    ...
}
```

### Storage

Kubernetes [storage][k8s-storage] centers on providing data persistence for 
the cluster with shared storage and/or Pods with volumes. The volume classes
are extensive and vary by cloud provider, but
typically they include volume types for mechanical drives and 
SSDs, along with network backed storage such as [NFS][nfs], [EFS][aws-efs], and [CephFS][ceph-fs].

To provision a [PersistentVolume][k8s-pvs], we first must ensure we have the desired storage
classes created in the cluster. As of Kubernetes v1.11+ on EKS, a default `gp2`
[storage class][eks-storage-classes] will always be created automatically for the cluster by EKS.

Note, that at most one storage class should be marked as default.
If two or more of them are marked as default, as is the case with EKS if
a user also supplies their own default storage class,
a [`PersistentVolumeClaim`][k8s-pvs] without `storageClassName` explicitly specified
cannot be created.

See the [official EKS docs][eks-storage-classes] and [Kubernetes docs][k8s-storage-classes-default] for more details.

Create the storage classes using `kubectl`.

```bash
cat > storage-classes.yaml << EOF
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: gp2-encrypted
provisioner: kubernetes.io/aws-ebs
parameters:
  type: gp2 
  encrypted: "true"

---

kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: sc1
provisioner: kubernetes.io/aws-ebs
parameters:
  type: sc1 
EOF
```

```bash
$ kubectl apply -f storage-classes.yaml
```

or 

Create the storage classes using Pulumi.

```typescript
import * as eks from "@pulumi/eks";

// Create an EKS cluster with custom storage classes.
const cluster = new eks.Cluster(`${projectName}`, {
    storageClasses: {
        "gp2-encrypted": { type: "gp2", encrypted: true},
        "sc1": { type: "sc1"}
    },
    ...
}
```
With the desired storage classes created in the cluster, we can create any
necessary persistent volumes in the cluster.

Create the persistent volume with a persistent volume claim and `kubectl`.

```bash
cat > pvc.yaml << EOF
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: mypvc
  labels:
    app: myapp
spec:
  storageClassName: gp2-encrypted
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
EOF
```

```bash
$ kubectl apply -f pvc.yaml
```

or 

Create the persistent volume with a persistent volume claim and Pulumi.

```typescript
import * as eks from "@pulumi/eks";
import * as k8s from "@pulumi/k8s";

// Create a persistent volume claim with a storage class built into the cluster.
cluster.core.storageClasses["gp2-encrypted"].apply(sc => {
    sc.metadata.name.apply(name => {
        if (name) {
            const myPvc = new k8s.core.v1.PersistentVolumeClaim("mypvc", {
                    spec: {
                        accessModes: ["ReadWriteOnce"],
                        storageClassName: name,
                        resources: {requests: {storage: "1Gi"}}
                    }
                },
                { provider: cluster.provider }
            );
        }
    });
});

```

### Recommended Settings

With the core infrastruture in place for the control plane, there are some
general best-practices and recommendations to configure in the cluster.

  * Use a specific version of Kubernetes for the control plane. This pins the
    cluster to a particular release in a declarative manner, instead of
    implicitly using the latest available version, or using a smart default
    where both can be updated at any moment.
  * Tag resources under management to provide the ability to assign
    metadata to resources to make it easier to manage, search, and filter them.
  * Skip enabling the default node group in favor of managing them separately from
    the control plane, as demonstrated in [Create the Worker Nodes][nodegroups].
  * Refrain from using the `kube-dashboard` as it is generally not recommended due
    to its [potential security implications][kube-dash-security]. VMware's
    [Octant][octant] is recommended as a safe alternative.
  * Enable control plane logging to have diagnostics of the control
    plane's actions, and for use in debugging and auditing.
  * (Optional) Configure private accessibility of the control plane /
    API Server endpoint to prevent it from being publicly exposed on the
    Internet. Note, to enable this feature additional networking is required,
    and a [bastion host][aws-bastion] would be needed to access the control
    plane.

  ```typescript
  import * as eks from "@pulumi/eks";
  
  // Create an EKS cluster with recommended settings.
  const cluster = new eks.Cluster(`${projectName}`, {
      version: "1.14",
      tags: {
          "Project": "k8s-aws-cluster",
          "Org": "pulumi",
      },
      clusterSecurityGroupTags: { "ClusterSecurityGroupTag": "true" },
      nodeSecurityGroupTags: { "NodeSecurityGroupTag": "true" },
      skipDefaultNodeGroup: true,
      deployDashboard: false,
      enabledClusterLogTypes: ["api", "audit", "authenticator", "controllerManager", "scheduler"],
      // endpointPublicAccess: false,     // Requires bastion to access cluster API endpoint
      // endpointPrivateAccess: true,     // Requires bastion to access cluster API endpoint
      ...
  }
  ```

### Aggregated Cluster Example

Below is an aggregated example of the recommended EKS cluster configuration.

The full code for this stack is also available on [GitHub][gh-repo-stack].

```typescript
import * as aws from "@pulumi/aws";
import * as eks from "@pulumi/eks";

// Create an EKS cluster.
const cluster = new eks.Cluster(`${projectName}`, {
    instanceRoles: [
        aws.iam.Role.get("adminsIamRole", stdNodegroupIamRoleName),
        aws.iam.Role.get("devsIamRole", perfNodegroupIamRoleName),
    ],
    roleMappings: [
        {
            roleArn: config.adminsIamRoleArn,
            groups: ["system:masters"],
            username: "pulumi:admins",
        },
        {
            roleArn: config.devsIamRoleArn,
            groups: ["pulumi:devs"],
            username: "pulumi:alice",
        },
    ],
    vpcId: config.vpcId,
    publicSubnetIds: config.publicSubnetIds,
    privateSubnetIds: config.privateSubnetIds,
    storageClasses: {
        "gp2-encrypted": { type: "gp2", encrypted: true},
        "sc1": { type: "sc1"}
    },
    nodeAssociatePublicIpAddress: false,
    skipDefaultNodeGroup: true,
    deployDashboard: false,
    version: "1.14",
    tags: {
        "Project": "k8s-aws-cluster",
        "Org": "pulumi",
    },
    clusterSecurityGroupTags: { "ClusterSecurityGroupTag": "true" },
    nodeSecurityGroupTags: { "NodeSecurityGroupTag": "true" },
    enabledClusterLogTypes: ["api", "audit", "authenticator", "controllerManager", "scheduler"],
    // endpointPublicAccess: false,     // Requires bastion to access cluster API endpoint
    // endpointPrivateAccess: true,     // Requires bastion to access cluster API endpoint
});

// Export the cluster details.
export const kubeconfig = cluster.kubeconfig;
export const clusterName = cluster.core.cluster.name;
```

[eks]: https://aws.amazon.com/eks/
[gh-repo-stack]: https://github.com/metral/kubernetes-the-prod-way/tree/metral/crosswalk/aws/03-cluster-configuration
[k8s-docs]: https://kubernetes.io/docs/reference/
[k8s-concepts]: https://kubernetes.io/docs/concepts
[crosswalk-aws-identity]: {{< relref "/docs/guides/crosswalk/kubernetes/identity" >}}
[crosswalk-aws-infra]: {{< relref "/docs/guides/crosswalk/kubernetes/managed-infra" >}}
[crosswalk-aws-cluster-svcs]: {{< relref "/docs/guides/crosswalk/kubernetes/cluster-services" >}}
[crosswalk-aws-app-svcs]: {{< relref "/docs/guides/crosswalk/kubernetes/app-services" >}}
[crosswalk-aws-apps]: {{< relref "/docs/guides/crosswalk/kubernetes/apps" >}}
[k8s-rbac-docs]: https://kubernetes.io/docs/reference/access-authn-authz/rbac/
[role-mapping]: {{< relref "/docs/reference/pkg/nodejs/pulumi/eks#RoleMapping" >}}
[user-mapping]: {{< relref "/docs/reference/pkg/nodejs/pulumi/eks#UserMapping" >}}
[nodegroups]: #create-the-worker-nodes
[aws-instance-profile]: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html
[k8s-pod-networking]: https://kubernetes.io/docs/concepts/cluster-administration/networking/
[eks-subnet-tagging]: https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html#vpc-subnet-tagging
[pulumi-eks]: https://github.com/pulumi/pulumi-eks
[simplify-rbac]: /blog/simplify-kubernetes-rbac-in-amazon-eks-with-open-source-pulumi-packages/
[aws-k8s-cni]: https://github.com/aws/amazon-vpc-cni-k8s/
[k8s-ds]: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/
[configure-cni]: {{< relref "/docs/reference/pkg/nodejs/pulumi/eks#VpcCniOptions" >}}
[k8s-storage]: https://kubernetes.io/docs/concepts/storage/
[nfs]: https://en.wikipedia.org/wiki/Network_File_System
[aws-efs]: https://aws.amazon.com/efs/
[ceph-fs]: https://docs.ceph.com/docs/master/cephfs/
[k8s-pvs]: https://kubernetes.io/docs/concepts/storage/persistent-volumes/
[eks-storage-classes]: https://docs.aws.amazon.com/eks/latest/userguide/storage-classes.html
[k8s-storage-classes-default]: https://kubernetes.io/docs/tasks/administer-cluster/change-default-storage-class/#changing-the-default-storageclass

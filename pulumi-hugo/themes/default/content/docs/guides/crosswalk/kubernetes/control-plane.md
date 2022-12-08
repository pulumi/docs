---
title_tag: Creating a Kubernetes Control Plane | Crosswalk
title: Creating a Kubernetes Control Plane
meta_desc: This page will walk you through how to create on a Kubernetes Control Pane
           on AWS, Azure, and GCP.
menu:
  userguides:
    parent: crosswalk-kubernetes
    identifier: crosswalk-kubernetes-control-plane
    weight: 2
---

{{< chooser cloud "aws,azure,gcp" / >}}

{{% choosable cloud aws %}}

In order to run container workloads, you will need a Kubernetes cluster.
While it is possible to provision and manage a cluster manually on AWS,
their managed offering [Elastic Kubernetes Service (EKS)](https://aws.amazon.com/eks/) offers an
easier way to get up and running.

See the [official Kubernetes docs](https://kubernetes.io/docs/reference/) for more details.

The full code for this stack is on [GitHub](https://github.com/pulumi/kubernetes-guides/tree/master/aws/03-cluster-configuration).

{{% /choosable %}}

{{% choosable cloud azure %}}

In order to run container workloads, you will need a Kubernetes cluster.
While it is possible to provision and manage a cluster manually on Azure,
their managed offering, [Azure Kubernetes Service (AKS)](https://azure.microsoft.com/en-us/services/kubernetes-service/), offers an
easier way to get up and running.

See the [official Kubernetes docs](https://kubernetes.io/docs/reference/) for more details.

The full code for this stack is on [GitHub](https://github.com/pulumi/kubernetes-guides/tree/master/azure/03-cluster-configuration).

{{% /choosable %}}

{{% choosable cloud gcp %}}

In order to run container workloads, you will need a Kubernetes cluster.
While it is possible to provision and manage a cluster manually on GCP,
their managed offering, [Google Kubernetes Engine (GKE)](https://cloud.google.com/kubernetes-engine/), offers an
easier way to get up and running.

See the [official Kubernetes docs](https://kubernetes.io/docs/reference/) for more details.

The full code for this stack is on [GitHub](https://github.com/pulumi/kubernetes-guides/tree/master/gcp/03-cluster-configuration).

{{% /choosable %}}

## Overview

The [control plane](https://kubernetes.io/docs/concepts) is a collection of processes that coordinate and
manage the cluster's state, segmented by responsibilities. It also makes
scheduling decisions to facilitate the applications and cloud workflows that
the worker nodes run.

We'll configure and deploy:

* [Identity](#identity): For authentication and authorization of
cluster users and worker nodes.
* [Managed Infrastructure](#managed-infrastructure): To provide managed services for the cluster.
At a minimum, this includes a virtual network for the cluster.
* [Storage](#storage): To provide data stores for the cluster and its
  workloads.
* [Recommended Settings](#recommended-settings): To apply helpful features
and best-practices, such as version pinning, resource tags, and control plane logging.

## Identity

In [Identity](/docs/guides/crosswalk/kubernetes/identity/) we demonstrate how to create typical IAM resources for use in Kubernetes. You'll want to create the Identity stack first.

Separation of identities is important for several reasons: it can be used to
limit the scope of damage if a given group is compromised, can regulate the number
of API requests originating from a certain group, and can also help scope
privileges to specific workloads.

{{% choosable cloud azure %}}

Azure Kubernetes Service can be configured to use Azure Active Directory (Azure AD) for user authentication. Cluster administrators can then configure Kubernetes role-based access control (RBAC) based on a user's identity or directory group membership.

To provide Azure AD authentication for an AKS cluster, two Azure AD applications are created. The first application is a server component that provides user authentication. The second application is a client component that uses the server application for the actual authentication of the credentials provided by the client.

We configure applications and service principals using the `@pulumi/azuread` package. After the applications are created, there is manual step required to [grant admin consent](https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/configure-user-consent#grant-admin-consent-when-registering-an-app-in-the-azure-portal) for API permissions.

{{% /choosable %}}

### Users

{{% choosable cloud aws %}}

For **users**, we create an `admins` role for cluster administrators with
root privileges, and a limited scope `devs` role for general purpose
execution of workloads. Both roles will be tied into Kubernetes RBAC in
[Configure Access Control](/docs/guides/crosswalk/kubernetes/configure-access-control/).

For **worker nodes**, we create separate roles for a few typical
classes of worker node groups: a standard pool of nodes, and a performant
pool of nodes that differ by instance type.

Now that we have created roles for the users, we configure user identities
using roleMappings, and map it into Kubernetes RBAC as shown in the
[docs](https://kubernetes.io/docs/reference/access-authn-authz/rbac/).

Pulumi provides the following interfaces to map IAM into Kubernetes: [`RoleMapping`](/docs/reference/pkg/nodejs/pulumi/eks#RoleMapping) and
[`UserMapping`](/docs/reference/pkg/nodejs/pulumi/eks#UserMapping). Below we demonstrate using a `RoleMapping`.

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

{{% /choosable %}}

{{% choosable cloud azure %}}

For users, we create and use a ServicePrincipal for cluster administrators with
root privileges, and a limited scope `devs` user group for general purpose
execution of workloads. Both identities will be tied into Kubernetes RBAC in
[Configure Access Control](/docs/guides/crosswalk/kubernetes/configure-access-control/).

We configure the principal identities using `servicePrincipal` to create the
cluster, and set up `roleBasedAccessControl` to manage authentication into the cluster.

```typescript
import * as azure from "@pulumi/azure";

// Create the AKS cluster with IAM.
const cluster = new azure.containerservice.KubernetesCluster(`${name}`, {
    resourceGroupName: config.resourceGroupName,
    servicePrincipal: {
        clientId: config.adClientAppId,
        clientSecret: config.adClientAppSecret,
    },
    roleBasedAccessControl: {
        enabled: true,
        azureActiveDirectory: {
            clientAppId: config.adClientAppId,
            serverAppId: config.adServerAppId,
            serverAppSecret: config.adServerAppSecret,
        },
    },
    ...
}
```

{{% /choosable %}}

{{% choosable cloud gcp %}}

For users, we create and use a ServiceAccount for cluster administrators with
root privileges, and a limited scope `devs` ServiceAccount for general purpose
execution of workloads. Both identities will be tied into Kubernetes RBAC in
[Configure Access Control](/docs/guides/crosswalk/kubernetes/configure-access-control/).

By authenticating with the ServiceAccount using `gcloud`, as outlined in [Identity](/docs/guides/crosswalk/kubernetes/identity#create-an-iam-role-and-serviceaccount-for-admins), we automatically bind the ServiceAccount to be a cluster admin and no further action is required.

{{% /choosable %}}

{{% choosable cloud aws %}}

#### Worker Node Groups

We configure the worker identities using `instanceRoles` in the cluster.
Later on, when we [define the node groups](/docs/guides/crosswalk/kubernetes/worker-nodes/), we'll use an [instance profile](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html) of each group's role to allow them to join the
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

{{% /choosable %}}

## Managed Infrastructure

In [Managed Infrastructure](/docs/guides/crosswalk/kubernetes/managed-infra/) we demonstrate deploying managed services
and how to create or use an existing virtual network with Kubernetes.

You'll want to create the Managed Infrastructure stack next, before the Cluster
Configuration stack.

### Networking

{{% choosable cloud aws %}}

How you create the network will vary on your permissions and preferences.

Typical setups will provide Kubernetes with the following resources
to use for the cluster.

* Public subnets for provisioning public load balancers.
* Private subnets for provisioning private load balancers.
* Private subnets for use as the default subnets for workers to run in.
* Managed [Pod networking](https://kubernetes.io/docs/concepts/cluster-administration/networking/).

Kubernetes requires that all subnets be [properly tagged](https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html#vpc-subnet-tagging),
in order to determine which subnets it can provision load balancers in.

To ensure proper function, pass in **all** public and/or private subnets you
intend to use into the cluster definition. If these need to be updated to include more subnets, or
if some need to be removed, the change is accomplished with a Pulumi update.

By default, [`pulumi/eks`](https://github.com/pulumi/pulumi-eks) will deploy workers into the private subnets, if
specified. If no private subnets are specified, workers will be deployed into the public
subnets that were provided. Using private subnets for
workers without associating a public IP address is highly recommended - it
creates workers that will not be publicly accessible from the Internet,
and they'll typically be shielded within your VPC.

EKS will automatically manage Kubernetes Pod networking through
the use of the [AWS CNI Plugin](https://github.com/aws/amazon-vpc-cni-k8s/). This plugin is deployed by
default on worker nodes as a [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/) named `aws-node` in all clusters
provisioned with `pulumi/eks` and is [configurable](/docs/reference/pkg/nodejs/pulumi/eks#VpcCniOptions).

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

{{% /choosable %}}

{{% choosable cloud azure %}}

How you create the network will vary on your permissions and preferences.

Typical setups will provide Kubernetes with the following resources
to use for the cluster.

* Private subnets for provisioning private load balancers.
* Private subnets for use as the default subnets for workers to run in.
* Managed [Pod networking](https://kubernetes.io/docs/concepts/cluster-administration/networking/).

By default, [`pulumi/azure`](https://github.com/pulumi/pulumi-azure) will deploy workers into the
private subnets without associating a public IP address. This
creates workers that will not be publicly accessible from the Internet,
and they'll typically be shielded within your network.

AKS will manage Kubernetes Pod networking for us through
the use of the [AKS CNI Plugin](https://docs.microsoft.com/en-us/azure/aks/configure-azure-cni). This plugin is deployed by
default on worker nodes as a [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/) named `azure-cni-networkmonitor` in all clusters
provisioned with `pulumi/azure`.

```typescript
import * as azure from "@pulumi/azure";

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

How you create the network will vary on your permissions and preferences.

Typical setups will provide Kubernetes with the following resources
to use for the cluster.

* Private subnets for use as the default subnets for workers to run in.
* Managed [Pod networking](https://kubernetes.io/docs/concepts/cluster-administration/networking/).

By default, [`pulumi/gcp`](https://github.com/pulumi/pulumi-gcp) will deploy workers into the
private subnets without associating an external IP address. This
creates workers that will not be publicly accessible from the Internet,
and they'll typically be shielded within your network.

GKE will manage Kubernetes Pod networking for us through
the use of Alias IPs to address and route pods within a GCP network.

```typescript
// Create a new network.
const network = new gcp.compute.Network(projectName, {
    autoCreateSubnetworks: false,
});
export const networkName = network.name;

// Create a new subnet.
const subnet = new gcp.compute.Subnetwork(projectName, {
    ipCidrRange: "10.0.0.0/24",
    network: network.name,
    secondaryIpRanges: [{ rangeName: "pods", ipCidrRange: "10.1.0.0/16" }],
});
export const subnetworkName = subnet.name;
```

{{% /choosable %}}

### Storage

Kubernetes [storage](https://kubernetes.io/docs/concepts/storage/) provides data persistence for
the cluster with shared storage, and/or volumes for Pods.

The volume classes are extensive and vary by cloud provider, but they
typically include volume types for mechanical drives and
SSDs, along with network backed storage such as [NFS](https://en.wikipedia.org/wiki/Network_File_System), [iSCSI](https://kubernetes.io/docs/concepts/storage/#iscsi), and [CephFS](https://docs.ceph.com/docs/master/cephfs/).

To provision [PersistentVolumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/), we have to ensure that the
desired storage classes have been created in the cluster.

> Note: At most one storage class should be marked as default.
If two or more are marked as default, each [`PersistentVolumeClaim`](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) must explicitly
specify the `storageClassName`

See the [Kubernetes docs](https://kubernetes.io/docs/concepts/storage/storage-classes/) for more details.

{{% choosable cloud aws %}}

As of Kubernetes v1.11+ on EKS, a default `gp2`
storage class will be created automatically by EKS.

See the [official EKS docs](https://docs.aws.amazon.com/eks/latest/userguide/storage-classes.html) for more details.

{{< chooser k8s-language "typescript,yaml" >}}

{{< choosable k8s-language yaml >}}

Create the storage classes using `kubectl`.

```bash
$ cat > storage-classes.yaml << EOF
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

Create the persistent volume with a persistent volume claim and `kubectl`.

```bash
$ cat > pvc.yaml << EOF
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

{{< /choosable >}}

{{< choosable k8s-language typescript >}}

Create the storage classes using Pulumi.

```typescript
import * as eks from "@pulumi/eks";

// Create an EKS cluster with custom storage classes.
const cluster = new eks.Cluster(`${projectName}`, {
    storageClasses: {
        "gp2-encrypted": { type: "gp2", encrypted: true},
        "sc1": { type: "sc1"}
    },
}
```

With storage classes created in the cluster, we can now create
persistent volumes in the cluster.

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

{{< /choosable >}}

{{< /chooser >}}

{{% /choosable %}}

{{% choosable cloud azure %}}

See the [official AKS docs](https://docs.microsoft.com/en-us/azure/aks/concepts-storage) for more details.

{{< chooser k8s-language "typescript,yaml" >}}

{{< choosable k8s-language yaml >}}

After the cluster is provisioned and running, create a StorageClass to
provision Azure disks.

Create the storage classes using `kubectl`.

```yaml
cat > storage-classes.yaml << EOF
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: managed-premium-retain
provisioner: kubernetes.io/azure-disk
parameters:
  storageaccounttype: Premium_LRS
  kind: Managed
EOF
```

```bash
$ kubectl apply -f storage-classes.yaml
```

Create the persistent volume with a persistent volume claim and `kubectl`.

```yaml
cat > pvc.yaml << EOF
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: mypvc
  labels:
    app: myapp
spec:
  storageClassName: managed-premium-retain
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

{{< /choosable >}}

{{< choosable k8s-language typescript >}}

```ts
import * as k8s from "@pulumi/k8s";

// Create the premium StorageClass.
const sc = new k8s.storage.v1.StorageClass("premium",
    {
        provisioner: "kubernetes.io/azure-disk",
        parameters: {
            "storageaccounttype": "Premium_LRS",
            "kind": "Managed"
        },
    },
    { provider: provider }
);
```

With storage classes created in the cluster, we can now create
persistent volumes in the cluster.

Create the persistent volume with a persistent volume claim and Pulumi.

```ts
import * as k8s from "@pulumi/k8s";

// Create a Persistent Volume Claim on the StorageClass.
const myPvc = new k8s.core.v1.PersistentVolumeClaim("mypvc", {
    spec: {
        accessModes: ["ReadWriteOnce"],
        storageClassName: sc.metadata.name,
        resources: {requests: {storage: "1Gi"}}
    }
},
    { provider: provider }
);
```

{{< /choosable >}}

{{< /chooser >}}

{{% /choosable %}}

{{% choosable cloud gcp %}}

See the [official GKE docs](https://cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes) for more details.

{{< chooser k8s-language "typescript,yaml" >}}

{{< choosable k8s-language yaml >}}

After the cluster is provisioned and running, create a StorageClass to
provision GCP disks.

Create the storage classes using `kubectl`.

```bash
cat > storage-classes.yaml << EOF
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: slow
provisioner: kubernetes.io/gce-pd
parameters:
  type: "pd-standard"
  replication-type: "none"
EOF
```

```bash
$ kubectl apply -f storage-classes.yaml
```

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
  storageClassName: slow
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

{{< /choosable >}}

{{< choosable k8s-language typescript >}}

```ts
import * as k8s from "@pulumi/k8s";

// Create the standard StorageClass.
const sc = new k8s.storage.v1.StorageClass("standard",
    {
        provisioner: "kubernetes.io/gce-pd",
        parameters: {
            "type": "pd-standard",
            "replication-type": "none"
        },
    },
    { provider: provider }
);
```

With storage classes created in the cluster, we can now create
persistent volumes in the cluster.

Create the persistent volume with a persistent volume claim and Pulumi.

```ts
import * as k8s from "@pulumi/k8s";

// Create a Persistent Volume Claim on the StorageClass.
const myPvc = new k8s.core.v1.PersistentVolumeClaim("mypvc", {
        spec: {
            accessModes: ["ReadWriteOnce"],
            storageClassName: sc.metadata.name,
            resources: {requests: {storage: "1Gi"}}
        }
    },
    { provider: provider }
);
```

{{< /choosable >}}

{{< /chooser >}}

{{% /choosable %}}

## Recommended Settings

With the core infrastructure in place for the control plane, there are some
general best-practices and recommendations to configure in the cluster.

**General:**

* Use a specific version of Kubernetes for the control plane. This pins the
  cluster to a particular release in a declarative manner rather than
  implicitly using the latest available version or a smart default
  that could be updated at any time.
* Instead of [using](https://blog.heptio.com/on-securing-the-kubernetes-dashboard-16b09b1b7aca) `kube-dashboard`, try [VMware's Octant](https://github.com/vmware-tanzu/octant).

{{% choosable cloud aws %}}

**EKS:**

* Tag resources under management, which makes it easier to manage, search and
  filter them.
* Skip enabling the default node group in favor of managing them separately from
  the control plane, as demonstrated in [Create the Worker Nodes](/docs/guides/crosswalk/kubernetes/worker-nodes/).
* Enable control plane logging for diagnostics of the control
  plane's actions, and for use in debugging and auditing.
* (Optional) Configure private accessibility of the control plane /
  API Server endpoint to prevent it from being publicly exposed on the
  Internet. To enable this feature, additional networking is required,
  and a [bastion host](https://docs.aws.amazon.com/quickstart/latest/linux-bastion/architecture.html) would be needed to access the control plane.

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

{{% /choosable %}}

{{% choosable cloud azure %}}

**AKS:**

* Enable [PodSecurityPolicies](https://kubernetes.io/docs/concepts/policy/pod-security-policy/) using `enablePodSecurityPolicy: true`
* Set [Node Labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) to identify nodes by attributes
* Enable Log Analytics using the `omsAgent` setting

    ```ts
    import * as azure from "@pulumi/azure";

    const cluster = new azure.containerservice.KubernetesCluster(`${name}`, {
            ...
            enablePodSecurityPolicy: true,
            kubernetesVersion: "1.14.8",
            addonProfile: {
                omsAgent: {
                    enabled: true,
                    logAnalyticsWorkspaceId: config.logAnalyticsWorkspaceId,
                },
            },
    });
    ```

{{% /choosable %}}

{{% choosable cloud gcp %}}

**GKE:**

* Enable [PodSecurityPolicies](https://kubernetes.io/docs/concepts/policy/pod-security-policy/) using `podSecurityPolicyConfig: { enabled: true }`
* Skip enabling the default node group in favor of managing them separately from
  the control plane, as demonstrated in [Create the Worker Nodes](/docs/guides/crosswalk/kubernetes/worker-nodes/).
* [Disable legacy metadata APIs](https://cloud.google.com/kubernetes-engine/docs/how-to/protecting-cluster-metadata#disable-legacy-apis) that are not v1 and do not enforce internal GCP metadata headers
* Enable control plane logging and monitoring through `oauthScopes` to have diagnostics of the control
  plane's actions, and for use in debugging and auditing.
* (Optional) Configure private accessibility of the control plane /
  API Server endpoint to prevent it from being publicly exposed on the
  Internet. To enable this feature, [additional networking](https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters) is required,
  and a [bastion host](https://cloud.google.com/nat/docs/gke-example) would be needed to access the control
  plane.

    ```typescript
    import * as gcp from "@pulumi/gcp";

    const cluster = new gcp.container.Cluster("cluster", {
            ...
            minMasterVersion: "1.14.7-gke.10",
            podSecurityPolicyConfig: { enabled: true },
            nodeConfig: {
                // We can't create a cluster without a node pool defined, but we want to
                // only use separately managed node pools. So we create the smallest
                // possible default node pool and immediately delete it.
                removeDefaultNodePool: true,
                initialNodeCount: 1,
                metadata: {
                    "disable-legacy-endpoints": "true",
                },
                oauthScopes: [
                    "https://www.googleapis.com/auth/logging.write",
                    "https://www.googleapis.com/auth/monitoring",
                ],
            },
    });
    ```

{{% /choosable %}}

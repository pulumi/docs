---
title: "Pulumi Crosswalk for Kubernetes - AWS"
linktitle: AWS
menu:
  userguides:
    parent: crosswalk-kubernetes
    identifier: crosswalk-kubernetes-aws
---

In order to run container workloads, you will need a Kubernetes cluster.
It is possible to provision and manage a cluster manually on AWS,
however the managed offering, [Elastic Kubernetes Service (EKS)][eks], offers an
easier way to get up and running.

The primary steps to follow include how to:

  * [Create the Control Plane](#create-the-control-plane)
  * [Create the Worker Nodes](#create-the-worker-nodes)
  * [Use the Cluster](#use-the-cluster)
  * [Set Defaults](#set-defaults)
  * [Use Kubernetes RBAC](#use-kubernetes-rbac)
  * [Deploy Cluster Services](#deploy-cluster-services)
  * [Deploy App Services](#deploy-app-services)
  * [Deploy Apps](#deploy-apps)
  * [Update the Worker Nodes](#update-the-worker-nodes)

The full code for this stack is on [GitHub][gh-repo-stack].

See the [official Kubernetes docs][k8s-docs] for more details.

## Create the Control Plane

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

## Create the Worker Nodes

The [worker nodes][k8s-concepts] are hosts that are responsible for
running the apps and workloads of the cluster after the control plane has 
scheduled it work. It also typically faciliates virtual networking using an
overlay or integrated network depending on setup.

Given that apps and workloads will vary in quantity, and in the resources they
require, it's wise to offer differing pools of nodes for Pods to use.

Pools can vary by machine `instanceType` for specific
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

## Use the Cluster

After running `pulumi up` the cluster will be created and there will exist
[Pulumi outputs][pulumi-outputs] with fields like the cluster's `kubeconfig`
and it's cluster name for reference and usage.

In EKS, the AWS account caller will be placed into the
`system:masters` Kubernetes RBAC group by default. The `kubeconfig`
generated will cater to this primary cluster creator use-case, and it must be
copied, and reconfigured to use with other IAM roles the caller assumes, as
demonstrated below in [Use Kubernetes RBAC](#use-kubernetes-rbac).

### Access the Cluster

To access your new Kubernetes cluster using `kubectl`, we need to setup the
`kubeconfig` file.

```bash
$ pulumi stack output kubeconfig > kubeconfig.json
```

Or in JSON pretty-print.

```bash
$ pulumi stack output kubeconfig | jq '.' > kubeconfig.json
```

Export the environment variable for `kubectl` usage.

```bash
$ export KUBECONFIG=`pwd`/kubeconfig.json
```

### Query the Cluster

Get cluster information.

```bash
$ kubectl version
$ kubectl cluster-info
```

Get nodes.

```bash
$ kubectl get nodes
$ kubectl get nodes -o wide --show-labels -l beta.kubernetes.io/instance-type=t2.medium
$ kubectl get nodes -o wide --show-labels -l beta.kubernetes.io/instance-type=t3.2xlarge
```

Get all pods.

```bash
$ kubectl get pods --all-namespaces -o wide --show-labels
```

### Deploy a Workload

Imperatively deploy a NGINX Pod and public load-balanced service:

```bash
$ kubectl run --generator=run-pod/v1 nginx --image=nginx --port=80 --expose --service-overrides='{"spec":{"type":"LoadBalancer"}}'
```

After a few moments, visit the load balancer URL.

```bash
$ if ING_LB=$((kubectl get svc nginx -o template --template='{{(index .status.loadBalancer.ingress 0).hostname}}') 2>&1) ; then echo "http://$ING_LB"; else echo "LB is not ready yet."; fi
```

Delete the pod and service.

```bash
$ kubectl delete pod/nginx svc/nginx
```

## Set Defaults

With a vanilla cluster running, create any desired resources, and logically
segment the cluster as needed.

### Namespaces

Create namespaces for typical stacks:

 * Cluster Services: Deploy cluster-scoped services, such as logging and monitoring.
 * App Services: Deploy application-scoped services, such as DNS and ingress management.
 * Apps: Deploy applications and workloads.

```typescript
import * as k8s from "@pulumi/kubernetes";

// Create Kubernetes namespaces.
const clusterSvcsNamespace = new k8s.core.v1.Namespace("cluster-svcs", undefined, { provider: cluster.provider });
export const clusterSvcsNamespaceName = clusterSvcsNamespace.metadata.name;

const appSvcsNamespace = new k8s.core.v1.Namespace("app-svcs", undefined, { provider: cluster.provider });
export const appSvcsNamespaceName = appSvcsNamespace.metadata.name;

const appNamespace = new k8s.core.v1.Namespace("apps", undefined, { provider: cluster.provider });
export const appNamespaceName = appNamespace.metadata.name;
```

### Quotas

Create [quotas][k8s-quotas] to restrict the amount of resources that can be consumed across
all Pods in a namespace.

```bash
cat > quota.yaml << EOF
apiVersion: v1
kind: ResourceQuota
metadata:
  name: quota
spec:
  hard:
    cpu: "20"
    memory: "1Gi"
    pods: "10"
    replicationcontrollers: "20"
    resourcequotas: "1"
    services: "5"
EOF
```

Create the quota using `kubectl`.

```bash
$ kubectl apply -f quota.yaml
```

or 

Create the quota using Pulumi.

```typescript
import * as k8s from "@pulumi/kubernetes";

// Create a resource quota in the apps namespace.
const quotaAppNamespace = new k8s.core.v1.ResourceQuota("apps", {
    metadata: {namespace: appNamespaceName},
    spec: {
        hard: {
            cpu: "20",
            memory: "1Gi",
            pods: "10",
            replicationcontrollers: "20",
            resourcequotas: "1",
            services: "5",
        },
    }
},{
    provider: cluster.provider
});
```

Track the quota usage in the namespace using `kubectl` and Pulumi output.

```bash
$ kubectl describe quota -n `pulumi stack output appNamespaceName`
Name:                   apps-tb8bxlvb
Namespace:              apps-x1z818eg
Resource                Used  Hard
--------                ----  ----
cpu                     0     20
memory                  0     1Gi
pods                    0     10
replicationcontrollers  0     20
resourcequotas          1     1
services                0     5
```

### PodSecurityPolicies

By default EKS ships with a fully privileged [PodSecurityPolicy][k8s-psp] named
`eks.privileged`. This privileged PSP should be removed **after** its replacements
have been created to ensure running workloads continue executing properly (order matters).

See the official [EKS Pod Security Policy][eks-psp] docs and the
[Kubernetes docs][k8s-psp] for more details.

## Use Kubernetes RBAC

### Use the admins IAM role in Kubernetes

Make a copy of the kubeconfig that will be edited for the admins.

```bash
$ cp kubeconfig.json kubeconfig-admins.json
```

Edit `kubeconfig-admins.json` by inserting a role to authenticate with in the
`args` for the [`aws-iam-authenticator`][aws-iam-auth], e.g.

```bash
...
"k8s-aws-cluster-eksCluster-1ef1afe",
"-r",
"arn:aws:iam::000000000000:role/admins-eksClusterAdmin-0627674"
```

The result should look similar to below.

```bash
{
  "apiVersion": "v1",
  "clusters": [
    {
      "cluster": {
        "certificate-authority-data": "<OMITTED>"
        "server": "https://093081F384CFC80A55E74581337E4C31.gr7.us-west-2.eks.amazonaws.com"
      },
      "name": "kubernetes"
    }
  ],
  "contexts": [
    {
      "context": {
        "cluster": "kubernetes",
        "user": "aws"
      },
      "name": "aws"
    }
  ],
  "current-context": "aws",
  "kind": "Config",
  "users": [
    {
      "name": "aws",
      "user": {
        "exec": {
          "apiVersion": "client.authentication.k8s.io/v1alpha1",
          "args": [
            "token",
            "-i",
            "k8s-aws-cluster-eksCluster-1ef1afe",
            "-r",
            "arn:aws:iam::000000000000:role/admins-eksClusterAdmin-0627674"
          ],
          "command": "aws-iam-authenticator"
        }
      }
    }
  ]
}
```

Update and use the new `kubeconfig`.

```bash
$ export KUBECONFIG=`pwd`/kubeconfig-admins.json
$ kubectl cluster-info
```

Test the admins role by using it and viewing all resources in the cluster as
expected.

```bash
$ kubectl get all -A
NAMESPACE     NAME                           READY   STATUS    RESTARTS   AGE
kube-system   pod/aws-node-6zm79             1/1     Running   0          15h
kube-system   pod/aws-node-9wmjv             1/1     Running   0          15h
kube-system   pod/aws-node-ctgxs             1/1     Running   0          15h
kube-system   pod/aws-node-nrr6n             1/1     Running   0          15h
kube-system   pod/aws-node-qbknp             1/1     Running   0          15h
kube-system   pod/aws-node-rsf75             1/1     Running   0          15h
kube-system   pod/coredns-6f647f5754-5knx2   1/1     Running   0          15h
kube-system   pod/coredns-6f647f5754-bhf6h   1/1     Running   0          15h
kube-system   pod/kube-proxy-2hhz7           1/1     Running   0          15h
kube-system   pod/kube-proxy-59lbd           1/1     Running   0          15h
kube-system   pod/kube-proxy-dchf5           1/1     Running   0          15h
kube-system   pod/kube-proxy-kdzfs           1/1     Running   0          15h
kube-system   pod/kube-proxy-r447m           1/1     Running   0          15h
kube-system   pod/kube-proxy-r9f8j           1/1     Running   0          15h

NAMESPACE     NAME                 TYPE        CLUSTER-IP    EXTERNAL-IP   PORT(S)         AGE
default       service/kubernetes   ClusterIP   10.100.0.1    <none>        443/TCP         15h
kube-system   service/kube-dns     ClusterIP   10.100.0.10   <none>        53/UDP,53/TCP   15h

NAMESPACE     NAME                        DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR   AGE
kube-system   daemonset.apps/aws-node     6         6         6       6            6           <none>          15h
kube-system   daemonset.apps/kube-proxy   6         6         6       6            6           <none>          15h

NAMESPACE     NAME                      READY   UP-TO-DATE   AVAILABLE   AGE
kube-system   deployment.apps/coredns   2/2     2            2           15h

NAMESPACE     NAME                                 DESIRED   CURRENT   READY   AGE
kube-system   replicaset.apps/coredns-6f647f5754   2         2         2       15h
```

### Use the developers IAM role in Kubernetes

Make a copy of the kubeconfig that will be edited for the developers.

```bash
$ cp kubeconfig.json kubeconfig-devs.json
```

Edit `kubeconfig-devs.json` by inserting a role to authenticate with in the
`args` for the [`aws-iam-authenticator`][aws-iam-auth], e.g.

```bash
...
"k8s-aws-cluster-eksCluster-1ef1afe",
"-r",
"arn:aws:iam::000000000000:role/devs-eksClusterDeveloper-e332028"
```

The result should look similar to below.

```bash
{
  "apiVersion": "v1",
  "clusters": [
    {
      "cluster": {
        "certificate-authority-data": "<OMITTED>"
        "server": "https://093081F384CFC80A55E74581337E4C31.gr7.us-west-2.eks.amazonaws.com"
      },
      "name": "kubernetes"
    }
  ],
  "contexts": [
    {
      "context": {
        "cluster": "kubernetes",
        "user": "aws"
      },
      "name": "aws"
    }
  ],
  "current-context": "aws",
  "kind": "Config",
  "users": [
    {
      "name": "aws",
      "user": {
        "exec": {
          "apiVersion": "client.authentication.k8s.io/v1alpha1",
          "args": [
            "token",
            "-i",
            "k8s-aws-cluster-eksCluster-1ef1afe",
            "-r",
            "arn:aws:iam::000000000000:role/devs-eksClusterDeveloper-e332028"
          ],
          "command": "aws-iam-authenticator"
        }
      }
    }
  ]
}
```

Update and use the new `kubeconfig`.

```bash
$ export KUBECONFIG=`pwd`/kubeconfig-devs.json
```

Test the developers role by using it and witnessing a lack of privileges.

```bash
$ kubectl get all -A
Error from server (Forbidden): pods is forbidden: User "pulumi:alice" cannot list resource "pods" in API group "" at the cluster scope
Error from server (Forbidden): replicationcontrollers is forbidden: User "pulumi:alice" cannot list resource "replicationcontrollers" in API group "" at the cluster scope
Error from server (Forbidden): services is forbidden: User "pulumi:alice" cannot list resource "services" in API group "" at the cluster scope
Error from server (Forbidden): daemonsets.apps is forbidden: User "pulumi:alice" cannot list resource "daemonsets" in API group "apps" at the cluster scope
Error from server (Forbidden): deployments.apps is forbidden: User "pulumi:alice" cannot list resource "deployments" in API group "apps" at the cluster scope
Error from server (Forbidden): replicasets.apps is forbidden: User "pulumi:alice" cannot list resource "replicasets" in API group "apps" at the cluster scope
Error from server (Forbidden): statefulsets.apps is forbidden: User "pulumi:alice" cannot list resource "statefulsets" in API group "apps" at the cluster scope
Error from server (Forbidden): horizontalpodautoscalers.autoscaling is forbidden: User "pulumi:alice" cannot list resource "horizontalpodautoscalers" in API group "autoscaling" at the cluster scope
Error from server (Forbidden): jobs.batch is forbidden: User "pulumi:alice" cannot list resource "jobs" in API group "batch" at the cluster scope
Error from server (Forbidden): cronjobs.batch is forbidden: User "pulumi:alice" cannot list resource "cronjobs" in API group "batch" at the cluster scope
```

### Configure Kubernetes RBAC

IAM is not configured by default with Kubernetes RBAC.

For example, in [Use the developers IAM role](#use-the-developers-iam-role-in-kubernetes) the
user is authenticated into the cluster using the IAM role, but it is not yet
authorized to do work in the cluster. This means that it cannot perform any operations in the cluster by
default, or retrieve information as shown in the `Error from server (Forbidden)`
messages.

```bash
$ export KUBECONFIG=`pwd`/kubeconfig-devs.json
$ kubectl run --generator=run-pod/v1 nginx --image=nginx --port=80 --expose --service-overrides='{"spec":{"type":"LoadBalancer"}}' -n `pulumi stack output appNamespaceName` --limits cpu=200m,memory=256Mi
Error from server (Forbidden): pods is forbidden: User "pulumi:alice" cannot create resource "pods" in API group "" in the namespace "apps-x1z818eg"
```

To allow the devs group to operate in the cluster, we must create [Kubernetes RBAC][k8s-rbac-docs]
resources to bind the IAM role to certain privileges.

Create a role with the ability to deploy common workloads **only** in the
`apps` namespace, created earlier during the setup of [cluster defaults](#set-defaults).

```typescript
import * as k8s from "@pulumi/kubernetes";

// Create a limited role for the `pulumi:devs` to use in the apps namespace.
let devsGroupRole = new k8s.rbac.v1.Role("pulumi-devs",
    {
        metadata: {
            namespace: appNamespaceName,
        },
        rules: [
            {
                apiGroups: ["", "apps"],
                resources: ["pods", "deployments", "replicasets", "persistentvolumeclaims"],
                verbs: ["get", "list", "watch", "create", "update", "delete"],
            },
        ],
    },
    {
        provider: cluster.provider,
    },
);

// Bind the `pulumi:devs` RBAC group to the new, limited role.
let devsGroupRoleBinding = new k8s.rbac.v1.RoleBinding("pulumi-devs", {
	metadata: {
		namespace: appNamespaceName,
	},
    subjects: [{
        kind: "Group",
        name: "pulumi:devs",
    }],
    roleRef: {
        kind: "Role",
        name: devsGroupRole.metadata.name,
        apiGroup: "rbac.authorization.k8s.io",
    },
}, {provider: cluster.provider});
```

After creating the `Role` and `RoleBinding` during a pulumi update, now try
deploying the workload with the new authorization.

```bash
$ kubectl run --generator=run-pod/v1 nginx --image=nginx --port=80 --expose --service-overrides='{"spec":{"type":"LoadBalancer"}}' -n `pulumi stack output appNamespaceName` --limits cpu=200m,memory=256Mi
service/nginx created
pod/nginx created
```

Delete the pod and service.

```bash
$ kubectl delete pod/nginx svc/nginx
```

For a complete example of this in action, please see [Simplifying Kubernetes
RBAC in Amazon EKS][simplify-rbac].

See the [official Kubernetes RBAC docs][k8s-rbac-docs] for more details.

## Deploy Cluster Services

TODO

[Cluster Services][crosswalk-aws-cluster-svcs].

## Deploy App Services

TODO

[App Services][crosswalk-aws-app-svcs].

## Deploy Apps

[Apps][crosswalk-aws-apps].

## Update the Worker Nodes

### Update an Existing Node Group

Updating an existing node group can be trivial for basic changes.

1. Verify that enough capacity is available in the cluster to handle workload
   spillover when the desired node group is scaled down.
1. Edit the `desiredCapacity` and `minSize` of the node group to scale down to
   a value of `0`.
1. Run an update with `pulumi up`.
1. Update the desired node group properties, such as the `instanceType` or `amiId`.
1. Run an update with `pulumi up`.

   > Note: [Don't drift][k8s-version-skew] far apart in minor Kubernetes versions between
   > the node group workers and the control plane.

See the [official AWS docs][aws-update-ng] for more details.

### Migrate to a New Node Group

For a complete example of migrating node groups, please see [Migrating Node Groups with Zero Downtime][migrate-ng-tutorial].  

See the [official AWS docs][aws-migrate-ng] for more details.

[k8s-labels]: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/
[k8s-taints]: https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/
[pulumi-outputs]: https://www.pulumi.com/docs/intro/concepts/programming-model/#outputs
[k8s-version-skew]: https://kubernetes.io/docs/setup/release/version-skew-policy/#supported-version-skew
[migrate-ng-tutorial]: {{< relref "/docs/tutorials/kubernetes/eks-migrate-nodegroups" >}}
[aws-update-ng]: https://docs.aws.amazon.com/eks/latest/userguide/update-stack.html
[aws-migrate-ng]: https://docs.aws.amazon.com/eks/latest/userguide/migrate-stack.html
[aws-k8s-cni]: https://github.com/aws/amazon-vpc-cni-k8s/
[k8s-quotas]: https://kubernetes.io/docs/concepts/policy/resource-quotas/#compute-resource-quota
[eks-psp]: https://docs.aws.amazon.com/eks/latest/userguide/pod-security-policy.html
[k8s-psp]: https://kubernetes.io/docs/concepts/policy/pod-security-policy/
[k8s-docs]: https://kubernetes.io/docs/reference/
[gh-repo-stack]: https://github.com/metral/kubernetes-the-prod-way/tree/metral/crosswalk/aws/03-cluster-configuration
[aws-iam-auth]: https://docs.aws.amazon.com/eks/latest/userguide/install-aws-iam-authenticator.html
[simplify-rbac]: /blog/simplify-kubernetes-rbac-in-amazon-eks-with-open-source-pulumi-packages/
[k8s-rbac-docs]: https://kubernetes.io/docs/reference/access-authn-authz/rbac/
[eks]: https://aws.amazon.com/eks/
[k8s-concepts]: https://kubernetes.io/docs/concepts
[crosswalk-aws-identity]: {{< relref "/docs/guides/crosswalk/kubernetes/aws/identity" >}}
[crosswalk-aws-infra]: {{< relref "/docs/guides/crosswalk/kubernetes/aws/managed-infra" >}}
[crosswalk-aws-cluster-svcs]: {{< relref "/docs/guides/crosswalk/kubernetes/aws/cluster-services" >}}
[crosswalk-aws-app-svcs]: {{< relref "/docs/guides/crosswalk/kubernetes/aws/app-services" >}}
[crosswalk-aws-apps]: {{< relref "/docs/guides/crosswalk/kubernetes/aws/apps" >}}
[role-mapping]: {{< relref "/docs/reference/pkg/nodejs/pulumi/eks#RoleMapping" >}}
[user-mapping]: {{< relref "/docs/reference/pkg/nodejs/pulumi/eks#UserMapping" >}}
[aws-instance-profile]: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html
[pulumi-eks]: https://github.com/pulumi/pulumi-eks
[eks-subnet-tagging]: https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html#vpc-subnet-tagging
[k8s-storage]: https://kubernetes.io/docs/concepts/storage/
[nfs]: https://en.wikipedia.org/wiki/Network_File_System
[aws-efs]: https://aws.amazon.com/efs/
[ceph-fs]: https://docs.ceph.com/docs/master/cephfs/
[eks-storage-classes]: https://docs.aws.amazon.com/eks/latest/userguide/storage-classes.html
[k8s-storage-classes-default]: https://kubernetes.io/docs/tasks/administer-cluster/change-default-storage-class/#changing-the-default-storageclass
[aws-bastion]: https://docs.aws.amazon.com/quickstart/latest/linux-bastion/architecture.html
[nodegroups]: #create-the-worker-nodes
[kube-dash-security]: https://blog.heptio.com/on-securing-the-kubernetes-dashboard-16b09b1b7aca
[octant]: https://github.com/vmware-tanzu/octant
[configure-cni]: {{< relref "/docs/reference/pkg/nodejs/pulumi/eks#VpcCniOptions" >}}
[k8s-kubelet]: https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/
[k8s-pvs]: https://kubernetes.io/docs/concepts/storage/persistent-volumes/
[k8s-pod-networking]: https://kubernetes.io/docs/concepts/cluster-administration/networking/
[k8s-ds]: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/
[crosswalk-sgs]: {{< relref "/docs/guides/crosswalk/aws/vpc#configuring-security-groups-for-a-vpc" >}}
[k8s-cluster-autoscaler]: https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler
[k8s-node-selector]: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/

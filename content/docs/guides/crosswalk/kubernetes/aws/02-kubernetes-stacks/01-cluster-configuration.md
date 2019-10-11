---

title: Kubernetes Cluster

aliases: ["/docs/guides/crosswalk/kubernetes/aws/cluster/"]
---

Manage the control plane, worker nodes, RBAC, and defaults.

  * [Create the Control Plane](#create-the-control-plane)
  * [Create the Worker Nodes](#create-the-worker-nodes)
  * [Use the Cluster](#use-the-cluster)
  * [Setting Defaults](#setting-defaults)
  * [Use Kuberntes RBAC](#use-kubernetes-rbac)
  * [Updating the Worker Nodes](#updating-the-worker-nodes)


The full code for this stack is on [GitHub][gh-repo-stack].

See the [official Kubernetes docs][k8s-docs] for more details.

## Create the Control Plane

Create a new EKS cluster control plane equipped with:

**Identity**

  * IAM roles for each worker node group.
  * IAM roles for users mapped into Kubernetes RBAC.

**Networking**

  * Public subnets for use with public load balancers.
  * Private subnets for use with private load balancers.
  * Private subnets used as the default subnets for workers, by design.
  * Pod networking managed by the [AWS CNI Plugin][aws-k8s-cni].

**Storage**

  * Default Kubernetes storage classes backed by cloud volume types.

**Workers**

  * No default worker node group in favor of specific, separately managed node groups.

**General**

  * A specific version of Kubernetes for the control plane.
  * Tags for resources under cluster management.
  * Control plane logging enabled.
  * Configurable accessibility for the cluster API endpoint (optional).

    ```typescript
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
            "gp2": { type: "gp2", encrypted: true},
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

Create new worker node groups equipped with:

**Identity**

  * IAM role instance profiles for each worker node group.

**Networking**

  * No public IP addresses assigned to node group workers.
  * Configurable security groups and ingress rules.

**Workers**

  * An AMI for a specific version of Kubernetes to use against the control plane.
  * Separate machine types by use-case.
  * Workers placed in an Auto Scaling Group.
  * Desired capacity, min, and max sizes of the node group.

**General**

  * Kubernetes [labels][k8s-labels] and [taints][k8s-taints] for worker node segmentation and scheduling.
  * Tags for resources under cluster management.

	```typescript
	import * as eks from "@pulumi/eks";
	
    // Create a Standard node group of t2.medium workers.
    const ngStandard = new eks.NodeGroup(`${projectName}-ng-standard`, {
        cluster: cluster,
        instanceProfile: new aws.iam.InstanceProfile("ng-standard-instanceProfile", {role: stdNodegroupIamRoleName}),
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
        instanceProfile: new aws.iam.InstanceProfile("ng-2xlarge-instanceProfile", {role: perfNodegroupIamRoleName}),
        nodeAssociatePublicIpAddress: false,
        nodeSecurityGroup: cluster.nodeSecurityGroup,
        clusterIngressRule: cluster.eksClusterIngressRule,
        amiId: "ami-0ca5998dc2c88e64b", // k8s v1.14.7 in us-west-2
        instanceType: "t3.2xlarge",
        desiredCapacity: 3,
        minSize: 3,
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

### Access the cluster

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

### Query the cluster

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

### Deploy a workload

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

## Setting Defaults

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

Create the quota using `pulumi`.

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

Test the developers role by using it and witnessing lack of privileges.

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
authorized. This means that it cannot perform any operations on the cluster by
default or retrieve information as shown in the `Error from server (Forbidden)`
messages.

```bash
$ export KUBECONFIG=`pwd`/kubeconfig-devs.json
$ kubectl run --generator=run-pod/v1 nginx --image=nginx --port=80 --expose --service-overrides='{"spec":{"type":"LoadBalancer"}}' -n `pulumi stack output appNamespaceName` --limits cpu=200m,memory=256Mi
Error from server (Forbidden): pods is forbidden: User "pulumi:alice" cannot create resource "pods" in API group "" in the namespace "apps-x1z818eg"
```

To allow the devs group to operate in the cluster, we must create [Kubernetes RBAC][k8s-rbac-docs]
resources to bind the IAM role to certain privileges.

Create a role with the ability to deploy common workloads **only** in the
`apps` namespace, created earlier during the setup of [cluster defaults](#setting-defaults).

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

## Updating the Worker Nodes

### Updating an Existing Node Group

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

### Migrating to a New Node Group

For a complete example of migrating node groups, please see [Migrating Node Groups with Zero Downtime][migrate-ng-tutorial].  

See the [official AWS docs][aws-migrate-ng] for more details.

[k8s-labels]: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/
[k8s-taints]: https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/
[pulumi-outputs]: https://www.pulumi.com/docs/intro/concepts/programming-model/#outputs
[k8s-version-skew]: https://kubernetes.io/docs/setup/release/version-skew-policy/#supported-version-skew
[migrate-ng-tutorial]: /docs/tutorials/kubernetes/eks-migrate-nodegroups/
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

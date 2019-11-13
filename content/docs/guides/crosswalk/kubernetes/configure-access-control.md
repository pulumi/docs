---
title: Configure Access Control
menu:
  userguides:
    parent: crosswalk-kubernetes
    identifier: crosswalk-kubernetes-configure-authorization
    weight: 5
---

{{< cloudchoose >}}

<div class="cloud-prologue-aws"></div>
<div class="mt">
{{% md %}}

Access control in Kubernetes is done by configuring permissions for IAM users
and roles to operate in the cluster.

The `kubeconfig` will be shared across users for access, and each IAM role
will have a particular binding into the cluster's auth to determine how it works
with the cluster.

The full code for this stack is on [GitHub][gh-repo-stack].
[gh-repo-stack]: https://github.com/pulumi/kubernetes-the-prod-way/tree/master/aws/03-cluster-configuration

{{% /md %}}
</div>

<div class="cloud-prologue-azure"></div>
<div class="mt">
{{% md %}}

Access control in Kubernetes is done by configuring permissions for Azure Active Directory (AD) users
and groups to operate in the cluster.

The `kubeconfig` will contain user authentication tokens for access, and each AD group
will have a particular binding into the cluster's auth to determine how it works
with the cluster.

The full code for this stack is on [GitHub][gh-repo-stack].
[gh-repo-stack]: https://github.com/pulumi/kubernetes-the-prod-way/tree/master/azure/03-cluster-configuration

{{% /md %}}
</div>

<div class="cloud-prologue-gcp"></div>
<div class="mt">
{{% md %}}

Access control in Kubernetes is done by configuring permissions for IAM
ServiceAccounts to operate in the cluster.

The `kubeconfig` will be shared across ServiceAccounts for access, and each
ServiceAccount will have a particular binding into the cluster's auth to determine how it works
with the cluster.

The full code for this stack is on [GitHub][gh-repo-stack].
[gh-repo-stack]: https://github.com/pulumi/kubernetes-the-prod-way/tree/master/gcp/03-cluster-configuration

{{% /md %}}
</div>

## Overview

We'll examine how to:

  * [Configure RBAC Authorization](#configure-rbac-authorization)

## Configure RBAC Authorization

<div class="cloud-prologue-azure"></div>
<div class="mt">
{{% md %}}

Access control is not configured by default for **non-admins** with Kubernetes RBAC.

In [Identity][crosswalk-identity] developers can **authenticate** into the cluster
using the kubeconfig, but they are not yet **authorized** to do work in the cluster.

This means that the user cannot perform any operations in the cluster by
default, such as retrieve information, as shown in the `Error from server (Forbidden)`
messages.

```bash
$ az login --service-principal --username $ARM_CLIENT_ID --password $ARM_CLIENT_SECRET --tenant $ARM_TENANT_ID
$ export KUBECONFIG=`pwd`/kubeconfig-devs.json
$ kubectl run --namespace=`pulumi stack output appsNamespaceName` --generator=run-pod/v1 nginx --image=nginx --port=80 --expose --service-overrides='{"spec":{"type":"LoadBalancer"}}' --limits cpu=200m,memory=256Mi
Error from server (Forbidden): pods is forbidden: User "pulumi:alice" cannot create resource "pods" in API group "" in the namespace "apps-x1z818eg"
```

Below is an example of how to create a Kubernetes Role and RoleBiding for the `devs` to **only** deploy common
workloads in the `apps` namespace (created in  [cluster defaults][crosswalk-configure-defaults]).

Assume the `admin` user.

```ts
$ az login --service-principal --username $ARM_CLIENT_ID --password $ARM_CLIENT_SECRET --tenant $ARM_TENANT_ID
$ export KUBECONFIG=`pwd`/kubeconfig-admin.json
```
[crosswalk-configure-defaults]: {{< relref "/docs/guides/crosswalk/kubernetes/configure-defaults" >}}
[crosswalk-identity]: {{< relref "/docs/guides/crosswalk/kubernetes/identity" >}}

{{% /md %}}
</div>

<div class="cloud-prologue-aws"></div>
<div class="mt">
{{% md %}}

Access control is not configured by default for **non-admins** with Kubernetes RBAC.

In [Identity][crosswalk-identity] developers can **authenticate** into the cluster
using the IAM role and kubeconfig, but it is not yet **authorized** to do work in the cluster.

This means that the user cannot perform any operations in the cluster by
default such as retrieve information, as shown in the `Error from server (Forbidden)`
messages.

```bash
$ aws sts assume-role --role-arn `pulumi stack output devsIamRoleArn` --role-session-name k8s-devs
$ export KUBECONFIG=`pwd`/kubeconfig-devs.json
$ kubectl run --namespace=`pulumi stack output appsNamespaceName` --generator=run-pod/v1 nginx --image=nginx --port=80 --expose --service-overrides='{"spec":{"type":"LoadBalancer"}}' --limits cpu=200m,memory=256Mi
Error from server (Forbidden): pods is forbidden: User "pulumi:alice" cannot create resource "pods" in API group "" in the namespace "apps-x1z818eg"
```

Below is an example of how to create a Kubernetes `Role` with the ability to **only** deploy common
workloads in the `apps` namespace (created in [cluster defaults][crosswalk-configure-defaults]). We also create a `RoleBinding`
to associate the Kubernetes `Role` to the IAM `devs` role.

Assume the `admin` user.

```bash
$ aws sts assume-role --role-arn `pulumi stack output adminsIamRoleArn` --role-session-name k8s-admins
$ export KUBECONFIG=`pwd`/kubeconfig-admin.json
```
[crosswalk-configure-defaults]: {{< relref "/docs/guides/crosswalk/kubernetes/configure-defaults" >}}
[crosswalk-identity]: {{< relref "/docs/guides/crosswalk/kubernetes/identity" >}}
{{% /md %}}
</div>

<div class="cloud-prologue-gcp"></div>
<div class="mt">
{{% md %}}

In [Identity][crosswalk-identity], access control is configured on the ServiceAccounts to bind to
[Predefined GKE Roles][gke-predefined-roles] for GKE managed Kubernetes RBAC.

If you wish to not bind a ServiceAccount to predefined GKE roles,
the user will be able to **authenticate** into the cluster, but they will not be
**authorized** to do work until given permissions.

This means that the user cannot perform any operations in the cluster by
default such as retrieve information, as shown in the `Error from server (Forbidden)`
messages.

```bash
$ gcloud auth activate-service-account --key-file k8s-devs-sa-key.json
$ export KUBECONFIG=`pwd`/kubeconfig.json
$ kubectl run --namespace=`pulumi stack output appsNamespaceName` --generator=run-pod/v1 nginx --image=nginx --port=80 --expose --service-overrides='{"spec":{"type":"LoadBalancer"}}' --limits cpu=200m,memory=256Mi
Error from server (Forbidden): pods is forbidden: User "pulumi:alice" cannot create resource "pods" in API group "" in the namespace "apps-x1z818eg"
```

As an example, if the `devs` ServiceAccount was not bound to the `roles/container.developer` permission,
an `admin` would need to create [Kubernetes RBAC][k8s-rbac-docs] resources to bind the ServiceAccount to certain privileges.

Below is an example of how to create a Kubernetes `Role` with the ability to **only** deploy common
workloads in the `apps` namespace (created in [cluster defaults][crosswalk-configure-defaults]), and a `RoleBinding` to associate
the Kubernetes `Role` to the IAM `devs` role.

[crosswalk-configure-defaults]: {{< relref "/docs/guides/crosswalk/kubernetes/configure-defaults" >}}
[k8s-rbac-docs]: https://kubernetes.io/docs/reference/access-authn-authz/rbac/
[gke-predefined-roles]: https://cloud.google.com/kubernetes-engine/docs/how-to/iam#predefined
[crosswalk-identity]: {{< relref "/docs/guides/crosswalk/kubernetes/identity" >}}

Assume the `admin` user.

```bash
$ gcloud auth activate-service-account --key-file k8s-admin-sa-key.json
$ export KUBECONFIG=`pwd`/kubeconfig-admin.json
```
{{% /md %}}
</div>

Create a Role and RoleBinding for the `pulumi-devs` group in the `apps`
Namespace.

```typescript
import * as k8s from "@pulumi/kubernetes";

// Create a limited role for the `pulumi:devs` to use in the apps namespace.
let devsGroupRole = new k8s.rbac.v1.Role("pulumi-devs",
    {
        metadata: {namespace: appNamespaceName},
        rules: [
            {
                apiGroups: [""],
                resources: ["pods", "secrets", "services", "persistentvolumeclaims"],
                verbs: ["get", "list", "watch", "create", "update", "delete"],
            },
            {
                apiGroups: ["extensions", "apps"],
                resources: ["replicasets", "deployments"],
                verbs: ["get", "list", "watch", "create", "update", "delete"],
            },
        ],
    },
    {provider: cluster.provider},
);

// Bind the `pulumi:devs` RBAC group to the new, limited role.
let devsGroupRoleBinding = new k8s.rbac.v1.RoleBinding("pulumi-devs", {
	metadata: {namespace: appNamespaceName},
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

<div class="cloud-prologue-aws"></div>
<div class="mt">
{{% md %}}
After creating the Role and RoleBinding in a Pulumi update, now try
deploying the workload using the `devs` role.

```bash
$ aws sts assume-role --role-arn `pulumi stack output devsIamRoleArn` --role-session-name k8s-devs
$ export KUBECONFIG=`pwd`/kubeconfig-devs.json
$ kubectl run --namespace=`pulumi stack output appsNamespaceName` --generator=run-pod/v1 nginx --image=nginx --port=80 --expose --service-overrides='{"spec":{"type":"LoadBalancer"}}' --limits cpu=200m,memory=256Mi
service/nginx created
pod/nginx created
```
{{% /md %}}
</div>
<div class="cloud-prologue-azure"></div>
<div class="mt">
{{% md %}}
After creating the Role and RoleBinding in a Pulumi update, now try
deploying the workload using the `devs` role.

```bash
$ az login --service-principal --username $ARM_CLIENT_ID --password $ARM_CLIENT_SECRET --tenant $ARM_TENANT_ID
$ export KUBECONFIG=`pwd`/kubeconfig-devs.json
$ kubectl run --namespace=`pulumi stack output appsNamespaceName` --generator=run-pod/v1 nginx --image=nginx --port=80 --expose --service-overrides='{"spec":{"type":"LoadBalancer"}}' --limits cpu=200m,memory=256Mi
service/nginx created
pod/nginx created
```
{{% /md %}}
</div>
<div class="cloud-prologue-gcp"></div>
<div class="mt">
{{% md %}}
After creating the Role and RoleBinding in a Pulumi update, now try
deploying the workload using the `devs` role.

```bash
$ gcloud auth activate-service-account --key-file k8s-devs-sa-key.json
$ export KUBECONFIG=`pwd`/kubeconfig.json
$ kubectl run --namespace=`pulumi stack output appsNamespaceName` --generator=run-pod/v1 nginx --image=nginx --port=80 --expose --service-overrides='{"spec":{"type":"LoadBalancer"}}' --limits cpu=200m,memory=256Mi
service/nginx created
pod/nginx created
```
{{% /md %}}
</div>

Delete the pod and service.

```bash
$ kubectl delete --namespace=`pulumi stack output appsNamespaceName` pod/nginx svc/nginx
```

<div class="cloud-prologue-aws"></div>
<div class="mt">
{{% md %}}

For a complete example of this in action, please see [Simplifying Kubernetes
RBAC in Amazon EKS][simplify-rbac].
[simplify-rbac]: /blog/simplify-kubernetes-rbac-in-amazon-eks-with-open-source-pulumi-packages/

{{% /md %}}
</div>

See the [official Kubernetes RBAC docs][k8s-rbac-docs] for more details.

[crosswalk-identity]: {{< relref "/docs/guides/crosswalk/kubernetes/identity" >}}
[k8s-rbac-docs]: https://kubernetes.io/docs/reference/access-authn-authz/rbac/
[crosswalk-configure-defaults]: {{< relref "/docs/guides/crosswalk/kubernetes/configure-defaults" >}}

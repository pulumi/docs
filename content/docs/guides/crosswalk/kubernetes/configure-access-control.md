---
title: Configure Access Control
menu:
  userguides:
    parent: crosswalk-kubernetes
    identifier: crosswalk-kubernetes-configure-authorization
    weight: 6
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
[gh-repo-stack]: https://github.com/pulumi/kubernetes-the-prod-way/tree/crosswalk/aws/03-cluster-configuration

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
[gh-repo-stack]: https://github.com/pulumi/kubernetes-the-prod-way/tree/crosswalk/azure/03-cluster-configuration

{{% /md %}}
</div>

<div class="cloud-prologue-gcp"></div>
<div class="mt">
{{% md %}}

The full code for this stack is on [GitHub][gh-repo-stack].
[gh-repo-stack]: https://github.com/pulumi/kubernetes-the-prod-way/tree/crosswalk/gcp/03-cluster-configuration

{{% /md %}}
</div>

## Overview

We'll examine how to:

<div class="cloud-prologue-aws"></div>
<div class="mt">
{{% md %}}

  * [Use the `admins` IAM Role](#use-the-admins-iam-role)
  * [Use the `devs` IAM Role](#use-the-devs-iam-role)
  * [Configure RBAC Authorization](#configure-rbac-authorization)

### Use the `admins` IAM role

In [Identity][crosswalk-identity] we demonstrate how to create typical IAM roles for
use in Kubernetes.

We created an `admins` role for cluster administrators with root privileges, that
will be tied into Kubernetes RBAC.

Make a copy of the kubeconfig that will be edited for the `admins`.

```bash
$ cp kubeconfig.json kubeconfig-admins.json
```

Edit `kubeconfig-admins.json` by inserting a role to authenticate with in the
`args` for the [`aws-iam-authenticator`][aws-iam-auth], e.g.

```bash
...
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
```

Update and use the new `kubeconfig`.

```bash
$ export KUBECONFIG=`pwd`/kubeconfig-admins.json
$ kubectl cluster-info
```

Test the `admins` role by using it and viewing all resources in the cluster as
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

[aws-iam-auth]: https://docs.aws.amazon.com/eks/latest/userguide/install-aws-iam-authenticator.html
{{% /md %}}
</div>

<div class="cloud-prologue-azure"></div>
<div class="mt">
{{% md %}}

  * [Use the `admins` AD Group](#use-the-admins-ad-group)
  * [Use the `devs` AD Group](#use-the-devs-iam-group)
  * [Configure RBAC Authorization](#configure-rbac-authorization)

### Use the `admins` AD group

In [Identity][crosswalk-identity] we demonstrate how to create typical roles for
use in Kubernetes.

We created an `admins` role for cluster administrators with root privileges, that
will be tied into Kubernetes RBAC.

Start with the `kubeconfig` exported from the Pulumi stack. It has no Active Directory authentication information.

Use `kubectl` to retrieve cluster information. You will see a prompt to log in:

```bash
$ kubectl cluster-info
To sign in, use a web browser to open the page https://microsoft.com/devicelogin and enter the code CF3TDACCY to authenticate.
```

Proceed to the webpage and use the mentioned code to authenticate as an administrator user. The interactive login is only required once: the successful attempt will save the token to the `kubeconfig` file.

After the login, cluster information will be displayed in the command-line console.
{{% /md %}}
</div>

<div class="cloud-prologue-gcp"></div>
<div class="mt">
{{% md %}}

TODO

```typescript
// TODO
```

{{% /md %}}
</div>

<div class="cloud-prologue-aws"></div>
<div class="mt">
{{% md %}}

### Use the `devs` IAM role

In [Identity][crosswalk-identity] we demonstrate how to create typical IAM roles for
use in Kubernetes.

We create limited scope `devs` role for general purpose execution of workloads,
that will be tied into Kubernetes RBAC.

Make a copy of the kubeconfig that will be edited for the `devs`.

```bash
$ cp kubeconfig.json kubeconfig-devs.json
```

Edit `kubeconfig-devs.json` by inserting a role to authenticate with in the
`args` for the [`aws-iam-authenticator`][aws-iam-auth], e.g.

```bash
...
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
```

Update and use the new `kubeconfig`.

```bash
$ export KUBECONFIG=`pwd`/kubeconfig-devs.json
```

Test the `devs` role by using it and witnessing a lack of privileges.

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

[aws-iam-auth]: https://docs.aws.amazon.com/eks/latest/userguide/install-aws-iam-authenticator.html
{{% /md %}}
</div>

<div class="cloud-prologue-azure"></div>
<div class="mt">
{{% md %}}

### Use the `devs` AD group

In [Identity][crosswalk-identity] we demonstrate how to create typical roles for
use in Kubernetes.

We create limited scope `devs` role for general purpose execution of workloads,
that will be tied into Kubernetes RBAC.

Start with the `kubeconfig` exported from the Pulumi stack. It has no Active Directory authentication information.

Use `kubectl` to retrieve cluster information. You will see a prompt to log in:

```bash
$ kubectl cluster-info
To sign in, use a web browser to open the page https://microsoft.com/devicelogin and enter the code CF3TDACCY to authenticate.
```

Proceed to the webpage and use the mentioned code to authenticate as an dev user. The interactive login is only required once: the successful attempt will save the token to the `kubeconfig` file.

After the login, cluster information retrieval fails because of lack of permissions:

```bash
Error from server (Forbidden): services is forbidden: User "alice@example.com" cannot list resource "services" in API group "" in the namespace "kube-system"
```

Test the `devs` role by using it and witnessing a lack of privileges.

```bash
$ kubectl get all
Error from server (Forbidden): pods is forbidden: User "alice@example.com" cannot list resource "pods" in API group "" at the cluster scope
Error from server (Forbidden): replicationcontrollers is forbidden: User "alice@example.com" cannot list resource "replicationcontrollers" in API group "" at the cluster scope
Error from server (Forbidden): services is forbidden: User "alice@example.com" cannot list resource "services" in API group "" at the cluster scope
Error from server (Forbidden): daemonsets.apps is forbidden: User "alice@example.com" cannot list resource "daemonsets" in API group "apps" at the cluster scope
Error from server (Forbidden): deployments.apps is forbidden: User "alice@example.com" cannot list resource "deployments" in API group "apps" at the cluster scope
Error from server (Forbidden): replicasets.apps is forbidden: User "alice@example.com" cannot list resource "replicasets" in API group "apps" at the cluster scope
Error from server (Forbidden): statefulsets.apps is forbidden: User "alice@example.com" cannot list resource "statefulsets" in API group "apps" at the cluster scope
Error from server (Forbidden): horizontalpodautoscalers.autoscaling is forbidden: User "alice@example.com" cannot list resource "horizontalpodautoscalers" in API group "autoscaling" at the cluster scope
Error from server (Forbidden): jobs.batch is forbidden: User "alice@example.com" cannot list resource "jobs" in API group "batch" at the cluster scope
Error from server (Forbidden): cronjobs.batch is forbidden: User "alice@example.com" cannot list resource "cronjobs" in API group "batch" at the cluster scope
```
{{% /md %}}
</div>

<div class="cloud-prologue-gcp"></div>
<div class="mt">
{{% md %}}

TODO

```typescript
// TODO
```

{{% /md %}}
</div>

### Configure RBAC Authorization

Access control is not configured by default with Kubernetes RBAC.

In [Use the `devs` IAM role](#use-the-devs-iam-role) the
user is **authenticated** into the cluster using the IAM role, but it is not yet
**authorized** to do work in the cluster.

This means that the user cannot perform any operations in the cluster by
default, or retrieve information as shown in the `Error from server (Forbidden)`
messages.

```bash
$ export KUBECONFIG=`pwd`/kubeconfig-devs.json
$ kubectl run --generator=run-pod/v1 nginx --image=nginx --port=80 --expose --service-overrides='{"spec":{"type":"LoadBalancer"}}' -n `pulumi stack output appNamespaceName` --limits cpu=200m,memory=256Mi
Error from server (Forbidden): pods is forbidden: User "pulumi:alice" cannot create resource "pods" in API group "" in the namespace "apps-x1z818eg"
```

For example, to allow the `devs` group to operate in the cluster, we must create [Kubernetes RBAC][k8s-rbac-docs]
resources to bind the IAM role to certain privileges.

Below we create the Kubernetes `Role` with the ability to **only** deploy common
workloads in the `apps` namespace, created earlier during the configuration of
[cluster defaults][crosswalk-configure-defaults], and a `RoleBinding` to associate
the Kubernetes `Role` to the IAM `devs` role.

```typescript
import * as k8s from "@pulumi/kubernetes";

// Create a limited role for the `pulumi:devs` to use in the apps namespace.
let devsGroupRole = new k8s.rbac.v1.Role("pulumi-devs",
    {
        metadata: {namespace: appNamespaceName},
        rules: [
            {
                apiGroups: ["", "apps"],
                resources: ["pods", "deployments", "replicasets", "persistentvolumeclaims"],
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

After creating the `Role` and `RoleBinding` during a Pulumi update, now try
deploying the workload with the new authorization for the `devs` role.

```bash
$ export KUBECONFIG=`pwd`/kubeconfig-devs.json
$ kubectl run --generator=run-pod/v1 nginx --image=nginx --port=80 --expose --service-overrides='{"spec":{"type":"LoadBalancer"}}' -n `pulumi stack output appNamespaceName` --limits cpu=200m,memory=256Mi
service/nginx created
pod/nginx created
```

Delete the pod and service.

```bash
$ kubectl delete pod/nginx svc/nginx
```

<div class="cloud-prologue-aws"></div>
<div class="mt">
{{% md %}}

For a complete example of this in action, please see [Simplifying Kubernetes
RBAC in Amazon EKS][simplify-rbac].
[simplify-rbac]: /blog/simplify-kubernetes-rbac-in-amazon-eks-with-open-source-pulumi-packages/

{{% /md %}}
</div>

<div class="cloud-prologue-azure"></div>
<div class="mt">
{{% md %}}

TODO - Extra links to docs / examples

{{% /md %}}
</div>

<div class="cloud-prologue-gcp"></div>
<div class="mt">
{{% md %}}

TODO - Extra links to docs / examples

{{% /md %}}
</div>

See the [official Kubernetes RBAC docs][k8s-rbac-docs] for more details.

[crosswalk-identity]: {{< relref "/docs/guides/crosswalk/kubernetes/identity" >}}
[k8s-rbac-docs]: https://kubernetes.io/docs/reference/access-authn-authz/rbac/
[crosswalk-configure-defaults]: {{< relref "/docs/guides/crosswalk/kubernetes/configure-defaults" >}}

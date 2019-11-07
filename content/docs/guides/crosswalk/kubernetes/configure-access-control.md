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

```bash
$ pulumi stack output adminsIamRoleArn
arn:aws:iam::000000000000:role/admins-eksClusterAdmin-0627674
```

Make a copy of the kubeconfig that will be edited for the `admins` to use the
`adminsIamRoleArn` output.

```bash
$ pulumi stack output kubeconfig | jq '.' > kubeconfig-admin.json
```

Edit `kubeconfig-admin.json` by inserting a role to authenticate with in the
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
$ export KUBECONFIG=`pwd`/kubeconfig-admin.json
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
...
```

[crosswalk-identity]: {{< relref "/docs/guides/crosswalk/kubernetes/identity" >}}
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

```bash
$ pulumi stack output kubeconfigAdmin > kubeconfig-admin.json
$ export KUBECONFIG=`pwd`/kubeconfig-admin.json
```

Use `kubectl` to retrieve cluster information. You will see a prompt to log in:

```bash
$ kubectl cluster-info
To sign in, use a web browser to open the page https://microsoft.com/devicelogin and enter the code CF3TDACCY to authenticate.
```

Proceed to the webpage and use the mentioned code to authenticate as an administrator user. The interactive login is only required once: the successful attempt will save the token to the `kubeconfig` file.
After the login, cluster information will be displayed in the command-line console.

Test the `admins` role by using it and viewing all resources in the cluster as
expected.

```bash
$ kubectl get all -A
NAMESPACE     NAME                                       READY   STATUS    RESTARTS   AGE
kube-system   pod/azure-cni-networkmonitor-4fh89         1/1     Running   0          3h57m
kube-system   pod/azure-cni-networkmonitor-629fq         1/1     Running   0          3h57m
kube-system   pod/azure-cni-networkmonitor-ck89n         1/1     Running   0          3h57m
kube-system   pod/azure-cni-networkmonitor-gs75m         1/1     Running   0          3h57m
kube-system   pod/azure-cni-networkmonitor-s7b67         1/1     Running   0          3h57m
kube-system   pod/azure-ip-masq-agent-27j2m              1/1     Running   0          3h57m
kube-system   pod/azure-ip-masq-agent-czlc9              1/1     Running   0          3h57m
kube-system   pod/azure-ip-masq-agent-g5txw              1/1     Running   0          3h57m
kube-system   pod/azure-ip-masq-agent-h55ws              1/1     Running   0          3h57m
kube-system   pod/azure-ip-masq-agent-tdvgm              1/1     Running   0          3h57m
kube-system   pod/coredns-7fc597cc45-4z685               1/1     Running   0          3h55m
kube-system   pod/coredns-7fc597cc45-k7p22               1/1     Running   0          4h
kube-system   pod/coredns-autoscaler-7ccc76bfbd-k7zwl    1/1     Running   0          4h
kube-system   pod/kube-proxy-9vbhg                       1/1     Running   0          3h57m
kube-system   pod/kube-proxy-ftfsw                       1/1     Running   0          3h57m
kube-system   pod/kube-proxy-rq8cm                       1/1     Running   0          3h57m
kube-system   pod/kube-proxy-ssmsd                       1/1     Running   0          3h57m
kube-system   pod/kube-proxy-x94dh                       1/1     Running   0          3h57m
kube-system   pod/kubernetes-dashboard-cc4cc9f58-z5clx   1/1     Running   1          4h
kube-system   pod/metrics-server-cbd95f966-mmgsg         1/1     Running   1          4h
kube-system   pod/omsagent-5w45c                         1/1     Running   1          3h57m
kube-system   pod/omsagent-dw2gc                         1/1     Running   0          3h57m
kube-system   pod/omsagent-fzh6h                         1/1     Running   1          3h57m
kube-system   pod/omsagent-kcqdm                         1/1     Running   0          3h57m
kube-system   pod/omsagent-qnkp5                         1/1     Running   1          3h57m
kube-system   pod/omsagent-rs-8555b897d9-26wks           1/1     Running   0          4h
kube-system   pod/tunnelfront-5b6d458fbc-nzc25           1/1     Running   0          4h
...
```

[crosswalk-identity]: {{< relref "/docs/guides/crosswalk/kubernetes/identity" >}}
{{% /md %}}
</div>

<div class="cloud-prologue-gcp"></div>
<div class="mt">
{{% md %}}

  * [Use the `admins` ServiceAccount](#use-the-admins-service-account)
  * [Use the `devs` ServiceAccount](#use-the-devs-service-account)
  * [Configure RBAC Authorization](#configure-rbac-authorization)

### Use the `admins` ServiceAccount

In [Identity][crosswalk-identity] we demonstrate how to create typical roles for
use in Kubernetes.

We created an `admins` ServiceAccount for cluster administrators with root privileges, that
will be tied into Kubernetes RBAC.

Authenticate as the `admins` ServiceAccount from the [Identity
stack][gcp-identity-stack].

```bash
$ pulumi stack output adminsIamServiceAccountSecret > k8s-admin-sa-key.json
$ gcloud auth activate-service-account --key-file k8s-admin-sa-key.json
```

Start with the `kubeconfig` exported from the Pulumi stack.

```bash
$ pulumi stack output --show-secrets kubeconfig > kubeconfig.json
```

Use `kubectl` to retrieve cluster information.

```bash
$ export KUBECONFIG=`pwd`/kubeconfig.json
$ kubectl cluster-info
```

Test the `admins` ServiceAccount by using it and viewing all resources in the cluster as
expected.

```bash
$ kubectl get all -A

NAMESPACE     NAME                                                                 READY   STATUS    RESTARTS   AGE
kube-system   pod/event-exporter-v0.2.5-7df89f4b8f-k84nc                           2/2     Running   0          12m
kube-system   pod/fluentd-gcp-scaler-54ccb89d5-njcgt                               1/1     Running   0          12m
kube-system   pod/fluentd-gcp-v3.1.1-4wknk                                         2/2     Running   0          3m55s
kube-system   pod/fluentd-gcp-v3.1.1-bswkj                                         2/2     Running   0          3m16s
kube-system   pod/fluentd-gcp-v3.1.1-bt8m4                                         2/2     Running   0          3m55s
kube-system   pod/fluentd-gcp-v3.1.1-gdhzw                                         2/2     Running   0          3m55s
kube-system   pod/heapster-55d5978c96-mpsdd                                        3/3     Running   0          4m12s
kube-system   pod/kube-dns-5877696fb4-5gw7b                                        4/4     Running   0          12m
kube-system   pod/kube-dns-5877696fb4-84jk4                                        4/4     Running   0          4m4s
kube-system   pod/kube-dns-autoscaler-85f8bdb54-qz9zn                              1/1     Running   0          12m
kube-system   pod/kube-proxy-gke-k8s-gke-cluster--performant-nodes-ab1e580a-pkwp   1/1     Running   0          10m
kube-system   pod/kube-proxy-gke-k8s-gke-cluster--performant-nodes-ab1e580a-xmxc   1/1     Running   0          10m
kube-system   pod/kube-proxy-gke-k8s-gke-cluster--standard-nodes-c-cca08c52-9zzp   1/1     Running   0          4m13s
kube-system   pod/kube-proxy-gke-k8s-gke-cluster--standard-nodes-c-cca08c52-bgjz   1/1     Running   0          4m11s
kube-system   pod/l7-default-backend-8f479dd9-npdkv                                1/1     Running   0          12m
kube-system   pod/metrics-server-v0.3.1-8d4c5db46-hvr45                            2/2     Running   0          4m3s
kube-system   pod/prometheus-to-sd-7jzkj                                           1/1     Running   0          4m13s
kube-system   pod/prometheus-to-sd-v5ccv                                           1/1     Running   0          4m12s
kube-system   pod/stackdriver-metadata-agent-cluster-level-5d4f66757f-t7sd6        1/1     Running   0          12m
...
```

[gcp-identity-stack]: https://github.com/pulumi/kubernetes-the-prod-way/tree/crosswalk/gcp/01-identity
[crosswalk-identity]: {{< relref "/docs/guides/crosswalk/kubernetes/identity" >}}
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

```bash
$ pulumi stack output devsIamRoleArn
arn:aws:iam::000000000000:role/devs-eksClusterDeveloper-e332028
```

Make a copy of the kubeconfig that will be edited for the `devs` to use the
`devsIamRoleArn` output.


```bash
$ pulumi stack output kubeconfig | jq '.' > kubeconfig-devs.json
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

[crosswalk-identity]: {{< relref "/docs/guides/crosswalk/kubernetes/identity" >}}
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
$ pulumi stack output kubeconfig > kubeconfig-devs.json
$ export KUBECONFIG=`pwd`/kubeconfig-devs.json
```

Proceed to the webpage and use the mentioned code to authenticate as an dev user. The interactive login is only required once: the successful attempt will save the token to the `kubeconfig` file.
After the login, cluster information retrieval fails because of lack of permissions:

Test the `devs` role by using it and witnessing a lack of privileges.

```bash
$ kubectl get all -A
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

[crosswalk-identity]: {{< relref "/docs/guides/crosswalk/kubernetes/identity" >}}
{{% /md %}}
</div>

<div class="cloud-prologue-gcp"></div>
<div class="mt">
{{% md %}}

### Use the `devs` ServiceAccount

In [Identity][crosswalk-identity] we demonstrate how to create typical roles for
use in Kubernetes.

We created an `devs` ServiceAccount for cluster administrators with root privileges, that
will be tied into Kubernetes RBAC.

Authenticate as the `devs` ServiceAccount from the [Identity
stack][gcp-identity-stack].

```bash
$ pulumi stack output devsIamServiceAccountSecret > k8s-devs-sa-key.json
$ gcloud auth activate-service-account --key-file k8s-devs-sa-key.json
```

Start with the `kubeconfig` exported from the Pulumi stack.

```bash
$ pulumi stack output --show-secrets kubeconfig > kubeconfig.json
```

Test the `devs` ServiceAccount by using it and viewing all resources in the cluster as
expected.

```bash
$ kubectl get all -A
Error from server (Forbidden): pods is forbidden: User "k8s-devs@pulumi-development.iam.gserviceaccount.com" cannot list resource "pods" in API group "" at the cluster scope: Required "container.pods.list" permission.
Error from server (Forbidden): replicationcontrollers is forbidden: User "k8s-devs@pulumi-development.iam.gserviceaccount.com" cannot list resource "replicationcontrollers" in API group "" at the cluster scope: Required "container.replicationControllers.list" permission.
Error from server (Forbidden): services is forbidden: User "k8s-devs@pulumi-development.iam.gserviceaccount.com" cannot list resource "services" in API group "" at the cluster scope: Required "container.services.list" permission.
Error from server (Forbidden): daemonsets.apps is forbidden: User "k8s-devs@pulumi-development.iam.gserviceaccount.com" cannot list resource "daemonsets" in API group "apps" at the cluster scope: Required "container.daemonSets.list" permission.
Error from server (Forbidden): deployments.apps is forbidden: User "k8s-devs@pulumi-development.iam.gserviceaccount.com" cannot list resource "deployments" in API group "apps" at the cluster scope: Required "container.deployments.list" permission.
Error from server (Forbidden): replicasets.apps is forbidden: User "k8s-devs@pulumi-development.iam.gserviceaccount.com" cannot list resource "replicasets" in API group "apps" at the cluster scope: Required "container.replicaSets.list" permission.
Error from server (Forbidden): statefulsets.apps is forbidden: User "k8s-devs@pulumi-development.iam.gserviceaccount.com" cannot list resource "statefulsets" in API group "apps" at the cluster scope: Required "container.statefulSets.list" permission.
Error from server (Forbidden): horizontalpodautoscalers.autoscaling is forbidden: User "k8s-devs@pulumi-development.iam.gserviceaccount.com" cannot list resource "horizontalpodautoscalers" in API group "autoscaling" at the cluster scope: Required "container.horizontalPodAutoscalers.list" permission.
Error from server (Forbidden): jobs.batch is forbidden: User "k8s-devs@pulumi-development.iam.gserviceaccount.com" cannot list resource "jobs" in API group "batch" at the cluster scope: Required "container.jobs.list" permission.
Error from server (Forbidden): cronjobs.batch is forbidden: User "k8s-devs@pulumi-development.iam.gserviceaccount.com" cannot list resource "cronjobs" in API group "batch" at the cluster scope: Required "container.cronJobs.list" permission.
```

[crosswalk-identity]: {{< relref "/docs/guides/crosswalk/kubernetes/identity" >}}
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
$ kubectl run --namespace=`pulumi stack output appsNamespaceName` --generator=run-pod/v1 nginx --image=nginx --port=80 --expose --service-overrides='{"spec":{"type":"LoadBalancer"}}' --limits cpu=200m,memory=256Mi
Error from server (Forbidden): pods is forbidden: User "pulumi:alice" cannot create resource "pods" in API group "" in the namespace "apps-x1z818eg"
```

For example, to allow the `devs` group to operate in the cluster, an `admin` must create [Kubernetes RBAC][k8s-rbac-docs]
resources to bind the IAM role to certain privileges.

Below we create the Kubernetes `Role` with the ability to **only** deploy common
workloads in the `apps` namespace, created earlier during the configuration of
[cluster defaults][crosswalk-configure-defaults], and a `RoleBinding` to associate
the Kubernetes `Role` to the IAM `devs` role.

<div class="cloud-prologue-azure"></div>
<div class="mt">
{{% md %}}

Assume the `admin` user.

```bash
$ pulumi stack output kubeconfigAdmin > kubeconfig-admin.json
$ export KUBECONFIG=`pwd`/kubeconfig-admin.json
```
{{% /md %}}
</div>

Create the [Role][k8s-rbac-docs] for the `apps` namespace that will be bound to `devs` group.

```bash
$ export KUBECONFIG=`pwd`/kubeconfig-admin.json
```

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

After creating the `Role` and `RoleBinding` during a Pulumi update, now try
deploying the workload with the new authorization for the `devs` role.

```bash
$ export KUBECONFIG=`pwd`/kubeconfig-devs.json
$ kubectl run --namespace=`pulumi stack output appsNamespaceName` --generator=run-pod/v1 nginx --image=nginx --port=80 --expose --service-overrides='{"spec":{"type":"LoadBalancer"}}' --limits cpu=200m,memory=256Mi
service/nginx created
pod/nginx created
```

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

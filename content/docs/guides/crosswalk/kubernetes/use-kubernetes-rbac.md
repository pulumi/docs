---
title: Configure Access Control
menu:
  userguides:
    parent: crosswalk-kubernetes
    identifier: crosswalk-kubernetes-configure-authorization
    weight: 6
---

TODO - Intro

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

[aws-iam-auth]: https://docs.aws.amazon.com/eks/latest/userguide/install-aws-iam-authenticator.html
[simplify-rbac]: /blog/simplify-kubernetes-rbac-in-amazon-eks-with-open-source-pulumi-packages/
[k8s-rbac-docs]: https://kubernetes.io/docs/reference/access-authn-authz/rbac/

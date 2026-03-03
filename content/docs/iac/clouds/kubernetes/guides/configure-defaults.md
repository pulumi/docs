---
title_tag: Configure Kubernetes Cluster Defaults | Crosswalk
meta_desc: This page will walk you through how to configure Kubernetes Cluster Defaults
           on AWS, Azure, and Google Cloud.
title: Cluster defaults
h1: Kubernetes cluster defaults
meta_image: /images/docs/meta-images/docs-clouds-kubernetes-meta-image.png
menu:
  iac:
    name: Cluster defaults
    parent: kubernetes-clouds-guides
    identifier: kubernetes-guides-defaults
    weight: 5
aliases:
  - /docs/guides/crosswalk/kubernetes/configure-defaults/
  - /docs/clouds/kubernetes/guides/configure-defaults/
---

{{< chooser cloud "aws,azure,gcp" / >}}

With a vanilla cluster running, create any desired resources, and logically
segment the cluster as needed.

{{% choosable cloud aws %}}

The full code for this stack is on [GitHub](https://github.com/pulumi/kubernetes-guides/tree/master/aws/03-cluster-configuration).

{{% /choosable %}}

{{% choosable cloud azure %}}

The full code for this stack is on [GitHub](https://github.com/pulumi/kubernetes-guides/tree/master/azure/03-cluster-configuration).

{{% /choosable %}}

{{% choosable cloud gcp %}}

The full code for this stack is on [GitHub](https://github.com/pulumi/kubernetes-guides/tree/master/gcp/03-cluster-configuration).

{{% /choosable %}}

## Overview

We'll examine how to create:

* [Namespaces](#namespaces)
* [Quotas](#quotas)
* [Pod Security Standards](#pod-security-standards)

## Prerequisites

{{% choosable cloud aws %}}

Authenticate as the `admins` role from the [Identity][aws-admin-identity-stack] stack.

```bash
$ aws sts assume-role --role-arn `pulumi stack output adminsIamRoleArn` --role-session-name k8s-admin
$ export KUBECONFIG=`pwd`/kubeconfig-admin.json
```

[aws-admin-identity-stack]: /docs/clouds/kubernetes/guides/identity/#create-an-iam-role-for-admins
{{% /choosable %}}
{{% choosable cloud azure %}}
Authenticate as the ServicePrincipal from the [Identity][azure-identity-stack] stack.

```bash
$ az login --service-principal --username $ARM_CLIENT_ID --password $ARM_CLIENT_SECRET --tenant $ARM_TENANT_ID
$ export KUBECONFIG=`pwd`/kubeconfig-admin.json
```

[azure-identity-stack]: /docs/clouds/kubernetes/guides/identity/#prerequisites

{{% /choosable %}}

{{% choosable cloud gcp %}}

Authenticate as the `admins` ServiceAccount from the [Identity][gcp-admin-identity-stack] stack.

```bash
$ gcloud auth activate-service-account --key-file k8s-admin-sa-key.json
$ export KUBECONFIG=`pwd`/kubeconfig.json
```

[gcp-admin-identity-stack]: /docs/clouds/kubernetes/guides/identity/#create-an-iam-role-for-admins

{{% /choosable %}}

## Namespaces

Create namespaces for typical stacks:

* Cluster Services: Deploy cluster-scoped services, such as logging and monitoring.
* App Services: Deploy application-scoped services, such as ingress or DNS management.
* Apps: Deploy applications and workloads.

{{< chooser k8s-language "typescript,yaml" / >}}

{{% choosable k8s-language yaml %}}

```yaml
cat > namespaces.yaml << EOF
apiVersion: v1
kind: Namespace
metadata:
  name: cluster-svcs
---
apiVersion: v1
kind: Namespace
metadata:
  name: app-svcs
---
apiVersion: v1
kind: Namespace
metadata:
  name: apps
EOF
```

```bash
$ kubectl apply -f namespaces.yaml
```

{{% /choosable %}}

{{% choosable k8s-language typescript %}}

```typescript
import * as k8s from "@pulumi/kubernetes";

// Create Kubernetes namespaces.
const clusterSvcsNamespace = new k8s.core.v1.Namespace("cluster-svcs", undefined, { provider: cluster.provider });
export const clusterSvcsNamespaceName = clusterSvcsNamespace.metadata.name;

const appSvcsNamespace = new k8s.core.v1.Namespace("app-svcs", undefined, { provider: cluster.provider });
export const appSvcsNamespaceName = appSvcsNamespace.metadata.name;

const appsNamespace = new k8s.core.v1.Namespace("apps", undefined, { provider: cluster.provider });
export const appsNamespaceName = appsNamespace.metadata.name;
```

{{% /choosable %}}

## Quotas

Create [quotas][k8s-quotas] to restrict the number of resources that can be consumed across
all Pods in a namespace.

<!-- markdownlint-disable url -->
[k8s-quotas]: https://kubernetes.io/docs/concepts/policy/resource-quotas/#compute-resource-quota
<!-- markdownlint-enable url -->

{{< chooser k8s-language "typescript,yaml" / >}}

{{% choosable k8s-language yaml %}}

```yaml
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

```bash
$ kubectl apply -f quota.yaml
```

{{% /choosable %}}

{{% choosable k8s-language typescript %}}

```typescript
import * as k8s from "@pulumi/kubernetes";

// Create a resource quota in the apps namespace.
const quotaAppNamespace = new k8s.core.v1.ResourceQuota("apps", {
    metadata: {namespace: appsNamespaceName},
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

{{% /choosable %}}

Track the quota usage in the namespace using `kubectl` and Pulumi output.

```bash
$ kubectl describe quota -n `pulumi stack output appsNamespaceName`
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

## Pod Security Standards

Kubernetes replaced PodSecurityPolicy (PSP) with the [Pod Security Admission][k8s-psa]
controller, which became stable in Kubernetes 1.25. PSP was removed in Kubernetes 1.25,
and is no longer available in current versions of EKS, AKS, or GKE.

Pod Security Admission enforces [Pod Security Standards][k8s-pss] at the namespace level
using namespace labels. There are three policy levels:

| Level | Description |
|---|---|
| `privileged` | Unrestricted; allows known privilege escalations |
| `baseline` | Minimally restrictive; prevents known privilege escalations |
| `restricted` | Heavily restricted; follows pod hardening best practices |

Each level can be applied in three modes:

| Mode | Description |
|---|---|
| `enforce` | Policy violations cause the pod to be rejected |
| `warn` | Policy violations trigger a user-facing warning but do not block |
| `audit` | Policy violations are recorded in the audit log |

<!-- markdownlint-disable url -->
[k8s-psa]: https://kubernetes.io/docs/concepts/security/pod-security-admission/
[k8s-pss]: https://kubernetes.io/docs/concepts/security/pod-security-standards/
<!-- markdownlint-enable url -->

### Apply Pod Security Standards to a namespace

Apply pod security standards to a namespace by adding labels. For most application
workloads, enforce the `restricted` level:

{{< chooser k8s-language "typescript,yaml" / >}}

{{% choosable k8s-language yaml %}}

```yaml
cat > apps-namespace.yaml << EOF
apiVersion: v1
kind: Namespace
metadata:
  name: apps
  labels:
    pod-security.kubernetes.io/enforce: restricted
    pod-security.kubernetes.io/warn: restricted
    pod-security.kubernetes.io/audit: restricted
EOF
```

```bash
$ kubectl apply -f apps-namespace.yaml
```

{{% /choosable %}}

{{% choosable k8s-language typescript %}}

```typescript
import * as k8s from "@pulumi/kubernetes";

const appsNamespace = new k8s.core.v1.Namespace("apps", {
    metadata: {
        labels: {
            "pod-security.kubernetes.io/enforce": "restricted",
            "pod-security.kubernetes.io/warn": "restricted",
            "pod-security.kubernetes.io/audit": "restricted",
        },
    },
}, { provider: cluster.provider });
```

{{% /choosable %}}

For workloads that require elevated permissions, such as ingress controllers, use the
`privileged` or `baseline` level on those specific namespaces instead:

{{< chooser k8s-language "typescript,yaml" / >}}

{{% choosable k8s-language yaml %}}

```yaml
cat > ingress-nginx-namespace.yaml << EOF
apiVersion: v1
kind: Namespace
metadata:
  name: ingress-nginx
  labels:
    pod-security.kubernetes.io/enforce: privileged
EOF
```

```bash
$ kubectl apply -f ingress-nginx-namespace.yaml
```

{{% /choosable %}}

{{% choosable k8s-language typescript %}}

```typescript
import * as k8s from "@pulumi/kubernetes";

const ingressNamespace = new k8s.core.v1.Namespace("ingress-nginx", {
    metadata: {
        name: "ingress-nginx",
        labels: {
            "pod-security.kubernetes.io/enforce": "privileged",
        },
    },
}, { provider: cluster.provider });
```

{{% /choosable %}}

For more details, see the [Kubernetes Pod Security Standards documentation][k8s-pss].

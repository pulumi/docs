---
title: Configure Cluster Defaults
menu:
  userguides:
    parent: crosswalk-kubernetes
    identifier: crosswalk-kubernetes-defaults
    weight: 5
---

{{< cloudchoose >}}

With a vanilla cluster running, create any desired resources, and logically
segment the cluster as needed.

TODO - Flush out intro

<div class="cloud-prologue-aws"></div>
<div class="mt">
{{% md %}}

The full code for this stack is on [GitHub][gh-repo-stack].
[gh-repo-stack]: https://github.com/pulumi/kubernetes-the-prod-way/tree/crosswalk/aws/03-cluster-configuration

{{% /md %}}
</div>

<div class="cloud-prologue-azure"></div>
<div class="mt">
{{% md %}}

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

We'll examine how to create:

  * [Namespaces](#namespaces)
  * [Quotas](#quotas)
  * [PodSecurityPolicies](#podsecuritypolicies)

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

const appsNamespace = new k8s.core.v1.Namespace("apps", undefined, { provider: cluster.provider });
export const appsNamespaceName = appsNamespace.metadata.name;
```

### Quotas

Create [quotas][k8s-quotas] to restrict the amount of resources that can be consumed across
all Pods in a namespace.

```bash
$ cat > quota.yaml << EOF
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

### PodSecurityPolicies

<div class="cloud-prologue-aws"></div>
<div class="mt">
{{% md %}}

By default EKS ships with a fully privileged [PodSecurityPolicy][k8s-psp] named
`eks.privileged`. This privileged PSP should be removed **after** its replacements
have been created to ensure running workloads continue executing properly (order matters).

See the official [EKS Pod Security Policy][eks-psp] docs and the
[Kubernetes docs][k8s-psp] for more details.

[k8s-psp]: https://kubernetes.io/docs/concepts/policy/pod-security-policy/
[eks-psp]: https://docs.aws.amazon.com/eks/latest/userguide/pod-security-policy.html
{{% /md %}}
</div>

<div class="cloud-prologue-azure"></div>
<div class="mt">
{{% md %}}

TODO

{{% /md %}}
</div>

<div class="cloud-prologue-gcp"></div>
<div class="mt">
{{% md %}}

TODO

{{% /md %}}
</div>

[k8s-quotas]: https://kubernetes.io/docs/concepts/policy/resource-quotas/#compute-resource-quota

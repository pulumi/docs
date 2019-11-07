--- title: Configure Cluster Defaults
menu:
  userguides:
    parent: crosswalk-kubernetes
    identifier: crosswalk-kubernetes-defaults
    weight: 5
---

{{< cloudchoose >}}

With a vanilla cluster running, create any desired resources, and logically
segment the cluster as needed.

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
 * App Services: Deploy application-scoped services, such as ingress or DNS management.
 * Apps: Deploy applications and workloads.

{{< k8s-language nokx >}}

<div class="k8s-language-prologue-yaml"></div>
<div class="mt">
{{% md %}}

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

{{% /md %}}
</div>

<div class="k8s-language-prologue-typescript"></div>
<div class="mt">
{{% md %}}
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
{{% /md %}}
</div>

### Quotas

Create [quotas][k8s-quotas] to restrict the amount of resources that can be consumed across
all Pods in a namespace.

{{< k8s-language nokx >}}

<div class="k8s-language-prologue-yaml"></div>
<div class="mt">
{{% md %}}
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
{{% /md %}}
</div>

<div class="k8s-language-prologue-typescript"></div>
<div class="mt">
{{% md %}}
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
{{% /md %}}
</div>

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

By default, EKS ships with a fully privileged [PodSecurityPolicy][k8s-psp] named
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

By default, AKS ships with a fully privileged [PodSecurityPolicy][k8s-psp] named
`privileged`. This privileged PSP should be removed **after** its replacements
have been created to ensure running workloads continue executing properly (order matters).

Users who are **not** admins will not be able to create Pods if the cluster was
created with `enablePodSecurityPolicy: true`, as the PSP is only bound to
admins, and requires a PSP be created and bound to the Kubernetes RBAC for these users.

See the official [AKS Pod Security Policy][aks-psp] docs and the
[Kubernetes docs][k8s-psp] for more details.
[k8s-psp]: https://kubernetes.io/docs/concepts/policy/pod-security-policy/
[aks-psp]: https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies

{{% /md %}}
</div>

<div class="cloud-prologue-gcp"></div>
<div class="mt">
{{% md %}}

By default, GKE ships with the following [PodSecurityPolicies][k8s-psp].
These PSPs are used by GKE Pods and should generally be left untouched. If you
choose to replace them, they should be removed **after** its replacements
have been created to ensure running workloads continue executing properly (order matters).

| PSP Name |
|---|
| gce.event-exporter |
| gce.fluentd-gcp |
| gce.persistent-volume-binder |
| gce.privileged |
| gce.unprivileged-addon |

See the official [GKE Pod Security Policy][gke-psp] docs and the
[Kubernetes docs][k8s-psp] for more details.

[k8s-psp]: https://kubernetes.io/docs/concepts/policy/pod-security-policy/
[gke-psp]: https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies
{{% /md %}}
</div>

#### Create a Restrictive PSP

Create a PSP that allows a restrictive, but usable set of permissions to deploy
workloads.

{{< k8s-language nokx >}}

<div class="k8s-language-prologue-yaml"></div>
<div class="mt">
{{% md %}}

```yaml
apiVersion: policy/v1beta1
kind: PodSecurityPolicy
metadata:
  name: restrictive
spec:
  privileged: false
  hostNetwork: false
  allowPrivilegeEscalation: false
  defaultAllowPrivilegeEscalation: false
  hostPID: false
  hostIPC: false
  runAsUser:
    rule: RunAsAny
  fsGroup:
    rule: RunAsAny
  seLinux:
    rule: RunAsAny
  supplementalGroups:
    rule: RunAsAny
  volumes:
  - 'configMap'
  - 'downwardAPI'
  - 'emptyDir'
  - 'persistentVolumeClaim'
  - 'secret'
  - 'projected'
  allowedCapabilities:
  - '*'

---

apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: restrictive
rules:
- apiGroups:
  - policy
  resourceNames:
  - restrictive
  resources:
  - podsecuritypolicies
  verbs:
  - use

---

apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: allow-restricted-kube-system
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: restrictive
subjects:
- kind: Group
  name: system:serviceaccounts
  namespace: kube-system
```
{{% /md %}}
</div>

<div class="k8s-language-prologue-typescript"></div>
<div class="mt">
{{% md %}}
{{% /md %}}
</div>

[k8s-quotas]: https://kubernetes.io/docs/concepts/policy/resource-quotas/#compute-resource-quota

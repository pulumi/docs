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

<div class="cloud-prologue-aws"></div>
<div class="mt">
{{% md %}}

The full code for this stack is on [GitHub][gh-repo-stack].
[gh-repo-stack]: https://github.com/pulumi/kubernetes-guides/tree/master/aws/03-cluster-configuration

{{% /md %}}
</div>

<div class="cloud-prologue-azure"></div>
<div class="mt">
{{% md %}}

The full code for this stack is on [GitHub][gh-repo-stack].
[gh-repo-stack]: https://github.com/pulumi/kubernetes-guides/tree/master/azure/03-cluster-configuration

{{% /md %}}
</div>

<div class="cloud-prologue-gcp"></div>
<div class="mt">
{{% md %}}

The full code for this stack is on [GitHub][gh-repo-stack].
[gh-repo-stack]: https://github.com/pulumi/kubernetes-guides/tree/master/gcp/03-cluster-configuration

{{% /md %}}
</div>

## Overview

We'll examine how to create:

  * [Namespaces](#namespaces)
  * [Quotas](#quotas)
  * [PodSecurityPolicies](#podsecuritypolicies)

## Prerequisites

<div class="cloud-prologue-aws"></div>
<div class="mt">
{{% md %}}

Authenticate as the `admins` role from the [Identity][aws-admin-identity-stack] stack.

```bash
$ aws sts assume-role --role-arn `pulumi stack output adminsIamRoleArn` --role-session-name k8s-admin
$ export KUBECONFIG=`pwd`/kubeconfig-admin.json
```
[aws-admin-identity-stack]: {{< relref "/docs/guides/crosswalk/kubernetes/identity#create-an-iam-role-for-admins" >}}
{{% /md %}}
</div>
<div class="cloud-prologue-azure"></div>
<div class="mt">
{{% md %}}
Authenticate as the ServicePrincipal from the [Identity][azure-identity-stack] stack.

```bash
$ az login --service-principal --username $ARM_CLIENT_ID --password $ARM_CLIENT_SECRET --tenant $ARM_TENANT_ID
$ export KUBECONFIG=`pwd`/kubeconfig-admin.json
```
[azure-identity-stack]: {{< relref "/docs/guides/crosswalk/kubernetes/identity#prerequisites" >}}
{{% /md %}}
</div>
<div class="cloud-prologue-gcp"></div>
<div class="mt">
{{% md %}}
Authenticate as the `admins` ServiceAccount from the [Identity][gcp-admin-identity-stack] stack.

```bash
$ gcloud auth activate-service-account --key-file k8s-admin-sa-key.json
$ export KUBECONFIG=`pwd`/kubeconfig.json
```

[gcp-admin-identity-stack]: {{< relref "/docs/guides/crosswalk/kubernetes/identity#create-an-iam-role-and-serviceaccount-for-admins" >}}
{{% /md %}}
</div>

## Namespaces

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

## Quotas

Create [quotas][k8s-quotas] to restrict the number of resources that can be consumed across
all Pods in a namespace.

[k8s-quotas]: https://kubernetes.io/docs/concepts/policy/resource-quotas/#compute-resource-quota

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

## PodSecurityPolicies

<div class="cloud-prologue-aws"></div>
<div class="mt">
{{% md %}}

By default, EKS ships with a fully privileged [PodSecurityPolicy][k8s-psp] named
`eks.privileged`. This PSP is bound to the `system:authenticated` group, which means **any**
authenticated user in the cluster can run privileged workloads. It is highly
recommended that you replace this PSP with an appropriate, restricted PSP by user.

> Note: PSPs should only be removed **after** its replacements have been created
to ensure running workloads continue executing properly (order matters).

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
`privileged`. [Per AKS][aks-psp-priv], this privileged PSP should not be removed.

Users who are **not** in the `cluster-admins` ClusterRole will not be able to
create Pods if the cluster was created with `enablePodSecurityPolicy: true`.
We'll need to create a PSP with proper Kubernetes RBAC for these users.

See the official [AKS Pod Security Policy][aks-psp] docs and the
[Kubernetes docs][k8s-psp] for more details.
[k8s-psp]: https://kubernetes.io/docs/concepts/policy/pod-security-policy/
[aks-psp]: https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies
[aks-psp-priv]: https://docs.microsoft.com/en-us/azure/aks/use-pod-security-policies

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

<div class="cloud-prologue-aws"></div>
<div class="mt">
{{% md %}}
<div class="k8s-language-prologue-yaml"></div>
<div class="mt">
{{% md %}}

```yaml
cat > restrictive-psp.yaml << EOF
apiVersion: policy/v1beta1
kind: PodSecurityPolicy
metadata:
  name: demo-restrictive
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

# Create a ClusterRole to use the restrictive PSP.

apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: demo-restrictive
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

# Create a binding to the restrictive PSP for the controllers running in
# kube-system that use ServiceAccounts.

apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: allow-restricted-kube-system
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: demo-restrictive
subjects:
- kind: Group
  name: system:serviceaccounts
  namespace: kube-system

---

# Create a binding to the restrictive PSP for the pulumi:devs RBAC group running in
# apps Namespace.

apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: allow-restricted-apps
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: demo-restrictive
subjects:
- kind: Group
  name: pulumi:devs
  namespace: `pulumi stack output appsNamespaceName`
EOF
```

```bash
$ kubectl apply -f restrictive-psp.yaml
```
{{% /md %}}
</div>

<div class="k8s-language-prologue-typescript"></div>
<div class="mt">
{{% md %}}

```ts
import * as k8s from "@pulumi/kubernetes";

// Create a restrictive PodSecurityPolicy.
const restrictivePSP = new k8s.policy.v1beta1.PodSecurityPolicy("demo-restrictive", {
    metadata: { name: "demo-restrictive" },
    spec: {
        privileged: false,
        hostNetwork: false,
        allowPrivilegeEscalation: false,
        defaultAllowPrivilegeEscalation: false,
        hostPID: false,
        hostIPC: false,
        runAsUser: { rule: "RunAsAny" },
        fsGroup: { rule: "RunAsAny" },
        seLinux: { rule: "RunAsAny" },
        supplementalGroups: { rule: "RunAsAny" },
        volumes: [
            "configMap",
            "downwardAPI",
            "emptyDir",
            "persistentVolumeClaim",
            "secret",
            "projected"
        ],
        allowedCapabilities: [
            "*"
        ]
    }
});

// Create a ClusterRole to use the restrictive PodSecurityPolicy.
const restrictiveClusterRole = new k8s.rbac.v1.ClusterRole("demo-restrictive", {
    metadata: { name: "demo-restrictive" },
    rules: [
        {
            apiGroups: [
                "policy"
            ],
            resourceNames: [
                restrictivePSP.metadata.name,
            ],
            resources: [
                "podsecuritypolicies"
            ],
            verbs: [
                "use"
            ]
        }
    ]
});

// Create a ClusterRoleBinding for the ServiceAccounts of Namespace kube-system
// to the ClusterRole that uses the restrictive PodSecurityPolicy.
const allowRestrictedKubeSystemCRB = new k8s.rbac.v1.ClusterRoleBinding("allow-restricted-kube-system", {
    metadata: { name: "allow-restricted-kube-system" },
    roleRef: {
        apiGroup: "rbac.authorization.k8s.io",
        kind: "ClusterRole",
        name: restrictiveClusterRole.metadata.name
    },
    subjects: [
        {
            kind: "Group",
            name: "system:serviceaccounts",
            namespace: "kube-system"
        }
    ]
});

// Create a ClusterRoleBinding for the RBAC group pulumi:devs
// to the ClusterRole that uses the restrictive PodSecurityPolicy.
const allowRestrictedAppsCRB = new k8s.rbac.v1.ClusterRoleBinding("allow-restricted-apps", {
    metadata: { name: "allow-restricted-apps" },
    roleRef: {
        apiGroup: "rbac.authorization.k8s.io",
        kind: "ClusterRole",
        name: restrictiveClusterRole.metadata.name
    },
    subjects: [
        {
            kind: "Group",
            name: "pulumi:devs",
            namespace: appsNamespaceName
        }
    ]
});
```

{{% /md %}}
</div>
{{% /md %}}
</div>

<div class="cloud-prologue-azure"></div>
<div class="mt">
{{% md %}}
<div class="k8s-language-prologue-yaml"></div>
<div class="mt">
{{% md %}}

```yaml
cat > restrictive-psp.yaml << EOF
apiVersion: policy/v1beta1
kind: PodSecurityPolicy
metadata:
  name: demo-restrictive
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

# Create a ClusterRole to use the restrictive PSP.

apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: demo-restrictive
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

# Create a binding to the restrictive PSP for the controllers running in
# kube-system that use ServiceAccounts.

apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: allow-restricted-kube-system
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: demo-restrictive
subjects:
- kind: Group
  name: system:serviceaccounts
  namespace: kube-system

---

# Create a binding to the restrictive PSP for the pulumi:devs RBAC group running in
# apps Namespace.

apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: allow-restricted-apps
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: demo-restrictive
subjects:
- kind: Group
  name: pulumi:devs
  namespace: `pulumi stack output appsNamespaceName`
EOF
```

```bash
$ kubectl apply -f restrictive-psp.yaml
```
{{% /md %}}
</div>

<div class="k8s-language-prologue-typescript"></div>
<div class="mt">
{{% md %}}

```ts
import * as k8s from "@pulumi/kubernetes";

// Create a restrictive PodSecurityPolicy.
const restrictivePSP = new k8s.policy.v1beta1.PodSecurityPolicy("demo-restrictive", {
    metadata: { name: "demo-restrictive" },
    spec: {
        privileged: false,
        hostNetwork: false,
        allowPrivilegeEscalation: false,
        defaultAllowPrivilegeEscalation: false,
        hostPID: false,
        hostIPC: false,
        runAsUser: { rule: "RunAsAny" },
        fsGroup: { rule: "RunAsAny" },
        seLinux: { rule: "RunAsAny" },
        supplementalGroups: { rule: "RunAsAny" },
        volumes: [
            "configMap",
            "downwardAPI",
            "emptyDir",
            "persistentVolumeClaim",
            "secret",
            "projected"
        ],
        allowedCapabilities: [
            "*"
        ]
    }
});

// Create a ClusterRole to use the restrictive PodSecurityPolicy.
const restrictiveClusterRole = new k8s.rbac.v1.ClusterRole("demo-restrictive", {
    metadata: { name: "demo-restrictive" },
    rules: [
        {
            apiGroups: [
                "policy"
            ],
            resourceNames: [
                restrictivePSP.metadata.name,
            ],
            resources: [
                "podsecuritypolicies"
            ],
            verbs: [
                "use"
            ]
        }
    ]
});

// Create a ClusterRoleBinding for the ServiceAccounts of Namespace kube-system
// to the ClusterRole that uses the restrictive PodSecurityPolicy.
const allowRestrictedKubeSystemCRB = new k8s.rbac.v1.ClusterRoleBinding("allow-restricted-kube-system", {
    metadata: { name: "allow-restricted-kube-system" },
    roleRef: {
        apiGroup: "rbac.authorization.k8s.io",
        kind: "ClusterRole",
        name: restrictiveClusterRole.metadata.name
    },
    subjects: [
        {
            kind: "Group",
            name: "system:serviceaccounts",
            namespace: "kube-system"
        }
    ]
});

// Create a ClusterRoleBinding for the RBAC group pulumi:devs
// to the ClusterRole that uses the restrictive PodSecurityPolicy.
const allowRestrictedAppsCRB = new k8s.rbac.v1.ClusterRoleBinding("allow-restricted-apps", {
    metadata: { name: "allow-restricted-apps" },
    roleRef: {
        apiGroup: "rbac.authorization.k8s.io",
        kind: "ClusterRole",
        name: restrictiveClusterRole.metadata.name
    },
    subjects: [
        {
            kind: "Group",
            name: "pulumi:devs",
            namespace: appsNamespaceName
        }
    ]
});
```

{{% /md %}}
</div>
{{% /md %}}
</div>

<div class="cloud-prologue-gcp"></div>
<div class="mt">
{{% md %}}
<div class="k8s-language-prologue-yaml"></div>
<div class="mt">
{{% md %}}

```yaml
cat > restrictive-psp.yaml << EOF
apiVersion: policy/v1beta1
kind: PodSecurityPolicy
metadata:
  name: demo-restrictive
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

# Create a ClusterRole to use the restrictive PSP.

apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: demo-restrictive
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

# Create a binding to the restrictive PSP for the controllers running in
# kube-system that use ServiceAccounts.

apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: allow-restricted-kube-system
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: demo-restrictive
subjects:
- kind: Group
  name: system:serviceaccounts
  namespace: kube-system

---

# Create a binding to the restrictive PSP for the pulumi:devs RBAC group running in
# apps Namespace.

apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: allow-restricted-apps
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: demo-restrictive
subjects:
- kind: User
  name: k8s-devs@pulumi-development.iam.gserviceaccount.com
  namespace: `pulumi stack output appsNamespaceName`
EOF
```

```bash
$ kubectl apply -f restrictive-psp.yaml
```
{{% /md %}}
</div>

<div class="k8s-language-prologue-typescript"></div>
<div class="mt">
{{% md %}}

```ts
import * as k8s from "@pulumi/kubernetes";

// Create a restrictive PodSecurityPolicy.
const restrictivePSP = new k8s.policy.v1beta1.PodSecurityPolicy("demo-restrictive", {
    metadata: { name: "demo-restrictive" },
    spec: {
        privileged: false,
        hostNetwork: false,
        allowPrivilegeEscalation: false,
        defaultAllowPrivilegeEscalation: false,
        hostPID: false,
        hostIPC: false,
        runAsUser: { rule: "RunAsAny" },
        fsGroup: { rule: "RunAsAny" },
        seLinux: { rule: "RunAsAny" },
        supplementalGroups: { rule: "RunAsAny" },
        volumes: [
            "configMap",
            "downwardAPI",
            "emptyDir",
            "persistentVolumeClaim",
            "secret",
            "projected"
        ],
        allowedCapabilities: [
            "*"
        ]
    }
});

// Create a ClusterRole to use the restrictive PodSecurityPolicy.
const restrictiveClusterRole = new k8s.rbac.v1.ClusterRole("demo-restrictive", {
    metadata: { name: "demo-restrictive" },
    rules: [
        {
            apiGroups: [
                "policy"
            ],
            resourceNames: [
                restrictivePSP.metadata.name,
            ],
            resources: [
                "podsecuritypolicies"
            ],
            verbs: [
                "use"
            ]
        }
    ]
});

// Create a ClusterRoleBinding for the ServiceAccounts of Namespace kube-system
// to the ClusterRole that uses the restrictive PodSecurityPolicy.
const allowRestrictedKubeSystemCRB = new k8s.rbac.v1.ClusterRoleBinding("allow-restricted-kube-system", {
    metadata: { name: "allow-restricted-kube-system" },
    roleRef: {
        apiGroup: "rbac.authorization.k8s.io",
        kind: "ClusterRole",
        name: restrictiveClusterRole.metadata.name
    },
    subjects: [
        {
            kind: "Group",
            name: "system:serviceaccounts",
            namespace: "kube-system"
        }
    ]
});

// Create a ClusterRoleBinding for the RBAC group pulumi:devs
// to the ClusterRole that uses the restrictive PodSecurityPolicy.
const allowRestrictedAppsCRB = pulumi.all([
    config.project,
    config.devsAccountId,
]).apply(([project, devsAccountId]) => {
    return new k8s.rbac.v1.ClusterRoleBinding("allow-restricted-apps", {
        metadata: { name: "allow-restricted-apps" },
        roleRef: {
            apiGroup: "rbac.authorization.k8s.io",
            kind: "ClusterRole",
            name: restrictiveClusterRole.metadata.name
        },
        subjects: [{
            kind: "User",
            name: `${devsAccountId}@${project}.iam.gserviceaccount.com`,
            namespace: appsNamespaceName
        }],
    })
});
```

{{% /md %}}
</div>
{{% /md %}}
</div>

#### Create a Privileged PSP Role Binding

If you wish to grant the ability to use a privileged PSP, we need to
create a ClusterRoleBinding to the PSP. For example, here's how to bind the PSP to
a given Namespace's (`ingress-nginx`) ServiceAccounts.

{{< k8s-language nokx >}}

<div class="k8s-language-prologue-yaml"></div>
<div class="mt">
{{% md %}}

<div class="cloud-prologue-aws"></div>
<div class="mt">
{{% md %}}
```yaml
cat > privileged-clusterrolebinding.yaml << EOF
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: allow-privileged-ingress-nginx
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: eks:podsecuritypolicy:privileged
subjects:
- kind: Group
  name: system:serviceaccounts:ingress-nginx
  apiGroup: rbac.authorization.k8s.io
EOF
```

```bash
$ kubectl apply -f privileged-rolebinding.yaml
```
{{% /md %}}
</div>
<div class="cloud-prologue-azure"></div>
<div class="mt">
{{% md %}}
```yaml
cat > privileged-clusterrolebinding.yaml << EOF
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: allow-privileged-ingress-nginx
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: psp:privileged
subjects:
- kind: Group
  name: system:serviceaccounts:ingress-nginx
  apiGroup: rbac.authorization.k8s.io
EOF
```

```bash
$ kubectl apply -f privileged-rolebinding.yaml
```
{{% /md %}}
</div>
<div class="cloud-prologue-gcp"></div>
<div class="mt">
{{% md %}}
```yaml
cat > privileged-clusterrolebinding.yaml << EOF
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: allow-privileged-ingress-nginx
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: gce:podsecuritypolicy:privileged
subjects:
- kind: Group
  name: system:serviceaccounts:ingress-nginx
  apiGroup: rbac.authorization.k8s.io
EOF
```

```bash
$ kubectl apply -f privileged-rolebinding.yaml
```
{{% /md %}}
</div>

{{% /md %}}
</div>

<div class="k8s-language-prologue-typescript"></div>
<div class="mt">
{{% md %}}
<div class="cloud-prologue-aws"></div>
<div class="mt">
{{% md %}}
```ts
import * as k8s from "@pulumi/kubernetes";

const privilegedCRB = new k8s.rbac.v1.ClusterRoleBinding("privileged", {
    metadata: { name: "allow-privileged-ingress-nginx" },
    roleRef: {
        apiGroup: "rbac.authorization.k8s.io",
        kind: "ClusterRole",
        name: "eks.privileged"
    },
    subjects: [
        {
            kind: "Group",
            name: "system:serviceaccounts:ingress-nginx",
            apiGroup: "rbac.authorization.k8s.io"
        }
    ]
});
```
{{% /md %}}
</div>

<div class="cloud-prologue-azure"></div>
<div class="mt">
{{% md %}}
```ts
import * as k8s from "@pulumi/kubernetes";

const privilegedCRB = new k8s.rbac.v1.ClusterRoleBinding("privileged", {
    metadata: { name: "allow-privileged-ingress-nginx" },
    roleRef: {
        apiGroup: "rbac.authorization.k8s.io",
        kind: "ClusterRole",
        name: "psp:privileged"
    },
    subjects: [
        {
            kind: "Group",
            name: "system:serviceaccounts:ingress-nginx",
            apiGroup: "rbac.authorization.k8s.io"
        }
    ]
});
```
{{% /md %}}
</div>

<div class="cloud-prologue-gcp"></div>
<div class="mt">
{{% md %}}
```ts
import * as k8s from "@pulumi/kubernetes";

// Create a ClusterRoleBinding for the SeviceAccounts of Namespace ingress-nginx
// to the ClusterRole that uses the privileged PodSecurityPolicy.
const privilegedCRB = new k8s.rbac.v1.ClusterRoleBinding("privileged", {
    metadata: { name: "allow-privileged-ingress-nginx" },
    roleRef: {
        apiGroup: "rbac.authorization.k8s.io",
        kind: "ClusterRole",
        name: "gce:podsecuritypolicy:privileged"
    },
    subjects: [
        {
            kind: "Group",
            name: "system:serviceaccounts:ingress-nginx",
            apiGroup: "rbac.authorization.k8s.io"
        }
    ]
});
```
{{% /md %}}
</div>

{{% /md %}}
</div>

---
title: "How to Provision a Kubernetes Cluster with Infrastructure as Code"
date: 2026-08-24
draft: false
meta_desc: "How to provision a Kubernetes cluster with infrastructure as code on EKS, AKS, and GKE using real Pulumi examples."
authors:
    - pulumi-content-team
tags:
    - kubernetes
    - infrastructure-as-code
    - aws
    - azure
    - google-cloud
category: general
faq_schema: true
howto_schema: true
estimated_time: 20
related_posts:
    - best-kubernetes-iac-tools-2026
    - terraform-kubernetes
    - aws-eks-auto-mode
social:
    twitter: |
        The best way to provision a Kubernetes cluster is with infrastructure as code.

        Here's one program that creates EKS, AKS, or GKE clusters with real Pulumi code, no YAML templates.
    linkedin: |
        A practical, answer-first guide to provisioning managed Kubernetes clusters on AWS, Azure, and Google Cloud with infrastructure as code.

        Real Pulumi examples for EKS, AKS, and GKE, plus how to deploy an application once the cluster exists.
    bluesky: |
        EKS, AKS, GKE: one infrastructure-as-code approach for all three.

        With working Pulumi code for each.
---

The best way to provision a Kubernetes cluster is with infrastructure as code: define the cluster in a real programming language, run one command to create it, and keep that definition in version control so every change is reviewable and repeatable. Pulumi does this for EKS, AKS, and GKE in Python, TypeScript, Go, C#, or Java, no YAML templates required.

<!--more-->

## What is the best way to provision a Kubernetes cluster?

The best way to provision a Kubernetes cluster is with infrastructure as code, rather than clicking through a cloud console or hand-writing YAML. Infrastructure as code lets you define the cluster, its node pools, and its networking in a single program, review changes before they apply, and reproduce the same cluster in another region or account. Pulumi supports this pattern natively for EKS, AKS, and GKE.

## How to provision a Kubernetes cluster with infrastructure as code

Provisioning a managed Kubernetes cluster with Pulumi follows the same shape regardless of cloud. Before starting, you need a Pulumi CLI installation, an account with the cloud you're targeting (an AWS account, an Azure account, or a Google Cloud account), and either Node.js and npm or Python installed, depending on which language you choose.

1. Install the Pulumi CLI and run `pulumi new` to scaffold a project, choosing the template for your target cloud and language.
2. Authenticate the Pulumi provider against your cloud account using its normal credential mechanism, such as environment variables or a CLI login.
3. Declare the cluster resource in your program: an `eks.Cluster` for AWS, a `containerservice.ManagedCluster` for Azure, or a `gcp.container.Cluster` for Google Cloud.
4. Configure the cluster's size and node type through the resource's arguments rather than a separate config file.
5. Run `pulumi preview` to see exactly which cloud resources will be created before anything changes.
6. Run `pulumi up` to provision the cluster; Pulumi waits until the control plane and nodes are ready.
7. Export the cluster's `kubeconfig` (or assemble it from the cluster's outputs, on GKE) so `kubectl` and Pulumi's own Kubernetes provider can reach it.
8. Commit the program to version control so the cluster's definition, not just its running state, is reviewable by your team.

## Provisioning an EKS cluster on AWS

The `@pulumi/eks` package wraps the VPC, IAM roles, and node group an EKS cluster needs into a single `Cluster` component, so a working cluster takes only a few lines:

{{< chooser language "typescript,python" / >}}

{{% choosable language "typescript" %}}

```typescript
import * as eks from "@pulumi/eks";

const cluster = new eks.Cluster("eks-cluster", {
    desiredCapacity: 2,
    minSize: 1,
    maxSize: 3,
    instanceType: "t3.medium",
});

export const kubeconfig = cluster.kubeconfig;
```

{{% /choosable %}}

{{% choosable language "python" %}}

```python
import pulumi
import pulumi_eks as eks

cluster = eks.Cluster("eks-cluster",
    desired_capacity=2,
    min_size=1,
    max_size=3,
    instance_type="t3.medium")

pulumi.export("kubeconfig", cluster.kubeconfig)
```

{{% /choosable %}}

`instanceType` describes the default managed node group; a fleet with mixed instance types uses a separate node group resource instead. EKS Auto Mode, covered in our [EKS Auto Mode post](/blog/aws-eks-auto-mode/), is a newer alternative that lets AWS manage node provisioning entirely, but the default node group above remains the registry's canonical starting point.

## Provisioning an AKS cluster on Azure

AKS clusters go through `@pulumi/azure-native`'s `ManagedCluster` resource. Credentials for `kubectl` come back from a separate call that must be decoded from base64:

{{< chooser language "typescript,python" / >}}

{{% choosable language "typescript" %}}

```typescript
import * as containerservice from "@pulumi/azure-native/containerservice";
import * as resources from "@pulumi/azure-native/resources";

const resourceGroup = new resources.ResourceGroup("rg");

const cluster = new containerservice.ManagedCluster("aks-cluster", {
    resourceGroupName: resourceGroup.name,
    agentPoolProfiles: [{
        count: 3,
        mode: "System",
        name: "agentpool",
        osType: "Linux",
        type: "VirtualMachineScaleSets",
        vmSize: "Standard_DS2_v2",
    }],
    dnsPrefix: resourceGroup.name,
    enableRBAC: true,
    identity: { type: "SystemAssigned" },
});

const creds = containerservice.listManagedClusterUserCredentialsOutput({
    resourceGroupName: resourceGroup.name,
    resourceName: cluster.name,
});

export const kubeconfig = creds.kubeconfigs[0].value
    .apply(enc => Buffer.from(enc, "base64").toString());
```

{{% /choosable %}}

{{% choosable language "python" %}}

```python
import base64
import pulumi
from pulumi_azure_native import containerservice, resources

resource_group = resources.ResourceGroup("rg")

cluster = containerservice.ManagedCluster("aks-cluster",
    resource_group_name=resource_group.name,
    agent_pool_profiles=[{
        "count": 3,
        "mode": "System",
        "name": "agentpool",
        "os_type": "Linux",
        "type": "VirtualMachineScaleSets",
        "vm_size": "Standard_DS2_v2",
    }],
    dns_prefix=resource_group.name,
    enable_rbac=True,
    identity={"type": "SystemAssigned"})

creds = containerservice.list_managed_cluster_user_credentials_output(
    resource_group_name=resource_group.name,
    resource_name=cluster.name)

def decode(kubeconfigs):
    return base64.b64decode(kubeconfigs[0]["value"]).decode()

pulumi.export("kubeconfig", creds.kubeconfigs.apply(decode))
```

{{% /choosable %}}

Azure returns the kubeconfig base64-encoded from `listManagedClusterUserCredentialsOutput`, so decoding it is a required step, not an optional cleanup pass.

## Provisioning a GKE cluster on Google Cloud

GKE splits cluster and node pool into two resources in `@pulumi/gcp`, and it defaults `deletionProtection` to `true`, which must be set explicitly for a cluster you intend to tear down later:

{{< chooser language "typescript,python" / >}}

{{% choosable language "typescript" %}}

```typescript
import * as gcp from "@pulumi/gcp";

const cluster = new gcp.container.Cluster("gke-cluster", {
    initialNodeCount: 1,
    removeDefaultNodePool: true,
    deletionProtection: false,
});

const nodePool = new gcp.container.NodePool("primary", {
    cluster: cluster.name,
    location: cluster.location,
    initialNodeCount: 2,
    nodeConfig: { machineType: "e2-medium" },
}, { dependsOn: [cluster] });

export const clusterName = cluster.name;
```

{{% /choosable %}}

{{% choosable language "python" %}}

```python
import pulumi
from pulumi_gcp import container

cluster = container.Cluster("gke-cluster",
    initial_node_count=1,
    remove_default_node_pool=True,
    deletion_protection=False)

node_pool = container.NodePool("primary",
    cluster=cluster.name,
    location=cluster.location,
    initial_node_count=2,
    node_config={"machine_type": "e2-medium"},
    opts=pulumi.ResourceOptions(depends_on=[cluster]))

pulumi.export("cluster_name", cluster.name)
```

{{% /choosable %}}

There is no `@pulumi/gke` package and no built-in `.kubeconfig` output the way `@pulumi/eks` provides one; a GKE kubeconfig is assembled from the cluster's name, endpoint, and `masterAuth.clusterCaCertificate`, plus the `gke-gcloud-auth-plugin` exec entry Google's provider now requires. That asymmetry across the three clouds is real, not an oversight in this guide.

## Deploying an application to the cluster you just created

Provisioning a cluster and deploying an application onto it are separate steps. Once any of the three clusters above is up, point Pulumi's Kubernetes provider at its kubeconfig and declare a Deployment the same way you declared the cluster:

```typescript
import * as k8s from "@pulumi/kubernetes";

const provider = new k8s.Provider("cluster", { kubeconfig });

const appLabels = { app: "hello" };
new k8s.apps.v1.Deployment("hello", {
    spec: {
        replicas: 2,
        selector: { matchLabels: appLabels },
        template: {
            metadata: { labels: appLabels },
            spec: { containers: [{ name: "hello", image: "nginx:latest" }] },
        },
    },
}, { provider });
```

For a full walkthrough of deploying a workload onto an existing cluster, including Services and scaling, see Pulumi's [Kubernetes get-started guide](/docs/iac/get-started/kubernetes/). That guide assumes a cluster already exists; this post is what creates one.

## How the three managed services compare

| | EKS (AWS) | AKS (Azure) | GKE (Google Cloud) |
|---|---|---|---|
| Pulumi package | `@pulumi/eks` | `@pulumi/azure-native` | `@pulumi/gcp` |
| Control plane management | Fully managed by AWS | Fully managed by Azure | Fully managed by Google Cloud |
| Node management | Managed node group by default | Agent pool profile | Separate node pool resource |
| Kubeconfig | Direct `cluster.kubeconfig` output | Base64-encoded credential call | Assembled from cluster fields plus an auth plugin |
| Teardown gotcha | None by default | None by default | `deletionProtection` must be set to `false` first |

## Where to go next

- [Best tools for managing Kubernetes infrastructure as code in 2026](/blog/best-kubernetes-iac-tools-2026/) compares Pulumi against Terraform, CDK, and Crossplane for Kubernetes workloads.
- [Terraform and Kubernetes: a practical guide for 2026](/blog/terraform-kubernetes/) looks at what changes if you're migrating an existing Terraform-managed cluster.
- [Pulumi's cloud provider guides](/docs/iac/guides/clouds/) cover AWS, Azure, and Google Cloud setup in more depth than fits in one post.
- [Deploying to Kubernetes with Pulumi](/docs/iac/get-started/kubernetes/) is the next step once your cluster is running.

## Frequently asked questions

### How do I provision an EKS cluster with infrastructure as code?

Use the `@pulumi/eks` package (or `pulumi_eks` in Python), which wraps the underlying AWS resources an EKS cluster needs into a single `Cluster` component. A minimal program creates the cluster, its managed node group, and its `kubeconfig` output in under twenty lines, with no separate IAM role or VPC wiring required for a default setup. Running `pulumi up` provisions the whole cluster in one step.

### How do I deploy an application to a Kubernetes cluster?

You provision the cluster first, then deploy applications onto it separately. Once a cluster exists, point Pulumi's Kubernetes provider at its kubeconfig and declare Deployments, Services, and other objects the same way you declared the cluster itself. Pulumi's [Kubernetes get-started guide](/docs/iac/get-started/kubernetes/) walks through deploying a workload to an existing cluster step by step.

### Can I manage EKS, AKS, and GKE clusters from one Pulumi project?

Yes. Pulumi projects are not tied to a single cloud, so one program can create an EKS cluster with `@pulumi/eks`, an AKS cluster with `@pulumi/azure-native`, and a GKE cluster with `@pulumi/gcp` side by side, using ordinary conditionals or separate stacks per cloud. Each provider authenticates against its own cloud account, and Pulumi tracks all three clusters' state independently.

### How long does it take to provision a managed Kubernetes cluster?

Provisioning time is set by the cloud provider, not Pulumi: EKS control planes typically take ten to fifteen minutes, AKS around ten minutes, and GKE five to ten minutes, plus a few minutes more for worker nodes to join. `pulumi up` blocks until the cluster and its `kubeconfig` are ready, so the program's own runtime adds negligible overhead beyond the cloud's provisioning time.

### Do I need to write YAML to manage Kubernetes with Pulumi?

No. Pulumi's Kubernetes provider represents Deployments, Services, and every other Kubernetes object as typed resources in Python, TypeScript, Go, C#, or Java, so you get autocomplete, type checking, and real functions and loops instead of YAML templating. You can still apply existing YAML manifests directly if you have them, but writing new YAML is never required.

### How do I destroy a cluster I provisioned with Pulumi?

Run `pulumi destroy` from the same project. For EKS and AKS this tears down the cluster and its supporting resources directly. For GKE, set `deletionProtection: false` on the `Cluster` resource before destroying; Google's provider defaults `deletionProtection` to `true`, and `pulumi destroy` fails against a protected cluster until that flag is turned off.

### Is a managed Kubernetes service better than running Kubernetes myself?

For most teams, yes. EKS, AKS, and GKE each run and patch the control plane for you, handle etcd and API server availability, and integrate with their cloud's identity and networking systems out of the box. Self-managed Kubernetes gives more control over the control plane itself, but that control comes with real operational cost most teams would rather spend on their applications.

### What is the difference between provisioning a cluster and deploying to it?

Provisioning creates the cluster: the control plane, node pools, and networking a cloud provider manages on your behalf. Deploying means declaring the applications and services that run inside an already-running cluster, such as Deployments and Services managed through Kubernetes' own API. Pulumi handles both, but they are separate steps using separate resources.

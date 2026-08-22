---
title: "GPU Kubernetes Infrastructure for AI Workloads with Pulumi"
date: 2026-08-01
draft: false
meta_desc: "How to provision, schedule, and govern GPU capacity on Kubernetes with Pulumi: node pools, Kueue quotas, time-slicing, and cost guardrails."
authors:
    - pulumi-content-team
tags:
    - kubernetes
    - ai
    - gpu
    - infrastructure-as-code
    - platform-engineering
category: general
faq_schema: true
howto_schema: true
social:
    twitter: |
        Agent frameworks get the headlines, but the GPUs underneath them are what actually run out first.

        Here's how to provision GPU node pools on Kubernetes with Pulumi, and keep them from being wasted with Kueue quotas and time-slicing.
    linkedin: |
        Every "agentic infrastructure" conversation eventually hits the same wall: someone has to provision, schedule, and pay for the GPUs underneath it.

        This post covers the layer most agent-framework content skips: GPU node pools on EKS, GKE, and AKS with Pulumi, Kueue-based quotas and ClusterQueues so teams don't starve each other, taints and tolerations to keep GPU nodes for GPU work, and time-slicing vs. MIG for when a workload doesn't need a whole card.

        If you're building the agent runtime itself, our post on running AI agents on Kubernetes is the right next stop. This one is about the substrate underneath it.
    bluesky: |
        The agent runtime gets the attention, but the GPU node pool underneath it is what actually runs out.

        Here's how to provision and govern GPU capacity on Kubernetes with Pulumi.
---

Provisioning GPU infrastructure for AI workloads on Kubernetes means creating GPU-backed node pools, installing a device plugin so the scheduler can see the accelerators, and adding quotas, taints, and cost guardrails so GPU capacity is shared fairly instead of claimed by whichever job launches first. On any major cloud, Pulumi provisions all of it, cluster and node pool alike, in the same program and the same language as everything else you deploy.

That is the substrate question. It's a different question from "how do I run an AI agent on Kubernetes," which is about the runtime: agent CRDs, tool-calling controllers, and the orchestration loop that decides what an agent is allowed to do. If that's what you're after, [our post on running AI agents on Kubernetes](/blog/ai-agents-on-kubernetes/) covers it end to end. This post is about the layer underneath: the GPU capacity every agent, model server, and training job ultimately competes for.

<!--more-->

## Why the compute substrate is the new platform boundary

Platform engineering predictions for 2026 keep circling back to the same idea: agents are becoming a first-class user of the platform, not a side project. Luca Galante, Managing Director & Senior Analyst at Weave Intelligence, put it directly in [10 platform engineering predictions for 2026](https://platformengineering.org/blog/10-platform-engineering-predictions-for-2026):

> "Prediction 1: Agentic infrastructure becomes standard architecture. AI agents will graduate from experimental tools to first-class platform citizens. By 2026, mature platforms will treat agents like any other user persona, complete with RBAC permissions, resource quotas, and governance policies."

Resource quotas and governance policies are exactly where GPU capacity planning lives. An agent with RBAC permissions but no GPU quota can still starve every other team's workload the moment it starts fanning out inference calls. The runtime layer decides what an agent can do; the substrate layer decides how much compute it can actually get, and that's the part that has to be provisioned, scheduled, and metered deliberately, not discovered by accident during an incident.

## What does a production GPU stack on Kubernetes actually include?

A GPU-ready cluster is more than a node pool with bigger instance types. Each layer below solves a distinct problem, and skipping one shows up later as an outage or a surprise bill.

| Layer | What it does | Typical Pulumi resource |
|---|---|---|
| GPU node pool | Adds nodes with attached accelerators (NVIDIA A100/H100/L4, etc.) to an existing cluster | `aws.eks.NodeGroup`, `gcp.container.NodePool`, `azure-native.containerservice.AgentPool` |
| Device plugin / GPU operator | Exposes GPUs as a schedulable resource (`nvidia.com/gpu`) to the Kubernetes scheduler | `kubernetes.helm.v4.Chart` (NVIDIA GPU Operator or device plugin) |
| Taints and tolerations | Keeps non-GPU workloads off expensive GPU nodes, and vice versa | Node pool `taints` property + pod `tolerations` |
| Quota and scheduling | Enforces per-team or per-namespace GPU limits and fair-share queuing | Kueue `ClusterQueue` / `ResourceFlavor` via `apiextensions.CustomResource`, or `kubernetes.core.v1.ResourceQuota` |
| Sharing strategy | Lets multiple workloads share one GPU when a job doesn't need a full card | Time-slicing config or NVIDIA MIG partition |
| Serving layer | Runs the actual model or agent workload against the provisioned capacity | KServe `InferenceService`, or your own Deployment |

Pulumi provisions every row in that table as ordinary resources in the same program, with the same testing, previews, and diffs you already use for the rest of your infrastructure.

## How do you provision a GPU node pool on Kubernetes with Pulumi?

The shape is the same across clouds: create (or reference) a cluster, add a node pool that requests GPU-backed instances, taint it so only GPU workloads land there, and install the operator that exposes GPUs to the scheduler.

1. Provision or reference an existing Kubernetes cluster with the cluster resource for your cloud of choice — `eks.Cluster` on AWS, `gcp.container.Cluster` on Google Cloud, or `azure-native.containerservice.ManagedCluster` on Azure.
2. Add a GPU-backed node pool using a GPU instance type or machine type (for example, `g5.xlarge` on AWS, `a2-highgpu-1g` on Google Cloud, or `Standard_NC24ads_A100_v4` on Azure).
3. Apply a taint to the GPU node pool, such as `nvidia.com/gpu=present:NoSchedule`, so only pods with a matching toleration are scheduled there.
4. Install the NVIDIA GPU Operator (or cloud-managed device plugin) with a Helm chart so the scheduler can see and allocate `nvidia.com/gpu` as a resource.
5. Define a Kueue `ResourceFlavor` and `ClusterQueue` (or a `ResourceQuota`) that caps how many GPUs a namespace or team can claim at once.
6. Deploy a GPU-requesting workload, such as a KServe `InferenceService` or a training Job, with a toleration for the GPU taint and a resource request for `nvidia.com/gpu`.

Here is the node pool and GPU Operator install in TypeScript, targeting AWS EKS:

```typescript
import * as aws from "@pulumi/aws";
import * as eks from "@pulumi/eks";
import * as k8s from "@pulumi/kubernetes";

const cluster = new eks.Cluster("ai-platform", {
    instanceType: "t3.medium",
    desiredCapacity: 2,
    minSize: 1,
    maxSize: 3,
});

const gpuNodeGroup = new eks.NodeGroup("gpu-pool", {
    cluster: cluster,
    instanceType: "g5.xlarge",
    gpu: true,
    desiredCapacity: 1,
    minSize: 0,
    maxSize: 4,
    labels: { "workload-type": "gpu" },
    taints: {
        "nvidia.com/gpu": {
            value: "present",
            effect: "NoSchedule",
        },
    },
});

const provider = new k8s.Provider("gpu-cluster", {
    kubeconfig: cluster.kubeconfig,
});

const gpuOperator = new k8s.helm.v4.Chart("gpu-operator", {
    chart: "gpu-operator",
    namespace: "gpu-operator",
    repositoryOpts: { repo: "https://helm.ngc.nvidia.com/nvidia" },
}, { provider, dependsOn: [gpuNodeGroup] });
```

The same shape in Python, targeting Google Kubernetes Engine:

```python
import pulumi
import pulumi_gcp as gcp
import pulumi_kubernetes as k8s

cluster = gcp.container.Cluster(
    "ai-platform",
    initial_node_count=1,
    remove_default_node_pool=True,
)

gpu_node_pool = gcp.container.NodePool(
    "gpu-pool",
    cluster=cluster.name,
    node_count=1,
    autoscaling=gcp.container.NodePoolAutoscalingArgs(
        min_node_count=0,
        max_node_count=4,
    ),
    node_config=gcp.container.NodePoolNodeConfigArgs(
        machine_type="a2-highgpu-1g",
        guest_accelerators=[gcp.container.NodePoolNodeConfigGuestAcceleratorArgs(
            type="nvidia-tesla-a100",
            count=1,
        )],
        taints=[gcp.container.NodePoolNodeConfigTaintArgs(
            key="nvidia.com/gpu",
            value="present",
            effect="NO_SCHEDULE",
        )],
        labels={"workload-type": "gpu"},
    ),
)

provider = k8s.Provider(
    "gpu-cluster",
    kubeconfig=pulumi.Config().require_secret("kubeconfig"),
)

gpu_operator = k8s.helm.v4.Chart(
    "gpu-operator",
    chart="gpu-operator",
    namespace="gpu-operator",
    repository_opts=k8s.helm.v4.RepositoryOptsArgs(
        repo="https://helm.ngc.nvidia.com/nvidia",
    ),
    opts=pulumi.ResourceOptions(provider=provider, depends_on=[gpu_node_pool]),
)
```

Both programs do the same three things: request GPU-backed nodes, taint them so ordinary workloads can't land there by accident, and install the operator that turns physical accelerators into a schedulable Kubernetes resource. Credentials for the cluster follow the same pattern as the rest of your Pulumi stack: pull them from Pulumi ESC rather than hardcoding a kubeconfig. In practice that means an ESC environment whose `pulumiConfig` section supplies the `kubeconfig` value that `pulumi.Config().require_secret("kubeconfig")` reads above; [Kubernetes cluster access with ESC](/docs/esc/guides/integrate-with/kubernetes-cluster-access/) shows the environment definition, including how to build that kubeconfig from a short-lived cloud login rather than a static credential.

## How do you keep GPU capacity from being wasted or blown through?

A GPU node pool without quotas is a shared resource with no rules, and the first team to notice finds out by having their job queued indefinitely behind someone else's. A few guardrails make the difference:

- **Per-team quotas.** A Kueue `ClusterQueue` paired with a `ResourceFlavor` scoped to your GPU node pool lets you cap how many GPUs each namespace or team can claim concurrently, with fair-share queuing when demand exceeds supply. A plain Kubernetes `ResourceQuota` on `requests.nvidia.com/gpu` covers simpler cases.
- **Taints and tolerations, not labels alone.** Labels tell the scheduler what a node *has*; taints tell it what a node *requires*. Use both, so a misconfigured pod without a GPU workload can't accidentally land on (and occupy) an expensive node.
- **Sharing strategy for partial workloads.** Not every workload needs a full accelerator. Time-slicing lets multiple pods share one GPU's compute cycles for latency-tolerant workloads; NVIDIA MIG partitions a single GPU into isolated, right-sized instances when workloads need dedicated memory and stronger isolation. Pick MIG when noisy-neighbor effects matter, time-slicing when they don't.
- **Autoscaling floors, not just ceilings.** Set `minSize: 0` on the GPU node pool so idle capacity actually scales to zero between jobs. GPU instances are the line item that makes an unbounded floor expensive fast.
- **Policy as code for anything else.** Enforcing "no GPU pod without a resource request," "no GPU pod without a namespace label," or "no GPU node pool above N nodes without an approval" is a policy-as-code problem, not a code-review problem, once more than one team shares the cluster.

## How do models and agents actually consume that capacity?

Once GPU nodes, quotas, and sharing rules exist, the serving layer is what actually claims them. A KServe `InferenceService` requests `nvidia.com/gpu` the same way any other pod does, and lands on the tainted GPU node pool because it carries the matching toleration. From there, whether the caller is a REST client, a batch job, or an autonomous agent making a tool call is a runtime concern, not a substrate one. That's the layer [our post on running AI agents on Kubernetes](/blog/ai-agents-on-kubernetes/) is built around, covering the agent CRDs, orchestration, and governance that sit on top of exactly the capacity this post provisions.

Joe Duffy summed up why the underlying infrastructure has to be code, not YAML or a ClickOps console, in [The Agentic Infrastructure Era](/blog/the-agentic-infrastructure-era/):

> "At the same time, we're seeing something magical happen here at Pulumi: LLMs are now doing over 20% of the infrastructure deployments, up from virtually zero a year ago."

A fifth of infrastructure changes being LLM-authored is exactly why the GPU layer needs the same testability and diff-ability as everything else in the stack. An agent proposing a change to a GPU node pool's `maxSize` or a Kueue quota should go through a `pulumi preview`, not a console click nobody reviews.

## Frequently asked questions

### How do you run GPU workloads on Kubernetes?

Add a GPU-backed node pool to your cluster, install the NVIDIA GPU Operator (or your cloud's managed device plugin) so the scheduler can see GPUs as a resource, then deploy workloads with a `nvidia.com/gpu` resource request and a toleration matching the node pool's taint.

### Do you need a GPU operator on Kubernetes?

Yes, in some form. Without a device plugin or GPU operator installed, Kubernetes has no way to know a node has an accelerator attached, and the scheduler will never place a GPU-requesting pod on it, even if the underlying instance has a card.

### How do you limit GPU costs on Kubernetes?

Combine autoscaling GPU node pools with `minSize: 0` so idle capacity scales down, quotas via Kueue `ClusterQueue`s or `ResourceQuota`s so no single team can claim the whole pool, and a sharing strategy (time-slicing or MIG) so workloads that don't need a full accelerator don't reserve one.

### Can Pulumi manage GPU node pools across AWS, Azure, and Google Cloud?

Yes. Pulumi's `aws.eks.NodeGroup`, `gcp.container.NodePool`, and `azure-native.containerservice.AgentPool` resources all support GPU-backed instance types, and can be provisioned from the same program alongside the operator, quota, and serving resources that sit on top of them.

### What is the difference between GPU time-slicing and MIG on Kubernetes?

Time-slicing lets multiple pods share one GPU's compute cycles in turn, with no hard isolation between them, which suits latency-tolerant or bursty workloads. MIG (Multi-Instance GPU) physically partitions a supported NVIDIA GPU into isolated instances with dedicated memory, which suits workloads that need predictable performance and can't tolerate a noisy neighbor.

## Where to go next

- [How to Run AI Agents on Kubernetes with Pulumi](/blog/ai-agents-on-kubernetes/) — the agent runtime layer that consumes the capacity this post provisions.
- [The Agentic Infrastructure Era](/blog/the-agentic-infrastructure-era/) — why infrastructure needs to be verifiable code as more of it is agent-authored.
- [Best AI Infrastructure Tools](/blog/ai-infrastructure-tools/) — a broader look at the AI infrastructure landscape.
- [Pulumi Kubernetes provider docs](/registry/packages/kubernetes/) — full resource reference for clusters, node pools, and workloads.
- [Pulumi ESC](/docs/esc/) — for brokering cloud credentials into GPU-provisioning stacks without static keys.

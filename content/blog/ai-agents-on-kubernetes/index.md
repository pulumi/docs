---
title: "How to Run AI Agents on Kubernetes with Pulumi"
date: 2026-07-28
draft: false
meta_desc: "How to provision and govern Kubernetes infrastructure for AI agents with Pulumi, in TypeScript and Python, and where kagent, KServe, Kueue, and Neo fit in."
authors:
    - joe-duffy
tags:
    - kubernetes
    - ai-agents
    - platform-engineering
    - pulumi-neo
    - infrastructure-as-code
    - mcp
category: general
faq_schema: true
howto_schema: true

# Social media copy — auto-posted to X, LinkedIn, and Bluesky when merged to master.
# Character limits: X ~280, Bluesky 300, LinkedIn 3000. Leave blank to skip a platform.
social:
    twitter: |
        66% of organizations plan to run generative AI workloads on Kubernetes (CNCF, 2026). But an agent isn't a stateless web service, and treating it like one gets expensive fast.

        Here's how to provision and govern that infrastructure with Pulumi.
    linkedin: |
        Kubernetes has quietly become the default substrate for agentic AI. CNCF's 2026 annual survey puts it at 66% of organizations betting on Kubernetes for generative AI workloads, and a fast-moving ecosystem — kagent, KServe, Kueue, vLLM/llm-d, the Gateway API Inference Extension — has grown up around running agents and models on the cluster.

        The catch: an AI agent is not a stateless web service. It needs GPU-aware scheduling, long-lived and bursty sessions, credentials for whatever it's allowed to touch, and a blast radius that's very different from a typical Deployment.

        We wrote up how we think about provisioning and governing that infrastructure with Pulumi — real TypeScript and Python, not just YAML, plus where policy-as-code, secrets management, and Pulumi Neo fit in when the infrastructure itself has to answer to an agent.
    bluesky: |
        An AI agent on Kubernetes isn't just another Deployment: GPUs, long-lived sessions, and a much bigger credential blast radius.

        Here's how to provision and govern that infrastructure with Pulumi, in TypeScript and Python.
---

Kubernetes has become the default place teams run agentic AI workloads: CNCF's 2026 annual survey found that 66% of organizations are betting on Kubernetes to run their generative AI workloads.[^cncf-survey] An entire ecosystem has grown up around that fact — agent runtimes, model servers, GPU schedulers — and most of it assumes the infrastructure underneath is already handled. It usually isn't. An AI agent is not a stateless web service, and provisioning for one takes more than copying a Deployment YAML and swapping the image.

<!--more-->

I spend a lot of my time these days thinking about what changes when the thing consuming your infrastructure isn't a person or a fixed pipeline, but an agent making its own calls about what to do next — and Kubernetes is where I keep seeing that question show up first, because it's already where most teams run everything else. This post is about that gap: what changes about Kubernetes infrastructure when the workload is an agent, what the current agentic-Kubernetes ecosystem actually looks like, and how to provision and govern that infrastructure with [Pulumi](/docs/iac/get-started/kubernetes/) using TypeScript and Python — plus where [Pulumi Neo](/product/neo/) fits once the infrastructure itself has to answer to an agent. If you haven't read our take on the broader shift toward agentic infrastructure, [What Is Agentic Infrastructure?](/what-is/what-is-agentic-infrastructure/) is a good companion piece; this post stays specific to the Kubernetes layer.

## What makes agentic AI workloads different from ordinary Kubernetes workloads?

An agent's resource and governance profile looks nothing like a typical web service, largely because it schedules accelerators, holds state across long sessions, and reaches out to systems a normal Deployment never touches.

| Dimension | Typical web service | Agent workload |
| --- | --- | --- |
| Compute | CPU, predictable | Often GPU/accelerator, bursty |
| Session shape | Short-lived, stateless requests | Long-lived sessions, conversational state |
| Egress | Internal services, one database | Model provider APIs, arbitrary tools, other agents |
| Credential surface | A handful of scoped secrets | API keys for one or more model providers, plus whatever tools/MCP servers the agent is allowed to call |
| Access/RBAC | Fixed, narrow | Potentially broad — an agent that can act on infrastructure needs infrastructure-shaped permissions |
| Cost profile | Roughly linear with traffic | Token- and GPU-time-driven, harder to predict |

None of this means Kubernetes is the wrong place to run agents — the opposite: its scheduler, autoscaling, and RBAC primitives are exactly the right building blocks for these problems. It means the infrastructure around an agent deserves more deliberate design than "reuse the Deployment template," particularly around GPU scheduling, secrets, and the blast radius of what the agent is allowed to do.

## What does the agentic Kubernetes stack look like in 2026?

There isn't one "agents on Kubernetes" product; there's a stack, and most of it is open source and CNCF-adjacent. Being fair to that ecosystem matters here, because Pulumi's job is to provision and govern the infrastructure underneath these tools, not to replace them.

| Project | What it does | Status |
| --- | --- | --- |
| [kagent](https://kagent.dev/) | Framework for running AI agents on Kubernetes, with its own MCP server and CRDs for agents and model providers | CNCF Sandbox (accepted May 22, 2025)[^kagent-cncf] |
| [KServe](https://kserve.github.io/website/) | Model-serving on Kubernetes | CNCF Incubating (accepted Sept 29, 2025)[^kserve-cncf] |
| [Kueue](https://kueue.sigs.k8s.io/) | Job queueing for batch and ML workloads | CNCF Sandbox |
| [KubeRay](https://github.com/ray-project/kuberay) | Runs Ray (and Ray Serve) clusters on Kubernetes | Kubernetes SIG / Ray ecosystem project |
| vLLM + [llm-d](https://llm-d.ai/) | High-throughput, Kubernetes-native distributed LLM inference | Red Hat-launched, community project |
| [LeaderWorkerSet](https://github.com/kubernetes-sigs/lws) / [JobSet](https://github.com/kubernetes-sigs/jobset) | Multi-node inference and batch training workload APIs | kubernetes-sigs |
| Dynamic Resource Allocation (DRA) | Kubernetes-native API for scheduling GPUs and other accelerators | GA in Kubernetes v1.34[^dra-ga] |
| [Gateway API Inference Extension](https://gateway-api-inference-extension.sigs.k8s.io/) | Routing and load balancing tuned for LLM inference traffic | GA |
| [NVIDIA GPU Operator](https://github.com/NVIDIA/gpu-operator) | Manages NVIDIA drivers and device plugins on cluster nodes | NVIDIA-maintained |

kagent is worth a closer look since it's the piece most directly aimed at "run an agent on Kubernetes." As of its current release (v0.9.9), it defines its own custom resources — `Agent`, `ModelConfig`, `ModelProviderConfig`, `RemoteMCPServer`, and `SandboxAgent` — and ships an MCP server with built-in tools for Kubernetes, Helm, Istio, Argo, and Prometheus, plus the ability to connect to any external MCP server via the `RemoteMCPServer` CRD.[^kagent-crds] It's a genuinely useful abstraction for defining what an agent can do; it isn't, on its own, an answer for how the *cluster* the agent runs on got there, who's allowed to change it, or how secrets get to it safely. That's the layer Pulumi sits at.

## How do you provision Kubernetes infrastructure for AI agents with Pulumi?

A minimal but representative path from "no cluster" to "an agent running on it, governed" looks like this:

1. Provision a Kubernetes cluster with a GPU-enabled node group sized for your model workload.
2. Install the kagent CRDs and controller onto the cluster using a Pulumi Helm chart resource.
3. Store the model provider's API key as a Pulumi secret sourced from a Pulumi ESC environment, rather than a plaintext Kubernetes Secret.
4. Declare the agent itself as a custom resource so it's versioned and reviewed the same way as everything else in the stack.
5. Attach a policy pack so specific classes of change — like exposing a service publicly, or granting a service account cluster-admin — require an explicit review.
6. Roll changes out through CI, or through the [Pulumi Kubernetes Operator](/docs/integrations/clouds/kubernetes/pulumi-kubernetes-operator/) if you want the cluster itself to reconcile against a Pulumi stack.

Steps 1–4 in TypeScript:

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as kubernetes from "@pulumi/kubernetes";
import * as eks from "@pulumi/eks";

// 1. GPU-enabled node group alongside your existing EKS cluster.
const gpuNodeGroup = new eks.ManagedNodeGroup("agent-gpu-nodes", {
    cluster: eksCluster,
    nodeRole: nodeRole,
    instanceTypes: ["g6.8xlarge"],
    gpu: true,
    scalingConfig: { minSize: 1, desiredSize: 2, maxSize: 4 },
});

const k8sProvider = new kubernetes.Provider("k8s", {
    kubeconfig: eksCluster.kubeconfig,
});

// 2. kagent CRDs and controller via the Helm v4 Chart resource.
const kagentCrds = new kubernetes.helm.v4.Chart("kagent-crds", {
    chart: "oci://ghcr.io/kagent-dev/kagent/helm/kagent-crds",
    namespace: "kagent",
}, { provider: k8sProvider });

const kagent = new kubernetes.helm.v4.Chart("kagent", {
    chart: "oci://ghcr.io/kagent-dev/kagent/helm/kagent",
    namespace: "kagent",
    values: {
        providers: { default: "openAI" },
    },
}, { provider: k8sProvider, dependsOn: [kagentCrds] });

// 3. Model provider API key, sourced as a secret from a Pulumi ESC
// environment (declared in Pulumi.<stack>.yaml, not hardcoded here).
const config = new pulumi.Config();
const openAiApiKey = config.requireSecret("openAiApiKey");

const providerSecret = new kubernetes.core.v1.Secret("openai-credentials", {
    metadata: { namespace: "kagent" },
    stringData: { apiKey: openAiApiKey },
}, { provider: k8sProvider });

// 4. The agent itself, as a versioned custom resource.
const agent = new kubernetes.apiextensions.CustomResource("k8s-ops-agent", {
    apiVersion: "kagent.dev/v1alpha2",
    kind: "Agent",
    metadata: { namespace: "kagent" },
    spec: {
        description: "Answers questions about cluster state and proposes fixes",
        modelConfig: "openai-gpt",
        tools: ["kubernetes", "helm"],
    },
}, { provider: k8sProvider, dependsOn: [kagent] });
```

The same four steps in Python:

```python
import pulumi
import pulumi_eks as eks
import pulumi_kubernetes as kubernetes
from pulumi_kubernetes import apiextensions

# 1. GPU-enabled node group alongside your existing EKS cluster.
gpu_node_group = eks.ManagedNodeGroup("agent-gpu-nodes",
    cluster=eks_cluster,
    node_role=node_role,
    instance_types=["g6.8xlarge"],
    gpu=True,
    scaling_config={"min_size": 1, "desired_size": 2, "max_size": 4})

k8s_provider = kubernetes.Provider("k8s", kubeconfig=eks_cluster.kubeconfig)

# 2. kagent CRDs and controller via the Helm v4 Chart resource.
kagent_crds = kubernetes.helm.v4.Chart("kagent-crds",
    chart="oci://ghcr.io/kagent-dev/kagent/helm/kagent-crds",
    namespace="kagent",
    opts=pulumi.ResourceOptions(provider=k8s_provider))

kagent = kubernetes.helm.v4.Chart("kagent",
    chart="oci://ghcr.io/kagent-dev/kagent/helm/kagent",
    namespace="kagent",
    values={"providers": {"default": "openAI"}},
    opts=pulumi.ResourceOptions(provider=k8s_provider, depends_on=[kagent_crds]))

# 3. Model provider API key, sourced as a secret from a Pulumi ESC
# environment (declared in Pulumi.<stack>.yaml, not hardcoded here).
config = pulumi.Config()
openai_api_key = config.require_secret("openAiApiKey")

provider_secret = kubernetes.core.v1.Secret("openai-credentials",
    metadata={"namespace": "kagent"},
    string_data={"apiKey": openai_api_key},
    opts=pulumi.ResourceOptions(provider=k8s_provider))

# 4. The agent itself, as a versioned custom resource.
agent = apiextensions.CustomResource("k8s-ops-agent",
    api_version="kagent.dev/v1alpha2",
    kind="Agent",
    metadata={"namespace": "kagent"},
    spec={
        "description": "Answers questions about cluster state and proposes fixes",
        "modelConfig": "openai-gpt",
        "tools": ["kubernetes", "helm"],
    },
    opts=pulumi.ResourceOptions(provider=k8s_provider, depends_on=[kagent]))
```

The `Pulumi.<stack>.yaml` for the stack pulls the API key from an ESC environment instead of a plaintext value in source control:

```yaml
environment:
  - agents-team/production
```

Verify the exact CRD group/version (`kagent.dev/v1alpha2` above) against kagent's own CRD manifests before you ship this in production — CRD APIs move faster than blog posts do.

## Why write agent infrastructure in a general-purpose language instead of templated YAML?

Because an agent's infrastructure has exactly the kind of conditional, repeated, testable shape that general-purpose languages are built for, and templated YAML is not. A `for` loop that provisions one GPU node pool per region, a function that returns a standard "agent + its guardrail policy" bundle, a unit test that asserts a policy pack actually blocks an over-privileged service account before it ships — all of that is native to TypeScript, Python, Go, C#, and Java, and bolted-on at best in Helm templates or raw manifests.

This isn't a knock on Helm or Kustomize, which remain genuinely good tools for packaging and distributing charts — including kagent's own install, which is a Helm chart for a reason. The distinction is what you're doing with the result. Distributing a reusable, versioned package is a job Helm is built for. Composing that package into your specific cluster, wiring its secrets, gating its rollout with policy, and testing the whole thing before it ships is software engineering, and it benefits from a real language: loops, functions, types, unit tests, and the same CI/CD your application code already runs through.

## How do you keep agent workloads governed, least-privileged, and cost-aware?

An agent that can act on infrastructure needs infrastructure-shaped guardrails, not just a service account and a prayer. Three pieces of the Pulumi platform apply directly:

- **Policy as code.** [Pulumi Policies](/docs/insights/policy/) let you write rules — in the same general-purpose languages, not a separate policy DSL — that run before a change is applied: block a `Deployment` requesting cluster-admin, require GPU node pools to carry a cost-center label, or flag any `RemoteMCPServer` pointed at a host outside an allowlist.
- **[Pulumi ESC](/docs/esc/)** for secrets and configuration, so model-provider API keys and other credentials are centrally managed, rotated, and scoped, rather than copy-pasted into `Secret` manifests across every cluster an agent touches.
- **RBAC scoped to the agent's actual job.** The same custom-resource pattern used to declare the agent (shown above) is the natural place to also declare its `ServiceAccount`, `Role`, and `RoleBinding` — as code, reviewed the same way as the agent's own configuration, not layered on afterward.

I want to be precise here about Pulumi Insights, because I see the two products get conflated more than almost anything else we ship: Insights gives you discovery (a searchable inventory of resources across Pulumi, Terraform, CloudFormation, and manually created infrastructure) and policy enforcement, including pre-built compliance packs. Cost-optimization recommendations are a Neo capability, not an Insights one.

## Where does Pulumi Neo fit when the infrastructure itself is agentic?

Neo is Pulumi's own infrastructure agent, and it's worth being specific about what it actually does today rather than leaning on the general "AI for infrastructure" framing. Documented capabilities include answering questions about your existing infrastructure, proposing changes and opening a pull request for them, running a preview before anything lands, reviewing PRs, and taking on recurring maintenance work using your team's established Pulumi practices.[^neo-docs] The [Infrastructure AI docs](/docs/ai/) cover each of these in more depth.

The thing I care about most with Neo is trust, and trust gets earned one reviewed pull request at a time, not granted upfront. That's why every capability starts human-in-the-loop and only earns more autonomy once the guardrails have proven themselves in practice — the same discipline this post argues for everywhere else an agent touches your Kubernetes infrastructure. Pulumi's own product blog has also described Neo handling things like Terraform-to-Pulumi migrations and containerizing and migrating a service onto Kubernetes.[^neo-things]

The relevant framing for this post: Neo doesn't replace kagent, KServe, or any other workload-level agent framework running inside your cluster — it operates one layer up, on the infrastructure that provisions and governs the cluster itself. If your team is running kagent-based agents on Kubernetes, Neo is the thing that can propose the PR that adds a new GPU node pool, review the policy-pack change that locks down a `RemoteMCPServer`, or handle the maintenance toil around keeping that stack current.

## Frequently asked questions

### How do you deploy AI agents on Kubernetes?

Provision a cluster (with GPU node pools if your agent needs them), install an agent runtime — [kagent](https://kagent.dev/) is one of the more Kubernetes-native options as of 2026 — and declare the agent as a custom resource alongside its model configuration and any MCP tool servers it needs. Doing this with Pulumi means the cluster, the runtime install, the secrets, and the agent definition are all one reviewable, testable stack rather than a mix of `kubectl apply` commands run by hand.

### Do you need GPUs to run AI agents on Kubernetes?

Not always. An agent that only calls a hosted model API (OpenAI, Anthropic, and similar) needs CPU nodes to run its own logic and tool calls; the GPU-heavy work happens on the provider's infrastructure, not yours. GPUs matter once you're self-hosting inference — running an open-weight model via vLLM, KServe, or Ray Serve — which is where projects like Kueue, LeaderWorkerSet, and Dynamic Resource Allocation come in.

### How is kagent different from running an agent as a plain Deployment?

A plain `Deployment` gives you a running process; it doesn't give you a standard way to describe an agent's model configuration, its tool access, or its connections to MCP servers as first-class, versionable objects. kagent's CRDs (`Agent`, `ModelConfig`, `ModelProviderConfig`, `RemoteMCPServer`, `SandboxAgent`) exist specifically to make those concepts declarative, so a policy engine, a reviewer, or another automation can reason about them the same way it reasons about a `Deployment` or a `Service`.

### Can Pulumi manage Kubernetes resources that Helm or Terraform already created?

Yes. Pulumi Insights discovers and inventories resources regardless of what provisioned them — Pulumi, Terraform, CloudFormation, or manual changes — which is useful precisely because most clusters running agent workloads already have Helm-installed components like kagent, an ingress controller, or a GPU operator on them. You don't need to rip those out to bring the rest of the stack under Pulumi; `kubernetes.yaml.v2.ConfigFile` and `ConfigGroup` can also adopt existing manifests directly into a Pulumi program.

### What are Kubernetes best practices for AI workloads in 2026?

Match node pools to the workload (GPU pools for self-hosted inference, CPU pools for orchestration and tool-calling), use a queueing layer like Kueue for batch and training jobs so they don't starve latency-sensitive agent traffic, keep model-provider credentials in a secrets manager (not plaintext `Secret` objects), and scope every agent's RBAC to the specific tools it's allowed to call. For general Kubernetes hygiene beyond the AI-specific pieces, see [Kubernetes Best Practices I Wish I Had Known Before](/blog/kubernetes-best-practices-i-wish-i-had-known-before/).

### How does Pulumi Neo help manage Kubernetes infrastructure for AI agents?

Neo operates at the infrastructure layer underneath your agent workloads: it can answer questions about the state of your cluster, propose infrastructure changes as a reviewable pull request, run a preview before anything is applied, review incoming PRs, and take on the recurring maintenance that keeps a Kubernetes-plus-agents stack current — all using your team's existing Pulumi practices rather than a separate workflow.

## Where to go next

If you're starting from zero, the [Kubernetes get-started guide](/docs/iac/get-started/kubernetes/) and the [Kubernetes provider registry](https://www.pulumi.com/registry/packages/kubernetes/) cover the provisioning basics this post builds on. If you're already running agent workloads and want the governance layer, start with [Pulumi Policies](/docs/insights/policy/) and [Pulumi ESC](/docs/esc/). And if agent sprawl — not just agentic Kubernetes workloads, but the broader proliferation of agents across your org — is the more pressing problem, [Agent Sprawl Is Here. Your IaC Platform Is the Answer.](/blog/agent-sprawl-iac-platform-is-the-answer/) is the companion read.

[^cncf-survey]: CNCF Annual Survey Report, January 2026: [cncf.io/wp-content/uploads/2026/01/CNCF_Annual_Survey_Report_final.pdf](https://www.cncf.io/wp-content/uploads/2026/01/CNCF_Annual_Survey_Report_final.pdf).
[^kagent-cncf]: "kagent was accepted to CNCF on May 22, 2025 at the Sandbox maturity level." CNCF Projects: [cncf.io/projects/kagent/](https://www.cncf.io/projects/kagent/).
[^kserve-cncf]: KServe accepted as a CNCF Incubating project, September 29, 2025: [cncf.io/blog/2025/11/11/kserve-becomes-a-cncf-incubating-project/](https://www.cncf.io/blog/2025/11/11/kserve-becomes-a-cncf-incubating-project/).
[^dra-ga]: Dynamic Resource Allocation reached general availability in Kubernetes v1.34 (released August 27, 2025). Kubernetes blog: [kubernetes.io/blog](https://kubernetes.io/blog/).
[^kagent-crds]: kagent CRD kinds (`Agent`, `ModelConfig`, `ModelProviderConfig`, `RemoteMCPServer`, `SandboxAgent`) per the `kagent-dev/kagent` `v1alpha2` API types, and MCP server tooling per the project README: [github.com/kagent-dev/kagent](https://github.com/kagent-dev/kagent).
[^neo-docs]: Pulumi Infrastructure AI / Neo documentation: [pulumi.com/docs/ai/](/docs/ai/).
[^neo-things]: "10 Things You Can Do with Neo" and "10 More Things You Can Do with Neo," Pulumi blog: [pulumi.com/blogs/10-things-you-can-do-with-neo/](https://www.pulumi.com/blogs/10-things-you-can-do-with-neo/), [pulumi.com/blogs/10-more-things-you-can-do-with-neo/](https://www.pulumi.com/blogs/10-more-things-you-can-do-with-neo/).

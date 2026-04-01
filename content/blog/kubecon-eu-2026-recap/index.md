---
title: "KubeCon EU 2026 Recap: The Year AI Moved Into Production on Kubernetes"
allow_long_title: true
date: 2026-04-01T00:00:00-07:00
draft: false
meta_desc: "Recap of KubeCon EU 2026 in Amsterdam: AI in production on Kubernetes, agentic AI identity, inference routing, and platform engineering."
meta_image: meta.png
authors:
    - engin-diri
tags:
    - kubernetes
    - kubecon
    - ai
    - platform-engineering
    - cloud-native
social:
    twitter: "KubeCon EU 2026 just wrapped in Amsterdam. AI moved from demos to production Kubernetes, and inference is the new battleground. Here's what I saw on the ground."
    linkedin: |
        Just back from KubeCon EU 2026 in Amsterdam. 13,350 attendees, and one clear message: AI on Kubernetes has shifted from experimentation to production.

        I wrote up the biggest themes — inference infrastructure, agentic AI identity, gateway routing, sovereignty — and what they mean for platform teams right now.
---

Amsterdam in late March still has that sharp North Sea wind, but inside the RAI Convention Centre, 13,350 people generated enough energy to heat the building twice over. KubeCon + CloudNativeCon EU 2026 was the biggest European edition yet, and the shift from previous years was impossible to miss. AI was the main event. Not a side track, not a buzzword sprinkled into keynotes. The main event.

Here is the stat that framed the entire conference for me: 82% of organizations have adopted Kubernetes for AI workloads, but only 7% deploy to production daily. That gap between experimentation and actual production use defined every conversation I had in Amsterdam. The CNCF's own survey now counts 19.9 million cloud native developers worldwide, 7.3 million of them building AI workloads. The tooling and the infrastructure need to catch up.

My takeaway after four days on the ground: 2026 is the year of ROI. The prototypes are done. Teams are figuring out how to run inference at scale, how to secure agentic AI, how to make GPU infrastructure work like any other production system. Here is what I saw.

<!--more-->

## From training to inference: the big pivot

The numbers tell the story. Sixty-seven percent of AI compute now goes to inference, not training. The inference market is projected to hit $255 billion by 2030. Training gets the headlines, but inference is where the money and the operational complexity actually live.

NVIDIA leaned into this hard. Their open-source stack around NeMo and Dynamo got significant stage time, but the bigger move was donating three projects to the CNCF: the DRA driver for fractional GPU allocation, the KAI Scheduler for GPU-aware scheduling, and Grove. Moving these to community governance signals that GPU infrastructure is no longer a proprietary play. It is becoming part of the standard Kubernetes toolkit.

The SUSE, NVIDIA, and Vultr partnership caught my attention too. SUSE is positioning Rancher as an AI platform, well beyond its roots as a Kubernetes management tool. Combined with NVIDIA's inference stack and Vultr's GPU cloud, the pitch is a full enterprise inference pipeline that you can run on-premises or in the cloud. Whether that coheres into a real product remains to be seen, but the direction is clear: inference infrastructure is a first-class concern for platform teams now.

For Pulumi users, this shift matters directly. Multi-region inference deployments need declarative infrastructure management. You cannot hand-roll Terraform scripts for GPU node pools across three clouds and keep your sanity. [Pulumi's Kubernetes provider](/registry/packages/kubernetes/) and multi-cloud resource management make this the kind of problem IaC was built to solve. Define your inference topology once, deploy it everywhere, and let policy enforcement handle the guardrails.

## The CNCF donations that will reshape AI on Kubernetes

Every KubeCon has its crop of new CNCF projects, but this year's batch felt different. These are not incremental improvements. They are the building blocks of an AI runtime for Kubernetes.

**llm-d** was the headline donation. Created by IBM Research, Red Hat, and Google Cloud, it splits inference workloads by separating prefill and decode phases across different pods. The collaborator list reads like an industry consortium: NVIDIA, CoreWeave, AMD, Cisco, Hugging Face, Intel, Lambda, Mistral AI, UC Berkeley, and UChicago. When that many organizations agree on a single approach to distributed inference, pay attention.

NVIDIA's **DRA driver** enables fractional GPU allocation and multi-node NVLink support. GPU multi-tenancy is one of the hardest unsolved problems in Kubernetes right now. Scheduling, isolation, cost attribution — all of it breaks down when multiple workloads share a GPU. The DRA driver does not solve everything, but it gives the community a real starting point.

**KAI Scheduler** entered the CNCF Sandbox for GPU-aware scheduling. If llm-d handles the inference runtime and the DRA driver handles allocation, KAI Scheduler handles placement. Together, these three projects form the skeleton of a GPU-native Kubernetes stack.

**Velero**, donated by Broadcom, moved into CNCF Sandbox for backup and restore. AI workloads are stateful now (model weights, checkpoints, fine-tuning data), and backup is no longer optional. Good timing.

**Microsoft AI Runway** is an open-source Kubernetes API for inference that plugs in Hugging Face model discovery, GPU memory fit calculations, and cost estimates. Think of it as a model-aware control plane. **HolmesGPT** and **Dalec**, also from Microsoft, entered CNCF Sandbox for AI-powered troubleshooting and dependency analysis.

The **Kubernetes AI Conformance Program** is growing fast, with certifications nearly doubled and three new requirements proposed for Kubernetes 1.36. Conformance programs are boring until they are not. This one will determine which distributions can credibly claim AI readiness.

For platform teams running Pulumi, every one of these projects introduces new CRDs and infrastructure components. [Pulumi's Kubernetes provider](/registry/packages/kubernetes/) handles CRD management natively, so you can adopt llm-d or KAI Scheduler without leaving your existing IaC workflow.

## Agentic AI gets an identity layer

If inference was this year's production story, agentic AI was the architecture story. Agents are proliferating, and nobody has quite figured out how to manage and secure them inside Kubernetes yet.

**kagent**, donated to CNCF Sandbox by Solo.io, defines agents as Kubernetes CRDs. It ships with pre-built MCP (Model Context Protocol) servers for Kubernetes, Istio, Helm, Argo, Prometheus, Grafana, and Cilium. An agent becomes a first-class Kubernetes resource, schedulable and observable and subject to RBAC, instead of a rogue process running in someone's notebook.

**kagenti** from IBM goes after the identity problem directly. Using SPIFFE and SPIRE, it gives agents cryptographic identities. When an agent calls an API, you can verify exactly which agent made the call, what trust domain it belongs to, and whether it is authorized. This kind of security work needs to happen before agents proliferate across production clusters. Retrofitting identity later is ugly.

**Dapr Agents** took a different angle with the actor model and durable execution. Each agent gets reliable state management and exactly-once messaging semantics. If your workflows cannot tolerate lost messages or duplicate actions, this matters.

**agentregistry** showed up as a centralized discovery service for MCP servers and agents. As agents and tool servers multiply, you need a registry to find and manage them, the same way container registries became necessary for images.

David Soria Parra from Anthropic gave a talk on MCP evolving beyond simple tool-calling into richer interaction patterns. Google announced the **Kubernetes Agent Sandbox** for running agentic AI workloads in secure, isolated environments.

Pulumi fits into this picture in two ways. The [Kubernetes Operator](/docs/iac/using-pulumi/continuous-delivery/pulumi-kubernetes-operator/) can manage the CRDs that kagent and kagenti introduce. And [Pulumi ESC](/docs/esc/) handles agent credentials, SPIFFE trust bundles, and the secrets that agents need to authenticate against external services.

## AI gateways and inference routing

Gateway infrastructure had its own mini-conference within KubeCon. The Gateway API Inference Extension from the Kubernetes SIG introduces model-aware routing and load balancing at the gateway level. Instead of routing by URL path, your gateway routes by model name, version, and capacity. That changes how inference traffic flows through a cluster in a fundamental way.

**Envoy AI Gateway** builds on Envoy's existing proxy capabilities with token-aware rate limiting and provider failover. If your primary inference provider is saturated, traffic shifts to a secondary automatically. Rate limiting by token count rather than request count makes much more sense for LLM workloads, where a single request can consume vastly different amounts of compute.

I want to call out **Agentgateway** specifically. Written in Rust, it proxies LLM traffic, MCP connections, and agent-to-agent communication, with Cedar and CEL policy engines for fine-grained access control. Rust's performance characteristics matter here because inference gateway latency adds directly to user-perceived response time.

**Kuadrant**, now in CNCF Sandbox, layers policy on top of gateway infrastructure and includes MCP server aggregation. Gateways are evolving from dumb traffic proxies into intelligent control planes for AI workloads, and these four projects are driving that shift.

For governance, [Pulumi CrossGuard](/docs/iac/using-pulumi/crossguard/) can enforce policy-as-code on gateway configurations. Rate limits, failover rules, and routing policies get validated against your organization's standards before they reach production.

## Platform engineering absorbs LLMOps

The observability and platform engineering vendors showed up in force. The message was consistent: LLMOps is not a separate discipline. It is platform engineering with new requirements.

**Chronosphere** demonstrated parallel AI investigation, with multiple agents analyzing different aspects of an incident simultaneously and combining their findings. **SUSE Liz** takes a domain-specialized approach, deploying different AI agents for different operational domains rather than one general-purpose assistant. **groundcover** combines eBPF with OpenTelemetry to give coding agents rich runtime context about the systems they are modifying. That last one is subtle but important: if an AI agent is writing code that touches a service, it should understand that service's actual runtime behavior, not just its source code.

**Dynatrace** and **DevCycle** partnered to make feature flags observable primitives via OpenFeature. Rolling out AI features behind feature flags is table stakes, but having those flags show up in your observability pipeline as first-class signals closes a real gap.

Shadow AI governance emerged as its own theme. **CAST AI's Kimchi** can route requests across 50+ models while providing centralized visibility into what models are being used, by whom, and at what cost. Every large organization I talked to had some version of the same problem: teams spinning up model endpoints without central oversight, burning through GPU budgets, creating compliance blind spots they did not even know about.

GPU multi-tenancy remains genuinely unsolved. Scheduling, workload isolation, cost attribution across shared GPUs — all of it breaks down at scale. Multiple talks addressed pieces of this, but nobody had a complete answer.

Pulumi addresses several of these concerns. [Self-service infrastructure](/docs/pulumi-cloud/developer-portals/) lets platform teams offer pre-approved AI infrastructure templates. The [Automation API](/docs/iac/using-pulumi/automation-api/) enables programmatic infrastructure provisioning that plugs into your existing developer portals. CrossGuard policies can enforce guardrails on AI infrastructure before resources are provisioned: GPU quotas, approved model lists, data residency requirements.

## Sovereignty shapes infrastructure architecture

The European context was impossible to ignore. The EU Cyber Resilience Act is driving compliance requirements deep into software supply chains, and every European organization I spoke with is feeling the pressure. This is not abstract regulation. It changes how you build, deploy, and operate software.

Sovereign Kubernetes is a platform architecture requirement now, not something you can defer to next quarter. Organizations need Kubernetes distributions and cloud regions that guarantee data residency, and they need the tooling to enforce those guarantees programmatically. Self-hosted models are proliferating partly because of capability and cost, but data sovereignty is the accelerant. If your data cannot leave a jurisdiction, neither can your model.

Runtime isolation is expanding beyond containers. Several talks covered KVM-based isolation for AI workloads, which is heavier than containers but necessary when the threat model includes side-channel attacks on shared GPU memory. The sandboxing conversation has gotten more sophisticated since last year.

These constraints are not uniquely European. Any organization operating across jurisdictions faces similar pressures, and the regulatory direction globally is toward more data sovereignty requirements, not fewer.

Pulumi's multi-cloud and multi-region deployment capabilities handle the infrastructure side of sovereignty. [Pulumi ESC](/docs/esc/) provides credential isolation across environments and regions. CrossGuard policies can enforce data residency at the infrastructure level, blocking deployments to non-compliant regions before they happen rather than catching them in an audit.

## What this means for your team

Four days in Amsterdam distilled into five things I would act on now:

1. **Treat inference workloads like production services.** If you are still deploying models with scripts and hope, stop. Inference infrastructure needs the same IaC discipline as any other production system: version-controlled, tested, policy-enforced.

1. **Evaluate the Gateway API Inference Extension and llm-d.** These are not speculative projects. They have broad industry backing and solve real problems around inference routing and distributed serving. Get them into your test environments.

1. **Plan agent identity before agents proliferate.** SPIFFE and SPIRE for agent identity is not optional if you are running agents in production. Retrofitting identity onto an existing agent fleet is painful. Start with kagenti now.

1. **Platform teams should own AI infrastructure.** Shadow AI is already happening in your organization. The platform engineering team needs to provide self-service AI infrastructure with guardrails before ungoverned model endpoints become a security and cost problem.

1. **Sovereignty and GPU multi-tenancy are universal.** Even if you are not subject to the EU Cyber Resilience Act today, data residency requirements are spreading globally. GPU multi-tenancy will affect every organization running inference at scale.

Kubernetes spent the past decade proving it could orchestrate containers. The next decade will test whether it can orchestrate intelligence. Based on what I saw in Amsterdam, the community is building the right pieces, but the gap between what exists and what production demands is still wide. That gap is where the interesting work happens.

If you want more context on how Pulumi fits into the cloud native ecosystem, check out my earlier post on [Pulumi in a cloud native world](/blog/pulumi-in-a-cloud-native-world/).

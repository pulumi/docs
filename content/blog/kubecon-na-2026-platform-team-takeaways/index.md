---
title: "KubeCon NA 2026 Recap: What Platform Teams Should Take Back About AI Agents"
allow_long_title: true
date: 2026-11-24T00:00:00-08:00
draft: false
meta_desc: "A recap of KubeCon NA 2026 for platform teams: agent sandboxes, agent identity, policy and approvals, and the cost of running AI on Kubernetes."
feature_image: feature.png
authors:
    - pulumi-content-team
tags:
    - kubernetes
    - kubecon
    - ai
    - platform-engineering
    - cloud-native
category: community
faq_schema: true
social:
    twitter: |
        KubeCon NA 2026 treated AI agents as a production workload class. Our recap for platform teams: agent sandboxes, agent identity, policy outside the prompt, and who pays for the GPUs.
    linkedin: |
        KubeCon + CloudNativeCon NA 2026 in Salt Lake City had a clear subject for platform teams: AI agents as a workload class that needs its own runtime, its own identity, and policy that lives outside the prompt.

        We read through the schedule, the Linux Foundation and Kubernetes announcements, and the vendor recaps, and wrote up four themes: sandboxing agents, identifying them, putting policy and approvals between an agent and production, and the cost and operations side of running AI on Kubernetes.

        We also flag where a claim comes from a session abstract or a vendor recap rather than a talk we watched.
    bluesky: |
        KubeCon NA 2026 treated AI agents as a production workload class on Kubernetes.

        Our recap for platform teams: sandboxes, agent identity, policy outside the prompt, and GPU and token costs.
---

KubeCon + CloudNativeCon North America 2026 in Salt Lake City (November 9-12) treated AI agents as a production workload class. For platform teams, four ideas stood out: agents need their own sandboxed runtime, their own identity, policy and approvals enforced outside the prompt, and cost tracking that covers GPUs and tokens.

<!--more-->

This recap is built from the published schedule, announcements from the Linux Foundation and the Kubernetes project, and write-ups from vendors who attended. Where a point comes from a session abstract or a vendor's own recap, we say so, because an abstract describes what a speaker planned to cover and a vendor recap reflects what that vendor sells. Our [attendee guide](/blog/pulumi-at-kubecon-na-2026/) covers where Pulumi showed up; this post covers what we took away. For comparison, here is what we saw in Amsterdam in the spring: [KubeCon EU 2026 recap](/blog/kubecon-eu-2026-recap/).

## Why did KubeCon treat AI agents as a new kind of Kubernetes workload?

Several sessions started from the same premise: agents behave differently from the services platform teams already run. The abstract for the Tim Hockin and Jonathan Berkovich session, "Kubernetes Solutions for Agent-Shaped Problems," says that "agents and agent-like workloads are becoming a predominant class of workloads on Kubernetes, but they are different from 'traditional' apps." It describes a lightweight control plane with active session management and network-triggered wake-ups, aimed at running far more agent-like workloads than before.

Other talks approached the same problem from the runtime side. Idit Levine's "The Harness Is the New Runtime" argued, in its abstract, that agent harnesses will become the dominant runtime for agents on Kubernetes. Jorge Palma's session described agentic AI as moving from experiments to production, with Kubernetes as a natural place to decide how those workloads run. A kagent talk by Eitan Yarmush defined the sandbox as the boundary for what an agent can see, touch, call, and persist: filesystem access, tool permissions, credentials, network policy, identity, and cleanup.

Vendors saw the same pattern. Edera's recap described agents as effectively production-ready workloads and reported that panel questions kept returning to isolation and to how much an agent is allowed to spend. Stacklok's recap put it this way: "Agents are becoming tenants of the internal platform. The teams that built golden paths for services will build them for agents too."

What to take back: treat an agent like a tenant. It gets a namespace or sandbox, a network policy, a scoped set of credentials, and a cleanup path, all defined as code so they can be reviewed and reproduced.

## Who is the agent in your cluster, and how do you prove it?

Identity was the thread that connected most of the security conversation. Abdel Sghiouar's keynote abstract describes an agent as a non-deterministic entity that generates dynamic network calls, triggers external APIs, and runs machine-generated code, then asks the question directly: when an autonomous agent invokes a local tool or accesses a cloud database, what identity does it present?

There was movement on the standards side. On November 10, the Linux Foundation [welcomed Agent Name Service (ANS)](https://www.linuxfoundation.org/press/linux-foundation-welcomes-agent-name-service-to-bring-verifiable-identity-and-discovery-to-ai-agents), an open standard for identity, verification, and discovery of AI agents that uses existing DNS infrastructure. A DigiCert executive quoted in the announcement framed the need as "knowing which agents are operating, controlling what they can do, and having the ability to revoke their access when trust changes."

Inside Kubernetes, the "Authorized? It Depends." session covered conditional authorization. Per its abstract, authorizers used to answer only Allow, Deny, or NoOpinion, and now they can say "Allow if..." or "Deny if...", which makes decisions that depend on context possible. Stacklok's recap summarized the vendor view: governance is the biggest thing holding enterprises back from deploying agents, and governance starts with identity.

What to take back: give every agent its own identity instead of a shared service account, and make sure you can revoke it without touching anything else.

## Where do policy and human approvals sit between an agent and production?

The sharpest framing came from a session by Goel and Bugwadia on Envoy AI Gateway and Kyverno. Its abstract states that "standard Kubernetes RBAC cannot govern non-deterministic actions driven by unvalidated prompts," and proposes intercepting the intents a model extracts and applying declarative YAML policies to allow or block them in real time. Jessica Forrester's keynote abstract made the stakes concrete: an agent with too much access, through choice or a lack of knowledge, can take down entire production stacks and wipe databases.

Stacklok's recap noted that talks such as "The Agent Did What? Reconstructing MCP Tool-Call Attacks" treated prompt injection through tool calls as a real incident class, with forensics. The practical consequence is that a rule written in a system prompt cannot be your only control. Controls need to sit in the gateway, the admission layer, or the credentials the agent holds.

Human approval is the other half. In the same week, Pulumi announced Pulumi Agents (details in [our launch post](/blog/everything-after-code-as-code/)), and we will use its documented behavior as one example, with the obvious disclosure that it is our product. Neo, the built-in agent, has three approval modes: Manual, Balanced, and Auto. Balanced approves routine requests automatically and waits for sensitive actions such as `pulumi up` and destructive changes. The [permissions documentation](/docs/ai/agents/permissions/) is explicit about a limit that applies to any agent tool: an approval does not grant additional access, and read-only mode does not restrict the credentials used by connected tools. Approvals decide when a human is asked. The credentials still have to enforce what the agent can actually do.

What to take back: layer the controls. Scope credentials tightly, enforce policy where the request lands, and require human approval for changes that can destroy data or spend money.

## What did the cost and operations talks say about running AI on Kubernetes?

The operations side was less about agents and more about the infrastructure under them. In the AWS keynote session, Mike Stefaniak described what AI changed for Kubernetes: container images in the tens of gigabytes, clusters approaching 100,000 nodes, and accelerators that a simple device count cannot describe. The abstract highlights Dynamic Resource Allocation, which lets a pod ask for a GPU and a network adapter on the same PCIe root, and notes that Karpenter can now provision for it.

Cost showed up as its own topic. The KServe session "Who Ran Up the Inference Bill? AI Traffic Control with KServe and Gateway API Inference Extensions" is a good example of the question platform teams are now asked. The TAG Operational Resilience abstract, from Alolita Sharma, widens "reliability" to cover everything from microservice cascades to GenAI token costs and energy efficiency. A Meta session described a different kind of scale: about 15 engineers running about 100 Kubernetes clusters for AI research and inference, after moving from Terraform on cron to GitOps.

Heading into the event, the Kubernetes project reported that [AI Conformance grew from 18 to 31 certified platforms](https://kubernetes.io/blog/2026/10/29/sig-arch-ai-conformance-2026/) within a few months, and that it now tests DRA accelerator support. A separate [Workload Conformance working group](https://kubernetes.io/blog/2026/10/27/announcing-workload-conformance-wg/) is at an early stage. It points out that Certified Kubernetes tests the cluster and AI Conformance tests whether a cluster can run AI and ML workloads, while nothing comparable exists yet for the workloads themselves.

For teams that manage this layer as code, the [Pulumi Kubernetes provider](/registry/packages/kubernetes/) covers clusters, namespaces, quotas, and the custom resources that configure things like Karpenter, so GPU pools and per-team limits are reviewed like any other change.

What to take back: attribute GPU and token spend per team or per agent from day one, because the question of who ran up the bill arrives sooner than expected.

## What should platform teams do before the next KubeCon?

A short list is enough to start. Inventory the agents already running in your organization, including the ones individual developers started. Give each one a distinct identity and the narrowest credentials that work. Move policy out of prompts and into the gateway, admission, and credential layers. Decide which actions need a human approval. Tag compute and token usage so costs trace back to an owner. All of this is easier when the definitions live in code under review, which is the same discipline platform teams already apply to the rest of their infrastructure.

## Frequently asked questions

### When and where was KubeCon + CloudNativeCon North America 2026?

It took place November 9-12, 2026, in Salt Lake City, Utah.

### Are KubeCon NA 2026 talks recorded?

KubeCon sessions are typically published afterward on the [CNCF YouTube channel](https://www.youtube.com/c/cloudnativefdn). Check the [schedule](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/program/schedule/) for individual session pages and slides.

### What is Kubernetes AI Conformance?

It is a Kubernetes project program that certifies whether a platform can run AI and ML workloads. According to the project's October 2026 update, it grew from 18 to 31 certified platforms and now covers DRA-based accelerator support.

### Is an approval prompt enough to make an AI agent safe?

No. An approval controls when a human is asked, and the agent's credentials still determine what it can do. Pair approvals with scoped credentials and policy enforced outside the prompt. Neo, the agent in Pulumi Agents, follows this model, and its [permissions documentation](/docs/ai/agents/permissions/) describes how approval modes and access relate.

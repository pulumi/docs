---
title: "The Superintelligence Flywheel: Infrastructure for the AI Era"
date: 2025-12-11T00:00:00-00:00
draft: false
meta_desc: Discover why the rise of superintelligence requires intelligent, automated infrastructure and how Pulumi and Neo power the next generation of AI platforms.
meta_image: meta.png
authors:
    - joe-duffy
tags:
    - superintelligence
    - neo
    - iac
---

We've been in the infrastructure business for nearly a decade, and we've never been more excited about, or in awe of, the scale we are seeing as the industry pursues superintelligence. We are now hitting a tipping point that requires entirely different approaches to managing and scaling infrastructure in this new era.

What do we mean by superintelligence? Superintelligence means AI systems that operate with genuine autonomy---planning, reasoning, executing, adapting---at scale, on the path toward human-level and eventually superhuman intelligence. The infrastructure needed to accomplish this is greater than anything we've ever seen. Jensen Huang projects $600 billion in AI infrastructure spending this year, scaling to $3-4 trillion by decade's end. Stargate committed $500 billion to AI infrastructure in the U.S. Microsoft, Meta, and Google are each spending $70-90 billion annually on datacenters. AWS just activated Project Rainier, a data center scaling to one million custom Trainium chips for Anthropic's frontier models.

Superintelligence is driving the biggest, fastest infrastructure scaling period in the history of computing. This is exciting but comes with challenges: all of that infrastructure has to be managed, secured, scaled, made compliant, and cost effective. Legacy infrastructure tools weren't built for this reality---they add friction that slows progress or breaks it altogether.

This reveals an important insight:

<div style="text-align: center; font-size: 1.5em; font-style: italic; margin: 2em 0;">
The infrastructure required to build superintelligence demands superintelligence for infrastructure.
</div>

<!--more-->

The systems being built today for superintelligence are already straining human platform teams to their limits and yet we're still only just getting started. To succeed, we will have no choice but to use AI itself to help us manage the infrastructure scaling ahead on the path to superintelligence.

Superintelligence demands more infrastructure, which demands superintelligent approaches to managing and scaling that infrastructure, which leads to faster progress towards superintelligence.

We call this the *superintelligence flywheel*.

---

## The Flywheel Defined

The superintelligence flywheel describes a self-reinforcing cycle between two forces:

**Superintelligence Infrastructure**: The massively distributed compute, storage, networking, and orchestration systems required to train and serve frontier AI models.

**Infrastructure Superintelligence**: AI systems capable of managing infrastructure with increasing autonomy. These systems handle the full spectrum of infrastructure automation, from provisioning to securing to evolving and scaling entire environments.

These reinforce one another. As AI infrastructure grows more complex, human teams will increasingly use AI to manage it. This affects all of us: frontier labs, technology innovators, and enterprises modernizing their products and workforces with an AI-first mindset. Infrastructure agents are simply a requirement for all of us in this new world.

The flywheel accelerates.

![The Superintelligence Flywheel](flywheel.svg)

---

## The Technical Reality

Frontier labs have the most extreme requirements, but everybody else is somewhere on the curve. You don't have to be training GPT-5 to feel this pressure. If you're deploying fine-tuned models, running inference at scale, or just trying to keep up with AI-assisted developers shipping faster---you're on the same curve, just earlier. To stay competitive and innovative in this new era, access to infrastructure needs to be democratized and inherently automation- and experimentation-friendly.

This can be seen most vividly with frontier lab-scale infrastructure challenges:

**Training** starts with data preparation. Petabytes of data turns into trillions of curated tokens across thousands of CPU cores. Pre-training runs massive GPU clusters hot for months, at a scale where hardware failures are statistical certainties. Checkpoint management, gradient synchronization, and fault-tolerant scheduling become first-order concerns. Fine-tuning and reinforcement learning add even more coordination complexity: synthetic data generation, AI judges, multiple model copies running simultaneously in tightly coupled loops, hundreds of experiment variants, infrastructure that scales elastically as experiments converge or diverge.

**Inference** means serving models to an ever-elastic sea of users across massive GPU fleets, many clouds, and distributed globally. ChatGPT, for instance, handles over 2.5 billion queries per day with sub-second time-to-first-token expectations. Traffic patterns shift by geography, time, and viral adoption, and the software must be ready to react. The difference between good and poor GPU utilization at this scale can make or break the user experience and the bank.

These examples share three properties that break traditional infrastructure approaches:

1. **Massive scale**: Thousands or millions of coordinated resources with complex architectures across multiple regions and cloud providers.  

2. **Extreme dynamism**: Infrastructure that must spin up, reallocate, and tear down continuously based on job requirements, spot pricing, capacity availability, and failures.

3. **Velocity beyond human capacity**: Infrastructure changes that occur faster than human operators can review, approve, and execute manually, often initiated by AI agents.

Of course, even smaller scale examples share these challenges. Whether you're using AWS SageMaker or Google Vertex AI to fine-tune models for your enterprise, building out your data engineering function to train custom models, or moving your first ML workloads to production---these infrastructure demands become relevant as you scale.

AI-assisted software development tools are making engineers dramatically more productive. Developers are shipping more code than ever before. But unlike software engineering, legacy infrastructure practices lack inherent guardrails to enable AI-assisted infrastructure engineering: linters, static analysis, testing frameworks, canaries, staged rollouts. The tooling that worked when humans were the limiting factor won't work when AI agents are generating and deploying infrastructure code at machine speed.

### Infrastructure Fungibility: The Holy Grail

Instead of treating each use case as a special snowflake, the holy grail is infrastructure fungibility across many clouds. In this world, infrastructure is dynamically allocated based on availability, demand, and data locality. Inference gets served based on current user demand. Experiments get capacity when it's available. Long-horizon training runs on whatever's left over.

This is extraordinarily difficult. But without it, the costs compound: researchers waiting for capacity, GPU-hours sitting idle between workloads, time delays that let competitors ship first. At frontier scale, even small inefficiencies translate to tens of millions of dollars.

This level of dynamism can't be managed by humans watching dashboards and approving PRs. The infrastructure itself needs to become intelligent---capable of planning, executing, and adapting without waiting for human operators.

The frontier labs building this have learned through direct experience. They have historically had to work around legacy infrastructure tools and slow-moving DevOps teams, taking matters into their own hands. As one infrastructure lead put it: "There are thirty people in the world that know how to do this right now." It is time for this knowledge to spread faster, in the hands of platform teams, because everyone building with AI is running into some version of the same problem.

---

## Towards a Superintelligence Platform

There are two foundations that form a cohesive superintelligence platform:

### Foundation \#1: Pulumi as the Infrastructure Automation Substrate

We built Pulumi on three principles that are well-suited to the unique challenges of this era:

**Infrastructure as code must be actual code.** Domain-specific languages and static configuration formats create a ceiling. Instead, standing on the shoulders of giants with real programming languages provides type systems, conditionals, loops, abstractions, package management, testing frameworks, and more. These capabilities facilitate *scale*. Just as importantly, your team already knows Python, TypeScript, and Go---why force them to learn yet another proprietary DSL and context-switch constantly between application code and infrastructure configuration?

But there's a deeper reason this matters now. LLMs have been trained on billions of lines of Python, TypeScript, and Go, and deeply understand how to code correctly. Infrastructure in real programming languages becomes infrastructure that AI systems can reason about, generate correctly, and modify safely. We call this an "LLM-sympathetic architecture": by projecting cloud infrastructure into code space, LLMs can manipulate infrastructure through coding, something they are already superb at which ensures it can be done repeatably and correctly.

**One substrate across all of the clouds.** Every cloud, every SaaS provider. Frontier labs run training jobs wherever capacity exists: AWS, Azure, Google Cloud, Oracle Cloud, CoreWeave, Lambda Labs. GPU availability is the constraint; cloud provider preference is now secondary.

A single lab may prefer to train on GCP, overflow to AWS when spot capacity becomes available, and tap CoreWeave when the reservations in the major cloud providers are used up. Inference deployments span every region where users exist, across whichever providers offer the best latency and cost characteristics.

Infrastructure platforms that aren’t inherently multi-cloud simply can't serve these requirements, forcing teams to adopt many fragmented tools and workflows. A platform for the superintelligence era simply must treat multi-cloud as a given with unified resource management, policy enforcement, and state tracking across all providers.

**Agent-ready architecture.** Human-in-the-loop infrastructure management doesn't scale to the velocity of the new era. The path forward is progressive autonomy: AI agents that operate infrastructure with increasing independence, bounded by human-defined policies and guardrails.

This requires platforms designed for agent interaction from the ground up, with APIs agents can invoke, state they can reason about, policies that define boundaries, audit trails that maintain accountability. The infrastructure platform becomes the substrate on which agents operate. Infrastructure as code, it turns out, is already very good at this thanks to its declarative core.

### Foundation \#2: Neo as the Agentic Layer

If managing superintelligence scale infrastructure requires AI agents that can handle infrastructure automation, the critical question is: what should those agents look like?

Neo is our answer. Neo is an AI agent that operates infrastructure like a senior platform engineer, built on top of Pulumi's foundation. Because Pulumi already provides the guardrails that software engineering takes for granted---previews, policy enforcement, state tracking---Neo can handle infrastructure tasks automatically while validating changes before they hit production.

**Uniquely enabled by infrastructure as code**. Neo operates on infrastructure code, not opaque configurations or cloud APIs directly. Even for resources not yet managed by Pulumi, Neo seamlessly imports them under code management before making changes. Every action flows through version control, policy checks, and state tracking. This ensures the underlying LLM’s coding smarts apply to infrastructure changes.

**Built for progressive autonomy**. Organizations configure Neo's independence by environment and task type. Dev environments might permit fully autonomous operation---daily waste cleanup, weekly drift reconciliation---while production changes may require human approval. When Neo encounters unexpected state or errors, it can self-diagnose or loop in a human for assistance as needed. As confidence builds, the autonomy boundary expands, towards full autonomy.

**Inherently understands and respects guardrails.** The same velocity that creates opportunity creates risk. An agent that can provision 1,000 resources can also misconfigure 1,000 resources. Pulumi's infrastructure as code foundation provides the safety mechanisms software engineering takes for granted: previews before deployment, policy as code enforcement, audit trails, human-in-the-loop approvals, and organizational best practices encoded in components. Just as you wouldn't ship code without version control, you shouldn't let AI manage infrastructure without these guardrails.

**Agentically automate anything**: Give Neo a prompt like "Provision a PyTorch training environment for LoRA fine-tuning on GKE with 50 A100s using Nvidia's GPU Operator and Kueue---then run a smoke test." Neo generates the project, previews changes, provisions everything, verifies it works. Days become minutes. It's not just for new infrastructure: one customer used Neo to tackle 300,000+ policy violations---work they estimated would take years is now done in weeks.

**Frontier models plus infrastructure smarts**: Neo builds on a mixture of frontier models while incorporating nearly a decade of infrastructure expertise. Neo benefits from Pulumi’s nearly one billion deployments, hundreds of thousands of AI interactions and known-to-be-working code examples, and many petabytes of semantically-understood, anonymized infrastructure metadata. This foundation is something that no other company in the world has at their disposal.

### Pulumi \+ Neo: The Superintelligence Platform

Pulumi without Neo is already a powerful infrastructure platform---but one that still requires human operators for every change. Neo without Pulumi would never be production-ready, as it would lack the cloud-to-code projection and guardrails that make Neo so good. Together, humans define intent and policy, and intelligent agents handle execution with autonomy.

This is the foundation for setting the superintelligence flywheel in motion.

---

## Evidence at Scale

The flywheel isn’t theoretical. We're facilitating it daily with thousands of customers:

**Hyper-scale**: Wiz manages over one million cloud resources across tens of thousands of Kubernetes clusters in hundreds of data centers across every cloud provider imaginable. They do hundreds of thousands of updates daily across thousands of Kubernetes clusters, leading to 5x faster customer onboarding and entering new markets in days rather than months. They treat infrastructure provisioning as just another service in their distributed system.

**Infrastructure democratization**: Supabase achieved the infrastructure velocity needed to keep up with the AI era’s demand for their own product, empowering 20x more teammates to scale infrastructure in TypeScript, the same language as their application code, rather than proprietary DSLs that nobody understood. New regions deploy in about a week, with 43,000 new databases daily and 100,000+ API calls per second. According to their platform team, now thanks to Pulumi, "the infrastructure team acts as groundkeepers, not gatekeepers."

**Frontier science**: We manage infrastructure for organizations including NVIDIA and multiple frontier labs building the models that will define the next decade. The scale requirements for these workloads exceed any we've ever seen and are only getting bigger. Just as many customers democratize infrastructure for their developers, we're seeing frontier labs use Pulumi to accelerate getting science into production with self-service infrastructure for AI researchers.

---

## The Superintelligence Flywheel is in Motion

AI is driving the largest infrastructure buildout in history—whether you're training frontier models or deploying your first ML workloads to production. That complexity demands intelligent agents. Organizations that embrace this—building infrastructure for AI while using AI for infrastructure—will define the next era of computing.

The superintelligence flywheel is spinning fast and it’s only going to get faster from here.

---

*Pulumi provides the infrastructure platform for the superintelligence era: infrastructure as code in general-purpose languages, unified multi-cloud management, and Neo for progressive infrastructure autonomy.*

[*Pulumi Neo*](/product/neo) *・ [Case Studies](/case-studies) ・ [Contact](/contact)*

---
title: "Best Internal Developer Platform (IDP) Tools in 2026"
date: 2026-09-04
draft: false
meta_desc: "Compare 9 internal developer platform tools for 2026 across the portal, orchestration, and infrastructure layers: Backstage, Port, Crossplane, Pulumi, and more"
feature_image: feature.png
authors:
    - pulumi-content-team
tags:
    - platform-engineering
    - infrastructure-as-code
    - devops
    - kubernetes
category: general
itemlist_name: "Internal Developer Platform Tools"
itemlist:
    - name: "Backstage"
    - name: "Roadie / Spotify Portal for Backstage"
    - name: "Port"
    - name: "Cortex"
    - name: "OpsLevel"
    - name: "Humanitec"
    - name: "Kratix"
    - name: "Crossplane"
    - name: "Pulumi"
      url: "https://www.pulumi.com/"

social:
    twitter: |
        Most "best IDP tools" lists compare a portal to an orchestrator to a control plane as if they compete. They don't. Here's how to evaluate 9 platform engineering tools by the layer they actually occupy.
    linkedin: |
        Internal developer platform tools get compared as if they're one category. They aren't.

        A software catalog like Backstage or Port, an orchestrator like Humanitec or Kratix, and a control plane like Crossplane or Pulumi solve different problems, and most platform teams end up running one from each layer rather than picking a single winner.

        We compared 9 tools across those three layers on licensing, provisioning behavior, policy support, and honest limitations, sourced and cited throughout. No single "winner," because the market doesn't have one.
    bluesky: |
        Backstage, Port, Cortex, Humanitec, Kratix, Crossplane, Pulumi: most "best IDP tools" roundups compare them as if they're one category. They sit at three different layers of the stack. Here's how to evaluate each one honestly.
---

Ask five platform engineers to name the best internal developer platform tool and you will get five different answers, because they are often not answering the same question. Backstage catalogs services. Humanitec orchestrates deployment configuration. Crossplane provisions cloud resources. These tools get compared in the same breath and ranked on the same list, but they solve different problems at different layers of the platform stack.

This guide sorts nine widely used IDP tools into the layer they actually occupy: the portal and catalog layer, the orchestration layer, and the infrastructure layer. Most platform teams end up combining one tool from each rather than picking a single winner, so this comparison evaluates each tool honestly within its own layer, including where Pulumi fits and where it does not.

## What is an internal developer platform?

An internal developer platform (IDP) is the set of tools and workflows a platform team builds so application developers can self-serve infrastructure, environments, and deployments without filing a ticket. A mature IDP combines a catalog of what exists, golden paths for how to provision it, and guardrails that keep self-service safe. No single tool in this guide covers all three on its own; that gap is exactly why the tooling landscape splits into layers. For the full architecture, components, and build-versus-buy tradeoffs, see [what is an internal developer platform](/what-is/what-is-an-internal-developer-platform/).

## How should you evaluate IDP tools?

### How much self-service does the tool actually deliver?

A catalog that only displays information is not self-service; a tool is self-service when a developer can request and receive a working resource without a platform engineer in the loop. Test this directly: ask whether a new service, database, or environment can go from request to running infrastructure inside the tool itself, or whether the tool just links out to a ticket, a Slack thread, or a manual pull request review.

### Can it enforce golden paths, or does it only document them?

A golden path is a paved, approved way to build something, and the difference between documenting one and enforcing one is the difference between a wiki page and a working platform. Look for scaffolding or templating that generates real, running infrastructure from an approved pattern instead of a README describing one. Pulumi's [organization templates](/docs/idp/concepts/organization-templates/) are one example of enforcement rather than documentation: they scaffold real projects from platform-team-authored code.

### Where do policy and guardrails live?

Every IDP eventually needs to answer who can provision what, in which environment, under which constraints, and that answer has to live somewhere enforceable, not in a review checklist. Some tools bundle policy as a first-class feature; others expect you to bring policy as code from elsewhere in the stack, such as [Pulumi Policies](/docs/insights/policy/). Ask where guardrails are actually evaluated: at request time, at provisioning time, or only after the fact in an audit.

### Does it work across clouds, or only on Kubernetes?

Several tools in this category, including Crossplane and Kratix, are built on Kubernetes control planes and assume workloads and infrastructure both run through Kubernetes. That is a strength for Kubernetes-native organizations and a real constraint for teams provisioning serverless, managed databases, or non-Kubernetes compute across multiple clouds. Confirm whether a tool's provisioning model is Kubernetes-native, cloud-API-native, or IaC-agnostic before standardizing on it.

### How extensible is it?

Every platform outgrows its starting set of golden paths, so extensibility determines whether a team can keep building on the tool or has to route around it within a year. Reusable, composable building blocks, such as [components](/docs/iac/concepts/components/) in Pulumi or Promises in Kratix, let a platform team add new capabilities without forking the tool itself. A rigid tool with a fixed set of supported patterns will need workarounds sooner than a composable one.

## The best internal developer platform tools in 2026

### Portal and catalog layer

Portal and catalog tools answer "what exists and who owns it." None of the five tools below provision infrastructure themselves; they organize, surface, and add self-service actions on top of infrastructure that other tools create.

#### 1. Backstage

Backstage is the open-source developer portal framework originally built at Spotify, licensed under Apache 2.0 and fully self-hostable. It has been a CNCF Incubating project since March 2022 and remains the most widely adopted framework in this category, with over 3,000 documented adopters as of late 2024, including CVS Health, Siemens, and LinkedIn. Its plugin ecosystem and customizable software catalog are the biggest draw, and it does not provision infrastructure on its own: teams commonly wire its Scaffolder templates to Terraform, Crossplane, or Pulumi to actually create resources, including through [Pulumi's official Backstage plugin](/docs/idp/integrations/backstage-plugin/). The honest tradeoff is operational cost. Running Backstage well typically requires a dedicated platform team, and its flexibility can produce unnecessary complexity for teams that need to move fast rather than customize deeply.

#### 2. Roadie and Spotify Portal for Backstage

Roadie and Spotify Portal are commercial, fully managed distributions of Backstage, built to remove the self-hosting burden that makes the open-source framework expensive to run well. Both are SaaS products layered on the same Apache 2.0 core, so migrating between them and a self-hosted instance is more straightforward than switching to a differently architected portal. The tradeoff for that convenience is cost and reduced control: neither publishes fully transparent enterprise pricing, and adopting a managed distribution trades infrastructure ownership for a subscription. Teams already committed to Backstage's plugin ecosystem but unwilling to staff a dedicated platform team are the clearest fit.

#### 3. Port

Port is a commercial, closed-source developer portal that combines a software catalog with self-service actions, positioning itself as a faster-to-adopt alternative to self-hosted Backstage. It does not provision infrastructure directly; its self-service actions and Terraform provider trigger existing IaC pipelines or webhooks rather than creating resources natively. Port raised a $100 million Series C at an $800 million valuation, giving it substantial resources to invest in the product, and its published pricing starts at $30 per developer seat per month before moving to custom enterprise pricing. The tradeoff mirrors any closed-source SaaS portal: faster time to value than building on Backstage, at the cost of vendor lock-in on the catalog layer itself.

#### 4. Cortex

Cortex is a commercial, closed-source engineering operations platform built around scorecards that measure service quality, security posture, and production readiness rather than around a general-purpose catalog. Gartner named it a representative vendor in its 2025 Market Guide for Internal Developer Portals, and its resource catalog extends beyond services to infrastructure components like databases and message queues. Like Port, it does not provision infrastructure; it catalogs and scores what already exists. Pricing is not public, and independent, non-vendor commentary on its limitations is thin in the available record, so teams evaluating it should weigh vendor claims against a direct trial rather than third-party reviews alone.

#### 5. OpsLevel

OpsLevel is a commercial, closed-source service catalog focused on Checks and Scorecards that measure engineering maturity against a team's own standards. It includes ownership discovery that suggests likely service owners from recent commit activity, though that suggestion is not automatic reassignment. OpsLevel does not provision infrastructure and does not publish self-serve pricing; third-party estimates put typical implementation costs in the $10,000 to $50,000 range depending on catalog size. It competes most directly with Cortex on the scorecard-driven governance angle rather than with Backstage or Port on catalog breadth.

### Orchestration layer

Orchestration tools sit between the catalog and the infrastructure. They take a developer's request, apply organizational rules and configuration, and hand off the actual provisioning work to an IaC tool underneath.

#### 6. Humanitec

Humanitec's Platform Orchestrator standardizes application configuration and infrastructure provisioning behind a declarative Workload Specification called Score, which Humanitec co-created as a CNCF Sandbox project. The Orchestrator itself is commercial and closed-source, while Score and Humanitec's driver library for integrating existing IaC tools are open source. It explicitly positions itself to sit behind a portal like Backstage, Port, or Cortex rather than compete with one, and it delegates actual resource creation to Terraform, Crossplane, or Pulumi through its driver framework rather than provisioning from scratch. The tradeoff is buying into a proprietary control plane even though the interface spec is open, a standard commercial-orchestrator lock-in that teams should weigh against building the same standardization themselves.

#### 7. Kratix

Kratix is an open-source, Apache 2.0-licensed, Kubernetes-native framework for building custom platform APIs called Promises, maintained by Syntasso, which is a CNCF member company though Kratix itself is not a CNCF-hosted project. Promises can wrap arbitrary tooling, including Terraform modules, so a platform team defines the self-service API once and Kratix handles the workflow that fulfills it. Syntasso sells commercial enterprise and agentic tiers on top of the free core for teams that want support and additional integrations. Kratix is closer to a toolkit than a turnkey product: teams get more flexibility and lower lock-in than a packaged commercial orchestrator, at the cost of having to build more of the platform themselves.

### Infrastructure layer

Infrastructure and control-plane tools are where resources actually get created. Everything above this layer eventually calls down into a tool like these two, whether directly or through an orchestrator.

#### 8. Crossplane

Crossplane is an open-source, Apache 2.0-licensed Kubernetes control-plane framework that graduated within the CNCF on October 28, 2025, its highest maturity tier. Platform teams define custom Kubernetes CRDs, called Composite Resources, that represent opinionated infrastructure abstractions backed by real cloud resources, and Crossplane's own controllers provision those resources directly against cloud provider APIs rather than shelling out to Terraform. That native provisioning model is also its steepest learning curve: designing Composite Resources well takes real investment, and the project has publicly acknowledged control-plane performance challenges as the number of installed provider CRDs grows, addressed partly through provider families. Crossplane requires a Kubernetes cluster to run even for teams not deploying Kubernetes workloads, which is real operational overhead for non-Kubernetes-centric organizations.

#### 9. Pulumi

Pulumi is not a developer portal. Its IDP capabilities are an infrastructure and code-first platform layer: reusable [components](/docs/iac/concepts/components/) written in general-purpose languages, [organization templates](/docs/idp/concepts/organization-templates/) that scaffold golden-path projects, a [private registry](/docs/idp/concepts/private-registry/) where platform teams publish those building blocks, [Pulumi Policies](/docs/insights/policy/) for policy as code, and [Pulumi ESC](/docs/esc/) for secrets and configuration, all reachable through the CLI, the Pulumi Cloud console, and CI/CD. Where Pulumi does offer a portal-like surface, it is intentionally thin: a New Project Wizard and no-code stacks inside the console, plus a one-click "Deploy with Pulumi" button. That is a deliberately thin surface, not a full catalog UI. For teams that already run a portal, Pulumi ships an [official Backstage plugin](/docs/idp/integrations/backstage-plugin/) so Backstage calls into Pulumi rather than the two competing. A team evaluating IDP tools often ends up pairing Pulumi at the infrastructure layer with a catalog like Backstage, Port, or Cortex at the portal layer, rather than choosing one instead of the other.

## Comparison at a glance

| Tool | Layer | License / hosting | Provisions infrastructure? | Policy & guardrails |
|---|---|---|---|---|
| Backstage | Portal | Apache 2.0, self-hosted | No, delegates via plugins | Bring your own |
| Roadie / Spotify Portal | Portal | Commercial SaaS (Backstage-based) | No, delegates via plugins | Bring your own |
| Port | Portal | Commercial, closed-source SaaS | No, delegates via Terraform provider or webhooks | Self-service action approvals |
| Cortex | Portal | Commercial, closed-source SaaS | No, catalogs and scores | Scorecards, not enforcement |
| OpsLevel | Portal | Commercial, closed-source SaaS | No, catalogs and scores | Checks and Scorecards |
| Humanitec | Orchestration | Commercial core, open Score spec | No, delegates via driver framework | Central to the Workload Spec |
| Kratix | Orchestration | Apache 2.0, open-core | No, delegates via Promises | Defined per Promise |
| Crossplane | Infrastructure | Apache 2.0, self-hosted | Yes, via native controllers | Kubernetes RBAC, bring your own policy engine |
| Pulumi | Infrastructure | Commercial, plus open-source SDKs | Yes, via native providers | Pulumi Policies (policy as code) |

## How do you choose?

Start by identifying the gap you actually have rather than shopping for a single tool. A team with scattered service ownership and no catalog needs a portal first, whether that is self-hosted Backstage, a managed Backstage distribution, or a commercial catalog like Port, Cortex, or OpsLevel. A team with a catalog but inconsistent, manually reviewed provisioning needs an orchestration layer like Humanitec or Kratix to standardize the workflow. A team whose infrastructure code itself is fragmented, hard to reuse, or ungoverned needs to fix the infrastructure layer first, since a polished portal in front of inconsistent infrastructure just makes the inconsistency easier to request. That is where a code-first platform like [Pulumi](/product/) fits: teams that need real, reusable infrastructure building blocks, golden-path templates, and policy enforcement, whether standalone or as the layer beneath an existing portal.

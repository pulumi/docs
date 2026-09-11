---
title: "Best Platform Engineering Tools in 2026"
date: 2026-09-11
draft: false
meta_desc: "Compare 10 platform engineering tools for 2026 on one question: how much of your golden path do you build yourself, and how much do you buy?"
feature_image: feature.png
authors:
    - pulumi-content-team
tags:
    - platform-engineering
    - infrastructure-as-code
    - devops
    - kubernetes
category: general
itemlist_name: "Platform Engineering Tools"
itemlist:
    - name: "Backstage"
    - name: "Crossplane"
    - name: "Kratix"
    - name: "Argo CD"
    - name: "Score"
    - name: "Port"
    - name: "Cortex"
    - name: "Humanitec"
    - name: "Terraform and OpenTofu"
    - name: "Pulumi"
      url: "https://www.pulumi.com/"

social:
    twitter: |
        Every platform engineering tool decision comes down to one question: how much of your golden path do you build, and how much do you buy? We compared 10 tools across that spectrum, sourced and cited.
    linkedin: |
        Platform engineering roundups tend to list tools by category and stop there. The decision that actually matters is upstream of category: how much of your golden path are you willing to assemble yourself, versus buying one that ships pre-built?

        We compared 10 widely used tools, from Backstage and Crossplane on the build end to Port and Humanitec on the buy end, plus the IaC layer both approaches sit on top of. Every claim is sourced, every limitation is one we could defend to the vendor's face.
    bluesky: |
        Backstage, Crossplane, Kratix, Argo CD, Score, Port, Cortex, Humanitec, Terraform, Pulumi: 10 platform engineering tools, one real axis of comparison. How much golden path do you build versus buy?
---

By 2026, 80% of large software engineering organizations will have established platform engineering teams as internal providers of reusable services, up from 45% in 2022, according to [Gartner](https://www.gartner.com/en/infrastructure-and-it-operations-leaders/topics/platform-engineering). DORA's 2025 research puts internal developer platform adoption at 90% of organizations, with 76% now running a dedicated platform team. The practice has moved from experiment to default. What has not settled is the tooling, because every platform engineering tool decision is really one decision wearing different clothes: how much of your golden path do you build yourself, and how much do you buy pre-assembled.

## What is platform engineering?

Platform engineering is the discipline of designing and building the internal developer platform, tooling, and self-service workflows that let application teams ship software without navigating raw infrastructure, security, and operational complexity themselves. A platform team treats the platform as an internal product, with developers as its customers, and measures success by developer self-service adoption rather than ticket volume. Read [our guide to platform engineering](/blog/the-guide-platform-engineering-idp-steps-best-practices/) for the steps and practices behind standing one up.

## The build-versus-buy question comes first

Every tool in this list sits somewhere on a spectrum between two postures. On one end, a team assembles its own golden path from open, composable pieces: a catalog, a control plane, a delivery engine, an infrastructure layer, wired together and owned in-house. On the other end, a team buys a platform orchestrator or portal that ships an opinionated golden path out of the box, trading assembly effort for vendor lock-in and a subscription line item. Neither posture is wrong. The mistake is picking a tool before deciding which posture your team can actually sustain. Four questions cut through most of the noise.

### How much of the golden path does the tool build for you?

A framework like Backstage or Crossplane gives you the primitives to assemble a golden path and expects you to do the assembly. A product like Port, Cortex, or Humanitec ships an opinionated golden path already wired together, at the cost of a subscription and less flexibility to deviate from its model. Deciding which side you want is the first filter, before comparing feature lists.

### What does developer self-service actually look like?

Self-service ranges from a scaffolder template that stamps out a new service, to a full self-service API that provisions infrastructure on request, to a scorecard that nudges teams toward standards without enforcing them. The right depth depends on how much autonomy your organization is comfortable delegating and how much guardrail engineering you are prepared to build around that autonomy.

### How does the tool integrate with your infrastructure as code?

Some tools are the infrastructure-as-code layer itself. Others sit above it, orchestrating or cataloging resources that Terraform, OpenTofu, or Pulumi actually provision. Knowing which layer a tool occupies prevents the common mistake of comparing a catalog to a provisioning engine as if they compete.

### Where do observability hooks attach?

A platform that stops at provisioning and deployment leaves teams to bolt on monitoring separately. The stronger platforms in this list expose Prometheus, Grafana, or equivalent hooks natively, or integrate cleanly with an existing observability stack rather than requiring a parallel one.

## The best platform engineering tools in 2026

### Tools for assembling your own golden path

#### 1. Backstage

[Backstage](https://backstage.io/) is the CNCF's open-source framework for building a developer portal: a software catalog plus scaffolder templates for stamping out new services on a golden path. It moved from CNCF Sandbox to Incubating status in March 2022 and remains the de facto standard for platform teams building their own portal, backed by the largest plugin ecosystem in the category and Apache 2.0 licensing with no vendor lock-in. The tradeoff is operational: Backstage has no paid tier of its own, so the cost shows up as engineering time to stand it up, maintain plugins, and keep the frontend-system migration current, rather than as a subscription invoice. It integrates with infrastructure as code through plugins, including a maintained [Pulumi plugin for Backstage](/docs/idp/integrations/backstage-plugin/), and reaches observability tools like Prometheus and Grafana the same way: through plugins, not natively.

#### 2. Crossplane

[Crossplane](https://www.crossplane.io/) is a Kubernetes-native, open-source control plane framework for composing and managing cloud infrastructure as custom Kubernetes resources. The CNCF graduated Crossplane on November 6, 2025, its highest maturity level, and Crossplane 2.0 shipped three months earlier removing the "claims" abstraction so the project can build control planes for applications generally, not just infrastructure. It is Apache 2.0 licensed with no vendor behind the license terms. The limitation is depth of general-purpose language support: Crossplane compositions are defined in YAML or embedded functions, so teams that want to define infrastructure in Python, TypeScript, Go, or another general-purpose language for testing and reuse typically pair it with, or replace it with, a tool built on that model. Observability hooks are not native; teams typically layer Prometheus metrics on top of the control plane.

#### 3. Kratix

[Kratix](https://www.syntasso.io/), maintained by Syntasso, is an open-source Kubernetes-native framework for building "Promises," reusable definitions of a platform capability that developers can request through a self-service API. Kratix is company-backed open source rather than a CNCF-hosted project, and its license has not been independently reconfirmed for this piece, so verify before treating it as a drop-in Apache 2.0 dependency. Syntasso extended the model in 2026 with Syntasso Kratix Agentic in private preview, aimed at letting AI agents consume platform capabilities the same way developers do. The strength is a clean separation between defining a platform capability once and letting any number of teams request it; the limitation is a smaller adoption base and ecosystem than Backstage or Crossplane, so fewer prebuilt Promises exist off the shelf. CNCF has documented Kratix consuming Terraform modules directly as a Promise implementation.

#### 4. Argo CD

[Argo CD](https://argo-cd.readthedocs.io/) is the CNCF-graduated GitOps continuous-delivery engine for Kubernetes, reconciling cluster state to what is declared in Git. A July 2025 CNCF end-user survey found it the majority-adopted GitOps solution for Kubernetes with an NPS of 79. It is Apache 2.0 licensed and free at its core, with managed offerings available from third-party vendors. Argo CD's scope is deliberately narrow: it assumes the infrastructure it deploys onto already exists, provisioned by something else, whether that is Crossplane, Pulumi, or Terraform. Self-service is indirect, expressed through Git access and ApplicationSets rather than a dedicated developer-facing API, and golden paths come from repository conventions your platform team establishes rather than a built-in template system.

#### 5. Score

[Score](https://score.dev/) is a CNCF Sandbox project, accepted in July 2024, that defines a platform-agnostic YAML specification for a developer's workload: one file describing what a service needs, portable across environments and target platforms. Score originated at Humanitec, which later donated it to CNCF. It solves a narrow, real problem, letting a developer describe intent once instead of maintaining separate configuration per environment, without requiring adoption of any single vendor's runtime. The honest limitation is that a specification alone does nothing: Score requires an implementation, whether that is the Score CLI targeting Kubernetes, Docker Compose, or a platform like Humanitec, to actually provision anything, and adoption is still early at Sandbox maturity.

### Tools that ship a golden path for you

#### 6. Port

[Port](https://www.port.io/) is a vendor SaaS internal developer portal, positioned in 2026 around what it calls an "Agentic SDLC Platform," that ships self-service actions and blueprints as a pre-built golden path rather than raw primitives to assemble. Port raised a $100 million Series C in December 2025, bringing total funding to $160 million, and publishes tiered pricing starting around $30 per seat per month with a free tier for individuals, a meaningfully more transparent pricing posture than most of its direct competitors. The tradeoff for that speed to value is that the catalog and workflow logic live inside Port's proprietary SaaS rather than a portable open-source artifact, so migrating off Port later means rebuilding those workflows elsewhere. Port documents a direct Pulumi integration for provisioning infrastructure from its self-service actions.

#### 7. Cortex

[Cortex](https://www.cortex.io/) is a vendor SaaS developer portal built around service catalogs and engineering-maturity scorecards that nudge teams toward standards rather than enforcing a fixed template. It raised a $60 million Series C in September 2024 and has published no new funding round since, with roughly $112 to $116 million raised across its history per third-party trackers. Cortex does not publish pricing; prospective buyers get a custom quote, which makes budget planning harder up front than a published-tier competitor like Port. Its strength is genuinely strong maturity scoring for driving organization-wide standards adoption, and its integrations catalog lists 30 or more observability and tooling connections, including Prometheus and Sentry.

#### 8. Humanitec

[Humanitec](https://humanitec.com/) is a vendor platform orchestrator for building internal developer platforms, and the company that originated Score before donating it to CNCF. In 2026 Humanitec repositioned its messaging around governing AI-generated infrastructure changes rather than only manual ones, while continuing to operate its existing orchestration product. A team license has been quoted around $999 per month after a 30-day trial in the company's own materials. Humanitec's scope sits above infrastructure provisioning: it orchestrates deployment configuration and policy at the environment level rather than authoring the underlying cloud resources, so it is typically paired with an IaC engine underneath rather than replacing one.

### The infrastructure layer both approaches depend on

#### 9. Terraform and OpenTofu

Every tool above eventually hands off to something that actually provisions cloud resources, and for most teams that is still [Terraform](https://www.terraform.io/) or its open-source fork, [OpenTofu](https://opentofu.org/). IBM closed its $6.4 billion acquisition of HashiCorp on February 27, 2025, making Terraform formally an IBM product under the Business Source License HashiCorp adopted in August 2023, a source-available term rather than a true open-source one. OpenTofu forked from Terraform's pre-BUSL codebase, moved to Linux Foundation governance around April 2025, and remains MPL-2.0 licensed; its June 2025 1.10 release reported 9.8 million downloads. Both are declarative, HCL-based tools where self-service and golden paths are typically layered on with separate wrapper tooling such as Atlantis or Spacelift rather than built in, and both lack native testing, refactoring, or general-purpose-language reuse, since HCL is a configuration language rather than a programming one.

#### 10. Pulumi

[Pulumi](https://www.pulumi.com/) takes a different position at the same infrastructure layer: infrastructure defined in Python, TypeScript, Go, C#, Java, or YAML, using the same languages, IDEs, and testing frameworks a team already uses for application code. That matters directly for platform engineering, because a golden path built in a real programming language can express loops, functions, tests, and reusable [components](/docs/iac/concepts/components/) the way a shared software library works, rather than a copy-pasted module. [Pulumi Policies](/docs/discovery-governance/policy/) give a platform team the guardrail layer that Humanitec or Cortex provide as a separate product, built into the same platform that provisions the infrastructure. Because it speaks real languages, Pulumi is also built to work as an interface for AI coding agents, which already read, write, and test code, rather than requiring a specialized HCL-generation step the way Terraform-based agent workflows do. Pulumi integrates with Backstage through a maintained plugin and imports existing Terraform state directly, so teams do not have to rewrite their estate to adopt it. The honest tradeoff against Terraform and OpenTofu is ecosystem size: Terraform's decade-plus head start means a larger catalog of community modules exists for it today, even as Pulumi's registry of providers continues to close that gap.

## Comparison at a glance

| Tool | Golden-path posture | License / hosting | Self-service surface | IaC integration | Observability hooks |
|---|---|---|---|---|---|
| Backstage | Build | Apache 2.0, self-hosted | Scaffolder templates | Plugin ecosystem (incl. Pulumi) | Plugin (Prometheus, Grafana) |
| Crossplane | Build | Apache 2.0, self-hosted | Custom Kubernetes APIs | Is the IaC layer (K8s-native) | Not native |
| Kratix | Build | Company-backed OSS, self-hosted | Promise-based self-service API | Consumes Terraform modules as Promises | Not confirmed |
| Argo CD | Build | Apache 2.0, self-hosted | Indirect, via Git/ApplicationSets | Deploys onto existing infra | Native sync/health dashboards |
| Score | Build | CNCF Sandbox spec | Workload spec, needs an implementation | Sits above IaC | Depends on implementation |
| Port | Buy | Proprietary SaaS, tiered pricing | Self-service actions and blueprints | Direct Pulumi integration | Integrations catalog |
| Cortex | Buy | Proprietary SaaS, custom quote | Scorecard-driven standards | Not independently confirmed | 30+ integrations |
| Humanitec | Buy | Proprietary, ~$999/mo team tier | Environment/deployment orchestration | Sits above IaC | Policy dashboards |
| Terraform / OpenTofu | Infrastructure layer | BUSL (Terraform) / MPL-2.0 (OpenTofu) | Layered on via wrapper tools | Is the IaC layer | Layered on |
| Pulumi | Infrastructure layer | Open source core, Pulumi Cloud | Components, policy, IDE-native | Is the IaC layer, in general-purpose languages | Native via Pulumi Cloud + integrations |

## How do you decide what to build and what to buy?

Start from your platform team's actual size and mandate, not from the tool list. A one- or two-person platform team rarely has the headcount to assemble and maintain Backstage, Crossplane, and Argo CD as three separate open-source projects; a Port or Humanitec subscription buys back that engineering time at the cost of a recurring bill and less control over the golden path's shape. A larger, well-resourced platform team often finds the reverse true: the subscription cost compounds faster than the assembly cost, and owning the stack means the golden path can evolve exactly as the organization's infrastructure does, rather than waiting on a vendor roadmap.

Whichever side of that line you land on, the infrastructure layer underneath deserves its own separate decision, because it is the one piece every other tool in this list ultimately depends on. A control plane, an orchestrator, and a portal all eventually need something that actually provisions the cloud resources they describe, and that choice determines whether your golden path can be tested, refactored, and reused the way the rest of your software already is. [Explore what building a platform on Pulumi looks like](/product/) if that language-native approach to the infrastructure layer is the piece you have not evaluated yet.

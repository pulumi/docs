---
title: What is Platform Engineering?
allow_long_title: true
meta_desc: "Platform engineering builds an internal developer platform that gives product teams self-service infrastructure on golden paths with built-in guardrails."
meta_image: /images/what-is/what-is-platform-engineering-meta.png
type: what-is
page_title: What is Platform Engineering?
lastmod: 2026-05-20
authors: ["christian-nunciato"]
---

**Platform engineering is the discipline of building and operating an internal developer platform (IDP) — a curated set of self-service tools, infrastructure, and workflows that lets product teams ship software faster without reinventing the underlying cloud, CI/CD, security, or operations stack.** A dedicated platform team treats developers as customers and ships the platform as an internal product.

The shift to platform engineering is a response to cloud-native complexity. Modern infrastructure (Kubernetes, multi-cloud, serverless, dozens of SaaS providers, policy-as-code, observability) is too much for every product team to learn from scratch. Platform engineering packages the right defaults into golden paths so the easy thing to do is also the secure, reliable, cost-aware thing.

{{< youtube "AUCt28gVR6Y?rel=0" >}}

In this article, we'll cover the key questions about platform engineering:

* Why does platform engineering matter?
* What is an internal developer platform (IDP), and what is a golden path?
* What does a platform engineer do?
* How is platform engineering different from DevOps and SRE?
* What are the requirements for a platform engineering practice?
* How do I get started with platform engineering?
* What are the common challenges of platform engineering?
* How is AI changing platform engineering?
* Frequently asked questions about platform engineering
* Platform engineering case studies

## Why does platform engineering matter?

Developers need infrastructure to run their applications. Traditional models (a central infrastructure team that provisions on behalf of developers) bottleneck under cloud-native load: requests outpace the team that fulfills them, and product teams that try to self-serve end up reinventing the same patterns in different shapes.

Platform engineering exists because:

* **The cloud has become too complex to use unaided.** A single production service can depend on dozens of cloud and SaaS resources, each with its own configuration surface, IAM model, and failure mode.
* **Product teams want speed; the org wants control.** Without a paved road, those goals conflict. With one, they compose.
* **Reinvention compounds.** Every product team that builds its own Kubernetes namespace, CI/CD pipeline, secret rotation flow, and monitoring stack adds drift the security and SRE teams have to manage forever.

In its 2022 Hype Cycle for Software Engineering, Gartner predicted that by 2026, 80% of large software engineering organizations would establish platform teams as internal providers of reusable services, components, and tools for application delivery (up from 45% in 2022). That shift is now well underway across financial services, retail, healthcare, and software-as-a-service.

## What is an internal developer platform (IDP), and what is a golden path?

Two ideas anchor most platform engineering practice.

An **internal developer platform (IDP)** is the product the platform team ships to its developers. It is the unified surface through which developers self-serve everything they need to build, run, and operate their services. A typical IDP combines a developer portal, [infrastructure as code](/what-is/what-is-infrastructure-as-code/) templates, [CI/CD](/what-is/what-is-ci-cd/) pipelines, secrets and policy management, and observability tooling. An IDP is not a single product you buy; it is a curated composition of tools and shared services that reflects your organization's stack, security model, and developer workflows.

A **golden path** (sometimes called a *paved road*) is an opinionated, well-supported route through the platform for a common task — for example, "deploy a stateless TypeScript service to production." Golden paths are designed to be the fastest, lowest-friction, and most secure option for the most common case. Developers can still go off-road for unusual needs, but the platform team commits to maintaining and improving the golden paths as a product.

The combination of an IDP and well-defined golden paths is what makes self-service possible without sacrificing security, compliance, or operational consistency.

## What does a platform engineer do?

*Platform engineer* is the title most often given to the engineers who build and operate a platform team's IDP, but in practice the work is done under many titles: software engineer, DevOps engineer, SRE, cloud architect, cloud engineer.

The role spans product, infrastructure, and developer-facing work:

* **Discovering developer needs.** Running interviews and surveys with internal customers, tracking feedback, and prioritizing the platform roadmap like a product manager would.
* **Building shared infrastructure components.** Authoring reusable [infrastructure as code](/what-is/what-is-infrastructure-as-code/) modules, secure-by-default templates, and service blueprints that developers can compose.
* **Operating the platform itself.** Treating the IDP as production software — running it on SLOs, owning its on-call rotation, and managing its own CI/CD.
* **Embedding guardrails.** Codifying security, compliance, and cost policies (via [Pulumi Policies](/docs/insights/policy/) or similar) so they are enforced automatically rather than reviewed manually.
* **Enabling adoption.** Producing documentation, examples, office hours, and migration tooling so product teams can self-serve onto the platform.

The role draws on a broad skill base: cloud infrastructure and container orchestration, IaC, CI/CD, observability, security, and the product and communication skills required to treat developers as customers.

## How is platform engineering different from DevOps and SRE?

Platform engineering, [DevOps](/what-is/what-is-devops/), and site reliability engineering (SRE) all aim to make software delivery faster and more reliable, but they answer different questions and produce different artifacts.

| | Platform engineering | DevOps | Site reliability engineering (SRE) |
|---|---|---|---|
| Primary goal | Reduce developer friction with self-service infrastructure | Bridge dev and ops through shared culture and tooling | Keep production services reliable at scale |
| Who they serve | Application developers, treated as customers | The whole engineering organization | End users of production services |
| Primary deliverables | Internal platform, golden paths, IDPs, IaC components | CI/CD pipelines, automation, shared practices | SLOs, error budgets, incident response |
| Success metric | Developer self-service adoption and lead time | Deployment frequency and change-failure rate | Service availability against SLOs |
| Mindset | Product engineering for developers | Cultural collaboration across functions | Software engineering applied to operations |

The three disciplines are complementary, not mutually exclusive. Many organizations run all three: DevOps sets the cultural baseline, SRE protects production, and platform engineering productizes the shared tooling that both depend on.

## What are the requirements for a platform engineering practice?

Regardless of implementation details, most successful platform teams converge on the same baseline requirements:

* **Simple and powerful user experience.** Meet developers at their level of expertise with a mix of IaC libraries, CLIs, portals, and templates.
* **Automation as default.** No ClickOps. Every change is tested, traceable, and reversible. Infrastructure, configuration, environments, and secrets are all tracked in version control.
* **Full visibility on everything.** Log, monitor, and observe every layer of the platform for operational control and cost optimization.
* **Security as a foundation.** Fine-grained access controls, dynamic short-lived credentials over long-lived keys, and policy as code that runs on every change.
* **Well-architected by design.** Decouple application complexity from infrastructure complexity. Build shareable components for high availability and low operational maintenance.

## How do I get started with platform engineering?

There is no one-size-fits-all blueprint, but most successful platform initiatives follow a similar sequence:

1. **Identify your developer customers and their top pain points.** Talk to product teams about what currently slows them down (environment provisioning, secrets management, deployment, observability) and rank the problems by frequency and cost.
1. **Treat the platform as a product, not a project.** Stand up a dedicated team with a product manager (or product-minded engineer), define a roadmap, and measure success by developer adoption and lead time rather than infrastructure metrics alone.
1. **Define your first golden path.** Pick the single most common developer workflow (for example, "stand up a new service in production") and pave it end to end. Resist supporting every framework, language, and cloud up front.
1. **Build on reusable IaC components.** Package your golden path as IaC modules, templates, and policies that developers consume rather than copy. Pulumi supports this with general-purpose languages, [reusable components](/docs/iac/concepts/components/), and [policy as code](/docs/insights/policy/).
1. **Layer in self-service through an internal developer portal.** Whether you use [Backstage](https://backstage.io/), [Port](https://www.port.io/), or a custom portal, surface the platform through an interface that meets developers where they already work.
1. **Iterate against a maturity model.** The [CNCF Platform Engineering Maturity Model](https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/) defines five capability areas (investment, adoption, interfaces, operations, measurement) across four stages (provisional, operational, scalable, optimizing).

Team structure matters as much as tooling. The [Team Topologies](https://teamtopologies.com/) framework, widely adopted in platform engineering practice, frames the platform team as a dedicated topology that exists to reduce the cognitive load on stream-aligned product teams.

## What are the common challenges of platform engineering?

Even well-resourced platform teams hit a predictable set of pitfalls:

* **Building in a vacuum.** Platforms designed without continuous developer feedback ship features no one uses. Treat developer interviews and adoption metrics as core platform telemetry.
* **Trying to support everything at once.** Spreading the platform across too many languages, frameworks, or clouds before any single golden path is solid leads to a shallow surface that no team trusts.
* **Confusing platform engineering with shared services.** A central infrastructure team that simply owns shared tooling is not a platform team. Platform engineering requires a product mindset, a defined developer customer, and treating the platform as a first-class internal product.
* **Heavy-handed governance.** Mandating the platform without making it the lowest-friction path drives developers to work around it. Guardrails should be embedded in golden paths, not bolted on as approval gates.
* **Under-investing in operations.** An IDP that is unreliable, slow, or undocumented quickly loses developer trust. Run the platform itself with the same SLOs, observability, and on-call discipline you expect of any production service.

## How is AI changing platform engineering?

Platform engineering is one of the disciplines most directly reshaped by AI. The shift shows up in three places at once:

* **More infrastructure, more surface area to govern.** AI coding assistants let application developers generate infrastructure faster than ever, which means platform teams are now responsible for guardrails over a much larger volume of cloud resources, IaC programs, and configurations than they were even two years ago. Policy as code, drift detection, and centralized observability move from "nice to have" to load-bearing.
* **AI agents as a new class of platform consumer.** Human developers are no longer the only callers of the platform's APIs. Coding agents, deployment agents, and on-call agents increasingly provision, debug, and remediate infrastructure directly. That makes a clean, programmatic, well-documented platform interface significantly more valuable, with strong authentication, authorization, and audit trails on it as table stakes.
* **AI as a force multiplier for platform engineers themselves.** Routine platform work (writing new IaC modules, diagnosing failed deployments, reconciling drift, keeping dependencies current across many stacks) is increasingly automatable. The most leveraged platform teams use AI to extend the surface area a small team can credibly support, not to replace headcount.

[Pulumi Neo](/product/neo/) is a purpose-built AI infrastructure agent designed for this shift. It works inside a platform team's existing Pulumi setup, enforces the same policy as code, and takes on provisioning, debugging, and remediation work, freeing the team to focus on platform design and developer experience.

## Frequently asked questions about platform engineering

### What is the difference between platform engineering and DevOps?

DevOps is a cultural and process shift that aims to break down silos between development and operations. Platform engineering is one concrete way to operationalize DevOps at scale: a dedicated platform team builds an internal product (the platform) that packages DevOps practices into self-service tools for developers. DevOps is the philosophy; platform engineering productizes it.

### Is platform engineering the same as an internal developer platform (IDP)?

No. Platform engineering is the practice; an IDP is one of the artifacts that practice produces. A platform team's deliverables typically include the IDP plus the golden paths, IaC libraries, security guardrails, CI/CD integrations, and operational runbooks that surround it.

### When should an organization invest in a platform team?

The strongest signals are repeated developer wait time on a central ops or infrastructure team, divergent infrastructure patterns across product teams, recurring security or compliance gaps in self-built setups, and growth past the point where shared tooling clearly outweighs the cost of building it. Below that scale, a lightweight set of templates and conventions usually suffices.

### How big should a platform engineering team be?

There is no universal answer, but platform teams often start small (a handful of engineers) and scale with the breadth of the platform's surface area rather than headcount alone. A focused team owning a well-scoped platform consistently outperforms a larger team spread thin across too many internal products.

### Does platform engineering replace SRE?

No — the two are complementary. SRE focuses on the reliability of production services through SLOs, error budgets, and incident response. Platform engineering focuses on developer experience and self-service infrastructure. Most companies that adopt platform engineering keep SRE in place; the platform team often surfaces SRE-defined guardrails through the internal platform itself.

### What tools do platform engineering teams use?

A typical platform stack combines [infrastructure as code](/what-is/what-is-infrastructure-as-code/) (such as Pulumi), a container orchestrator (commonly Kubernetes), a [CI/CD](/what-is/what-is-ci-cd/) system, a secrets and configuration layer (like [Pulumi ESC](/product/esc/) or HashiCorp Vault), a policy-as-code engine ([Pulumi Policies](/docs/insights/policy/), Open Policy Agent), and an IDP front end (Backstage, Port, or a custom portal). The specific tools matter less than how cleanly they compose into a coherent self-service experience.

### How do you measure the success of a platform team?

Adoption and lead-time metrics tend to be more useful than infrastructure metrics. Common ones: the percentage of services on the golden path, the time from a new developer's first commit to their first production deploy, the number of out-of-platform infrastructure changes (lower is better), and the platform's own SLO compliance.

### What's the difference between Backstage, Port, and a custom IDP?

[Backstage](https://backstage.io/) is an open-source developer portal originally from Spotify, highly extensible but operationally heavy. [Port](https://www.port.io/) is a hosted SaaS alternative that lowers the operational burden. A custom IDP — often built on top of a portal framework plus a Pulumi-based [Automation API](/docs/iac/packages-and-automation/automation-api/) layer — is the right call when the off-the-shelf options don't match your team's workflows. Most large platform teams end up with a hybrid.

### Does platform engineering only apply to Kubernetes?

No. Kubernetes is a common workload type, but plenty of platform teams pave roads for serverless, container-based PaaS (Cloud Run, App Service, ECS), data-platform workloads (Snowflake, Databricks), and non-cloud workflows. The discipline is about self-service for developers, not about a specific compute primitive.

### How does Pulumi support platform engineering?

Pulumi gives platform teams general-purpose languages for IaC (TypeScript, Python, Go, C#, Java), [reusable components](/docs/iac/concepts/components/) for packaging golden paths, [Pulumi ESC](/product/esc/) for centralized secrets and configuration, [Pulumi Policies](/docs/insights/policy/) for guardrails, the [Automation API](/docs/iac/packages-and-automation/automation-api/) for embedding IaC inside an IDP or portal, and [Pulumi Insights](/product/pulumi-insights/) for cross-cloud search and analytics. The combination is what makes Pulumi the IaC layer for many production internal platforms.

## Platform engineering case studies

### Elkjøp Nordic

{{< youtube "aoa_O-rh5KE?rel=0" >}}

Elkjøp Nordic is the leading consumer electronics retailer in the Nordics. The company had a modernization strategy to increase the agility of development teams by giving them ownership over their services and the infrastructure that runs them. At the same time, they wanted to create security and compliance guardrails that prevent issues while maintaining developers' freedom. They accomplished this by building an infrastructure platform application that enabled developers to provision infrastructure running on Kubernetes in Azure. Learn more in the [blog post](/blog/how-elkjop-nordic-enables-developers-to-self-serve-infrastructure/).

### Washington Trust Bank

{{< youtube "Q63ZaX340M4?rel=0" >}}

Washington Trust Bank modernized its software development and infrastructure practices since migrating to Azure and adopting infrastructure as code. It enables developers with self-service infrastructure components, prevents developers from deploying forbidden resources with Pulumi Policies, and uses automation to save time and effort.

## Conclusion

Given platform engineering's strong focus on infrastructure management, automation, and standardization, platform teams need a solution that lets them adhere to the discipline's principles while empowering developers to leverage the cloud in a secure, scalable, reliable, and consistent way.

![Pulumi's solution for platform teams](/images/product/platform-teams-diagram.png)

Pulumi's solution for platform teams encompasses all of the key requirements described earlier:

1. The *developer control plane* enables the simple and powerful user experience, allowing platform teams to meet the varying needs of different developers and product teams. Pulumi's core IaC tool supports the languages teams already use (TypeScript, Python, Go, C#, Java, and YAML), with full IDE support and integration with internal developer portals like [AWS Proton](https://aws.amazon.com/proton/) and [Backstage](https://backstage.io/).
1. *Integration and delivery* supports automation as the default through extensive integration with CI/CD systems and Pulumi's own offering, [Pulumi Deployments](/docs/pulumi-cloud/deployments/). The [Automation API](/docs/iac/packages-and-automation/automation-api/) makes it possible to embed IaC inside application software, enabling reusable infrastructure workflows.
1. *Monitoring and logging* provides full visibility on everything through support for leading monitoring and logging solutions. [Pulumi Insights](/product/pulumi-insights/) adds search, analytics, and AI over [Pulumi Cloud](/product/pulumi-cloud/) for actionable knowledge on cloud usage and cost optimization.
1. *Security and identity* ensures security is foundational. [Pulumi Policies](/docs/insights/policy/) provides policy-based controls (including remediation of policy violations) in the same general-purpose languages Pulumi IaC supports. [Pulumi ESC](/product/esc/) provides centralized access to secrets and configuration.
1. Pulumi's robust *provider ecosystem* opens up access to the services, platforms, and offerings needed to build well-architected designs across any cloud.

Pulumi offers a modern, flexible approach to the needs of platform engineering teams. [Request a demo](/contact?form=demo) of Pulumi, or [get started using Pulumi's tools](/docs/iac/get-started/) today.

Related reading:

* [What is Infrastructure as Code (IaC)?](/what-is/what-is-infrastructure-as-code/)
* [What is DevOps?](/what-is/what-is-devops/)
* [What is CI/CD?](/what-is/what-is-ci-cd/)
* [What is Pulumi?](/what-is/what-is-pulumi/)
* [What is Secrets Management?](/what-is/what-is-secrets-management/)
* [What is Cloud Security?](/what-is/what-is-cloud-security/)

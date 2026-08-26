---
title: What is Platform Engineering?
allow_long_title: true
meta_desc: |
    Platform engineering is the discipline of building internal platforms that let developers self-serve infrastructure. Learn what a platform engineer does.
type: what-is
page_title: What is Platform Engineering?
lastmod: 2026-08-21
authors: ["christian-nunciato"]
---

**Platform engineering is the discipline of designing, building, and operating an internal platform, a curated set of self-service tools, infrastructure, and golden paths, that lets application developers provision and manage cloud infrastructure without waiting on a central operations team.** A dedicated platform team treats that internal platform as a product and application developers as its customers, applying product-management discipline (interviews, a roadmap, adoption metrics) to what used to be handled as one-off infrastructure tickets.

{{< youtube "AUCt28gVR6Y?rel=0" >}}

## What is platform engineering?

In a platform engineering approach, one or more teams (often referred to as the platform engineering team or the platform team) build a comprehensive set of shared tools and services (aka "the platform") to help development teams develop, deploy, and operate cloud infrastructure on a self-service basis. This includes cloud infrastructure, container orchestration platforms, databases, networking, monitoring, code repositories, and deployment pipelines.

Platform teams use a customer-driven mindset where they treat the application developers that they serve as customers that must be understood and won over through products that solve their problems. The products these teams offer are infrastructure tools and building blocks that development teams use to provision and manage standardized infrastructure for their applications and services. Typically, these tools have built-in guardrails that enforce best practices and security standards without impeding developers' agility and workflow. This is all done in service of increasing the speed of delivery for the company's products.

## Golden paths and internal developer platforms

Two ideas anchor most platform engineering practice: the *internal developer platform* and the *golden path*.

An **[internal developer platform (IDP)](/what-is/what-is-an-internal-developer-platform/)** is the product that a platform team ships to its developers: the unified surface through which developers self-serve everything they need to build, run, and operate their services. An IDP typically combines a developer portal, [infrastructure as code](/what-is/what-is-infrastructure-as-code/) templates, [CI/CD](/what-is/what-is-ci-cd/) pipelines, secrets and policy management, and observability tooling. An IDP is not a single product you buy; it's a curated composition of tools and shared services that reflects your organization's stack, security model, and developer workflows.

A **golden path** (sometimes called a *paved road*) is an opinionated, well-supported route through the platform for a common task, for example, "deploy a stateless TypeScript service to production." Golden paths are designed to be the fastest, lowest-friction, and most secure option for the most common case. Developers can still go off-road for unusual needs, but the platform team commits to maintaining, supporting, and improving the golden paths as a product. The combination of an IDP and well-defined golden paths is what makes self-service possible without sacrificing security, compliance, or operational consistency.

## What are some of the requirements for platform engineering?

Regardless of implementation details or specific methods, there are some simple requirements that many platform engineering teams follow. All of these requirements are driving toward maximizing the use of the cloud at scale across an organization while being secure and compliant and enabling developers and development teams to ship faster.

* **Simple and powerful user experience**: Build curated experiences that empower developers by meeting them at their level of expertise. Use a variety of approaches to provide an ideal user/developer experience, including infrastructure code libraries (reusable pieces of code), infrastructure CLIs, internal developer portals (IDPs), or shared IaC templates.
* **Automation as default**: Automation reduces devastating errors. Don't leave anything to ClickOps. Every change to infrastructure must be run through tests before rolling into production. No change should be untraceable. All infrastructure from resources, configurations, environments, and secrets are tracked in version control. Everything from infrastructure provisioning to control plane orchestrations needs to be programmable.
* **Full visibility on everything**: Log, monitor, and observe all infrastructure for greater operational control. Optimize against unnecessary costs.
* **Security as a foundation**: Security and compliance guardrails need to exist for everything. Fine-grained access controls should exist for every piece of infrastructure. Prefer dynamic, short-lived credentials over long-lived, static credentials with seamless integration into development workflows.
* **Well architected by design**: Decouple the application complexity from the infrastructure complexity, reducing the blast radius of incidents while increasing resiliency. Construct shareable infrastructure components that are built for high availability and low operational maintenance. Operate seamlessly across heterogeneous environments while implementing best-in-class infrastructure.

## What is a platform engineer?

_Platform engineer_ is a term used to describe the engineers that make up a platform team or a platform engineering team. Typically, these engineers have the multi-disciplinary skills, experience, and empathy needed to build a great product, serve developers' needs, and "go to market" within their company. Often, they have experience with multiple engineering disciplines like infrastructure or DevOps and software engineering. The reality is that many engineers who perform platform engineering responsibilities do not have the title "platform engineer." In practice they have varying job titles like software engineer, DevOps engineer, SRE, cloud architect, cloud engineer, and more. By providing developers with infrastructure and tooling to deploy and operate their applications efficiently, platform engineers enable developers to focus on building great software.

Platform engineers typically take on a mix of responsibilities that span product, infrastructure, and developer-facing work:

* **Discovering developer needs**: Running interviews and surveys with internal customers, tracking feedback, and prioritizing the platform roadmap like a product manager would.
* **Building shared infrastructure components**: Authoring reusable infrastructure as code modules, secure-by-default templates, and service blueprints that developers can compose.
* **Operating the platform itself**: Treating the IDP as production software: running it on SLOs, owning its on-call rotation, and managing its own CI/CD.
* **Embedding guardrails**: Codifying security, compliance, and cost policies so they are enforced automatically rather than reviewed manually.
* **Enabling adoption**: Producing documentation, examples, office hours, and migration tooling so development teams can self-serve onto the platform.

The role draws on a broad skill base: cloud infrastructure and container orchestration, [infrastructure as code](/what-is/what-is-infrastructure-as-code/), CI/CD, observability, security, and the product and communication skills required to treat developers as customers.

### How do you become a platform engineer?

The common route in is from software engineering, DevOps, or SRE backgrounds rather than a dedicated "platform engineering" degree or bootcamp, since the discipline is only a few years old. The path that consistently works: get fluent in an [infrastructure as code](/what-is/what-is-infrastructure-as-code/) tool and a general-purpose language, learn container orchestration (typically Kubernetes), and practice treating internal users as customers by writing docs, running office hours, and measuring adoption rather than only shipping infrastructure. Contributing to an internal platform or IDP effort at your current company, even part time, is the fastest way in.

## How do you build a platform engineering team?

Team composition matters as much as tooling choice. A first platform team is often small, three to six engineers, and deliberately narrow in scope: it picks one golden path, ships it end to end, and expands only after developers are actually using it. The [Team Topologies](https://teamtopologies.com/) framework, widely adopted in platform engineering practice, models the platform team as its own topology that exists specifically to reduce the cognitive load carried by stream-aligned product teams, rather than as a shared-services pool.

Platform teams, once established, tend to stick rather than get rolled back into a central ops function. A platform team typically needs at least one person with product-management instincts (even if that's not their title) to run the roadmap and adoption metrics, alongside engineers who can build and operate the shared infrastructure components themselves. Skipping the product role is one of the most common reasons platform initiatives regress into a renamed ticket queue; see [common challenges](#common-challenges-of-platform-engineering), and the [step-by-step guide to platform engineering and IDPs](/blog/the-guide-platform-engineering-idp-steps-best-practices/) for a fuller walkthrough of team structure and rollout sequencing.

## What tools do platform engineering teams use?

No single product is "the platform." Most platform teams compose tools from each of the following categories into one coherent, self-service experience:

| Category | What it does | Common examples |
|---|---|---|
| Infrastructure as code | Defines and provisions cloud infrastructure declaratively or in a general-purpose language | Pulumi, Terraform, OpenTofu |
| Developer portal / catalog | Gives developers a single self-service front end onto the platform | Backstage, Port, Cortex |
| Container orchestration | Runs and schedules containerized workloads | Kubernetes |
| CI/CD | Builds, tests, and deploys application and infrastructure changes, often via [GitOps](/what-is/what-is-gitops/) | GitHub Actions, Argo CD, Flux |
| Policy and governance | Enforces [policy as code](/what-is/what-is-policy-as-code/) rules for security, cost, and compliance automatically | Pulumi Policies, Open Policy Agent |
| Secrets and configuration | Manages credentials and environment configuration across stacks | Pulumi ESC, HashiCorp Vault |
| Observability | Monitors platform and application health | Datadog, Prometheus, Grafana |

The specific vendor in each row matters less than the seams between rows: a platform where IaC, policy, secrets, and the portal all speak the same language and share the same audit trail is easier to operate and easier for an AI agent to reason about than a stack assembled from disconnected point tools.

## How does platform engineering differ from DevOps and SRE?

Platform engineering, [DevOps](/what-is/what-is-devops/), and site reliability engineering (SRE) all aim to make software delivery faster and more reliable, but they answer different questions and produce different artifacts.

|                       | Platform engineering                                            | DevOps                                                | Site reliability engineering (SRE)                 |
|-----------------------|-----------------------------------------------------------------|-------------------------------------------------------|----------------------------------------------------|
| Primary goal          | Reduce developer friction with self-service infrastructure      | Bridge dev and ops through shared culture and tooling | Keep production services reliable at scale         |
| Who they serve        | Application developers, treated as customers                    | The whole engineering organization                    | End users of production services                   |
| Primary deliverables  | Internal platform, golden paths, IDPs, IaC components           | CI/CD pipelines, automation, shared practices         | SLOs, error budgets, incident response             |
| Success metric        | Developer self-service adoption and lead time                   | Deployment frequency and change failure rate          | Service availability against SLOs                  |
| Mindset               | Product engineering for developers                              | Cultural collaboration across functions               | Software engineering applied to operations         |

The three disciplines are complementary, not mutually exclusive. Many organizations run all three: DevOps sets the cultural baseline, SRE protects production, and platform engineering productizes the shared tooling that both depend on.

## How do you measure whether a platform is working?

Measurement is the discipline's weakest point in practice: the Platform Engineering community's [State of Platform Engineering Report Volume 4](https://platformengineering.org/reports/state-of-platform-engineering-volume-4) (518 respondents, 2025) found that 29.6% of platform teams do not measure success at all. Skipping measurement makes it impossible to defend the platform's budget or rank its roadmap against competing infrastructure requests.

The metrics that hold up in practice fall into three groups:

* **Adoption**: What fraction of eligible services run on a golden path versus a bespoke setup, and how quickly do new services onboard.
* **Delivery performance**: The [DORA metrics](https://dora.dev/) (deployment frequency, lead time for changes, change failure rate, and time to restore service) measured for teams using the platform versus those that are not.
* **Developer experience**: Time-to-first-deploy for a new hire or new service, and direct developer satisfaction with the platform, gathered the same way a product team would gather customer feedback.

According to DORA's [2025 research on platform engineering](https://dora.dev/capabilities/platform-engineering/), adoption of internal developer platforms has become close to universal, with 90% of organizations reporting they use one and 76% having established a dedicated platform team, which raises the bar: a platform without measurement is now competing against platforms that can prove their impact.

## What are the most common myths about platform engineering?

* **"Platform engineering is just DevOps with a new name."** DevOps is a cultural and process philosophy; platform engineering is one concrete way to operationalize it by shipping DevOps practices as a self-service product. The two are related, not interchangeable; see the [comparison table](#how-does-platform-engineering-differ-from-devops-and-sre).
* **"A shared infrastructure team is already a platform team."** A central team that owns shared tooling without a product mindset, a defined developer customer, and measured adoption is functionally an ops team with a new title. It will hit the same request-queue bottlenecks platform engineering exists to solve.
* **"Platform engineering is only for large enterprises."** The pattern scales down: a two- or three-person platform effort that paves a single golden path for a 20-person engineering org delivers the same self-service benefit at a smaller surface area.
* **"A platform team has to build everything in-house."** Most mature platforms compose existing tools (an IaC engine, a portal, a CI/CD system) rather than building each layer from scratch. The platform team's product is the curated, self-service composition, not every underlying component.

## How is AI changing platform engineering?

Platform engineering is one of the disciplines most directly reshaped by AI, and the shift accelerated again in 2026. The Platform Engineering community's [State of AI in Platform Engineering 2025](https://platformengineering.org/reports/state-of-ai-in-platform-engineering-2025) report found that 88% of platform engineers now use AI daily, and its companion [State of Platform Engineering Report Volume 4](https://platformengineering.org/reports/state-of-platform-engineering-volume-4) found 94% of organizations view AI as critical to the discipline's future. Perforce's [State of DevOps Report 2026](https://www.perforce.com/resources/state-of-devops) (820 respondents) found that DevOps maturity is now the strongest predictor of AI success: 72% of high-maturity organizations report AI embedded across their software delivery lifecycle, against 43% of mid-maturity and 18% of low-maturity organizations.

The change shows up in four places at once:

* **More infrastructure, more surface area to govern**: AI coding assistants let application developers generate infrastructure faster than ever, which means platform teams are now responsible for guardrails over a much larger volume of cloud resources, IaC programs, and configurations than they were even two years ago. Policy as code, [drift detection](/what-is/what-is-infrastructure-drift/), and centralized observability move from "nice to have" to load-bearing.
* **AI agents as a new class of platform consumer**: Human developers are no longer the only callers of the platform's APIs. Coding agents, deployment agents, and on-call agents increasingly provision, debug, and remediate infrastructure directly. That makes a clean, programmatic, well-documented platform interface significantly more valuable, with strong authentication, authorization, and audit trails on it as table stakes. For the operational questions this raises, identity and credential scope, where policy evaluates, and what replaces code review when no human is watching, see [how to govern and secure agentic infrastructure](/what-is/what-is-agentic-infrastructure/#how-do-you-govern-and-secure-agentic-infrastructure).
* **Agents as first-class platform tenants, not only assistants**: The Platform Engineering community's [predictions for 2026](https://platformengineering.org/blog/10-platform-engineering-predictions-for-2026) include "agentic infrastructure becomes standard architecture": platform teams are starting to give AI agents their own identities, role-based access controls, and resource quotas, the same governance primitives they already apply to human developers, and to define "agent golden paths" alongside the human ones. Treating an agent as an unmanaged superuser, or conversely blocking it from the platform entirely, are both failure modes; the platform's job is to give agents the same paved road it gives people.
* **AI as a force multiplier for platform engineers themselves**: Routine platform work (writing new IaC modules, diagnosing failed deployments, reconciling drift, keeping dependencies current across many stacks) is increasingly automatable. The most leveraged platform teams use AI to extend the surface area a small team can credibly support, not to replace headcount.

That said, IaC does not disappear as agents take on more of this work, a theme explored further in [what is agentic infrastructure](/what-is/what-is-agentic-infrastructure/). Microsoft's Azure engineering team put it directly in its 2026 analysis of [platform engineering for the agentic era](https://devblogs.microsoft.com/all-things-azure/platform-engineering-for-the-agentic-ai-era/): "Infrastructure as Code (IaC) remains the system of record for enterprise platforms... IaC provides a deterministic desired-state model, versioned change history, reviewable plans, and a reconciliation mechanism for drift." As the interaction stack collapses from *human → ticket → central team → IaC* to *human intent → agent (reasoning and policy) → IaC and APIs*, IaC's declarative, reviewable, versioned nature is exactly what lets an agent's actions stay auditable and reversible rather than opaque.

[Pulumi Neo](/product/neo/) is a purpose-built AI infrastructure agent designed for this shift. It works inside a platform team's existing Pulumi setup, enforces the same policy as code, and takes on provisioning, debugging, and remediation work, freeing the team to focus on platform design and developer experience rather than ticket queues. For how it compares with other options in the category, see our guide to the [best AI infrastructure tools](/blog/ai-infrastructure-tools/).

## How to get started with platform engineering

There is no one-size-fits-all blueprint, but most successful platform initiatives follow a similar sequence:

1. **Identify your developer customers and their top pain points.** Talk to development teams about what currently slows them down (environment provisioning, secrets management, deployment, observability) and rank the problems by frequency and cost.
1. **Treat the platform as a product, not a project.** Stand up a dedicated team with a product manager (or product-minded engineer), define a roadmap, and measure success by developer adoption and lead time rather than infrastructure metrics alone.
1. **Define your first golden path.** Pick the single most common developer workflow (for example, "stand up a new service in production") and pave it end to end. Resist the temptation to support every framework, language, and cloud up front.
1. **Build on reusable infrastructure as code components.** Package your golden path as IaC modules, templates, and policies that developers consume rather than copy. Pulumi supports this with general-purpose languages, [reusable components](/docs/iac/concepts/components/), and [policy as code](/docs/insights/policy/).
1. **Layer in self-service through an internal developer portal.** Whether you use [Backstage](https://backstage.io/), [Port](https://www.port.io/), a custom portal, or [Pulumi's own IDP building blocks](/docs/idp/), surface the platform through an interface that meets developers where they already work.
1. **Iterate against a maturity model.** The [CNCF Platform Engineering Maturity Model](https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/) defines five capability areas (investment, adoption, interfaces, operations, and measurement) across four stages (provisional, operational, scalable, and optimizing), and gives platform teams a shared vocabulary for tracking progress. See our [walkthrough of the model](/blog/platform-engineering-cncf-maturity-model/) for how to score your own platform against it.

Team structure matters as much as tooling; see [how do you build a platform engineering team?](#how-do-you-build-a-platform-engineering-team) for how the Team Topologies framework applies to platform teams specifically.

## Common challenges of platform engineering

Even well-resourced platform teams hit a predictable set of pitfalls. Knowing them in advance is half the battle:

* **Building in a vacuum**: Platforms designed without continuous developer feedback tend to ship features no one uses. Treat developer interviews and adoption metrics as core platform telemetry.
* **Trying to support everything at once**: Spreading the platform across too many languages, frameworks, or clouds before any single golden path is solid leads to a shallow surface that no team trusts.
* **Confusing platform engineering with shared services**: A central infrastructure team that simply owns shared tooling is not a platform team. Platform engineering requires a product mindset, a defined developer customer, and treating the platform as a first-class internal product.
* **Heavy-handed governance**: Mandating the platform without making it the lowest-friction path drives developers to work around it. Guardrails should be embedded in golden paths, not bolted on as approval gates.
* **Under-investing in operations**: An IDP that is unreliable, slow, or undocumented quickly loses developer trust. Run the platform itself with the same SLOs, observability, and on-call discipline you expect of any production service.
* **Not measuring impact**: Nearly 3 in 10 platform teams report no success metrics at all. Without adoption and delivery-performance data, a platform team cannot defend its roadmap or its budget against competing infrastructure priorities.

## Frequently asked questions

### What is the difference between platform engineering and DevOps?

DevOps is a cultural and process shift that aims to break down silos between development and operations. Platform engineering is one concrete way to operationalize DevOps at scale: a dedicated platform team builds an internal product (the platform) that packages DevOps practices into self-service tools for developers. In short, DevOps is the philosophy; platform engineering is a discipline that productizes it.

### Is platform engineering the same as an Internal Developer Platform (IDP)?

No. Platform engineering is the practice; an [Internal Developer Platform (IDP)](/what-is/what-is-an-internal-developer-platform/) is one of the artifacts that practice produces. A platform team's deliverables typically include the IDP plus the golden paths, infrastructure code libraries, security guardrails, CI/CD integrations, and operational runbooks that surround it.

### When should an organization invest in a platform team?

The strongest signals are repeated developer wait time on a central ops or infrastructure team, divergent infrastructure patterns across product teams, recurring security or compliance gaps in self-built setups, and growth past the point where shared tooling clearly outweighs the cost of building it. Below that scale, a lightweight set of templates and conventions suffices.

### How big should a platform engineering team be?

There is no universal answer, but platform teams often start small (a handful of engineers) and scale with the breadth of the platform's surface area rather than headcount alone. A focused team owning a well-scoped platform consistently outperforms a larger team spread thin across too many internal products.

### Does platform engineering replace SRE?

No. The two are complementary. SRE focuses on the reliability of production services through SLOs, error budgets, and incident response. Platform engineering focuses on developer experience and self-service infrastructure. Most companies that adopt platform engineering keep SRE in place; the platform team often surfaces SRE-defined guardrails through the internal platform itself.

## Why is platform engineering important?

Developers need infrastructure to run their applications and services. Traditionally, companies have used central infrastructure teams that provision and manage infrastructure on behalf of developers, but this model is prone to bottlenecks as developer requests for infrastructure overwhelm central teams. As modern development teams have taken responsibility over owning and operating their own infrastructure, they also need fast, self-service ways of provisioning it while adhering to best practices.

Platform teams solve these challenges:

* The cloud is too complex and unwieldy for most developers to use without abstractions and tooling
* Developers need to know which infrastructure resources to provision
* Developers need a self-service way to provision, configure, and manage infrastructure
* Infrastructure provisioned by developers needs to adhere to company best practices

Platform engineering can increase development velocity, improve security, increase infrastructure's adherence to best practices, and reduce operational costs through automation. It helps organizations increase the ROI on cloud investments and improves the software delivery lifecycle so that developers can ship new features faster.

Many companies have already created dedicated teams for platform engineering. In its 2022 Hype Cycle for Software Engineering, Gartner predicted that by 2026, 80% of large software engineering organizations would establish platform teams as internal providers of reusable services, components, and tools for application delivery (up from 45% in 2022), a prediction that tracks closely with DORA's 2025 finding that 76% of organizations have already established a dedicated platform team, a shift that is now well underway across the industry, from financial services to consumer retail (see the [case studies](#case-studies)).

## Case studies

### Elkjøp Nordic

{{< youtube "aoa_O-rh5KE?rel=0" >}}

Elkjøp Nordic is the leading consumer electronics retailer in the Nordics. The company had a modernization strategy to increase agility of development teams by giving them ownership over their services and the infrastructure that runs them. At the same time, they wanted to create security and compliance guardrails that prevent issues while maintaining developers' freedom. They accomplished this by building an infrastructure platform application that enabled developers to provision infrastructure running on Kubernetes in Azure. Learn more in the [blog post](/blog/how-elkjop-nordic-enables-developers-to-self-serve-infrastructure/).

### Washington Trust Bank

{{< youtube "Q63ZaX340M4?rel=0" >}}

Washington Trust Bank modernized its software development and infrastructure practices since migrating to Azure and adopting infrastructure as code. It enables developers with self-service infrastructure components, prevents developers from deploying forbidden resources with Pulumi Policies, and uses automation to save time and effort. As Dennis Sauvé, the bank's first DevOps Engineer, put it: "Pulumi was exactly the Swiss Army Knife versatility we were looking for. We've only uncovered more of what we love about Pulumi as our relationship has evolved." Read the [full case study](/blog/how-a-bank-modernized-its-software-engineering-with-infrastructure-as-code-automation/).

## Conclusion

The defining move in platform engineering is treating shared infrastructure as a product, with developers as its customers, rather than treating it as another central team's ticket queue. A central team that owns shared tooling but skips the product mindset, the defined developer customer, and the commitment to maintained golden paths is no more than a renamed ops team, and it will hit the same bottlenecks. The discipline pays off when self-service is genuinely the lowest-friction path, so guardrails are something developers move through rather than wait on. Get that right, and the platform becomes the route teams choose, not the one they route around.

[Get started with Pulumi](/docs/get-started) to build the reusable components and policy as code your golden paths run on.

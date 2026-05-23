---
title: What is an Internal Developer Platform (IDP)?
allow_long_title: true
meta_desc: "An Internal Developer Platform (IDP) is a self-service layer over an organization's infrastructure. Learn what's in one, why it matters, and how to build."
meta_image: /images/what-is/what-is-an-internal-developer-platform-meta.png
type: what-is
page_title: What is an Internal Developer Platform (IDP)?
authors: ["sarah-hughes"]
---

**An Internal Developer Platform (IDP) is a self-service layer built on top of an organization's infrastructure, CI/CD, and operational tooling that lets application developers provision environments, ship code, and run services without needing to operate the underlying systems.** It abstracts the cloud, container, secrets, and policy stack behind a paved-road interface — a portal, a CLI, an API, or all three — so that the routine path from idea to production is fast, consistent, and safe.

An IDP is the *product* that a [platform engineering](/what-is/what-is-platform-engineering/) team builds. The point isn't to hide the cloud from developers; it's to make the right thing the easy thing. Developers self-serve from a curated catalog of vetted templates and components, and the platform team encodes the organization's standards (security, compliance, cost, reliability) into the platform itself.

{{< youtube "is83TV8nrTg?rel=0" >}}

In this article, we'll cover the key questions about Internal Developer Platforms:

* Why do organizations build IDPs?
* What is inside an Internal Developer Platform?
* How is an IDP different from platform engineering and a PaaS?
* How do you build an Internal Developer Platform?
* What are the benefits of an IDP?
* What are the common pitfalls and anti-patterns?
* What tools are used to build IDPs?
* Frequently asked questions about IDPs

## Why do organizations build IDPs?

A few pressures consistently push engineering organizations toward an internal platform.

### Cognitive load on product teams has gotten unmanageable

A modern application touches dozens of cloud services, a container runtime, a CI/CD system, a secrets store, observability, identity, policy, and cost controls. Expecting every product team to be expert in all of those (and to keep up as the stack changes) is no longer realistic. An IDP moves that expertise into the platform.

### Patterns are repeated everywhere

Without a platform, every team reinvents the same things: a Kubernetes namespace with the right defaults, a database with the right backup policy, a CI/CD template with the right gates, a logging stack with the right indexes. Multiplied across many teams, the duplicated work and divergent quality become a serious tax.

### Standards exist on paper but not in code

Compliance baselines, security policies, and cost rules tend to live in PDFs and wiki pages until someone violates them. An IDP turns those standards into the only path that exists: encryption is on by default because the platform turns it on; secrets come from the central vault because the platform wires them in; cost tags exist because the platform applies them.

### Hiring and onboarding don't scale linearly

A new engineer who has to learn an organization's bespoke combination of cloud, Kubernetes, CI/CD, and policy before they can ship anything is a slow ramp. An IDP collapses the learning curve to "use the portal" for everything routine, freeing the deep ramp for the genuinely novel work.

## What is inside an Internal Developer Platform?

There is no single blueprint, but most production IDPs include some combination of these components.

| Capability | What it does |
|---|---|
| **Service catalog and templates** | "Golden paths" for common service shapes — REST API, worker, scheduled job, data pipeline. New services come from templates. |
| **Self-service infrastructure** | Developers can spin up environments, databases, queues, and clusters from the portal or API without filing a ticket. |
| **Environment management** | Consistent dev / staging / production environments with promotion workflows. |
| **CI/CD integration** | Pre-wired pipelines for build, test, scan, deploy. Developers don't author pipelines from scratch. |
| **Configuration and secrets** | Hierarchical configuration and secrets pulled at runtime from a central store like [Pulumi ESC](/product/esc/) or HashiCorp Vault. |
| **Security and policy guardrails** | [Policy as code](/docs/insights/policy/) blocks insecure configurations; encryption, IAM, and network defaults are baked into platform components. |
| **Observability** | Metrics, logs, traces, and SLO-based alerts wired into every service automatically. |
| **Cost and ownership** | Resources are tagged, attributable, and visible in cost dashboards. |
| **Documentation and discovery** | Searchable catalog of services, owners, dependencies, and runbooks. |

A useful sanity check: if a developer has to read three wikis and ask in two Slack channels to ship a routine change, the IDP doesn't cover enough of the lifecycle yet.

## How is an IDP different from platform engineering and a PaaS?

These three terms get used interchangeably in marketing material. They are not the same thing.

| Term | What it is |
|---|---|
| **Platform engineering** | The discipline and practice of designing, building, and operating internal platforms. The people and the process. |
| **Internal Developer Platform (IDP)** | The product that platform engineering builds — the actual portal, CLI, API, templates, and components developers use. |
| **PaaS (Platform as a Service)** | A vendor-operated platform like Heroku, Vercel, or Google App Engine. Developers consume it; nobody at the customer organization builds or operates it. |

The clearest distinction: with a PaaS, the platform is someone else's product. With an IDP, the platform is *your organization's* product, built by your platform engineering team on top of cloud primitives and best-of-breed tools to fit your organization's specific needs. A PaaS is "rent"; an IDP is "build to suit."

For more on the discipline that produces an IDP, see [what is platform engineering?](/what-is/what-is-platform-engineering/).

## How do you build an Internal Developer Platform?

There is no single right architecture, but the most consistently successful path is incremental.

### Start with the painful path

Identify the single workflow that consumes the most product-team time today — typically environment provisioning, deploying a new service, or onboarding a new developer. Build the first slice of the platform around that workflow. Resist the temptation to design the "platform of the future" before solving today's problem.

### Treat the platform as a product

The platform's users are internal engineers. Apply normal product practice: user research, roadmap, releases, support, telemetry on what's actually used. The teams that succeed run their platform with a product manager and a backlog, not as a side project of an SRE team.

### Build on infrastructure as code

[Infrastructure as code](/what-is/what-is-infrastructure-as-code/) is the substrate. Every platform component (a Kubernetes namespace, a database, a CI/CD pipeline, an observability hookup) is a reusable [Pulumi component](/docs/iac/concepts/components/) that the platform composes on demand. The platform's "Provision a new environment" button is, underneath, a Pulumi program.

### Encode standards as code, not policy documents

Policy, security, and cost rules belong in the same pipeline as the code they govern. [Pulumi Policies](/docs/insights/policy/) and Open Policy Agent let you block insecure configurations before they deploy. The platform consumes the same checks, so the paved-road path is also the compliant path.

### Centralize configuration and secrets

Secrets in code, in CI logs, or in container images are a frequent breach pattern. The platform should pull secrets at runtime from a central store like [Pulumi ESC](/product/esc/), and developers should never see plaintext credentials in their workflow.

### Provide a clear interface

Most IDPs expose two interfaces: a web portal for discovery, requests, and visibility (often built on [Backstage](https://backstage.io/) or [Pulumi IDP](/product/internal-developer-platforms/)), and a CLI or API for the actual work. Both should feel obvious; if developers need training to use the platform, the platform has lost.

### Measure adoption and satisfaction

Track the percentage of services going through the paved road, lead time for a new environment, and qualitative developer satisfaction (typically with NPS-style surveys). Adoption is the leading indicator of value; satisfaction is the leading indicator of churn.

## What are the benefits of an IDP?

Organizations that successfully roll out an IDP see compounding gains:

* **Faster delivery.** New services bootstrap in minutes instead of weeks. Routine changes ship without ticket queues.
* **Faster onboarding.** New engineers ship a real change in days, not months.
* **Consistent practice.** Every service ships with the same observability, the same security defaults, the same on-call wiring.
* **Stronger compliance posture.** Standards are enforced in code, so the paved road is the audit trail.
* **Lower cognitive load.** Product teams stop having to be experts in Kubernetes, IAM, networking, and CI/CD just to ship a feature.
* **Better leverage for platform teams.** A small platform team can multiply hundreds of product engineers.

## What are the common pitfalls and anti-patterns?

A few patterns reliably cause IDP programs to stall:

* **Building everything before delivering anything.** Big-bang platform launches consistently underperform an iterative paved-road approach.
* **Treating the platform as infrastructure, not as a product.** Without a PM and a feedback loop, the platform drifts away from what developers actually need.
* **Over-abstraction.** Hiding the cloud completely from developers backfires the first time they need to debug a real production issue. The platform should be a paved road, not a closed system.
* **Mandate without value.** If the platform's only selling point is "you have to use it," teams will route around it. Adoption has to be pulled, not pushed.
* **Stopping at the portal.** A portal that submits tickets is not a self-service platform. The portal has to invoke automation that actually does the work.
* **Ignoring exit paths.** The platform should make routine work easy *and* leave the underlying primitives accessible for the genuinely novel cases. A platform with no escape hatch eventually loses the senior engineers.

## What tools are used to build IDPs?

A real IDP is a stack, not a single product. Most teams use a mix.

| Layer | Representative tools |
|---|---|
| Platform portal | [Pulumi IDP](/product/internal-developer-platforms/), Backstage, Port, Cortex |
| Infrastructure as code | [Pulumi](/), Terraform, OpenTofu, AWS CDK |
| Container orchestration | Kubernetes, Amazon ECS, GKE Autopilot |
| CI/CD | GitHub Actions, GitLab CI, Argo CD, Buildkite |
| Configuration and secrets | [Pulumi ESC](/product/esc/), HashiCorp Vault, AWS Secrets Manager |
| Policy as code | [Pulumi Policies](/docs/insights/policy/), Open Policy Agent, Kyverno |
| Observability | Prometheus, Grafana, Datadog, OpenTelemetry |
| Service mesh / identity | Istio, Linkerd, SPIFFE, workload identity |

The choice of each tool matters less than the fact that they're stitched together into one paved-road experience.

## Frequently asked questions about IDPs

### What is an Internal Developer Platform in simple terms?

It's the in-house "easy button" that lets developers do all the routine cloud, infrastructure, and deployment work themselves through a curated portal or API, instead of filing tickets to a central team. The platform team builds and operates it; everyone else uses it.

### What is the difference between an IDP and platform engineering?

Platform engineering is the *discipline* — the people, practices, and culture of building developer-facing platforms. The IDP is the *product* of that discipline. You don't have one without the other, but they're not the same thing.

### Do you need an IDP if you have a small team?

Not on day one. A small team can succeed with a few good templates, a shared CI/CD pipeline, and a curated set of [Pulumi components](/docs/iac/concepts/components/). The IDP investment pays back once the number of product teams exceeds what a central group can support directly — typically somewhere in the dozens of engineers.

### Will an IDP replace our infrastructure or operations teams?

No. It changes what they spend their time on. Infrastructure and operations specialists are still needed to architect, scale, troubleshoot, and evolve the underlying systems, but they shift from doing repetitive provisioning work to building and operating the platform that does it.

### How long does it take to build an IDP?

The first useful slice ships in weeks (a templated new-service workflow, a single paved-road CI/CD pipeline). A platform that covers most of an org's services is measured in quarters and years. Treat it as an ongoing investment, not a project with an end date.

### Is Backstage an IDP?

Backstage is a developer portal — a UI layer. It's a common front-end for an IDP, but the platform itself is the combination of Backstage (or Port, Cortex, or [Pulumi IDP](/product/internal-developer-platforms/)) plus the automation, IaC, policy, secrets, and CI/CD that actually do the work.

### Can an IDP work in a regulated industry?

Yes — and arguably it's where IDPs pay off most. Compliance frameworks like SOC 2, HIPAA, and FedRAMP are easier to evidence when standards are enforced in code through [policy as code](/docs/insights/policy/), and when every change leaves a Git audit trail.

### How does an IDP work with multiple clouds?

Cleanly, if it's built on a multi-cloud-capable layer like [Pulumi](/). The platform abstracts cloud-specific differences behind shared components ("a database," "a queue," "a Kubernetes namespace"), and the underlying [infrastructure as code](/what-is/what-is-infrastructure-as-code/) provisions the right primitive on AWS, Azure, GCP, or on-prem.

### How is an IDP different from GitOps?

GitOps is a workflow pattern — desired state in Git, controllers reconcile the live system. An IDP is the broader self-service surface. Many IDPs use GitOps under the hood for deployment, but the IDP also covers things GitOps doesn't (templated service creation, environment provisioning, ticketless onboarding, cost attribution).

### Does Pulumi help build an IDP?

Yes. [Pulumi IDP](/product/internal-developer-platforms/) provides templates, components, and a control plane built on Pulumi's infrastructure-as-code engine, so platform teams can offer self-service infrastructure in TypeScript, Python, Go, C#, Java, or YAML without building everything from scratch. See [announcing Pulumi IDP](/blog/announcing-pulumi-idp/) for the design intent.

## Learn more

Pulumi gives platform engineering teams the building blocks for an Internal Developer Platform: [infrastructure as code](/what-is/what-is-infrastructure-as-code/) in real languages, reusable [components](/docs/iac/concepts/components/), [policy as code](/docs/insights/policy/), [configuration and secrets](/product/esc/), and a control plane that ties them together. [Get started with Pulumi](/docs/get-started/) or [request a demo](/request-a-demo/) of Pulumi IDP.

Related reading:

* [What is Platform Engineering?](/what-is/what-is-platform-engineering/)
* [What is Infrastructure as Code (IaC)?](/what-is/what-is-infrastructure-as-code/)
* [What is DevOps?](/what-is/what-is-devops/)
* [What is DevOps Automation?](/what-is/what-is-devops-automation/)
* [What is Configuration Management?](/what-is/what-is-configuration-management/)
* [Announcing Pulumi IDP](/blog/announcing-pulumi-idp/)

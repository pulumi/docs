---
title: Top Infrastructure as Code Tools
meta_desc: "A comparison of the top Infrastructure as Code (IaC) tools — Pulumi, Terraform, OpenTofu, CloudFormation, ARM/Bicep, GCP Deployment Manager, AWS CDK."
meta_image: /images/what-is/top-iac-tools-meta.png
type: what-is
page_title: "Top Infrastructure as Code Tools"
authors: ["adam-gordon-bell"]
---

**An infrastructure as code (IaC) tool lets you define, provision, update, and destroy cloud resources using a declarative or programmatic specification stored in version control, instead of clicking through a cloud console.** The right tool for a given team depends on which clouds it targets, what languages its engineers already use, how it wants to model state, and how aggressively it intends to test and govern infrastructure.

This page covers the most widely adopted IaC tools as of 2025. It is intentionally opinionated about the criteria that matter — the trade-offs between multi-cloud and cloud-specific tools are real and worth being explicit about. For a primer on the underlying idea, see [what is infrastructure as code?](/what-is/what-is-infrastructure-as-code/).

In this article, we'll cover the key questions about IaC tools:

* What criteria should you use to evaluate IaC tools?
* What are the top multi-cloud IaC tools?
* What are the top cloud-specific IaC tools?
* How do the top IaC tools compare side by side?
* How do you choose between them?
* Frequently asked questions about IaC tools

## What criteria should you use to evaluate IaC tools?

The headline question — "which tool is best?" — isn't useful without context. These are the dimensions that actually differentiate IaC tools in practice.

| Criterion | Why it matters |
|---|---|
| **Languages** | HCL, YAML, and DSLs versus real programming languages affects what you can express, how easy it is to test, and how much your existing engineers can already help. |
| **Multi-cloud** | Whether the tool natively supports the clouds and SaaS providers you target today *and* the ones you might in 24 months. |
| **State model** | Whether state is managed for you, lives in a file you have to host, or is implicit in the cloud platform. Affects collaboration, locking, and disaster recovery. |
| **Testing and abstractions** | First-class support for unit tests, integration tests, and reusable modules/components versus ad-hoc templating. |
| **Ecosystem and providers** | Number of supported providers, package registry quality, and community size. |
| **Governance** | Native policy as code, drift detection, audit trails, and identity integration. |
| **License** | OSS license terms and the implications for self-hosting and enterprise use. |

The list of tools below is filtered down to actively maintained, production-grade options. Niche or stalled tools are omitted.

## What are the top multi-cloud IaC tools?

Multi-cloud tools prevent provider lock-in, normalize skill investment, and let one team manage AWS, Azure, GCP, Oracle, Kubernetes, and SaaS providers with the same workflow.

### [Pulumi](/)

Pulumi defines infrastructure in general-purpose programming languages: TypeScript, JavaScript, Python, Go, C#, Java, and YAML. That choice has downstream consequences — loops, conditionals, abstractions, and testing all come from the language rather than a custom DSL. Pulumi supports over 290 cloud and SaaS providers and ships a managed state backend (Pulumi Cloud) with built-in encryption and locking, plus self-managed backends for teams that need them.

* **Languages.** TypeScript, JavaScript, Python, Go, C#, Java, YAML.
* **Multi-cloud.** AWS, Azure, GCP, Oracle, Kubernetes, plus 290+ providers across cloud and SaaS.
* **State.** Managed by default in Pulumi Cloud with encryption and locking; self-managed backends supported.
* **Testing and abstractions.** Native unit and integration testing; reusable [components](/docs/iac/concepts/components/) in real code.
* **Governance.** [Pulumi Policies](/docs/insights/policy/) (policy as code in the same languages), [Pulumi ESC](/product/esc/) for secrets and environments, audit logs, RBAC.
* **License.** Apache 2.0 (open source); commercial Pulumi Cloud features.

### [Terraform](https://www.terraform.io/)

Terraform popularized multi-cloud IaC. It uses HCL, a declarative DSL designed to be human-readable but limited compared to general-purpose languages — loops, conditionals, and complex logic require Terraform-specific patterns. State lives in a file you host (S3, Azure Blob, GCS, or HashiCorp's commercial backend) with locking, which works but requires explicit setup. As of August 2023, Terraform's license changed from the open-source MPL 2.0 to the source-available Business Source License (BSL).

* **Languages.** HCL (declarative DSL).
* **Multi-cloud.** Wide provider support: AWS, Azure, GCP, Oracle, and many others.
* **State.** State file managed by the user; remote backends and locking require manual setup.
* **Testing and abstractions.** Modules for reuse; testing improved with Terraform Test (1.6+) but limited compared to general-purpose languages.
* **Governance.** Sentinel (commercial) for policy; OSS users typically pair with Open Policy Agent.
* **License.** Business Source License (BSL) since August 2023.

For a direct comparison see [Pulumi vs. Terraform](/docs/iac/comparisons/terraform/).

### [OpenTofu](https://opentofu.org/)

OpenTofu is a community fork of Terraform 1.6.x created in response to the BSL license change. It maintains compatibility with Terraform's HCL, modules, and providers under the Linux Foundation's stewardship. Most Terraform users can migrate by re-pointing their tooling; over time OpenTofu is expected to diverge with community-driven features.

* **Languages.** HCL (Terraform-compatible).
* **Multi-cloud.** Broad — uses the existing Terraform provider ecosystem.
* **State.** State file, same model as Terraform; remote backends supported.
* **Testing and abstractions.** Inherits Terraform's module model.
* **Governance.** Open Policy Agent integration; Sentinel-equivalent OSS options developing.
* **License.** Mozilla Public License 2.0 (open source).

See [Terraform vs. OpenTofu](/docs/iac/comparisons/terraform/opentofu/) for a deeper look.

### [Crossplane](https://www.crossplane.io/)

Crossplane runs as a Kubernetes control plane that provisions cloud resources via custom resource definitions (CRDs). If your team already runs Kubernetes and prefers GitOps for everything, Crossplane lets you manage cloud resources with the same `kubectl` and Argo CD workflow as your applications. It's narrower than the general-purpose tools but a strong fit for Kubernetes-centric platforms.

* **Languages.** YAML (Kubernetes CRDs); composition packages for reuse.
* **Multi-cloud.** AWS, Azure, GCP, plus a growing provider catalog; depth varies.
* **State.** Stored as Kubernetes resources; controllers reconcile continuously.
* **Testing and abstractions.** Composition functions for reuse; testing is improving but less mature than general-purpose tools.
* **Governance.** Inherits Kubernetes RBAC and admission controllers; OPA integration via Kyverno or Gatekeeper.
* **License.** Apache 2.0 (open source); part of the CNCF.

## What are the top cloud-specific IaC tools?

Cloud-specific tools offer tighter integration with one provider's services and use platform-native state tracking. They're a reasonable choice for teams fully committed to a single cloud, but they tie skill investment and code portability to that provider.

### [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)

CloudFormation is AWS's first-party IaC service. Templates are JSON or YAML; deployments are managed as "stacks" with cross-account and cross-region support (StackSets). State is implicit and managed by AWS, which removes a class of operational concerns and adds AWS-specific limitations: template size caps, dependency challenges past a certain scale, and notoriously terse error messages.

* **Languages.** JSON or YAML templates.
* **Multi-cloud.** AWS only.
* **State.** Managed by AWS as part of the stack.
* **Testing and abstractions.** Nested stacks and reusable templates; testing limited.
* **Governance.** AWS Config and Service Catalog; integrates with AWS-native CI/CD.
* **License.** Proprietary (AWS service).

### [AWS Cloud Development Kit (CDK)](https://aws.amazon.com/cdk/)

AWS CDK lets you define infrastructure in TypeScript, JavaScript, Python, Java, or C#. CDK code is synthesized to CloudFormation templates and deployed via CloudFormation, so it shares CloudFormation's strengths (managed state, deep AWS integration) and constraints (AWS-only, CloudFormation's resource limits). CDK is a good choice for teams that want general-purpose languages but are committed to AWS.

* **Languages.** TypeScript, JavaScript, Python, Java, C#.
* **Multi-cloud.** AWS only. The "CDK for Terraform" (CDKTF) project extends the model to Terraform providers, with the caveats of any indirection layer.
* **State.** Managed by CloudFormation after synthesis.
* **Testing and abstractions.** Constructs for reuse; supports unit testing.
* **Governance.** Inherits CloudFormation governance and AWS native services.
* **License.** Apache 2.0 (open source); deploys via the AWS CloudFormation service.

### [Azure Resource Manager (ARM) and Bicep](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/overview)

Azure Resource Manager is Microsoft's native deployment service; ARM templates are JSON. Bicep is an Azure-specific DSL that compiles to ARM JSON and is much easier to read and write. State is implicit and managed by Azure. ARM/Bicep is the right tool when your footprint is entirely Azure and Azure DevOps is your CI/CD.

* **Languages.** ARM JSON or Bicep (Azure DSL).
* **Multi-cloud.** Azure only.
* **State.** Managed by Azure.
* **Testing and abstractions.** Bicep modules; testing through pre-deployment validation.
* **Governance.** Azure Policy and Blueprints.
* **License.** Proprietary (Azure service); Bicep tooling is MIT-licensed.

### [Google Cloud Deployment Manager and Config Connector](https://cloud.google.com/deployment-manager/docs)

Google Cloud Deployment Manager (CDM) manages GCP resources using YAML and Jinja2 templates. It is a relatively narrow tool and Google now positions Config Connector — a Kubernetes-based controller that manages GCP resources via CRDs — as the modern GCP-first IaC layer. For non-Kubernetes GCP-only workloads, CDM still works; for newer projects, most GCP teams either adopt Config Connector or a multi-cloud tool.

* **Languages.** YAML, Jinja2 templates (CDM); YAML CRDs (Config Connector).
* **Multi-cloud.** GCP only.
* **State.** Managed by GCP (CDM) or by Kubernetes (Config Connector).
* **Testing and abstractions.** Templates for CDM; composition via Kubernetes for Config Connector.
* **Governance.** GCP Organization Policy, IAM Conditions.
* **License.** Proprietary (GCP services).

## How do the top IaC tools compare side by side?

| Tool | Languages | Clouds | State | Reuse | Testing | License |
|---|---|---|---|---|---|---|
| **Pulumi** | TS, JS, Python, Go, C#, Java, YAML | Multi (290+ providers) | Managed (or self-hosted) | Real-language components | First-class unit + integration | Apache 2.0 |
| **Terraform** | HCL | Multi | User-hosted state file | Modules (HCL) | Terraform Test (1.6+) | BSL 1.1 |
| **OpenTofu** | HCL | Multi | User-hosted state file | Modules (HCL) | Inherits Terraform model | MPL 2.0 |
| **Crossplane** | YAML (Kubernetes CRDs) | Multi (via providers) | Kubernetes-native | Compositions | Improving | Apache 2.0 |
| **AWS CloudFormation** | JSON, YAML | AWS only | Managed by AWS | Nested stacks | Limited | Proprietary |
| **AWS CDK** | TS, JS, Python, Java, C# | AWS only (CloudFormation) | Managed by CloudFormation | Constructs | Unit tests supported | Apache 2.0 |
| **Azure ARM / Bicep** | JSON, Bicep DSL | Azure only | Managed by Azure | Bicep modules | Pre-deploy validation | Proprietary (Bicep MIT) |
| **GCP CDM / Config Connector** | YAML, Jinja2, CRDs | GCP only | Managed by GCP / Kubernetes | Templates / CRDs | Limited | Proprietary |

## How do you choose between them?

A practical decision tree:

* **You're committed to a single cloud and want the deepest provider integration.** Use the native tool (CloudFormation/CDK for AWS, ARM/Bicep for Azure, CDM/Config Connector for GCP). You give up portability for native depth.
* **You're multi-cloud or expect to be, and your team is comfortable with HCL.** Terraform or OpenTofu. Pick OpenTofu if license openness is a hard requirement; pick Terraform if you want the broader commercial ecosystem.
* **You're multi-cloud, your engineers already use TypeScript/Python/Go, and you care about testing and reuse.** Pulumi. The investment in components, tests, and policy as code in real languages pays off as the platform grows.
* **You're a Kubernetes-first platform team and want GitOps for everything.** Crossplane. The trade-off is narrower provider coverage and a different operational model.

Most teams aren't choosing in a vacuum. They're choosing relative to where they are today — a Terraform shop adding policy, an AWS shop hitting CloudFormation's limits, a Kubernetes team standardizing on one workflow. The right tool is the one whose model matches the next 18 months of your roadmap, not the one with the largest community on GitHub today.

## Frequently asked questions about IaC tools

### What is the most popular IaC tool?

Terraform has the largest community and ecosystem by GitHub stars and download counts. Pulumi is the fastest-growing among teams that want general-purpose languages and built-in testing, and AWS CloudFormation has the largest deployed footprint on AWS because it's the platform default. "Most popular" depends on the cohort you measure.

### Is Pulumi better than Terraform?

For most multi-cloud teams that already use general-purpose languages, yes — Pulumi removes the friction of learning a DSL and brings testing, abstraction, and IDE support that HCL doesn't have. For teams deeply invested in HCL, Terraform's ecosystem is the bigger draw. See [Pulumi vs. Terraform](/docs/iac/comparisons/terraform/) for a detailed comparison.

### What is the difference between Terraform and OpenTofu?

OpenTofu is a community fork of Terraform 1.6.x created after HashiCorp relicensed Terraform under the source-available Business Source License in 2023. OpenTofu remains open source (MPL 2.0) under Linux Foundation stewardship and maintains compatibility with Terraform's HCL and provider ecosystem.

### Can I use multiple IaC tools together?

Yes, and many teams do. A common pattern is one tool for the cloud primitives and another for configuration management or Kubernetes manifests. Pulumi can also import Terraform state and consume Terraform modules directly, so teams migrating off Terraform don't have to do it all at once. See the [Terraform get-started guide](/docs/iac/get-started/terraform/).

### Is YAML a good language for IaC?

For small, mostly-static configurations, yes. It starts to crack when you need loops, conditionals, reusable abstractions, or tests — which is when teams reach for a real programming language. Pulumi supports both, so you can start in [YAML](/what-is/what-is-yaml/) and graduate without changing platforms.

### Are IaC tools free?

Most are open source for the core tool (Pulumi, OpenTofu, Crossplane, AWS CDK), with commercial offerings for managed backends, RBAC, and policy. Terraform's core is now source-available under BSL. The cloud-native services (CloudFormation, ARM, CDM) are free to use but lock you into one provider.

### Do IaC tools work with Kubernetes?

Yes. Pulumi has a strongly-typed Kubernetes provider with CRD support and Helm chart integration. Terraform and OpenTofu have Kubernetes providers; CloudFormation can create EKS clusters; Bicep can create AKS clusters; CDM can create GKE clusters. Crossplane goes further and runs *as* a Kubernetes control plane.

### How does policy as code fit in?

Policy as code lets you encode security, compliance, and cost rules that run against every infrastructure change. [Pulumi Policies](/docs/insights/policy/) work in the same languages as the IaC programs; Open Policy Agent (OPA) is the cross-tool standard; HashiCorp Sentinel is Terraform's commercial option.

### How do you handle secrets in IaC?

Never embed secrets in code or state files. Pull them at runtime from a dedicated store. [Pulumi ESC](/product/esc/) provides hierarchical environments and dynamic secrets across teams and clouds; HashiCorp Vault, AWS Secrets Manager, and Azure Key Vault are common alternatives.

### What is drift, and how do IaC tools handle it?

Drift is when the real cloud state diverges from what's declared in code — usually because someone made a manual change. Pulumi surfaces drift on every `pulumi preview`; Terraform/OpenTofu detect it on `plan`; CloudFormation flags it via Drift Detection. The mitigation in all cases is to make the IaC pipeline the only way to change production.

## Learn more

Pulumi is open-source infrastructure as code in TypeScript, JavaScript, Python, Go, C#, Java, and YAML. It supports over 290 cloud and SaaS providers, ships with policy as code and secrets management, and integrates with the CI/CD systems your team already uses. [Get started for free](/docs/get-started/).

Related reading:

* [What is Infrastructure as Code (IaC)?](/what-is/what-is-infrastructure-as-code/)
* [What is Pulumi?](/what-is/what-is-pulumi/)
* [Pulumi vs. Terraform](/docs/iac/comparisons/terraform/)
* [What is DevOps?](/what-is/what-is-devops/)
* [What is YAML?](/what-is/what-is-yaml/)
* [What is Configuration Management?](/what-is/what-is-configuration-management/)

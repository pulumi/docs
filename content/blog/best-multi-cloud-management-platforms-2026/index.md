---
title: "Best Multi-Cloud Management Platforms in 2026"
date: 2026-11-20
draft: false
meta_desc: "The best multi-cloud management platforms in 2026, grouped by job: Pulumi, Terraform, OpenTofu, Spacelift, Scalr, env zero, Crossplane, Morpheus, and more."
authors:
    - pulumi-content-team
tags:
    - multi-cloud
    - infrastructure-as-code
    - platform-engineering
    - cloud-engineering
category: general
faq_schema: true
itemlist_name: "Multi-Cloud Management Platforms"
itemlist:
    - name: "Pulumi"
      url: "https://www.pulumi.com/"
    - name: "Terraform and HCP Terraform"
    - name: "OpenTofu"
    - name: "Spacelift"
    - name: "Scalr"
    - name: "env zero"
    - name: "Crossplane"
    - name: "HPE Morpheus Software"
    - name: "CloudBolt"
    - name: "Red Hat Ansible Automation Platform"
    - name: "CloudHealth by Broadcom"
    - name: "Flexera One"
    - name: "Azure Arc"
    - name: "GKE Enterprise"

related_posts:
    - infrastructure-as-code-tools
    - best-terraform-alternatives
    - multicloud-app
    - multicloud-policy-as-code

# Social media copy: auto-posted to X, LinkedIn, and Bluesky when merged to master.
# Character limits: X ~280, Bluesky 300, LinkedIn 3000. Leave blank to skip a platform.
social:
    twitter: |
        "Multi-cloud management platform" covers six different jobs: provisioning, IaC orchestration, Kubernetes control planes, hybrid self-service, FinOps, and provider-native hybrid.

        We sorted 14 tools by job and compared them honestly.
    linkedin: |
        Search for "multi-cloud management platform" and you get Terraform, Ansible, cost dashboards, and hybrid VM managers in one list, as if they were interchangeable. They solve different problems.

        We grouped 14 tools by the job they do: provisioning (Pulumi, Terraform, OpenTofu), IaC orchestration (Spacelift, Scalr, env zero), Kubernetes control planes (Crossplane, GKE Enterprise), hybrid self-service (HPE Morpheus, CloudBolt, Ansible), FinOps (CloudHealth, Flexera), and provider-native options (Azure Arc).

        Each entry covers strengths, limits, and best fit, with a comparison table, a section on what portability across clouds really takes, and an FAQ.
    bluesky: |
        "Multi-cloud management platform" spans provisioning, IaC orchestration, Kubernetes control planes, hybrid self-service, FinOps, and provider-native hybrid.

        We sorted 14 tools by job and compared them honestly, Pulumi's tradeoffs included.
---

The best multi-cloud management platform depends on the job. Pulumi, Terraform, and OpenTofu provision infrastructure. Spacelift, Scalr, and env zero orchestrate IaC runs. Crossplane and GKE Enterprise manage Kubernetes fleets. HPE Morpheus and CloudBolt handle hybrid self-service. CloudHealth and Flexera cover cost. Many teams combine two or three.

<!--more-->

Many organizations become multi-cloud without planning to. Flexera's [2026 State of the Cloud report](https://www.flexera.com/about-us/press-center/flexera-finds-cloud-value-is-rising-while-ai-waste-grows) found AWS running active enterprise workloads at 83% of organizations surveyed and Azure at 79%, and it attributes the continued rise in multi-cloud to mergers, SaaS sprawl, and decentralized teams more often than to deliberate strategy. The same survey puts 73% of organizations on hybrid estates.

Once a second cloud shows up, someone has to decide how to manage it, and a search for "multi-cloud management" returns infrastructure as code (IaC) tools, run orchestrators, hybrid virtual machine managers, and cost dashboards in a single list. This guide sorts 14 tools into the job each one does, compares them in one table, and then takes on the question most lists skip: what makes infrastructure portable across clouds, and what does not.

We build Pulumi, so Pulumi is on the list and we say where it fits and where it does not. Competitor details come from each vendor's public documentation and pricing pages, linked throughout. Where a price is not published, we say so.

## What is a multi-cloud management platform?

A multi-cloud management platform is software that lets a team provision, govern, or observe infrastructure across two or more cloud providers from one place. The label covers several categories: IaC tools that create resources, orchestrators that run IaC safely, control planes that manage clusters, self-service portals for hybrid estates, FinOps tools that track spend, and provider-native hybrid options.

No single product covers all of them well. A practical stack picks one tool per job that matters to your team and avoids paying for overlap.

## Six jobs hide behind one label

Sort tools by job before comparing features. Two products in different categories rarely compete, and two in the same category usually differ on how you define infrastructure and who runs it.

| Job | What it answers | Tools in this guide |
| --- | --- | --- |
| Provision infrastructure | How do we define and change resources across clouds? | Pulumi, Terraform and HCP Terraform, OpenTofu |
| Orchestrate and govern IaC runs | How do we run plans, apply policy, and detect drift across teams? | Spacelift, Scalr, env zero |
| Kubernetes control plane | How do we manage clusters and cloud resources through Kubernetes APIs? | Crossplane, GKE Enterprise |
| Hybrid self-service and automation | How do we offer a governed catalog across VMs, private cloud, and public cloud? | HPE Morpheus Software, CloudBolt, Ansible Automation Platform |
| Cost and FinOps | Where is the money going across clouds? | CloudHealth by Broadcom, Flexera One |
| Provider-native hybrid | How do we extend one provider's governance to other environments? | Azure Arc, GKE Enterprise |

## Comparison table: 14 multi-cloud management platforms

| Tool | Job | Where it works | How you define infrastructure | Open source | Public pricing | Best for |
| --- | --- | --- | --- | --- | --- | --- |
| Pulumi | Provision, plus platform layer | AWS, Azure, Google Cloud, Kubernetes, SaaS, on-prem | TypeScript, Python, Go, C#, Java, YAML | Yes (SDK and engine) | Free, then Essentials $40/mo, Pro $400/mo, Enterprise by quote | Teams that want real programming languages |
| Terraform / HCP Terraform | Provision, managed runs | Any cloud with a provider | HCL | Source-available (BSL) | Free tier up to 500 resources; paid by managed resources | Orgs standardized on Terraform |
| OpenTofu | Provision | Terraform-compatible providers | HCL | Yes | Free | Terraform-style IaC under neutral governance |
| Spacelift | Orchestrate | Terraform, OpenTofu, Pulumi, and others | Whatever the underlying tool uses | No | Free plan; Starter from $399/mo; Business and Enterprise by quote | Platform teams running several IaC tools |
| Scalr | Orchestrate | Terraform and OpenTofu | HCL | No | Free to 50 runs/month, then per run | Teams that want per-run billing |
| env zero | Orchestrate, self-service | Terraform, OpenTofu, and others | Whatever the underlying tool uses | No | Free tier (250 runs/month); paid by quote | Governed, expiring environments for developers |
| Crossplane | Kubernetes control plane | AWS, Azure, Google Cloud via providers | Kubernetes YAML and compositions | Yes (CNCF graduated) | Free; commercial via Upbound | Kubernetes-centric platform teams |
| HPE Morpheus Software | Hybrid self-service | VMs, containers, private and public cloud | Catalogs, blueprints, automation | No | Per-socket subscription | VMware-estate modernization |
| CloudBolt | Hybrid self-service, FinOps | Hybrid and multi-cloud | Catalogs and blueprints | No | Paid plans by quote | Governed self-service across estates |
| Ansible Automation Platform | Configuration and automation | Anything reachable by SSH or API | YAML playbooks | Core is open source | Subscription | Configuration and day-2 operations |
| CloudHealth by Broadcom | FinOps | AWS, Azure, Google Cloud, hybrid | Not applicable | No | By quote | FinOps in Broadcom-aligned enterprises |
| Flexera One | FinOps and ITAM | Public cloud, SaaS, on-prem | Not applicable | No | By quote | Unifying cloud cost and software assets |
| Azure Arc | Provider-native hybrid | Non-Azure servers, Kubernetes, data services | Azure Resource Manager | No | Mixed; add-on services billed | Microsoft-centric organizations |
| GKE Enterprise | Kubernetes fleet management | GKE, Google Distributed Cloud, attached clusters | Kubernetes manifests | No | Per-vCPU edition billing | Kubernetes-heavy teams on or near Google Cloud |

Pricing details change often, so confirm against each vendor's pricing page before budgeting.

## Provision infrastructure: Pulumi, Terraform, and OpenTofu

### Pulumi lets you define multi-cloud infrastructure in general-purpose languages

[Pulumi](/) is an open source IaC platform where you write infrastructure in TypeScript, Python, Go, C#, Java, or YAML. One program and one state model can create resources in AWS, Azure, Google Cloud, Kubernetes, and SaaS providers, drawing on hundreds of packages in the [Pulumi Registry](/registry/). Because the code is a real language, you get loops, functions, tests, package managers, and IDE support.

The Pulumi CLI, engine, and SDKs are open source under the Apache 2.0 license and run without Pulumi Cloud. You can keep state in a [self-managed backend](/docs/iac/concepts/state-and-backends/) such as Amazon S3, Azure Blob Storage, Google Cloud Storage, or PostgreSQL, and the [Pulumi Cloud and open source comparison](/docs/iac/guides/basics/pulumi-cloud-vs-oss/) lays out what each option leaves you to run yourself.

Pulumi Cloud adds the platform layer: managed state, [Pulumi ESC](/docs/esc/) for secrets and configuration, Pulumi Discovery for inventory and scanning across accounts and clouds, Pulumi Policies for policy as code, deployments, and Neo, an infrastructure agent that proposes changes and opens pull requests with human approval. Components and templates let platform teams publish reusable building blocks that developers consume as libraries. Some of these features depend on the edition: policy enforcement modes start at Essentials, and drift detection starts at Pro.

- **Strengths:** abstraction and testing in languages teams already know; one workflow across clouds; strong fit for AI coding agents that already work in those languages.
- **Watch out for:** the module ecosystem is smaller than Terraform's, teams need some comfort with a programming language, and Pulumi Cloud pricing is credit-based, so size it before you commit.
- **Pricing:** Free for one user; Essentials $40/month for up to 500 managed resources; Pro $400/month for up to 2,000; Enterprise by quote, per the [pricing page](/pricing/).
- **Best for:** teams that want infrastructure in code they can test and reuse, with state, secrets, policy, and inventory in one place.

### Terraform and HCP Terraform have the largest provider and module ecosystem

[Terraform](https://developer.hashicorp.com/terraform) uses HCL, a domain-specific language, and reaches nearly any cloud or SaaS product through its provider registry. [HCP Terraform](https://developer.hashicorp.com/terraform/cloud-docs/overview) adds managed runs, policy through Sentinel or OPA, and a private registry. HashiCorp is now part of IBM, and the Terraform CLI has been under the Business Source License since 2023.

Pulumi works alongside Terraform in two separate ways, and neither requires rewriting Terraform code. [Pulumi HCL](/docs/iac/languages-sdks/hcl/) runs the same `.tf` files on Pulumi's engine, with [documented differences](/docs/iac/languages-sdks/hcl/hcl-language-reference/#terraform-compatibility), so a team can keep writing HCL and use Pulumi state and secrets. Pulumi Cloud can also act as a [Terraform state backend](/docs/integrations/terraform/state-backend/): teams keep running the Terraform or OpenTofu CLI, and Pulumi Cloud stores the state with update history, locking, and access controls.

- **Strengths:** the deepest talent pool, module library, and third-party tooling in the category.
- **Watch out for:** HCL offers less abstraction than a general-purpose language and its testing is limited to the built-in `terraform test` framework, the license matters to some buyers, and paid HCP Terraform plans are metered by managed resources.
- **Best for:** organizations already standardized on Terraform that want first-party managed runs and enterprise support.

### OpenTofu is the vendor-neutral Terraform fork

[OpenTofu](https://opentofu.org/) forked Terraform in 2023 under the Linux Foundation and keeps Terraform-style HCL workflows and provider compatibility. The CNCF [accepted it as a Sandbox project](https://www.cncf.io/projects/opentofu/) in April 2025. OpenTofu is free and has no commercial owner. Version 1.7 added [state encryption](https://opentofu.org/docs/language/state/encryption/), which encrypts state files at rest with a passphrase or a cloud key management service.

- **Strengths:** neutral governance, familiar syntax for Terraform users, and built-in state encryption.
- **Watch out for:** still HCL, no first-party managed platform, and the ecosystem may diverge from Terraform over time.
- **Best for:** teams that want open source Terraform-style IaC without a single vendor behind it.

## Orchestrate and govern IaC runs: Spacelift, Scalr, and env zero

These tools sit above an IaC tool. They run plans and applies, enforce policy, detect drift, and manage access across teams. You still need an IaC tool underneath. Our [comparison of IaC orchestration platforms](/docs/iac/comparisons/tacos/) covers the category in more depth.

### Spacelift supports many IaC tools behind one policy engine

[Spacelift](https://spacelift.io/) orchestrates Terraform, OpenTofu, Pulumi, CloudFormation, Ansible, and Kubernetes workflows, with stack dependencies, drift detection, and a flexible policy engine. Its [pricing page](https://spacelift.io/pricing) lists a free plan, a Starter plan from $399 per month with 10 users, and Business and Enterprise tiers by quote. Spacelift also publishes its own long list of multi-cloud tools, which is a useful second opinion.

Spacelift runs Pulumi stacks, so a team can write infrastructure in Pulumi and orchestrate it with Spacelift. A team that uses only Pulumi gets runs, policy, and drift detection from Pulumi Cloud, so for them the two compete. See our [Pulumi and Spacelift comparison](/docs/iac/comparisons/spacelift/) for the details.

- **Strengths:** multi-tool support and policy flexibility.
- **Watch out for:** it adds a layer on top of your IaC tool, and Business and Enterprise pricing requires a sales conversation.
- **Best for:** platform teams that run several IaC tools and want one governed workflow.

### Scalr offers Terraform and OpenTofu runs with per-run pricing

[Scalr](https://scalr.com/) provides remote operations for Terraform and OpenTofu with a hierarchical account and RBAC model, plus [Open Policy Agent policies](https://docs.scalr.io/docs/policy-as-code) and [Checkov scans](https://docs.scalr.io/docs/checkov) built into runs. Its [pricing](https://scalr.com/pricing) is based on runs, with a free tier up to 50 runs per month and no per-user or per-resource fees.

- **Strengths:** predictable billing for teams that dislike resource-based metering; free self-hosted agents.
- **Watch out for:** focused on Terraform and OpenTofu, with a smaller footprint than Spacelift or HCP Terraform.
- **Best for:** teams moving off resource-metered pricing that would rather pay per run.

### env zero focuses on governed self-service environments

[env zero](https://www.envzero.com/) (formerly env0) manages IaC deployments with self-service environments, guardrails and policies, and drift management across Terraform, OpenTofu, and other tools. Its [pricing page](https://www.envzero.com/pricing) lists a free tier with 250 runs per month and 30 active environments; paid plans are custom.

The [Cloud Compass](https://docs.envzero.com/guides/cloud-compass/cloud-compass) feature extends env zero to infrastructure it does not manage yet. It scans AWS, Azure, and Google Cloud accounts for resources that no IaC manages and can generate Terraform or OpenTofu code to bring them under management.

- **Strengths:** developer self-service with governance guardrails, visibility into unmanaged resources, and a generous free tier.
- **Watch out for:** paid pricing is not public, and like the others it needs an IaC tool beneath it.
- **Best for:** teams that want developers to spin up governed, expiring environments.

## Kubernetes control planes: Crossplane and GKE Enterprise

### Crossplane turns cloud resources into Kubernetes-native APIs

[Crossplane](https://www.crossplane.io/) lets platform teams define composite resource definitions (XRDs) and compositions that expose cloud resources as Kubernetes custom resources, then reconciles them continuously through controllers. The CNCF [announced its graduation](https://www.cncf.io/announcements/2025/11/06/cloud-native-computing-foundation-announces-graduation-of-crossplane/) in November 2025, and Upbound sells a commercial platform built on it.

Crossplane and Pulumi can run together. Pulumi's Kubernetes provider can install Crossplane and apply its manifests, so some teams bootstrap Crossplane with Pulumi. Teams that want continuous, GitOps-style reconciliation without writing compositions can run the [Pulumi Kubernetes Operator](/docs/integrations/clouds/kubernetes/pulumi-kubernetes-operator/), which keeps Pulumi stacks for any cloud in sync from inside a cluster. See our [Pulumi and Crossplane comparison](/docs/iac/comparisons/crossplane/) for more paths.

- **Strengths:** continuous reconciliation and a natural fit for self-service platform APIs.
- **Watch out for:** requires Kubernetes expertise and YAML composition skills, and debugging compositions has a learning curve.
- **Best for:** Kubernetes-centric platform teams building internal infrastructure APIs.

### GKE Enterprise manages Kubernetes fleets from Google Cloud

[GKE Enterprise](https://cloud.google.com/kubernetes-engine/enterprise/docs) is the premium GKE edition that replaced the Anthos brand. It provides fleet management, configuration sync, and policy across GKE, Google Distributed Cloud, and attached clusters. Billing is per vCPU under management, per the [GKE pricing page](https://cloud.google.com/kubernetes-engine/pricing).

- **Strengths:** deep integration with GKE and fleet-level policy.
- **Watch out for:** scope is Kubernetes only and the center of gravity is Google Cloud.
- **Best for:** Kubernetes-heavy teams on or near Google Cloud.

## Hybrid self-service and automation: Morpheus, CloudBolt, and Ansible

### HPE Morpheus Software unifies governance across hypervisors and clouds

[HPE Morpheus Software](https://www.hpe.com/us/en/products/software/morpheus-software.html) is a cloud management platform for self-service catalogs, automation, and governance across VMs, containers, private cloud, and public cloud. HPE positions it for VMware-estate modernization and sells it by CPU socket.

- **Strengths:** broad coverage of on-premises and public environments in one catalog.
- **Watch out for:** built around infrastructure operations more than developer workflows.
- **Best for:** enterprises with large private cloud or VMware footprints that need multi-cloud governance.

### CloudBolt adds governed self-service and FinOps for hybrid estates

[CloudBolt](https://www.cloudbolt.io/) combines a cloud management platform with cost optimization features for hybrid and multi-cloud environments. Paid pricing is by quote.

- **Strengths:** self-service with guardrails and cost visibility in one product.
- **Watch out for:** pricing and some roadmap details require vendor conversations.
- **Best for:** enterprises that need governed provisioning across mixed estates.

### Ansible Automation Platform automates configuration and day-2 operations

[Red Hat Ansible Automation Platform](https://www.redhat.com/en/technologies/management/ansible) runs agentless automation against any environment reachable by SSH or API. Ansible is strong for configuration management and operations, and weaker as a state-tracked provisioning tool.

- **Strengths:** a large content collection ecosystem and a gentle learning curve.
- **Watch out for:** playbooks are procedural, so drift and resource lifecycle need extra care.
- **Best for:** configuration and operational automation across heterogeneous estates, often alongside an IaC tool.

## Cost and FinOps: CloudHealth and Flexera One

### CloudHealth by Broadcom gives mature multi-cloud cost governance

[CloudHealth by Broadcom](https://www.broadcom.com/products/software/finops/cloudhealth) covers cost visibility, allocation, and governance across AWS, Azure, Google Cloud, and hybrid environments. It does not provision anything.

- **Strengths:** long track record and enterprise-grade reporting.
- **Watch out for:** pricing is by quote, and the product now sits inside Broadcom's wider portfolio, so check roadmap commitments.
- **Best for:** FinOps teams in enterprises already aligned with Broadcom.

### Flexera One joins cloud cost with software and asset management

[Flexera One](https://www.flexera.com/products/flexera-one) combines FinOps with IT asset management and SaaS management across public cloud, SaaS, and on-premises estates.

- **Strengths:** a single view of cloud, SaaS, and license spend.
- **Watch out for:** breadth can mean complexity, and it does not provision infrastructure.
- **Best for:** enterprises that want cloud cost and IT asset data together.

## Provider-native hybrid: Azure Arc

[Azure Arc](https://learn.microsoft.com/en-us/azure/azure-arc/overview) projects non-Azure servers, Kubernetes clusters, and data services into Azure Resource Manager so you can apply Azure Policy, RBAC, and Defender to them. Many control-plane features are free, and add-on services are billed separately.

- **Strengths:** consistent governance for Microsoft-centric organizations.
- **Watch out for:** the control plane is Azure, so it extends one provider's model rather than offering a cloud-neutral one.
- **Best for:** organizations that already govern through Azure and want to bring other environments under it.

## What makes multi-cloud infrastructure portable?

All of these tools say they work across clouds, and the provisioning tools mean it literally: one program can target AWS and Azure. Targeting two clouds is not the same as being able to move a workload between them. IaC lowers the rewrite cost of a move, and three things decide how much work is left.

1. **How infrastructure is defined.** If every resource is a provider-specific block, a move means rewriting each one. If you wrap provider resources in components with a stable interface, such as a "database" or "cluster" component, you swap the implementation behind the interface and keep the callers unchanged. Real programming languages make this pattern ordinary software engineering. Our [multi-cloud application walkthrough](/blog/multicloud-app/) shows the idea in code.
1. **How state, secrets, and policy are managed.** If these live in one system with one workflow, changing clouds changes the resources and leaves the process intact. Policy written once and applied to every cloud keeps guardrails consistent, as described in [multi-cloud policy as code](/blog/multicloud-policy-as-code/).
1. **Which services you depend on.** Managed databases, queues, identity systems, and machine learning services have different APIs and behavior on each cloud, and a portable program still calls each one on its own terms.

Data is the other hard limit. Moving terabytes between providers involves egress fees and downtime planning that no tool automates away. Treat portability as a way to reduce rewrite effort and negotiating risk, and plan data moves separately.

If you are weighing a change of IaC tool as part of this, the [Pulumi and Terraform comparison](/docs/iac/comparisons/terraform/) walks through the technical differences and migration paths. Our roundup of [Terraform alternatives](/blog/best-terraform-alternatives/) covers the wider field.

## How do you choose the right multi-cloud management platform?

Start from the problem you have today, then add a layer only when a new problem appears:

- **You need to define and change infrastructure across clouds:** choose an IaC tool. Pulumi suits teams that want languages and tests; Terraform suits teams that value the largest module ecosystem; OpenTofu suits teams that want neutral open source HCL.
- **Many teams share IaC and you need guardrails, drift detection, and approvals:** add an orchestrator such as Spacelift, Scalr, or env zero, or use the policy and deployment features built into your IaC platform.
- **Your platform is built on Kubernetes:** evaluate Crossplane, or Pulumi if you prefer defining those resources in code.
- **You run large VM and private cloud estates:** look at HPE Morpheus or CloudBolt for self-service and governance, and Ansible for configuration.
- **Finance asks where cloud spend goes:** add CloudHealth or Flexera One alongside your provisioning tool.
- **Most of your estate is one cloud with some extensions:** the provider's native option, such as Azure Arc or GKE Enterprise, may be enough.

Avoid buying overlapping layers. A common failure is stacking an orchestrator, a cloud management platform, and a cost tool before the team has settled how it defines infrastructure.

## Who runs multi-cloud infrastructure with Pulumi?

Public case studies show the scale teams reach:

- **Wiz** provisions Kubernetes clusters on every major cloud provider, in every region its customers use. Built on the Pulumi Automation API and Go SDK, the system runs thousands of stacks across more than 100 data centers and manages over a million cloud resources, per its [case study](/customers/wiz/).
- **Supabase** manages roughly 80,000 Pulumi resources across 16 AWS regions, up from about 30,000 a year earlier, per its [case study](/customers/supabase/).
- **Atlassian** reported cutting developer time spent on maintenance by more than 50%, per its [case study](/customers/atlassian/).

## Frequently asked questions

### What is a multi-cloud management platform?

A multi-cloud management platform is software that lets teams provision, govern, or monitor infrastructure across two or more cloud providers from one place. The term spans IaC tools, IaC orchestrators, Kubernetes control planes, hybrid self-service portals, and FinOps tools. Many organizations combine two or three rather than relying on one.

### What is the difference between multi-cloud and hybrid cloud?

Multi-cloud means using services from more than one public cloud provider, such as AWS and Azure. Hybrid cloud means combining public cloud with private or on-premises infrastructure. Many organizations are both, which is why platforms like HPE Morpheus and Azure Arc market to both cases.

### Is Terraform a multi-cloud management tool?

Terraform is a multi-cloud provisioning tool. It creates and changes resources on any cloud with a provider, using HCL. Terraform does not track spend, run a hybrid self-service catalog, or manage Kubernetes fleets, so teams usually pair it with other tools for those jobs. Pulumi and OpenTofu fill the same provisioning role.

### Do I need a cloud management platform if I already use IaC?

Often not. If your goal is consistent, reviewable provisioning, an IaC tool with state, policy, and secrets management covers it. Add a cloud management platform when you must offer a governed self-service catalog over VMs and private cloud, or add a FinOps tool when finance needs allocation and forecasting.

### Can you combine these tools?

Yes, and many teams do. Spacelift can orchestrate Pulumi stacks, Pulumi Cloud can store Terraform and OpenTofu state, a Pulumi program can install Crossplane into a cluster, and a FinOps tool such as CloudHealth reads spend no matter which tool provisioned the resources. The thing to avoid is two tools doing the same job, such as two orchestrators running the same stacks.

### Do you need Pulumi Cloud to use Pulumi?

No. The Pulumi CLI, engine, and SDKs are open source under Apache 2.0 and can store state in a self-managed backend such as S3, Azure Blob Storage, Google Cloud Storage, or PostgreSQL. Pulumi Cloud adds managed state, Pulumi ESC, deployments, Pulumi Policies, Pulumi Discovery, and Neo, with some features tied to the edition.

### What is the difference between an IaC engine and a governance tool?

An IaC engine such as Pulumi, Terraform, or OpenTofu defines resources, computes the changes, applies them, and records state. A governance or orchestration layer such as Spacelift, Scalr, env zero, HCP Terraform, or Pulumi Cloud decides who can run those changes, enforces policy, and detects drift. Discovery features such as Pulumi Discovery or env zero's Cloud Compass also find resources that no IaC manages.

### What are the best open source multi-cloud management tools?

Pulumi (SDK and engine), OpenTofu, Crossplane, and the core of Ansible are open source options. Pulumi uses general-purpose languages, OpenTofu uses HCL, Crossplane works through Kubernetes APIs, and Ansible handles configuration.

### Do open source tools need a paid layer in production?

Not always. Pulumi and OpenTofu run in production with self-managed state, and Crossplane runs in your own cluster. Teams usually add a commercial layer once several teams share infrastructure and need access controls, audit history, managed runs, or policy enforcement across stacks. Pulumi Cloud, HCP Terraform, Spacelift, Scalr, env zero, and Upbound all sell that layer.

### How do I control costs across multiple clouds?

Start with tagging and allocation standards enforced through policy as code, then add a FinOps tool such as CloudHealth or Flexera One for reporting and forecasting. Expiring environments in an orchestrator such as env zero stop forgotten test stacks from running up a bill. Provisioning tools help by making cost-relevant settings explicit and reviewable in code.

### Can AI agents manage multi-cloud infrastructure?

Yes, with guardrails. AI agents work best when infrastructure is defined in code they can read, preview, test, and check against policy before changes apply. Pulumi Neo, for example, proposes changes, runs previews, and opens pull requests for human approval. Keep approvals and policy checks in the loop.

### How hard is it to move workloads between clouds?

Moving the infrastructure definition is the easier part if you use components and avoid provider-specific coupling. Moving data and re-platforming managed services is harder because of egress fees and API differences. Plan workload moves in stages and test with non-critical environments first.

## Choosing a platform that fits your architecture

Many teams end up with a stack: one way to define infrastructure, plus orchestration, discovery, or cost tooling where their complexity sits. Choose the provisioning layer first, because every other layer reads its state, runs its plans, or reports on what it created. Revisit the rest when the estate changes, for example when an acquisition brings in a cloud you did not choose.

- Compare [Pulumi and Terraform](/docs/iac/comparisons/terraform/), [Pulumi and Crossplane](/docs/iac/comparisons/crossplane/), and [Pulumi and Spacelift](/docs/iac/comparisons/spacelift/).
- Read the wider [infrastructure as code tools guide](/blog/infrastructure-as-code-tools/) and the [best policy as code tools](/blog/best-policy-as-code-tools/).
- Browse providers in the [Pulumi Registry](/registry/).
- [Sign up for Pulumi](https://app.pulumi.com/signup) and deploy your first stack across two clouds.

---
title: "The Best Terraform Alternatives in 2026"
date: 2026-07-19
draft: false
meta_desc: "Terraform alternatives split into five real categories, not one ranked list. Here's how OpenTofu, Pulumi, AWS CDK, Crossplane, and others actually compare."
feature_image: feature.png
authors:
    - alex-leventer
tags:
    - infrastructure-as-code
    - terraform
    - platform-engineering
    - devops
category: general
faq_schema: true
---

"Terraform alternatives" isn't one question. A team leaving Terraform over the BSL license wants something different than a team that never liked HCL's limits as a programming model, and both want something different from a platform team that's really asking "how do we give every service team a paved path without writing bespoke Terraform modules forever." This guide splits Terraform alternatives into the five categories they actually fall into, so you can start with the one that matches why you're looking in the first place.

<!--more-->

## Why teams evaluate Terraform alternatives in 2026

Terraform earned its position honestly: it was the first infrastructure-as-code tool to treat "define infrastructure as a diffable, plannable artifact" as a first-class product, and a decade of provider development means it still covers more of the cloud than almost anything else. That's not going away, and any fair comparison has to start there. Terraform also isn't standing still — `terraform test` shipped as a first-class testing framework in 1.6 (October 2023), and HashiConf 2025 introduced Terraform Stacks for HCP Terraform customers who want native environment orchestration instead of hand-rolled workspace patterns.

What changed the conversation is HashiCorp's own trajectory. In August 2023, Terraform moved from the open-source Mozilla Public License 2.0 to the Business Source License (BSL) 1.1 — source-available, but no longer OSI-approved open source, and with restrictions on competing commercial use. IBM's acquisition of HashiCorp closed on February 27, 2025, folding Terraform into a much larger enterprise portfolio. Neither event breaks anything that's running today, but both are exactly the kind of governance shift that makes platform teams reassess a foundational dependency, the same way many did after similar moves elsewhere in the license-and-acquisition news cycle.

Layer on top of that a second, newer force: AI coding agents are now a normal part of how engineering teams ship software, and they are dramatically better at reasoning about, testing, and refactoring real programming languages than they are at generating correct HCL. That's less a Terraform-specific complaint than a structural one — any tool built on a bespoke configuration language faces the same ceiling as agentic workflows become standard.

## The five kinds of Terraform alternative

Most "Terraform alternatives" roundups list ten tools in an arbitrary order. That's not that useful, because the tools aren't interchangeable — they solve different problems. Here's the actual map:

| Category | What it solves | Examples |
|---|---|---|
| Drop-in HCL fork | Keep your `.tf` files and workflow, change the vendor and license | OpenTofu |
| General-purpose-language IaC | Write infrastructure in a real language with loops, tests, and packages | Pulumi, AWS CDK |
| Kubernetes-native control plane | Continuous reconciliation from inside a cluster, not a CLI apply | Crossplane |
| Managed run & collaboration platforms (TACOS) | Run and govern Terraform/OpenTofu itself, better | Spacelift, env0, Scalr, HCP Terraform |
| Cloud-vendor-native | Deep, single-cloud integration with no abstraction layer | AWS CloudFormation, Azure Bicep |

There's also a sixth honest answer, which is "you don't need a Terraform alternative at all" — configuration management tools like Ansible solve a genuinely different problem (imperative changes on existing hosts) and app-centric frameworks like SST solve a narrower one (deploying serverless apps quickly). Both come up constantly in these conversations, so they're worth naming even though they aren't drop-in replacements.

## 1. OpenTofu — the literal drop-in

**Best for:** teams that like their existing Terraform code and workflow and just want out from under the BSL.

OpenTofu is the Linux Foundation-governed fork of Terraform's last MPL-licensed release, built specifically to give the millions of lines of existing `.tf` configuration somewhere to go without a rewrite. It reads your state, understands your modules, and runs through mostly the same CLI muscle memory — migration is a state-file and tooling change, not a re-platforming project.

It's also no longer just "Terraform with a different name on the license." OpenTofu 1.7 shipped state encryption and provider-defined functions as OpenTofu-exclusive features, and the project has kept a steady release cadence since (1.12 shipped in May 2026), meaning the fork is now adding capability HashiCorp's Terraform doesn't have, not just patching around what it lost.

The honest trade-off: OpenTofu inherits HCL's ceiling along with everything else. If your actual complaint about Terraform was the configuration language rather than the license, OpenTofu solves the governance problem and leaves the modeling problem exactly where it was. (For a closer look at where the two forks diverge feature by feature, see our [OpenTofu vs. Terraform comparison](/docs/iac/comparisons/terraform/opentofu/).)

## 2. Pulumi — general-purpose languages, one engine

**Best for:** teams that want infrastructure defined in the same languages, IDEs, and test frameworks the rest of engineering already uses — and want an agentic path forward, not just a language swap.

Pulumi takes a different starting premise than either Terraform or OpenTofu: instead of a domain-specific language, you write infrastructure in TypeScript, Python, Go, C#, Java, or YAML, against the same state and provider model. That means real loops and conditionals instead of `count` and `for_each` workarounds, unit tests in whatever framework your team already runs, and packages you can publish and version through npm, PyPI, or NuGet instead of a bespoke module registry. Under the hood, most of Pulumi's providers are generated from the Terraform provider bridge, so day-one coverage of a given cloud API across the [Pulumi Registry](/registry/) — every major cloud plus a long tail of SaaS and community providers — is comparable rather than a gap you have to wait out.

The clearest expression of why the language choice matters now is [Neo](/product/neo/), Pulumi's infrastructure agent, which reached public preview in September 2025. Neo proposes changes, runs previews, checks them against policy, and opens pull requests — and it can do that fluently because it's reasoning about real Python or TypeScript, the same code an AI coding agent would be asked to review or extend anywhere else in your stack. That's the structural advantage of a general-purpose language: the same tooling ecosystem — linters, test runners, AI agents — works on your infrastructure code without anyone building a bespoke HCL-aware version first.

The honest trade-off: migrating from Terraform or OpenTofu means an actual rewrite, not a state-file swap, and Pulumi's ecosystem, while sizable, has less accumulated Stack Overflow and tutorial mass than Terraform's decade-plus head start. Teams that value "boring and proven" over "faster to extend" should weigh that.

## 3. AWS CDK — real languages, one cloud

**Best for:** AWS-only shops that want general-purpose languages but are comfortable staying inside AWS's own tooling.

AWS CDK lets you write CloudFormation stacks in TypeScript, Python, Java, or C#, synthesizing your code down to a CloudFormation template at deploy time. That gets you real language ergonomics — functions, tests, constructs you can share — while staying inside AWS's native deployment pipeline and support surface.

The synthesis step is also CDK's most-cited caveat: your actual deployment artifact is still a CloudFormation template, which means you inherit CloudFormation's deployment model, error messages, and troubleshooting patterns even though you never write YAML directly. And if your infrastructure spans more than one cloud, CDK doesn't help you there at all — it's an AWS tool, full stop. Worth flagging directly: CDK for Terraform (CDKTF), the sibling project that let you write CDK-style code against Terraform's provider ecosystem, was deprecated by HashiCorp in December 2025, which removes one of the multi-cloud, general-purpose-language paths that used to exist alongside plain CDK.

## 4. Crossplane — a control plane, not a CLI

**Best for:** platform teams that want infrastructure reconciled continuously from inside Kubernetes, not applied on a schedule from a CI job.

Crossplane extends the Kubernetes API itself so that cloud resources — an RDS instance, an S3 bucket, a whole VPC — become custom resources your cluster reconciles the same way it reconciles a Deployment. That's a genuinely different operating model from Terraform, OpenTofu, Pulumi, or CDK, all of which are fundamentally "run a command, get a diff, apply it." Crossplane's control loop notices drift and corrects it continuously, and it composes cleanly with the rest of a platform team's Kubernetes-native tooling — GitOps controllers, admission policies, the works.

The honest trade-off: that power comes with real platform-engineering lift. You're now running and maintaining a control plane, not just a CLI, and teams without existing Kubernetes operational maturity will feel that cost before they feel the benefit. It's the right answer for "we're building an internal platform on Kubernetes," and the wrong one for "we want infrastructure as code without adopting a new operational model."

## 5. Managed run platforms (TACOS) — better Terraform operations, not a new engine

**Best for:** teams whose actual pain is CI/CD plumbing, state locking, and approval workflows around Terraform or OpenTofu — not the language or engine itself.

Spacelift, env0, Scalr, and HashiCorp's own HCP Terraform are what the industry calls Terraform Automation and Collaboration Software (TACOS): managed run environments that wrap Terraform or OpenTofu with policy gates, drift detection, cost estimates, and role-based approvals, so platform teams don't have to hand-build that pipeline in Jenkins or GitHub Actions. Spacelift in particular is notable for supporting OpenTofu as a first-class runner alongside Terraform, letting teams switch the underlying engine without changing how they operate it.

The honest trade-off: none of these tools change what you write. If your infrastructure-as-code language is the actual source of friction — testing, reuse, agent readability — a better runner around Terraform doesn't solve that. It solves "our Terraform operations are ad hoc," which is a real and common problem, just a different one.

## 6. Cloud-vendor-native tools — deep, single-cloud

**Best for:** single-cloud teams that want the tightest possible integration with that one provider's console, support, and release cadence.

AWS CloudFormation and Azure Bicep are the cloud providers' own answers to infrastructure as code: YAML/JSON (CloudFormation) or a purpose-built DSL (Bicep), maintained by the same team that ships the underlying services, usually with same-day support for new resource types. For teams committed to a single cloud with no near-term multi-cloud plans, that tight coupling is a legitimate advantage, not a limitation.

The honest trade-off is the one everyone already expects: neither tool has any concept of a second cloud provider. The moment a second cloud enters the picture — even just for one workload — you're maintaining a second, unrelated infrastructure-as-code stack alongside the first.

## Two honest mentions: not drop-in, but worth naming

**Ansible** solves a different problem than any tool above: imperative configuration and orchestration on existing hosts, not declarative provisioning of new cloud resources. Plenty of teams run Ansible for configuration management *alongside* Terraform, OpenTofu, or Pulumi for provisioning — it's a complement, not really a competitor, and treating it as a Terraform replacement usually means someone is solving the wrong problem.

**SST** is an app-centric deployment framework for serverless applications on AWS, and it's worth a specific technical note: SST's current major version (Ion) is built on Pulumi's underlying engine. It's a good fit if your unit of infrastructure is "my serverless app," not "our cloud estate," and a poor fit for anything broader than that.

One more name that comes up in these conversations: Winglang generated attention as a general-purpose-language infrastructure tool, but its parent company, Monada, shut down in 2025, and the project now continues as a community-run effort. It's fine to know it exists — it's not a safe default for a team making an infrastructure bet in 2026.

## How to choose

Work backward from why you're actually looking, not from a feature checklist:

- **Leaving because of the license or acquisition, and happy with HCL?** OpenTofu is the direct path — same code, same workflow, different governance.
- **Want infrastructure in a real programming language, tested and reused like the rest of your software, with an agentic roadmap?** Pulumi (multi-cloud) or AWS CDK (AWS-only) are your general-purpose-language options.
- **Building an internal platform on Kubernetes, where continuous reconciliation matters more than a CLI apply?** Crossplane is the right operating model.
- **Your Terraform or OpenTofu code is fine, but your CI/CD, approvals, and drift detection around it are ad hoc?** A TACOS platform — Spacelift, env0, Scalr, or HCP Terraform — solves that without touching your code.
- **All-in on one cloud, no multi-cloud plans?** CloudFormation or Bicep give you the tightest native integration available.

## Frequently asked questions

### Is OpenTofu a drop-in replacement for Terraform?

For most configurations, yes. OpenTofu forked from Terraform's last MPL-licensed release and maintains compatibility with existing `.tf` files, state, and provider ecosystems, so migration is typically a tooling and CI change rather than a rewrite. Since the fork, OpenTofu has also added capabilities Terraform doesn't have, like state encryption.

### Is Terraform still open source?

No. HashiCorp moved Terraform from the open-source MPL 2.0 license to the Business Source License (BSL) 1.1 in August 2023. Terraform's source remains publicly viewable, but the BSL is not an OSI-approved open-source license and restricts certain competing commercial uses.

### What's the best Terraform alternative for a multi-cloud team?

Pulumi and OpenTofu are the two realistic multi-cloud options. Pulumi if you want a general-purpose programming language and an agentic workflow; OpenTofu if you want to keep your existing HCL and provider ecosystem and just change the license and vendor underneath it.

### Do I have to rewrite everything to migrate off Terraform?

It depends which alternative you pick. Moving to OpenTofu typically requires no code rewrite at all. Moving to a general-purpose-language tool like Pulumi or AWS CDK does require rewriting your infrastructure definitions, though most teams migrate incrementally, resource group by resource group, rather than all at once.

### What's the best Terraform alternative for a Kubernetes-native platform team?

Crossplane, if your team already operates Kubernetes with production maturity and wants cloud resources reconciled the same way as any other cluster resource. For teams that want infrastructure as code without adopting a new Kubernetes-based operating model, Pulumi or OpenTofu are a lower-lift starting point.

### Is Pulumi free?

Pulumi's open-source SDK and CLI are free and Apache-2.0 licensed. Pulumi Cloud, the managed state backend and collaboration layer, has a free tier for individuals and small teams, with paid tiers for organizations that need team management, policy as code, and premium capabilities like Neo.

## Where Pulumi fits

If the honest answer to "why are we looking" is "we want infrastructure defined the way the rest of our software already is — tested, reused, reviewed by the same AI tools our engineers use everywhere else" — that's the problem Pulumi was built to solve, and it's the direction the whole category is heading as agentic engineering becomes normal rather than novel. If your answer is "we like Terraform, we just want off the BSL," OpenTofu is the more honest recommendation, and we'd rather point you there than pretend otherwise.

Explore the [Pulumi vs. Terraform comparison](/docs/iac/comparisons/terraform/) for a detailed side-by-side, or start with the [Terraform migration guide](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/) if you're ready to try an incremental move.

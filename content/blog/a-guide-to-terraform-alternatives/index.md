---
title: "A Guide to Terraform Alternatives"
date: 2026-07-15
meta_desc: "A guide to the main Terraform alternatives, including OpenTofu, Pulumi, AWS CDK, and Crossplane, how to evaluate them, and how to migrate off Terraform."
feature_image: feature.png
authors:
    - alex-leventer
tags:
    - infrastructure-as-code
    - terraform
    - opentofu
    - pulumi
    - platform-engineering
category: general
schema_type: auto
---

Terraform has been a cornerstone of infrastructure as code for the better part of a decade, and for many teams it remains a great fit. Even so, more organizations are now taking a look at what else is out there, whether prompted by Terraform's 2023 move to the Business Source License, a preference for writing infrastructure in a general-purpose language, or a specific operational need. If you are running that kind of evaluation, the useful question is less about whether Terraform is good and more about which tool best fits your constraints, because the alternatives now span several distinct categories, each suited to a different situation.

## TL;DR

- The two biggest reasons teams evaluate a Terraform alternative are the 2023 license change (Terraform is no longer open source) and the limits of HCL as projects grow.
- The alternatives fall into four groups: drop-in forks (OpenTofu), general-purpose-language tools (Pulumi, AWS CDK), Kubernetes-native control planes (Crossplane), and single-cloud native tools (CloudFormation, Bicep).
- Evaluate on five criteria: language model, state and secrets handling, policy as code, licensing, and the migration path from your existing HCL.
- You rarely need a big-bang rewrite. Most alternatives support running alongside Terraform, importing live resources, or converting HCL automatically.

## Why teams look for a Terraform alternative

Two pressures drive most of these evaluations. The first is licensing. Since version 1.6, the Terraform CLI has shipped under the Business Source License 1.1 rather than an open source license, which matters to organizations with policies against depending on non-open-source tooling, and to vendors who build products on top of infrastructure tools. The second is the authoring experience. HCL is a configuration language, and it fits small projects cleanly, but its patterns for control flow, dynamic blocks, and reuse get harder to read as a codebase grows into hundreds of modules across many teams.

Beyond those two, a few operational frustrations recur: sensitive values sitting unencrypted in state files, a policy framework gated behind a commercial tier, and the general worry about lock-in that follows any acquisition. None of these makes Terraform a bad tool. They are simply the reasons a platform team starts a serious evaluation, and the reason the field of alternatives has gotten crowded enough to need a map.

## The main Terraform alternatives

It helps to sort the options by the problem they solve rather than listing them flat.

### OpenTofu

[OpenTofu](/docs/iac/comparisons/opentofu/) is the closest thing to a drop-in replacement. It is a fork of Terraform created after the license change, released under the open source MPL-2.0 license and maintained by the Linux Foundation. It reads the same HCL, uses the same providers, and behaves like the Terraform most teams already know. For an organization whose only concern is the license, OpenTofu is the lowest-friction move, because existing configurations and skills carry over almost unchanged. It has also started to diverge with its own features, such as client-side state encryption.

### General-purpose-language tools

A second group replaces HCL with real programming languages. Pulumi is the broad, multi-cloud option here: you author infrastructure in Python, TypeScript, Go, C#, Java, or YAML, and you get the loops, functions, classes, package managers, and IDE support those languages already provide. AWS CDK takes a similar language-first approach but compiles down to CloudFormation and targets AWS specifically. CDK for Terraform (CDKTF) lets you write in a programming language while still using the Terraform engine underneath. The trade in this group is expressiveness and testing against a steeper conceptual jump from static configuration.

### Kubernetes-native control planes

Crossplane represents a different model again. Instead of a CLI you run, it installs into a Kubernetes cluster and manages cloud resources through the Kubernetes API and continuous reconciliation. Teams that already run everything through Kubernetes and want infrastructure to follow the same control-plane pattern gravitate here, though it assumes a Kubernetes-centric operating model that not every team wants.

### Single-cloud native tools

Finally, each major cloud ships its own tool: AWS CloudFormation, Azure's Bicep and ARM templates, and Google Cloud's infrastructure manager. These give the deepest same-day integration with one provider at the cost of portability. They make sense when your scope is genuinely committed to a single cloud.

## How to evaluate a Terraform alternative

Once you know the categories, five criteria separate the options in practice.

**Language model.** Do you want to keep a configuration DSL (OpenTofu), or move to a general-purpose language (Pulumi, AWS CDK)? This is the single biggest fork in the road, because it shapes how you handle reuse, testing, and abstraction.

**State and secrets.** Look at where state lives, whether locking and history come built in, and how sensitive values are handled. Terraform does not encrypt values inside its state file, so it is worth checking whether an alternative treats secrets as first class.

**Policy as code.** If governance matters, check whether the policy engine is open source or gated behind a commercial tier, and which languages it accepts.

**Licensing.** If the license was your reason for looking, confirm the alternative's license actually meets your policy, and who governs the project.

**Migration path.** The most important practical question: can you adopt the tool incrementally, or does it demand a rewrite? Favor tools that read your existing state, import live resources, or convert HCL for you.

## A closer look at Pulumi

Because this guide sits on the Pulumi blog, it is worth being specific about where Pulumi fits against those criteria, and [Pulumi and Terraform compared in depth](/docs/iac/comparisons/terraform/) covers the full feature matrix.

On the language axis, Pulumi is squarely in the general-purpose-language group, which means [component resources](/docs/iac/concepts/components/), unit tests, and package managers come from the language rather than a bespoke module system. On state, Pulumi [manages state](/docs/iac/concepts/state-and-backends/) through Pulumi Cloud by default with locking and history, and supports self-managed S3, Azure Blob, and Google Cloud Storage backends. On secrets, it [encrypts secret values in state](/docs/iac/concepts/secrets/) by default with per-stack keys and pluggable KMS providers. On policy, [Pulumi Policies](/docs/insights/policy/) is open source under Apache 2.0 with rules in Python, TypeScript, or Rego. On licensing, the CLI and SDKs are Apache 2.0.

Two capabilities are worth calling out because they have no direct Terraform equivalent. The [Automation API](/docs/iac/concepts/automation-api/) is an embeddable SDK for driving deployments from inside another program, which is how teams build internal developer platforms and per-pull-request preview environments. And Pulumi can [adapt any Terraform provider](/docs/iac/concepts/providers/any-terraform-provider/), so moving tools does not mean losing access to a provider ecosystem. Teams have leaned on this at scale: [Starburst](/case-studies/starburst/) replaced Terraform and cut a deployment that took about two weeks down to roughly three hours, and [Wiz](/case-studies/wiz/) manages more than a million cloud resources through the Automation API. Those figures come from Pulumi's own customer case studies rather than independent benchmarks, and Terraform's longer incumbency still means a larger catalog of community modules today.

## Moving off Terraform without a big-bang rewrite

The evaluation is easier when adoption is incremental, and Pulumi supports several paths that can be combined. You can run both tools side by side and reference existing Terraform state, [use existing Terraform modules](/docs/iac/guides/building-extending/using-existing-tools/use-terraform-module/) directly, convert HCL with `pulumi convert --from terraform`, or bring already-provisioned resources under management with [`pulumi import`](/docs/iac/guides/migration/import/). Teams that want to keep running Terraform for now can even [store Terraform state in Pulumi Cloud](/docs/iac/get-started/terraform/terraform-state-backend/) to get encryption, history, and locking first. The full sequence is in the [migration guide](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/).

## Frequently asked questions

### What is the best open source alternative to Terraform?

It depends on how far you want to move. OpenTofu is the closest open source drop-in, since it reads the same HCL and uses the same providers under the Linux Foundation's governance. Pulumi is the open source option if you also want to leave HCL for a general-purpose language; its CLI and SDKs are Apache 2.0.

### Is Terraform still open source?

Not since version 1.6. The Terraform CLI is distributed under the Business Source License 1.1, which is a source-available license rather than an open source one. OpenTofu was created specifically to keep a Terraform-compatible tool under a genuine open source license.

### Do I have to rewrite my HCL to switch?

Usually not all at once. Depending on the alternative you can run it alongside Terraform, import live resources, or convert HCL automatically. With Pulumi, `pulumi convert --from terraform` translates existing configurations, and you can adopt incrementally rather than in a single cutover.

### How do I choose between OpenTofu and Pulumi?

Choose OpenTofu when your only goal is an open source Terraform that behaves identically and preserves your HCL and skills. Choose Pulumi when you also want to author infrastructure in a general-purpose language, encrypt secrets in state by default, and use open source policy as code.

## Where this leaves you

The right Terraform alternative is the one that matches the reason you started looking. If the license is the whole problem, OpenTofu keeps everything else the same. If HCL itself is the ceiling, a general-purpose-language tool like Pulumi changes how you write, test, and reuse infrastructure. Run the five criteria against your own constraints, insist on an incremental migration path, and the shortlist gets short quickly. When you are ready to try one hands-on, [get started with Pulumi](/docs/iac/get-started/) takes about ten minutes.

---
title_tag: "Pulumi vs. Terraform Automation and Collaboration Software (TACOS)"
authors: ["cam-soper"]
meta_desc: "Pulumi vs. Terraform Automation and Collaboration Software (TACOS): how Pulumi compares with Spacelift, HCP Terraform, env0, Scalr, and Atlantis."
title: TACOS
h1: Pulumi vs. Terraform Automation and Collaboration Software (TACOS)
menu:
    iac:
        name: TACOS
        parent: iac-comparisons
        weight: 35
    concepts:
        identifier: vs-tacos
        parent: vs
        weight: 75
aliases:
- /docs/reference/vs/tacos/
- /docs/intro/vs/tacos/
- /docs/concepts/vs/tacos/
- /docs/iac/concepts/vs/tacos/
---

[Terraform Automation and Collaboration Software](https://scalr.com/learning-center/tacos-terraform-automation-and-collaboration-software/) (TACOS) is the category of platforms that wrap automation, collaboration, and governance around Terraform. [HCP Terraform](https://www.hashicorp.com/products/terraform) (formerly Terraform Cloud), [Spacelift](https://spacelift.io/), [env0](https://www.env0.com/), [Scalr](https://scalr.com/), and the open-source [Atlantis](https://www.runatlantis.io/) all fall under it. They exist because Terraform on its own leaves you to assemble remote state, run automation, policy, drift detection, and access control yourself, and a TACOS bundles that scaffolding into one service.

Pulumi covers the same management ground from a different starting point. Rather than sitting on top of Terraform, Pulumi is a full infrastructure as code platform: you write infrastructure in a general-purpose language (Python, TypeScript, JavaScript, Go, C#, Java, or YAML) instead of HCL, and [Pulumi Cloud](/docs/iac/concepts/pulumi-cloud/) and [Pulumi Deployments](/docs/deployments/) provide the state, policy, RBAC, and Git-driven runs a TACOS is bought for. The decision between them comes down to the authoring layer: keep writing HCL and add a platform to manage it, or move to a platform where the language and the management are built together. This page compares the two approaches, shows where they overlap, and covers how teams run them side by side.

## What is Pulumi?

{{< what-is-pulumi >}}

If you're weighing a TACOS, the parts of Pulumi that line up with it are [Pulumi Cloud](/docs/iac/concepts/pulumi-cloud/) and [Pulumi Deployments](/docs/deployments/): managed state, role-based access control, policy, drift detection, and remote runs triggered from Git. What differs is what sits underneath — those features manage infrastructure you wrote as a Pulumi program, not HCL executed by a separate service.

## What are TACOS?

TACOS platforms turn Terraform into a managed, team-ready workflow. [Scalr](https://scalr.com/learning-center/tacos-terraform-automation-and-collaboration-software/), which helped coin the term, calls them CI/CD reimagined for infrastructure as code. In practice they give you remote state with locking, policy enforcement, drift detection, private module and provider registries, and per-scope access control — the operational pieces Terraform leaves you to build.

The tools don't all cover the same ground. [HCP Terraform](https://www.hashicorp.com/products/terraform) is HashiCorp's own service and runs Terraform. [Scalr](https://scalr.com/) and the open-source [Atlantis](https://www.runatlantis.io/) focus on Terraform and OpenTofu. [Spacelift](https://spacelift.io/) and [env0](https://www.env0.com/) reach wider: alongside Terraform and OpenTofu, both also run Pulumi, plus tools like CloudFormation and Kubernetes. That last detail matters here, because adopting Pulumi doesn't always mean leaving your TACOS behind.

## Detailed comparison

| Feature | Pulumi | TACOS |
| --- | --- | --- |
| Role in the stack | Full infrastructure as code platform: authors *and* manages infrastructure | A management and automation layer for Terraform, and for some tools other IaC as well |
| Authoring language | General-purpose languages — Python, TypeScript, JavaScript, Go, C#, Java — plus [YAML](/docs/iac/languages-sdks/yaml/) | HCL; the platform runs your Terraform, it doesn't change the language |
| IaC tools covered | Pulumi programs; consumes [any Terraform or OpenTofu provider](/docs/iac/concepts/providers/any-terraform-provider/) and can adopt existing state | Terraform and OpenTofu across the category; Spacelift and env0 also run Pulumi, CloudFormation, and Kubernetes, while Scalr and Atlantis stay Terraform- and OpenTofu-focused |
| State management | [Managed by Pulumi Cloud by default](/docs/iac/concepts/state-and-backends/); self-managed backends include Amazon S3, Azure Blob Storage, and Google Cloud Storage | Managed Terraform state with locking, a core feature across the category |
| Remote execution | [Pulumi Deployments](/docs/deployments/) for Git-driven runs; the [Automation API](/docs/iac/concepts/automation-api/); or the local CLI | Managed runs triggered by version control or pull requests, on hosted or self-hosted runners |
| Drift detection | [`pulumi refresh`](/docs/iac/cli/commands/pulumi_refresh/) and `pulumi preview --diff`; [scheduled detection and remediation](/docs/deployments/concepts/drift/) in Pulumi Deployments | Scheduled drift detection, common across the category |
| Policy as code | [Pulumi Policies](/docs/insights/policy/) in Python, TypeScript, or Open Policy Agent Rego; open source, with [compliance packs](/docs/insights/policy/policy-packs/pre-built-packs/) in Pulumi Cloud | Policy enforcement, usually Open Policy Agent Rego, or Sentinel on HCP Terraform |
| Secrets management | [First-class encrypted secrets](/docs/iac/concepts/secrets/) plus [Pulumi ESC](/docs/esc/) for centralized secrets and configuration | Encrypted variables, with integrations for external secret stores |
| Access control | [Pulumi Cloud](/docs/iac/concepts/pulumi-cloud/) teams, role-based access control, SSO/SAML, and audit logs | Per-scope RBAC and SSO/SAML, varying by vendor and tier |
| AI and agents | [Pulumi Neo](/product/neo/), the [Pulumi MCP server](/docs/ai/mcp-server/), and [Agent Skills](/docs/ai/skills/); author with any coding agent | Emerging and vendor-specific, such as [Spacelift Intelligence and Intent](https://spacelift.io/platform/intelligence) |
| Open source | Yes — CLI, SDKs, and providers under [Apache 2.0](https://github.com/pulumi/pulumi/blob/master/LICENSE) | Mixed — Atlantis is open source; HCP Terraform, Spacelift, env0, and Scalr are commercial |
| Commercial option | [Pulumi Cloud](/docs/iac/concepts/pulumi-cloud/) | Commercial across the category, aside from self-hosted Atlantis |

## Key differences

### The authoring layer is where they really differ

A TACOS doesn't change how you write infrastructure. You still author in HCL; the platform runs it, stores its state, and governs it. That's the point of the category — make Terraform manageable without changing Terraform. Pulumi differs a layer down: infrastructure is a program in a language you already use, so loops, conditionals, functions, real types, unit tests, IDE support, and package managers are all there, and you reach for them the way you would in application code. Comparing Pulumi to a TACOS is comparing a change of authoring model to a change of operations model. A Pulumi program can still use [any Terraform or OpenTofu provider](/docs/iac/concepts/providers/any-terraform-provider/), so moving off HCL doesn't cost you provider coverage.

### Where they overlap: the management layer

State, run automation, drift detection, policy, and access control appear on both sides. [Pulumi Cloud](/docs/iac/concepts/pulumi-cloud/) is the default state backend and adds RBAC, [policy](/docs/insights/policy/), and audit logs; [Pulumi Deployments](/docs/deployments/) runs infrastructure remotely from Git, with [review stacks](/docs/deployments/concepts/review-stacks/) per pull request, [scheduled runs](/docs/deployments/concepts/schedules/), and [drift detection with remediation](/docs/deployments/concepts/drift/). A TACOS offers a comparable set for Terraform. The structural difference is that a TACOS is a second system you run alongside Terraform, while Pulumi's management is part of the same platform that authors the infrastructure, so state, identity, and runs live in one place instead of two.

### Bringing your Terraform with you

Teams usually reach for a TACOS because they already have Terraform and need to operate it at scale. Pulumi can carry that investment forward rather than discarding it: it [uses existing Terraform modules](/docs/iac/guides/building-extending/using-existing-tools/use-terraform-module/), works with [any Terraform or OpenTofu provider](/docs/iac/concepts/providers/any-terraform-provider/), and [converts HCL](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/#converting-terraform-hcl-to-pulumi) with `pulumi convert --from terraform`. The question that leaves is whether your next step is more HCL with a platform layered on top, or a language-based platform that still consumes what you've already built.

### Running Pulumi on a TACOS

[Spacelift](https://docs.spacelift.io/vendors/pulumi/) and [env0](https://www.env0.com/) run Pulumi as a supported tool, so Pulumi and a TACOS aren't mutually exclusive. A team standardized on either platform can author in Pulumi and keep its existing run workflow, policies, and RBAC. Because the platform invokes the Pulumi CLI rather than replacing it, Pulumi's state still lives in Pulumi Cloud or a backend you configure. For teams that would rather not run a separate platform at all, Pulumi Cloud and Pulumi Deployments cover the same operational needs on their own.

### AI and agents

AI is arriving across the category. Spacelift has added [Intelligence and Intent](https://spacelift.io/platform/intelligence) for natural-language provisioning and a hosted MCP server, and other vendors are moving the same way. Pulumi approaches it from the authoring side: because infrastructure is code in general-purpose languages, the coding agents your team already uses — Claude Code, Cursor, Codex — can work with it through [Agent Skills](/docs/ai/skills/) and the [Pulumi MCP server](/docs/ai/mcp-server/), and [Pulumi Neo](/product/neo/) is a purpose-built infrastructure agent for deeper, governed automation. Use your own agent, use Neo, or use both.

## When to choose Pulumi vs. a TACOS

**Choose Pulumi when** you:

1. Want infrastructure in a general-purpose language, with the tests, package managers, and IDE tooling that come with it.
1. Want authoring and management in one platform, rather than Terraform plus a separate service to run it.
1. Are starting fresh, or are ready to modernize a Terraform estate while keeping its modules and providers.
1. Want to embed provisioning in your own software through the [Automation API](/docs/iac/concepts/automation-api/).

**Choose a TACOS when** you:

1. Are committed to Terraform or OpenTofu and want to keep authoring in HCL, adding automation and governance around it.
1. Need to run several IaC tools through one workflow — Spacelift and env0 span Terraform, OpenTofu, Pulumi, and more.
1. Want an open-source, pull-request-driven runner with no vendor relationship, which is where Atlantis fits.

**Use both when** you author in Pulumi but run a TACOS such as Spacelift or env0 as your orchestration layer.

## Adoption

You can adopt Pulumi alongside or in place of a TACOS in a few common ways, and they can be combined:

1. **Consolidate on Pulumi Cloud and Pulumi Deployments.** Author in Pulumi and use [Pulumi Deployments](/docs/deployments/) for remote runs, drift detection, review stacks, and Git-driven deploys, without operating a separate management platform.
1. **Run Pulumi on a TACOS that supports it.** If your team is standardized on [Spacelift](https://docs.spacelift.io/vendors/pulumi/) or [env0](https://www.env0.com/), author in Pulumi and orchestrate through the platform you already run, with state remaining in Pulumi Cloud or your own backend.
1. **Move a Terraform estate onto Pulumi.** [`pulumi convert --from terraform`](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/) translates HCL, [`pulumi import`](/docs/iac/guides/migration/import/) brings already-provisioned resources under management, and Pulumi [uses your existing Terraform modules](/docs/iac/guides/building-extending/using-existing-tools/use-terraform-module/) and providers so you can migrate incrementally.

## Frequently asked questions

### What does TACOS stand for?

Terraform Automation and Collaboration Software: the category of platforms — HCP Terraform, Spacelift, env0, Scalr, and Atlantis among them — that add run automation, remote state, policy, and collaboration around Terraform.

### Is Pulumi a TACOS?

Not quite. A TACOS manages Terraform, while Pulumi is a full infrastructure as code platform with its own authoring model and a built-in management layer. It overlaps with what a TACOS does through Pulumi Cloud and Pulumi Deployments, but you write programs rather than HCL run by a separate service.

### Can I use Pulumi with a TACOS?

Yes, with the ones that support it. Spacelift and env0 run Pulumi as a first-class tool, so you can author in Pulumi and keep your existing run and policy workflow. Scalr, Atlantis, and HCP Terraform are focused on Terraform and OpenTofu.

### Do I still need a TACOS if I adopt Pulumi?

Usually not. Pulumi Cloud and Pulumi Deployments provide the managed state, RBAC, policy, drift detection, and Git-driven runs a TACOS is bought for, as part of the same platform you author in.

### How do I move a Terraform estate onto Pulumi?

[`pulumi convert --from terraform`](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/) translates HCL into a Pulumi program, [`pulumi import`](/docs/iac/guides/migration/import/) brings existing resources under management, and Pulumi can [use your Terraform modules](/docs/iac/guides/building-extending/using-existing-tools/use-terraform-module/) and providers directly, so you can migrate a piece at a time. See [Migrating from Terraform to Pulumi](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/) for a walkthrough.

## Next steps

- [Get started with Pulumi](/docs/iac/get-started/)
- [Pulumi Cloud](/docs/iac/concepts/pulumi-cloud/)
- [Pulumi Deployments](/docs/deployments/)
- [Pulumi vs. Terraform](/docs/iac/comparisons/terraform/)

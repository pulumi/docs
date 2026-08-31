---
title_tag: "Pulumi vs. Terraform Automation and Collaboration Software (TACOS)"
faq_schema: true
authors: ["cam-soper"]
meta_desc: "Pulumi is a full infrastructure as code platform; TACOS tools like Spacelift, HCP Terraform, env0, and Scalr add a management layer to Terraform."
title: TACOS
h1: Pulumi vs. Terraform Automation and Collaboration Software (TACOS)
menu:
    iac:
        name: TACOS
        parent: iac-comparisons
        weight: 35
aliases:
- /docs/reference/vs/tacos/
- /docs/intro/vs/tacos/
- /docs/concepts/vs/tacos/
- /docs/iac/concepts/vs/tacos/
---

[Terraform Automation and Collaboration Software](https://scalr.com/learning-center/tacos-terraform-automation-and-collaboration-software/) (TACOS) is the category of platforms that wrap automation, collaboration, and governance around Terraform. [HCP Terraform](https://www.hashicorp.com/products/terraform) (formerly Terraform Cloud), [Spacelift](https://spacelift.io/), [env0](https://www.env0.com/), [Scalr](https://scalr.com/), and the open-source [Atlantis](https://www.runatlantis.io/) all fall under it. They exist because Terraform on its own leaves you to assemble remote state, run automation, policy, drift detection, and access control yourself, and a TACOS bundles that scaffolding into one service.

Pulumi covers the same management ground from a different starting point. Rather than sitting on top of Terraform, Pulumi is a full infrastructure as code platform: you write infrastructure in a general-purpose language ({{< pulumi-languages "general-purpose" >}}), in YAML, or in [HCL](/docs/iac/languages-sdks/hcl/), and [Pulumi Cloud](/docs/iac/concepts/pulumi-cloud/) and [Pulumi Deployments](/docs/deployments/) provide the state, policy, RBAC, and Git-driven runs a TACOS is bought for.

That used to be an either-or: keep writing HCL and add a platform to manage it, or move to a platform where the language and the management are built together. It isn't anymore. [Pulumi Cloud can hold your Terraform and OpenTofu state directly](/docs/iac/get-started/terraform/terraform-state-backend/), and [run the plans and applies](/docs/iac/get-started/terraform/terraform-remote-execution/) with approval gates on VCS-triggered applies, so you can adopt the management layer without touching the authoring layer — and change the authoring layer later, project by project, if you decide you want to. This page compares the two approaches, shows where they overlap, and covers how teams run them side by side.

## What is Pulumi?

{{< what-is-pulumi >}}

If you're weighing a TACOS, the parts of Pulumi that line up with it are [Pulumi Cloud](/docs/iac/concepts/pulumi-cloud/) and [Pulumi Deployments](/docs/deployments/): managed state, role-based access control, policy, drift detection, and remote runs triggered from Git. Those features manage infrastructure you wrote as a Pulumi program, and Pulumi Cloud additionally serves as a [state backend](/docs/iac/get-started/terraform/terraform-state-backend/) and [remote runner](/docs/iac/get-started/terraform/terraform-remote-execution/) for the Terraform and OpenTofu CLIs, which is the job a TACOS is most often bought to do.

## What are TACOS?

TACOS platforms turn Terraform into a managed, team-ready workflow. [Scalr](https://scalr.com/learning-center/tacos-terraform-automation-and-collaboration-software/), which helped coin the term, describes them as bringing CI/CD-style automation to infrastructure as code. In practice they give you remote state with locking, policy enforcement, drift detection, private module and provider registries, and per-scope access control — the operational pieces Terraform leaves you to build.

The tools don't all cover the same ground. [HCP Terraform](https://www.hashicorp.com/products/terraform) is HashiCorp's own service and runs Terraform. [Scalr](https://scalr.com/) and the open-source [Atlantis](https://www.runatlantis.io/) focus on Terraform and OpenTofu. [Spacelift](https://spacelift.io/) and [env0](https://www.env0.com/) reach wider: alongside Terraform and OpenTofu, both also run Pulumi, plus tools like CloudFormation and Kubernetes. That last detail matters here, because adopting Pulumi doesn't always mean leaving your TACOS behind.

## Detailed comparison

| Feature | Pulumi | TACOS |
| --- | --- | --- |
| Role in the stack | Full infrastructure as code platform: authors *and* manages infrastructure | A management and automation layer for Terraform, and for some tools other IaC as well |
| Authoring language | General-purpose languages — {{< pulumi-languages "general-purpose" >}} — plus [YAML](/docs/iac/languages-sdks/yaml/) and [HCL](/docs/iac/languages-sdks/hcl/), which runs valid Terraform and OpenTofu configurations with a [short list of documented exceptions](/docs/iac/languages-sdks/hcl/#terraform-compatibility) | HCL; the platform runs your Terraform, it doesn't change the language |
| IaC tools covered | Pulumi programs; consumes [any Terraform or OpenTofu provider](/docs/iac/concepts/providers/any-terraform-provider/) and [existing Terraform modules](/docs/iac/guides/building-extending/using-existing-tools/use-terraform-module/); runs HCL natively; and backs Terraform and OpenTofu state for CLI-driven workflows | Terraform and OpenTofu across the category; Spacelift and env0 also run Pulumi, CloudFormation, and Kubernetes, while Scalr and Atlantis stay Terraform- and OpenTofu-focused |
| State management | [Managed by Pulumi Cloud by default](/docs/iac/concepts/state-and-backends/); self-managed backends include Amazon S3, Azure Blob Storage, and Google Cloud Storage; Pulumi Cloud also [manages Terraform and OpenTofu state](/docs/iac/get-started/terraform/terraform-state-backend/) with locking, plus [remote execution](/docs/iac/get-started/terraform/terraform-remote-execution/) and approval gates | Managed Terraform state with locking, a core feature across the category |
| Remote execution | [Pulumi Deployments](/docs/deployments/) for Git-driven runs; the [Automation API](/docs/iac/concepts/automation-api/); or the local CLI | Managed runs triggered by version control or pull requests, on hosted or self-hosted runners |
| Drift detection | [`pulumi refresh`](/docs/iac/cli/commands/pulumi_refresh/) and `pulumi preview --diff`; [scheduled detection and remediation](/docs/deployments/concepts/drift/) in Pulumi Deployments | Scheduled drift detection, common across the category |
| Policy as code | [Pulumi Policies](/docs/insights/policy/) in Python, TypeScript, or Open Policy Agent Rego; open source, with [compliance packs](/docs/insights/policy/policy-packs/pre-built-packs/) in Pulumi Cloud | Policy enforcement with Open Policy Agent Rego, or Sentinel on HCP Terraform |
| Secrets management | [First-class encrypted secrets](/docs/iac/concepts/secrets/) plus [Pulumi ESC](/docs/esc/) for centralized secrets and configuration | Encrypted variables, with integrations for external secret stores |
| Access control | [Pulumi Cloud](/docs/iac/concepts/pulumi-cloud/) teams, role-based access control, SSO/SAML, and audit logs | Per-scope RBAC and SSO/SAML, varying by vendor and tier |
| AI and agents | [Pulumi Neo](/product/neo/), the [Pulumi MCP server](/docs/ai/mcp-server/), and [Agent Skills](/docs/ai/skills/); author with any coding agent | Emerging and vendor-specific, such as [Spacelift Intelligence and Intent](https://spacelift.io/platform/intelligence) |
| Open source | Yes — CLI, SDKs, and providers under [Apache 2.0](https://github.com/pulumi/pulumi/blob/master/LICENSE) | Mixed — Atlantis is open source; HCP Terraform, Spacelift, env0, and Scalr are commercial |
| Commercial option | [Pulumi Cloud](/docs/iac/concepts/pulumi-cloud/) | Commercial across the category, aside from self-hosted Atlantis |

## Key differences

### The authoring layer is where they really differ

A TACOS doesn't change how you write infrastructure. You still author in HCL; the platform runs it, stores its state, and governs it. That's the point of the category — make Terraform manageable without changing Terraform. Pulumi differs a layer down: infrastructure can be a program in a language you already use, so loops, conditionals, functions, real types, unit tests, IDE support, and package managers are all there, and you reach for them the way you would in application code. A Pulumi program can still use [any Terraform or OpenTofu provider](/docs/iac/concepts/providers/any-terraform-provider/), so moving off HCL doesn't cost you provider coverage.

The two changes are separable, though, which is what makes this comparison different from a straight either-or. Adopting Pulumi Cloud as your [Terraform state backend](/docs/iac/get-started/terraform/terraform-state-backend/) changes the operations model and leaves the authoring model alone — the same trade a TACOS offers. Adopting [Pulumi HCL](/docs/iac/languages-sdks/hcl/) moves your `.tf` files onto the Pulumi engine without changing their syntax. Rewriting a project in Python or Go is a third, independent step you can take when a team wants it, or never. A TACOS can only ever offer the first of those.

### Where they overlap: the management layer

State, run automation, drift detection, policy, and access control appear on both sides. [Pulumi Cloud](/docs/iac/concepts/pulumi-cloud/) is the default state backend and adds RBAC, [policy](/docs/insights/policy/), and audit logs; [Pulumi Deployments](/docs/deployments/) runs infrastructure remotely from Git, with [review stacks](/docs/deployments/concepts/review-stacks/) per pull request, [scheduled runs](/docs/deployments/concepts/schedules/), and [drift detection with remediation](/docs/deployments/concepts/drift/). A TACOS offers a comparable set for Terraform. The structural difference is that a TACOS is a second system you run alongside Terraform, while Pulumi's management is part of the same platform that authors the infrastructure, so state, identity, and runs live in one place instead of two.

### Bringing your Terraform with you

Teams reach for a TACOS because they already have Terraform and need to operate it at scale. Pulumi can carry that investment forward rather than discarding it, and the first step requires no code change at all: point Terraform or OpenTofu at [Pulumi Cloud as its state backend](/docs/iac/get-started/terraform/terraform-state-backend/) and you get managed state, locking, [remote execution](/docs/iac/get-started/terraform/terraform-remote-execution/), approval gates, RBAC, and policy enforcement, which is most of what you were buying a TACOS for. From there, Pulumi [runs HCL natively](/docs/iac/languages-sdks/hcl/), [uses existing Terraform modules](/docs/iac/guides/building-extending/using-existing-tools/use-terraform-module/), works with [any Terraform or OpenTofu provider](/docs/iac/concepts/providers/any-terraform-provider/), and [converts HCL](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/#converting-terraform-hcl-to-pulumi) with `pulumi convert --from terraform` when a team wants a general-purpose language.

### Running Pulumi on a TACOS

[Spacelift](https://docs.spacelift.io/vendors/pulumi/) and [env0](https://www.env0.com/) run Pulumi as a supported tool, so Pulumi and a TACOS aren't mutually exclusive. A team standardized on either platform can author in Pulumi and keep its existing run workflow, policies, and RBAC. Because the platform invokes the Pulumi CLI rather than replacing it, Pulumi's state still lives in Pulumi Cloud or a backend you configure. For teams that would rather not run a separate platform at all, Pulumi Cloud and Pulumi Deployments cover the same operational needs on their own.

### AI and agents

AI is arriving across the category. Spacelift has added [Intelligence and Intent](https://spacelift.io/platform/intelligence) for natural-language provisioning and a hosted [MCP server](https://docs.spacelift.io/integrations/api-development-with-mcp), and other vendors are moving the same way. Pulumi approaches it from the authoring side: because infrastructure is code in general-purpose languages, the coding agents your team already uses — Claude Code, Cursor, Codex — can work with it through [Agent Skills](/docs/ai/skills/) and the [Pulumi MCP server](/docs/ai/mcp-server/), and [Pulumi Neo](/product/neo/) is a purpose-built infrastructure agent for deeper, governed automation. Use your own agent, use Neo, or use both.

## When to use Pulumi or a TACOS

These aren't mutually exclusive. Pulumi authors infrastructure and manages it, so it works as a complete platform on its own. A TACOS adds an orchestration layer on top of your IaC, and because Spacelift and env0 run Pulumi, the two pair cleanly: author in Pulumi and orchestrate through the platform your team already runs.

**Lead with Pulumi when** you:

1. Want infrastructure in a general-purpose language, with the tests, package managers, and IDE tooling that come with it.
1. Want authoring and management in one platform, rather than one tool to write infrastructure and a separate service to run it.
1. Are starting fresh, or are ready to modernize a Terraform estate while keeping its modules and providers.
1. Want to embed provisioning in your own software through the [Automation API](/docs/iac/concepts/automation-api/).

**Reach for a TACOS alongside Pulumi when** you:

1. Run several IaC tools and want one orchestration plane across them — Spacelift and env0 run Pulumi next to Terraform, OpenTofu, and the rest.
1. Have already standardized on Spacelift or env0 and want to keep its run workflow, policies, and RBAC while authoring in Pulumi.

Staying in HCL is no longer a reason to wait. Pulumi Cloud can [back your Terraform state](/docs/iac/get-started/terraform/terraform-state-backend/) with no change to your configurations, [Pulumi HCL](/docs/iac/languages-sdks/hcl/) runs `.tf` files on the Pulumi engine as-is, and [adopting your existing Terraform](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/) with a general-purpose language stays available whenever you want it. Pulumi still runs on Spacelift or env0 if you'd rather keep a TACOS in the loop.

## Adoption

You can adopt Pulumi alongside or in place of a TACOS in a few common ways, and they can be combined:

1. **Keep Terraform, swap the management layer.** Point Terraform or OpenTofu at [Pulumi Cloud as its state backend](/docs/iac/get-started/terraform/terraform-state-backend/) by adding a standard `backend "remote"` block. Your code and workflow are unchanged, and you get managed state with locking, [remote plans and applies](/docs/iac/get-started/terraform/terraform-remote-execution/), approval gates, RBAC, policy enforcement, and Resource Search — without adding a second platform.
1. **Consolidate on Pulumi Cloud and Pulumi Deployments.** Author in Pulumi and use [Pulumi Deployments](/docs/deployments/) for remote runs, drift detection, review stacks, and Git-driven deploys, without operating a separate management platform.
1. **Run Pulumi on a TACOS that supports it.** If your team is standardized on [Spacelift](https://docs.spacelift.io/vendors/pulumi/) or [env0](https://www.env0.com/), author in Pulumi and orchestrate through the platform you already run, with state remaining in Pulumi Cloud or your own backend.
1. **Move a Terraform estate onto Pulumi.** [`pulumi convert --from terraform`](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/) translates HCL, [`pulumi import`](/docs/iac/guides/migration/import/) brings already-provisioned resources under management, and Pulumi [uses your existing Terraform modules](/docs/iac/guides/building-extending/using-existing-tools/use-terraform-module/) and providers so you can migrate incrementally.

## Frequently asked questions

### What does TACOS stand for?

Terraform Automation and Collaboration Software: the category of platforms — HCP Terraform, Spacelift, env0, Scalr, and Atlantis among them — that add run automation, remote state, policy, and collaboration around Terraform.

### Is Pulumi a TACOS?

Pulumi is a full infrastructure as code platform with its own authoring model and a built-in management layer, so it's a broader category than a TACOS. That said, Pulumi Cloud does now perform the core TACOS job for Terraform: it [manages Terraform and OpenTofu state](/docs/iac/get-started/terraform/terraform-state-backend/) with locking, [runs plans and applies remotely](/docs/iac/get-started/terraform/terraform-remote-execution/) with approval gates, and applies RBAC and policy to those stacks — while your team keeps using the Terraform or OpenTofu CLI. One difference to know about: drift detection requires a Pulumi program, so it doesn't apply to Terraform-managed stacks.

### Can I use Pulumi with a TACOS?

Yes, with the ones that support it. Spacelift and env0 run Pulumi as a first-class tool, so you can author in Pulumi and keep your existing run and policy workflow. Scalr, Atlantis, and HCP Terraform are focused on Terraform and OpenTofu.

### Do I still need a TACOS if I adopt Pulumi?

Not necessarily. Pulumi Cloud and Pulumi Deployments provide the managed state, RBAC, policy, drift detection, and Git-driven runs a TACOS is bought for, as part of the same platform you author in. Teams running several IaC tools may still want a TACOS to orchestrate all of them from one place.

### Can Pulumi Cloud replace my TACOS if I'm staying on Terraform?

Yes, for the state and run-management job. [Pulumi Cloud implements the Terraform remote backend API](/docs/iac/get-started/terraform/terraform-state-backend/), so Terraform and OpenTofu projects use it by adding a standard `backend "remote"` block, with no change to your resource code. You get managed state with locking, [remote plans and applies](/docs/iac/get-started/terraform/terraform-remote-execution/), approval gates on VCS-triggered applies, update history, RBAC, policy enforcement, and Resource Search across your estate. Drift detection is the gap — it needs a Pulumi program — and a TACOS still makes sense if you orchestrate more than one IaC tool from a single control plane.

### How do I move a Terraform estate onto Pulumi?

You can move as little or as much as you want. The smallest step changes no code: use [Pulumi Cloud as your Terraform state backend](/docs/iac/get-started/terraform/terraform-state-backend/). Beyond that, [Pulumi HCL](/docs/iac/languages-sdks/hcl/) runs your `.tf` files on the Pulumi engine, [`pulumi convert --from terraform`](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/) translates HCL into a Pulumi program in another language, [`pulumi import`](/docs/iac/guides/migration/import/) brings existing resources under management, and Pulumi can [use your Terraform modules](/docs/iac/guides/building-extending/using-existing-tools/use-terraform-module/) and providers directly. See [Migrating from Terraform to Pulumi](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/) for a walkthrough.

## Next steps

- [Get started with Pulumi](/docs/get-started/)
- [Pulumi Cloud](/docs/iac/concepts/pulumi-cloud/)
- [Pulumi Deployments](/docs/deployments/)
- [Using Pulumi Cloud as a Terraform state backend](/docs/iac/get-started/terraform/terraform-state-backend/)
- [Pulumi vs. Terraform](/docs/iac/comparisons/terraform/)
- [Pulumi vs. Terraform Cloud (HCP Terraform)](/docs/iac/comparisons/terraform-cloud/)
- [Pulumi vs. Spacelift](/docs/iac/comparisons/spacelift/)

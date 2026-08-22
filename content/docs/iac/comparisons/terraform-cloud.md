---
title_tag: "Best Terraform Cloud Alternative for Multi-Cloud Teams"
faq_schema: true
authors: ["pulumi-content-team"]
meta_desc: "The best Terraform Cloud alternative for large multi-cloud teams: Pulumi pairs real languages with one platform for policy, secrets, and AI."
title: Terraform Cloud
h1: "Pulumi vs. Terraform Cloud: The Best Alternative for Large Multi-Cloud Teams"
menu:
    iac:
        name: Terraform Cloud
        parent: iac-comparisons
        weight: 11
        identifier: iac-comparisons-terraform-cloud
---

Pulumi is the best Terraform Cloud (HCP Terraform) alternative for large, multi-cloud teams, and you can adopt it without rewriting anything. Pulumi Cloud is a drop-in backend for your existing Terraform and OpenTofu state, HCL runs as a first-class Pulumi language, and your existing Terraform modules import directly into programs written in any language. What you get in return is one unified platform where state, policy, secrets, estate visibility, and AI-assisted automation operate on the same resource graph under a single pool of Pulumi Credits, rather than an HCL runner metered by resource count with a separate secrets manager, policy engine, and inventory assembled around it.

## Why teams are re-evaluating HCP Terraform right now

Three changes to HCP Terraform are pushing platform teams to look at alternatives sooner than they'd planned.

First, HashiCorp has moved HCP Terraform's pricing model from a per-seat basis to Resources Under Management (RUM): what you pay now scales with the number of resources tracked in your state files, not the number of people using the product. For a large multi-cloud estate, where a single application can touch hundreds of subnets, security group rules, IAM bindings, and managed service instances across several providers, a resource-based cost model can climb quickly and unpredictably as the estate grows, even when headcount stays flat. <!-- verified: 2026-08 -->

Second, HashiCorp retired the legacy, user-based Free plan on March 31, 2026, automatically moving the organizations still on it to the enhanced Free tier introduced in 2023, which caps out at 500 managed resources. That's a workable ceiling for a small project, but it's nowhere near enough for a platform team managing infrastructure across a large multi-cloud estate, so teams already past that line are choosing between a paid plan and self-hosted Terraform Enterprise. <!-- verified: 2026-08 -->

Third, HashiCorp itself changed hands: IBM completed its acquisition of HashiCorp in February 2025. That's not inherently a red flag, but any time a core piece of infrastructure tooling changes ownership, it's a reasonable moment for a platform team to ask who is setting the roadmap for the tool their entire organization depends on, and to make sure their infrastructure investment isn't locked to a single vendor's proprietary language and commercial runner.

## Adopt Pulumi Cloud without leaving Terraform

Replacing HCP Terraform doesn't have to begin with a code change. Pulumi interoperates with Terraform and OpenTofu at the level of state, language, and modules, so you can move the pieces you want to move and leave the rest running unchanged.

### Pulumi Cloud as your Terraform state backend

Pulumi Cloud implements the Terraform remote backend API, so pointing an existing project at it means adding a standard `backend "remote"` block and nothing else. Your resource code is untouched. The [state backend guide](/docs/iac/get-started/terraform/terraform-state-backend/) covers migrating from HCP Terraform as well as from Amazon S3, Azure Blob Storage, Google Cloud Storage, and local files.

Stacks created through the Terraform or OpenTofu CLI [run plans and applies remotely](/docs/iac/get-started/terraform/terraform-remote-execution/) on Pulumi Cloud by default, matching the behavior your team already expects from HCP Terraform and Terraform Enterprise, with full visibility from both your local CLI and the Pulumi Cloud console. VCS-triggered applies pause after the plan and wait for manual approval, with **Confirm** and **Discard** in the console. Stacks that predate remote execution stay on local execution until you set the `terraform:execution-mode` stack tag to `remote`.

Stacks holding Terraform state are first-class entities in Pulumi Cloud, not read-only imports:

* Govern them with [tag-based access control and team and user role assignments](/docs/administration/access-identity/rbac/).
* Keep backend configuration in [Pulumi ESC](/docs/esc/), inject OIDC credentials at apply time, and expose Terraform root module outputs as stack outputs for downstream stacks and services.
* Run [preventative policies](/docs/insights/policy/) against a Terraform plan on remotely executed stacks, blocking an apply when a resource is non-compliant, and keep scanning with audit policies afterward.
* Get [Neo code reviews](/docs/ai/neo/code-reviews/) on Terraform and OpenTofu pull requests, informed by what Pulumi Cloud knows about the infrastructure you actually have running.
* Search every Terraform-managed resource in [Pulumi Insights](/docs/insights/) next to your Pulumi-managed ones.

### Keep writing HCL

[HCL is a first-class Pulumi language](/docs/iac/languages-sdks/hcl/). A project is a `Pulumi.yaml` with `runtime: hcl` alongside ordinary `.tf` files. Pulumi HCL runs valid Terraform and OpenTofu configurations, with a [short list of documented exceptions](/docs/iac/languages-sdks/hcl/#terraform-compatibility), so the code your team writes today runs on the Pulumi engine with access to the entire Pulumi provider ecosystem. It requires Pulumi CLI 3.256.0 or later and nothing else.

That matters for two groups: teams who prefer HCL and shouldn't have to trade it away to get a modern engine, and platform teams whose HCL projects and general-purpose-language projects need to share the same components.

### Reuse your Terraform modules

Pulumi programs in any language can [consume Terraform modules natively](/docs/iac/get-started/terraform/terraform-modules/) with `pulumi package add hcl module <source> [version]`, resolving from the Terraform Registry, a private registry, or a local path. The module itself doesn't change.

[Pulumi Cloud's registry also hosts your Terraform modules](/docs/idp/concepts/terraform-modules/) alongside Pulumi packages, so your teams have one place to look for reusable building blocks rather than two. The publish API is wire-compatible with HCP Terraform's private registry: point your existing go-tfe or `hashicorp/tfe` provider pipelines at `tf.pulumi.com`, supply a Pulumi access token, and they run unchanged. Every version you publish is also converted into a Pulumi package with typed inputs and outputs and a generated SDK, while your existing `.tf` consumers keep resolving the module over the Terraform protocol.

## Choosing a language, not being assigned one

Terraform's configuration language, HCL, works well for small, well-scoped projects. At the scale of a large multi-cloud organization, its limits start to show. HCL has no real classes, limited runtime logic, and reuse only through its module system, so teams end up copying and adapting modules rather than composing shared abstractions the way they would in a general-purpose language. Testing is a similar story: native HCL testing (`terraform test`) and policy checks in HCP Terraform (Sentinel or Open Policy Agent) are useful, but they sit alongside the configuration language rather than inside the same software engineering toolchain — the linters, type checkers, unit test frameworks, and package managers — that the rest of a large engineering organization already uses for application code.

The difference with Pulumi isn't that those constraints vanish the moment you switch. It's that they become a per-project decision you can revisit. A team that's productive in HCL keeps writing HCL, on the Pulumi engine. A team that wants classes, real test frameworks, and package management moves its project to Python, TypeScript, or Go. Both teams still share the same components, modules, state model, and policies. On HCP Terraform, HCL is the language for everyone: HashiCorp deprecated the Cloud Development Kit for Terraform in December 2025, so there is no longer a supported path to authoring in a general-purpose language.

Workspace organization has a similar shape. Because HCP Terraform organizes infrastructure into workspaces per environment or component, large multi-cloud estates tend to accumulate workspace sprawl and fragmented state that a platform team has to manually stitch back together to get a single picture of what's actually running.

## How Pulumi is different

Pulumi lets you define infrastructure in the same general-purpose languages your engineering organization already uses: {{< pulumi-languages "general-purpose" >}}, plus YAML for teams that prefer a markup format and [HCL](/docs/iac/languages-sdks/hcl/) for teams that want to keep the syntax they already know. Choosing a general-purpose language means real loops, conditionals, classes, and functions instead of a DSL's limited expressiveness; the testing frameworks, linters, and IDE tooling (autocomplete, type checking, go-to-definition) your teams already rely on for application code; and dependency management through the same package managers — npm, PyPI, NuGet, Maven, Go modules — your teams use everywhere else. Infrastructure code becomes software, reviewed, tested, and refactored the same way, rather than a separate discipline bolted onto the side of engineering.

That same language flexibility carries through to cloud coverage. Pulumi supports [200+ providers](/registry/) spanning AWS, Azure, Google Cloud, Kubernetes, and hundreds of SaaS platforms, including schema-generated native providers for [Kubernetes](/registry/packages/kubernetes/), [Azure Native](/registry/packages/azure-native/), [AWS Cloud Control](/registry/packages/aws-native/), and [Google Cloud Native](/registry/packages/google-native/) that ship support for new cloud APIs without waiting on a hand-authored release. For an organization running true multi-cloud, that means one platform, one state model, and one policy framework across every provider, rather than stitching together separate workspaces and separate governance for each cloud.

## One unified platform, not a pile of point tools

The most important difference for a large multi-cloud team isn't a single feature. It's that Pulumi Cloud is one platform where state, policy, secrets, estate visibility, and AI-assisted automation all operate on the same resource graph, instead of a managed HCL runner that platform teams then have to wire up to a separate secrets manager, a separate CMDB, and a separate policy engine. Because Terraform state stored in Pulumi Cloud feeds that same resource graph, everything below covers the Terraform you haven't converted, not only the Pulumi programs you've written.

[Pulumi Policies](/docs/insights/policy/) is Pulumi's policy as code framework: write governance rules in Python, TypeScript, or Open Policy Agent's Rego, and enforce them automatically on every `pulumi up`, with centralized management and reporting available on Pulumi Cloud's commercial plans. Because it's part of the same platform rather than a bolt-on product, a policy violation shows up in the same preview and the same audit trail as everything else your teams are already looking at.

[Pulumi ESC](/docs/esc/) (Environments, Secrets, and Configuration) centralizes secrets and configuration across your infrastructure and applications, so a large multi-cloud team isn't reconciling separate secrets stores per cloud or per team. [Pulumi Insights](/docs/insights/) gives that same team a single inventory of every cloud resource across every provider and account, regardless of how it was provisioned, with policy scanning layered on top so drift and non-compliant resources surface automatically rather than through a quarterly audit.

Pulumi's code-first model also means the AI coding agents your teams already use — Claude Code, Codex, Cursor, GitHub Copilot — can read, write, and reason about infrastructure directly, with [Agent Skills](/docs/ai/skills/) and the [Pulumi MCP server](/docs/ai/mcp-server/) giving them Pulumi-specific context. [Pulumi Neo](/docs/ai/), Pulumi's purpose-built infrastructure agent, goes further because it operates inside this same platform: it can scaffold a Terraform-to-Pulumi migration, run and interpret `pulumi preview` output, respond to failed updates, and review Terraform and OpenTofu pull requests against what Pulumi Cloud knows is actually running. Most teams get value from both.

## Proven at multi-cloud scale

Mercedes-Benz Research & Development adopted Pulumi specifically to unify application and infrastructure teams onto one platform, describing the result as taming the complexity of many teams working across many clouds. [Wiz](/case-studies/wiz/) uses Pulumi's Automation API to manage over one million cloud resources across thousands of Kubernetes clusters worldwide, handling hundreds of thousands of infrastructure updates daily. [BMW](/case-studies/bmw/)'s Software Factory manages 20,000-plus cloud resources with Python-based infrastructure code integrated directly into its existing CI/CD pipelines. [Supabase](/case-studies/supabase/) scaled from a single AWS region to 80,000 Pulumi-managed resources across 16 regions as its platform grew. [Atlassian](/case-studies/atlassian/) cut the time its team spends on infrastructure maintenance by half after adopting Pulumi for Bitbucket. And [Spear AI](/case-studies/spear-ai/) used Pulumi's built-in policy and compliance tooling to reach Authority to Operate six times faster, cutting an 18-month certification process down to three months.

## Pulumi vs. HCP Terraform, feature by feature

| | Pulumi | HCP Terraform |
| --- | --- | --- |
| Language | {{< pulumi-languages "general-purpose" >}}, plus YAML — general-purpose languages with native testing, IDE support, and package management — and [HCL](/docs/iac/languages-sdks/hcl/) via `runtime: hcl`, which runs valid Terraform and OpenTofu configurations with a [short list of documented exceptions](/docs/iac/languages-sdks/hcl/#terraform-compatibility) | HCL, a configuration-focused DSL; `terraform test` covers native unit testing, but reuse and abstraction are limited to the module system |
| Terraform and OpenTofu state | [Pulumi Cloud implements the Terraform remote backend API](/docs/iac/get-started/terraform/terraform-state-backend/) as a drop-in target, with [remote execution](/docs/iac/get-started/terraform/terraform-remote-execution/) and approval gates for VCS-triggered applies, alongside Pulumi's own state | Native, but state and runs are scoped to HCP Terraform workspaces |
| Modularity and reuse | [Component Resources](/docs/iac/concepts/components/) authored in any supported language; [Pulumi Packages](/docs/iac/concepts/packages/) let a component written in one language be consumed from any Pulumi language; native language package managers (npm, PyPI, NuGet, Maven, Go modules); and the [Pulumi Registry](/registry/) for publicly available packages; plus existing Terraform modules pulled in directly with [`pulumi package add hcl module`](/docs/iac/get-started/terraform/terraform-modules/) and [hosted in Pulumi Cloud's registry](/docs/idp/concepts/terraform-modules/) via an HCP-compatible publish API | Modules published to the Terraform Registry or a private registry, resolvable only from Terraform and OpenTofu configurations |
| Pricing model | Pulumi Credits are one currency across IaC, secrets, estate visibility, workflows, and AI usage, so a single credit pool covers the whole platform rather than a separate meter per product; the Team edition starts at $40/month with 40 included Credits and 500 included resources, and additional IaC resources are billed at $0.00025 per resource-hour ($0.1825/month) | Resources Under Management (RUM)---billed by the count of resources tracked in state, in addition to plan tier |
| Free tier | Individual tier is free with no resource cap for personal use | Enhanced Free tier caps out at 500 managed resources per organization |
| Policy as code | [Pulumi Policies](/docs/insights/policy/), written in Python, TypeScript, or OPA Rego, enforced on every `pulumi up` and — for [remotely executed](/docs/iac/get-started/terraform/terraform-remote-execution/) Terraform stacks — against Terraform plans, as part of the same platform | Sentinel or OPA policy checks, run as a distinct step in the HCP Terraform run pipeline |
| Secrets and configuration | [Pulumi ESC](/docs/esc/) centralizes secrets and config across infrastructure and applications | Workspace variables plus a separate HashiCorp Vault integration for centralized secrets |
| Estate visibility | [Pulumi Insights](/docs/insights/) inventories every resource across every provider, however it was provisioned, including resources in Terraform-backed stacks | No equivalent; visibility is scoped to what's tracked in HCP Terraform workspaces |
| AI and agent readiness | [Pulumi Neo](/docs/ai/) and general-purpose AI coding agents operate directly on real, familiar code | Agents must generate and reason about HCL, a narrower and less common training target |
| Multi-cloud coverage | 200+ providers, one state model, one policy framework across every cloud | Large, mature provider ecosystem; state and policy are scoped per workspace, so multi-cloud governance is assembled by the platform team |
| Migration path | Point Terraform at Pulumi Cloud as its backend and change no code, or bring existing HCL and already-provisioned resources under Pulumi management incrementally with `pulumi convert` and `pulumi import` | N/A |
| Ecosystem maturity | Fast-growing registry, with any existing Terraform provider or module usable from Pulumi | The largest and most mature IaC provider and module ecosystem in the industry today |

Terraform's ecosystem maturity and community size are real advantages, and they're worth naming plainly: more public modules exist for Terraform than for any single alternative, Pulumi included. Pulumi closes that gap by adapting [any existing Terraform provider](/docs/iac/concepts/providers/any-terraform-provider/) into a Pulumi provider and by letting Pulumi programs [consume existing Terraform modules directly](/docs/iac/get-started/terraform/terraform-modules/), so adopting Pulumi doesn't mean starting the provider and module ecosystem over from zero. It's the same ecosystem, reachable from more languages.

## Moving off HCP Terraform, at your own pace

Leaving HCP Terraform is not a single decision, and none of these steps require the ones after it. In roughly ascending order of effort:

1. **Swap the backend.** Point Terraform at [Pulumi Cloud as its state backend](/docs/iac/get-started/terraform/terraform-state-backend/) and change nothing else. Your code, workflow, and CLI stay the same.
1. **Reuse what you've built.** Bring your existing [Terraform modules](/docs/iac/get-started/terraform/terraform-modules/) into new Pulumi projects instead of rewriting them, and [move your private module registry](/docs/idp/concepts/terraform-modules/) by repointing your publish pipelines at `tf.pulumi.com`.
1. **Write new projects in HCL.** Use [Pulumi HCL](/docs/iac/languages-sdks/hcl/) to get the Pulumi engine and ecosystem without changing the syntax your team writes.
1. **Convert when a team wants a general-purpose language.** [`pulumi convert --from terraform`](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/) translates existing HCL into Pulumi programs in your language of choice as a starting point for review, and [`pulumi import`](/docs/iac/guides/migration/import/) brings already-provisioned resources under Pulumi management without recreating them.
1. **Coexist for as long as you need.** Pulumi can reference an existing `.tfstate` file, so both tools run side by side during a gradual cutover, with Neo available to help scaffold conversions and interpret the resulting `pulumi preview` output.

## Frequently asked questions

### Can I use Pulumi Cloud as my Terraform state backend without changing my code?

Yes. Pulumi Cloud implements the Terraform remote backend API, so you add a standard `backend "remote"` block and your resource code stays as it is. Stacks created through the CLI [run plans and applies on Pulumi Cloud](/docs/iac/get-started/terraform/terraform-remote-execution/) by default, VCS-triggered applies wait for manual approval, and the resulting stack gets RBAC, policy enforcement, audit history, and Resource Search like any other Pulumi Cloud stack. See [Using Pulumi Cloud as a Terraform state backend](/docs/iac/get-started/terraform/terraform-state-backend/).

### Can I keep writing HCL with Pulumi?

Yes. [HCL is a first-class Pulumi language](/docs/iac/languages-sdks/hcl/): set `runtime: hcl` in `Pulumi.yaml` and write ordinary `.tf` files. Pulumi HCL runs valid Terraform and OpenTofu configurations, with a [short list of documented exceptions](/docs/iac/languages-sdks/hcl/#terraform-compatibility), and it has the same access to Pulumi's provider ecosystem as any other language.

### Can I use my existing Terraform modules in Pulumi?

Yes, without modifying them. `pulumi package add hcl module <source> [version]` makes a module available to a Pulumi program in any language, resolving from the Terraform Registry, a private registry, or a local path. See [Using Terraform modules in Pulumi](/docs/iac/get-started/terraform/terraform-modules/).

You can also [host your own modules in the Pulumi Cloud registry](/docs/idp/concepts/terraform-modules/). Its publish API is wire-compatible with HCP Terraform's, so existing go-tfe or `hashicorp/tfe` provider pipelines migrate by changing the host to `tf.pulumi.com`. Published modules stay usable from both Pulumi and Terraform programs.

### Is HCP Terraform (Terraform Cloud) still free?

HCP Terraform's enhanced Free tier remains available, but it's capped at 500 managed resources per organization; the legacy user-based Free plan reached end of life on March 31, 2026. <!-- verified: 2026-08 --> For a large multi-cloud estate, that ceiling is typically reached well before the team's infrastructure footprint stabilizes, which forces a move to a paid, resource-metered plan.

### How does Pulumi's pricing compare to HCP Terraform's Resources Under Management model?

HCP Terraform bills primarily by Resources Under Management, so cost rises directly with the size of your infrastructure footprint, and that's the only meter running. Pulumi Cloud also has on-demand resource pricing beyond its included allotment, but that allotment sits inside one credit pool that covers IaC state, secrets, estate visibility, and AI usage together, so a large multi-cloud estate is buying one consolidated capability rather than paying separately for a policy engine, a secrets vault, and a resource inventory on top of its Terraform runner.

### How do I migrate my existing Terraform state and code to Pulumi?

Three options, usable independently or together: convert HCL to a Pulumi program with `pulumi convert --from terraform`, bring already-provisioned resources under Pulumi management with `pulumi import`, or reference your existing Terraform state directly from Pulumi and run both tools side by side until you're ready to cut over. See the [migration guide](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/) for the full walkthrough.

### Can Pulumi manage multiple clouds in a single project?

Yes. Pulumi supports [200+ providers](/registry/) across AWS, Azure, Google Cloud, Kubernetes, and hundreds of SaaS platforms from the same program, in the same state, under the same policy framework, which is what large organizations with genuinely multi-cloud estates use it for today.

### Does Pulumi work with AI coding agents?

Yes, in two ways. General-purpose AI coding agents like Claude Code, Codex, and Cursor already understand Pulumi's real programming languages, so they can read, write, and reason about your infrastructure code directly. Pulumi also offers [Neo](/docs/ai/), a purpose-built infrastructure agent that runs previews, responds to failures, and opens pull requests inside your existing workflows.

### Do I have to rewrite everything to switch from Terraform Cloud to Pulumi?

No, and you don't have to rewrite anything to start. The smallest possible move is pointing Terraform at [Pulumi Cloud as its state backend](/docs/iac/get-started/terraform/terraform-state-backend/), which leaves your code and workflow untouched. From there you can reuse your Terraform modules, write new projects in HCL on the Pulumi engine, or convert HCL with `pulumi convert` and adopt existing resources with `pulumi import` when a team wants a general-purpose language.

## Next steps

* [Best Terraform Cloud Alternative for Large Multi-Cloud Teams](/blog/best-terraform-cloud-alternative/) --- a broader comparison against HCP Terraform, Spacelift, env0, and Scalr
* [Get started with Pulumi](/docs/get-started/)
* [Using Pulumi Cloud as a Terraform state backend](/docs/iac/get-started/terraform/terraform-state-backend/)
* [Using Terraform modules in Pulumi](/docs/iac/get-started/terraform/terraform-modules/)
* [Terraform modules in the Pulumi Cloud registry](/docs/idp/concepts/terraform-modules/)
* [Writing Pulumi programs in HCL](/docs/iac/languages-sdks/hcl/)
* [Migrating from Terraform to Pulumi](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/)
* [Pulumi vs. Terraform](/docs/iac/comparisons/terraform/)
* [Pulumi vs. OpenTofu](/docs/iac/comparisons/opentofu/)

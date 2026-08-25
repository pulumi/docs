---
title_tag: "Pulumi vs. Spacelift"
faq_schema: true
authors: ["cam-soper"]
meta_desc: "Pulumi vs. Spacelift: Pulumi is an infrastructure as code platform; Spacelift is a CI/CD orchestration platform that runs IaC tools, including Pulumi."
title: Spacelift
h1: Pulumi vs. Spacelift
menu:
    iac:
        name: Spacelift
        parent: iac-comparisons
        weight: 35
    concepts:
        identifier: vs-spacelift
        parent: vs
        weight: 75
aliases:
- /docs/reference/vs/spacelift/
- /docs/intro/vs/spacelift/
- /docs/concepts/vs/spacelift/
- /docs/iac/concepts/vs/spacelift/
---

Pulumi and [Spacelift](https://spacelift.io/) sit at different layers of the infrastructure stack. Pulumi is an infrastructure as code platform: you define infrastructure in general-purpose languages ({{< pulumi-languages "general-purpose" >}}), plus YAML and [HCL](/docs/iac/languages-sdks/hcl/), and [Pulumi Cloud](/docs/iac/concepts/pulumi-cloud/) and [Pulumi Deployments](/docs/deployments/) manage state, enforce policy, and run deployments. Spacelift is a CI/CD and orchestration platform for infrastructure as code: it doesn't author infrastructure itself, but runs and manages the IaC tools you already use — including Pulumi, Terraform, OpenTofu, CloudFormation, Ansible, and Kubernetes — from a single control plane.

Because Spacelift runs Pulumi as a first-class runtime, the two are frequently used together. Where they genuinely overlap is the management layer: Spacelift's orchestration, policy, and collaboration features cover much the same ground as Pulumi Cloud and Pulumi Deployments. This page covers what each tool is, a feature-by-feature comparison, the key differences in detail, and how Pulumi and Spacelift work together.

## What is Pulumi?

{{< what-is-pulumi >}}

For teams coming from Spacelift, the closest points of comparison are [Pulumi Cloud](/docs/iac/concepts/pulumi-cloud/) and [Pulumi Deployments](/docs/deployments/). Together they provide managed state, role-based access control, policy enforcement, drift detection, and remote, Git-driven runs, forming a management layer built for infrastructure you author with Pulumi. Pulumi's engine is open source and runs anywhere, so you can also drive it from any CI/CD system, Spacelift included.

## What is Spacelift?

[Spacelift](https://spacelift.io/) is a commercial CI/CD and orchestration platform for infrastructure as code. It runs the IaC tools you already use and wraps a management layer around them: version-control integration, policy enforcement, access control, and continuous drift detection. Spacelift supports [Terraform, OpenTofu, Terragrunt, Pulumi, AWS CloudFormation, Kubernetes, and Ansible](https://docs.spacelift.io/) as run backends, so an organization can manage a heterogeneous mix of tools from one control plane.

Work in Spacelift is organized into [stacks](https://docs.spacelift.io/concepts/stack/) — each a combination of source code, state, and configuration tied to a Git repository — that execute runs when changes are pushed. Runs execute on [worker pools](https://docs.spacelift.io/concepts/worker-pools): a public pool hosted by Spacelift, or private workers you operate in your own cloud account for tighter control over credentials and network access. Governance is handled through [policies](https://docs.spacelift.io/concepts/policy/) written in [Open Policy Agent's](https://www.openpolicyagent.org/) Rego language, which Spacelift evaluates at distinct decision points across a run's lifecycle, from login and stack access to plan approval and notification routing.

Spacelift is proprietary software, though it's built on open-source components such as Open Policy Agent and Docker. It's delivered primarily as a hosted SaaS product, with self-hosted and airgapped options on its highest tier. [Pricing](https://spacelift.io/pricing) starts with a free tier of two users and one public worker, then moves up through annual subscription plans for larger teams.

## Detailed comparison

| Feature | Pulumi | Spacelift |
| --- | --- | --- |
| Role in the stack | Infrastructure as code platform: authors *and* manages infrastructure | Orchestration and CI/CD platform: runs and manages IaC that you author with another tool |
| Infrastructure authoring | General-purpose languages — {{< pulumi-languages "general-purpose" >}} — plus [YAML](/docs/iac/languages-sdks/yaml/) and [HCL](/docs/iac/languages-sdks/hcl/) | None of its own; you bring your existing tool (Terraform, OpenTofu, Pulumi, CloudFormation, Ansible, or Kubernetes) |
| IaC tools it works with | Runs Pulumi programs; consumes [any Terraform or OpenTofu provider](/docs/iac/concepts/providers/any-terraform-provider/) and [existing Terraform modules](/docs/iac/guides/building-extending/using-existing-tools/use-terraform-module/); runs HCL natively; and can [hold Terraform or OpenTofu state](/docs/iac/get-started/terraform/terraform-state-backend/) for CLI-driven workflows | Orchestrates [Terraform, OpenTofu, Terragrunt, Pulumi, CloudFormation, Kubernetes, and Ansible](https://docs.spacelift.io/) |
| State management | [Managed by Pulumi Cloud by default](/docs/iac/concepts/state-and-backends/); self-managed backends include Amazon S3, Azure Blob Storage, and Google Cloud Storage; Pulumi Cloud also [manages Terraform and OpenTofu state](/docs/iac/get-started/terraform/terraform-state-backend/), with [remote execution](/docs/iac/get-started/terraform/terraform-remote-execution/) and approval gates on VCS-triggered applies | Managed state backend for Terraform and OpenTofu; for Pulumi you configure your own backend, which Spacelift connects to with `pulumi login` |
| Remote execution | [Pulumi Deployments](/docs/deployments/) for remote, Git-driven runs; the [Automation API](/docs/iac/concepts/automation-api/); or the local CLI | Runs on [public or private worker pools](https://docs.spacelift.io/concepts/worker-pools), triggered by version-control events or the API |
| Drift detection | [`pulumi refresh`](/docs/iac/cli/commands/pulumi_refresh/) and `pulumi preview --diff`; [scheduled drift detection and remediation](/docs/deployments/concepts/drift/) in Pulumi Deployments | [Scheduled drift detection](https://docs.spacelift.io/concepts/stack/drift-detection) with optional reconciliation (requires private workers and a paid plan) |
| Policy as code | [Pulumi Policies](/docs/insights/policy/) in Python, TypeScript, or Open Policy Agent Rego; open source, with centralized management and [compliance packs](/docs/insights/policy/policy-packs/pre-built-packs/) in Pulumi Cloud | [Rego policies](https://docs.spacelift.io/concepts/policy/) evaluated at multiple decision points — login, access, approval, plan, push, trigger, and notification |
| Secrets management | [First-class encrypted secrets](/docs/iac/concepts/secrets/) in state, plus [Pulumi ESC](/docs/esc/) for centralized secrets and configuration | Encrypted environment variables, mounted files, and reusable contexts for configuration and credentials |
| Access control | [Pulumi Cloud](/docs/iac/concepts/pulumi-cloud/) teams and role-based access control, SAML/SSO, and [audit logs](/docs/administration/concepts/audit-logs/) | Spaces plus login and access policies; SSO/SAML on higher tiers |
| Version control | [GitHub, GitLab, Azure DevOps, and Bitbucket](/docs/deployments/concepts/review-stacks/) | GitHub, GitLab, Bitbucket, and Azure DevOps |
| Programmatic API | [Automation API](/docs/iac/concepts/automation-api/) to embed provisioning in your own application or platform | GraphQL API and `spacectl` CLI; a Terraform/OpenTofu provider for managing Spacelift itself |
| Execution location | Local CLI anywhere; managed Pulumi Deployments runners or [self-hosted runners](/docs/deployments/concepts/customer-managed-runners/) | Public workers hosted by Spacelift, or private workers in your own environment; fully self-hosted on the top tier |
| Open source | Yes — CLI, SDKs, and providers under [Apache 2.0](https://github.com/pulumi/pulumi/blob/master/LICENSE) | No — proprietary, built on open-source components such as Open Policy Agent and Docker |
| Commercial option | [Pulumi Cloud](/docs/iac/concepts/pulumi-cloud/) | Commercial only, from a free tier up to enterprise plans |

## Key differences

### Two layers: an infrastructure as code platform and an orchestration platform

Pulumi and Spacelift come at infrastructure from opposite ends. Pulumi is an infrastructure as code platform: it's where infrastructure is *authored*, in a general-purpose language, and it ships with a management layer — Pulumi Cloud and Pulumi Deployments — for state, policy, access control, and remote runs. Spacelift's core job is orchestration: it runs infrastructure you've written in another tool and adds governance and collaboration on top. In the landscape of infrastructure tooling, Spacelift sits alongside offerings like Terraform Cloud: a management plane for infrastructure code more than the code itself.

A like-for-like comparison, then, is less "Pulumi vs. Spacelift" than "Pulumi Cloud and Pulumi Deployments vs. Spacelift." And because Spacelift runs Pulumi as one of its supported tools, the most common outcome is teams using them together, authoring with Pulumi and orchestrating with Spacelift.

### Infrastructure authoring and language support

Pulumi programs are written in general-purpose languages, so you get loops, conditionals, classes, package management, IDE support, and the testing frameworks that already exist in those ecosystems, along with [YAML](/docs/iac/languages-sdks/yaml/) for teams who prefer a markup format. Spacelift has no authoring model of its own; what you write depends on the tool you run on it. If that tool is Terraform, you write HCL; if it's Pulumi, you write a Pulumi program and keep every one of Pulumi's language features. When the question is really about how infrastructure is expressed, then, the comparison is between Pulumi and whichever tool you'd otherwise run, not between Pulumi and Spacelift, which is happy to run Pulumi.

Worth noting for teams running HCL on Spacelift: choosing Pulumi doesn't mean choosing against HCL. [Pulumi HCL](/docs/iac/languages-sdks/hcl/) is a first-class Pulumi language that runs valid Terraform HCL, with a [short list of documented exceptions](/docs/iac/languages-sdks/hcl/#terraform-compatibility), so an existing HCL codebase can move onto the Pulumi engine without a rewrite, and teams can adopt a general-purpose language later, project by project, if they want one.

### Execution model, GitOps, and drift

Both platforms give you managed, Git-driven runs, and they reach a similar experience from opposite directions. Spacelift is built around version control: a push opens a [proposed run](https://docs.spacelift.io/concepts/run/proposed) that previews changes on a pull request, and a merge triggers a [tracked run](https://docs.spacelift.io/concepts/run/tracked) that applies them, all executed on public or private [worker pools](https://docs.spacelift.io/concepts/worker-pools). [Pulumi Deployments](/docs/deployments/) offers the same shape for Pulumi specifically: remote runs triggered by Git, [review stacks](/docs/deployments/concepts/review-stacks/) that stand up an ephemeral environment per pull request, [scheduled deployments](/docs/deployments/concepts/schedules/), and [time-to-live stacks](/docs/deployments/concepts/ttl/), all running on Pulumi-hosted or [self-hosted runners](/docs/deployments/concepts/customer-managed-runners/). Both detect drift on a schedule and can remediate it: [Pulumi Deployments](/docs/deployments/concepts/drift/) and [Spacelift](https://docs.spacelift.io/concepts/stack/drift-detection) each run a periodic check and, where configured, open a run to reconcile. The practical difference is scope. Pulumi Deployments is purpose-built for Pulumi, while Spacelift applies one execution model across every tool it supports.

### State and secrets

Pulumi manages [state in Pulumi Cloud](/docs/iac/concepts/state-and-backends/) by default, or in a self-managed backend such as Amazon S3, Azure Blob Storage, or Google Cloud Storage, and it treats [secrets as a first-class primitive](/docs/iac/concepts/secrets/): values marked secret are encrypted in transit and at rest, with per-stack encryption keys and pluggable KMS providers. [Pulumi ESC](/docs/esc/) extends this into centralized secrets and configuration shared across stacks and environments.

Spacelift provides a managed state backend too, but only for Terraform and OpenTofu. For Pulumi, Spacelift runs `pulumi login` against a backend you configure, which means your Pulumi state still lives in Pulumi Cloud or your own self-managed backend even when Spacelift orchestrates the run. Spacelift secures its own configuration and credentials with encrypted environment variables and contexts. The upshot is that adopting Spacelift for orchestration doesn't move your Pulumi state off Pulumi's backends; the two responsibilities stay cleanly separated.

That relationship is no longer one-directional. [Pulumi Cloud now manages Terraform and OpenTofu state](/docs/iac/get-started/terraform/terraform-state-backend/) as well, implementing the same remote backend API those CLIs speak, with [remote execution](/docs/iac/get-started/terraform/terraform-remote-execution/), approval gates on VCS-triggered applies, RBAC, and policy enforcement. A team using Spacelift primarily as a managed state backend and runner for Terraform therefore has a direct alternative, while a team using it to orchestrate a genuinely mixed estate still has a reason to keep it.

### Policy as code and governance

[Pulumi Policies](/docs/insights/policy/) runs as part of `pulumi preview` and `pulumi up`, and policies can be written in Python, TypeScript, or Open Policy Agent Rego. It's open source and free, and Pulumi Cloud adds centralized management, policy groups, and [pre-built compliance packs](/docs/insights/policy/policy-packs/pre-built-packs/) for frameworks like CIS, HITRUST, NIST, and PCI DSS. Spacelift also builds on Open Policy Agent, but takes a broader, orchestration-oriented view: [Rego policies](https://docs.spacelift.io/concepts/policy/) run at distinct points in a run's lifecycle — who can log in, who can access a stack, whether a plan is approved, how a Git push is interpreted, and how notifications are routed. Because Pulumi Policies run inside the deployment itself, they apply on Spacelift too; Pulumi's enforcement and compliance packs stay in force even when Spacelift orchestrates the run. The two operate at different scopes: Pulumi Policies govern Pulumi deployments, while Spacelift's Rego policies govern the whole run lifecycle across every tool it orchestrates.

### Building platforms programmatically

Pulumi's [Automation API](/docs/iac/concepts/automation-api/) lets a host application drive Pulumi directly, without shelling out to the CLI, which is useful for embedding provisioning in a SaaS product, building an internal developer platform, or generating preview environments from CI. It puts the IaC engine inside your software. Spacelift exposes a GraphQL API, a `spacectl` CLI, and a Terraform/OpenTofu provider for managing Spacelift objects like stacks and policies. The difference is one of altitude: the Automation API embeds infrastructure provisioning in your own code, while Spacelift's API automates the orchestration platform that runs your infrastructure tools.

### AI and agents

Both platforms have moved into AI-assisted infrastructure from different starting points. Spacelift's [Intelligence](https://spacelift.io/platform/intelligence) layer comprises an assistant that answers questions about your estate; [Intent](https://docs.spacelift.io/concepts/intelligence/intent), which provisions from natural language by calling cloud provider APIs directly, bypassing Terraform/OpenTofu entirely; and a hosted [MCP server](https://docs.spacelift.io/integrations/api-development-with-mcp) that applies Spacelift's policies and access controls to AI coding tools like Claude Code and Codex. Pulumi comes at it from the authoring side: because infrastructure lives in general-purpose languages, the coding agents your team already uses can read and change it directly through [Agent Skills](/docs/ai/skills/) and the [Pulumi MCP server](/docs/ai/mcp-server/), and [Pulumi Neo](/product/neo/) is a purpose-built infrastructure agent for deeper, governed automation. Use your own agent, use Neo, or use both. Either way, both keep humans and policy in the loop, and the split mirrors the rest of this comparison: Spacelift governs AI-driven changes to the tools it orchestrates, while Pulumi brings AI to authoring and managing infrastructure as code.

### Using Pulumi and Spacelift together

Because Spacelift treats Pulumi as a first-class runtime, running the two together is a supported, documented path rather than a workaround. Spacelift's [Pulumi integration](https://docs.spacelift.io/vendors/pulumi/) runs the Pulumi CLI directly, so your Pulumi programs behave as they do anywhere the CLI runs. On each run it executes `pulumi login` against your backend, selects your stack, and runs `pulumi preview` and `pulumi up` with refresh and diff enabled. Plan policies receive the Pulumi plan as structured input, and Pulumi secrets are redacted as `[secret]` rather than shown in plaintext. A couple of Pulumi features are limited under Spacelift today: module CI/CD isn't available, and `pulumi import` isn't supported, so you import resources with tasks instead. For teams that would rather not operate a separate orchestration platform, Pulumi Deployments provides the same Git-driven runs, drift detection, and review environments as an integrated part of Pulumi.

## When to use Pulumi or Spacelift

These aren't mutually exclusive. Pulumi authors infrastructure and manages it, so it works as a complete platform on its own. Spacelift runs Pulumi as a first-class tool, so the two pair cleanly: author in Pulumi and orchestrate through Spacelift. They overlap at the management layer, where Pulumi Cloud and Pulumi Deployments cover the same ground Spacelift does for the tools it runs.

**Lead with Pulumi (with Pulumi Cloud and Pulumi Deployments) when** you:

1. Want a single platform that both authors and manages infrastructure, without operating a separate orchestration tool.
1. Are standardizing on Pulumi and want a management layer built for it — managed state, first-class encrypted secrets, [Pulumi ESC](/docs/esc/), [review stacks](/docs/deployments/concepts/review-stacks/), and [drift detection](/docs/deployments/concepts/drift/).
1. Need an embeddable SDK, the [Automation API](/docs/iac/concepts/automation-api/), to drive provisioning from your own application or internal developer platform.
1. Prefer policy authored in the same general-purpose languages as your infrastructure.
1. Want an open-source engine you can run anywhere, on any CI/CD system.

**Reach for Spacelift alongside Pulumi when** you:

1. Run a heterogeneous estate of IaC tools — Terraform, Pulumi, CloudFormation, and Ansible side by side — and want one orchestration plane across all of them, with Pulumi running next to the rest.
1. Have already standardized on Spacelift and want to keep its worker pools, Rego policies, and run workflow while authoring in Pulumi.

Whichever way you run it, Pulumi is where infrastructure is authored and managed; Spacelift or Pulumi Deployments handles the orchestration.

## Adoption: using Pulumi with Spacelift

You can adopt Pulumi alongside or in place of Spacelift in a few common ways, and they can be combined:

1. **Run Pulumi on Spacelift.** Configure a Spacelift stack with the [Pulumi vendor](https://docs.spacelift.io/vendors/pulumi/), point it at your Pulumi backend, and Spacelift orchestrates `pulumi preview` and `pulumi up` on every change while your state stays in Pulumi Cloud or your own backend. This lets a team keep authoring in Pulumi while running a mixed-tool estate through one control plane.
1. **Standardize on Pulumi Cloud and Pulumi Deployments.** If you'd rather not operate a separate orchestration platform, [Pulumi Deployments](/docs/deployments/) provides remote runs, drift detection, review stacks, and Git-driven deploys as an integrated part of Pulumi.
1. **Bring a Terraform estate on Spacelift into Pulumi.** If much of your Spacelift estate is Terraform, Pulumi can embrace it rather than replace it. The lowest-effort step changes no code at all: point Terraform or OpenTofu at [Pulumi Cloud as its state backend](/docs/iac/get-started/terraform/terraform-state-backend/) and get managed state, [remote execution](/docs/iac/get-started/terraform/terraform-remote-execution/), approval gates on VCS-triggered applies, RBAC, and policy enforcement. From there you can [run HCL on the Pulumi engine](/docs/iac/languages-sdks/hcl/), [use existing Terraform modules](/docs/iac/guides/building-extending/using-existing-tools/use-terraform-module/), [work with any Terraform or OpenTofu provider](/docs/iac/concepts/providers/any-terraform-provider/), and [convert HCL](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/) with `pulumi convert --from terraform`, while [`pulumi import`](/docs/iac/guides/migration/import/) brings already-provisioned resources under management. You can keep orchestrating with Spacelift or move those workloads to Pulumi Deployments.

## Frequently asked questions

### Is Spacelift an infrastructure as code tool?

No. Spacelift is an orchestration and CI/CD platform for infrastructure as code, not an IaC language or framework of its own; it runs the IaC tools you author with — Pulumi, Terraform, OpenTofu, CloudFormation, Ansible, and Kubernetes — and adds state, policy, access control, and drift detection around them.

### Can Pulumi run on Spacelift?

Yes. Spacelift runs Pulumi as a first-class vendor, invoking the Pulumi CLI on its workers. On each run it executes `pulumi login` against your configured backend, then `pulumi preview` and `pulumi up` with refresh and diff. Two Pulumi-specific features are limited: module CI/CD isn't available, and `pulumi import` isn't supported, so you import resources with tasks instead. See [Spacelift's Pulumi documentation](https://docs.spacelift.io/vendors/pulumi/) for details.

### Does Spacelift replace Pulumi?

No — the two work together at different layers. You author infrastructure with Pulumi, and Spacelift orchestrates the runs. Where Spacelift overlaps with Pulumi is the management layer, Pulumi Cloud and Pulumi Deployments, not Pulumi's authoring engine.

### If you run Terraform on Spacelift, should you consider Pulumi?

Often, yes. Teams frequently adopt Spacelift to add collaboration and governance on top of Terraform. Pulumi offers a different path: rather than orchestrating Terraform in place, you can bring that Terraform investment into a general-purpose IaC platform with an integrated management layer, and you can do it without a rewrite. [Pulumi Cloud can hold your Terraform or OpenTofu state](/docs/iac/get-started/terraform/terraform-state-backend/) with no change to your configurations, [HCL runs as a first-class Pulumi language](/docs/iac/languages-sdks/hcl/), Pulumi [uses existing Terraform modules directly](/docs/iac/guides/building-extending/using-existing-tools/use-terraform-module/) and [works with any Terraform or OpenTofu provider](/docs/iac/concepts/providers/any-terraform-provider/), and [`pulumi convert --from terraform`](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/#converting-terraform-hcl-to-pulumi) is there when a team wants a general-purpose language. For a team weighing how to evolve its Terraform estate, that's often a stronger long-term move than adding an orchestration layer on top of it.

### Does Spacelift manage Pulumi state?

No. Spacelift offers a managed state backend for Terraform and OpenTofu, but for Pulumi you bring your own backend. Spacelift runs `pulumi login` against the backend you configure, so Pulumi state continues to live in [Pulumi Cloud](/docs/iac/concepts/state-and-backends/) or a self-managed backend — Amazon S3, Azure Blob Storage, Google Cloud Storage, or a local file — even when Spacelift orchestrates the run.

### Can Pulumi Cloud manage the Terraform state I keep in Spacelift?

Yes. [Pulumi Cloud implements the Terraform remote backend API](/docs/iac/get-started/terraform/terraform-state-backend/), so Terraform and OpenTofu projects can use it as their state backend by adding a standard `backend "remote"` block — no change to your resource code. Stacks created through the CLI [run plans and applies on Pulumi Cloud](/docs/iac/get-started/terraform/terraform-remote-execution/) by default, VCS-triggered applies wait for manual approval, and the stacks get encrypted state, update history, state locking, RBAC, policy enforcement, and Resource Search alongside your Pulumi-managed resources. If managed state and runs for Terraform are the main reason you use Spacelift, this covers that job directly; if you orchestrate more than one IaC tool through Spacelift, that breadth is still its own argument.

### Is Spacelift open source like Pulumi?

No. Pulumi's CLI, SDKs, and providers are open source under [Apache 2.0](https://github.com/pulumi/pulumi/blob/master/LICENSE), and [Pulumi Cloud](/docs/iac/concepts/pulumi-cloud/) is the commercial offering, with a Free edition and paid editions. Spacelift is proprietary, commercial software; it's built on open-source components like Open Policy Agent and Docker, but it isn't an open-source product itself.

## Next steps

- [Get started with Pulumi](/docs/get-started/)
- [Pulumi Deployments](/docs/deployments/)
- [Pulumi Cloud](/docs/iac/concepts/pulumi-cloud/)
- [Pulumi vs. Terraform](/docs/iac/comparisons/terraform/)

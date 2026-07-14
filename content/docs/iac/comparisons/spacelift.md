---
title_tag: "Pulumi vs. Spacelift"
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

Pulumi and [Spacelift](https://spacelift.io/) are sometimes compared, but they sit at different layers of the infrastructure stack. Pulumi is an infrastructure as code platform: you define infrastructure in general-purpose languages (Python, TypeScript, Go, C#, Java, or YAML), and [Pulumi Cloud](/docs/iac/concepts/pulumi-cloud/) and [Pulumi Deployments](/docs/deployments/) manage state, enforce policy, and run deployments. Spacelift is a CI/CD and orchestration platform for infrastructure as code: it doesn't author infrastructure itself, but runs and manages the IaC tools you already use — including Pulumi, Terraform, OpenTofu, CloudFormation, Ansible, and Kubernetes — from a single control plane.

Because Spacelift runs Pulumi as a first-class runtime, the two are frequently used together rather than chosen one over the other. Where they genuinely overlap is the management layer: Spacelift's orchestration, policy, and collaboration features cover much the same ground as Pulumi Cloud and Pulumi Deployments. This page covers what each tool is, a feature-by-feature comparison, the key differences in detail, and the ways Pulumi and Spacelift can work together or stand in for each other.

## What is Pulumi?

{{< what-is-pulumi >}}

For teams coming from Spacelift, the closest points of comparison are [Pulumi Cloud](/docs/iac/concepts/pulumi-cloud/) and [Pulumi Deployments](/docs/deployments/). Together they provide managed state, role-based access control, policy enforcement, drift detection, and remote, Git-driven runs, forming a management layer built for infrastructure you author with Pulumi. Pulumi's engine is open source and runs anywhere, so you can also drive it from any CI/CD system, Spacelift included.

## What is Spacelift?

[Spacelift](https://spacelift.io/) is a commercial CI/CD and orchestration platform for infrastructure as code, founded in 2020. Rather than defining infrastructure itself, it runs the IaC tools you already use and wraps a management layer around them: version-control integration, policy enforcement, access control, and continuous drift detection. Spacelift supports [Terraform, OpenTofu, Terragrunt, Pulumi, AWS CloudFormation, Kubernetes, and Ansible](https://docs.spacelift.io/vendors/) as run backends, so an organization can manage a heterogeneous mix of tools from one control plane.

Work in Spacelift is organized into [stacks](https://docs.spacelift.io/concepts/stack/) — each a combination of source code, state, and configuration tied to a Git repository — that execute runs when changes are pushed. Runs execute on [worker pools](https://docs.spacelift.io/concepts/worker-pools): a public pool hosted by Spacelift, or private workers you operate in your own cloud account for tighter control over credentials and network access. Governance is handled through [policies](https://docs.spacelift.io/concepts/policy/) written in [Open Policy Agent's](https://www.openpolicyagent.org/) Rego language, which Spacelift evaluates at distinct decision points across a run's lifecycle, from login and stack access to plan approval and notification routing.

Spacelift is proprietary software, though it's built on open-source components such as Open Policy Agent and Docker. It's delivered primarily as a hosted SaaS product, with self-hosted and airgapped options on its highest tier. [Pricing](https://spacelift.io/pricing) starts with a free tier of two users and one public worker, then moves up through annual subscription plans for larger teams.

## Detailed comparison

| Feature | Pulumi | Spacelift |
| --- | --- | --- |
| Role in the stack | Infrastructure as code platform: authors *and* manages infrastructure | Orchestration and CI/CD platform: runs and manages IaC that you author with another tool |
| Infrastructure authoring | General-purpose languages — Python, TypeScript, JavaScript, Go, C#, Java — plus [YAML](/docs/iac/languages-sdks/yaml/) | None of its own; you bring your existing tool (Terraform, OpenTofu, Pulumi, CloudFormation, Ansible, or Kubernetes) |
| IaC tools it works with | Runs Pulumi programs; consumes [any Terraform or OpenTofu provider](/docs/iac/concepts/providers/any-terraform-provider/) and can adopt existing state | Orchestrates [Terraform, OpenTofu, Terragrunt, Pulumi, CloudFormation, Kubernetes, and Ansible](https://docs.spacelift.io/vendors/) |
| State management | [Managed by Pulumi Cloud by default](/docs/iac/concepts/state-and-backends/); self-managed backends include Amazon S3, Azure Blob Storage, and Google Cloud Storage | Managed state backend for Terraform and OpenTofu; for Pulumi you configure your own backend, which Spacelift connects to with `pulumi login` |
| Remote execution | [Pulumi Deployments](/docs/deployments/) for remote, Git-driven runs; the [Automation API](/docs/iac/concepts/automation-api/); or the local CLI | Runs on [public or private worker pools](https://docs.spacelift.io/concepts/worker-pools), triggered by version-control events or the API |
| Drift detection | [`pulumi refresh`](/docs/iac/cli/commands/pulumi_refresh/) and `pulumi preview --diff`; [scheduled drift detection and remediation](/docs/deployments/concepts/drift/) in Pulumi Deployments | [Scheduled drift detection](https://docs.spacelift.io/concepts/stack/drift-detection) with optional reconciliation (requires private workers and a paid plan) |
| Policy as code | [Pulumi Policies](/docs/insights/policy/) in Python, TypeScript, or Open Policy Agent Rego; open source, with centralized management and [compliance packs](/docs/insights/policy/policy-packs/pre-built-packs/) in Pulumi Cloud | [Rego policies](https://docs.spacelift.io/concepts/policy/) evaluated at multiple decision points — login, access, approval, plan, push, trigger, and notification |
| Secrets management | [First-class encrypted secrets](/docs/iac/concepts/secrets/) in state, plus [Pulumi ESC](/docs/esc/) for centralized secrets and configuration | Encrypted environment variables, mounted files, and reusable contexts for configuration and credentials |
| Access control | [Pulumi Cloud](/docs/iac/concepts/pulumi-cloud/) teams and role-based access control, SAML/SSO, and [audit logs](/docs/pulumi-cloud/audit-logs/) | Spaces plus login and access policies; SSO/SAML on higher tiers |
| Version control | [GitHub, GitLab, Azure DevOps, and Bitbucket](/docs/deployments/concepts/review-stacks/) | GitHub, GitLab, Bitbucket, and Azure DevOps |
| Programmatic API | [Automation API](/docs/iac/concepts/automation-api/) to embed provisioning in your own application or platform | GraphQL API and `spacectl` CLI; a Terraform/OpenTofu provider for managing Spacelift itself |
| Execution location | Local CLI anywhere; managed Pulumi Deployments runners or [self-hosted runners](/docs/deployments/concepts/customer-managed-runners/) | Public workers hosted by Spacelift, or private workers in your own environment; fully self-hosted on the top tier |
| Open source | Yes — CLI, SDKs, and providers under [Apache 2.0](https://github.com/pulumi/pulumi/blob/master/LICENSE) | No — proprietary, built on open-source components such as Open Policy Agent and Docker |
| Commercial option | [Pulumi Cloud](/docs/iac/concepts/pulumi-cloud/) | Commercial only, from a free tier up to enterprise plans |

## Key differences

### Two layers: an infrastructure as code platform and an orchestration platform

This is the distinction that shapes every other one. Pulumi is an infrastructure as code platform: it's where infrastructure is *authored*, in a general-purpose language, and it ships with a management layer — Pulumi Cloud and Pulumi Deployments — for state, policy, access control, and remote runs. Spacelift authors nothing. It's an orchestration platform that takes infrastructure you've written in some other tool and runs it, adding governance and collaboration on top. In the landscape of infrastructure tooling, Spacelift sits alongside offerings like Terraform Cloud: a management plane for infrastructure code, not the code itself.

So a like-for-like comparison isn't really "Pulumi vs. Spacelift" so much as "Pulumi Cloud and Pulumi Deployments vs. Spacelift." And because Spacelift runs Pulumi as one of its supported tools, the most common outcome is teams using them together, authoring with Pulumi and orchestrating with Spacelift. The rest of this page compares the overlapping management features, then covers how the two combine.

### Infrastructure authoring and language support

Pulumi programs are written in general-purpose languages, so you get loops, conditionals, classes, package management, IDE support, and the testing frameworks that already exist in those ecosystems, along with [YAML](/docs/iac/languages-sdks/yaml/) for teams who prefer a markup format. Spacelift has no authoring model of its own; what you write depends on the tool you run on it. If that tool is Terraform, you write HCL; if it's Pulumi, you write a Pulumi program and keep every one of Pulumi's language features. When the question is really about how infrastructure is expressed, then, the comparison is between Pulumi and whichever tool you'd otherwise run, not between Pulumi and Spacelift, which is happy to run Pulumi.

### Execution model, GitOps, and drift

Both platforms give you managed, Git-driven runs, and they reach a similar experience from opposite directions. Spacelift is built around version control: a push opens a proposed run that previews changes on a pull request, and a merge triggers a tracked run that applies them, all executed on public or private [worker pools](https://docs.spacelift.io/concepts/worker-pools). [Pulumi Deployments](/docs/deployments/) offers the same shape for Pulumi specifically: remote runs triggered by Git, [review stacks](/docs/deployments/concepts/review-stacks/) that stand up an ephemeral environment per pull request, [scheduled deployments](/docs/deployments/concepts/schedules/), and [time-to-live stacks](/docs/deployments/concepts/ttl/), all running on Pulumi-hosted or [self-hosted runners](/docs/deployments/concepts/customer-managed-runners/). Both detect drift on a schedule and can remediate it: [Pulumi Deployments](/docs/deployments/concepts/drift/) and [Spacelift](https://docs.spacelift.io/concepts/stack/drift-detection) each run a periodic check and, where configured, open a run to reconcile. The practical difference is scope. Pulumi Deployments is purpose-built for Pulumi, while Spacelift applies one execution model across every tool it supports.

### State and secrets

Here the layering shows through clearly. Pulumi manages [state in Pulumi Cloud](/docs/iac/concepts/state-and-backends/) by default, or in a self-managed backend such as Amazon S3, Azure Blob Storage, or Google Cloud Storage, and it treats [secrets as a first-class primitive](/docs/iac/concepts/secrets/): values marked secret are encrypted in transit and at rest, with per-stack encryption keys and pluggable KMS providers. [Pulumi ESC](/docs/esc/) extends this into centralized secrets and configuration shared across stacks and environments.

Spacelift provides a managed state backend too, but only for Terraform and OpenTofu. For Pulumi, Spacelift runs `pulumi login` against a backend you configure, which means your Pulumi state still lives in Pulumi Cloud or your own self-managed backend even when Spacelift orchestrates the run. Spacelift secures its own configuration and credentials with encrypted environment variables and contexts. The upshot is that adopting Spacelift for orchestration doesn't move your Pulumi state off Pulumi's backends; the two responsibilities stay cleanly separated.

### Policy as code and governance

[Pulumi Policies](/docs/insights/policy/) runs as part of `pulumi preview` and `pulumi up`, and policies can be written in Python, TypeScript, or Open Policy Agent Rego. It's open source and free, and Pulumi Cloud adds centralized management, policy groups, and [pre-built compliance packs](/docs/insights/policy/policy-packs/pre-built-packs/) for frameworks like CIS, HITRUST, NIST, and PCI DSS. Spacelift also builds on Open Policy Agent, but takes a broader, orchestration-oriented view: [Rego policies](https://docs.spacelift.io/concepts/policy/) run at distinct points in a run's lifecycle — who can log in, who can access a stack, whether a plan is approved, how a Git push is interpreted, and how notifications are routed. If you want policy expressed in the same general-purpose language as your infrastructure, Pulumi Policies fits naturally. If you want a single Rego-based control plane governing many tools at once, that's Spacelift's model.

### Building platforms programmatically

Pulumi's [Automation API](/docs/iac/concepts/automation-api/) lets a host application drive Pulumi directly, without shelling out to the CLI, which is useful for embedding provisioning in a SaaS product, building an internal developer platform, or generating preview environments from CI. It puts the IaC engine inside your software. Spacelift exposes a GraphQL API, a `spacectl` CLI, and a Terraform/OpenTofu provider for managing Spacelift objects like stacks and policies. The difference is one of altitude: the Automation API embeds infrastructure provisioning in your own code, while Spacelift's API automates the orchestration platform that runs your infrastructure tools.

### Using Pulumi and Spacelift together

Because Spacelift treats Pulumi as a first-class runtime, running the two together is a supported, documented path rather than a workaround. Spacelift's [Pulumi integration](https://docs.spacelift.io/vendors/pulumi/) works with the C#, Go, TypeScript, and Python runtimes. On each run it executes `pulumi login` against your backend, selects your stack, and runs `pulumi preview` and `pulumi up` with refresh and diff enabled. Plan policies receive the Pulumi plan as structured input, and Pulumi secrets are redacted as `[secret]` rather than shown in plaintext. A couple of Pulumi features are limited under Spacelift today: module CI/CD isn't available, and `pulumi import` isn't supported, so you import resources with tasks instead. For teams that would rather not operate a separate orchestration platform, Pulumi Deployments provides the same Git-driven runs, drift detection, and review environments as an integrated part of Pulumi.

## When to choose Pulumi vs. Spacelift

Because Spacelift orchestrates Pulumi, this often isn't an either-or decision. When the real question is which management and orchestration layer to standardize on, here's how the two line up.

**Choose Pulumi (with Pulumi Cloud and Pulumi Deployments) when** you:

1. Want a single platform that both authors and manages infrastructure, without operating a separate orchestration tool.
1. Are standardizing on Pulumi and want a management layer built for it — managed state, first-class encrypted secrets, [Pulumi ESC](/docs/esc/), [review stacks](/docs/deployments/concepts/review-stacks/), and [drift detection](/docs/deployments/concepts/drift/).
1. Need an embeddable SDK, the [Automation API](/docs/iac/concepts/automation-api/), to drive provisioning from your own application or internal developer platform.
1. Prefer policy authored in the same general-purpose languages as your infrastructure.
1. Want an open-source engine you can run anywhere, on any CI/CD system.

**Choose Spacelift when** you:

1. Run a heterogeneous estate of IaC tools — say Terraform, Pulumi, CloudFormation, and Ansible side by side — and want one orchestration and governance plane across all of them.
1. Want a tool-agnostic CI/CD platform for infrastructure, with version-control-driven runs, worker pools in your own cloud, and Rego policy spanning the run lifecycle.
1. Are consolidating orchestration for teams that have each standardized on a different tool.

If you author with Pulumi but want Spacelift as the orchestration plane across a mixed estate, you don't have to choose. See [Adoption](#adoption-using-pulumi-with-spacelift) below.

## Adoption: using Pulumi with Spacelift

There are a few common paths for adopting Pulumi alongside or in place of Spacelift, and they can be combined:

1. **Run Pulumi on Spacelift.** Configure a Spacelift stack with the [Pulumi vendor](https://docs.spacelift.io/vendors/pulumi/), point it at your Pulumi backend, and Spacelift orchestrates `pulumi preview` and `pulumi up` on every change while your state stays in Pulumi Cloud or your own backend. This lets a team keep authoring in Pulumi while running a mixed-tool estate through one control plane.
1. **Consolidate on Pulumi Cloud and Pulumi Deployments.** If you'd rather not operate a separate orchestration platform, [Pulumi Deployments](/docs/deployments/) provides remote runs, drift detection, review stacks, and Git-driven deploys as an integrated part of Pulumi.
1. **Migrate from Terraform on Spacelift to Pulumi.** If your Spacelift estate is mostly Terraform and you want to move to Pulumi, [`pulumi convert`](/docs/iac/concepts/converters/) translates HCL into a Pulumi program, and [`pulumi import`](/docs/iac/guides/migration/import/) brings already-provisioned resources under Pulumi management. You can keep orchestrating with Spacelift or move those workloads to Pulumi Deployments. See [Migrating from Terraform to Pulumi](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/) for a walkthrough.

## Frequently asked questions

### Is Spacelift an infrastructure as code tool?

No. Spacelift is an orchestration and CI/CD platform for infrastructure as code. It doesn't define infrastructure itself; it runs the IaC tools you author with — Pulumi, Terraform, OpenTofu, CloudFormation, Ansible, and Kubernetes — and adds state, policy, access control, and drift detection around them.

### Can I run Pulumi on Spacelift?

Yes. Spacelift supports Pulumi as a first-class runtime for C#, Go, TypeScript, and Python. On each run it executes `pulumi login` against your configured backend, then `pulumi preview` and `pulumi up` with refresh and diff. Two Pulumi-specific features are limited: module CI/CD isn't available, and `pulumi import` isn't supported, so you import resources with tasks instead. See [Spacelift's Pulumi documentation](https://docs.spacelift.io/vendors/pulumi/) for details.

### Does Spacelift replace Pulumi?

No. Spacelift operates at a different layer than Pulumi's authoring engine, overlapping instead with Pulumi's management layer, Pulumi Cloud and Pulumi Deployments. You still author infrastructure with Pulumi (or another tool); Spacelift orchestrates the runs.

### Does Spacelift manage Pulumi state?

No. Spacelift offers a managed state backend for Terraform and OpenTofu, but for Pulumi you bring your own backend. Spacelift runs `pulumi login` against the backend you configure, so Pulumi state continues to live in [Pulumi Cloud](/docs/iac/concepts/state-and-backends/) or a self-managed backend — Amazon S3, Azure Blob Storage, Google Cloud Storage, or a local file — even when Spacelift orchestrates the run.

### Is Spacelift open source like Pulumi?

No. Pulumi's CLI, SDKs, and providers are open source under [Apache 2.0](https://github.com/pulumi/pulumi/blob/master/LICENSE), and [Pulumi Cloud](/docs/iac/concepts/pulumi-cloud/) is the commercial offering, with a free Individual tier and paid plans. Spacelift is proprietary, commercial software; it's built on open-source components like Open Policy Agent and Docker, but it isn't an open-source product itself.

### Should I use Pulumi Deployments or Spacelift?

If you've standardized on Pulumi and want an integrated management layer with no separate platform to operate, [Pulumi Deployments](/docs/deployments/) covers remote runs, drift detection, review stacks, and Git-driven deploys. If you run several IaC tools and want a single orchestration plane across all of them, Spacelift's tool-agnostic model is the better fit, and it can orchestrate Pulumi alongside the rest.

## Next steps

- [Get started with Pulumi](/docs/iac/get-started/)
- [Pulumi Deployments](/docs/deployments/)
- [Pulumi Cloud](/docs/iac/concepts/pulumi-cloud/)
- [Pulumi vs. Terraform](/docs/iac/comparisons/terraform/)

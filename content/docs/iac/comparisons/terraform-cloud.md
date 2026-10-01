---
title_tag: "Pulumi vs. HCP Terraform (Terraform Cloud)"
faq_schema: true
authors: ["pulumi-content-team"]
meta_desc: "Compare Pulumi Cloud and HCP Terraform (Terraform Cloud): languages, state, remote runs, policy, secrets, pricing, and running Terraform on Pulumi Cloud."
title: Terraform Cloud
h1: Pulumi vs. HCP Terraform (Terraform Cloud)
menu:
    iac:
        name: Terraform Cloud
        parent: iac-comparisons
        weight: 11
        identifier: iac-comparisons-terraform-cloud
---

Pulumi Cloud and [HCP Terraform](https://developer.hashicorp.com/terraform/cloud-docs) (formerly Terraform Cloud) are both managed platforms for running infrastructure as code as a team. Each stores state, runs deployments remotely, enforces policy, and controls who can change what. They differ mainly in which infrastructure as code tools they run: HCP Terraform runs Terraform configurations written in HCL, while Pulumi Cloud runs Pulumi programs written in general-purpose languages ({{< pulumi-languages "general-purpose" >}}), YAML, or [HCL](/docs/iac/languages-sdks/hcl/), and can also act as a state backend and remote runner for the Terraform and OpenTofu CLIs.

This page covers what each product is, a feature-by-feature comparison, the most important differences in detail, and the available paths for adopting Pulumi Cloud alongside or instead of HCP Terraform. For a comparison of the Pulumi and Terraform engines themselves, see [Pulumi vs. Terraform](/docs/iac/comparisons/terraform/).

## What is Pulumi?

{{< what-is-pulumi >}}

Pulumi Cloud's capabilities for teams include [Pulumi Deployments](/docs/deployments/) for remote and Git-driven runs, [Pulumi Policies](/docs/discovery-governance/concepts/policy-as-code/) for policy as code, [Pulumi ESC](/docs/esc/) for secrets and configuration, and [Pulumi Discovery](/docs/discovery-governance/) for a searchable inventory of cloud resources. Pulumi Cloud is available as a managed service or [self-hosted](/docs/administration/self-hosting/).

## What is HCP Terraform?

HCP Terraform is HashiCorp's managed service for running Terraform. It stores Terraform state, runs `terraform plan` and `terraform apply` remotely through CLI-driven, VCS-driven, or API-driven workflows, and organizes infrastructure into workspaces grouped by project. It includes a private registry for modules and providers, policy enforcement with Sentinel or Open Policy Agent, dynamic provider credentials for AWS, Azure, Google Cloud, and other platforms, and self-hosted agents for running operations inside private networks. [Terraform Enterprise](https://developer.hashicorp.com/terraform/enterprise) is the self-hosted distribution of the same product.

HCP Terraform is priced by Resources Under Management (RUM), the number of resources tracked in the state files it manages. Its Free tier covers up to 500 managed resources per organization; HashiCorp retired the older user-based Free plan on March 31, 2026. <!-- verified: 2026-08 -->

## Detailed comparison

| Feature | Pulumi Cloud | HCP Terraform |
| --- | --- | --- |
| Languages | {{< pulumi-languages "general-purpose" >}}, YAML, and [HCL](/docs/iac/languages-sdks/hcl/) (`runtime: hcl`), which runs valid Terraform and OpenTofu configurations with a [short list of documented exceptions](/docs/iac/languages-sdks/hcl/#terraform-compatibility) | HCL |
| Terraform and OpenTofu CLI support | [Implements the Terraform remote backend API](/docs/integrations/terraform/state-backend/), so the `terraform` and `tofu` CLIs can store state in Pulumi Cloud and [run plans and applies remotely](/docs/integrations/terraform/remote-execution/) on it | Native backend and runner for the `terraform` CLI |
| State management | Managed state for Pulumi stacks and for Terraform and OpenTofu stacks, with update history, locking, and encryption | Managed state per workspace, with state versions and locking |
| Remote execution | [Pulumi Deployments](/docs/deployments/): Git-push, API, schedule, and click-to-deploy triggers; [review stacks](/docs/deployments/concepts/review-stacks/) per pull request; Pulumi-managed or [customer-managed runners](/docs/deployments/concepts/customer-managed-runners/) | CLI-driven, VCS-driven, and API-driven runs; speculative plans on pull requests; HashiCorp-managed workers or self-hosted agents |
| Drift detection | [Scheduled drift detection](/docs/deployments/concepts/drift/) through Pulumi Deployments, with optional remediation | Health assessments detect drift and evaluate continuous validation checks on eligible plans |
| Policy as code | [Pulumi Policies](/docs/discovery-governance/concepts/policy-as-code/), written in Python, TypeScript, or OPA Rego; enforced on Pulumi previews and updates and, for [remotely executed](/docs/integrations/terraform/remote-execution/) Terraform stacks, against Terraform plans; audit policies can scan existing resources | Sentinel or OPA policy sets, evaluated as a step in each run with advisory, soft-mandatory, or hard-mandatory enforcement |
| Secrets and configuration | [Pulumi ESC](/docs/esc/) manages secrets and configuration for infrastructure and applications, and can pull from external stores such as AWS Secrets Manager and HashiCorp Vault; stack secrets are encrypted in state | Sensitive workspace variables and variable sets; HashiCorp Vault is a separate product for centralized secrets |
| Dynamic cloud credentials | OIDC-based credentials through [Pulumi ESC](/docs/esc/) and Pulumi Deployments | Dynamic provider credentials for AWS, Azure, Google Cloud, Kubernetes, and Vault |
| Module and package registry | Private registry for [Pulumi packages and components](/docs/iac/concepts/packages/) and for [Terraform modules](/docs/integrations/terraform/module-registry/), with a publish API compatible with HCP Terraform's | Private registry for Terraform modules and providers, including no-code-ready modules |
| Resource inventory | [Pulumi Discovery](/docs/discovery-governance/) inventories cloud resources across accounts and providers, including resources not managed by any infrastructure as code tool | Explorer reports on workspaces, modules, providers, and Terraform versions across the organization |
| Access control and audit | [Role-based access control](/docs/administration/concepts/rbac/), SAML SSO, SCIM, and [audit logs](/docs/administration/concepts/audit-logs/) | Team-based permissions, SSO, and audit trails |
| Programmatic API | REST API, plus the [Automation API](/docs/iac/concepts/automation-api/), an SDK for driving Pulumi operations from application code | REST API, with the `go-tfe` client and the `tfe` Terraform provider |
| AI assistance | [Pulumi Neo](/docs/ai/), [Agent Skills](/docs/ai/skills/), and the [Pulumi MCP server](/docs/ai/mcp-server/) | HashiCorp publishes a Terraform MCP server for AI assistants |
| Self-hosted option | [Self-hosted Pulumi Cloud](/docs/administration/self-hosting/) | Terraform Enterprise |
| Pricing model | Editions with a monthly base price and Pulumi Credits consumed across IaC resources, Deployments, ESC, and Neo; see [pricing](/pricing/) | Resources Under Management (RUM), with a Free tier up to 500 managed resources |

## Key differences

### Language support

HCP Terraform runs Terraform, so configurations are written in HCL. HCL is a declarative configuration language with built-in functions and meta-arguments such as `for_each`, `count`, and `dynamic`; reuse happens through modules, and `terraform test` provides a native test framework.

Pulumi Cloud runs Pulumi programs, which can be written in general-purpose languages, YAML, or HCL. A general-purpose language brings its own package manager, test frameworks, and IDE tooling, and lets you build reusable [components](/docs/iac/concepts/components/) as classes or functions. [Pulumi HCL](/docs/iac/languages-sdks/hcl/) runs existing `.tf` files on the Pulumi engine, so language is a per-project choice: HCL projects and general-purpose-language projects in the same organization can share components, policies, and state. HashiCorp deprecated the Cloud Development Kit for Terraform (CDKTF) in December 2025, so HCL is the supported authoring language for HCP Terraform.

### Running Terraform on Pulumi Cloud

Pulumi Cloud can manage Terraform and OpenTofu configurations without converting them. It implements the Terraform remote backend API, so an existing project moves to it by adding a `backend "remote"` block and running `terraform init -migrate-state`. From there:

* Stacks created through the CLI [run plans and applies on Pulumi Cloud](/docs/integrations/terraform/remote-execution/) by default. VCS-triggered applies pause after the plan and wait for **Confirm** or **Discard** in the console. Stacks that predate remote execution stay on local execution until you set the `terraform:execution-mode` stack tag to `remote`.
* Access is governed by the same [RBAC](/docs/administration/concepts/rbac/) as other Pulumi Cloud stacks.
* Backend configuration and OIDC credentials can come from [Pulumi ESC](/docs/esc/), and root module outputs are exposed as stack outputs for other stacks to consume.
* [Preventative policies](/docs/discovery-governance/concepts/policy-as-code/) run against the Terraform plan on remotely executed stacks and can block a non-compliant apply.
* Terraform-managed resources appear in [Pulumi Discovery](/docs/discovery-governance/) alongside Pulumi-managed ones, and [Neo](/docs/ai/neo/code-reviews/) can review Terraform and OpenTofu pull requests.

Pulumi programs in any language can also [consume Terraform modules](/docs/integrations/terraform/modules/) with `pulumi package add hcl module <source> [version]`, resolving from the Terraform Registry, a private registry, or a local path.

### Remote execution and workspaces

HCP Terraform organizes infrastructure into workspaces, each with its own state, variables, and run history, grouped into projects. Runs are triggered from the CLI, from VCS events, or through the API, and can execute on HashiCorp-managed workers or on self-hosted agents.

Pulumi organizes infrastructure into projects and stacks. [Pulumi Deployments](/docs/deployments/) runs `pulumi preview` and `pulumi up` remotely on Git pushes, API calls, [schedules](/docs/deployments/concepts/schedules/), or from the console, and can create [review stacks](/docs/deployments/concepts/review-stacks/) for each pull request. Stacks can read each other's outputs through [stack references](/docs/iac/concepts/stacks/#stackreferences). Runs can execute on Pulumi-managed runners or on [customer-managed runners](/docs/deployments/concepts/customer-managed-runners/) inside your network.

### Policy as code

HCP Terraform evaluates Sentinel or OPA policy sets as a step in each run, after the plan and before the apply. Policies can be advisory, soft-mandatory (can be overridden), or hard-mandatory.

[Pulumi Policies](/docs/discovery-governance/concepts/policy-as-code/) are written in Python, TypeScript, or OPA Rego. Preventative policies run during `pulumi preview` and `pulumi up` and block non-compliant changes; audit policies scan resources that already exist, including resources found by Pulumi Discovery. For Terraform stacks executed remotely on Pulumi Cloud, preventative policies evaluate the Terraform plan. The policy SDK is open source; centralized management and enforcement across an organization are Pulumi Cloud features.

### Secrets and configuration

HCP Terraform stores variables per workspace or in variable sets shared across workspaces. Variables marked sensitive are write-only in the UI and API. Dynamic provider credentials exchange a workload identity token for short-lived cloud credentials at run time. Centralized secrets management across infrastructure and applications is typically handled by HashiCorp Vault, a separate product.

[Pulumi ESC](/docs/esc/) manages secrets and configuration as composable environments that Pulumi stacks, Terraform stacks on Pulumi Cloud, applications, and CI systems can all consume. Environments can generate OIDC credentials for AWS, Azure, and Google Cloud and can reference secrets held in external stores, including Vault. Within Pulumi programs, values marked as secret are encrypted in state with per-stack keys.

### Pricing models

HCP Terraform charges by Resources Under Management: cost scales with the number of resources tracked in state across the organization. Its Free tier covers up to 500 managed resources. <!-- verified: 2026-08 -->

Pulumi Cloud sells editions with a monthly base price and Pulumi Credits, a shared unit consumed by managed IaC resources beyond an edition's included amount, Deployments minutes, ESC, and Neo. Both models charge for the resources you manage; the difference is whether other platform features draw from the same allowance. Current rates are on the [Pulumi pricing page](/pricing/) and [HashiCorp's pricing page](https://www.hashicorp.com/pricing).

### Ecosystem

Terraform has the largest public ecosystem of providers and modules of any infrastructure as code tool. Pulumi can use that ecosystem directly: [any Terraform provider](/docs/iac/concepts/providers/any-terraform-provider/) can be generated into a Pulumi SDK, and Pulumi programs can [consume Terraform modules](/docs/integrations/terraform/modules/) without modification. Pulumi also maintains native providers for [Kubernetes](/registry/packages/kubernetes/), [Azure Native](/registry/packages/azure-native/), and [AWS Cloud Control](/registry/packages/aws-native/) that are generated from each platform's API schema.

## When to choose Pulumi Cloud vs. HCP Terraform

**Choose Pulumi Cloud when** you:

1. Want teams to be able to write infrastructure in a general-purpose language, in HCL, or in both, on one platform.
1. Want to keep running Terraform or OpenTofu while using a managed backend that also runs Pulumi programs.
1. Want secrets and configuration management, resource inventory, and policy as code in the same product as state and remote runs.
1. Need an embeddable SDK ([Automation API](/docs/iac/concepts/automation-api/)) to drive deployments from your own application or internal developer platform.

**Choose HCP Terraform when** you:

1. Have standardized on Terraform and HCL and don't expect to author infrastructure in other languages.
1. Rely on HCP Terraform features without a Pulumi Cloud equivalent, such as Sentinel policies.
1. Already use other HashiCorp products, such as Vault, and want to consolidate on one vendor.
1. Prefer resource-count pricing for your workload.

## Adoption: coexistence, conversion, and import

These paths can be taken independently or combined, and none require the ones after them:

1. **Move Terraform state to Pulumi Cloud.** Point Terraform or OpenTofu at [Pulumi Cloud as its state backend](/docs/integrations/terraform/state-backend/). Configurations and the CLI workflow stay the same. The guide covers migrating from HCP Terraform as well as from Amazon S3, Azure Blob Storage, Google Cloud Storage, and local files.
1. **Move your private module registry.** [Pulumi Cloud's registry hosts Terraform modules](/docs/integrations/terraform/module-registry/) with a publish API compatible with HCP Terraform's private registry. Existing `go-tfe` or `hashicorp/tfe` publishing pipelines work after changing the host to `tf.pulumi.com` and supplying a Pulumi access token. Each published version is also available as a Pulumi package, and `.tf` consumers keep resolving it over the Terraform protocol.
1. **Reuse Terraform modules from Pulumi programs.** Add existing modules to Pulumi projects with [`pulumi package add hcl module`](/docs/integrations/terraform/modules/).
1. **Write projects in HCL on the Pulumi engine.** Use [Pulumi HCL](/docs/iac/languages-sdks/hcl/) with `runtime: hcl` and your existing `.tf` files. Requires Pulumi CLI 3.256.0 or later.
1. **Convert to a general-purpose language.** [`pulumi convert --from terraform`](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/) translates HCL into a Pulumi program as a starting point for review, and [`pulumi import`](/docs/iac/guides/migration/import/) brings existing resources under Pulumi management without recreating them.
1. **Run both side by side.** Pulumi programs can read outputs from Terraform state, so Terraform and Pulumi can manage different parts of the same environment during a gradual migration.

## Frequently asked questions

### Can I use Pulumi Cloud as my Terraform state backend without changing my code?

Yes. Pulumi Cloud implements the Terraform remote backend API, so you add a standard `backend "remote"` block and your resource code stays as it is. Stacks created through the CLI [run plans and applies on Pulumi Cloud](/docs/integrations/terraform/remote-execution/) by default, VCS-triggered applies wait for manual approval, and the stack gets the same RBAC, policy enforcement, and update history as other Pulumi Cloud stacks. See [Using Pulumi Cloud as a Terraform state backend](/docs/integrations/terraform/state-backend/).

### Can I keep writing HCL with Pulumi?

Yes. [HCL is a Pulumi language](/docs/iac/languages-sdks/hcl/): set `runtime: hcl` in `Pulumi.yaml` and write ordinary `.tf` files. Pulumi HCL runs valid Terraform and OpenTofu configurations, with a [short list of documented exceptions](/docs/iac/languages-sdks/hcl/#terraform-compatibility), and has the same access to Pulumi providers as any other Pulumi language.

### Can I use my existing Terraform modules in Pulumi?

Yes, without modifying them. `pulumi package add hcl module <source> [version]` makes a module available to a Pulumi program in any language, resolving from the Terraform Registry, a private registry, or a local path. See [Using Terraform modules in Pulumi](/docs/integrations/terraform/modules/). You can also [host your modules in the Pulumi Cloud registry](/docs/integrations/terraform/module-registry/), where they stay usable from both Pulumi and Terraform.

### Is HCP Terraform (Terraform Cloud) free?

HCP Terraform has a Free tier that covers up to 500 managed resources per organization. The legacy user-based Free plan reached end of life on March 31, 2026, and organizations still on it were moved to the current Free tier. <!-- verified: 2026-08 --> Pulumi Cloud also has a Free edition; see [pricing](/pricing/) for what each edition includes.

### How does Pulumi's pricing compare to HCP Terraform's?

HCP Terraform charges by Resources Under Management, the number of resources tracked in state. Pulumi Cloud charges a monthly base price per edition plus Pulumi Credits, which cover managed resources beyond the included amount as well as Deployments, ESC, and Neo usage. Which is less expensive depends on the number of resources you manage and which other features you use. See the [Pulumi pricing page](/pricing/) for current rates.

### How do I migrate my existing Terraform state and code to Pulumi?

You can move state without changing code by using [Pulumi Cloud as a Terraform backend](/docs/integrations/terraform/state-backend/). To move to the Pulumi engine, run existing `.tf` files with [Pulumi HCL](/docs/iac/languages-sdks/hcl/), convert HCL to another language with `pulumi convert --from terraform`, or adopt existing resources with `pulumi import`. See the [migration guide](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/) for a full walkthrough.

### Does Pulumi work with AI coding agents?

Yes. Coding agents such as Claude Code, Codex, Cursor, and GitHub Copilot can write Pulumi programs, and [Agent Skills](/docs/ai/skills/) and the [Pulumi MCP server](/docs/ai/mcp-server/) give them Pulumi-specific context. [Pulumi Neo](/docs/ai/) is Pulumi's infrastructure agent; it runs inside Pulumi Cloud and can run previews, investigate failed updates, and review Terraform and OpenTofu pull requests. Most teams get the most out of using Neo alongside the coding agent they already use.

## Next steps

* [Get started with Pulumi](/docs/get-started/)
* [Using Pulumi Cloud as a Terraform state backend](/docs/integrations/terraform/state-backend/)
* [Using Terraform modules in Pulumi](/docs/integrations/terraform/modules/)
* [Terraform modules in the Pulumi Cloud registry](/docs/integrations/terraform/module-registry/)
* [Writing Pulumi programs in HCL](/docs/iac/languages-sdks/hcl/)
* [Migrating from Terraform to Pulumi](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/)
* [Pulumi vs. Terraform](/docs/iac/comparisons/terraform/)
* [Pulumi vs. TACOS](/docs/iac/comparisons/tacos/)

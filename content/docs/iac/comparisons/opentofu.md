---
title_tag: "Pulumi vs. OpenTofu"
faq_schema: true
authors: ["joe-duffy"]
meta_desc: "Pulumi vs. OpenTofu: Pulumi is a multi-cloud IaC platform in general-purpose languages; OpenTofu is a Linux Foundation Terraform fork that uses HCL."
title: OpenTofu
h1: Pulumi vs. OpenTofu
menu:
    iac:
        name: OpenTofu
        parent: iac-comparisons
        weight: 30
    concepts:
        identifier: vs-opentofu
        parent: vs
        weight: 30
aliases:
- /docs/reference/vs/opentofu/
- /docs/intro/vs/opentofu/
- /docs/concepts/vs/opentofu/
- /docs/iac/concepts/vs/opentofu/
---

Pulumi and [OpenTofu](https://opentofu.org/) are both declarative infrastructure as code tools that provision resources across clouds and SaaS platforms. Pulumi lets you define infrastructure in general-purpose languages ({{< pulumi-languages "general-purpose" >}}), as well as YAML and [HCL](/docs/iac/languages-sdks/hcl/) itself; OpenTofu is a Linux Foundation fork of Terraform that uses the HashiCorp Configuration Language (HCL).

The two are unusually interoperable. [Pulumi HCL](/docs/iac/languages-sdks/hcl/) runs valid OpenTofu configurations, with a [short list of documented exceptions](/docs/iac/languages-sdks/hcl/#terraform-compatibility), and resolves providers against the OpenTofu registry by default. Pulumi Cloud can operate as a managed [OpenTofu backend](/docs/iac/get-started/terraform/terraform-state-backend/) and [remote runner](/docs/iac/get-started/terraform/terraform-remote-execution/) for the `tofu` CLI. Pulumi programs can execute your existing OpenTofu modules. Adopting Pulumi does not require leaving HCL, your modules, or the OpenTofu ecosystem behind.

This page covers what each tool is, a feature-by-feature comparison, the most important differences in detail, and the available paths for adopting Pulumi alongside or instead of OpenTofu.

## What is Pulumi?

{{< what-is-pulumi >}}

For users coming from OpenTofu, Pulumi can also consume the existing OpenTofu ecosystem directly: the [Any Terraform Provider](/docs/iac/concepts/providers/any-terraform-provider/) feature generates a typed Pulumi SDK from any provider in the OpenTofu or Terraform registry, and Pulumi can [execute existing OpenTofu modules](/docs/iac/guides/building-extending/using-existing-tools/use-terraform-module/) as components inside a Pulumi program.

Pulumi also runs HCL itself. [Pulumi HCL](/docs/iac/languages-sdks/hcl/) is a first-class Pulumi language: set `runtime: hcl` in `Pulumi.yaml`, keep your `.tf` files, and providers resolve against the [OpenTofu registry](https://opentofu.org/registry/) and are bridged automatically, exactly as they are in OpenTofu. The syntax is the same, apart from a [short list of documented exceptions](/docs/iac/languages-sdks/hcl/#terraform-compatibility).

## What is OpenTofu?

OpenTofu is an open-source, declarative infrastructure as code tool forked from Terraform 1.6 and governed by the [Linux Foundation](https://www.linuxfoundation.org/press/announcing-opentofu). OpenTofu uses the [Mozilla Public License 2.0](https://github.com/opentofu/opentofu/blob/main/LICENSE) and the HashiCorp Configuration Language (HCL), the same DSL as Terraform. OpenTofu supports the same provider ecosystem as Terraform — the [OpenTofu Registry](https://search.opentofu.org/) indexes the same providers as the Terraform Registry, along with additional community providers. OpenTofu itself has no commercial tier; managed-state and collaboration features come from third-party services such as Spacelift, env0, and Scalr.

## Detailed comparison

| Feature | Pulumi | OpenTofu |
| --- | --- | --- |
| Language support | {{< pulumi-languages "general-purpose" >}} — general-purpose languages with familiar syntax for loops, conditionals, and abstractions — plus [YAML](/docs/iac/languages-sdks/yaml/) and [HCL](/docs/iac/languages-sdks/hcl/), which runs valid OpenTofu configurations with a [short list of documented exceptions](/docs/iac/languages-sdks/hcl/#terraform-compatibility) and resolves providers against the OpenTofu registry by default | [HashiCorp Configuration Language (HCL)](https://opentofu.org/docs/language/) — a declarative DSL with a fixed set of functions and meta-arguments |
| Cloud and service support | [Pulumi Registry](/registry/) of packages, including [bridged, native, parameterized, and dynamic providers](/docs/iac/concepts/providers/#types-of-providers); first-party native providers for [Kubernetes](/registry/packages/kubernetes/) and [Azure Native](/registry/packages/azure-native/) generated from upstream API schemas; [any OpenTofu or Terraform provider](/docs/iac/concepts/providers/any-terraform-provider/) can be generated into a Pulumi SDK with `pulumi package add terraform-provider <name>` | Providers from the [OpenTofu Registry](https://search.opentofu.org/) or the Terraform Registry; community and custom providers are installed and pinned through the `required_providers` block |
| Transpiled to another format? | No — programs run directly in their host language | No — HCL is interpreted by the OpenTofu CLI |
| State management | [Managed by Pulumi Cloud by default](/docs/iac/concepts/state-and-backends/); self-managed backends include Amazon S3, Azure Blob Storage, Google Cloud Storage, local files, and others; Pulumi Cloud can also [operate as an OpenTofu backend](/docs/iac/get-started/terraform/terraform-state-backend/) | [Self-managed by default](https://opentofu.org/docs/language/state/) (local file); remote backends include S3, GCS, Azure Blob, HTTP, and others; managed offerings available from Pulumi Cloud and third parties (Spacelift, env0, Scalr) |
| Secrets management | [Encrypted in transit and at rest](/docs/iac/concepts/secrets/) in the state file by default, with per-stack encryption keys; pluggable KMS providers (AWS KMS, Azure Key Vault, Google Cloud KMS, HashiCorp Vault) | [State and plan encryption](https://opentofu.org/docs/language/state/encryption/) (added in OpenTofu 1.7) with pluggable key providers; individual variable values are not encrypted as a first-class primitive |
| Execution model | Local CLI, programmatic via [Automation API](/docs/iac/concepts/automation-api/), or remote runs in [Pulumi Deployments](/docs/deployments/) | Local CLI; remote execution requires a runner — Pulumi Cloud [runs `tofu` plans and applies](/docs/iac/get-started/terraform/terraform-remote-execution/) when it backs your state, or use a third-party service |
| Rollback on failed operation | Failed updates leave the stack in a partially-updated state; subsequent `pulumi up` runs reconcile toward the desired state, and you can roll forward by reverting program code | No automatic rollback; failed `tofu apply` runs leave resources in their last reported state and require a follow-up `apply` to reconcile |
| Programmatic API for tools and platforms | [Automation API](/docs/iac/concepts/automation-api/) — a programmatic SDK for building custom CLIs, internal developer platforms, and services that drive `up`, `preview`, and `destroy` without shelling out to the Pulumi CLI | No embeddable SDK; orchestration goes through `tofu` CLI invocations |
| Modularity and reuse | [Component Resources](/docs/iac/concepts/components/) authored in any supported language; [Pulumi Packages](/docs/iac/concepts/packages/) let a component written in one language be consumed from any Pulumi language; language-native package managers (npm, PyPI, NuGet, Maven, Go modules); and the [Pulumi Registry](/registry/) for publicly available packages | [Modules](https://opentofu.org/docs/language/modules/) referenced from local paths, Git, or registries; Pulumi can also [consume OpenTofu modules directly](/docs/iac/guides/building-extending/using-existing-tools/use-terraform-module/) and [host them in Pulumi Cloud's registry](/docs/idp/concepts/terraform-modules/), where `tofu init` can still resolve them |
| Import existing resources | [`pulumi import`](/docs/iac/guides/migration/import/) and the [`import` resource option](/docs/iac/concepts/resources/options/import/), both of which generate code in your language | [`tofu import`](https://opentofu.org/docs/cli/commands/import/) and the [`import` block](https://opentofu.org/docs/language/import/); HCL for the imported resource must be authored by hand |
| Policy as code | [Pulumi Policies](/docs/insights/policy/) — open source, with rules written in Python, TypeScript, or Open Policy Agent Rego; Pulumi Cloud commercial plans add centralized policy management plus [Pulumi-maintained policy packs](/docs/insights/policy/policy-packs/pre-built-packs/) for compliance frameworks like CIS, HITRUST, NIST, and PCI DSS | No built-in policy-as-code; external tools such as [Open Policy Agent](https://www.openpolicyagent.org/) or [Checkov](https://www.checkov.io/) can evaluate plan output |
| Open source | Yes — [Apache License 2.0](https://github.com/pulumi/pulumi/blob/master/LICENSE) | Yes — [Mozilla Public License 2.0](https://github.com/opentofu/opentofu/blob/main/LICENSE) |
| Commercial option | [Pulumi Cloud](/docs/iac/guides/basics/pulumi-cloud-vs-oss/) | None from the OpenTofu project itself; commercial managed-state and collaboration tooling comes from Pulumi Cloud or third parties (Spacelift, env0, Scalr) |

## Key differences

### Language support and the authoring experience

OpenTofu configurations are written in [HCL](https://opentofu.org/docs/language/), a declarative DSL with a fixed set of [built-in functions](https://opentofu.org/docs/language/functions/) and meta-arguments (`for_each`, `count`, `dynamic`) for shaping resources. HCL is declarative and configuration-focused. General-purpose languages offer a different model, with classes, richer runtime logic, package management, IDE features (autocomplete, type checking, refactoring, go-to-definition), and the testing frameworks that already exist in those ecosystems, so Pulumi lets you choose the approach that fits the project. Pulumi supports HCL natively as well, alongside [YAML](/docs/iac/languages-sdks/yaml/) for users who prefer a markup format.

Pulumi does not require you to give up HCL to get any of this. [Pulumi HCL](/docs/iac/languages-sdks/hcl/) is a first-class language that runs the HCL you already write, with a [short list of documented exceptions](/docs/iac/languages-sdks/hcl/#terraform-compatibility), down to resolving unqualified provider sources against the [OpenTofu registry](https://opentofu.org/registry/). The practical difference is that on Pulumi the language is a per-project decision you can revisit — an HCL project and a Go project share the same components, modules, state model, and policies — whereas on OpenTofu, HCL is the only option.

### Cloud and service coverage

OpenTofu and Pulumi target broadly the same set of clouds and SaaS platforms, but reach them through different mechanisms. OpenTofu uses providers from the [OpenTofu Registry](https://search.opentofu.org/) (and, where compatible, the Terraform Registry), installed and pinned through the `required_providers` block. Pulumi pulls from the [Pulumi Registry](/registry/), which includes [bridged, native, parameterized, and dynamic providers](/docs/iac/concepts/providers/#types-of-providers). Pulumi also maintains native providers for [Kubernetes](/registry/packages/kubernetes/) and [Azure Native](/registry/packages/azure-native/), generated directly from each platform's API schema for same-day coverage of new resources.

When a provider is not packaged in the Pulumi Registry, the [Any Terraform Provider](/docs/iac/concepts/providers/any-terraform-provider/) feature generates a typed Pulumi SDK from any provider in the OpenTofu or Terraform registry by running `pulumi package add terraform-provider <name>`. The result is a strongly typed local SDK usable from any Pulumi language — so an OpenTofu user's existing third-party providers are first-class citizens in Pulumi without writing or maintaining a separate bridge.

### Execution and rollbacks

OpenTofu runs locally through the `tofu` CLI; remote execution requires a runner. That runner can be Pulumi Cloud: when it [holds your OpenTofu state](/docs/iac/get-started/terraform/terraform-state-backend/), stacks created through the CLI [run plans and applies on Pulumi Cloud](/docs/iac/get-started/terraform/terraform-remote-execution/) by default, with VCS-triggered applies pausing for manual approval, so you get managed remote runs without adopting a third-party service (Spacelift, env0, Scalr) or building a custom CI pipeline. Pulumi itself runs through the local CLI, programmatically through the [Automation API](/docs/iac/concepts/automation-api/), or remotely through [Pulumi Deployments](/docs/deployments/). Neither tool performs automatic rollback on a failed `apply`/`up`: both leave the stack in a partially updated state and reconcile on the next run. The difference is in surface area — Pulumi offers an embeddable SDK and a first-party managed runner; OpenTofu relies on the CLI and external automation.

### Secrets handling

Pulumi treats secrets as a first-class primitive. Values marked as secrets are encrypted in transit and at rest in the state file, anything derived from a secret is also encrypted, and each stack has its own encryption key. The default encryption provider can be replaced with [AWS KMS, Azure Key Vault, Google Cloud KMS, or HashiCorp Vault](/docs/iac/concepts/secrets/#available-encryption-providers). OpenTofu added [state and plan encryption](https://opentofu.org/docs/language/state/encryption/) in version 1.7, which encrypts the entire state and plan files using a pluggable key provider, but individual sensitive variables are not encrypted as their own primitive — sensitive values are typically fetched at runtime from a secrets store such as HashiCorp Vault or AWS Secrets Manager.

### Policy as code

[Pulumi Policies](/docs/insights/policy/) is open source and free. Policies can be written in Python, TypeScript, or Open Policy Agent Rego, and Pulumi Cloud adds centralized management, policy groups, and enforcement across stacks. Pulumi Cloud commercial plans also include [Pulumi-maintained policy packs](/docs/insights/policy/policy-packs/pre-built-packs/) for common compliance frameworks (CIS, HITRUST, NIST, and PCI DSS), so teams don't have to author and maintain those rules themselves. OpenTofu has no built-in policy-as-code feature; teams typically reach for external tools such as [Open Policy Agent](https://www.openpolicyagent.org/) or [Checkov](https://www.checkov.io/) to evaluate plan output as a separate step.

### Modularity and reuse

OpenTofu modules are units of HCL referenced from a local path, a Git URL, or a registry. Modules compose within HCL. Pulumi's [Component Resources](/docs/iac/concepts/components/) are runtime objects that can share helpers and types with the rest of your program, with explicit parent/child relationships, so a component and the resources inside it form a coherent unit in plan output, deletion, and state. Components can be authored in one language and consumed from any other supported language by publishing them as a [Pulumi Package](/docs/iac/concepts/packages/). Pulumi can also [consume OpenTofu modules directly](/docs/iac/guides/building-extending/using-existing-tools/use-terraform-module/), automatically installing and invoking OpenTofu to execute them — useful for teams that have invested heavily in module libraries and want to keep using them while moving to Pulumi.

### Automation API

The [Automation API](/docs/iac/concepts/automation-api/) lets a host application drive Pulumi without shelling out to the CLI. Practical uses include embedding stack creation in a SaaS product, building an internal developer platform that provisions environments per team or per branch, generating ephemeral preview environments from CI, and orchestrating cross-cloud deployments where each step runs as part of a larger workflow. OpenTofu is invoked through the `tofu` CLI and does not provide an equivalent embeddable SDK; programmatic use means shelling out to the CLI and parsing its output.

## When to choose Pulumi vs. OpenTofu

**Choose Pulumi when** you:

1. Want to write infrastructure in a general-purpose language with the testing frameworks, package managers, and IDE tooling that already exist in that ecosystem.
1. Need an embeddable SDK ([Automation API](/docs/iac/concepts/automation-api/)) to drive deployments from a host application — internal developer platforms, SaaS products, or ephemeral preview environments per pull request.
1. Want first-class encrypted secrets with pluggable KMS providers and per-stack encryption keys.
1. Want a single managed offering ([Pulumi Cloud](/docs/iac/guides/basics/pulumi-cloud-vs-oss/)) that covers state, RBAC, audit logs, policy management, and remote runs.

**Choose OpenTofu when** you:

1. Want a fully open-source, vendor-neutral IaC tool governed by an independent foundation, with no commercial tier from the project itself.
1. Want the engine itself under MPL 2.0 and community governance, rather than depending on a vendor-operated control plane for state, runs, and policy.
1. Prefer to assemble managed-state and collaboration features from third-party services (Spacelift, env0, Scalr) rather than buying them from a single vendor.

An existing investment in HCL, modules, and team expertise is no longer a reason on its own. Pulumi runs [HCL as a first-class language](/docs/iac/languages-sdks/hcl/) with OpenTofu-compatible provider resolution, [executes your existing OpenTofu modules](/docs/iac/guides/building-extending/using-existing-tools/use-terraform-module/), and can [back your OpenTofu state](/docs/iac/get-started/terraform/terraform-state-backend/) without any change to your configurations. The two can also coexist — see [Adoption](#adoption-coexistence-conversion-and-import).

## Adoption: coexistence, conversion, and import

There are several common paths for adopting Pulumi alongside or in place of OpenTofu, and they can be combined:

1. **Use OpenTofu alongside Pulumi.** A Pulumi program can reference an existing OpenTofu state file and read its outputs through [`terraform.state.getLocalReference`](/registry/packages/terraform/api-docs/state/getlocalreference/) or [`terraform.state.getRemoteReference`](/registry/packages/terraform/api-docs/state/getremotereference/) (both functions live in the `terraform` package and work with OpenTofu state). Pulumi can also [execute existing OpenTofu modules directly](/docs/iac/guides/building-extending/using-existing-tools/use-terraform-module/) — Pulumi auto-installs and invokes OpenTofu to run the module — which lets teams keep using their module libraries while adopting Pulumi for new work.
1. **Use Pulumi Cloud as your OpenTofu state backend.** [Pulumi Cloud implements the Terraform remote backend API](/docs/iac/get-started/terraform/terraform-state-backend/), which the `tofu` CLI speaks, so adding a standard `backend "remote"` block and running `tofu init -migrate-state` is the only change. Plans and applies then [run on Pulumi Cloud](/docs/iac/get-started/terraform/terraform-remote-execution/) by default, with approval gates on VCS-triggered applies, and the stack gets encrypted state, update history, state locking, RBAC, policy enforcement, and Resource Search.
1. **Write new projects in HCL on the Pulumi engine.** [Pulumi HCL](/docs/iac/languages-sdks/hcl/) takes your `.tf` files as-is with `runtime: hcl`, resolving providers from the OpenTofu registry just as OpenTofu does.
1. **Convert HCL with `pulumi convert`.** [`pulumi convert --from terraform`](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/#converting-terraform-hcl-to-pulumi) translates HCL into a Pulumi program in the language of your choice. The same flag handles both Terraform and OpenTofu HCL — there is no separate `--from opentofu` flag, because the configuration language is the same.
1. **Import existing resources.** [`pulumi import`](/docs/iac/guides/migration/import/) and the [`import` resource option](/docs/iac/concepts/resources/options/import/) bring already-provisioned resources under Pulumi management and generate the corresponding code in your chosen language. `pulumi import --from hcl <state-file>` does this in bulk: it reads an OpenTofu or Terraform state file and adopts the resources it describes into Pulumi state.

For a complete walkthrough including coexistence patterns and conversion, see [Migrating from Terraform to Pulumi](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/) — the same guide applies to OpenTofu.

## Frequently asked questions

### Is OpenTofu the same as Terraform?

OpenTofu was forked from Terraform 1.6 in 2023 after HashiCorp changed Terraform's license from MPL 2.0 to the Business Source License. The two projects share the HCL configuration language and a largely overlapping provider ecosystem, but they have since diverged: OpenTofu is governed by the Linux Foundation and has added features such as state encryption that Terraform does not have, while Terraform has continued to ship its own new features. For most existing configurations, OpenTofu is a drop-in replacement, but the projects are not identical.

### Can Pulumi use existing OpenTofu providers and modules?

Yes. The [Any Terraform Provider](/docs/iac/concepts/providers/any-terraform-provider/) feature generates a typed Pulumi SDK from any provider in the OpenTofu or Terraform registry by running `pulumi package add terraform-provider <name>`. Pulumi can also [execute existing OpenTofu modules](/docs/iac/guides/building-extending/using-existing-tools/use-terraform-module/) as components inside a Pulumi program — Pulumi auto-installs OpenTofu and invokes it to run the module.

### Can I write Pulumi programs in HCL?

Yes. [Pulumi HCL](/docs/iac/languages-sdks/hcl/) is a first-class Pulumi language: set `runtime: hcl` in `Pulumi.yaml` and keep your `.tf` files. It runs valid OpenTofu configurations, with a [short list of documented exceptions](/docs/iac/languages-sdks/hcl/#terraform-compatibility), and unqualified provider sources resolve against the [OpenTofu registry](https://opentofu.org/registry/) and are bridged automatically — the same behavior you get from `tofu`. Prefix a source with `pulumi/` to use a native Pulumi provider instead. Requires Pulumi CLI 3.256.0 or later.

### Can I keep running OpenTofu and store state in Pulumi Cloud?

Yes, with no change to your configurations. [Pulumi Cloud implements the Terraform remote backend API](/docs/iac/get-started/terraform/terraform-state-backend/) that the `tofu` CLI speaks, so you add a standard `backend "remote"` block and run `tofu init -migrate-state`. Stacks created through the CLI [run plans and applies on Pulumi Cloud](/docs/iac/get-started/terraform/terraform-remote-execution/) by default, VCS-triggered applies wait for manual approval, and you get encrypted state, update history, state locking, RBAC, policy enforcement, and Resource Search while continuing to use `tofu` day-to-day.

### How do I migrate from OpenTofu to Pulumi?

You have four options that can be combined: run your existing `.tf` files as-is on [Pulumi HCL](/docs/iac/languages-sdks/hcl/), convert HCL to another language with [`pulumi convert --from terraform`](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/#converting-terraform-hcl-to-pulumi) (which handles OpenTofu HCL — there is no separate `--from opentofu` flag), bring already-provisioned resources under Pulumi management with [`pulumi import`](/docs/iac/guides/migration/import/) (including `pulumi import --from hcl` to bulk-import from an OpenTofu state file), or run both tools side by side until you're ready to cut over. See the [migration guide](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/) for a full walkthrough.

### Does Pulumi support OpenTofu state files?

Yes. A Pulumi program can read outputs from an OpenTofu state file via [`terraform.state.getLocalReference`](/registry/packages/terraform/api-docs/state/getlocalreference/) for local state and [`terraform.state.getRemoteReference`](/registry/packages/terraform/api-docs/state/getremotereference/) for remote backends. Both functions live in the `terraform` package and work with OpenTofu state because the state file format is shared between the two tools.

### Is Pulumi free like OpenTofu?

The Pulumi CLI and SDKs are open source under Apache 2.0 and free to use. [Pulumi Cloud](/docs/iac/guides/basics/pulumi-cloud-vs-oss/) has a free Individual tier and paid plans that add managed state, RBAC, audit logs, policy management, and other features for running Pulumi at organizational scale. OpenTofu itself is free under MPL 2.0; commercial managed-state and collaboration tooling is sold separately by third parties such as Spacelift, env0, and Scalr.

### Can Pulumi and OpenTofu run side by side during migration?

Yes — and this is one of the more common adoption patterns. Pulumi can read outputs from OpenTofu state files and execute OpenTofu modules directly, so teams typically keep existing infrastructure under OpenTofu while using Pulumi for new work, then incrementally convert or import as the project allows.

## Next steps

- [Get started with Pulumi](/docs/get-started/)
- [Pulumi vs. Terraform](/docs/iac/comparisons/terraform/)
- [Using any Terraform or OpenTofu provider with Pulumi](/docs/iac/concepts/providers/any-terraform-provider/)
- [Using Pulumi Cloud as a Terraform or OpenTofu state backend](/docs/iac/get-started/terraform/terraform-state-backend/)
- [Writing Pulumi programs in HCL](/docs/iac/languages-sdks/hcl/)
- [Migrating from Terraform to Pulumi](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/)

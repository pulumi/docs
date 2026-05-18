---
title_tag: "Pulumi vs. OpenTofu"
meta_desc: "Pulumi vs. OpenTofu: Pulumi is a multi-cloud IaC platform in general-purpose languages; OpenTofu is a Linux Foundation Terraform fork that uses HCL."
title: OpenTofu
h1: Pulumi vs. OpenTofu
meta_image: /images/docs/meta-images/docs-meta.png
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

Pulumi and [OpenTofu](https://opentofu.org/) are both declarative infrastructure as code tools that provision resources across clouds and SaaS platforms. Pulumi lets you define infrastructure in general-purpose languages (Python, TypeScript, JavaScript, Go, C#, Java, or YAML); OpenTofu is a Linux Foundation fork of Terraform 1.6 that uses the HashiCorp Configuration Language (HCL).

This page covers what each tool is, a feature-by-feature comparison, the most important differences in detail, and the available paths for adopting Pulumi alongside or instead of OpenTofu.

## What is Pulumi?

{{< what-is-pulumi >}}

For users coming from OpenTofu, Pulumi can also consume the existing OpenTofu ecosystem directly: the [Any Terraform Provider](/docs/iac/concepts/providers/any-terraform-provider/) feature generates a typed Pulumi SDK from any provider in the OpenTofu or Terraform registry, and Pulumi can [execute existing OpenTofu modules](/docs/iac/guides/building-extending/using-existing-tools/use-terraform-module/) as components inside a Pulumi program.

## What is OpenTofu?

OpenTofu is an open-source, declarative infrastructure as code tool forked from Terraform 1.6 and governed by the [Linux Foundation](https://www.linuxfoundation.org/press/announcing-opentofu). OpenTofu uses the [Mozilla Public License 2.0](https://github.com/opentofu/opentofu/blob/main/LICENSE) and the HashiCorp Configuration Language (HCL), the same DSL as Terraform. OpenTofu supports the same provider ecosystem as Terraform — the [OpenTofu Registry](https://search.opentofu.org/) indexes the same providers as the Terraform Registry, along with additional community providers. OpenTofu itself has no commercial tier; managed-state and collaboration features come from third-party services such as Spacelift, env0, and Scalr.

## Detailed comparison

| Feature | Pulumi | OpenTofu |
| --- | --- | --- |
| Language support | Python, TypeScript, JavaScript, Go, C#, Java, and YAML — general-purpose languages with familiar syntax for loops, conditionals, and abstractions | [HashiCorp Configuration Language (HCL)](https://opentofu.org/docs/language/) — a declarative DSL with a fixed set of functions and meta-arguments |
| Cloud and service support | [Pulumi Registry](/registry/) of packages, including [bridged, native, parameterized, and dynamic providers](/docs/iac/concepts/providers/#types-of-providers); first-party native providers for [Kubernetes](/registry/packages/kubernetes/) and [Azure Native](/registry/packages/azure-native/) generated from upstream API schemas; [any OpenTofu or Terraform provider](/docs/iac/concepts/providers/any-terraform-provider/) can be generated into a Pulumi SDK with `pulumi package add terraform-provider <name>` | Providers from the [OpenTofu Registry](https://search.opentofu.org/) or the Terraform Registry; community and custom providers are installed and pinned through the `required_providers` block |
| Transpiled to another format? | No — programs run directly in their host language | No — HCL is interpreted by the OpenTofu CLI |
| State management | [Managed by Pulumi Cloud by default](/docs/iac/concepts/state-and-backends/); self-managed backends include Amazon S3, Azure Blob Storage, Google Cloud Storage, local files, and others | [Self-managed by default](https://opentofu.org/docs/language/state/) (local file); remote backends include S3, GCS, Azure Blob, HTTP, and others; managed offerings available from third parties (Spacelift, env0, Scalr) |
| Secrets management | [Encrypted in transit and at rest](/docs/iac/concepts/secrets/) in the state file by default, with per-stack encryption keys; pluggable KMS providers (AWS KMS, Azure Key Vault, Google Cloud KMS, HashiCorp Vault) | [State and plan encryption](https://opentofu.org/docs/language/state/encryption/) (added in OpenTofu 1.7) with pluggable key providers; individual variable values are not encrypted as a first-class primitive |
| Execution model | Local CLI, programmatic via [Automation API](/docs/iac/automation-api/), or remote runs in [Pulumi Deployments](/docs/deployments/) | Local CLI; remote execution requires a third-party runner |
| Rollback on failed operation | Failed updates leave the stack in a partially-updated state; subsequent `pulumi up` runs reconcile toward the desired state, and you can roll forward by reverting program code | No automatic rollback; failed `tofu apply` runs leave resources in their last reported state and require a follow-up `apply` to reconcile |
| Programmatic API for tools and platforms | [Automation API](/docs/iac/automation-api/) — a programmatic SDK for building custom CLIs, internal developer platforms, and services that drive `up`, `preview`, and `destroy` without shelling out to the Pulumi CLI | No embeddable SDK; orchestration goes through `tofu` CLI invocations |
| Modularity and reuse | [Component Resources](/docs/iac/concepts/components/) authored in any supported language; [Pulumi Packages](/docs/iac/concepts/packages/) let a component written in one language be consumed from any Pulumi language; language-native package managers (npm, PyPI, NuGet, Maven, Go modules); and the [Pulumi Registry](/registry/) for publicly available packages | [Modules](https://opentofu.org/docs/language/modules/) referenced from local paths, Git, or registries; Pulumi can also [consume OpenTofu modules directly](/docs/iac/guides/building-extending/using-existing-tools/use-terraform-module/) |
| Import existing resources | [`pulumi import`](/docs/iac/guides/migration/import/) and the [`import` resource option](/docs/iac/concepts/resources/options/import/), both of which generate code in your language | [`tofu import`](https://opentofu.org/docs/cli/commands/import/) and the [`import` block](https://opentofu.org/docs/language/import/); HCL for the imported resource must be authored by hand |
| Policy as code | [Pulumi Policies](/docs/insights/policy/) — open source, with rules written in Python, TypeScript, or Open Policy Agent Rego; Pulumi Cloud commercial plans add centralized policy management plus [Pulumi-maintained policy packs](/docs/insights/policy/policy-packs/pre-built-packs/) for compliance frameworks like CIS, HITRUST, NIST, and PCI DSS | No built-in policy-as-code; external tools such as [Open Policy Agent](https://www.openpolicyagent.org/) or [Checkov](https://www.checkov.io/) can evaluate plan output |
| Open source | Yes — [Apache License 2.0](https://github.com/pulumi/pulumi/blob/master/LICENSE) | Yes — [Mozilla Public License 2.0](https://github.com/opentofu/opentofu/blob/main/LICENSE) |
| Commercial option | [Pulumi Cloud](/docs/iac/guides/basics/pulumi-cloud-vs-oss/) | None from the OpenTofu project itself; commercial managed-state and collaboration tooling comes from third parties (Spacelift, env0, Scalr) |

## Key differences

### Language support and the authoring experience

OpenTofu configurations are written in [HCL](https://opentofu.org/docs/language/), a declarative DSL with a fixed set of [built-in functions](https://opentofu.org/docs/language/functions/) and meta-arguments (`for_each`, `count`, `dynamic`) for shaping resources. The DSL keeps configurations declarative but constrains abstraction: there are no classes, no first-class testing frameworks, and no general-purpose package ecosystem. Pulumi programs are written in general-purpose languages, so authors get loops, conditionals, classes, package management, IDE features (autocomplete, type checking, refactoring, go-to-definition), and the testing frameworks that already exist in those ecosystems. Pulumi also supports [YAML](/docs/iac/languages-sdks/yaml/) for users who prefer a markup format.

### Cloud and service coverage

OpenTofu and Pulumi target broadly the same set of clouds and SaaS platforms, but reach them through different mechanisms. OpenTofu uses providers from the [OpenTofu Registry](https://search.opentofu.org/) (and, where compatible, the Terraform Registry), installed and pinned through the `required_providers` block. Pulumi pulls from the [Pulumi Registry](/registry/), which includes [bridged, native, parameterized, and dynamic providers](/docs/iac/concepts/providers/#types-of-providers). Pulumi also maintains native providers for [Kubernetes](/registry/packages/kubernetes/) and [Azure Native](/registry/packages/azure-native/), generated directly from each platform's API schema for same-day coverage of new resources.

When a provider is not packaged in the Pulumi Registry, the [Any Terraform Provider](/docs/iac/concepts/providers/any-terraform-provider/) feature generates a typed Pulumi SDK from any provider in the OpenTofu or Terraform registry by running `pulumi package add terraform-provider <name>`. The result is a strongly typed local package usable from any Pulumi language — so an OpenTofu user's existing third-party providers are first-class citizens in Pulumi without writing or maintaining a separate bridge.

### Execution and rollbacks

OpenTofu runs locally through the `tofu` CLI; remote execution requires a third-party runner (Spacelift, env0, Scalr, or a custom CI pipeline). Pulumi runs through the local CLI, programmatically through the [Automation API](/docs/iac/automation-api/), or remotely through [Pulumi Deployments](/docs/deployments/). Neither tool performs automatic rollback on a failed `apply`/`up`: both leave the stack in a partially-updated state and reconcile on the next run. The difference is in surface area — Pulumi offers an embeddable SDK and a first-party managed runner; OpenTofu relies on the CLI and external automation.

### Secrets handling

Pulumi treats secrets as a first-class primitive. Values marked as secrets are encrypted in transit and at rest in the state file, anything derived from a secret is also encrypted, and each stack has its own encryption key. The default encryption provider can be replaced with [AWS KMS, Azure Key Vault, Google Cloud KMS, or HashiCorp Vault](/docs/iac/concepts/secrets/#available-encryption-providers). OpenTofu added [state and plan encryption](https://opentofu.org/docs/language/state/encryption/) in version 1.7, which encrypts the entire state and plan files using a pluggable key provider, but individual sensitive variables are not encrypted as their own primitive — sensitive values are typically fetched at runtime from a secrets store such as HashiCorp Vault or AWS Secrets Manager.

### Policy as code

[Pulumi Policies](/docs/insights/policy/) is open source and free. Policies can be written in Python, TypeScript, or Open Policy Agent Rego, and Pulumi Cloud adds centralized management, policy groups, and enforcement across stacks. Pulumi Cloud commercial plans also include [Pulumi-maintained policy packs](/docs/insights/policy/policy-packs/pre-built-packs/) for common compliance frameworks (CIS, HITRUST, NIST, and PCI DSS), so teams don't have to author and maintain those rules themselves. OpenTofu has no built-in policy-as-code feature; teams typically reach for external tools such as [Open Policy Agent](https://www.openpolicyagent.org/) or [Checkov](https://www.checkov.io/) to evaluate plan output as a separate step.

### Modularity and reuse

OpenTofu modules are units of HCL referenced from a local path, a Git URL, or a registry. They compose well within HCL but cannot share runtime helpers or types with non-module code. Pulumi's [Component Resources](/docs/iac/concepts/components/) are runtime objects with explicit parent/child relationships, so a component and the resources inside it form a coherent unit in plan output, deletion, and state. Components can be authored in one language and consumed from any other supported language by publishing them as a [Pulumi Package](/docs/iac/concepts/packages/). Pulumi can also [consume OpenTofu modules directly](/docs/iac/guides/building-extending/using-existing-tools/use-terraform-module/), automatically installing and invoking OpenTofu to execute them — useful for teams that have invested heavily in module libraries and want to keep using them while moving to Pulumi.

### Automation API

The [Automation API](/docs/iac/automation-api/) lets a host application drive Pulumi without shelling out to the CLI. Practical uses include embedding stack creation in a SaaS product, building an internal developer platform that provisions environments per team or per branch, generating ephemeral preview environments from CI, and orchestrating cross-cloud deployments where each step runs as part of a larger workflow. OpenTofu is invoked through the `tofu` CLI and does not provide an equivalent embeddable SDK; programmatic use means shelling out to the CLI and parsing its output.

## When to choose Pulumi vs. OpenTofu

**Choose Pulumi when** you:

1. Want to write infrastructure in a general-purpose language with the testing frameworks, package managers, and IDE tooling that already exist in that ecosystem.
1. Need an embeddable SDK ([Automation API](/docs/iac/automation-api/)) to drive deployments from a host application — internal developer platforms, SaaS products, or ephemeral preview environments per pull request.
1. Want first-class encrypted secrets with pluggable KMS providers and per-stack encryption keys.
1. Want a single managed offering ([Pulumi Cloud](/docs/iac/guides/basics/pulumi-cloud-vs-oss/)) that covers state, RBAC, audit logs, policy management, and remote runs.

**Choose OpenTofu when** you:

1. Want a fully open-source, vendor-neutral IaC tool governed by an independent foundation, with no commercial tier from the project itself.
1. Have a large existing investment in HCL configurations, Terraform/OpenTofu modules, and team expertise that you don't want to migrate.
1. Prefer to assemble managed-state and collaboration features from third-party services (Spacelift, env0, Scalr) rather than buying them from a single vendor.

The two can also coexist — see [Adoption](#adoption-coexistence-conversion-and-import) below.

## Adoption: coexistence, conversion, and import

There are several common paths for adopting Pulumi alongside or in place of OpenTofu, and they can be combined:

1. **Use OpenTofu alongside Pulumi.** A Pulumi program can reference an existing OpenTofu state file and read its outputs through [`terraform.state.getLocalReference`](/registry/packages/terraform/api-docs/state/getlocalreference/) or [`terraform.state.getRemoteReference`](/registry/packages/terraform/api-docs/state/getremotereference/) (both functions live in the `terraform` package and work with OpenTofu state). Pulumi can also [execute existing OpenTofu modules directly](/docs/iac/guides/building-extending/using-existing-tools/use-terraform-module/) — Pulumi auto-installs and invokes OpenTofu to run the module — which lets teams keep using their module libraries while adopting Pulumi for new work.
1. **Convert HCL with `pulumi convert`.** [`pulumi convert --from terraform`](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/#converting-terraform-hcl-to-pulumi) translates HCL into a Pulumi program in the language of your choice. The same flag handles both Terraform and OpenTofu HCL — there is no separate `--from opentofu` flag, because the configuration language is the same.
1. **Import existing resources.** [`pulumi import`](/docs/iac/guides/migration/import/) and the [`import` resource option](/docs/iac/concepts/resources/options/import/) bring already-provisioned resources under Pulumi management and generate the corresponding code in your chosen language.

For a complete walkthrough including coexistence patterns and conversion, see [Migrating from Terraform to Pulumi](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/) — the same guide applies to OpenTofu.

## Frequently asked questions

### Is OpenTofu the same as Terraform?

OpenTofu was forked from Terraform 1.6 in 2023 after HashiCorp changed Terraform's license from MPL 2.0 to the Business Source License. The two projects share the HCL configuration language and a largely overlapping provider ecosystem, but they have since diverged: OpenTofu is governed by the Linux Foundation and has added features such as state encryption that Terraform does not have, while Terraform has continued to ship its own new features. For most existing configurations, OpenTofu is a drop-in replacement, but the projects are not identical.

### Can Pulumi use existing OpenTofu providers and modules?

Yes. The [Any Terraform Provider](/docs/iac/concepts/providers/any-terraform-provider/) feature generates a typed Pulumi SDK from any provider in the OpenTofu or Terraform registry by running `pulumi package add terraform-provider <name>`. Pulumi can also [execute existing OpenTofu modules](/docs/iac/guides/building-extending/using-existing-tools/use-terraform-module/) as components inside a Pulumi program — Pulumi auto-installs OpenTofu and invokes it to run the module.

### How do I migrate from OpenTofu to Pulumi?

You have three options that can be combined: convert HCL with [`pulumi convert --from terraform`](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/#converting-terraform-hcl-to-pulumi) (which handles OpenTofu HCL — there is no separate `--from opentofu` flag), bring already-provisioned resources under Pulumi management with [`pulumi import`](/docs/iac/guides/migration/import/), or run both tools side by side until you're ready to cut over. See the [migration guide](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/) for a full walkthrough.

### Does Pulumi support OpenTofu state files?

Yes. A Pulumi program can read outputs from an OpenTofu state file via [`terraform.state.getLocalReference`](/registry/packages/terraform/api-docs/state/getlocalreference/) for local state and [`terraform.state.getRemoteReference`](/registry/packages/terraform/api-docs/state/getremotereference/) for remote backends. Both functions live in the `terraform` package and work with OpenTofu state because the state file format is shared between the two tools.

### Is Pulumi free like OpenTofu?

The Pulumi CLI and SDKs are open source under Apache 2.0 and free to use. [Pulumi Cloud](/docs/iac/guides/basics/pulumi-cloud-vs-oss/) has a free Individual tier and paid plans that add managed state, RBAC, audit logs, policy management, and other features for running Pulumi at organizational scale. OpenTofu itself is free under MPL 2.0; commercial managed-state and collaboration tooling is sold separately by third parties such as Spacelift, env0, and Scalr.

### Can Pulumi and OpenTofu run side by side during migration?

Yes — and this is one of the more common adoption patterns. Pulumi can read outputs from OpenTofu state files and execute OpenTofu modules directly, so teams typically keep existing infrastructure under OpenTofu while using Pulumi for new work, then incrementally convert or import as the project allows.

## Next steps

- [Get started with Pulumi](/docs/iac/get-started/)
- [Pulumi vs. Terraform](/docs/iac/comparisons/terraform/)
- [Pulumi terms and command equivalents for OpenTofu users](/docs/iac/comparisons/terraform/#terraform-terms-and-command-equivalents)
- [Using any Terraform or OpenTofu provider with Pulumi](/docs/iac/concepts/providers/any-terraform-provider/)
- [Migrating from Terraform to Pulumi](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/)

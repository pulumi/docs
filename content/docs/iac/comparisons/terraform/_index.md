---
title_tag: "Pulumi vs. Terraform"
meta_desc: "Pulumi vs. Terraform: Pulumi uses general-purpose languages (Python, TypeScript, Go) across any cloud; Terraform uses HCL with HashiCorp's providers."
title: Terraform
h1: Pulumi vs. Terraform
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Terraform
        parent: iac-comparisons
        weight: 10
        identifier: iac-comparisons-terraform
    concepts:
        identifier: vs-terraform
        parent: vs
        weight: 10
aliases:
- /docs/reference/vs/terraform/
- /docs/intro/vs/terraform/
- /docs/concepts/vs/terraform/
- /docs/iac/concepts/vs/terraform/
---

Pulumi and [HashiCorp Terraform](https://developer.hashicorp.com/terraform) are both declarative infrastructure as code tools with overlapping capabilities and several meaningful differences. Pulumi lets you define infrastructure in general-purpose languages (Python, TypeScript, JavaScript, Go, .NET, Java, or YAML) and supports any cloud or SaaS provider through the [Pulumi Registry](/registry/); Terraform uses [HashiCorp Configuration Language (HCL)](https://developer.hashicorp.com/terraform/language) with HashiCorp's provider ecosystem.

This page covers what each tool is, a feature-by-feature comparison, the most important differences in detail, and the available paths for adopting Pulumi alongside or instead of Terraform.

## What is Pulumi?

{{< what-is-pulumi >}}

Pulumi's provider ecosystem covers the major hyperscalers and SaaS platforms. Several providers are generated directly from upstream API schemas, including [Kubernetes](/registry/packages/kubernetes/), [Azure Native](/registry/packages/azure-native/), [AWS Cloud Control](/registry/packages/aws-native/), and [Google Cloud Native](/registry/packages/google-native/), so new resources and API versions land without waiting for a hand-authored release.

## What is Terraform?

Terraform is an infrastructure as code tool created by HashiCorp (acquired by IBM in February 2025). Programs are written in [HashiCorp Configuration Language (HCL)](https://developer.hashicorp.com/terraform/language), a domain-specific language. Terraform supports many cloud and SaaS providers through its [provider ecosystem](https://registry.terraform.io/browse/providers). The Terraform CLI is distributed under the [Business Source License 1.1](https://github.com/hashicorp/terraform/blob/main/LICENSE), and HashiCorp also offers [HCP Terraform](https://developer.hashicorp.com/terraform/cloud-docs) (formerly Terraform Cloud) and Terraform Enterprise as commercial products for managed state, remote runs, policy, and team workflows.

## Detailed comparison

| Feature | Pulumi | Terraform |
| --- | --- | --- |
| Language support | Python, TypeScript, JavaScript, Go, .NET, Java, and YAML — general-purpose languages with familiar syntax for loops, conditionals, and abstractions | HashiCorp Configuration Language (HCL) — a configuration-focused DSL whose syntax for control flow and dynamic blocks grows harder to read as project complexity increases |
| Cloud and service support | [Pulumi Registry](/registry/) of packages, including [bridged, native, parameterized, and dynamic providers](/docs/iac/concepts/providers/#types-of-providers); schema-generated native providers include [Kubernetes](/registry/packages/kubernetes/), [Azure Native](/registry/packages/azure-native/), [AWS Cloud Control](/registry/packages/aws-native/), and [Google Cloud Native](/registry/packages/google-native/); [any Terraform provider](/docs/iac/concepts/providers/any-terraform-provider/) can be adapted into a Pulumi provider | HashiCorp- and community-maintained providers in the [Terraform Registry](https://registry.terraform.io/) |
| Transpiled to another format? | No — programs run directly in their host language | No — HCL is interpreted directly by the Terraform CLI |
| State management | [Managed by Pulumi Cloud by default](/docs/iac/concepts/state-and-backends/); self-managed backends include S3, Azure Blob Storage, Google Cloud Storage, local files, and others | Local files by default; remote backends include S3, Azure Blob Storage, Google Cloud Storage, Consul, and HCP Terraform's [managed state](https://developer.hashicorp.com/terraform/cloud-docs/workspaces/state) |
| Secrets management | [Encrypted in transit and at rest](/docs/iac/concepts/secrets/) by default in the state file, with per-stack encryption keys; pluggable KMS providers (AWS KMS, Azure Key Vault, Google Cloud KMS, HashiCorp Vault) | [Sensitive values](https://developer.hashicorp.com/terraform/language/values/variables#sensitive-input-variables) are not encrypted in the state file; HCP Terraform encrypts state at rest, and Vault integration is a separate product |
| Execution model | Local CLI, programmatic via [Automation API](/docs/iac/automation-api/), or remote runs in [Pulumi Cloud Deployments](/docs/deployments/) | Local CLI or remote runs in HCP Terraform / Terraform Enterprise |
| Rollback on failed operation | Failed updates leave the stack in a partially-updated state; subsequent `pulumi up` runs reconcile toward the desired state, and you can roll forward by reverting program code | Failed applies leave the workspace in a partially-applied state; subsequent `terraform apply` runs reconcile toward the desired state, and you can roll forward by reverting program code |
| Programmatic API for tools and platforms | [Automation API](/docs/iac/automation-api/) — a programmatic SDK for building custom CLIs, internal developer platforms, and services that stand up ephemeral environments without shelling out to the Pulumi CLI | No equivalent |
| Modularity and reuse | [Component Resources](/docs/iac/concepts/components/) authored in any supported language; [Pulumi Packages](/docs/iac/concepts/packages/) let a component written in one language be consumed from any Pulumi language; language-native package managers (npm, PyPI, NuGet, Maven, Go modules); and the [Pulumi Registry](/registry/) for publicly available packages | [Terraform modules](https://developer.hashicorp.com/terraform/language/modules) (HCL) and the [Terraform Registry](https://registry.terraform.io/) for public modules |
| Import existing resources | [`pulumi import`](/docs/iac/guides/migration/import/) and the [`import` resource option](/docs/iac/concepts/resources/options/import/), both of which generate code in your language | [`terraform import`](https://developer.hashicorp.com/terraform/cli/commands/import) and [`import` blocks](https://developer.hashicorp.com/terraform/language/import); HCL must be hand-authored, though `terraform plan -generate-config-out` can emit a draft |
| Policy as code | [Pulumi Policies](/docs/insights/policy/) — open source, with rules written in Python, TypeScript, or Open Policy Agent Rego; Pulumi Cloud commercial plans add centralized policy management plus [Pulumi-maintained policy packs](/docs/insights/policy/policy-packs/pre-built-packs/) for compliance frameworks like CIS, PCI DSS, and SOC 2 | [Sentinel](https://developer.hashicorp.com/sentinel) (proprietary, HCP Terraform / Enterprise only) and Open Policy Agent |
| Open source | Yes — [Apache License 2.0](https://github.com/pulumi/pulumi/blob/master/LICENSE) | No — [Business Source License 1.1](https://github.com/hashicorp/terraform/blob/main/LICENSE) |
| Commercial option | [Pulumi Cloud](/docs/iac/guides/basics/pulumi-cloud-vs-oss/) | HCP Terraform / Terraform Enterprise |

## Key differences

### Language support and the authoring experience

Terraform requires HCL, a domain-specific language designed for configuration. HCL fits compactly into small projects but lacks the abstractions of a general-purpose language: there are no classes, limited runtime logic, and reuse only through the module system. Pulumi programs are written in general-purpose languages, so authors get loops, conditionals, classes, package management, IDE features (autocomplete, type checking, refactoring, go-to-definition), and the testing frameworks that already exist in those ecosystems. Pulumi also supports [YAML](/docs/iac/languages-sdks/yaml/) for users who prefer a markup format.

### Provider and cloud coverage

Both tools have large provider ecosystems. Pulumi can use any provider published in the [Pulumi Registry](/registry/), and it can adapt any existing Terraform provider into a Pulumi provider — see [types of providers](/docs/iac/concepts/providers/#types-of-providers) for the difference between bridged, native, parameterized, and dynamic providers. In addition, Pulumi maintains [native providers](/blog/pulumiup-native-providers/) for [Kubernetes](/registry/packages/kubernetes/), [Azure Native](/registry/packages/azure-native/), [AWS Cloud Control](/registry/packages/aws-native/), and [Google Cloud Native](/registry/packages/google-native/) that are generated directly from each platform's API schema, which lets them ship same-day support for new APIs and features rather than waiting for a hand-authored provider release.

### Execution and orchestration

Both tools provide a CLI and a managed remote-run service: Pulumi Cloud Deployments for Pulumi, and HCP Terraform for Terraform. Pulumi additionally exposes the [Automation API](/docs/iac/automation-api/), a programmatic SDK that lets you drive `up`, `preview`, and `destroy` from inside another program — for example, to ship a CLI that wraps Pulumi, build a self-service portal for application teams, or orchestrate many stacks dynamically from a higher-level service. Terraform does not have a programmatic equivalent.

### Secrets handling

Pulumi treats secrets as a first-class primitive. Values marked as secrets are encrypted in transit and at rest in the state file, anything derived from a secret is also encrypted, and each stack has its own encryption key. The default encryption provider can be replaced with [AWS KMS, Azure Key Vault, Google Cloud KMS, or HashiCorp Vault](/docs/iac/concepts/secrets/#available-encryption-providers). Terraform does not encrypt sensitive values in its state file; the recommended approach is to integrate with HashiCorp Vault, which is a separate product. HCP Terraform encrypts state at rest, but values inside that state are still readable to anyone with access to the workspace.

### Policy as code

[Pulumi Policies](/docs/insights/policy/) is open source and free. Policies can be written in Python, TypeScript, or Open Policy Agent Rego, and Pulumi Cloud adds centralized management, policy groups, and enforcement across stacks. Pulumi Cloud commercial plans also include [Pulumi-maintained policy packs](/docs/insights/policy/policy-packs/pre-built-packs/) for common compliance frameworks (CIS, PCI DSS, SOC 2, HITRUST, NIST) so teams don't have to author and maintain those rules themselves. Terraform's first-party policy framework, [Sentinel](https://developer.hashicorp.com/sentinel), is proprietary and only available in HCP Terraform and Terraform Enterprise. Open Policy Agent can also be used with Terraform via external tooling.

### Modularity and reuse

Pulumi's [Component Resources](/docs/iac/concepts/components/) are runtime objects with explicit parent/child relationships, so a component and the resources inside it form a coherent unit in plan output, deletion, and state. Components can be authored in one language and consumed from any other supported language by publishing them as a [Pulumi Package](/docs/iac/concepts/packages/). Terraform modules are static HCL units that organize source code, with module instances appearing flat in state.

### Automation API

The [Automation API](/docs/iac/automation-api/) lets a host application drive Pulumi without shelling out to the CLI. Practical uses include embedding stack creation in a SaaS product, building an internal developer platform that provisions environments per team or per branch, generating ephemeral preview environments from CI, and orchestrating cross-cloud deployments where each step runs as part of a larger workflow. Terraform is invoked through its CLI (or HCP Terraform's remote runs) and does not provide an equivalent embeddable SDK.

## When to choose Pulumi vs. Terraform

**Choose Pulumi when** you:

1. Want to write infrastructure in a general-purpose language and use the testing frameworks, package managers, and IDE tooling that already exist in that ecosystem.
1. Need an embeddable SDK ([Automation API](/docs/iac/automation-api/)) to drive deployments from a host application (internal developer platforms, SaaS products, or ephemeral preview environments per pull request).
1. Want built-in secrets encryption, pluggable KMS providers, and per-stack encryption keys without bolting on a separate service.
1. Need open source policy as code ([Pulumi Policies](/docs/insights/policy/) under Apache 2.0, with rules in Python, TypeScript, or Open Policy Agent Rego) rather than a proprietary framework gated behind a commercial tier.
1. Prefer an Apache 2.0-licensed core ([Pulumi CLI and SDKs](https://github.com/pulumi/pulumi/blob/master/LICENSE)) over Terraform's [Business Source License 1.1](https://github.com/hashicorp/terraform/blob/main/LICENSE).

**Choose Terraform when** you:

1. Have a large existing investment in HCL, modules, and team expertise that you don't want to migrate.
1. Depend on HCP Terraform–specific features such as [Sentinel](https://developer.hashicorp.com/sentinel) policies, run tasks, or no-code provisioning that are tightly coupled to HashiCorp's managed service.
1. Want to standardize on a single tool when your scope is limited to providers that already exist in the Terraform Registry and you don't need an embeddable SDK or cross-language module sharing.

The two can also coexist; see [Adoption](#adoption-coexistence-conversion-and-import) below.

## Adoption: coexistence, conversion, and import

There are several common paths for adopting Pulumi alongside or in place of Terraform, and they can be combined:

1. **Use Terraform alongside Pulumi.** Pulumi programs can [reference an existing Terraform state file](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/#referencing-terraform-state) (local or remote) and read outputs from it, which lets you keep some infrastructure in Terraform while you incrementally adopt Pulumi for new work.
1. **Use Pulumi Cloud as a Terraform state backend.** [Pulumi Cloud can store Terraform state](/docs/iac/get-started/terraform/terraform-state-backend/) for teams that want encrypted state, update history, state locking, RBAC, and audit policies while continuing to run Terraform or OpenTofu day-to-day.
1. **Use existing Terraform providers from Pulumi.** The [Terraform bridge](/docs/iac/concepts/providers/any-terraform-provider/) lets Pulumi adapt any Terraform provider, so you can manage resources from a Terraform-only ecosystem in a Pulumi program. Many providers in the Pulumi Registry are built this way.
1. **Consume Terraform modules from Pulumi.** Pulumi can [use existing Terraform modules directly](/docs/iac/guides/building-extending/using-existing-tools/use-terraform-module/) from a Pulumi program, so investments in module ecosystems (community modules, internal modules) carry forward.
1. **Convert HCL to Pulumi.** [`pulumi convert --from terraform`](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/#converting-terraform-hcl-to-pulumi) translates Terraform HCL into a Pulumi program in the language of your choice, preserving names, modules, and structure where possible.
1. **Import existing resources.** [`pulumi import`](/docs/iac/guides/migration/import/) and the [`import` resource option](/docs/iac/concepts/resources/options/import/) bring already-provisioned cloud resources under Pulumi management and generate the corresponding code in your chosen language.

For a complete walkthrough including bulk conversion and state migration, see [Migrating from Terraform to Pulumi](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/).

## Frequently asked questions

### Can Pulumi use existing Terraform providers?

Yes. The [any-Terraform-provider](/docs/iac/concepts/providers/any-terraform-provider/) feature lets Pulumi adapt any provider published in the Terraform Registry into a Pulumi provider, so resources from a Terraform-only ecosystem can be managed from a Pulumi program. Many providers in the [Pulumi Registry](/registry/) are built this way — see [types of providers](/docs/iac/concepts/providers/#types-of-providers) for the differences between bridged, native, parameterized, and dynamic providers.

### Can Pulumi consume existing Terraform modules?

Yes. Pulumi can [use existing Terraform modules directly](/docs/iac/guides/building-extending/using-existing-tools/use-terraform-module/) from a Pulumi program, so investments in community and internal HCL modules carry forward as you adopt Pulumi.

### How do I migrate from Terraform to Pulumi?

You have three options that can be combined: convert HCL with [`pulumi convert --from terraform`](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/#converting-terraform-hcl-to-pulumi), bring already-provisioned resources under Pulumi management with [`pulumi import`](/docs/iac/guides/migration/import/), or run both tools side by side and reference [existing Terraform state](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/#referencing-terraform-state) from Pulumi until you're ready to cut over. See the [migration guide](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/) for a full walkthrough.

### Is Pulumi free and open source like Terraform used to be?

The Pulumi CLI and SDKs are open source under [Apache 2.0](https://github.com/pulumi/pulumi/blob/master/LICENSE) and free to use. [Pulumi Cloud](/docs/iac/guides/basics/pulumi-cloud-vs-oss/) has a free Individual tier and paid plans that add managed state, RBAC, audit logs, policy management, and other features for running Pulumi at organizational scale. Note that Terraform is no longer open source: since version 1.6 it has been distributed under the [Business Source License 1.1](https://github.com/hashicorp/terraform/blob/main/LICENSE). [OpenTofu](/docs/iac/comparisons/opentofu/) is the MPL-2.0 open source fork maintained by the Linux Foundation.

### Does Pulumi support remote state and state locking like Terraform?

Yes. By default, [Pulumi Cloud manages state](/docs/iac/concepts/state-and-backends/) with state locking, history, and access control. Self-managed backends include Amazon S3, Azure Blob Storage, Google Cloud Storage, and local files, with state locking supported on the cloud backends.

### Can I keep using Terraform but store state in Pulumi Cloud?

Yes. [Pulumi Cloud as a Terraform state backend](/docs/iac/get-started/terraform/terraform-state-backend/) stores Terraform state with encryption, update history, state locking, RBAC, and audit policies for teams that want a managed state experience while continuing to run Terraform or OpenTofu day-to-day.

### How does Pulumi handle drift detection?

[`pulumi refresh`](/docs/iac/cli/commands/pulumi_refresh/) compares the state file to the actual state in the cloud and reports differences, and `pulumi preview --diff` shows what would change on the next update. Pulumi Cloud commercial plans add [scheduled drift detection and remediation](/docs/deployments/deployments/drift/) that runs on a configurable cadence and can auto-remediate.

## Next steps

- [Get started with Pulumi](/docs/iac/get-started/)
- [Pulumi terms and command equivalents for Terraform users](/docs/iac/comparisons/terraform/terminology/)
- [Pulumi vs. OpenTofu](/docs/iac/comparisons/opentofu/)
- [OpenTofu vs. Terraform](/docs/iac/comparisons/terraform/opentofu/)

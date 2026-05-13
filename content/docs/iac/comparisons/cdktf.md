---
title_tag: "Pulumi vs. CDKTF"
meta_desc: "Compare Pulumi and CDK for Terraform (CDKTF, deprecated December 2025): language support, providers, state, secrets, and migration paths — side-by-side."
title: CDKTF
h1: Pulumi vs. CDKTF
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: CDKTF
        parent: iac-comparisons
        weight: 4
        identifier: iac-comparisons-cdktf
    concepts:
        parent: vs
        weight: 4
aliases:
- /docs/iac/comparisons/cloud-template-transpilers/cdktf/
---

{{% notes type="info" %}}
As of December 2025, CDK for Terraform (CDKTF) has been [deprecated](/blog/cdktf-is-deprecated-whats-next-for-your-team/) and its [GitHub repository](https://github.com/hashicorp/terraform-cdk) has been archived. This page is preserved for teams evaluating migration paths.
{{% /notes %}}

Pulumi and CDK for Terraform (CDKTF, deprecated December 2025) are both infrastructure as code tools that let you author cloud resources in general-purpose programming languages. They differ in how programs are turned into provisioned infrastructure: Pulumi runs programs directly through its own deployment engine and supports any cloud or SaaS platform through the [Pulumi Registry](/registry/), while CDKTF transpiled programs into Terraform JSON for deployment by the Terraform CLI.

This page covers what each tool is, a feature-by-feature comparison, the most important differences in detail, and the available paths for migrating from CDKTF to Pulumi.

## What is Pulumi?

{{< what-is-pulumi >}}

Many of Pulumi's most popular providers are derived from the same open-source Terraform provider schemas that CDKTF used, so their resource models are typically identical and migration is usually a code-shape change rather than a re-architecture.

## What is CDKTF?

CDK for Terraform (CDKTF) was a HashiCorp project, released in 2020 and [deprecated in December 2025](/blog/cdktf-is-deprecated-whats-next-for-your-team/), that let you define infrastructure in TypeScript, Python, Go, C#, and Java. CDKTF was a [transpiler](https://en.wikipedia.org/wiki/Source-to-source_compiler) (a.k.a. source-to-source compiler): `cdktf synth` produced Terraform JSON, which was then deployed by the Terraform CLI against the open-source Terraform provider ecosystem. The [GitHub repository](https://github.com/hashicorp/terraform-cdk) is archived and no longer receives updates.

## Detailed comparison

| Feature | Pulumi | CDKTF |
| --- | --- | --- |
| Language support | Python, TypeScript, JavaScript, Go, C#, Java, and YAML | TypeScript, Python, Go, C#, Java |
| Cloud and service support | [Pulumi Registry](/registry/) of packages, including [bridged, native, parameterized, and dynamic providers](/docs/iac/concepts/providers/#types-of-providers); first-party native providers for [Kubernetes](/registry/packages/kubernetes/) and [Azure Native](/registry/packages/azure-native/); [any Terraform provider](/docs/iac/concepts/providers/any-terraform-provider/) can be adapted into a Pulumi provider, and [Terraform modules](/docs/iac/using-pulumi/extending-pulumi/use-terraform-module/) can be consumed directly | Terraform providers only, accessed through project-specific SDKs generated on demand by `cdktf get` |
| Transpiled to another format? | No — programs run directly in their host language | Yes — programs are synthesized into Terraform JSON and deployed by the Terraform CLI |
| State management | [Managed by Pulumi Cloud by default](/docs/iac/concepts/state-and-backends/); self-managed backends include Amazon S3, Azure Blob Storage, Google Cloud Storage, local files, and others | Local, remote, or cloud-hosted (the Terraform state model) |
| Secrets management | [Encrypted in transit and at rest](/docs/iac/concepts/secrets/) in the state file by default, with per-stack encryption keys; pluggable KMS providers (AWS KMS, Azure Key Vault, Google Cloud KMS, HashiCorp Vault) | No built-in secrets primitive |
| Execution model | Local CLI, programmatic via [Automation API](/docs/iac/automation-api/), or remote runs in [Pulumi Deployments](/docs/deployments/) | Terraform CLI only (invoked by the `cdktf` CLI) |
| Rollback on failed operation | Failed updates leave the stack in a partially-updated state; subsequent `pulumi up` runs reconcile toward the desired state, and you can roll forward by reverting program code | No automatic rollback; reconciliation requires fixing code and re-running `terraform apply` |
| Programmatic API for tools and platforms | [Automation API](/docs/iac/automation-api/) — a programmatic SDK for building custom CLIs, internal developer platforms, and services that drive `up`, `preview`, and `destroy` without shelling out to the Pulumi CLI | None |
| Modularity and reuse | [Component Resources](/docs/iac/concepts/components/) authored in any supported language; [Pulumi Packages](/docs/iac/concepts/packages/) let a component written in one language be consumed from any Pulumi language; language-native package managers; and the [Pulumi Registry](/registry/) for publicly available packages | CDKTF constructs (built on the [constructs](https://github.com/aws/constructs) library) and direct consumption of Terraform modules |
| Import existing resources | [`pulumi import`](/docs/iac/guides/migration/import/) and the [`import` resource option](/docs/iac/concepts/resources/options/import/), both of which generate code in your language | `cdktf import` and `terraform import`, with hand-authored code wrappers |
| Policy as code | [Pulumi Policies](/docs/insights/policy/) — open source, with rules in Python, TypeScript, or Open Policy Agent Rego; Pulumi Cloud commercial plans add centralized policy management plus [Pulumi-maintained policy packs](/docs/insights/policy/policy-packs/pre-built-packs/) for compliance frameworks like CIS, PCI DSS, and SOC 2 | None first-party; teams typically integrated [OPA](https://www.openpolicyagent.org/) or Sentinel (Terraform Cloud commercial plans) against the synthesized Terraform JSON |
| Open source | Yes — [Apache License 2.0](https://github.com/pulumi/pulumi/blob/master/LICENSE) | The CDKTF framework was [Mozilla Public License 2.0](https://github.com/hashicorp/terraform-cdk/blob/main/LICENSE) until archived; the Terraform CLI that deployed its output moved to the [Business Source License 1.1](https://github.com/HashiCorp/terraform/blob/main/LICENSE) in 2023 |
| Commercial option | [Pulumi Cloud](/docs/iac/concepts/pulumi-cloud/) | HashiCorp Cloud Platform (HCP Terraform, formerly Terraform Cloud); CDKTF itself had no separate commercial tier |

## Key differences

### Language support and the authoring experience

Pulumi and CDKTF both let you author infrastructure in general-purpose languages. Pulumi additionally supports [YAML](/docs/iac/languages-sdks/yaml/) and runs programs directly through its deployment engine, so programs can be unit-tested against their own object graph using the [Pulumi testing tools](/docs/iac/using-pulumi/testing/). CDKTF programs were always synthesized to Terraform JSON before deployment, so testing centered on assertions against the synthesized JSON.

### Cloud and service coverage

CDKTF supported Terraform providers through project-specific SDKs generated on demand by `cdktf get`. Pulumi supports the [Pulumi Registry](/registry/) of pre-built providers — including native providers for [Kubernetes](/registry/packages/kubernetes/) and [Azure Native](/registry/packages/azure-native/) generated directly from each platform's API schema for same-day coverage of new resources — and can additionally [generate typed SDKs on demand](/docs/iac/get-started/terraform/terraform-providers/) for any Terraform provider. Pulumi also supports referencing [Terraform modules directly](/docs/iac/using-pulumi/extending-pulumi/use-terraform-module/) without rewriting them, so existing module investment is preserved during migration.

### Execution and rollbacks

CDKTF provisioned and managed exclusively through the Terraform CLI: `cdktf synth` produced Terraform JSON, then `cdktf deploy` invoked `terraform apply` on it. Pulumi runs deployments through the local CLI, programmatically through the [Automation API](/docs/iac/automation-api/), or remotely through [Pulumi Deployments](/docs/deployments/). Neither tool performs automatic rollback on failure; both leave failed updates in a partially-updated state for the operator to reconcile.

### Secrets handling

Pulumi has built-in support for [secrets management](/docs/iac/concepts/secrets/), encrypting sensitive data in the state file in transit and at rest with per-stack encryption keys. The default encryption provider can be replaced with [AWS KMS, Azure Key Vault, Google Cloud KMS, or HashiCorp Vault](/docs/iac/concepts/secrets/#available-encryption-providers). [Pulumi ESC](/docs/esc/) adds centralized secrets management, integration with third-party services, and dynamic credential retrieval via OpenID Connect. CDKTF had no built-in secrets management.

### Policy as code

[Pulumi Policies](/docs/insights/policy/) is open source and free, with rules written in Python, TypeScript, or Open Policy Agent Rego. Pulumi Cloud adds centralized management and [Pulumi-maintained policy packs](/docs/insights/policy/policy-packs/pre-built-packs/) for frameworks like CIS, PCI DSS, and SOC 2. CDKTF had no first-party policy engine; teams typically wired up [Open Policy Agent](https://www.openpolicyagent.org/) against synthesized Terraform JSON, or relied on Sentinel (commercial Terraform Cloud / HCP Terraform).

### Modularity and reuse

Pulumi's [Component Resources](/docs/iac/concepts/components/) are runtime objects with explicit parent/child relationships, so a component and the resources inside it form a coherent unit in plan output, deletion, and state. Components can be authored in one language and consumed from any other supported language by publishing them as a [Pulumi Package](/docs/iac/concepts/packages/). CDKTF offered constructs built on the [constructs](https://github.com/aws/constructs) library and direct consumption of existing Terraform modules.

### Automation API

The [Automation API](/docs/iac/automation-api/) lets a host application drive Pulumi without shelling out to the CLI. Practical uses include embedding stack creation in a SaaS product, building an internal developer platform that provisions environments per team or per branch, generating ephemeral preview environments from CI, and orchestrating cross-cloud deployments where each step runs as part of a larger workflow. CDKTF had no equivalent embeddable SDK.

## When to choose Pulumi vs. CDKTF

**Choose Pulumi when** you:

1. Need an actively maintained, supported infrastructure as code platform — CDKTF was deprecated in December 2025 and no longer receives updates.
1. Want one tool that targets the Pulumi Registry, Terraform providers, and Terraform modules from the same program.
1. Need built-in secrets encryption, pluggable KMS providers, and per-stack encryption keys.
1. Need an embeddable SDK ([Automation API](/docs/iac/automation-api/)) to drive deployments from a host application.
1. Want a free, open-source policy-as-code engine with rules in Python, TypeScript, or Rego.

**Choose CDKTF when** you:

1. Have an existing, working CDKTF deployment and are not yet ready to migrate. Because CDKTF is deprecated and unmaintained, the only durable choice in this case is to plan a migration — see [Adoption](#adoption-coexistence-conversion-and-import) below.

## Adoption: coexistence, conversion, and import

There are several common paths for migrating from CDKTF to Pulumi, and they can be combined:

1. **Use Terraform/CDKTF state alongside Pulumi.** Pulumi can [reference local or remote Terraform state](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/) — including the state produced by a CDKTF deployment — from a Pulumi program. This lets you continue managing a subset of your infrastructure with CDKTF (or Terraform) while incrementally moving the rest to Pulumi.
1. **Consume Terraform modules directly.** Pulumi can [reference Terraform modules directly](/docs/iac/using-pulumi/extending-pulumi/use-terraform-module/) by generating language-specific SDKs on demand, so existing module investment is preserved.
1. **Convert with `pulumi convert --from terraform`.** Run `cdktf synth` to produce Terraform JSON, then convert that JSON to Pulumi with `pulumi convert --from terraform`. For state, [`pulumi-terraform-migrate`](https://github.com/pulumi/pulumi-tool-terraform-migrate) translates Terraform state into Pulumi state.
1. **Import existing resources.** [`pulumi import`](/docs/iac/guides/migration/import/) and the [`import` resource option](/docs/iac/concepts/resources/options/import/) bring already-provisioned resources under Pulumi management and generate the corresponding code in your chosen language.
1. **Automated migration with Pulumi Neo (recommended).** [Pulumi Neo](/product/neo/) automates code conversion and state migration, then runs `pulumi preview` to verify zero changes before you commit. See [Migrating from Terraform/CDKTF to Pulumi](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/).

For a complete walkthrough, see [Migrating from Terraform or CDKTF to Pulumi](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/).

## Frequently asked questions

### Is CDKTF deprecated?

Yes. HashiCorp [deprecated CDKTF in December 2025](/blog/cdktf-is-deprecated-whats-next-for-your-team/) and archived its [GitHub repository](https://github.com/hashicorp/terraform-cdk). The project no longer receives bug fixes, security updates, or new features.

### What is the recommended replacement for CDKTF?

Pulumi is a direct replacement because it covers the same primary use case — defining infrastructure in TypeScript, Python, Go, C#, or Java — without a transpilation step, and it supports the same Terraform providers and Terraform modules that CDKTF relied on. See [Migrating from Terraform or CDKTF to Pulumi](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/).

### How do I migrate from CDKTF to Pulumi?

You have several options that can be combined: use [Pulumi Neo](/product/neo/) for automated conversion and import; run `cdktf synth` to produce Terraform JSON and convert with [`pulumi convert --from terraform`](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/#converting-terraform-hcl-to-pulumi); migrate state with [`pulumi-terraform-migrate`](https://github.com/pulumi/pulumi-tool-terraform-migrate); or use [`pulumi import`](/docs/iac/guides/migration/import/) to bring resources under Pulumi management resource-by-resource.

### Can I keep my Terraform state when migrating from CDKTF?

Yes. [`pulumi-terraform-migrate`](https://github.com/pulumi/pulumi-tool-terraform-migrate) translates an existing Terraform state file (including state produced by CDKTF) into Pulumi state, so the underlying resources are not destroyed or replaced. Pulumi can also [reference local or remote Terraform state](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/) during incremental migrations.

### Does Pulumi support Terraform modules and providers?

Yes. Pulumi can [adapt any Terraform provider](/docs/iac/concepts/providers/any-terraform-provider/) and can [reference Terraform modules directly](/docs/iac/using-pulumi/extending-pulumi/use-terraform-module/) by generating language-specific SDKs on demand. Many of Pulumi's most popular registry providers are also derived from upstream Terraform provider schemas, so resource models often map one-to-one with CDKTF code.

### Can Pulumi coexist with existing Terraform or CDKTF deployments?

Yes. Pulumi programs can [reference local or remote Terraform state](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/), so you can continue running CDKTF (or Terraform) for a subset of infrastructure while building new work in Pulumi and incrementally migrating.

### Is Pulumi free like CDKTF was?

The Pulumi CLI and SDKs are open source under Apache 2.0 and free to use. [Pulumi Cloud](/docs/iac/concepts/pulumi-cloud/) has a free Individual tier and paid plans that add managed state, RBAC, audit logs, policy management, and other features for running Pulumi at organizational scale. CDKTF itself was free and open source under MPL 2.0; the Terraform CLI that deployed its output moved to the Business Source License 1.1 in 2023.

## Next steps

- [Get started with Pulumi](/docs/iac/get-started/)
- [Pulumi vs. Terraform](/docs/iac/comparisons/terraform/)
- [Pulumi vs. AWS CDK](/docs/iac/comparisons/aws-cdk/)
- [Migrating from Terraform or CDKTF to Pulumi](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/)

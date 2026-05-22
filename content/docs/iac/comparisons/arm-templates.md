---
title_tag: "Pulumi vs. ARM Templates"
meta_desc: "Pulumi vs. ARM Templates: Pulumi is a multi-cloud IaC platform in general-purpose languages; ARM Templates and Bicep are Azure-only declarative templates."
title: ARM Templates
h1: Pulumi vs. ARM Templates
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: ARM Templates
        parent: iac-comparisons
        weight: 40
        identifier: iac-comparisons-arm-templates
    concepts:
        identifier: vs-arm-templates
        parent: vs
        weight: 40
aliases:
- /docs/reference/vs/arm/
- /docs/intro/vs/arm/
- /docs/concepts/vs/arm/
- /docs/iac/concepts/vs/arm/
- /docs/reference/vs/arm-templates/
- /docs/intro/vs/arm-templates/
- /docs/concepts/vs/arm-templates/
- /docs/iac/concepts/vs/arm-templates/
---

Pulumi and [Azure Resource Manager (ARM) Templates](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/overview) are both declarative infrastructure as code tools for Microsoft Azure. Pulumi lets you define infrastructure in general-purpose languages (Python, TypeScript, JavaScript, Go, C#, Java, or YAML) and supports any cloud or SaaS provider through the [Pulumi Registry](/registry/); ARM Templates and [Bicep](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/overview) — a domain-specific language that compiles to ARM JSON — provision only Azure resources and run through Azure's centralized deployment service.

This page covers what each tool is, a feature-by-feature comparison, the most important differences in detail, and the available paths for adopting Pulumi alongside or instead of ARM Templates and Bicep.

## What is Pulumi?

{{< what-is-pulumi >}}

For users coming from ARM Templates or Bicep, the most relevant Pulumi provider is [Azure Native](/registry/packages/azure-native/), which is generated directly from the Azure Resource Manager REST API specifications and offers same-day coverage of new Azure resources. The [Azure Classic](/registry/packages/azure/) provider, built on the AzureRM Terraform provider, is also available for existing projects. The Pulumi Registry also covers AWS, Google Cloud, Kubernetes, and SaaS platforms like Datadog, Auth0, GitHub, and Cloudflare.

## What is ARM Templates?

ARM Templates are Azure's original declarative infrastructure as code format. Templates are authored in [JSON](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/overview) and submitted to the Azure Resource Manager service, which evaluates them and creates, updates, or deletes the corresponding Azure resources. Microsoft owns and operates ARM, and templates are deployed through the Azure Portal, Azure CLI, Azure PowerShell, or the ARM REST API; deployment history is tracked inside the Azure subscription, so there is no separate user-managed state file.

[Bicep](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/overview) is a newer domain-specific language created by Microsoft that compiles to ARM JSON. Bicep offers cleaner syntax, [modules](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/modules), and type checking, but it is still deployed by the same ARM engine and remains Azure-only; the Bicep CLI is [open source](https://github.com/Azure/bicep) under the MIT license, while the underlying ARM deployment service is a closed-source Microsoft service. Both formats are free to use beyond the cost of the resources they manage, and neither has a separately licensed commercial tier. Third-party resources are limited: Azure does not have an equivalent to the AWS CloudFormation Registry, and extending the model typically requires a [custom resource provider](https://learn.microsoft.com/en-us/azure/azure-resource-manager/custom-providers/) or a [deployment script](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/deployment-script-template).

## Detailed comparison

| Feature | Pulumi | ARM Templates |
| --- | --- | --- |
| Language support | Python, TypeScript, JavaScript, Go, C#, Java, and YAML — general-purpose languages with familiar syntax for loops, conditionals, and abstractions | [JSON templates](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/overview) or [Bicep](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/overview) (a DSL that compiles to JSON), with [template functions](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/template-functions) for limited dynamic logic |
| Cloud and service support | [Pulumi Registry](/registry/) of packages, including [bridged, native, parameterized, and dynamic providers](/docs/iac/concepts/providers/#types-of-providers); first-party native providers for [Azure Native](/registry/packages/azure-native/) and [Kubernetes](/registry/packages/kubernetes/) generated from upstream API schemas; [any Terraform provider](/docs/iac/concepts/providers/any-terraform-provider/) can be adapted into a Pulumi provider | Azure resources only; third-party resources require a [custom resource provider](https://learn.microsoft.com/en-us/azure/azure-resource-manager/custom-providers/) or [deployment scripts](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/deployment-script-template) |
| Transpiled to another format? | No — programs run directly in their host language | Bicep compiles to ARM JSON before deployment; JSON ARM templates are interpreted directly by the ARM service |
| State management | [Managed by Pulumi Cloud by default](/docs/iac/concepts/state-and-backends/); self-managed backends include Amazon S3, Azure Blob Storage, Google Cloud Storage, local files, and others | Managed by the ARM service inside the Azure subscription as [deployment history](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/deployment-history); no user-accessible state file |
| Secrets management | [Encrypted in transit and at rest](/docs/iac/concepts/secrets/) in the state file by default, with per-stack encryption keys; pluggable KMS providers (AWS KMS, Azure Key Vault, Google Cloud KMS, HashiCorp Vault) | No built-in secrets primitive; sensitive values are passed via [`secureString` and `secureObject` parameters](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/data-types#secure-strings-and-objects) or [Key Vault references](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/key-vault-parameter) resolved at deploy time |
| Execution model | Local CLI, programmatic via [Automation API](/docs/iac/concepts/automation-api/), or remote runs in [Pulumi Deployments](/docs/deployments/) | Centralized Azure-managed service driven through the Azure Portal, Azure CLI (`az deployment`), Azure PowerShell, the Bicep CLI, or the ARM REST API |
| Rollback on failed operation | Failed updates leave the stack in a partially-updated state; subsequent `pulumi up` runs reconcile toward the desired state, and you can roll forward by reverting program code | [Optional rollback on error to the last successful deployment](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/rollback-on-error) when enabled at deploy time |
| Programmatic API for tools and platforms | [Automation API](/docs/iac/concepts/automation-api/) — a programmatic SDK for building custom CLIs, internal developer platforms, and services that drive `up`, `preview`, and `destroy` without shelling out to the Pulumi CLI | No embeddable SDK; orchestration goes through the Azure CLI, Azure SDKs, or the ARM REST API |
| Modularity and reuse | [Component Resources](/docs/iac/concepts/components/) authored in any supported language; [Pulumi Packages](/docs/iac/concepts/packages/) let a component written in one language be consumed from any Pulumi language; language-native package managers (npm, PyPI, NuGet, Maven, Go modules); and the [Pulumi Registry](/registry/) for publicly available packages | [Linked templates](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/linked-templates) and [Bicep modules](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/modules); shared through the [Bicep public module registry](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/private-module-registry) and [template specs](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/template-specs) |
| Import existing resources | [`pulumi import`](/docs/iac/guides/migration/import/) and the [`import` resource option](/docs/iac/concepts/resources/options/import/), both of which generate code in your language | No first-class import; existing resources can be referenced read-only via the [`existing` keyword in Bicep](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/existing-resource), or adopted by hand-authoring a template that matches the deployed state |
| Policy as code | [Pulumi Policies](/docs/insights/policy/) — open source, with rules written in Python, TypeScript, or Open Policy Agent Rego; Pulumi Cloud commercial plans add centralized policy management plus [Pulumi-maintained policy packs](/docs/insights/policy/policy-packs/pre-built-packs/) for compliance frameworks like CIS, HITRUST, NIST, and PCI DSS | [Azure Policy](https://learn.microsoft.com/en-us/azure/governance/policy/overview) — a separate Azure service that enforces rules at the subscription or management-group level rather than as part of the template authoring loop |
| Open source | Yes — [Apache License 2.0](https://github.com/pulumi/pulumi/blob/master/LICENSE) | [Bicep](https://github.com/Azure/bicep) is MIT-licensed; the ARM deployment service itself is a closed-source Microsoft service |
| Commercial option | [Pulumi Cloud](/docs/iac/guides/basics/pulumi-cloud-vs-oss/) | None — ARM and Bicep are part of Azure with no separate commercial tier |

## Key differences

### Language support and the authoring experience

ARM Templates are written in JSON, whose verbosity, nested objects, and lack of comments make non-trivial templates difficult to read. Dynamic behavior comes from a fixed set of [template functions](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/template-functions) and constructs such as `copy` loops and `condition`, which keep templates declarative but become harder to follow as logic grows. Bicep was created by Microsoft to address those ergonomic problems: it offers cleaner syntax, type-aware tooling, and first-class [modules](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/modules), but it is still a markup-style DSL that compiles to ARM JSON and runs through the same ARM deployment engine, so it inherits the same execution model and Azure-only scope.

Pulumi programs are written directly in general-purpose languages, so authors get loops, conditionals, classes, package management, IDE features (autocomplete, type checking, refactoring, go-to-definition), and the testing frameworks that already exist in those ecosystems. Pulumi also supports [YAML](/docs/iac/languages-sdks/yaml/) for users who prefer a markup format closer to ARM or Bicep.

### Cloud and service coverage

ARM Templates and Bicep manage Azure resources only; third-party support is limited to custom resource providers and deployment scripts. Pulumi targets any cloud or SaaS platform through the [Pulumi Registry](/registry/), which includes [bridged, native, parameterized, and dynamic providers](/docs/iac/concepts/providers/#types-of-providers). For Azure specifically, Pulumi maintains the [Azure Native](/registry/packages/azure-native/) provider, generated directly from the Azure Resource Manager REST API specifications, which gives same-day coverage of new Azure resources — the same coverage story that ARM Templates offer, but consumed from Python, TypeScript, Go, C#, Java, or YAML. The [Azure Classic](/registry/packages/azure/) provider, built on the AzureRM Terraform provider, is also available and is appropriate for existing projects. When a resource is not available in a Pulumi provider, Pulumi can [adapt any Terraform provider](/docs/iac/concepts/providers/any-terraform-provider/) for use from a Pulumi program.

### Execution and rollbacks

ARM Templates run deployments inside an Azure-managed service. Templates are submitted through the Azure Portal, Azure CLI, Azure PowerShell, the Bicep CLI, or the ARM REST API; the ARM service evaluates the template, executes changes, and — when [rollback on error](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/rollback-on-error) is enabled — restores the resource group to its last successful deployment if the new deployment fails. Pulumi runs deployments through the local CLI, programmatically through the [Automation API](/docs/iac/concepts/automation-api/), or remotely through [Pulumi Deployments](/docs/deployments/), and `pulumi preview` shows the exact set of changes before they are made. Failed Pulumi updates leave the stack in a partially-updated state; subsequent `pulumi up` runs reconcile toward the desired state, and you can roll forward by reverting program code. The two models trade off differently between automated cleanup on failure (ARM) and direct, scriptable control over the deployment loop (Pulumi).

### Secrets handling

Pulumi treats secrets as a first-class primitive. Values marked as secrets are encrypted in transit and at rest in the state file, anything derived from a secret is also encrypted, and each stack has its own encryption key. The default encryption provider can be replaced with [AWS KMS, Azure Key Vault, Google Cloud KMS, or HashiCorp Vault](/docs/iac/concepts/secrets/#available-encryption-providers). ARM Templates have no built-in secrets primitive; sensitive values are typically declared as [`secureString` or `secureObject` parameters](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/data-types#secure-strings-and-objects), which Azure omits from the activity log and deployment history, or passed in through [Key Vault references](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/key-vault-parameter) that resolve to a Key Vault secret at deploy time. In both cases the protection depends on configuring and integrating an external Key Vault rather than on the template engine itself.

### Policy as code

[Pulumi Policies](/docs/insights/policy/) is open source and free. Policies can be written in Python, TypeScript, or Open Policy Agent Rego, and Pulumi Cloud adds centralized management, policy groups, and enforcement across stacks. Pulumi Cloud commercial plans also include [Pulumi-maintained policy packs](/docs/insights/policy/policy-packs/pre-built-packs/) for common compliance frameworks (CIS, HITRUST, NIST, and PCI DSS), so teams don't have to author and maintain those rules themselves. ARM Templates have no policy-as-code mechanism built into the templating language; teams use [Azure Policy](https://learn.microsoft.com/en-us/azure/governance/policy/overview), a separate Azure service that enforces rules at the subscription or management-group level, to gate the resources that ARM is allowed to create.

### Modularity and reuse

Pulumi's [Component Resources](/docs/iac/concepts/components/) are runtime objects with explicit parent/child relationships, so a component and the resources inside it form a coherent unit in plan output, deletion, and state. Components can be authored in one language and consumed from any other supported language by publishing them as a [Pulumi Package](/docs/iac/concepts/packages/), and they are distributed through language-native package managers (npm, PyPI, NuGet, Maven, Go modules) and the [Pulumi Registry](/registry/). ARM offers [linked templates](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/linked-templates) and [Bicep modules](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/modules), shared through the [Bicep public module registry](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/private-module-registry) and [template specs](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/template-specs). Both approaches let teams package reusable infrastructure, but Pulumi components are real objects in the program's type system, while ARM modules remain static template fragments that the ARM engine evaluates at deploy time.

### Automation API

The [Automation API](/docs/iac/concepts/automation-api/) lets a host application drive Pulumi without shelling out to the CLI. Practical uses include embedding stack creation in a SaaS product, building an internal developer platform that provisions environments per team or per branch, generating ephemeral preview environments from CI, and orchestrating cross-cloud deployments where each step runs as part of a larger workflow. ARM Templates and Bicep are invoked through the Azure Portal, Azure CLI, Azure PowerShell, or the ARM REST API directly, and do not provide an equivalent embeddable SDK.

## When to choose Pulumi vs. ARM Templates

**Choose Pulumi when** you:

1. Manage infrastructure across multiple clouds or SaaS providers (AWS, Google Cloud, Kubernetes, Datadog, Cloudflare, etc.) and want one tool for all of it.
1. Want to write infrastructure in a general-purpose language with the testing frameworks, package managers, and IDE tooling that already exist in that ecosystem.
1. Need an embeddable SDK ([Automation API](/docs/iac/concepts/automation-api/)) to drive deployments from a host application — internal developer platforms, SaaS products, or ephemeral preview environments per pull request.
1. Want built-in secrets encryption, pluggable KMS providers, and per-stack encryption keys without bolting on a separate service.

**Choose ARM Templates or Bicep when** you:

1. Provision only Azure resources and want a service fully managed inside your Azure subscription with no external dependencies.
1. Have an existing investment in ARM templates, Bicep modules, template specs, and Azure team expertise that you don't want to migrate.
1. Depend on ARM-specific behavior such as rollback on error, the Bicep [`existing` keyword](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/existing-resource) for read-only references, or [deployment scripts](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/deployment-script-template) that run as part of a deployment.

The two can also coexist — see [Adoption](#adoption-coexistence-conversion-and-import) below.

## Adoption: coexistence, conversion, and import

There are several common paths for adopting Pulumi alongside or in place of ARM Templates and Bicep, and they can be combined:

1. **Use ARM or Bicep alongside Pulumi.** A Pulumi program can reference an existing ARM deployment and read its outputs through `azure-native.resources.Deployment.get()`, which lets you keep some infrastructure in ARM or Bicep while incrementally adopting Pulumi for new work. See [Coexist with ARM](/docs/iac/guides/migration/migrating-to-pulumi/from-arm/#coexist-with-arm) in the migration guide for an example.
1. **Convert templates with `pulumi convert`.** [`pulumi convert --from arm`](/docs/iac/guides/migration/converters/) translates JSON ARM templates into a Pulumi program in the language of your choice, and `pulumi convert --from bicep` does the same for Bicep. Both produce code that uses the Azure Native provider.
1. **Import existing resources.** [`pulumi import`](/docs/iac/guides/migration/import/) and the [`import` resource option](/docs/iac/concepts/resources/options/import/) bring already-provisioned Azure resources under Pulumi management and generate the corresponding code in your chosen language.
1. **Use Pulumi Neo for AI-assisted migration.** [Pulumi Neo](/product/neo/) can automate ARM-to-Pulumi conversion, generate import mappings, and verify zero changes with `pulumi preview` before you commit. See the [migration guide](/docs/iac/guides/migration/migrating-to-pulumi/from-arm/) for details.

For a complete walkthrough including coexistence patterns and resource adoption, see [Migrating from Azure Resource Manager to Pulumi](/docs/iac/guides/migration/migrating-to-pulumi/from-arm/).

## Frequently asked questions

### Does Pulumi support Bicep?

Yes. [`pulumi convert --from bicep`](/docs/iac/guides/migration/converters/) translates Bicep files into a Pulumi program in Python, TypeScript, Go, C#, Java, or YAML. The generated program uses the [Azure Native](/registry/packages/azure-native/) provider, which is built from the same Azure Resource Manager REST API specifications that Bicep ultimately deploys to, so the resource model matches what Bicep produces.

### Does Pulumi cover the same Azure resources as ARM Templates?

Yes. The [Azure Native](/registry/packages/azure-native/) provider is generated directly from the Azure Resource Manager REST API specifications — the same specifications ARM Templates and Bicep deploy against — so it offers same-day coverage of new Azure services and resources.

### Can Pulumi reference existing ARM deployments?

Yes. A Pulumi program can read outputs from an existing ARM deployment with `azure-native.resources.Deployment.get()` without taking ownership of its resources. This lets you keep some infrastructure in ARM or Bicep while consuming its outputs from a Pulumi program. See [Coexist with ARM](/docs/iac/guides/migration/migrating-to-pulumi/from-arm/#coexist-with-arm) for an example.

### How do I migrate from ARM or Bicep to Pulumi?

You have several options that can be combined: convert templates with [`pulumi convert --from arm`](/docs/iac/guides/migration/converters/) or `--from bicep`, bring already-provisioned resources under management with [`pulumi import`](/docs/iac/guides/migration/import/), or run both tools side by side until you're ready to cut over. See [Migrating from Azure Resource Manager to Pulumi](/docs/iac/guides/migration/migrating-to-pulumi/from-arm/) for a full walkthrough.

### Is Pulumi free like ARM Templates?

The Pulumi CLI and SDKs are open source under Apache 2.0 and free to use. [Pulumi Cloud](/docs/iac/guides/basics/pulumi-cloud-vs-oss/) has a free Individual tier and paid plans that add managed state, RBAC, audit logs, policy management, and other features for running Pulumi at organizational scale. ARM Templates and Bicep have no usage cost beyond the resources they manage.

### Can Pulumi detect drift like ARM?

Pulumi has first-class drift detection: [`pulumi refresh`](/docs/iac/cli/commands/pulumi_refresh/) compares the state file to the actual state in Azure and reports differences, and `pulumi preview --diff` shows what would change on the next update. Pulumi Cloud commercial plans add [scheduled drift detection and remediation](/docs/deployments/deployments/drift/). ARM Templates do not have a first-class drift detection feature.

## Next steps

- [Get started with Pulumi](/docs/iac/get-started/)
- [Get started with Pulumi and Azure](/docs/iac/get-started/azure/)
- [Pulumi for Azure](/docs/integrations/clouds/azure/)
- [Pulumi Azure Native provider](/registry/packages/azure-native/)
- [Migrating from Azure Resource Manager to Pulumi](/docs/iac/guides/migration/migrating-to-pulumi/from-arm/)

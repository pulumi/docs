---
title_tag: "Pulumi vs. AWS CloudFormation"
meta_desc: "Pulumi vs. AWS CloudFormation: Pulumi is a multi-cloud IaC tool in general-purpose languages; CloudFormation is AWS-only with JSON/YAML templates."
title: AWS CloudFormation
h1: Pulumi vs. AWS CloudFormation
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: AWS CloudFormation
        parent: iac-comparisons
        weight: 20
        identifier: iac-comparisons-cloudformation
    concepts:
        parent: vs
        weight: 20
aliases:
- /docs/intro/vs/cloud-templates/cloudformation/
- /docs/concepts/vs/cloud-templates/cloudformation/
- /docs/iac/concepts/vs/cloud-templates/cloudformation/
- /docs/iac/comparisons/cloud-templates/cloudformation/
- /docs/reference/vs/cloud_templates/
- /docs/intro/vs/cloud_templates/
- /docs/intro/vs/cloud-templates/
- /docs/concepts/vs/cloud-templates/
- /docs/iac/concepts/vs/cloud-templates/
- /docs/iac/comparisons/cloud-templates/
---

Pulumi and [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) are both declarative infrastructure as code tools for AWS. Pulumi lets you define infrastructure in general-purpose languages (Python, TypeScript, JavaScript, Go, C#, Java, or YAML) and supports any cloud or SaaS provider through the [Pulumi Registry](/registry/); AWS CloudFormation uses JSON or YAML templates and provisions only AWS resources.

This page covers what each tool is, a feature-by-feature comparison, the most important differences in detail, and the available paths for adopting Pulumi alongside or instead of AWS CloudFormation.

## What is Pulumi?

{{< what-is-pulumi >}}

For users coming from CloudFormation, the most relevant Pulumi providers are the [AWS Classic](/registry/packages/aws/) provider (built on the AWS Terraform provider) and the [AWS Cloud Control](/registry/packages/aws-native/) provider, which is generated from the AWS Cloud Control API and offers same-day coverage of new AWS resources. The Pulumi Registry also covers Azure, Google Cloud, Kubernetes, and SaaS platforms like Datadog, Auth0, GitHub, and Cloudflare.

## What is AWS CloudFormation?

AWS CloudFormation is an AWS-managed service for provisioning AWS resources from templates written in JSON or YAML. Templates are uploaded to the CloudFormation service, which evaluates them and creates, updates, or deletes the corresponding AWS resources. CloudFormation is AWS-only; third-party resources are supported through [CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) extensions published by AWS partners and the community. CloudFormation is a closed-source AWS service with no usage cost beyond the cost of the resources it manages, and no separately licensed commercial tier.

## Detailed comparison

| Feature | Pulumi | AWS CloudFormation |
| --- | --- | --- |
| Language support | Python, TypeScript, JavaScript, Go, C#, Java, and YAML — general-purpose languages with familiar syntax for loops, conditionals, and abstractions | JSON or YAML templates, with [intrinsic functions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference.html) (`Fn::Join`, `Fn::If`, `Fn::ForEach`, etc.) for limited dynamic logic |
| Cloud and service support | [Pulumi Registry](/registry/) of packages, including [bridged, native, parameterized, and dynamic providers](/docs/iac/concepts/providers/#types-of-providers); first-party native providers for [Kubernetes](/registry/packages/kubernetes/) and [Azure Native](/registry/packages/azure-native/) generated from upstream API schemas; [any Terraform provider](/docs/iac/concepts/providers/any-terraform-provider/) can be adapted into a Pulumi provider | AWS services only; third-party resources are supported through [CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) extensions and [custom resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-custom-resources.html) backed by AWS Lambda |
| Transpiled to another format? | No — programs run directly in their host language | No — templates are interpreted by the CloudFormation service |
| State management | [Managed by Pulumi Cloud by default](/docs/iac/concepts/state-and-backends/); self-managed backends include Amazon S3, Azure Blob Storage, Google Cloud Storage, local files, and others | Managed by the CloudFormation service inside the AWS account; no user-accessible state file |
| Secrets management | [Encrypted in transit and at rest](/docs/iac/concepts/secrets/) in the state file by default, with per-stack encryption keys; pluggable KMS providers (AWS KMS, Azure Key Vault, Google Cloud KMS, HashiCorp Vault) | No built-in secrets primitive; sensitive values are typically passed via [`NoEcho` parameters](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html) or [dynamic references](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html) to AWS Secrets Manager or SSM Parameter Store |
| Execution model | Local CLI, programmatic via [Automation API](/docs/iac/automation-api/), or remote runs in [Pulumi Deployments](/docs/deployments/) | Centralized AWS-managed service driven through the AWS Console, AWS CLI, AWS SDKs, or [change sets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.html) |
| Rollback on failed operation | Failed updates leave the stack in a partially-updated state; subsequent `pulumi up` runs reconcile toward the desired state, and you can roll forward by reverting program code | [Automatic stack rollback](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-rollback-triggers.html) on failed create or update; configurable rollback triggers and `DisableRollback` for debugging |
| Programmatic API for tools and platforms | [Automation API](/docs/iac/automation-api/) — a programmatic SDK for building custom CLIs, internal developer platforms, and services that drive `up`, `preview`, and `destroy` without shelling out to the Pulumi CLI | No embeddable SDK; orchestration goes through the AWS CLI, AWS SDKs, or the CloudFormation API |
| Modularity and reuse | [Component Resources](/docs/iac/concepts/components/) authored in any supported language; [Pulumi Packages](/docs/iac/concepts/packages/) let a component written in one language be consumed from any Pulumi language; language-native package managers (npm, PyPI, NuGet, Maven, Go modules); and the [Pulumi Registry](/registry/) for publicly available packages | [Nested stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html), [CloudFormation modules](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/modules.html) registered through the CloudFormation Registry, and [Cross-stack references](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/walkthrough-crossstackref.html) via exported outputs |
| Import existing resources | [`pulumi import`](/docs/iac/guides/migration/import/) and the [`import` resource option](/docs/iac/concepts/resources/options/import/), both of which generate code in your language | [Import existing resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import.html) through a change set, with a hand-authored template fragment describing the resources to adopt |
| Policy as code | [Pulumi Policies](/docs/insights/policy/) — open source, with rules written in Python, TypeScript, or Open Policy Agent Rego; Pulumi Cloud commercial plans add centralized policy management plus [Pulumi-maintained policy packs](/docs/insights/policy/policy-packs/pre-built-packs/) for compliance frameworks like CIS, PCI DSS, and SOC 2 | [CloudFormation Hooks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/hooks.html) (authored in Java, Python, or TypeScript and registered with the CloudFormation Registry) and [CloudFormation Guard](https://docs.aws.amazon.com/cfn-guard/latest/ug/what-is-guard.html) for policy-as-code rules |
| Open source | Yes — [Apache License 2.0](https://github.com/pulumi/pulumi/blob/master/LICENSE) | No — CloudFormation is a closed-source AWS service |
| Commercial option | [Pulumi Cloud](/docs/iac/concepts/pulumi-cloud/) | None — CloudFormation is part of AWS and has no separate commercial tier |

## Key differences

### Language support and the authoring experience

CloudFormation templates are written in JSON or YAML. Dynamic behavior comes from a fixed set of [intrinsic functions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference.html) such as `Fn::If`, `Fn::Join`, and `Fn::ForEach`, which keep templates declarative but become harder to read as logic grows. Pulumi programs are written in general-purpose languages, so authors get loops, conditionals, classes, package management, IDE features (autocomplete, type checking, refactoring, go-to-definition), and the testing frameworks that already exist in those ecosystems. Pulumi also supports [YAML](/docs/iac/languages-sdks/yaml/) for users who prefer a markup format closer to CloudFormation.

### Cloud and service coverage

CloudFormation manages AWS resources, with third-party support added through CloudFormation Registry extensions and custom resources backed by AWS Lambda. Pulumi targets any cloud or SaaS platform through the [Pulumi Registry](/registry/), which includes [bridged, native, parameterized, and dynamic providers](/docs/iac/concepts/providers/#types-of-providers). For AWS specifically, Pulumi offers the [AWS Classic](/registry/packages/aws/) provider, built on the AWS Terraform provider, and the [AWS Cloud Control](/registry/packages/aws-native/) provider, which is generated from the AWS Cloud Control API and offers same-day coverage of new AWS resources. Pulumi also maintains native providers for [Kubernetes](/registry/packages/kubernetes/) and [Azure Native](/registry/packages/azure-native/) generated directly from each platform's API schema. When a resource is not available in a Pulumi provider, Pulumi can [adapt any Terraform provider](/docs/iac/concepts/providers/any-terraform-provider/) for use from a Pulumi program.

### Execution and rollbacks

CloudFormation runs deployments inside an AWS-managed service. The CloudFormation service evaluates a template, executes changes, and on failure rolls the stack back to its last stable state by default; rollback behavior is configurable through [rollback triggers](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-rollback-triggers.html) and `DisableRollback`. Pulumi runs deployments through the local CLI, programmatically through the [Automation API](/docs/iac/automation-api/), or remotely through [Pulumi Deployments](/docs/deployments/). Failed Pulumi updates leave the stack in a partially-updated state; subsequent `pulumi up` runs reconcile toward the desired state, and you can roll forward by reverting program code. The two models trade off differently between automated cleanup on failure (CloudFormation) and direct, scriptable control over the deployment loop (Pulumi).

### Secrets handling

Pulumi treats secrets as a first-class primitive. Values marked as secrets are encrypted in transit and at rest in the state file, anything derived from a secret is also encrypted, and each stack has its own encryption key. The default encryption provider can be replaced with [AWS KMS, Azure Key Vault, Google Cloud KMS, or HashiCorp Vault](/docs/iac/concepts/secrets/#available-encryption-providers). CloudFormation has no built-in secrets primitive; sensitive values are typically passed in through [`NoEcho` parameters](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html) (which masks values in the AWS Console but stores them in the template processing path) or through [dynamic references](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html) that resolve to values in AWS Secrets Manager or SSM Parameter Store at deploy time.

### Policy as code

[Pulumi Policies](/docs/insights/policy/) is open source and free. Policies can be written in Python, TypeScript, or Open Policy Agent Rego, and Pulumi Cloud adds centralized management, policy groups, and enforcement across stacks. Pulumi Cloud commercial plans also include [Pulumi-maintained policy packs](/docs/insights/policy/policy-packs/pre-built-packs/) for common compliance frameworks (CIS, PCI DSS, SOC 2, HITRUST, NIST), so teams don't have to author and maintain those rules themselves. CloudFormation's first-party options are [CloudFormation Hooks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/hooks.html), which run pre-provisioning checks authored in Java, Python, or TypeScript and registered with the CloudFormation Registry, and [CloudFormation Guard](https://docs.aws.amazon.com/cfn-guard/latest/ug/what-is-guard.html), an open-source CLI for evaluating templates against rules.

### Modularity and reuse

Pulumi's [Component Resources](/docs/iac/concepts/components/) are runtime objects with explicit parent/child relationships, so a component and the resources inside it form a coherent unit in plan output, deletion, and state. Components can be authored in one language and consumed from any other supported language by publishing them as a [Pulumi Package](/docs/iac/concepts/packages/). CloudFormation offers [nested stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html), [CloudFormation modules](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/modules.html) registered through the CloudFormation Registry, and [cross-stack references](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/walkthrough-crossstackref.html) via exported outputs.

### Automation API

The [Automation API](/docs/iac/automation-api/) lets a host application drive Pulumi without shelling out to the CLI. Practical uses include embedding stack creation in a SaaS product, building an internal developer platform that provisions environments per team or per branch, generating ephemeral preview environments from CI, and orchestrating cross-cloud deployments where each step runs as part of a larger workflow. CloudFormation is invoked through the AWS Console, AWS CLI, AWS SDKs, or the CloudFormation API directly, and does not provide an equivalent embeddable SDK.

## When to choose Pulumi vs. AWS CloudFormation

**Choose Pulumi when** you:

1. Manage infrastructure across multiple clouds or SaaS providers (Azure, Google Cloud, Kubernetes, Datadog, Cloudflare, etc.) and want one tool for all of it.
1. Want to write infrastructure in a general-purpose language with the testing frameworks, package managers, and IDE tooling that already exist in that ecosystem.
1. Need an embeddable SDK ([Automation API](/docs/iac/automation-api/)) to drive deployments from a host application — internal developer platforms, SaaS products, or ephemeral preview environments per pull request.
1. Want built-in secrets encryption, pluggable KMS providers, and per-stack encryption keys without bolting on a separate service.

**Choose AWS CloudFormation when** you:

1. Provision only AWS resources and want a service fully managed inside your AWS account with no external dependencies.
1. Depend on CloudFormation-specific features such as automatic stack rollback on failure, [Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html), or [StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html) for multi-account deployments.
1. Have an existing investment in CloudFormation templates, custom resources, and team expertise that you don't want to migrate.

The two can also coexist — see [Adoption](#adoption-coexistence-conversion-and-import) below.

## Adoption: coexistence, conversion, and import

There are several common paths for adopting Pulumi alongside or in place of AWS CloudFormation, and they can be combined:

1. **Use CloudFormation alongside Pulumi.** A Pulumi program can reference an existing CloudFormation stack and read its outputs through [`aws.cloudformation.getStack`](/registry/packages/aws/api-docs/cloudformation/getstack/), which lets you keep some infrastructure in CloudFormation while incrementally adopting Pulumi for new work. Pulumi can also manage CloudFormation stacks themselves through [`aws.cloudformation.Stack`](/registry/packages/aws/api-docs/cloudformation/stack/) when you need a CloudFormation-specific feature.
1. **Convert templates with `pulumi convert`.** [`pulumi convert --from cloudformation`](/docs/iac/guides/migration/migrating-to-pulumi/from-cloudformation/#converting-stacks-and-resources) translates a CloudFormation JSON or YAML template into a Pulumi program in the language of your choice, preserving names and structure where possible.
1. **Import existing resources.** [`pulumi import`](/docs/iac/guides/migration/import/) and the [`import` resource option](/docs/iac/concepts/resources/options/import/) bring already-provisioned AWS resources under Pulumi management and generate the corresponding code in your chosen language.

For a complete walkthrough including coexistence patterns and conversion, see [Migrating from AWS CloudFormation to Pulumi](/docs/iac/guides/migration/migrating-to-pulumi/from-cloudformation/).

## Frequently asked questions

### Can Pulumi manage existing AWS CloudFormation stacks?

Yes. A Pulumi program can read outputs from an existing CloudFormation stack via [`aws.cloudformation.getStack`](/registry/packages/aws/api-docs/cloudformation/getstack/), and can create and manage CloudFormation stacks themselves with [`aws.cloudformation.Stack`](/registry/packages/aws/api-docs/cloudformation/stack/). This lets you keep some infrastructure in CloudFormation while incrementally adopting Pulumi.

### How do I migrate from CloudFormation to Pulumi?

You have three options that can be combined: convert templates with [`pulumi convert --from cloudformation`](/docs/iac/guides/migration/migrating-to-pulumi/from-cloudformation/#converting-stacks-and-resources), bring already-provisioned resources under Pulumi management with [`pulumi import`](/docs/iac/guides/migration/import/), or run both tools side by side until you're ready to cut over. See the [migration guide](/docs/iac/guides/migration/migrating-to-pulumi/from-cloudformation/) for a full walkthrough.

### Does Pulumi cover the same AWS resources as CloudFormation?

Yes. The [AWS Cloud Control](/registry/packages/aws-native/) provider is generated from the AWS Cloud Control API — the same API CloudFormation uses — so it offers same-day coverage of new AWS resources. The [AWS Classic](/registry/packages/aws/) provider, built on the AWS Terraform provider, offers long-standing, comprehensive coverage and is appropriate for the majority of production use cases.

### Is Pulumi free like AWS CloudFormation?

The Pulumi CLI and SDKs are open source under Apache 2.0 and free to use. [Pulumi Cloud](/docs/iac/concepts/pulumi-cloud/) has a free Individual tier and paid plans that add managed state, RBAC, audit logs, policy management, and other features for running Pulumi at organizational scale. CloudFormation itself has no usage cost beyond the resources it manages.

### How does Pulumi handle rollback if there is no automatic stack rollback?

On a failed update, Pulumi leaves the stack in a partially-updated state and reports exactly which resources changed. You roll forward by fixing the program and running `pulumi up` again, or revert the program to a previous commit and re-deploy. This gives direct, scriptable control over the deployment loop at the cost of CloudFormation's automated cleanup behavior.

### Can Pulumi detect drift like CloudFormation?

Yes. [`pulumi refresh`](/docs/iac/cli/commands/pulumi_refresh/) compares the state file to the actual state in the cloud and reports differences, and `pulumi preview --diff` shows what would change on the next update. Pulumi Cloud commercial plans add [scheduled drift detection and remediation](/docs/deployments/deployments/drift/).

### Can I use Pulumi for non-AWS resources alongside CloudFormation for AWS?

Yes — and this is one of the more common adoption patterns. Teams keep AWS infrastructure in CloudFormation while using Pulumi for Kubernetes, Azure, Google Cloud, Datadog, Cloudflare, or other SaaS platforms, then optionally migrate AWS later.

## Next steps

- [Get started with Pulumi](/docs/iac/get-started/)
- [Pulumi vs. AWS CDK](/docs/iac/comparisons/cloud-template-transpilers/aws-cdk/)
- [Pulumi vs. Terraform](/docs/iac/comparisons/terraform/)
- [Migrating from AWS CloudFormation to Pulumi](/docs/iac/guides/migration/migrating-to-pulumi/from-cloudformation/)

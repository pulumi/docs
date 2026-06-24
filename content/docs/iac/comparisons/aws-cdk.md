---
title_tag: "Pulumi vs. AWS CDK"
meta_desc: "Compare Pulumi and AWS CDK: language support, multi-cloud coverage, state, secrets, policy, and migration paths. Neutral, side-by-side, with adoption guidance."
title: AWS CDK
h1: Pulumi vs. AWS CDK
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: AWS CDK
        parent: iac-comparisons
        weight: 25
        identifier: iac-comparisons-aws-cdk
    concepts:
        parent: vs
        weight: 25
aliases:
- /docs/intro/vs/cloud-template-transpilers/aws-cdk/
- /docs/concepts/vs/cloud-template-transpilers/aws-cdk/
- /docs/iac/concepts/vs/cloud-template-transpilers/aws-cdk/
- /docs/iac/comparisons/cloud-template-transpilers/aws-cdk/
- /docs/intro/vs/cloud_template_transpilers/
- /docs/concepts/vs/cloud-template-transpilers/
- /docs/iac/concepts/vs/cloud-template-transpilers/
- /docs/iac/comparisons/cloud-template-transpilers/
---

Pulumi and [AWS Cloud Development Kit (CDK)](https://aws.amazon.com/cdk/) are both infrastructure as code tools that let you author cloud resources in general-purpose programming languages. They differ in how programs are turned into provisioned infrastructure: Pulumi runs programs directly through its own deployment engine and supports any cloud or SaaS platform through the [Pulumi Registry](/registry/), while AWS CDK transpiles programs into [AWS CloudFormation](/docs/iac/comparisons/cloudformation/) templates that the AWS CloudFormation service deploys, and supports AWS only.

This page covers what each tool is, a feature-by-feature comparison, the most important differences in detail, and the available paths for adopting Pulumi alongside or instead of AWS CDK.

## What is Pulumi?

{{< what-is-pulumi >}}

For users coming from AWS CDK, the most relevant Pulumi providers are the [AWS Classic](/registry/packages/aws/) provider (built on the AWS Terraform provider) and the [AWS Cloud Control](/registry/packages/aws-native/) provider, which is generated from the AWS Cloud Control API — the same API CloudFormation uses — and offers same-day coverage of new AWS resources.

## What is AWS CDK?

AWS Cloud Development Kit (CDK) is an AWS-maintained framework, released in 2018, for defining AWS infrastructure in TypeScript, Python, Go, C#, and Java. CDK is a [transpiler](https://en.wikipedia.org/wiki/Source-to-source_compiler) (a.k.a. source-to-source compiler): running `cdk synth` produces an [AWS Cloud Assembly](https://docs.aws.amazon.com/cdk/v2/guide/apps.html#apps_cloud_assembly) — CloudFormation JSON or YAML templates plus other deployment assets — which is uploaded to Amazon S3/ECR and deployed by the [AWS CloudFormation](/docs/iac/comparisons/cloudformation/) service. CDK is AWS-only. The CDK framework is open source under the [Apache 2.0 license](https://github.com/aws/aws-cdk/blob/main/LICENSE); the CloudFormation deployment engine it depends on is a closed-source AWS service.

## Detailed comparison

| Feature | Pulumi | AWS CDK |
| --- | --- | --- |
| Language support | Python, TypeScript, JavaScript, Go, C#, Java, and YAML — general-purpose languages with familiar syntax for loops, conditionals, and abstractions | TypeScript, JavaScript, Python, Go, C#, and Java |
| Cloud and service support | [Pulumi Registry](/registry/) of packages, including [bridged, native, parameterized, and dynamic providers](/docs/iac/concepts/providers/#types-of-providers); first-party native providers for [Kubernetes](/registry/packages/kubernetes/) and [Azure Native](/registry/packages/azure-native/) generated from upstream API schemas; [any Terraform provider](/docs/iac/concepts/providers/any-terraform-provider/) can be adapted into a Pulumi provider | AWS only; third-party resources are supported through [CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) extensions and [custom resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-custom-resources.html) backed by AWS Lambda |
| Transpiled to another format? | No — programs run directly in their host language | Yes — programs are synthesized into CloudFormation templates and an [AWS Cloud Assembly](https://docs.aws.amazon.com/cdk/v2/guide/apps.html#apps_cloud_assembly) |
| State management | [Managed by Pulumi Cloud by default](/docs/iac/concepts/state-and-backends/); self-managed backends include Amazon S3, Azure Blob Storage, Google Cloud Storage, local files, and others | Managed by the CloudFormation service inside the AWS account; no user-accessible state file |
| Secrets management | [Encrypted in transit and at rest](/docs/iac/concepts/secrets/) in the state file by default, with per-stack encryption keys; pluggable KMS providers (AWS KMS, Azure Key Vault, Google Cloud KMS, HashiCorp Vault) | No built-in secrets primitive; sensitive values are typically passed via [`NoEcho` parameters](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html) or [dynamic references](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html) to AWS Secrets Manager or SSM Parameter Store |
| Execution model | Local CLI, programmatic via [Automation API](/docs/iac/concepts/automation-api/), or remote runs in [Pulumi Deployments](/docs/deployments/) | `cdk deploy` invokes the AWS CloudFormation service; can also run through AWS CodePipeline or any CI/CD tool that wraps the CDK CLI |
| Rollback on failed operation | Failed updates leave the stack in a partially-updated state; subsequent `pulumi up` runs reconcile toward the desired state, and you can roll forward by reverting program code | [Automatic stack rollback](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-rollback-triggers.html) on failed create or update; configurable rollback triggers and `DisableRollback` for debugging |
| Programmatic API for tools and platforms | [Automation API](/docs/iac/concepts/automation-api/) — a programmatic SDK for building custom CLIs, internal developer platforms, and services that drive `up`, `preview`, and `destroy` without shelling out to the Pulumi CLI | No embeddable SDK; orchestration goes through the CDK CLI, the AWS CLI, AWS SDKs, or the CloudFormation API |
| Modularity and reuse | [Component Resources](/docs/iac/concepts/components/) authored in any supported language; [Pulumi Packages](/docs/iac/concepts/packages/) let a component written in one language be consumed from any Pulumi language; language-native package managers (npm, PyPI, NuGet, Maven, Go modules); and the [Pulumi Registry](/registry/) for publicly available packages | [Constructs](https://docs.aws.amazon.com/cdk/v2/guide/constructs.html) — reusable abstractions built on the [constructs](https://github.com/aws/constructs) library and published to language-specific package managers; the [Construct Hub](https://constructs.dev/) indexes public constructs |
| Import existing resources | [`pulumi import`](/docs/iac/guides/migration/import/) and the [`import` resource option](/docs/iac/concepts/resources/options/import/), both of which generate code in your language | [Resource import](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import.html) through a CloudFormation change set, with a hand-authored CDK wrapper around the imported resources |
| Policy as code | [Pulumi Policies](/docs/insights/policy/) — open source, with rules written in Python, TypeScript, or Open Policy Agent Rego; Pulumi Cloud commercial plans add centralized policy management plus [Pulumi-maintained policy packs](/docs/insights/policy/policy-packs/pre-built-packs/) for compliance frameworks like CIS, PCI DSS, and NIST | [CloudFormation Hooks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/hooks.html) (authored in Java, Python, or TypeScript and registered with the CloudFormation Registry) and [CloudFormation Guard](https://docs.aws.amazon.com/cfn-guard/latest/ug/what-is-guard.html) for policy-as-code rules |
| Open source | Yes — [Apache License 2.0](https://github.com/pulumi/pulumi/blob/master/LICENSE) | The CDK framework is [Apache License 2.0](https://github.com/aws/aws-cdk/blob/main/LICENSE); the CloudFormation deployment engine it depends on is a closed-source AWS service |
| Commercial option | [Pulumi Cloud](/docs/iac/concepts/pulumi-cloud/) | None — CDK is part of AWS and has no separate commercial tier |

## Key differences

### Language support and the authoring experience

Pulumi programs are written in general-purpose languages and run directly through Pulumi's deployment engine. Authors get loops, conditionals, classes, package management, IDE features (autocomplete, type checking, refactoring, go-to-definition), and the testing frameworks that already exist in those ecosystems. AWS CDK programs are also written in general-purpose languages, but every program is synthesized into CloudFormation templates before deployment, so CDK testing centers on assertions against the synthesized template rather than the program's own object graph. Pulumi additionally supports [YAML](/docs/iac/languages-sdks/yaml/) for users who prefer a markup format.

### Cloud and service coverage

AWS CDK manages AWS resources only. Third-party support is added through CloudFormation Registry extensions and custom resources backed by AWS Lambda. CDK organizes its abstractions into three levels — L1 (auto-generated CloudFormation bindings), L2 (curated higher-level constructs), and L3 (multi-resource patterns) — but all three levels target AWS.

Pulumi targets any cloud or SaaS platform through the [Pulumi Registry](/registry/), which includes [bridged, native, parameterized, and dynamic providers](/docs/iac/concepts/providers/#types-of-providers). For AWS specifically, Pulumi offers the [AWS Classic](/registry/packages/aws/) provider (built on the AWS Terraform provider) and the [AWS Cloud Control](/registry/packages/aws-native/) provider, generated from the AWS Cloud Control API for same-day coverage of new AWS resources. Pulumi also maintains native providers for [Kubernetes](/registry/packages/kubernetes/) and [Azure Native](/registry/packages/azure-native/) generated directly from each platform's API schema. When a resource is not available in a Pulumi provider, Pulumi can [adapt any Terraform provider](/docs/iac/concepts/providers/any-terraform-provider/) for use from a Pulumi program.

### Execution and rollbacks

AWS CDK runs deployments through the AWS CloudFormation service. CDK inherits CloudFormation's properties, including its [500-resource-per-template limit](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html), [automatic stack rollback](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-rollback-triggers.html) on failed create or update operations, and the minutes-scale feedback loop of CloudFormation change sets. The synthesis step adds an additional template-generation phase between code and deployment.

Pulumi runs deployments through the local CLI, programmatically through the [Automation API](/docs/iac/concepts/automation-api/), or remotely through [Pulumi Deployments](/docs/deployments/). Failed Pulumi updates leave the stack in a partially-updated state; subsequent `pulumi up` runs reconcile toward the desired state, and you can roll forward by reverting program code. The two models trade off differently between automated cleanup on failure (CloudFormation/CDK) and direct, scriptable control over the deployment loop (Pulumi).

### Secrets handling

Pulumi treats secrets as a first-class primitive. Values marked as secrets are encrypted in transit and at rest in the state file, anything derived from a secret is also encrypted, and each stack has its own encryption key. The default encryption provider can be replaced with [AWS KMS, Azure Key Vault, Google Cloud KMS, or HashiCorp Vault](/docs/iac/concepts/secrets/#available-encryption-providers). AWS CDK has no built-in secrets primitive; sensitive values are typically passed in through [`NoEcho` parameters](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html) or through [dynamic references](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html) that resolve to values in AWS Secrets Manager or SSM Parameter Store at deploy time.

### Policy as code

[Pulumi Policies](/docs/insights/policy/) is open source and free. Policies can be written in Python, TypeScript, or Open Policy Agent Rego, and Pulumi Cloud adds centralized management, policy groups, and enforcement across stacks. Pulumi Cloud commercial plans also include [Pulumi-maintained policy packs](/docs/insights/policy/policy-packs/pre-built-packs/) for common compliance frameworks (CIS, PCI DSS, HITRUST, NIST), so teams don't have to author and maintain those rules themselves. CDK inherits CloudFormation's policy options: [CloudFormation Hooks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/hooks.html), which run pre-provisioning checks authored in Java, Python, or TypeScript and registered with the CloudFormation Registry, and [CloudFormation Guard](https://docs.aws.amazon.com/cfn-guard/latest/ug/what-is-guard.html), an open-source CLI for evaluating templates against rules.

### Modularity and reuse

Pulumi's [Component Resources](/docs/iac/concepts/components/) are runtime objects with explicit parent/child relationships, so a component and the resources inside it form a coherent unit in plan output, deletion, and state. Components can be authored in one language and consumed from any other supported language by publishing them as a [Pulumi Package](/docs/iac/concepts/packages/). AWS CDK offers [Constructs](https://docs.aws.amazon.com/cdk/v2/guide/constructs.html) built on the [constructs](https://github.com/aws/constructs) library and published as language-specific packages; public constructs are indexed by the [Construct Hub](https://constructs.dev/). Cross-language consumption of a single construct requires that the construct be authored with [jsii](https://github.com/aws/jsii) and published to multiple package managers.

### Automation API

The [Automation API](/docs/iac/concepts/automation-api/) lets a host application drive Pulumi without shelling out to the CLI. Practical uses include embedding stack creation in a SaaS product, building an internal developer platform that provisions environments per team or per branch, generating ephemeral preview environments from CI, and orchestrating cross-cloud deployments where each step runs as part of a larger workflow. AWS CDK is invoked through the `cdk` CLI and does not provide an equivalent embeddable SDK.

## When to choose Pulumi vs. AWS CDK

**Choose Pulumi when** you:

1. Manage infrastructure across multiple clouds or SaaS providers (Azure, Google Cloud, Kubernetes, Datadog, Cloudflare, etc.) and want one tool for all of it.
1. Want to run programs directly without a CloudFormation synthesis step, including the ability to test the program's own object graph rather than the synthesized template.
1. Need an embeddable SDK ([Automation API](/docs/iac/concepts/automation-api/)) to drive deployments from a host application — internal developer platforms, SaaS products, or ephemeral preview environments per pull request.
1. Want built-in secrets encryption, pluggable KMS providers, and per-stack encryption keys without bolting on a separate service.
1. Want a free, open-source policy-as-code engine with rules in Python, TypeScript, or Rego.

**Choose AWS CDK when** you:

1. Provision only AWS resources and want to stay within AWS-managed tooling (CloudFormation, AWS CLI, AWS SDKs, AWS CodePipeline) end to end.
1. Depend on CloudFormation-specific features such as automatic stack rollback on failure, [Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html) integration, or [StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html) for multi-account deployments.
1. Have an existing investment in CDK constructs, custom resources, and team expertise that you don't want to migrate.

The two can also coexist — see [Adoption](#adoption-coexistence-conversion-and-import) below.

## Adoption: coexistence, conversion, and import

There are several common paths for adopting Pulumi alongside or in place of AWS CDK, and they can be combined:

1. **Use AWS CDK alongside Pulumi.** The [Pulumi CDK Adapter](https://github.com/pulumi/pulumi-cdk) embeds CDK constructs directly inside Pulumi programs, so existing CDK constructs continue to work while the surrounding program is managed by Pulumi. Outputs flow in both directions between CDK constructs and other Pulumi resources. See [Using Pulumi with AWS CDK](/docs/iac/guides/migration/migrating-to-pulumi/migrating-from-cdk/using-pulumi-cdk/) and the [Pulumi CDK guide](/docs/iac/guides/clouds/aws/cdk/).
1. **Import existing resources.** [`pulumi import`](/docs/iac/guides/migration/import/) and the [`import` resource option](/docs/iac/concepts/resources/options/import/) bring already-provisioned AWS resources under Pulumi management and generate the corresponding code in your chosen language.
1. **Automated migration with Pulumi Neo (recommended).** [Pulumi Neo](/product/neo/) automates the conversion of an existing CDK application — converting code, importing existing CloudFormation resources, and running `pulumi preview` to verify zero changes — without downtime. See [Migrating existing AWS CDK applications to Pulumi](/docs/iac/guides/migration/migrating-to-pulumi/migrating-from-cdk/migrating-existing-cdk-app/).

For a complete walkthrough, see [Migrating from AWS CDK to Pulumi](/docs/iac/guides/migration/migrating-to-pulumi/from-cdk/).

## Frequently asked questions

### Can Pulumi run AWS CDK constructs?

Yes. The [Pulumi CDK Adapter](https://github.com/pulumi/pulumi-cdk) embeds CDK constructs directly inside Pulumi programs, so existing CDK constructs and stacks can be referenced from a Pulumi program. Outputs from CDK constructs can feed other Pulumi resources, and outputs from Pulumi resources can feed CDK constructs. See the [Pulumi CDK guide](/docs/iac/guides/clouds/aws/cdk/) for details.

### How do I migrate from AWS CDK to Pulumi?

You have three options that can be combined: use [Pulumi Neo](/product/neo/) for automated conversion and import; bring existing resources under Pulumi management with [`pulumi import`](/docs/iac/guides/migration/import/); or run both tools side by side using the [Pulumi CDK Adapter](https://github.com/pulumi/pulumi-cdk) until you're ready to cut over. The [migration guide](/docs/iac/guides/migration/migrating-to-pulumi/from-cdk/) has the full walkthrough.

### Does Pulumi cover the same AWS resources as AWS CDK?

Yes. The [AWS Cloud Control](/registry/packages/aws-native/) provider is generated from the AWS Cloud Control API — the same API CloudFormation uses — so it offers same-day coverage of new AWS resources. The [AWS Classic](/registry/packages/aws/) provider, built on the AWS Terraform provider, offers long-standing, comprehensive coverage and is appropriate for the majority of production use cases.

### Is Pulumi free like AWS CDK?

The Pulumi CLI and SDKs are open source under Apache 2.0 and free to use. [Pulumi Cloud](/docs/iac/concepts/pulumi-cloud/) has a free Individual tier and paid plans that add managed state, RBAC, audit logs, policy management, and other features for running Pulumi at organizational scale. AWS CDK is open source; the AWS CloudFormation deployment engine it depends on has no usage cost beyond the resources it manages, but is itself a closed-source AWS service.

### Does Pulumi have automatic rollback like CloudFormation/CDK?

No. On a failed update, Pulumi leaves the stack in a partially-updated state and reports exactly which resources changed. You roll forward by fixing the program and running `pulumi up` again, or revert the program to a previous commit and re-deploy. This gives direct, scriptable control over the deployment loop at the cost of CloudFormation's automated cleanup behavior.

### Can I use Pulumi for non-AWS resources alongside AWS CDK for AWS?

Yes — and this is one of the more common adoption patterns. Teams keep AWS infrastructure in CDK while using Pulumi for Kubernetes, Azure, Google Cloud, Datadog, Cloudflare, or other SaaS platforms, then optionally migrate AWS later. The [Pulumi CDK Adapter](https://github.com/pulumi/pulumi-cdk) also supports the reverse pattern, where a Pulumi program embeds existing CDK constructs.

### How does the CloudFormation 500-resource-per-stack limit compare to Pulumi?

AWS CDK inherits CloudFormation's [500-resource-per-template limit](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html); teams working around it typically split deployments across nested stacks or multiple top-level stacks. Pulumi imposes no equivalent hard limit on resources per stack, so very large deployments do not require artificial decomposition.

### Can Pulumi detect drift like CloudFormation?

Yes. [`pulumi refresh`](/docs/iac/cli/commands/pulumi_refresh/) compares the state file to the actual state in the cloud and reports differences, and `pulumi preview --diff` shows what would change on the next update. Pulumi Cloud commercial plans add [scheduled drift detection and remediation](/docs/deployments/concepts/drift/).

## Next steps

- [Get started with Pulumi](/docs/iac/get-started/)
- [Pulumi vs. AWS CloudFormation](/docs/iac/comparisons/cloudformation/)
- [Pulumi vs. CDKTF](/docs/iac/comparisons/cdktf/)
- [Pulumi vs. Terraform](/docs/iac/comparisons/terraform/)
- [Migrating from AWS CDK to Pulumi](/docs/iac/guides/migration/migrating-to-pulumi/from-cdk/)

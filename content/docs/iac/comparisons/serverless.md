---
title_tag: "Pulumi vs. Serverless Framework"
meta_desc: "Compare Pulumi and the Serverless Framework: a multi-cloud IaC platform in general-purpose languages versus an AWS-focused tool for deploying Lambda apps."
title: Serverless Framework
h1: Pulumi vs. Serverless Framework
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Serverless Framework
        parent: iac-comparisons
        weight: 5
    concepts:
        parent: vs
        weight: 5
aliases:
- /docs/reference/vs/serverless/
- /docs/intro/vs/serverless/
- /docs/concepts/vs/serverless/
- /docs/iac/concepts/vs/serverless/
---

Pulumi and the [Serverless Framework](https://www.serverless.com/framework/docs) are both tools for provisioning cloud infrastructure as code, but they have different scopes. Pulumi is a general-purpose infrastructure as code platform that provisions resources across any cloud or SaaS provider using general-purpose languages; the Serverless Framework is an AWS-focused tool for deploying serverless applications — primarily AWS Lambda functions and closely related resources — defined in a `serverless.yml` file.

This page covers what each tool is, a feature-by-feature comparison, the most important differences in detail, and the available paths for adopting Pulumi alongside or instead of the Serverless Framework.

## What is Pulumi?

{{< what-is-pulumi >}}

For users coming from the Serverless Framework, the most relevant Pulumi providers are the [AWS Classic](/registry/packages/aws/) provider (built on the AWS Terraform provider) and the [AWS Cloud Control](/registry/packages/aws-native/) provider, which is generated from the AWS Cloud Control API and offers same-day coverage of new AWS resources. The same Pulumi program can also manage resources outside AWS — Azure, Google Cloud, Kubernetes, and SaaS platforms like Datadog, Auth0, and Cloudflare — through the [Pulumi Registry](/registry/).

## What is Serverless Framework?

The [Serverless Framework](https://www.serverless.com/framework/docs) is a tool maintained by [Serverless, Inc.](https://github.com/serverless/serverless) for building and deploying serverless applications. It is AWS-focused: applications are described in a `serverless.yml` file, which the framework compiles into an AWS CloudFormation template and deploys as a CloudFormation stack. Its model centers on AWS Lambda functions and the resources that surround them — API Gateway, event sources, IAM roles, and CloudWatch log groups — with any additional infrastructure declared in a [`resources` block](https://www.serverless.com/framework/docs/providers/aws/guide/resources) containing raw CloudFormation. Functionality beyond the core is added through a large [plugin ecosystem](https://www.serverless.com/plugins).

The Serverless Framework is operated through a CLI, with the [Serverless Framework Dashboard](https://www.serverless.com/framework/docs/guides/dashboard) providing a web console for metrics, CI/CD, and subscription management. Versions 3 and earlier were released under the MIT license; [version 4](https://www.serverless.com/blog/serverless-framework-v4-a-new-model), the current line, is distributed under a proprietary license and is not open source. Under the [V4 model](https://www.serverless.com/pricing), the CLI is free for individuals and for organizations below a stated annual revenue threshold; organizations above that threshold require a paid Serverless Subscription. Provider support outside AWS (Azure, Google Cloud, and others) historically existed through community plugins but is deprecated in V4.

## Detailed comparison

| Feature | Pulumi | Serverless Framework |
| --- | --- | --- |
| Language support | Python, TypeScript, JavaScript, Go, C#, Java, and YAML — general-purpose languages with familiar syntax for loops, conditionals, and abstractions | [`serverless.yml`](https://www.serverless.com/framework/docs/providers/aws/guide/serverless.yml) — a YAML configuration file with a [variable system](https://www.serverless.com/framework/docs/guides/variables) for limited dynamic values |
| Cloud and service support | [Pulumi Registry](/registry/) of packages, including [bridged, native, parameterized, and dynamic providers](/docs/iac/concepts/providers/#types-of-providers); first-party native providers for [Kubernetes](/registry/packages/kubernetes/) and [Azure Native](/registry/packages/azure-native/) generated from upstream API schemas; [any Terraform provider](/docs/iac/concepts/providers/any-terraform-provider/) can be adapted into a Pulumi provider | AWS is the primary, fully supported provider; non-AWS providers historically existed through community plugins but are deprecated in [version 4](https://www.serverless.com/blog/serverless-framework-v4-a-new-model) |
| Transpiled to another format? | No — programs run directly in their host language | Yes — for AWS, `serverless.yml` is compiled into an [AWS CloudFormation template](https://www.serverless.com/framework/docs/providers/aws/guide/resources) that CloudFormation then deploys |
| State management | [Managed by Pulumi Cloud by default](/docs/iac/concepts/state-and-backends/); self-managed backends include Amazon S3, Azure Blob Storage, Google Cloud Storage, local files, and others | No independent state store; for AWS, state is the CloudFormation stack (named `{service}-{stage}`) managed inside the AWS account |
| Secrets management | [Encrypted in transit and at rest](/docs/iac/concepts/secrets/) in the state file by default, with per-stack encryption keys; pluggable KMS providers (AWS KMS, Azure Key Vault, Google Cloud KMS, HashiCorp Vault) | No built-in secrets primitive; sensitive values are referenced at deploy time through the [variable system](https://www.serverless.com/framework/docs/guides/variables/aws/ssm) from AWS SSM Parameter Store or AWS Secrets Manager |
| Execution model | Local CLI, programmatic via [Automation API](/docs/iac/automation-api/), or remote runs in [Pulumi Deployments](/docs/deployments/) | Local CLI (`serverless deploy`), with the [Serverless Framework Dashboard](https://www.serverless.com/framework/docs/guides/dashboard) for metrics, CI/CD, and subscription management |
| Rollback on failed operation | Failed updates leave the stack in a partially-updated state; subsequent `pulumi up` runs reconcile toward the desired state, and you can roll forward by reverting program code | [`serverless rollback`](https://www.serverless.com/framework/docs/providers/aws/cli-reference/rollback) reverts a service to a previous deployment, and the underlying CloudFormation service rolls back failed create or update operations automatically |
| Programmatic API for tools and platforms | [Automation API](/docs/iac/automation-api/) — a programmatic SDK for building custom CLIs, internal developer platforms, and services that drive `up`, `preview`, and `destroy` without shelling out to the Pulumi CLI | No embeddable SDK; orchestration goes through `serverless` CLI invocations |
| Modularity and reuse | [Component Resources](/docs/iac/concepts/components/) authored in any supported language; [Pulumi Packages](/docs/iac/concepts/packages/) let a component written in one language be consumed from any Pulumi language; language-native package managers (npm, PyPI, NuGet, Maven, Go modules); and the [Pulumi Registry](/registry/) for publicly available packages | [Plugins](https://www.serverless.com/plugins) extend CLI behavior; configuration is reused by composing `serverless.yml` files and referencing external files through the variable system |
| Import existing resources | [`pulumi import`](/docs/iac/guides/migration/import/) and the [`import` resource option](/docs/iac/concepts/resources/options/import/), both of which generate code in your language | No first-class import command; existing resources are brought in through [CloudFormation's resource import](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import.html) and then described in `serverless.yml` |
| Policy as code | [Pulumi Policies](/docs/insights/policy/) — open source, with rules written in Python, TypeScript, or Open Policy Agent Rego; Pulumi Cloud commercial plans add centralized policy management plus [Pulumi-maintained policy packs](/docs/insights/policy/policy-packs/pre-built-packs/) for compliance frameworks like CIS, PCI DSS, and SOC 2 | No built-in policy-as-code feature; teams typically rely on external tools such as [CloudFormation Guard](https://docs.aws.amazon.com/cfn-guard/latest/ug/what-is-guard.html) or [Open Policy Agent](https://www.openpolicyagent.org/) against the generated CloudFormation template |
| Open source | Yes — [Apache License 2.0](https://github.com/pulumi/pulumi/blob/master/LICENSE) | Versions 3 and earlier were MIT-licensed; [version 4](https://www.serverless.com/blog/serverless-framework-v4-a-new-model) is distributed under a proprietary license |
| Commercial option | [Pulumi Cloud](/docs/iac/concepts/pulumi-cloud/) | [Serverless Subscription](https://www.serverless.com/pricing) — required for organizations above a stated annual revenue threshold; free for individuals and smaller organizations |

## Key differences

### Language support and the authoring experience

The Serverless Framework is configured through `serverless.yml`, a YAML file with a [variable system](https://www.serverless.com/framework/docs/guides/variables) that resolves values from files, the CLI, environment variables, and AWS parameter stores. This keeps configurations declarative, but dynamic logic — loops, conditionals, computed values — is limited to what the variable system and plugins provide. Pulumi programs are written in general-purpose languages, so authors get loops, conditionals, classes, package management, IDE features (autocomplete, type checking, refactoring, go-to-definition), and the testing frameworks that already exist in those ecosystems. Pulumi also supports [YAML](/docs/iac/languages-sdks/yaml/) for users who prefer a markup format.

### Scope: serverless applications vs. general-purpose infrastructure

The Serverless Framework is built around serverless applications. Its model is function-centric: you declare functions and the events that trigger them, and the framework generates the Lambda functions, API Gateway resources, IAM roles, and log groups needed to run them. Infrastructure that is not a function or a function trigger — databases, queues, VPCs, DNS — is declared in the [`resources` block](https://www.serverless.com/framework/docs/providers/aws/guide/resources) as raw CloudFormation, dropping out of the framework's higher-level abstractions. Pulumi is a general-purpose infrastructure as code platform: Lambda functions, databases, networking, Kubernetes clusters, and SaaS resources are all first-class resources expressed the same way in the same program, whether they are serverless or not.

### Cloud and service coverage

The Serverless Framework's fully supported target is AWS; non-AWS providers existed through community plugins but are deprecated in version 4. Pulumi targets any cloud or SaaS platform through the [Pulumi Registry](/registry/), which includes [bridged, native, parameterized, and dynamic providers](/docs/iac/concepts/providers/#types-of-providers). For AWS specifically, Pulumi offers the [AWS Classic](/registry/packages/aws/) provider, built on the AWS Terraform provider, and the [AWS Cloud Control](/registry/packages/aws-native/) provider, generated from the AWS Cloud Control API for same-day coverage of new AWS resources. Pulumi also maintains native providers for [Kubernetes](/registry/packages/kubernetes/) and [Azure Native](/registry/packages/azure-native/) generated directly from each platform's API schema, and can [adapt any Terraform provider](/docs/iac/concepts/providers/any-terraform-provider/) when a resource is not yet packaged in a Pulumi provider.

### Execution and rollbacks

The Serverless Framework runs through its CLI: `serverless deploy` compiles `serverless.yml` to a CloudFormation template and hands it to the CloudFormation service, which executes the changes. On a failed create or update, CloudFormation rolls the stack back to its last stable state automatically, and [`serverless rollback`](https://www.serverless.com/framework/docs/providers/aws/cli-reference/rollback) can revert a service to an earlier deployment on demand. Pulumi runs deployments through the local CLI, programmatically through the [Automation API](/docs/iac/automation-api/), or remotely through [Pulumi Deployments](/docs/deployments/). Failed Pulumi updates leave the stack in a partially-updated state; subsequent `pulumi up` runs reconcile toward the desired state, and you can roll forward by reverting program code. The two models trade off differently between automated cleanup on failure (CloudFormation, via the Serverless Framework) and direct, scriptable control over the deployment loop (Pulumi).

### Secrets handling

Pulumi treats secrets as a first-class primitive. Values marked as secrets are encrypted in transit and at rest in the state file, anything derived from a secret is also encrypted, and each stack has its own encryption key. The default encryption provider can be replaced with [AWS KMS, Azure Key Vault, Google Cloud KMS, or HashiCorp Vault](/docs/iac/concepts/secrets/#available-encryption-providers). The Serverless Framework has no built-in secrets primitive; sensitive values are referenced through the [variable system](https://www.serverless.com/framework/docs/guides/variables/aws/ssm), which resolves them at deploy time from AWS SSM Parameter Store or AWS Secrets Manager.

### Policy as code

[Pulumi Policies](/docs/insights/policy/) is open source and free. Policies can be written in Python, TypeScript, or Open Policy Agent Rego, and Pulumi Cloud adds centralized management, policy groups, and enforcement across stacks. Pulumi Cloud commercial plans also include [Pulumi-maintained policy packs](/docs/insights/policy/policy-packs/pre-built-packs/) for common compliance frameworks (CIS, PCI DSS, SOC 2, HITRUST, NIST), so teams don't have to author and maintain those rules themselves. The Serverless Framework has no built-in policy-as-code feature; teams typically evaluate the generated CloudFormation template with external tools such as [CloudFormation Guard](https://docs.aws.amazon.com/cfn-guard/latest/ug/what-is-guard.html) or [Open Policy Agent](https://www.openpolicyagent.org/).

### Modularity and reuse

The Serverless Framework reuses configuration by composing `serverless.yml` files, referencing external files through the variable system, and installing [plugins](https://www.serverless.com/plugins) that extend CLI behavior. Pulumi's [Component Resources](/docs/iac/concepts/components/) are runtime objects with explicit parent/child relationships, so a component and the resources inside it form a coherent unit in plan output, deletion, and state. Components can be authored in one language and consumed from any other supported language by publishing them as a [Pulumi Package](/docs/iac/concepts/packages/), and they are distributed through the language-native package managers teams already use.

### Automation API

The [Automation API](/docs/iac/automation-api/) lets a host application drive Pulumi without shelling out to the CLI. Practical uses include embedding stack creation in a SaaS product, building an internal developer platform that provisions environments per team or per branch, generating ephemeral preview environments from CI, and orchestrating cross-cloud deployments where each step runs as part of a larger workflow. The Serverless Framework is invoked through its CLI and does not provide an equivalent embeddable SDK; programmatic use means shelling out to the CLI and parsing its output.

## When to choose Pulumi vs. Serverless Framework

**Choose Pulumi when** you:

1. Manage more than serverless functions — databases, networking, Kubernetes, SaaS resources — and want one tool and one programming model for all of it.
1. Work across multiple clouds or SaaS providers, or expect to.
1. Want to write infrastructure in a general-purpose language with the testing frameworks, package managers, and IDE tooling that already exist in that ecosystem.
1. Need an embeddable SDK ([Automation API](/docs/iac/automation-api/)) to drive deployments from a host application — internal developer platforms, SaaS products, or ephemeral preview environments per pull request.
1. Want built-in secrets encryption, pluggable KMS providers, and per-stack encryption keys without bolting on a separate service.

**Choose the Serverless Framework when** you:

1. Build AWS serverless applications and want a tool whose model is centered on functions and their event triggers.
1. Have an existing investment in `serverless.yml` definitions, plugins, and team expertise that you don't want to migrate.
1. Want the framework's function-packaging and deployment conventions and are comfortable expressing other infrastructure as raw CloudFormation.

The two can also coexist — see [Adoption](#adoption-coexistence-import-and-rewrite) below.

## Adoption: coexistence, import, and rewrite

There are several common paths for adopting Pulumi alongside or in place of the Serverless Framework, and they can be combined:

1. **Use the Serverless Framework alongside Pulumi.** Because the Serverless Framework deploys through CloudFormation, a Pulumi program can reference an existing Serverless Framework stack and read its outputs — such as the API endpoint and function ARNs — through [`aws.cloudformation.getStack`](/registry/packages/aws/api-docs/cloudformation/getstack/). This lets you keep some services on the Serverless Framework while building new infrastructure with Pulumi.
1. **Import existing resources.** [`pulumi import`](/docs/iac/guides/migration/import/) and the [`import` resource option](/docs/iac/concepts/resources/options/import/) bring already-provisioned AWS resources under Pulumi management and generate the corresponding code in your chosen language.
1. **Rewrite `serverless.yml` as Pulumi code.** Translate your function and resource definitions into a Pulumi program, importing the underlying AWS resources as you go so nothing is recreated. The migration guide includes a `serverless.yml`-to-Pulumi resource mapping to work from.

For a complete walkthrough — including referencing stack outputs, the resource mapping, and step-by-step import instructions — see [Migrating from Serverless Framework to Pulumi](/docs/iac/guides/migration/migrating-to-pulumi/from-serverless/).

## Frequently asked questions

### How do I migrate from the Serverless Framework to Pulumi?

You have several options that can be combined: bring already-provisioned resources under Pulumi management with [`pulumi import`](/docs/iac/guides/migration/import/), rewrite your `serverless.yml` definitions as Pulumi code, or reference existing Serverless Framework stacks with [`aws.cloudformation.getStack`](/registry/packages/aws/api-docs/cloudformation/getstack/) and run both tools side by side until you're ready to cut over. See the [migration guide](/docs/iac/guides/migration/migrating-to-pulumi/from-serverless/) for a full walkthrough, including a `serverless.yml`-to-Pulumi resource mapping.

### Can Pulumi manage resources created by the Serverless Framework?

Yes. Because Serverless Framework services are CloudFormation stacks, a Pulumi program can read their outputs via [`aws.cloudformation.getStack`](/registry/packages/aws/api-docs/cloudformation/getstack/) to coexist with them, or use [`pulumi import`](/docs/iac/guides/migration/import/) to bring the underlying AWS resources under Pulumi management. The [migration guide](/docs/iac/guides/migration/migrating-to-pulumi/from-serverless/) covers retaining resources during the handoff so nothing is destroyed.

### Can Pulumi deploy serverless applications like the Serverless Framework?

Yes. Pulumi manages AWS Lambda functions, API Gateway, event source mappings, IAM roles, and log groups as first-class resources, the same way it manages any other infrastructure. The difference is scope: Pulumi expresses functions and non-function infrastructure in the same general-purpose program, rather than treating functions as the central abstraction and other resources as raw CloudFormation.

### Is Pulumi open source?

The Pulumi CLI and SDKs are open source under the Apache 2.0 license. [Pulumi Cloud](/docs/iac/concepts/pulumi-cloud/) is the commercial product, with a free Individual tier and paid plans that add managed state, RBAC, audit logs, policy management, and other features for running Pulumi at organizational scale. The Serverless Framework was MIT-licensed through version 3; version 4 is distributed under a proprietary license.

### Can I use Pulumi for non-AWS infrastructure alongside the Serverless Framework?

Yes — and this is a common adoption pattern. Teams keep AWS serverless services on the Serverless Framework while using Pulumi for Kubernetes, Azure, Google Cloud, Datadog, Cloudflare, or other platforms, then optionally migrate the AWS services later.

## Next steps

- [Get started with Pulumi](/docs/iac/get-started/)
- [Pulumi vs. AWS CloudFormation](/docs/iac/comparisons/cloudformation/)
- [Pulumi vs. AWS CDK](/docs/iac/comparisons/cloud-template-transpilers/aws-cdk/)
- [Migrating from Serverless Framework to Pulumi](/docs/iac/guides/migration/migrating-to-pulumi/from-serverless/)

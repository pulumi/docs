---
title_tag: "AWS | Pulumi Integrations"
meta_desc: AWS integration with Pulumi — providers, packages, architecture templates, guides, ESC integrations, cloud account scanning, and pre-built policy packs.
title: AWS
linktitle: AWS
h1: AWS
menu:
  integrations:
    name: AWS
    identifier: aws-clouds
    parent: integrations-clouds
    weight: 1
aliases:
- /docs/iac/clouds/aws/
- /docs/clouds/aws/
---

Build, deploy, and manage AWS infrastructure with Pulumi. This page links to every Pulumi capability for AWS: Infrastructure as Code, Environments, Secrets, and Configuration (ESC), cloud account scanning, and policy packs.

To start from scratch, follow the [get-started guide](/up/).

## Infrastructure as Code

[Pulumi IaC](/docs/iac/) lets you define cloud infrastructure using TypeScript, JavaScript, Python, Go, .NET, Java, YAML, or HCL — with deterministic deployments, a state backend, and a rich ecosystem of packages.

Pulumi provides several packages for working with AWS. Most projects combine more than one. For a deeper comparison, see [Choosing a Pulumi AWS provider](/docs/iac/guides/clouds/aws/providers/).

- [AWS provider](/registry/packages/aws/) — the default AWS provider. Uses the AWS SDK to manage all AWS services.
- [AWS Cloud Control provider](/registry/packages/aws-native/) — full coverage of resources available in the AWS Cloud Control API.
- [AWSx](/registry/packages/awsx/) — higher-level components that encapsulate AWS best practices.
- [AWS API Gateway](/registry/packages/aws-apigateway/) — simplified construction of AWS API Gateway REST APIs.
- [Amazon EKS](/registry/packages/eks/) — create and manage Amazon Elastic Kubernetes Service clusters with sensible defaults.
- [Docker](/registry/packages/docker/) — build and push Docker images to Amazon ECR or other registries.
- [Kubernetes](/registry/packages/kubernetes/) — deploy application workloads to Amazon EKS or any Kubernetes cluster.

## Tutorials, templates, and examples

The [Pulumi Dev Center](/dev/cloud/aws/) collects hands-on AWS content, filterable by language and topic:

- [Tutorials](/dev/browse/?type=tutorial&cloud=aws) — step-by-step guides to building on AWS with Pulumi.
- [Templates](/dev/browse/?type=template&cloud=aws) — ready-to-deploy starting points for common architectures. Run `pulumi new <template>` to bootstrap a project.
- [Examples](/dev/browse/?type=example&cloud=aws) — complete Pulumi programs you can read, run, and adapt.
- [Workshops](/dev/browse/?type=workshop&cloud=aws) — instructor-led workshops, live and on demand.

## Guides

- [Pulumi CDK Adapter for AWS](/docs/iac/guides/migration/migrating-to-pulumi/migrating-from-cdk/using-pulumi-cdk/) — use AWS CDK constructs inside a Pulumi program.
- [AWS CodePipeline & CodeDeploy](/docs/iac/operations/continuous-delivery/aws-code-services/) — drive Pulumi stack updates from AWS developer tools.

## Secrets & configuration (ESC)

[Pulumi ESC (Environments, Secrets, and Configuration)](/docs/esc/) is a centralized service for managing secrets, configuration, and short-lived credentials. It composes values from many sources — including AWS — into environments that Pulumi programs, CLIs, and CI/CD workflows can consume.

ESC integrates directly with AWS for short-lived credentials and secret retrieval:

- [AWS OIDC login](/docs/esc/providers/login/aws-login/) — generate short-lived AWS credentials for Pulumi programs and workflows.
- [AWS Secrets Manager](/docs/esc/providers/secrets/aws-secrets/) — pull secrets from Secrets Manager into ESC environments.
- [AWS Systems Manager Parameter Store](/docs/esc/providers/secrets/aws-parameter-store/) — pull configuration and secrets from Parameter Store into ESC environments.
- [AWS IAM credential rotation](/docs/esc/providers/rotators/aws-iam/) — rotate IAM access keys on a schedule.
- [AWS Lambda rotator](/docs/esc/operations/rotation/aws-lambda/) — rotate arbitrary secrets via an AWS Lambda function.

## Discovery

[Pulumi Discovery](/docs/discovery-governance/) continuously scans your clouds to build a searchable inventory of every resource — whether created by Pulumi or not — so you can find, audit, and govern cloud infrastructure across accounts, regions, and providers.

For AWS, Discovery connects AWS accounts (including AWS Partitions) to inventory existing resources, search across accounts, and export data. See [Add an AWS account](/docs/discovery-governance/get-started/create-a-discovery-account/) for a step-by-step setup guide and [Discovery overview](/docs/discovery-governance/concepts/discovery/) for background.

## Policy packs

[Pulumi Policies](/docs/discovery-governance/concepts/policy-as-code/) lets you enforce rules on infrastructure at preview and update time, rejecting stacks that violate security, cost, or compliance standards. [Pre-built policy packs](/docs/discovery-governance/guides/pre-built-policy-packs/) are maintained by Pulumi and cover common regulatory and best-practice frameworks.

For AWS:

- [Pulumi best practices for AWS](/docs/reference/pre-built-policy-packs/pulumi-best-practices/aws/) — Pulumi-authored policies for common AWS misconfigurations.
- [CIS AWS Foundations Benchmark](/docs/reference/pre-built-policy-packs/cis/aws/)
- [NIST 800-53 for AWS](/docs/reference/pre-built-policy-packs/nist/aws/)
- [PCI DSS for AWS](/docs/reference/pre-built-policy-packs/pci-dss/aws/)
- [HITRUST CSF for AWS](/docs/reference/pre-built-policy-packs/hitrust/aws/)
- [ISO/IEC 27001 for AWS](/docs/reference/pre-built-policy-packs/iso-27001/aws/)
- [CMMC 2.0 for AWS](/docs/reference/pre-built-policy-packs/cmmc/aws/)
- [CIS Kubernetes Benchmark on AWS](/docs/reference/pre-built-policy-packs/cis-kubernetes/aws/) — for EKS clusters.
- [AWS Organizations Tag Policies](/docs/reference/pre-built-policy-packs/aws-organizations-tag-policies/aws/) — enforce Organizations tagging standards on Pulumi-managed resources.
- [AWS Organizations tag policies in Discovery](/docs/discovery-governance/guides/aws-organizations-tag-policies/) — integration with Pulumi Discovery.

## Migration

Migrate existing AWS infrastructure from another IaC tool to Pulumi. The guides below walk through converting or coexisting with each source format.

- [From CloudFormation](/docs/iac/guides/migration/migrating-to-pulumi/from-cloudformation/) — convert CloudFormation templates to Pulumi.
- [From AWS CDK](/docs/iac/guides/migration/migrating-to-pulumi/from-cdk/) — move from AWS CDK to Pulumi, or use CDK constructs inside Pulumi programs.
- [From Terraform](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/) — convert Terraform HCL and state to Pulumi.

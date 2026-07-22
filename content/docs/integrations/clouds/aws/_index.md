---
title_tag: "AWS | Pulumi Integrations"
meta_desc: AWS integration with Pulumi — providers, packages, architecture templates, guides, ESC integrations, Insights account scanning, and pre-built policy packs.
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

Build, deploy, and manage AWS infrastructure with Pulumi. This page links to every Pulumi capability for AWS: Infrastructure as Code, Environments, Secrets, and Configuration (ESC), Insights account scanning, and policy packs.

To start from scratch, follow the [AWS get-started guide](/docs/iac/get-started/aws/).

## Infrastructure as Code

[Pulumi IaC](/docs/iac/) lets you define cloud infrastructure using TypeScript, Python, Go, C#, Java, or YAML — with deterministic deployments, a state backend, and a rich ecosystem of packages.

Pulumi provides several packages for working with AWS. Most projects combine more than one. For a deeper comparison, see [Choosing a Pulumi AWS provider](/docs/iac/guides/clouds/aws/providers/).

- [AWS provider](/registry/packages/aws/) — the default AWS provider. Uses the AWS SDK to manage all AWS services.
- [AWS Cloud Control provider](/registry/packages/aws-native/) — full coverage of resources available in the AWS Cloud Control API.
- [AWSx](/registry/packages/awsx/) — higher-level components that encapsulate AWS best practices.
- [AWS API Gateway](/registry/packages/aws-apigateway/) — simplified construction of AWS API Gateway REST APIs.
- [Amazon EKS](/registry/packages/eks/) — create and manage Amazon Elastic Kubernetes Service clusters with sensible defaults.
- [Docker](/registry/packages/docker/) — build and push Docker images to Amazon ECR or other registries.
- [Kubernetes](/registry/packages/kubernetes/) — deploy application workloads to Amazon EKS or any Kubernetes cluster.

## Architecture templates

[Pulumi templates](/templates/) are ready-to-deploy starting points for common architectures. Run `pulumi new <template>` to bootstrap a new project.

Start new AWS projects from a pre-built template:

- [Container service on AWS](/templates/container-service/aws/) — containerized service on Amazon ECS Fargate.
- [Serverless application on AWS](/templates/serverless-application/aws/) — AWS Lambda behind API Gateway with supporting resources.
- [Static website on AWS](/templates/static-website/aws/) — S3-hosted static site with CloudFront CDN.
- [Virtual machine on AWS](/templates/virtual-machine/aws/) — EC2 instance with configurable networking.
- [Kubernetes cluster on AWS](/templates/kubernetes/aws/) — Amazon EKS cluster ready for workloads.

## Guides

Hands-on Infrastructure as Code guides for building on AWS with Pulumi.

- [Pulumi CDK Adapter for AWS](/docs/iac/guides/clouds/aws/cdk/) — use AWS CDK constructs inside a Pulumi program.
- [AWS Identity & Access Management (IAM)](/docs/iac/guides/clouds/aws/iam/) — model IAM roles, policies, and users in code.
- [AWS Virtual Private Cloud (VPC)](/docs/iac/guides/clouds/aws/vpc/) — define VPCs, subnets, and routing.
- [AWS Lambda & serverless events](/docs/iac/guides/clouds/aws/lambda/) — author Lambda functions and event sources in code.
- [Amazon ECS](/docs/iac/guides/clouds/aws/ecs/) — run containers on Elastic Container Service.
- [Amazon EKS](/docs/iac/guides/clouds/aws/eks/) — run workloads on Elastic Kubernetes Service.
- [Amazon ECR](/docs/iac/guides/clouds/aws/ecr/) — build and publish images to Elastic Container Registry.
- [Elastic Load Balancing](/docs/iac/guides/clouds/aws/elb/) — configure application and network load balancers.
- [AWS API Gateway](/docs/iac/guides/clouds/aws/api-gateway/) — configure HTTP and REST APIs on API Gateway.
- [AWS CodePipeline & CodeDeploy](/docs/iac/operations/continuous-delivery/aws-code-services/) — drive Pulumi stack updates from AWS developer tools.

## Secrets & configuration (ESC)

[Pulumi ESC (Environments, Secrets, and Configuration)](/docs/esc/) is a centralized service for managing secrets, configuration, and short-lived credentials. It composes values from many sources — including AWS — into environments that Pulumi programs, CLIs, and CI/CD workflows can consume.

ESC integrates directly with AWS for short-lived credentials and secret retrieval:

- [AWS OIDC login](/docs/esc/providers/login/aws-login/) — generate short-lived AWS credentials for Pulumi programs and workflows.
- [AWS Secrets Manager](/docs/esc/providers/secrets/aws-secrets/) — pull secrets from Secrets Manager into ESC environments.
- [AWS Systems Manager Parameter Store](/docs/esc/providers/secrets/aws-parameter-store/) — pull configuration and secrets from Parameter Store into ESC environments.
- [AWS IAM credential rotation](/docs/esc/providers/rotators/aws-iam/) — rotate IAM access keys on a schedule.
- [AWS Lambda rotator](/docs/esc/operations/rotation/aws-lambda/) — rotate arbitrary secrets via an AWS Lambda function.

## Insights

[Pulumi Insights](/docs/insights/) continuously scans your clouds to build a searchable inventory of every resource — whether created by Pulumi or not — so you can find, audit, and govern cloud infrastructure across accounts, regions, and providers.

For AWS, Insights connects AWS accounts (including AWS Partitions) to inventory existing resources, search across accounts, and export data. See [Add an AWS account](/docs/insights/discovery/get-started/create-accounts/) for a step-by-step setup guide and [Insights discovery overview](/docs/insights/discovery/accounts/) for background.

## Policy packs

[Pulumi Policies](/docs/insights/policy/) lets you enforce rules on infrastructure at preview and update time, rejecting stacks that violate security, cost, or compliance standards. [Pre-built policy packs](/docs/insights/policy/policy-packs/pre-built-packs/) are maintained by Pulumi and cover common regulatory and best-practice frameworks.

For AWS:

- [Pulumi best practices for AWS](/docs/reference/pre-built-policy-packs/pulumi-best-practices/aws/) — Pulumi-authored policies for common AWS misconfigurations.
- [CIS AWS Foundations Benchmark](/docs/reference/pre-built-policy-packs/cis/aws/)
- [NIST 800-53 for AWS](/docs/reference/pre-built-policy-packs/nist/aws/)
- [PCI DSS for AWS](/docs/reference/pre-built-policy-packs/pci-dss/aws/)
- [HITRUST CSF for AWS](/docs/reference/pre-built-policy-packs/hitrust/aws/)
- [CIS Kubernetes Benchmark on AWS](/docs/reference/pre-built-policy-packs/cis-kubernetes/aws/) — for EKS clusters.
- [AWS Organizations Tag Policies](/docs/reference/pre-built-policy-packs/aws-organizations-tag-policies/aws/) — enforce Organizations tagging standards on Pulumi-managed resources.
- [AWS Organizations Tag Policies in Insights](/docs/insights/policy/integrations/aws-organizations-tag-policies/) — integration with Pulumi Insights.

## Migration

Migrate existing AWS infrastructure from another IaC tool to Pulumi. The guides below walk through converting or coexisting with each source format.

- [From CloudFormation](/docs/iac/guides/migration/migrating-to-pulumi/from-cloudformation/) — convert CloudFormation templates to Pulumi.
- [From AWS CDK](/docs/iac/guides/migration/migrating-to-pulumi/from-cdk/) — move from AWS CDK to Pulumi, or use CDK constructs inside Pulumi programs.
- [From Terraform](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/) — convert Terraform HCL and state to Pulumi.

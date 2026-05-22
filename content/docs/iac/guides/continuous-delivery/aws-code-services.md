---
title_tag: "Using AWS Code Services with Pulumi | CI/CD"
meta_desc: Run Pulumi in AWS CodeBuild and CodePipeline to preview and deploy infrastructure changes through a trunk-based continuous delivery workflow.
title: AWS Code Services
h1: Using AWS Code Services with Pulumi
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: AWS Code Services
        parent: iac-using-pulumi-cicd
        weight: 20
aliases:
- /docs/iac/using-pulumi/continuous-delivery/aws-code-services/
- /docs/reference/cd-aws-code-services/
- /docs/console/continuous-delivery/aws-code-services/
- /docs/guides/continuous-delivery/aws-code-services/
- /docs/guides/continuous-delivery/cd-aws-code-services/
- /docs/using-pulumi/continuous-delivery/cd-aws-code-services/
- /docs/using-pulumi/continuous-delivery/aws-code-services/
- /docs/iac/packages-and-automation/continuous-delivery/aws-code-services/
---

AWS Code Services are a suite of [developer tools](https://aws.amazon.com/products/developer-tools/) for building and shipping software on AWS. The services most relevant to running Pulumi are [CodeBuild](https://aws.amazon.com/codebuild/), a managed build environment, and [CodePipeline](https://aws.amazon.com/codepipeline/), which models a release process as an ordered set of stages. [CodeDeploy](https://aws.amazon.com/codedeploy/) automates application rollouts onto the infrastructure Pulumi provisions.

Pulumi runs in **CodeBuild**: it executes your Pulumi program to compute the desired state of your cloud resources, and CodeBuild supplies the compute environment to do that. **CodePipeline** then invokes CodeBuild as one stage of a larger pipeline, so a Pulumi update can run wherever it fits in your existing release process.

{{% notes type="info" %}}
This guide assumes you use [Pulumi Cloud](https://app.pulumi.com/signin) as your [state backend](/docs/iac/concepts/state-and-backends/). Pulumi also supports [self-managed backends](/docs/iac/concepts/state-and-backends/#using-a-diy-backend) in CI/CD, but the authentication steps in this guide are written for Pulumi Cloud.
{{% /notes %}}

## How Pulumi works with AWS Code Services

To apply infrastructure changes, Pulumi has to run your program with the Pulumi CLI. A CodeBuild project provides that environment: it checks out your source, installs the CLI and your program's dependencies, and runs `pulumi` commands.

A CodeBuild project can run on its own — triggered directly by a source-repository event — or as a stage inside CodePipeline. In a CodePipeline pipeline, a source stage pulls your repository and a build stage runs the CodeBuild project that invokes Pulumi. You add the build stage wherever an infrastructure update belongs relative to the rest of your pipeline.

## Prerequisites

Before you begin, make sure you have:

- A [Pulumi Cloud](https://app.pulumi.com/signin) account and organization.
- An AWS account with permission to create CodeBuild projects and IAM roles.
- A [Pulumi program](/docs/iac/concepts/projects/) in a Git repository.
- Familiarity with [CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) and, if you use it, [CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html).

## Authenticate with Pulumi Cloud

CodeBuild authenticates to Pulumi Cloud with a single [Pulumi access token](/docs/administration/access-identity/access-tokens/), supplied through the `PULUMI_ACCESS_TOKEN` environment variable. Prefer an [organization or team token](/docs/administration/access-identity/access-tokens/#creating-an-organization-access-token) over a personal token so the pipeline's identity is not tied to an individual.

Because the token is a sensitive credential, store it in [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html) (as a `SecureString`) or [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html), and reference it from the CodeBuild project rather than hardcoding it. CodeBuild resolves the value at build time and never persists it in the build definition.

{{% notes type="warning" %}}
Do not store the access token in plaintext environment variables or commit it to your repository. Keep it in Parameter Store or Secrets Manager so access is auditable and the value stays encrypted at rest.
{{% /notes %}}

## Provide AWS credentials

When Pulumi runs, your program also needs AWS credentials to read and modify cloud resources. You can supply them in one of two ways.

### CodeBuild service role

Every CodeBuild project runs as an IAM [service role](https://docs.aws.amazon.com/codebuild/latest/userguide/setting-up.html#setting-up-service-role). When `pulumi up` runs on the build host, the AWS provider uses that role's credentials by default. Attach IAM policies to the service role that grant the permissions your Pulumi program needs to manage its resources.

This is the simplest option, but the service role accumulates every permission any pipeline program requires, and those permissions differ from what developers use on their own machines.

{{% notes type="info" %}}
The service role only authenticates to AWS. If your Pulumi program uses other providers — another cloud, a SaaS provider, or a Kubernetes cluster — the service role does not supply those credentials, and you must provide them another way, such as through [Pulumi ESC](#pulumi-esc-recommended).
{{% /notes %}}

### Pulumi ESC (recommended)

[Pulumi ESC](/docs/esc/) (Environments, Secrets, and Configuration) delivers cloud credentials, secrets, and configuration to your Pulumi program from a central environment definition. Configure an ESC environment to broker short-lived AWS credentials through [OpenID Connect (OIDC)](/docs/esc/guides/configuring-oidc/aws/), and your program receives temporary credentials scoped to exactly what it needs.

Because ESC supplies those values the same way whether the consumer is a CodeBuild project or a developer's machine, a single environment definition works in both places — the pipeline only needs its Pulumi access token, and everything else flows from ESC.

## Configure the CodeBuild project

CodeBuild reads build instructions from a `buildspec.yml` file in your repository. The following minimal `buildspec.yml` installs the Pulumi CLI, installs your program's dependencies, and updates a [stack](/docs/iac/concepts/stacks/):

```yaml
version: 0.2

phases:
  install:
    commands:
      - curl -fsSL https://get.pulumi.com/ | sh
      - export PATH=$PATH:$HOME/.pulumi/bin
  pre_build:
    commands:
      - pulumi install
  build:
    commands:
      - pulumi stack select acme/website/production
      - pulumi up --yes
```

[`pulumi install`](/docs/iac/cli/commands/pulumi_install/) installs the program's language dependencies and required plugins, so the same `buildspec.yml` works for a Pulumi program written in any supported language.

Expose the Pulumi access token to the build by adding an environment variable to the CodeBuild project that pulls from Parameter Store:

```yaml
environment:
  environmentVariables:
    - name: PULUMI_ACCESS_TOKEN
      type: PARAMETER_STORE
      value: /pulumi/access-token
```

## Build a trunk-based CI/CD workflow

The most common way to run Pulumi in CI/CD follows a [trunk-based development model](/docs/iac/guides/continuous-delivery/#the-trunk-based-development-workflow): work merges into a single main branch, and deployments flow outward from there. CodePipeline's [source triggers](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-trigger-source-repository-events.html) distinguish pull request, branch, and tag events, so you can map each step of the workflow to its own pipeline or CodeBuild project.

### Preview infrastructure changes in a pull request

When a pull request is opened, run a dry run instead of a deployment. Trigger a CodeBuild project on pull request events and have it run [`pulumi preview`](/docs/iac/cli/commands/pulumi_preview/):

```yaml
  build:
    commands:
      - pulumi stack select acme/website/staging
      - pulumi preview
```

`pulumi preview` reports the proposed changes without modifying any resources, giving reviewers a summary of what the merge would do. To let reviewers exercise the change in a live environment, use a [Review Stack](/docs/deployments/deployments/review-stacks/), which provisions an ephemeral stack for the pull request and destroys it when the pull request closes.

### Deploy to staging on merge to the main branch

When a pull request merges, run [`pulumi up`](/docs/iac/cli/commands/pulumi_up/) against an environment that receives continuous delivery, such as a shared development or staging environment. Trigger a CodeBuild project on pushes to the main branch:

```yaml
  build:
    commands:
      - pulumi stack select acme/website/staging
      - pulumi up --yes
```

### Promote to production with a git tag

Production updates should be deliberate. Keep production on its own stack and deploy it only when you push a release tag — for example, a moving `production` tag that you advance to a commit already validated in staging:

```yaml
  build:
    commands:
      - pulumi stack select acme/website/production
      - pulumi up --yes
```

Configure this CodeBuild project (or CodePipeline source stage) to trigger on git tag events rather than branch pushes. Promotion then becomes a single, traceable Git operation, and production never deploys from an untested commit.

## Manage the pipeline with Pulumi

The CodeBuild projects, CodePipeline pipelines, IAM roles, and Parameter Store entries described above are themselves AWS resources, so you can define them with Pulumi using the [AWS provider](/registry/packages/aws/). Managing the pipeline as code keeps it versioned, reviewable, and reproducible alongside the infrastructure it deploys.

See the AWS provider's [CodeBuild](/registry/packages/aws/api-docs/codebuild/), [CodePipeline](/registry/packages/aws/api-docs/codepipeline/), and [CodeDeploy](/registry/packages/aws/api-docs/codedeploy/) modules in the Pulumi Registry for the available resources and their inputs.

If you operate many pipelines that are similar or identical, package the pattern once instead of copying it. Wrap these resources in a [component](/docs/iac/concepts/components/) so each pipeline becomes a single resource with a small set of inputs, or publish a [template](/docs/iac/guides/building-extending/creating-templates/) so teams can scaffold a new pipeline with `pulumi new`.

## Additional resources

- [Continuous delivery](/docs/iac/guides/continuous-delivery/) — overview of running Pulumi in CI/CD.
- [Pulumi ESC](/docs/esc/) — deliver credentials, secrets, and configuration to pipelines and developers consistently.
- [OIDC issuers](/docs/administration/access-identity/oidc-issuers/) — exchange a CI/CD system's OIDC token for a short-lived Pulumi access token.
- [AWS provider](/registry/packages/aws/) — manage AWS resources, including the pipeline itself, as code.
- [Component resources](/docs/iac/concepts/components/) — package a reusable pipeline pattern as a single resource.
- [Review Stacks](/docs/deployments/deployments/review-stacks/) — ephemeral environments created automatically for each pull request.
- [CI/CD troubleshooting](/docs/iac/guides/continuous-delivery/troubleshooting/) — diagnose common failures when running Pulumi in a pipeline.

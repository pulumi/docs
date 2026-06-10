---
title_tag: "Using Azure DevOps with Pulumi | CI/CD"
meta_desc: Run Pulumi in Azure Pipelines with the Pulumi Task Extension, authenticate with Pulumi Cloud, and ship infrastructure through a trunk-based CI/CD workflow.
title: Azure DevOps
h1: Using Azure DevOps with Pulumi
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  iac:
    name: Azure DevOps
    parent: iac-operations-cicd
    weight: 30
aliases:
    - /docs/iac/guides/continuous-delivery/azure-devops/
    - /docs/integrations/azure-devops/
    - /docs/iac/integrations/azure-devops/
    - /docs/iac/using-pulumi/continuous-delivery/azure-devops/
    - /docs/reference/cd-azure-devops/
    - /docs/console/continuous-delivery/azure-devops/
    - /docs/guides/continuous-delivery/azure-devops/
    - /docs/guides/continuous-delivery/cd-azure-devops/
    - /docs/using-pulumi/continuous-delivery/cd-azure-devops/
    - /docs/using-pulumi/continuous-delivery/azure-devops/
    - /docs/iac/packages-and-automation/continuous-delivery/azure-devops/
---

[Azure DevOps](https://azure.microsoft.com/products/devops) provides source control through Azure Repos and CI/CD through Azure Pipelines. You run Pulumi in Azure Pipelines with the [Pulumi Task Extension](https://marketplace.visualstudio.com/items?itemName=pulumi.build-and-release-task), a Pulumi-maintained extension on the Visual Studio Marketplace. It installs the Pulumi CLI and runs Pulumi commands in your pipeline without custom scripts.

The task runs CLI commands, so it works with a Pulumi program written in any [supported language](/docs/iac/languages-sdks/). It also works with [any cloud provider](/registry/) Pulumi supports, not only Azure.

{{% notes type="info" %}}
This guide assumes you use [Pulumi Cloud](https://app.pulumi.com/signin) as your [state backend](/docs/iac/concepts/state-and-backends/). Pulumi also supports [self-managed backends](/docs/iac/concepts/state-and-backends/#using-a-diy-backend) in CI/CD, but the authentication steps in this guide are written for Pulumi Cloud.
{{% /notes %}}

{{< pulumi-docker-images-note >}}

## Prerequisites

Before you begin, make sure you have:

1. A [Pulumi Cloud](https://app.pulumi.com/signin) account and organization.
1. An Azure DevOps organization and project containing a Git repository.
1. A Pulumi program. If you don't have one yet, follow a [Get started](/docs/iac/get-started/) guide.

## Install the Pulumi Task Extension

Install the [Pulumi Task Extension](https://marketplace.visualstudio.com/items?itemName=pulumi.build-and-release-task) from the Visual Studio Marketplace to your Azure DevOps organization. After installation, the `Pulumi@1` task is available in every pipeline across the organization.

## Authenticate with Pulumi Cloud

Your pipeline needs a single [Pulumi access token](/docs/administration/access-identity/access-tokens/) to authenticate with Pulumi Cloud.

The task looks for the pipeline variable `pulumi.access.token` and maps it automatically to the `PULUMI_ACCESS_TOKEN` environment variable. Store the token as a [secret pipeline variable](https://learn.microsoft.com/azure/devops/pipelines/process/set-secret-variables) or in a linked [variable group](https://learn.microsoft.com/azure/devops/pipelines/library/variable-groups) so it isn't checked into source control. Prefer an organization or team token over a personal token.

[Pulumi ESC](/docs/esc/) (Environments, Secrets, and Configuration) then supplies cloud credentials, secrets, and configuration to your Pulumi program. Because ESC delivers those values the same way whether the consumer is a pipeline or a developer's machine, a single environment definition works in both places — you don't store separate cloud provider keys in the pipeline.

## The trunk-based development workflow

The most common way to run Pulumi in Azure Pipelines follows a trunk-based development model, where work merges into a single main branch and deployments flow outward from there:

1. **Open a pull request.** The pipeline runs `pulumi preview` and posts the proposed changes for review.
1. **Merge to the main branch.** The pipeline runs `pulumi up` to deploy the change to an environment that receives continuous delivery, such as a shared development or staging environment.
1. **Promote to production.** Pushing a git tag triggers a deployment to production, keeping production updates deliberate and traceable.

The pipeline below implements all three stages. It assumes a Pulumi program in an `infra/` directory and stacks named `acme/website/staging` and `acme/website/production`.

```yaml
# azure-pipelines.yml
trigger:
  branches:
    include:
      - main
  tags:
    include:
      - release-*

pr:
  branches:
    include:
      - main

pool:
  vmImage: ubuntu-latest

steps:
  # Pull request: preview the proposed changes.
  - task: Pulumi@1
    displayName: Preview changes
    condition: eq(variables['Build.Reason'], 'PullRequest')
    inputs:
      command: preview
      stack: acme/website/staging
      cwd: infra/
      createPrComment: true

  # Merge to main: deploy to the staging environment.
  - task: Pulumi@1
    displayName: Deploy to staging
    condition: and(eq(variables['Build.SourceBranch'], 'refs/heads/main'), ne(variables['Build.Reason'], 'PullRequest'))
    inputs:
      command: up
      args: --yes
      stack: acme/website/staging
      cwd: infra/

  # Tag push: promote to production.
  - task: Pulumi@1
    displayName: Deploy to production
    condition: startsWith(variables['Build.SourceBranch'], 'refs/tags/release-')
    inputs:
      command: up
      args: --yes
      stack: acme/website/production
      cwd: infra/
```

To promote a release, push a tag that matches the `release-*` pattern:

```bash
git tag release-2026-05-20
git push origin release-2026-05-20
```

For an optional ephemeral environment on each pull request, pair the preview step with a [Review Stack](/docs/deployments/deployments/review-stacks/), which provisions and tears down a per-PR environment automatically.

## PR comments

The task can post pipeline output as a comment on the pull request that triggered the build. To enable this feature:

1. Set `createPrComment: true` in the task inputs.
1. Grant the build service user the **Contribute to pull requests** permission:
   - Navigate to **Project Settings** > **Repositories** > select your repo > **Security** tab.
   - Under **Users**, find the build service user (named `<Project name> Build Service`).
   - Set **Contribute to pull requests** to **Allow**.

{{% notes type="info" %}}
PR comments are only supported for repositories hosted in Azure DevOps. GitHub, GitLab, and Bitbucket repositories are not supported.
{{% /notes %}}

## Task reference

The `Pulumi@1` task accepts the following inputs:

| Parameter | Required | Description |
|-----------|----------|-------------|
| `stack` | Yes | Stack name in the form `ORG/STACK` or `ORG/PROJECT/STACK`. |
| `command` | No | Pulumi CLI command to run (e.g., `preview`, `up`, `destroy`). |
| `args` | No | Option flags passed to the command (e.g., `--yes`). Separate multiple args with spaces. |
| `cwd` | No | Working directory for the Pulumi commands. Use if your Pulumi program is in a subdirectory. |
| `azureSubscription` | No | Reference a service connection for Azure credentials. If omitted, configure cloud credentials as environment variables. |
| `versionSpec` | No | Pulumi CLI version to use. Defaults to the latest version. |
| `createStack` | No | Set to `true` to create the stack if it doesn't exist. Defaults to `false`. |
| `createPrComment` | No | Set to `true` to post pipeline output as a pull request comment. Only supported for PRs in Azure DevOps-hosted repositories. Defaults to `false`. |
| `useThreadedPrComments` | No | Set to `true` to append to an existing comment thread. Defaults to `true`. |

Use the `env` directive on the task to pass additional environment variables to your Pulumi program.

## Using with other cloud providers

To use the task with AWS, Google Cloud, or another provider, pass the required credentials as pipeline variables or link variable groups to your pipeline. For example, for AWS:

```yaml
- task: Pulumi@1
  inputs:
    command: up
    stack: acme/website/production
    args: --yes
  env:
    AWS_ACCESS_KEY_ID: $(awsAccessKeyId)
    AWS_SECRET_ACCESS_KEY: $(awsSecretAccessKey)
```

Using [Pulumi ESC](/docs/esc/) to broker short-lived cloud credentials avoids storing provider keys as pipeline variables at all.

## Managing Azure DevOps with Pulumi

You can also manage Azure DevOps itself — projects, repositories, pipelines, and service connections — as code with the [Azure DevOps provider](/registry/packages/azuredevops/) in the Pulumi Registry.

## Additional resources

- [Continuous delivery](/docs/iac/operations/continuous-delivery/) — overview of running Pulumi in CI/CD.
- [Azure DevOps version control integration](/docs/integrations/version-control/azure-devops-integration/) — connect Azure DevOps repositories to Pulumi Cloud Deployments to deploy on push and preview pull requests without managing your own pipeline.
- [Pulumi ESC](/docs/esc/) — deliver credentials, secrets, and configuration to pipelines and developers consistently.

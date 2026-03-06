---
title_tag: "Azure DevOps Task Extension | Integrations"
meta_desc: The Pulumi Task Extension for Azure Pipelines installs the Pulumi CLI and runs commands in your pipeline without scripts.
title: Azure DevOps Task Extension
h1: Azure DevOps Task Extension
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  iac:
    name: Azure DevOps
    parent: iac-using-pulumi-cicd
    weight: 1
aliases:
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

The [Pulumi Task Extension for Azure Pipelines](https://marketplace.visualstudio.com/items?itemName=pulumi.build-and-release-task) is a Pulumi-maintained extension available on the Visual Studio Marketplace. It installs the Pulumi CLI and runs Pulumi commands in your Azure Pipelines without requiring custom scripts.

> The Pulumi Task Extension can be used with [any cloud provider](/registry/) that Pulumi supports — not just Azure.

## Installing the task extension

Install the task from the [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=pulumi.build-and-release-task) to your Azure DevOps organization. After installation, the `Pulumi@1` task is available in all pipelines across your organization.

## Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `stack` | Yes | Stack name in the form `ORG/STACK` or `ORG/PROJECT/STACK`. |
| `command` | No | Pulumi CLI command to run (e.g., `preview`, `up`, `destroy`). |
| `args` | No | Option flags passed to the command (e.g., `--yes`). Separate multiple args with spaces. |
| `cwd` | No | Working directory for the Pulumi commands. Use if your Pulumi app is in a subdirectory. |
| `azureSubscription` | No | Reference a service connection for Azure credentials. If omitted, configure cloud credentials as environment variables. |
| `versionSpec` | No | Pulumi CLI version to use. Defaults to the latest version. |
| `createStack` | No | Set to `true` to create the stack if it doesn't exist. Defaults to `false`. |
| `createPrComment` | No | Set to `true` to post pipeline output as a pull request comment. Only supported for PRs in Azure DevOps-hosted repositories. Defaults to `false`. |
| `useThreadedPrComments` | No | Set to `true` to append to an existing comment thread. Defaults to `true`. |

The task looks for the build variable `pulumi.access.token` and maps it automatically to `PULUMI_ACCESS_TOKEN`. You can also use the `env` directive to pass additional environment variables to your Pulumi program.

## Basic usage

```yaml
- task: Pulumi@1
  condition: or(eq(variables['Build.Reason'], 'PullRequest'), eq(variables['Build.Reason'], 'Manual'))
  inputs:
    azureSubscription: "My Service Connection"
    command: "preview"
    cwd: "infra/"
    stack: "acmeCorp/acmeProject/acme-ui"
```

## PR comments

The task can post pipeline output as a comment on the pull request that triggered the build. To enable this feature:

1. Set `createPrComment: true` in the task inputs.
1. Grant the build service user the **Contribute to pull requests** permission:
   - Go to **Project Settings** > **Repositories** > select your repo > **Security** tab.
   - Under **Users**, find the build service user (named `<Project name> Build Service`).
   - Set **Contribute to pull requests** to **Allow**.

> PR comments are only supported for repositories hosted in Azure DevOps. GitHub, GitLab, and Bitbucket repositories are not supported.

## Using with other cloud providers

To use the task extension with AWS, Google Cloud, or other providers, pass the required credentials as pipeline variables or link variable groups to your pipeline. For example, for AWS:

```yaml
- task: Pulumi@1
  inputs:
    command: "up"
    stack: "myOrg/myProject/prod"
    args: "--yes"
  env:
    AWS_ACCESS_KEY_ID: $(awsAccessKeyId)
    AWS_SECRET_ACCESS_KEY: $(awsSecretAccessKey)
```

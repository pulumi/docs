---
title_tag: "Deployment Settings | Pulumi Deployments"
meta_desc: Learn how to configure Deployment Settings for Pulumi Deployments
title: "Deployments Settings"
h1: "Pulumi Deployment Settings"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  cloud:
    parent: pulumi-cloud-deployments-using
    weight: 1
---

Deployment settings refer to the full set of configuration required to run a Pulumi Deployment, defined on a per-stack basis. These settings can be managed through the Pulumi Cloud UI, via the REST API, or defined as code with the Pulumi Cloud provider.

## Creating Deployment Settings

You can create and manage deployment settings in several ways:

### From the Pulumi Cloud UI

From the Pulumi Console, a stack's deployment settings can be accessed via the `Settings > Deploy` tab. Once the settings are defined via the UI, they apply to all Deployment triggers, including push-to-deploy (if you have the GitHub app installed), click-to-deploy and the REST API.

![Pulumi UI - Deployment Settings](../../ui-settings.png)

### From the API

Alternatively, a stack's deployment settings may be defined and subsequently modified using the REST API. For more information, see [Patch Settings](/docs/pulumi-cloud/reference/deployments/#patch-settings) in the [Pulumi Deployments REST API docs](/docs/pulumi-cloud/reference/deployments).

### Defined as Code with the Pulumi Cloud provider

Finally, a stack's deployment settings may be defined as a resource within the stack itself using the Pulumi Cloud provider. This lets you securely store your settings in source control alongside your code. For more information, see the [`pulumiservice.DeploymentSettings`](https://www.pulumi.com/registry/packages/pulumiservice/api-docs/deploymentsettings/) resource docs in the [Pulumi Registry](/registry).

{{% notes type="info" %}}
Pulumi recommends against a stack defining its own Deployment Settings (that is, including a `pulumiService.DeploymentSettings` resource that defines settings for the current stack), as this would require two deployments for the settings changes to take effect. Instead, create a separate Pulumi program that defines Deployment Settings for multiple stacks that share similar configuration.
{{% /notes %}}

## Path Filtering

When using the GitHub app and push-to-deploy, you may want to filter deployment events to only target file changes in specific directories. You can easily do this using path filtering, so a deployment is only triggered if there is a change in files that match the path filters. This is especially useful for monorepos where you may have multiple Pulumi programs within the same repository.

Path filters are relative to the repository root, and should reference a file by name or a directory must reference files by name relative to the repository or directories via glob patterns such as `/**` to include all changes within a directory.

![Pulumi UI - Path Filters](../../ui-path-filters.png)

As with any other deployment setting, the path filters may be set via the Pulumi Console, using the REST API or defined in code using the Pulumi Cloud provider.

## Deployment Runner Pools

When using Pulumi Deployments, you have options for where your deployments run:

- **Default Runner Pool**: Managed by Pulumi and available to all Pulumi Cloud customers
- **Customer-Managed Agents**: Self-hosted runners that can access private networks and resources

For more information on customer-managed agents, see the [Customer Managed Agents documentation](../../customer-managed-agents).

## Pre-Run Commands

Pre-run commands allow you to execute arbitrary shell commands before the deployment process starts. This is useful for environment setup, authentication with private package repositories, or other preparatory work. Note that each line of your pre-run command runs in a separate shell.

For example, you might use pre-run commands to:

- Install additional dependencies
- Configure authentication for private repositories
- Generate configuration files
- Set up environment variables - see [here](#pulumi_env) if you need to persist these to your Pulumi program.

Pre-run commands can be configured through the UI, REST API, or as code with the Pulumi Cloud provider.

{{% notes type="info" %}}
You can use Pulumi ESC with pre-run commands by prefixing each command with `pulumi env run`. For example:

```bash
pulumi env run my-aws-env -- aws s3 ls
```

This executes the `aws s3 ls` command with credentials from your `my-aws-env` ESC environment. See the [Pulumi ESC CLI documentation](/docs/esc/usage/cli-commands/#env) for more details.
{{% /notes %}}

## Skipping Automatic Dependency Installation

By default, the deployment executor will attempt to install dependencies for your project by using the default dependency manager for the language (i.e. `npm` for nodejs or `virtualenv` for python). However, there may be scenarios where you may want to have more control over the dependency installation step (e.g. you are using `yarn` and/or a different version of `node` than the one that is installed by default).

This is enabled by skipping the default dependency installation step (under Advanced Settings in the UI), and setting a few pre-run commands and environment variables.

![Pulumi UI - Node Version](../../ui-node-version.png)

## Skipping Intermediate Deployments

By default, when multiple deployments are pushed, they will be executed sequentially until the backlog is completed. In some cases, you may wish to only execute the most recent deployment since the changes are accumulative. By enabling the `Skip intermediate deployments` setting, Pulumi will skip all intermediary deployments of the same type and will execute only the latest.

![Pulumi UI - Skip intermediate deployments](../../ui-skip-intermediate-deployments.png)

## Custom Executor Images

By default, the deployment is executed using the [pulumi/pulumi](https://hub.docker.com/r/pulumi/pulumi) image.
The pulumi/pulumi image is a unix-based image which includes the pulumi CLI in its `$PATH` and the [LTS versions](https://github.com/pulumi/pulumi-docker-containers/blob/main/README.md#version-policy) of all supported SDK runtime(s) for your Pulumi program.

However, there may be scenarios where you might want to customize the image used for the execution, e.g. if you want to use a different version of python or need to include additional dependencies.

This is possible by specifying a custom executor image for your deployment. Using the custom executor image field, you can pin to a specific version of the pulumi/pulumi image,
or point to a completely custom image hosted in a public or private container registry.

![Pulumi UI - Custom Executor](../../ui-custom-executor.png)

Image requirements:

- It must be a unix-based image which includes `curl`.
- It must include the `pulumi` CLI in its `$PATH`.
- It must include the required SDK runtime(s) for your Pulumi program.

{{% notes "info" %}}
Using a custom image may result in slower execution due to time spent pulling the image.

Additionally, we only support static credentials in custom executor images.
{{% /notes %}}

## Open ID Connect (OIDC)

Pulumi Deployments supports OIDC for authenticating with cloud providers. This enables your deployments to access your cloud resources without storing static credentials in Pulumi Cloud.

{{% notes type="info" %}}
There are multiple approaches for supplying cloud credentials to Pulumi Deployments. For guidance on choosing between Deployments OIDC and Pulumi ESC, see [Supplying Cloud Credentials to Pulumi Deployments](/docs/pulumi-cloud/deployments/cloud-credentials/).
{{% /notes %}}

For details on supported clouds see [OIDC Setup for Pulumi Deployments](/docs/pulumi-cloud/deployments/oidc/).

## Dependency Caching

When using Pulumi-managed deployment agents, you have the option to speed up deployments using dependency caching.

{{% notes type="info" %}}
If you have configured the stack to use a [Customer-managed agent](/docs/pulumi-cloud/deployments/customer-managed-agents/) runner pool this option is unavailable. Running a customer-managed agent pool gives you full control over the lifetime of the agent and its caching.
{{% /notes %}}

The caching method is simple: during the first deployment, the deployment agent will automatically detect downloaded dependencies using lock files, zip them up and store the archive in blob storage. During all subsequent deployments, agents will pull such an archive down and unpack it, saving time it would normally take to download those dependencies. When your dependencies change, deployment agents will automatically invalidate the old cache and create a new one.

Caches are shared on the project level, so all stacks within a project can share the same cache. However, caches are fully isolated and never shared between customers.

Dependency caching is supported for the following runtimes:

- `.NET` - no special configuration required
- `Python` - ensure that you have `requirements.txt` in the root of your source code.
- `Go` - ensure that you have `go.mod` and `go.sum` in the root of your source code.
- `NodeJS` - ensure that you have `packageManager` field specified in `package.json`. For now, only `npm` and `yarn` are supported.
  - For `npm`, ensure that you have `package-lock.json` in the root of your source code.
  - For `yarn`, ensure that you have `yarn.lock` in the root of your source code.

To confirm dependency caching is working and/or to troubleshoot, check out logs of your deployments, specifically the `Restore Cache` and `Save Cache` steps.

## Environment Variables

By default, there are a set of environment variables set by the process automatically:

- `GITHUB_TOKEN`: Personal Access Token configured when the source is GitHub (unless there is a token configured by the custom environment variables)
- `PULUMI_ACCESS_TOKEN`: A temporary token with read-write access only to the stack being deployed.
- `PULUMI_DEPLOY_OIDC_CONFIG`: OIDC configuration provided for the cloud integrations
- `PULUMI_CI_SYSTEM`: "Pulumi Deployments"
- `PULUMI_CI_BUILD_ID`: Current deployment ID
- `PULUMI_CI_BUILD_NUMBER`: Current deployment version
- `PULUMI_CI_BUILD_URL`: Current deployment URL
- `PULUMI_CI_ORGANIZATION`: Current account organization
- `PULUMI_CI_PROJECT`: Current project name
- `PULUMI_CI_STACK`: Current stack name

These can be overridden or extended by configuring custom environment variables:

![Pulumi UI - Environment Variables](../../ui-custom-env-variables.png)

### PULUMI_ENV

Environment variables can be persisted between pre-run commands and the final pulumi deployment by appending them to the file on the file system named `PULUMI_ENV`.

Example Usage:

```bash
export GOOGLE_OAUTH_ACCESS_TOKEN=$(gcloud auth print-access-token)
echo GOOGLE_OAUTH_ACCESS_TOKEN=$GOOGLE_OAUTH_ACCESS_TOKEN >> /PULUMI_ENV
```

Running `env` in a subsequent pre-run command will show the environment variable and it should be usable by scripts or your pulumi program.
{{% notes type="info" %}}
If `/PULUMI_ENV` does not work, and you are on self hosted, you can look for the following message in the logs to get the location: `Loading PULUMI_ENV from`.
{{% /notes %}}

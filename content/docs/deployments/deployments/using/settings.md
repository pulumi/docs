---
title_tag: "Deployment Settings | Pulumi Deployments"
meta_desc: Learn how to configure Deployment Settings for Pulumi Deployments
title: "Deployments Settings"
h1: "Pulumi Deployment Settings"
meta_image: /images/docs/meta-images/docs-meta.png
aliases:
- /docs/pulumi-cloud/deployments/using/settings/
menu:
  deployments:
    parent: deployments-deployments-using
    weight: 1
---

Deployment settings refer to the full set of configuration required to run a Pulumi Deployment, defined on a per-stack basis. These settings can be managed through the Pulumi Cloud UI, via the REST API, or defined as code with the Pulumi Cloud provider.

## Creating Deployment Settings

You can create and manage deployment settings in several ways:

### From the Pulumi Cloud UI

From the Pulumi Cloud console, a stack's deployment settings can be accessed via the `Settings > Deploy` tab. Once the settings are defined via the UI, they apply to all Deployment triggers, including push-to-deploy (if you have a [VCS integration](/docs/integrations/version-control/) configured), click-to-deploy and the REST API.

![Pulumi UI - Deployment Settings](/docs/deployments/deployments/ui-settings.png)

### From the API

Alternatively, a stack's deployment settings may be defined and subsequently modified using the REST API. For more information, see [Patch Settings](/docs/reference/cloud-rest-api/deployments/#patch-settings) in the [Pulumi Deployments REST API docs](/docs/reference/cloud-rest-api/deployments).

### Defined as Code with the Pulumi Cloud provider

Finally, a stack's deployment settings may be defined as a resource within the stack itself using the Pulumi Cloud provider. This lets you securely store your settings in source control alongside your code. For more information, see the [`pulumiservice.DeploymentSettings`](https://www.pulumi.com/registry/packages/pulumiservice/api-docs/deploymentsettings/) resource docs in the [Pulumi Registry](/registry).

{{% notes type="info" %}}
Pulumi recommends against a stack defining its own Deployment Settings (that is, including a `pulumiService.DeploymentSettings` resource that defines settings for the current stack), as this would require two deployments for the settings changes to take effect. Instead, create a separate Pulumi program that defines Deployment Settings for multiple stacks that share similar configuration.
{{% /notes %}}

## Path Filtering

When using a [VCS integration](/docs/integrations/version-control/) and push-to-deploy, you may want a deployment to trigger only when a push changes files you care about. You can do this with path filters. This is especially useful for monorepos, where a single repository holds multiple Pulumi programs and you want each stack to deploy only when its own files change.

![Pulumi UI - Path Filters](/docs/deployments/deployments/ui-path-filters.png)

### Writing filters

Each filter is a glob pattern matched against the full path of every file changed by a push, relative to the repository root. A pattern must match the *entire* path:

- `infrastructure/Pulumi.dev.yaml` matches only that one file.
- `infrastructure/**` matches every file anywhere under the `infrastructure/` directory.

A filter is an **include filter** by default. Prefix it with `!` to make it an **exclude filter**:

- `infrastructure/**` — include changes under `infrastructure/`.
- `!infrastructure/docs/**` — exclude changes under `infrastructure/docs/`.

### How filters are evaluated

A push triggers a deployment when **at least one changed file matches the filters**. An individual file matches when both of these are true:

1. It matches at least one include filter (or no include filters are configured), and
1. It does not match any exclude filter.

A few consequences worth knowing:

- **No filters:** every push triggers a deployment.
- **Only exclude filters:** every file is included unless an exclude filter matches it.
- **Exclude always wins.** If a file matches an exclude filter, it is excluded even when it also matches an include filter. The order in which you list filters does not matter.

{{% notes type="warning" %}}
Path filters do **not** behave like a `.gitignore` file. In `.gitignore`, a later negated pattern can re-include a path that an earlier pattern excluded. Pulumi path filters have no equivalent: once a file matches an exclude filter, no include filter can bring it back.

For example, given these filters:

```
!foo/**
foo/bar/**
```

a change to `foo/bar/main.ts` does **not** trigger a deployment — it matches the `!foo/**` exclude filter, and the `foo/bar/**` include filter cannot override that. To deploy on changes under `foo/bar/` while ignoring the rest of `foo/`, exclude only the specific subdirectories you want to skip (for example `!foo/baz/**`) rather than excluding all of `foo/`.
{{% /notes %}}

### Setting path filters

As with any other deployment setting, path filters may be set via the Pulumi Cloud console, using the REST API, or defined in code using the Pulumi Cloud provider.

## Tag Filtering

When using a [VCS integration](/docs/integrations/version-control/) and push-to-deploy, you can trigger a deployment when a git tag is pushed instead of (or in addition to) a branch push. This is useful for release-based workflows where you deploy only when you cut a release — for example, pushing a `v1.2.0` tag — rather than on every commit. See [Deploying on git tags](/docs/deployments/deployments/using/triggers/#deploying-on-git-tags) for an overview.

Tag triggers are controlled by two deployment settings on your VCS configuration:

- **`deployTags`** — a boolean that enables deploying when a matching tag is pushed.
- **`tagFilters`** — a list of glob patterns that determine which tag names qualify. This is analogous to [path filters](#path-filtering), except the patterns are matched against the **tag name** rather than changed file paths.

### Writing filters

Each filter is a glob pattern matched against the full tag name. A pattern must match the *entire* tag name:

- `v1.0.0` matches only that exact tag.
- `v*` matches every tag beginning with `v`, such as `v1.0.0` and `v2.3.1`.

A filter is an **include filter** by default. Prefix it with `!` to make it an **exclude filter**:

- `v*` — include tags beginning with `v`.
- `!*-rc*` — exclude release candidates such as `v1.2.0-rc1`.

### How filters are evaluated

The same model as path filters applies, evaluated against the pushed tag name:

- **`deployTags` disabled:** tag pushes never trigger a deployment, regardless of filters.
- **No filters (`deployTags` enabled):** every tag push triggers a deployment.
- **Only exclude filters:** every tag triggers a deployment unless an exclude filter matches it.
- **Exclude always wins.** If a tag matches an exclude filter, it is excluded even when it also matches an include filter. The order in which you list filters does not matter.

{{% notes type="warning" %}}
Like path filters, tag filters do **not** behave like a `.gitignore` file: once a tag matches an exclude filter, no include filter can bring it back. To deploy on a subset of tags while ignoring others, prefer narrow include patterns over broad excludes.
{{% /notes %}}

Deleting a tag never triggers a deployment.

### Setting tag filters

As with any other deployment setting, `deployTags` and `tagFilters` may be set via the Pulumi Cloud console, using the REST API, or defined in code using the Pulumi Cloud provider. In the console, enable the **Run updates for pushed tags** toggle and enter your patterns in the **Tag filters** field as a comma-separated list. The REST API and the Pulumi Cloud provider take `tagFilters` as an array of patterns.

{{% notes type="info" %}}
GitLab integrations created before this feature did not subscribe to tag push events. To use tag triggers with one, enable **Tag push events** on the existing GitLab group webhook — there's no need to re-create the integration. See the [GitLab integration docs](/docs/integrations/version-control/gitlab/#push-to-deploy) for details. This caveat applies only to GitLab; other providers require no action.
{{% /notes %}}

## Deployment Runner Pools

When using Pulumi Deployments, you have options for where your workflows run:

- **Pulumi Hosted Pool**: Managed by Pulumi and available to all Pulumi Cloud customers
- **Customer-Managed Workflow Runners**: Self-hosted runners that can access private networks and resources, supporting deployments, [Insights](/docs/insights/) discovery scans, and [policy evaluations](/docs/insights/policy/)

If a stack does not have a pool explicitly configured, the deployment uses the organization's [default workflow runner pool](/docs/deployments/deployments/runs/customer-managed-agents/#setting-an-organization-default-pool) if one is set, and otherwise falls back to the Pulumi Hosted Pool.

For more information on customer-managed workflow runners, see the [Customer-Managed Workflow Runners documentation](/docs/deployments/deployments/runs/customer-managed-agents/).

### Role assignment

When configuring deployment settings, you can assign organization roles to the stack token used for deployments. This setting appears as a dropdown menu under "Role assignment" that displays available organization roles.

If no role is selected, the deployment will only have access to the specific stack being deployed. However, this limited access can cause failures when the deployment needs to:

- Access stack references from other stacks
- Access environments
- Manage organization resources such as teams, members, or OIDC issuers

By selecting an appropriate role, you provide the deployment with the necessary permissions to access these additional resources. For fine-grained access control, you can create custom roles with specific permissions tailored to what the deployment needs to accomplish.

Organization roles are managed through the Roles section. For more information on creating and managing roles, see the [Roles documentation](/docs/administration/access-identity/rbac/roles/).

## Pre-Run Commands

Pre-run commands allow you to execute arbitrary shell commands before the deployment process starts. This is useful for environment setup, authentication with private package repositories, or other preparatory work. Note that each line of your pre-run command runs in a separate shell.

For example, you might use pre-run commands to:

- Install additional dependencies
- Configure authentication for private repositories
- Generate configuration files
- Set up environment variables - see [PULUMI_ENV](#pulumi_env) if you need to persist these to your Pulumi program.

Pre-run commands can be configured through the UI, REST API, or as code with the Pulumi Cloud provider.

{{% notes type="info" %}}
You can use Pulumi ESC with pre-run commands by prefixing each command with `pulumi env run`. For example:

```bash
pulumi env run my-aws-env -- aws s3 ls
```

This executes the `aws s3 ls` command with credentials from your `my-aws-env` ESC environment. See the [Pulumi ESC CLI documentation](/docs/esc/cli/commands/esc_env/) for more details.
{{% /notes %}}

## Skipping Automatic Dependency Installation

By default, the deployment executor will attempt to install dependencies for your project by using the default dependency manager for the language (i.e. `npm` for nodejs or `virtualenv` for python). However, there may be scenarios where you may want to have more control over the dependency installation step (e.g. you are using `yarn` and/or a different version of `node` than the one that is installed by default).

This is enabled by skipping the default dependency installation step (under Advanced Settings in the UI), and setting a few pre-run commands and environment variables.

![Pulumi UI - Node Version](/docs/deployments/deployments/ui-node-version.png)

## Skipping Intermediate Deployments

By default, when multiple deployments are pushed, they will be executed sequentially until the backlog is completed. In some cases, you may wish to only execute the most recent deployment since the changes are accumulative. By enabling the `Skip intermediate deployments` setting, Pulumi will skip all intermediary deployments of the same type and will execute only the latest.

![Pulumi UI - Skip intermediate deployments](/docs/deployments/deployments/ui-skip-intermediate-deployments.png)

## Custom Executor Images

By default, deployments run inside the [`pulumi/pulumi`](https://hub.docker.com/r/pulumi/pulumi) image, which includes the `pulumi` CLI and [LTS versions](https://github.com/pulumi/pulumi-docker-containers/blob/main/README.md#version-policy) of all supported language runtimes. You can override this from the **Custom Executor Image** field in your stack's deployment settings, either to pin a specific Pulumi CLI version or to use your own image with additional tools.

![Pulumi UI - Custom Executor](/docs/deployments/deployments/ui-custom-executor.png)

For guidance on choosing between a pre-run install hook and a custom image, building a custom image, supported base images, and the trade-offs to consider, see [Deployment execution environment](/docs/deployments/deployments/runs/images/).

## Open ID Connect (OIDC)

Pulumi Deployments supports OIDC for authenticating with cloud providers. This enables your deployments to access your cloud resources without storing static credentials in Pulumi Cloud.

{{% notes type="info" %}}
There are multiple approaches for supplying cloud credentials to Pulumi Deployments. For guidance on choosing between Deployments OIDC and Pulumi ESC, see [Supplying Cloud Credentials to Pulumi Deployments](/docs/deployments/deployments/cloud-credentials/).
{{% /notes %}}

For details on supported clouds see [OIDC Setup for Pulumi Deployments](/docs/deployments/deployments/oidc/).

## Dependency Caching

When using Pulumi-managed agents, you can speed up deployments using dependency caching.

{{% notes type="info" %}}
If you have configured the stack to use a [Customer-managed agent](/docs/deployments/deployments/runs/customer-managed-agents/) runner pool this option is unavailable. Running a customer-managed agent pool gives you full control over the lifetime of the agent and its caching.
{{% /notes %}}

The caching method is simple: during the first deployment, the deployment agent will automatically detect downloaded dependencies using lock files, zip them up and store the archive in blob storage. During all subsequent deployments, agents will pull such an archive down and unpack it, saving time it would normally take to download those dependencies. When your dependencies change, deployment agents will automatically invalidate the old cache and create a new one.

Caches are shared on the project level, so all stacks within a project can share the same cache. However, caches are fully isolated and never shared between customers.

Dependency caching is supported for the following runtimes:

- `.NET` - no special configuration required
- `Python` - ensure that you have `requirements.txt` in the root of your source code.
- `Go` - ensure that you have `go.mod` and `go.sum` in the root of your source code.
- `NodeJS` - only `npm` and `yarn` are currently supported.
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
- `PULUMI_CI_OPERATION`: Current Pulumi operation (`update`, `preview`, `destroy`, `refresh`, `detect-drift`, or `remediate-drift`)

These can be overridden or extended by configuring custom environment variables:

![Pulumi UI - Environment Variables](/docs/deployments/deployments/ui-custom-env-variables.png)

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

---
title_tag: "Deployment Settings | Pulumi Deployments"
meta_desc: Learn how to configure Deployment Settings for Pulumi Deployments
title: "Deployments Settings"
h1: "Pulumi Deployment Settings"
aliases:
- /docs/deployments/deployments/using/settings/
- /docs/pulumi-cloud/deployments/using/settings/
menu:
  deployments:
    name: Deployments Settings
    parent: deployments-concepts
    identifier: deployments-concepts-settings
    weight: 20
---

Deployment settings refer to the full set of configuration required to run a Pulumi Deployment, defined on a per-stack basis. These settings can be managed through the Pulumi Cloud UI, via the REST API, or defined as code with the Pulumi Cloud provider.

## Creating deployment settings

You can create and manage deployment settings in several ways:

### From the Pulumi Cloud UI

From the Pulumi Cloud console, a stack's deployment settings can be accessed via the `Settings > Deploy` tab. Once the settings are defined via the UI, they apply to all Deployment triggers, including push-to-deploy (if you have a [VCS integration](/docs/integrations/version-control/) configured), click-to-deploy and the REST API.

### From the API

Alternatively, a stack's deployment settings may be defined and subsequently modified using the REST API. For more information, see [Patch Settings](/docs/reference/cloud-rest-api/deployments/#patch-settings) in the [Pulumi Deployments REST API docs](/docs/reference/cloud-rest-api/deployments).

### Defined as code with the Pulumi Cloud provider

Finally, a stack's deployment settings may be defined as a resource within the stack itself using the Pulumi Cloud provider. This lets you securely store your settings in source control alongside your code. For more information, see the [`pulumiservice.DeploymentSettings`](https://www.pulumi.com/registry/packages/pulumiservice/api-docs/deploymentsettings/) resource docs in the [Pulumi Registry](/registry).

{{% notes type="info" %}}
Pulumi recommends against a stack defining its own Deployment Settings (that is, including a `pulumiService.DeploymentSettings` resource that defines settings for the current stack), as this would require two deployments for the settings changes to take effect. Instead, create a separate Pulumi program that defines Deployment Settings for multiple stacks that share similar configuration.
{{% /notes %}}

## In this section

- **[Source settings](/docs/deployments/concepts/settings/source/)** — where a deployment gets the Pulumi program it runs: a version control integration, a Git URL, a template, or none.
- **[Path filtering](/docs/deployments/concepts/settings/path-filtering/)** — trigger deployments only when a push changes files you care about, especially useful for monorepos.
- **[Tag filtering](/docs/deployments/concepts/settings/tag-filtering/)** — trigger deployments when a matching git tag is pushed, for release-based workflows.
- **[Deployment runner pools](/docs/deployments/concepts/settings/runner-pools/)** — choose where deployments run, and assign the organization role a deployment uses.
- **[Pre-run commands](/docs/deployments/concepts/settings/pre-run-commands/)** — run arbitrary shell commands before a deployment starts, for setup or authentication.
- **[Skipping automatic dependency installation](/docs/deployments/concepts/settings/skip-dependency-installation/)** — take control of the dependency installation step yourself.
- **[Skipping intermediate deployments](/docs/deployments/concepts/settings/skip-intermediate-deployments/)** — collapse a backlog of queued deployments into a single run.
- **[Custom executor images](/docs/deployments/concepts/settings/custom-executor-images/)** — override the default image to pin a Pulumi version or add your own tools.
- **[Dependency caching](/docs/deployments/concepts/settings/dependency-caching/)** — speed up deployments by caching downloaded dependencies between runs.
- **[Environment variables](/docs/deployments/concepts/settings/environment-variables/)** — the variables Pulumi sets automatically, and how to define your own.

To authenticate with cloud providers using short-lived credentials instead of static secrets, see the [OIDC setup guide](/docs/deployments/guides/oidc/). For task-oriented walkthroughs — supplying cloud credentials, building custom images, and more — see the [Deployments guides](/docs/deployments/guides/).

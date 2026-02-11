---
title: New Project Wizard
title_tag: Get started with New Project Wizard
h1: New Project Wizard
meta_desc: Learn how to create new projects from Organization Templates, with Pulumi Deployments configured out-of-the-box.
menu:
  idp:
    name: New Project Wizard
    parent: idp-concepts
    weight: 30
    identifier: idp-concepts-new-project-wizard
aliases:
- /docs/idp/developer-portals/new-project-wizard/
- /docs/pulumi-cloud/developer-platforms/new-project-wizard/
- /docs/pulumi-cloud/developer-portals/new-project-wizard/
---

The New Project Wizard (NPW) is an interactive interface in the Pulumi Cloud console that streamlines creating new [projects](/docs/iac/concepts/projects/) and [stacks](/docs/iac/concepts/stacks/). The wizard consolidates multiple setup tasks into a single workflow, allowing you to configure project settings, repository details, stack [configuration](/docs/iac/concepts/config/), [deployment settings](/docs/deployments/deployments/), and service assignments all in one place.

## What the New Project Wizard does

The New Project Wizard supports three primary workflows:

1. **Create a new project from a template**: Create a new project and its first stack by forking code from a Pulumi organization [template](/docs/idp/concepts/organization-templates/). This creates a copy of the template code in your repository, which you can then modify independently.
1. **Add a no-code stack to a template**: Add a new stack to an organization template without forking the template code. The template code remains the single source of truth, and the stack references the template directly.
1. **Add a stack to an existing project**: Add a new stack to any existing Pulumi project, whether or not it was originally created from a template.

## Configuration options

Within the New Project Wizard, you can configure:

- **Project configuration**: When creating a new project, set the project name, description, and other metadata
- **Destination repository**: Select an existing repository or create a new one on GitHub
- **Stack configuration values**:
  - Import [ESC environments](/docs/esc/environments/) to provide configuration and secrets
  - Set individual configuration values using a form-based interface (see note below)
- **Deployment settings**: Configure [Pulumi Deployments](/docs/deployments/deployments/) for the new stack, including [drift detection and remediation](/docs/deployments/deployments/drift/)
- **Service assignment**: Assign the new stack to a Pulumi IDP [Service](/docs/idp/concepts/services/)

{{% notes "info" %}}
Configuration value forms are displayed in two scenarios:

1. When the project file (`Pulumi.yaml`) includes a `config` section directly
1. When the project file references an upstream template via `Pulumi.yaml` (e.g., `pulumi:template: https://github.com/org/repo/tree/HEAD/template-name`)

In the second scenario, the form uses the config section from the upstream template.
{{% /notes %}}

## Accessing the New Project Wizard

You can access the New Project Wizard from multiple locations in the Pulumi Cloud console:

To create a new project from a template (fork) or add a no-code stack to a template (no fork):

- Navigate to **Stacks** → **Create Project** → select a template from the card view → select **Use this Template**
- Navigate to **Platform** → **Templates** → select a template → select **Deploy with Pulumi**

To add a stack to an existing project:

- Navigate to **Stacks** → select a stack → select **Add Stack**

## Limitations

- No-code stacks are only supported on GitHub
- When forking templates, destination repositories can only be created on GitHub, even if the source template is hosted on GitLab

## GitHub OAuth application

To use the New Project Wizard with [Pulumi Deployments](/docs/deployments/deployments/), users must authorize a GitHub OAuth application.

The GitHub authorization requires permissions to manage public and private repositories and workflows. Pulumi uses these permissions to read template sources, write template content into repositories, and optionally create new repositories. While the authorization request includes additional repository permissions, Pulumi does not use all of them. This is due to GitHub lacking fine-grained repository permissions as part of the [OAuth application scopes](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps#available-scopes).

{{% notes "info" %}}
Make sure you [install](/docs/deployments/deployments/reference/#github-app-installation) the Pulumi GitHub App to ensure the New Project Wizard works seamlessly with [Pulumi Deployments](/docs/deployments/deployments/).
{{% /notes %}}

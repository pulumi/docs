---
title: New Project Wizard
title_tag: Get started with New Project Wizard
h1: The Pulumi Cloud New Project Wizard
meta_desc: Learn how to create new projects from Organization Templates, with Pulumi Deployments configured out-of-the-box.
menu:
  idp:
    name: New Project Wizard
    parent: idp-developer-portals
    weight: 2
    identifier: idp-developer-portals-npw
aliases:
- /docs/pulumi-cloud/developer-platforms/new-project-wizard/
- /docs/pulumi-cloud/developer-portals/new-project-wizard/
---

Pulumi Cloud provides a New Project Wizard to help walk your organization's members through the process of creating new Pulumi projects. This provides a more turnkey alternative to the [Pulumi Backstage Plugin](/docs/idp/developer-portals/backstage) or custom-built integrations.

By using the wizard, users can generate projects from your [Organization Templates](/docs/idp/developer-portals/templates), commit and push code to GitHub, and trigger an initial deployment -- all in a few clicks and without leaving the browser.

The New Project Wizard supports multiple deployment methods:
- **[Deployments - no-code](#deployments---no-code)**: Deploy without VCS, configuration stored in Pulumi ESC
- **[Deployments - git](#deployments---git)**: Full git integration with automated deployments
- **[CLI](#cli-step-by-step-commands)**: Step-by-step commands for local execution

For git-based deployments, [install](/docs/deployments/deployments/reference/#github-app-installation) the Pulumi GitHub App.

### Deployment method options

#### Deployments - no-code

The no-code deployment method enables users to create and deploy Pulumi stacks without writing to a VCS repository. Stack configuration is stored in [Pulumi ESC](/docs/esc/), making this ideal for self-service workflows where developers need to provision infrastructure quickly without managing source code.

**Requirements:**
- [Pulumi Deployments](/docs/deployments/deployments/) must be enabled for your organization
- Templates must be [organization templates](/docs/idp/developer-portals/templates/) (not public Pulumi templates)

**How it works:**
1. Select a template and provide configuration values
1. Choose "Deployments - no-code" as the deployment method
1. The stack is created and deployed automatically
1. Configuration is stored in Pulumi ESC (no VCS commits required)

For more information on no-code workflows, see [Workflows](/docs/idp/get-started/workflows).

#### Deployments - git

The git deployment method creates a full Pulumi project in a GitHub repository with [Pulumi Deployments](/docs/deployments/deployments/) configured for automated deployments. This is the traditional infrastructure-as-code approach where your Pulumi program is stored in version control.

**Requirements:**
- [Pulumi Deployments](/docs/deployments/deployments/) must be enabled
- The [Pulumi GitHub App](/docs/deployments/deployments/reference/#github-app-installation) must be installed
- Users must authorize the GitHub OAuth application (see [below](#github-oauth-application))

**How it works:**
1. Select a template and provide configuration values
1. Choose "Pulumi Deployments" as the deployment method
1. Select or create a GitHub repository
1. The project is committed to the repository and an initial deployment is triggered

For more detailed instructions, see [Get Started with Deployments](/docs/deployments/deployments/get-started/#new-project-wizard).

#### CLI (step-by-step commands)

If your organization doesn't have Pulumi Deployments configured, you can still use the New Project Wizard to generate projects. Instead of deploying from the browser, you'll receive step-by-step CLI commands to run in your terminal.

**How it works:**
1. Select a template and provide configuration values
1. Copy the generated CLI commands
1. Run the commands locally to create and deploy your project

## GitHub OAuth Application

In order to use the New Project Wizard with [Pulumi Deployments](/docs/pulumi-cloud/deployments), users will be prompted to authorize an additional GitHub OAuth application.

![New Project Wizard OAuth Prompt](/docs/idp/developer-portals/new-project-wizard/npw-github-oauth-prompt.png)

The GitHub authorization will require permissions to manage public and private repositories and workflows.

![New Project Wizard GitHub Permissions Prompt](/docs/idp/developer-portals/new-project-wizard/npw-github-permissions.png)

As part of the New Project Wizard, Pulumi must be able to read template sources, write template source content into repositories, and optionally create new repositories. While the GitHub authorization request will include additional permissions against repositories, Pulumi does not use these. This is due to GitHub lacking fine-grained repository permissions as part of the [OAuth application scopes](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps#available-scopes).

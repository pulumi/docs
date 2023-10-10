---
title: With New Project Wizard
title_tag: New Project Wizard
h1: Building Developer Portals with Pulumi's New Project Wizard
meta_desc: Learn how to create new projects from custom templates, with Deployments configured out-of-the-box.
menu:
  pulumicloud:
    weight: 2
    parent: developer-portals
---

Pulumi Cloud provides a New Project Wizard to help walk your organization's members through the process of creating new Pulumi projects.
This provides a more turn-key alternative to the [Pulumi Backstage plugin](/docs/pulumi-cloud/developer-portals/backstage) or custom-built integrations.

By using the Wizard, users can generate projects from your [custom templates](/docs/pulumi-cloud/developer-portals/templates), commit and pushing code to GitHub, and trigger an initial deployment -- all without leaving their browser.

{{% notes "info" %}}
Make sure you [install](/docs/pulumi-cloud/deployments/reference/#github-app-installation) the Pulumi GitHub App to ensure the New Project Wizard works seamlessly with [Deployments](/docs/pulumi-cloud/deployments).
{{% /notes %}}

The New Project Wizard can be found in the left sidebar:

![New Project Wizard Sidebar Location](../npw-sidebar.png)

If you chose to create a project from a template, you'll be able to pick from one of Pulumi's numerous public templates, or from your organization's [custom templates](/docs/pulumi-cloud/developer-portals/templates). Choosing a "starter" project will produce a small, empty project in your language of choice.

![New Project Wizard](../npw-start.png)

If you've configured your Pulumi organization to work with [Pulumi Deployments](/docs/pulumi-cloud/deployments), you'll be able to commit and deploy your new project entirely from your browser. Otherwise, you'll be able to follow step-by-step instructions to invoke in your terminal.

![New Project Wizard Deployment Method](../npw-deploy-method.png)

For more detailed instructions of how to use the New Project Wizard, see [Get Started with Deployments](/docs/pulumi-cloud/deployments/get-started/#new-project-wizard).

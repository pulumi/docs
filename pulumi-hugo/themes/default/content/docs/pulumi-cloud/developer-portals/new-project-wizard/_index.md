---
title: New Project Wizard
title_tag: Get started with New Project Wizard
h1: The Pulumi Cloud New Project Wizard
meta_desc: Learn how to create new projects from Organization Templates, with Pulumi Deployments configured out-of-the-box.
menu:
  pulumicloud:
    weight: 2
    parent: developer-portals
---

Pulumi Cloud provides a New Project Wizard to help walk your organization's members through the process of creating new Pulumi projects. This provides a more turnkey alternative to the [Pulumi Backstage Plugin](/docs/pulumi-cloud/developer-portals/backstage) or custom-built integrations.

By using the wizard, users can generate projects from your [Organization Templates](/docs/pulumi-cloud/developer-portals/templates), commit and push code to GitHub, and trigger an initial deployment -- all in a few clicks and without leaving the browser.

{{% notes "info" %}}
Make sure you [install](/docs/pulumi-cloud/deployments/reference/#github-app-installation) the Pulumi GitHub App to ensure the New Project Wizard works seamlessly with [Pulumi Deployments](/docs/pulumi-cloud/deployments).
{{% /notes %}}

The New Project Wizard can be found in the left sidebar:

![New Project Wizard Sidebar Location](/docs/pulumi-cloud/developer-portals/new-project-wizard/npw-sidebar.png)

If you chose to create a project from a template, you'll be able to pick from one of Pulumi's numerous public templates, or from your [Organization Templates](/docs/pulumi-cloud/developer-portals/templates). Choosing a "starter" creates a new Pulumi project with some basic scaffolding based on the cloud and language specified.

![New Project Wizard](/docs/pulumi-cloud/developer-portals/new-project-wizard/npw-start.png)

If you've configured your Pulumi organization to work with [Pulumi Deployments](/docs/pulumi-cloud/deployments), you'll be able to commit and deploy your new project entirely from your browser. Otherwise, you'll be able to follow step-by-step CLI commands to invoke in your terminal.

![New Project Wizard Deployment Method](/docs/pulumi-cloud/developer-portals/new-project-wizard/npw-deploy-method.png)

For more detailed instructions on how to use the New Project Wizard with Pulumi Deployments, see [Get Started with Deployments](/docs/pulumi-cloud/deployments/get-started/#new-project-wizard).

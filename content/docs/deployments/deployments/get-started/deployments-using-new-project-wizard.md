---
title: Use Pulumi Deployments with the New Project Wizard
title_tag: Use Pulumi Deployments with the New Project Wizard
meta_desc: Learn how to use Pulumi Deployments with the New Project Wizard
meta_image: /images/docs/meta-images/docs-meta.png
aliases:
- /docs/pulumi-cloud/deployments/get-started/deployments-using-new-project-wizard/
menu:
  deployments:
    name: New Project Wizard
    parent: deployments-deployments-get-started
    weight: 1
    identifier: deployments-deployments-get-started-npw
---

This guide describes how to start using Pulumi Deployments with a new Pulumi IaC project created via the Pulumi Cloud [New Project Wizard](/docs/idp/concepts/new-project-wizard/).

## Prerequisites

Before you start, see the GitHub app [installation instructions](/docs/iac/using-pulumi/continuous-delivery/github-app/#installation-and-configuration) to configure your Pulumi organization to work seamlessly with Deployments.

## New Project Wizard

It's possible to create a new Pulumi project, commit its code, and deploy it entirely from within your browser by using Deployments in combination with the New Project Wizard.

Navigate to the "New Project" tab.
Select "Use a template" if you'd like to create a fully featured project, or select "Use a starter" if you want to create a bare-bones project with only the minimal necessary boilerplate.

In order to use templates you will need to authorize Pulumi with GitHub so that it can clone private repositories as template sources and commit new code for your projects.
Click the button and accept the required permissions if you would like to use templates.

{{% notes "info" %}}
If you select "Use a template" and your Pulumi administrator has configured [custom templates](/docs/idp/concepts/templates) for your organization, you will be able to choose from your organization's custom templates in a later step.
If you select "Use a template" but your organization doesn't have custom templates, you'll be able to choose one of Pulumi's public templates.
{{% /notes %}}

On the next screen, select "Pulumi Deployments" as your deployment method.

{{% notes "info" %}}
You may need to [install the Pulumi GitHub app](/docs/deployments/deployments/reference/#github-app-installation) if you haven't already.
{{% /notes %}}

You'll now be prompted to enter some information about the project you're about to create.

### Project details

Provide a name for the project you're about to create, along with an optional description and a stack name to include.

This impacts the resulting `Pulumi.yaml` file and the name of `Pulumi.<stack>.yaml`.

### Configuration

This section allows you to provide values for any necessary configuration if you're using a [template](/docs/idp/concepts/templates) that declares required configuration keys.

This impacts the `config` stanza in `Pulumi.<stack>.yaml`.

### Environment

If you've configured [environments](/docs/pulumi-cloud/esc) with your organization, you can specify one to use with the resulting stack.

This enables the resulting stack to use a bundle of pre-configured secrets and configuration values without needing to re-specify all of them during project creation.

### Repository details

Here you can configure the repository and optional subdirectory to use when committing your new project code.

{{% notes "info" %}}
If you granted the Pulumi GitHub app access to _all_ repositories, the New Project Wizard will allow users to create projects with Deployments enabled in new repositories.

If the app only has access to _some_ repositories, users will only be able to create new projects with Deployments enabled in _existing_ repositories.
{{% /notes %}}

The GitHub owner is not configurable, as that must match the Pulumi GitHub app's owner in order to work with Deployments.

### Deployment settings

After you've configured your project settings, you will be able to configure the behavior of Deployments, including when to trigger new Deployments and environment variables to include with your updates.

A full description of each setting is available in [Pulumi Deployment Settings](/docs/deployments/deployments/using/settings).

After you've configured everything, you should see a new Deployment of your project.

In summary, after going through this wizard you will have:

* A new Pulumi project and stack, created from a project template or starter.
* Code committed and pushed into a new or existing GitHub repository.
* Pulumi Deployments configured on your new stack, and a preview Deployment in progress.

---
title_tag: Create and Manage cloud infrastructure with Pulumi Deployments | Learn Pulumi
title: "Create Infrastructure with Pulumi Deployments Click-to-Deploy"
layout: single
description: |
    Create infrastructure deployments using the New Project Wizard and GitHub integration to enable push-to-deploy in the Pulumi Cloud.
meta_desc: In this step-by-step tutorial, learn how to create and manage cloud infrastructure using Pulumi Deployments, the New Project Wizard, and GitHub integration.
meta_image: meta.png
weight: 50
summary: |
    In this tutorial, you'll learn how to create, deploy, and manage cloud infrastructure using Pulumi Deployments with Click-to-Deploy. You'll start by using the New Project Wizard to set up and launch infrastructure from your browser, selecting a template to get started quickly. Additionally, you'll configure the Pulumi GitHub App to support additional deployment triggers, including push-to-deploy.
you'll_learn:
  - How to use the New Project Wizard to create and deploy a Pulumi project from your browser
  - How to install and configure the Pulumi GitHub App
  - How to trigger and manage deployments directly from the Pulumi Cloud console using click-to-deploy
prereqs:
    - Completion of the [Getting Started](/docs/get-started/) guide or familiarity with the basics of the Pulumi workflow.
    - The [Pulumi CLI](/docs/install/)
    - A [Pulumi Cloud account](https://app.pulumi.com/signup)
    - An [Amazon Web Services](https://aws.amazon.com/) account
    - A [GitHub account](https://github.com/) with admin rights to a Git repository or organization
    - Familiarity with JavaScript, TypeScript, or Python
estimated_time: 10
allow_long_title: true
---

## What is Pulumi Deployments

[Pulumi Deployments](/docs/pulumi-cloud/deployments/) is a fully managed service designed to automate cloud infrastructure. Deployments provide the building blocks designed for scaling your cloud infrastructure, with tools to power public and private cloud platforms, APIs, and self-service infrastructure portals. These options provide flexibility to incorporate Pulumi Deployments into your existing workflows.

Deployments can be triggered through multiple methods: using the [REST API](/docs/pulumi-cloud/deployments/reference/#deployments-rest-api), integrating with GitHub via [push-to-deploy](/docs/pulumi-cloud/deployments/reference/#github-app-installation), or initiating directly from the [Pulumi Cloud Console](/docs/pulumi-cloud/deployments/reference/#pulumi-console).

## Setup a new Pulumi Deployment

First sign in to Pulumi Cloud via the [Pulumi sign in page](https://app.pulumi.com) or by running `pulumi login` via the Pulumi CLI.

## Install and configure the GitHub App

Next, install and configure the [Pulumi GitHub App](/docs/using-pulumi/continuous-delivery/github-app/) to enable Pulumi Deployment's New Project Wizard and push-to-deploy functionality. Follow the GitHub app [installation instructions](/docs/pulumi-cloud/deployments/reference/#github-app-installation) to ensure your Pulumi organization is set up to work seamlessly with Pulumi Deployments.

## Create a New Project with the New Project Wizard

To create a new Pulumi project, commit its code, and deploy it entirely from your browser, you will use the [New Project Wizard](/docs/pulumi-cloud/developer-portals/new-project-wizard/). The wizard allows you to start from one of Pulumi’s public templates, your [Organization Templates](/docs/pulumi-cloud/developer-portals/templates), or even generate a custom project using the cloud resources and your preferred language of choice with [Pulumi AI](link).

First, navigate to the **New Project** tab in the Pulumi Cloud console. Choose your source template from Pulumi, then you can optionally choose your cloud and language to filter the results or search all templates.

![Animation of how to create a new project in Pulumi Cloud](./pulumi-create-new-project.gif)

{{% notes type="info" %}}
If your Pulumi administrator has configured [custom templates](/docs/pulumi-cloud/developer-portals/templates) for your organization, you will be able to choose from your organization's custom templates from your own image source.
If you select "Use a template" but your organization doesn't have custom templates, you can choose one of Pulumi's public templates to get started.
{{% /notes %}}

Type `aws-python` or `aws-typescript` and click **next**.

### Project details

Provide a name for the project, along with an optional description and the stack name which will be set in the resulting `Pulumi.yaml` file and the name of `Pulumi.<stack>.yaml`.

### Configuration

Provide any values required for the configuration declared in the [template](/docs/pulumi-cloud/developer-portals/templates), in this example, you can set the **aws:region** you would like to deploy into.

These values populate the `config` section in the `Pulumi.<stack>.yaml` file, specifying the necessary settings for your project.

### Environment

If you've configured [environments](/docs/pulumi-cloud/esc) with your organization, you can specify one to use with the resulting stack. Environments enable teams to manage hierarchical collections of configuration and secrets without needing to re-specify all of them during project creation.

{{% notes type="info" %}}
Secret environment variables, such as `AWS_SECRET_ACCESS_KEY`, are encrypted end-to-end and can be set on each stack. However, by creating an environment with Pulumi ESC, you can centralize secrets and set up OIDC for secure authentication. This allows you to manage and share sensitive configuration data across multiple stacks efficiently.
{{% /notes %}}

### Repository

Configure the repository and optional subdirectory to use when committing your new project code.

{{% notes "info" %}}
If you granted the Pulumi GitHub app access to _all_ repositories, the New Project Wizard will allow users to create projects with Deployments enabled in new repositories.

If the app only has access to _some_ repositories, users will only be able to create new projects with Deployments enabled in _existing_ repositories.
{{% /notes %}}

The GitHub owner is not configurable, as that must match the Pulumi GitHub app's owner in order to work with Deployments.

### Deployment settings

Configure the behavior of Deployments, including when to trigger new Deployments and any environment variables required for the Pulumi program to run.

A full description of each setting is available [here](/docs/pulumi-cloud/deployments/reference/#deployment-settings).

### Deployment method

Finally, select Pulumi Deployments as the deployment method and **Create project** to trigger a deployment. You will see your new deployment start within your **Stacks Deployment** tab.

![Animation of how to create a new project in Pulumi](./pulumi-new-project-wizard.gif)

When your deployment is complete, you can now manage and deploy your infrastructure from the Pulumi Cloud Console. In your stack's **Actions** tab, use the **[Click to Deploy](https://www.pulumi.com/docs/pulumi-cloud/deployments/reference/#click-to-deploy)** button to trigger a deployment.

This feature is useful for day-to-day operational tasks, such as debugging a stuck stack or rectifying drift by performing a refresh. With Click to Deploy, you can execute these actions without needing to pull the stack and its source code onto your local machine.

![Image of the Pulumi cloud console actions](./pulumi-cloud-actions.png)

## Cleanup

To avoid incurring any unwanted charges, clean up the resources you created:

1. Navigate to your stack in the Pulumi console.
2. Delete the stack, by clicking on the **Settings** tab and the **Delete stack** button.
3. Delete the GitHub repository you created.

## Next steps

In this tutorial, you set up a basic push-to-deploy stack using Pulumi’s new project wizard. You configured your stack to use the GitHub app, deployed resources, and explored the fundamental Pulumi Deployment browser workflow.

To learn more about creating and managing deployments with Pulumi Cloud, take a look at the following resources:

- **Deployment Triggers**: Understand the different methods to trigger a deployment, such as using the REST API, clicking a button in the Pulumi Console, or using GitHub push-to-deploy. Check out the [Pulumi documentation](https://www.pulumi.com/docs/pulumi-cloud/deployments/reference/#deployment-triggers).

- **Deployment permissions**: Configure and manage deployment permissions to control access and ensure security. Detailed information is available in the [Pulumi documentation](https://www.pulumi.com/docs/pulumi-cloud/deployments/reference/#deployment-permissions).

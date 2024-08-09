---
title_tag: Create and Manage cloud infrastructure with Pulumi Deployments  | Learn Pulumi
title: "Create and manage cloud Infrastructure with Pulumi Deployments Click-to-deploy"
layout: single
description: |
    Create infrastructure deployments using the New Project Wizard and GitHub integration to enable push-to-deploy in the Pulumi Cloud.
meta_desc: In this tutorial, discover how to create and manage cloud infrastructure using Pulumi Deployments, the New Project Wizard, and GitHub integration. Follow step-by-step instructions to set up a Pulumi stack, enable push-to-deploy, and automate resource management through an intuitive, browser-based interface.
meta_image: meta.png
weight: 50
summary: |
    Learn how to create and manage cloud infrastructure using Pulumi Deployments with the New Project Wizard all within your web browser. 

you'll_learn:
  - How to use the New Project Wizard to create and deploy a Pulumi project from your browser
  - How to install and configure the Pulumi GitHub App
  - How to trigger and manage deployments directly from the Pulumi Cloud console using click-to-deploy
prereqs:
    - This tutorial assumes that you are familiar with the basics of the Pulumi workflow. If you are new to Pulumi, complete the [Get Started series](/docs/get-started/) first.
    - Install the [Pulumi CLI](/docs/install/)
    - Create a [Pulumi Cloud account](https://app.pulumi.com/signup)
    - An [Amazon Web Services](https://aws.amazon.com/) account
    - A [GitHub account](https://github.com/) with admin rights to a git repository or organization
    - You have familiarity with JavaScript, TypeScript, or Python
estimated_time: 10
collections:
    - deployments-fundamentals
---

## What is Pulumi Deployments

[Pulumi Deployments](/docs/pulumi-cloud/deployments/) is a fully managed service to create and manage cloud infrastructure automation. Whether you're setting up a new environment, managing existing infrastructure, or building a self-service platform to support your internal engineering team using Pulumi’s [automation APIs](/docs/automation-api/), Pulumi Deployments provides the tools you need to automate your preferred workflows. You can trigger deployments through various methods, such as a [REST API](/docs/pulumi-cloud/deployments/reference/#deployments-rest-api), [push-to-deploy with GitHub](/docs/pulumi-cloud/deployments/reference/#github-app-installation), or directly from the [Pulumi Cloud console](/docs/pulumi-cloud/deployments/reference/#pulumi-console). These options give you the flexibility to fit Pulumi Deployments into your existing processes.

## Setup a new Pulumi Deployment

First sign in to Pulumi Cloud via the [Pulumi sign in page](https://app.pulumi.com) or by running `pulumi login` via the Pulumi CLI.

## Install and configure the GitHub App

Next, install and configure the [Pulumi GitHub App](/docs/using-pulumi/continuous-delivery/github-app/) to enable Pulumi Deployment's New Project Wizard and push-to-deploy functionality. Follow the GitHub app [installation instructions](/docs/pulumi-cloud/deployments/reference/#github-app-installation) to ensure your Pulumi organization is set up to work seamlessly with Pulumi Deployments.

## Create a New Project with the New Project Wizard

You will create a new Pulumi project, commit its code, and deploy it entirely from your browser using the [New Project Wizard](/docs/pulumi-cloud/developer-portals/new-project-wizard/) in combination with Pulumi Deployments. The wizard allows you to start from one of Pulumi’s public templates, your [Organization Templates](/docs/pulumi-cloud/developer-portals/templates), or even generate a custom project using the cloud resources and your prefered language of choice with [Pulumi AI](link).

## Create a new project with the New Project Wizard

You’ll create a new Pulumi project, commit its code, and deploy it entirely from your browser using the [New Project Wizard](/docs/pulumi-cloud/developer-portals/new-project-wizard/) combined with Pulumi Deployments. The wizard lets you start from one of Pulumi’s public templates, your [Organization Templates](/docs/pulumi-cloud/developer-portals/templates), or even generate a custom project tailored to your preferred cloud resources and programming language using [Pulumi AI](link).

First, navigate to the `New Project` tab in the Pulumi Cloud console. Choose your source template from Pulumi, then you can optionally choose your cloud and language to filter the results or search all templates. Type `aws-python` or `aws-typescript` and click `next`.

![Animation of how to create a new project in Pulumi Cloud](./pulumi-create-new-project.gif)

{{% notes "info" %}}
If your Pulumi administrator has configured [custom templates](/docs/pulumi-cloud/developer-portals/templates) for your organization, you will be able to choose from your organization's custom templates from your own image source.
If you select "Use a template" but your organization doesn't have custom templates, you'll be able to choose one of Pulumi's public templates.
{{% /notes %}}

### Project details

Provide a name for the project, along with an optional description and the stack name which will be set in the resulting `Pulumi.yaml` file and the name of `Pulumi.<stack>.yaml`.

### Configuration

Provide any values required for the configuration declared in the [template](/docs/pulumi-cloud/developer-portals/templates), in this example, you can set the`aws:region` you would like to deploy into.

These values populate the `config` section in the `Pulumi.<stack>.yaml` file, specifying the necessary settings for your project.

### Environment

If you've configured [environments](/docs/pulumi-cloud/esc) with your organization, you can specify one to use with the resulting stack. Environments enable teams to manage hierarchical collections of configuration and secrets without needing to re-specify all of them during project creation.

{{% notes "info" %}}
Secret environment variables, such as `AWS_SECRET_ACCESS_KEY`, are encrypted end-to-end and can be set on each stack. However, by creating an Environment with Pulumi ESC, you can centralize secrets and set up OIDC for secure authentication. This allows you to manage and share sensitive configuration data across multiple stacks efficiently.
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

Finally, select Pulumi Deployments as the deployment method and `Create project` to trigger a deployment. You will see your new deployment start within your Stacks Deployment tab.

![Animation of how to create a new project in Pulumi](./pulumi-new-project-wizard.gif)

After setting up your project with the New Project Wizard, you can easily manage and deploy your infrastructure directly from the Pulumi Cloud Console. In the console, navigate to your stack's **Actions** tab. Here, you'll find the **[Click to Deploy](https://www.pulumi.com/docs/pulumi-cloud/deployments/reference/#click-to-deploy)** button, which allows you to trigger a deployment with a single click.

This feature is particularly useful for day-to-day operational tasks, such as debugging a stuck stack or rectifying drift by performing a refresh. With Click to Deploy, you can execute these actions without needing to pull the stack and its source code onto your local machine, streamlining your workflow and saving time.

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
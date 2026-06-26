---
title: Use Pulumi Deployments with the New Project Wizard
title_tag: Use Pulumi Deployments with the New Project Wizard
meta_desc: Learn how to use Pulumi Deployments with the New Project Wizard
aliases:
- /docs/deployments/deployments/get-started/deployments-using-new-project-wizard/
- /docs/pulumi-cloud/deployments/get-started/deployments-using-new-project-wizard/
menu:
  deployments:
    name: New Project Wizard
    parent: deployments-get-started
    weight: 1
    identifier: deployments-deployments-get-started-npw
---

This guide describes how to start using Pulumi Deployments with a new Pulumi IaC project created via the Pulumi Cloud [New Project Wizard](/docs/idp/concepts/new-project-wizard/).

## Prerequisites

Before you start, configure a [version control integration](/docs/integrations/version-control/) for your Pulumi organization. Deployments works with any of Pulumi's version control integrations.

## New Project Wizard

It's possible to create a new Pulumi project, commit its code, and deploy it entirely from within your browser by using Deployments in combination with the New Project Wizard.

Navigate to the "New Project" tab.
Select "Use a template" if you'd like to create a fully featured project, or select "Use a starter" if you want to create a bare-bones project with only the minimal necessary boilerplate.

For this guide, select the `random-typescript` template. This template uses the [Pulumi Random provider](/registry/packages/random/) to generate random values, so the deployment runs to completion without any cloud credentials or [OIDC](/docs/pulumi-cloud/oidc/) configuration — letting you see Deployments work end to end before wiring up a real cloud provider.

In order to use templates you will need to authorize Pulumi with your VCS provider so that it can clone private repositories as template sources and commit new code for your projects.
Click the button and accept the required permissions if you would like to use templates.

{{% notes "info" %}}
If you select "Use a template" and your Pulumi administrator has configured [custom templates](/docs/idp/concepts/templates) for your organization, you will be able to choose from your organization's custom templates in a later step.
If you select "Use a template" but your organization doesn't have custom templates, you'll be able to choose one of Pulumi's public templates.
{{% /notes %}}

On the next screen, select "Pulumi Deployments" as your deployment method.

{{% notes "info" %}}
You may need to configure a [version control integration](/docs/integrations/version-control/) if you haven't already.
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
If you granted the VCS integration access to _all_ repositories, the New Project Wizard will allow users to create projects with Deployments enabled in new repositories.

If the integration only has access to _some_ repositories, users will only be able to create new projects with Deployments enabled in _existing_ repositories.
{{% /notes %}}

The repository owner is not configurable, as that must match the VCS integration's configured owner in order to work with Deployments.

### Deployment settings

After you've configured your project settings, you will be able to configure the behavior of Deployments, including when to trigger new Deployments and environment variables to include with your updates.

A full description of each setting is available in [Pulumi Deployment Settings](/docs/deployments/concepts/settings).

## Run your first deployment

After you finish the wizard, Pulumi Cloud commits your new project to the repository and starts an initial deployment of your stack. Pulumi takes you to the stack's **Deployments** page, where you can watch the deployment run.

Select the in-progress deployment to follow its logs in real time. The deployment runs a `pulumi up` on managed compute, so it provisions the real resources defined by your program.

When the run finishes, its status changes to **Succeeded**. To confirm the operation completed:

* On the **Deployments** page, the latest deployment shows a green **Succeeded** status.
* On the stack's **Resources** page, you'll see the resources your program created.

If a deployment fails, open it to read the logs, fix the underlying issue, and trigger a new deployment from the **Deploy** button.

In summary, after going through this wizard you will have:

* A new Pulumi project and stack, created from a project template or starter.
* Code committed and pushed into a new or existing repository.
* Pulumi Deployments configured on your new stack.
* A successful deployment that provisioned your infrastructure.

## Next steps

Now that you have a stack deploying through Pulumi Deployments, here's where to go next:

* **Authenticate to your cloud without static credentials.** Use [Pulumi ESC](/docs/esc/) to broker short-lived cloud credentials via [OpenID Connect (OIDC)](/docs/esc/guides/configuring-oidc/), then reference that environment from your stack so deployments authenticate to [AWS](/docs/esc/guides/configuring-oidc/aws/), [Azure](/docs/esc/guides/configuring-oidc/azure/), or [GCP](/docs/esc/guides/configuring-oidc/gcp/) without long-lived secrets.
* **Tune your deployment settings.** Review the full set of [deployment settings](/docs/deployments/concepts/settings/) — pre-run commands, environment variables, OIDC, and executor options.
* **Preview changes on pull requests.** Enable [review stacks](/docs/deployments/concepts/review-stacks/) to spin up ephemeral infrastructure for each pull request.
* **Detect and remediate drift.** Turn on [drift detection](/docs/deployments/concepts/drift/) to catch changes made outside of Pulumi.
* **Run operations on a schedule.** Configure [scheduled deployments](/docs/deployments/concepts/schedules/) to run `pulumi up`, `preview`, or `refresh` automatically.

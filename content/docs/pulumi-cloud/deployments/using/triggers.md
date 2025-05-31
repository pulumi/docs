---
title_tag: "Deployment Triggers | Pulumi Deployments"
meta_desc: Learn how to configure and use Deployment Triggers for Pulumi Deployments
title: "Deployment Triggers"
h1: "Deployment Triggers"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  cloud:
    parent: pulumi-cloud-deployments-using
    weight: 2
---

A deployment trigger is a method of initializing a deployment.

## Available Deployments Triggers

Deployments may be triggered in the following ways:

- **[Click to Deploy](#click-to-deploy):** Run any Deployments operation on demand by clicking a button in the Pulumi Cloud console UI
- **[GitHub Push to Deploy](#github-push-to-deploy):** Automatically run a `pulumi preview` when a Pull Request is created and/or run `pulumi up` when a Pull Request is merged
- **[Review Stacks](#review-stacks):** Create and deploy an ephemeral stack on the current branch whenever a new Pull Request is created, and tear it down automatically once the Pull Request is merged
- **[Scheduled Deployments](#scheduled-deployments):** Run any Deployments operation on a recurring basis
- **[TTL Stacks](#ttl-stacks):** Run `pulumi destroy` on a stack (and optionally delete the stack entirely) after a specific amount of time has passed
- **[REST API](#rest-api):** Run any Deployments operation on demand programmatically by issuing an HTTP request against the Pulumi Deployments REST API
- **[Deployment Webhooks](#deployment-webhooks):** Trigger a Deployments operation in response to an event on another stack

## Available Deployments Operations

Pulumi Deployments supports the following operations:

- **Update:** Run the `pulumi up` command to create or update stack resources
- **Preview:** Review changes by running the `pulumi preview` command
- **Refresh:** Update your stack's state file with the current state of your resources from your cloud provider by running the `pulumi refresh` command
- **Destroy:** Delete all resources in your stack by running the `pulumi destroy` command
- **Detect drift:** Refresh your stack's state file with the `pulumi refresh` command and fail if any changes are detected
- **Remediate drift:** Refresh your stack's state file and ensure that the state of your resources matches the declared state in your Pulumi program via the `pulumi update --refresh` command

Note that not every operation is available for every trigger.

## Click to Deploy

A deployment may be triggered on demand by clicking a button in the Pulumi Console. This deployment trigger allows you to perform any supported Pulumi Deployments operation.

![Pulumi UI - Click to Deploy](../../ui-deploy-button.png)

## GitHub Push to Deploy

{{% notes type="info" %}}
Push to Deploy requires the [Pulumi GitHub App](/docs/iac/using-pulumi/continuous-delivery/github-app/#installation-and-configuration) be installed to your GitHub organization. The app requires read access to your repos so it can clone your Pulumi programs and listen to merge commits to automatically trigger deployments on `git push`.
{{% /notes %}}

Pulumi Deployments can run a `pulumi preview` for a stack (e.g., `dev`) when a Pull Request is opened against a particular git branch (e.g., a proposed change to the `main` branch). This will give the reviewer the full context necessary to understand the impact of the changes in your Pull Request: both the code changes _and the changes to your resources_ (i.e., the `pulumi preview` output). The Pulumi GitHub app will create or update a comment on your Pull Request with the results of `pulumi preview`.

{{% notes type="info" %}}
The `pulumi preview` on Pull Request capability requires that the Github user creating the Pull Request has their Github Organization Visibility set to `Public`.
{{% /notes %}}

GitHub Push to Deploy can also be configured to run a `pulumi update` for a stack when changes are merged to a particular git branch. This feature is useful to enable continuous delivery, for example to a shared development or QA environment.

## Scheduled Deployments

[Scheduled Deployments](/docs/pulumi-cloud/deployments/schedules) allow you to define Pulumi Deployments operations that you want to occur on a regular basis. For example, you may want to schedule a nightly deployment for a shared QA environment.

[Drift Detection](/docs/pulumi-cloud/deployments/drift) is a specialized case of a Scheduled Deployment that allows you to ensure that your declared state in your Pulumi program has not diverged from the actual state of your resources.

## TTL Stacks

[TTL (Time to Live) Stacks](/docs/pulumi-cloud/deployments/ttl) are temporary stacks that are automatically destroyed after a specified period of time. TTL Stacks are useful for controlling cloud costs and improving security posture by ensuring resources are torn down once they are no longer needed.

## Review Stacks

[Review Stacks](/docs/pulumi-cloud/deployments/review-stacks) are dedicated cloud environments that get created automatically every time a pull request is opened. Open a pull request, and Pulumi Deployments will stand up a stack with your changes and the Pulumi GitHub App will add a PR comment with the outputs from your deployment. Merge the PR and Pulumi Deployments will destroy the stack and free up the associated resources.

![Review Stack Pull Request Comment](../../comment.png)

## REST API

The Pulumi Deployments REST API allows you to trigger a deployment programmatically. Your stack does not need to have any Deployments Settings pre-defined - you can pass them in as part of the request. Alternatively, if your stack does have defined Deployments Settings, you can override any values by passing them in as part of the request.

For more information, see [Create Deployment](docs/pulumi-cloud/reference/deployments/#create-deployment) in the Pulumi Deployments REST API docs.

## Deployment Webhooks

[Deployment Webhooks](/docs/pulumi-cloud/webhooks/#deployment-webhooks) allow you to trigger Deployments on other stacks when a given event or occurs. Common use cases include:

- Update a dependent stack when an upstream stack (e.g. one that is referenced via a Stack Reference) changes.
- Update a higher environment (e.g. staging) when a lower environment (e.g. QA) successfully updates.

The [Pulumi Auto Deploy package](/registry/packages/auto-deploy) (currently in Preview) allows you to manage dependent stack updates in a declarative fashion.

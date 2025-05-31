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

A deployment trigger refers to a method of initializing a deployment. Deployments may be triggered in the following ways:

- **Click to Deploy:** Run any Deployments operation on demand by clicking a button in the Pulumi Cloud console UI
- **GitHub Push to Deploy:** Automatically run a `pulumi preview` when a Pull Request is created and/or run `pulumi up` when a Pull Request is merged
- **Review Stacks:** Create and deploy (i.e., run `pulumi up` on) an ephemeral stack on the current branch whenever a new Pull Request is created, and tear it down automatically once the Pull Request is merged
- **REST API:** Run any Deployments operation on demand by issuing an HTTP request against the Pulumi Deployments REST API
- **Scheduled Deployments:** Run any Deployments operation on a recurring basis
- **TTL Stacks:** Run `pulumi destroy` on a stack (and optionally delete the stack entirely) after a specific amount of time has passed

Pulumi Deployments supports the following operations:

- **Update:** Run the `pulumi up` command to create or update stack resources
- **Preview:** Review changes by running the `pulumi preview` command
- **Refresh:** Update your stack's state file with the current state of your resources from your cloud provider by running the `pulumi refresh` command
- **Destroy:** Delete all resources in your stack by running the `pulumi destroy` command
- **Detect drift:** Refresh your stack's state file with the `pulumi refresh` command and fail if any changes are detected
- **Remediate drift:** Refresh your stack's state file and run `pulumi update` to ensure that the state of your resources matches the declared state in your Pulumi program

## Click to Deploy

A deployment may be triggered on demand by clicking a button in the Pulumi Console.

![Pulumi UI - Click to Deploy](../../ui-deploy-button.png)

## GitHub Push to Deploy

Once you have the GitHub application installed in your Pulumi organization, you can choose to have deployments run a `pulumi preview` when Pull Requests are opened against a target branch, or `pulumi up` when a commit is pushed to a branch.

{{% notes type="info" %}}
The `pulumi preview` on Pull Request capability requires that the Github user creating the Pull Request has their Github Organization Visibility set to `Public`.
{{% /notes %}}

![Pulumi UI - Push to Deploy](../../ui-push-to-deploy.png)

### Configuring push-to-deploy from GitHub

#### GitHub App Installation

To use push-to-deploy functionality, you'll need to install and configure the [Pulumi GitHub App](/docs/iac/using-pulumi/continuous-delivery/github-app/#installation-and-configuration). The app requires read access to your repos so it can clone your Pulumi programs and listen to merge commits to automatically trigger deployments on `git push`.

The complete installation instructions are available in the [GitHub App documentation](/docs/iac/using-pulumi/continuous-delivery/github-app/#installation-and-configuration).

#### Configuring settings

Once the GitHub app has been installed, the deployment settings for a stack can be defined using the methods defined in the [Deployment Settings](./settings) section.

## TTL Stacks

TTL (Time to Live) Stacks are temporary stacks that are automatically destroyed after a specified period of time. They're ideal for ephemeral environments, such as testing or development environments, where cleanup is important.

For more information on TTL Stacks, see the [TTL Stacks documentation](../../ttl).

## Review Stacks

[Review Stacks](../../review-stacks) are dedicated cloud environments that get created automatically every time a pull request is opened, all powered by Pulumi Deployments. Open a pull request, and Pulumi Deployments will stand up a stack with your changes and the Pulumi GitHub App will add a PR comment with the outputs from your deployment. Merge the PR and Pulumi Deployments will destroy the stack and free up the associated resources.

![Review Stack Pull Request Comment](../../comment.png)

## REST API

Once deployment settings are defined for a stack, triggering a deployment is as simple as a one-line request.

```POST https://api.pulumi.com/api/stacks/{org}/{project}/{stack}/deployments```

```json
{
    "operation": "update/preview/refresh/destroy"
}
```

If you need to override some specific settings, you can specify them in the request body.

```POST https://api.pulumi.com/api/stacks/{org}/{project}/{stack}/deployments```

```json
{
    "operation": "update/preview/refresh/destroy",
    "operationContext": {
        "environmentVariables": {
            "EXTRA_VAR": {
                "secret": "my-super-secret-value"
            }
        }
    }
}
```

If you would rather not use the predefined settings at all, you must set `inheritSettings` to `false` in your request body and define the entire settings object.

The merge behavior of deployment settings are further explained in the [REST API documentation](../../api).

---
title: Use Pulumi Deployments with the Pulumi and GitHub CLIs
title_tag: Use Pulumi Deployments with the Pulumi and GitHub CLIs
meta_desc: Learn how to use Pulumi Deployments with the Pulumi and GitHub CLIs
aliases:
- /docs/deployments/deployments/get-started/deployments-using-cli/
- /docs/pulumi-cloud/deployments/get-started/deployments-using-cli/
menu:
  deployments:
    name: Pulumi and GitHub CLIs
    parent: deployments-get-started
    weight: 1
    identifier: deployments-deployments-get-started-cli
---

## Creating a new project manually

This walk-through shows you how to create a new project using `pulumi new`, upload to GitHub using the `gh` CLI, and then configure Pulumi Deployments.

### Prerequisites

Before you start, configure a [version control integration](/docs/integrations/version-control/) for your Pulumi organization. Deployments works with any of Pulumi's version control integrations. This walkthrough uses GitHub and the `gh` CLI, but the same workflow applies to any supported provider.

You will need the following tools to complete this tutorial:

* The [Pulumi CLI](/docs/install/)
* The [GitHub CLI](https://cli.github.com/)

### Create project and upload to a new GitHub repository

* Create a project by running `pulumi new` with the `random-typescript` template. Passing the template name and `--yes` accepts the default project name (the directory name), description, and stack name without prompting. This template uses the [Pulumi Random provider](/registry/packages/random/) to generate random values, so the deployment runs to completion without any cloud credentials or [OIDC](/docs/pulumi-cloud/oidc/) configuration — letting you see Deployments work end to end before wiring up a real cloud provider.

```bash
$ mkdir test_deployments && cd test_deployments
$ pulumi new random-typescript --yes
Created project 'test_deployments'
Created stack 'dev'
Installing dependencies...
Finished installing dependencies

Your new project is ready to go!
```

This creates a stack for you under your default Pulumi organization in Pulumi Cloud.

* Initialize the local git repository:

```bash
$ git init -b main
$ git add .
$ git commit -m "first commit"
```

* Create a new GitHub repository and push the local code.  Replace `<github_owner>` with your own GitHub owner.

```bash
$ gh repo create <github_owner>/test_deployments --private --source=. --push
✓ Created repository <github_owner>/test_deployments on GitHub
✓ Pushed commits to https://github.com/<github_owner>/test_deployments.git
```

### Configure deployment settings

Now that we have a GitHub repository, we can configure it to use Pulumi Deployments.

1. In [Pulumi Cloud](https://app.pulumi.com), select **Stacks** in the left navigation and open your `test_deployments/dev` stack.

1. From the stack page, select **Settings**, then **Deploy** in the left navigation to open the deployment settings.

1. Under **Source control settings**, connect the stack to your repository:

   * Select **GitHub** as the source control provider.
   * Select the `test_deployments` repository you created earlier.
   * Select the `main` branch.
   * Leave the **Pulumi.yaml folder** blank, since the project lives in the repository root.

1. The `random-typescript` template needs no cloud credentials, so you can leave the remaining settings at their defaults. When you later deploy a project that provisions cloud resources, this is where you'd configure things like:

   * [OIDC Connect](/docs/pulumi-cloud/oidc/) for cloud authentication
   * [Environment Variables](/docs/deployments/concepts/settings/#environment-variables)

   See [Pulumi Deployment Settings](/docs/deployments/concepts/settings) for more information about the available settings.

1. Select **Save deployment configuration** to save your settings.

### Run your first deployment

With deployment settings saved, you can run a deployment:

1. Select the **Deploy** button in the top right of the stack page to trigger a deployment.

1. Pulumi Cloud takes you to the deployment's page, where you can watch the logs in real time. The deployment runs a `pulumi up` on managed compute, so it provisions the resources defined by your program — in this case, the random values created by the `random-typescript` template.

1. When the run finishes, its status changes to **Succeeded**. Confirm the operation completed:

   * On the stack's **Deployments** page, the latest deployment shows a green **Succeeded** status.
   * On the stack's **Resources** page, you'll see the resources your program created.

If a deployment fails, open it to read the logs, fix the underlying issue, and select **Deploy** again to trigger a new deployment.

In summary, after completing this walkthrough you will have:

* A new Pulumi project and stack, created locally with `pulumi new`.
* Code committed and pushed to a new GitHub repository.
* Pulumi Deployments configured on your stack.
* A successful deployment that provisioned your infrastructure.

## Next steps

Now that you have a stack deploying through Pulumi Deployments, here's where to go next:

* **Authenticate to your cloud without static credentials.** Use [Pulumi ESC](/docs/esc/) to broker short-lived cloud credentials via [OpenID Connect (OIDC)](/docs/esc/guides/configuring-oidc/), then reference that environment from your stack so deployments authenticate to [AWS](/docs/esc/guides/configuring-oidc/aws/), [Azure](/docs/esc/guides/configuring-oidc/azure/), or [GCP](/docs/esc/guides/configuring-oidc/gcp/) without long-lived secrets.
* **Tune your deployment settings.** Review the full set of [deployment settings](/docs/deployments/concepts/settings/) — pre-run commands, environment variables, OIDC, and executor options.
* **Preview changes on pull requests.** Enable [review stacks](/docs/deployments/concepts/review-stacks/) to spin up ephemeral infrastructure for each pull request.
* **Detect and remediate drift.** Turn on [drift detection](/docs/deployments/concepts/drift/) to catch changes made outside of Pulumi.
* **Run operations on a schedule.** Configure [scheduled deployments](/docs/deployments/concepts/schedules/) to run `pulumi up`, `preview`, or `refresh` automatically.

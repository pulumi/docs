---
title: Pulumi GitHub Actions
meta_desc: Pulumi's Github Actions help you deploy apps and infrastructure to your cloud of
           choice, using nothing but code in your favorite language and GitHub.
menu:
    userguides:
        parent: cont_delivery
        weight: 1

aliases:
- /docs/reference/cd-github-actions/
- /docs/console/continuous-delivery/github-actions/
---

Pulumi's [GitHub Actions](https://developer.github.com/actions) help you deploy apps and
infrastructure to your cloud of choice, using nothing but code in your favorite language
and GitHub. This includes previewing, validating, and collaborating on proposed
deployments in the context of Pull Requests, and triggering deployments or promotions
between different environments by merging or directly committing changes.

Let's see how to get started -- it's easy!

## Pre-Requisites

Before proceeding, you'll need to [Sign Up for Pulumi](https://app.pulumi.com/) (if you
haven't already). This guide also assumes you've reviewed the [GitHub Actions
documentation](https://help.github.com/en/categories/automating-your-workflow-with-github-actions)
and are generally familiar with its concepts and syntax.

For your workflow to do anything interesting, you'll want to create a new Pulumi project
for it. There are three ways to do this:

1. [Clone an existing Pulumi example](https://github.com/pulumi/examples)
2. [Use the New Project wizard](https://app.pulumi.com/site/new-project)
3. [Download the CLI]({{< relref "/docs/get-started/install" >}}) and run `pulumi new` to
   select a template

## Creating a Workflow

Although the full power of the Pulumi CLI is available to use with GitHub Actions, we
recommend starting with our standard workflow, which consists of two workflow files, each
triggered by common GitHub events:

1. **Pulumi Preview** runs `pulumi preview` in response to a Pull Request, showing a preview of the changes
   to the target branch when the PR gets merged.
2. **Pulumi Up** runs `pulumi up` on the target branch, in response to a commit on that
   branch.

### Committing the Workflow Files

Let's get started by adding these two new workflow files to the GitHub repository
containing your Pulumi project.

#### The pull_request Workflow File

Add a new file to your Pulumi project repository at `.github/workflows/pull_request.yml`
containing the following workflow definition, which instructs GitHub Actions to run
`pulumi preview` in response to all `pull_request` events:

```yaml
name: Pulumi
on:
  - pull_request
jobs:
  preview:
    name: Preview
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v1
        with:
          fetch-depth: 1
      - run: scripts/build
      - uses: docker://pulumi/actions
        with:
          args: preview
        env:
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          PULUMI_ACCESS_TOKEN: ${{ secrets.PULUMI_ACCESS_TOKEN }}
          PULUMI_CI: pr

```

Note that by using the `pulumi/actions` Docker image, the workflow will automatically
download and use the latest version of Pulumi. If you prefer to use a specific version of
Pulumi, you can replace all occurrences of `uses: "docker://pulumi/actions"` in this and
other workflow files with a container reference that appends the desired version as a tag ---
for example, `uses: "docker://pulumi/actions:v1.0.0"`.

Also note that we've set several environment variables, some of which are referenced as [GitHub Actions secrets](https://help.github.com/en/articles/virtual-environments-for-github-actions#creating-and-using-secrets-encrypted-variables) (which we'll provide values for later), to expose to the workflow job at runtime.

Lastly, we've also included a preliminary `Build` step, in order to to demonstrate
running a setup script in advance of Pulumi. Feel free to remove this step if it doesn't
suit your particular situation.

#### The push Workflow File

Next, add a second workflow file at `.github/workflows/push.yml` containing the following
definition, which tells GitHub to run `pulumi up` in response to a commit on the `master`
branch:

```yaml
name: Pulumi
on:
  push:
    branches:
      - master
jobs:
  up:
    name: Update
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v1
        with:
          fetch-depth: 1
      - run: scripts/build
      - uses: docker://pulumi/actions
        with:
          args: up
        env:
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          PULUMI_ACCESS_TOKEN: ${{ secrets.PULUMI_ACCESS_TOKEN }}
          PULUMI_CI: up
```

Now that you've got these two common workflows defined, you'll need to configure your
secrets. Secrets are exposed as environment variables to the GitHub Actions runtime
environment. Minimally, you'll need to supply a Pulumi access token to allow the Pulumi CLI to
communicate with the Pulumi Service on your behalf, and you'll probably want to provide
credentials for communicating with your cloud provider as well.

### Configuring Your Secrets

With your workflow files committed and pushed to GitHub, head on over
to your repo's **Settings** tab, where you'll find the new **Secrets** area:

![Secrets](/images/docs/reference/gh-actions-secrets.png)

First, [create a new Pulumi Access Token](https://app.pulumi.com/account/tokens), then
submit that token as a new secret named named `PULUMI_ACCESS_TOKEN`. This enables your
GitHub Action to communicate with the Pulumi service on your behalf.

Next, add secrets for your cloud credentials, just as you did `PULUMI_ACCESS_TOKEN` above,
based on your provider of choice. For example:

* `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` for [AWS]({{< relref "/docs/intro/cloud-providers/aws/setup.md" >}})
* `ARM_CLIENT_ID`, `ARM_CLIENT_SECRET`, and `ARM_TENANT_ID` for [Azure]({{< relref "/docs/intro/cloud-providers/azure/setup.md" >}})
* `GOOGLE_CREDENTIALS` for [GCP]({{< relref "/docs/intro/cloud-providers/gcp/setup.md" >}})
* `KUBECONFIG` for [Kubernetes]({{< relref "/docs/intro/cloud-providers/kubernetes/setup.md" >}})

## Try It Out!

To try things out, simply create a Pull Request or commit, and you will see these new
actions showing up in the usual GitHub Checks dialog, with a green checkmark if everything
went as planned:

![Action Checks](/images/docs/reference/gh-actions-checks.png)

Click the Logs pane to see the full output of the Pulumi CLI, along with the URL of your
deployment on the Pulumi Console with more details:

![Action Logs](/images/docs/reference/gh-actions-logs.png)

For even better Pull Request integration, make sure to also [install our GitHub App]({{< relref "github-app.md" >}})!

![Action Pull Requests](/images/docs/reference/gh-actions-prs.png)

## Pull Request Flow

If you are using Pulumi's GitHub Actions to preview infrastructure changes from Pull
Requests, you may want to have Pulumi comment on those PRs so that you don't need to look
at the specific update logs to see if there were any changes.

There are two ways to do this: using the Pulumi GitHub App (recommended), or configuring
the GitHub Actions container directly.

### Pulumi GitHub App

The [Pulumi GitHub App]({{< relref "github-app.md" >}}) is something you install on your
GitHub organization. It allows the Pulumi service to leave comments on Pull Requests but does not give it access to your source code.

Once the Pulumi GitHub App is installed, when your GitHub Actions run Pulumi, a summary of
any resource changes will be left on the Pull Request, as well as links to the Pulumi
Console for more detailed information.

You can install the Pulumi GitHub App now, by visiting
[github.com/apps/pulumi](https://github.com/apps/pulumi) or clicking the button below.

<a class="btn" href="https://github.com/apps/pulumi" target="_blank">
    INSTALL
</a>

Example comment when using the Pulumi GitHub App:

![Comment from the Pulumi GitHub App](/images/docs/github-actions/pr-comment-gh-app.png)

### Comments By GitHub Actions

If you don't want to use the Pulumi GitHub App, you can configure Pulumi's GitHub Actions
to copy the output of the `pulumi` invocation on the Pull Request. This option doesn't
have as rich an output display as the Pulumi GitHub App, as it simply copies the raw
output of the Pulumi CLI.

To allow your GitHub Action to leave Pull Request comments, you'll need to set the
`COMMENT_ON_PR` environment variable, and add `GITHUB_TOKEN` to the list of `secrets`
passed to the action. (The `GITHUB_TOKEN` value will already be set in the running
environment, so there's no need to add one explicitly as a secret.) Add the following two
lines to the `env` block of the preview action:

```diff
name: Pulumi
on:
  - pull_request
jobs:
  preview:
    ...
    steps:
      ...
      - uses: docker://pulumi/actions
        with:
          args: preview
        env:
          ...
          PULUMI_CI: pr
          COMMENT_ON_PR: 1
```

Example comment when using GitHub Actions directly:

![Comment from GitHub Actions](/images/docs/github-actions/pr-comment-actions.png)

## Configuration

You can configure how Pulumi's GitHub Actions work to have more control about which stacks get updated, and when.

### Using a Different Root Directory

By default, the Pulumi GitHub Action assumes your Pulumi project is in your repo's root
directory. If you are using a different root directory for your project, simply set the
`PULUMI_ROOT` variable in your workflow action, with a relative path to your Pulumi
project directory. For example:

```hcl
name: Pulumi
on:
  - pull_request
jobs:
  preview:
    ...
    steps:
      ...
        env:
          ...
          PULUMI_ROOT: infra
```

This tells Pulumi that the project can be found underneath the repo's `infra` directory.

### Branch Mappings

Pulumi has a concept of *stacks*, which are isolated environments for your application
(e.g., production, staging, or even distinct services). By default, the GitHub Action will
assume a project has a single stack, and will associate the `master` branch with it. For
more sophisticated scenarios, this can be overridden by adding a `.pulumi/ci.json` file to
your repository as well.

This file is simply a JSON map of GitHub branch names to Pulumi stacks. For example:

```json
{
    "master": "production",
    "staging": "staging"
}
```

Often, we'll map `master` to a `production` stack, and `staging` to a distinct `staging`
stack, and then use Pull Requests to promote code between the two. This mappings file is
intentionally flexible.

Note that you'll need to create these stacks [in the usual
way]({{< relref "/docs/intro/concepts/stack" >}}) using the Pulumi Console or CLI.
After setting this up, everything will be on autopilot.

## Demos and Examples

To see some examples of this in action, see the following links:

* [Our introductory blog post]({{< relref "continuous-delivery-to-any-cloud-using-github-actions-and-pulumi" >}})
* [Dockerized Ruby on Rails, in Kubernetes, with hosted Cloud SQL](https://github.com/pulumi/actions-example-gke-rails)
* [Short 90 second video from GitHub Universe Keynote](https://www.youtube.com/watch?time_continue=56&v=59SxB2uY9E0)
* [Short 90 second video on GitOps and Pull Request workflows](https://www.youtube.com/watch?v=MKbDVDBuKUA)
* [Longer 7 minute video exploring the ins and outs of Pulumi GitHub Actions in practice](https://www.youtube.com/watch?time_continue=1&v=1Et2TkuxqJg)

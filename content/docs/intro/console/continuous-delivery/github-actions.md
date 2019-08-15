---
title: Pulumi GitHub Actions

menu:
    console:
        parent: cont_delivery

aliases: [/docs/reference/cd-github-actions/]
---

Pulumi's [GitHub Actions](https://developer.github.com/actions) help you deploy apps and infrastructure
to your cloud of choice, using nothing but code in your favorite language and GitHub. This includes previewing,
validating, and collaborating on proposed deployments in the context of Pull Requests, and triggering deployments
or promotions between different environments by merging or directly committing changes.

Let's see how to get started -- it's easy!

> **Note**: GitHub Actions is currently in public beta. Please [register for
> access](https://github.com/features/actions) to start using the feature. Until you've been added, the
> **Actions** tab won't show in your repos, and the `.pulumi/main.workflow` file described
> below will not be recognized by GitHub. Also note that these features only work on
> private repos in the specific account that has been granted access.

# Pre-Requisites

Before proceeding, you'll need to [Sign Up for Pulumi](https://app.pulumi.com/) (if you haven't already).

For your workflow to do anything interesting, you'll want to create a new Pulumi project.
There are three ways to do this:

1. [Clone an existing Pulumi example](https://github.com/pulumi/examples)
2. [Use the New Project wizard](https://app.pulumi.com/site/new-project)
3. [Download the CLI]({{< relref "/docs/reference/install.md" >}}) and run `pulumi new` to select a template

# Creating a Workflow

Although the full power of the Pulumi CLI is available to use with GitHub Actions, we recommend starting with
our standard workflow, which consists of two actions, both triggered by GitHub events:

1. **Pulumi Preview (Merged Stack)** runs `pulumi preview` in response to a Pull Request, showing what would happen if the PR were merged into the target branch.
2. **Pulumi Deploy (Current Stack)** runs `pulumi up` on the target branch, in response to a commit on that branch.

From here, there are two ways to configure actions in your repo: in code, by committing a
workflow file in your project repository, or by using the visual editor on GitHub.com.

We'll start with the file-based approach, but if you'd prefer to use the visual editor
instead, you can [skip to that section now](#using-the-visual-editor).

## Committing the Workflow File

Let's get started by adding a new workflow file to the GitHub repository containing your
Pulumi project.

To set up the workflow to run anytime you make a commit or a Pull Request (including
successive commits on PR branches), add a new file to the repository at
`.github/main.workflow`:

```hcl
action "Build" {
    uses = "docker://alpine"
    runs = ["scripts/build"]
}

workflow "Preview" {
    on = "pull_request"
    resolves = "Pulumi Preview (Merged Stack)"
}

action "Pulumi Preview (Merged Stack)" {
    needs = ["Build"]
    uses = "docker://pulumi/actions"
    args = ["preview"]
    env = {
        PULUMI_CI = "pr"
    }
    secrets = [
        "PULUMI_ACCESS_TOKEN"
    ]
}

workflow "Update" {
    on = "push"
    resolves = ["Pulumi Deploy (Current Stack)"]
}

action "Pulumi Deploy (Current Stack)" {
    needs = ["Build"]
    uses = "docker://pulumi/actions"
    args = ["up"]
    env = {
        PULUMI_CI = "up"
    }
    secrets = [
        "PULUMI_ACCESS_TOKEN"
    ]
}
```

Note that by using the `pulumi/actions` Docker image, these workflow actions will
automatically download and use the latest version of Pulumi. If you prefer to use a
specific version of Pulumi, you can replace all occurrences of `uses =
"docker://pulumi/actions"` with a container image that contains the version as a tag. For
instance `uses = "docker://pulumi/actions:v0.16.6"`.

We've also included a preliminary `Build` action &mdash; and declared it as a
dependency of both the Preview and Update actions &mdash; in order to demonstrate running
a setup script in advance of Pulumi. Feel free to remove this block (and the `needs`
references to it) if it doesn't suit your particular situation.

Now that you've got a workflow defined, you'll need to configure your secrets. Secrets are
exposed as environment variables to the GitHub Actions runtime environment. Minimally,
we'll need to supply a Pulumi access token in order to allow Pulumi CLI to communicate
with the Pulumi Service on your behalf, and you'll probably want to provide credentials
for communicating with your cloud provider as well.

## Configuring Your Secrets

After committing the workflow file into your repo as `.github/main.workflow`, head on over
to your repo's **Settings tab**, where you'll find the new **Secrets area**:

![Secrets](/images/docs/reference/gh-actions-secrets.png)

First, [create a new Pulumi Access Token](https://app.pulumi.com/account/tokens), then
submit that token as a new secret named named `PULUMI_ACCESS_TOKEN`. This enables your
GitHub Action to communicate with the Pulumi service.

Next, add secrets for your cloud credentials, just as you did `PULUMI_ACCESS_TOKEN` above,
based on your provider of choice. For example:

* `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` for [AWS]({{< relref "/docs/reference/clouds/aws/setup.md" >}})
* `ARM_CLIENT_ID`, `ARM_CLIENT_SECRET`, and `ARM_TENANT_ID` for [Azure]({{< relref "/docs/reference/clouds/azure/setup.md" >}})
* `GOOGLE_CREDENTIALS` for [GCP]({{< relref "/docs/reference/clouds/gcp/setup.md" >}})
* `KUBECONFIG` for [Kubernetes]({{< relref "/docs/reference/clouds/kubernetes/setup.md" >}})

> **Important**: Remember to add these variable names to the `secrets` lists in your
> workflow `action` blocks, or GitHub Actions won't make them available to the running
> container, and things will behave as if you hadn't set them at all!

# Using the Visual Editor

All of the above can be done using GitHub's visual editor if you prefer. We have listed
the manual instructions because not everybody will see the new UI while GitHub Actions is
in preview. But after your initial setup, this UI will become available, and you may find
it more convenient to edit things visually.

1. Go to your repo on GitHub, and click on the new **Actions** tab:

    ![Editor Actions Tab](/images/docs/reference/gh-actions-editor-tab.png)

2. Click the **Create a new workflow** button:

    ![Editor Create Workflow](/images/docs/reference/gh-actions-editor-create.png)

3. Click the **Edit new file** tab:

    ![Editor New File](/images/docs/reference/gh-actions-editor-newfile.png)

4. Replace the default workflow with the one we provided described above, along with your customizations:

    ![Editor Workflow Edit](/images/docs/reference/gh-actions-editor-edit.png)

If you select the **Visual editor** tab, you'll see the resulting workflow actions, and all secrets may be edited:

![Editor Visual Edit](/images/docs/reference/gh-actions-editor-visual.png)

To edit your secrets, scroll down and select the first Pulumi action, and click **Edit**:

![Editor Edit](/images/docs/reference/gh-actions-editor-configure.png)

This will open the action editor on the right-hand side, in which you'll enter your
various credentials (for Pulumi and your cloud). After configuring these, you should see
the green secrets with lock icons show up for your actions:

![Editor Secrets](/images/docs/reference/gh-actions-editor-secrets.png)

# Try It Out!

To try things out, simply create a Pull Request or commit, and you will see these new
actions showing up in the usual GitHub Checks dialog, with a green checkmark if everything
went as planned:

![Action Checks](/images/docs/reference/gh-actions-checks.png)

Click the Logs pane to see the full output of the Pulumi CLI, along with the URL of your
deployment on the Pulumi Cloud Console with more details:

![Action Logs](/images/docs/reference/gh-actions-logs.png)

For even better Pull Request integration, make sure to also [install our GitHub App]({{< relref "github-app.md" >}})!

![Action Pull Requests](/images/docs/reference/gh-actions-prs.png)

# Pull Request Flow

If you are using Pulumi's GitHub Actions to preview infrastructure changes from Pull
Requests, you may want to have Pulumi comment on those PRs so that you don't need to look
at the specific update logs to see if there were any changes.

There are two ways to do this: using the Pulumi GitHub App (recommended), or configuring
the GitHub Actions container directly.

## Pulumi GitHub App

The [Pulumi GitHub App]({{< relref "github-app.md" >}}) is something you install on your
GitHub organization. It allows the Pulumi service to leave comments on Pull Requests but does not give it access to your source code.
does not have access to your source code.)

Once the Pulumi GitHub App is installed, when your GitHub Actions run Pulumi, a summary of
any resource changes will be left on the Pull Request, as well as links to the Pulumi
Cloud Console for more detailed information.

You can install the Pulumi GitHub App now, by visiting
[github.com/apps/pulumi](https://github.com/apps/pulumi) or clicking the button below.

<a class="btn" href="https://github.com/apps/pulumi" target="_blank">
    INSTALL
</a>

Example comment when using the Pulumi GitHub App:

![Comment from the Pulumi GitHub App](/images/docs/github-actions/pr-comment-gh-app.png)

## Comments By GitHub Actions

If you don't want to use the Pulumi GitHub App, you can configure Pulumi's GitHub Actions
to copy the output of the `pulumi` invocation on the Pull Request. This option doesn't
have as rich an output display as the Pulumi GitHub App, as it simply copies the raw
output of the Pulumi CLI.

To allow your GitHub Action to leave Pull Request comments, you'll need to set the
`COMMENT_ON_PR` environment variable, and add `GITHUB_TOKEN` to the list of `secrets`
passed to the action. (The `GITHUB_TOKEN` value will already be set in the running
environment, so there's no need to add one explicitly as a secret.) For example:

```hcl
action "Pulumi Preview (Merged Stack)" {
  uses = "docker://pulumi/actions"
  args = ["preview"]
  env = {
    PULUMI_CI = "pr"
    COMMENT_ON_PR = "1"
  }
  secrets = [
    "PULUMI_ACCESS_TOKEN",
    "GITHUB_TOKEN"
  ]
}
```

Example comment when using GitHub Actions directly:

![Comment from GitHub Actions](/images/docs/github-actions/pr-comment-actions.png)

# Configuration

You can configure how Pulumi's GitHub Actions work to have more control about which stacks get updated, and when.

## Using a Different Root Directory

By default, the Pulumi GitHub Action assumes your Pulumi project is in your repo's root
directory. If you are using a different root directory for your project, simply set the
`PULUMI_ROOT` variable in your workflow action, with a relative path to your Pulumi
project directory. For example:

```hcl
action "Pulumi Deploy (Current Stack)" {
    ...
    env = {
        PULUMI_ROOT = "infra"
    }
}
```

This tells Pulumi that the project can be found underneath the repo's `infra` directory.

## Branch Mappings

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
way](https://www.pulumi.com/docs/reference/stack/) using the Pulumi Cloud Console or CLI.
After setting this up, everything will be on autopilot.

# Demos and Examples

To see some examples of this in action, see the following links:

* [Our introductory blog post]({{< relref "continuous-delivery-to-any-cloud-using-github-actions-and-pulumi" >}})
* [Dockerized Ruby on Rails, in Kubernetes, with hosted Cloud SQL](https://github.com/pulumi/actions-example-gke-rails)
* [Short 90 second video from GitHub Universe Keynote](https://www.youtube.com/watch?time_continue=56&v=59SxB2uY9E0)
* [Short 90 second video on GitOps and Pull Request workflows](https://www.youtube.com/watch?v=MKbDVDBuKUA)
* [Longer 7 minute video exploring the ins and outs of Pulumi GitHub Actions in practice](https://www.youtube.com/watch?time_continue=1&v=1Et2TkuxqJg)

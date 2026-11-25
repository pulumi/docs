---
title_tag: "Cursor Origin Integration | Version Control"
meta_desc: Connect Cursor Origin to Pulumi Cloud to preview infrastructure changes on pull requests, deploy on push, create review stacks, and report checks.
title: Cursor Origin
h1: Cursor Origin
menu:
    integrations:
        name: Cursor Origin
        identifier: integrations-version-control-cursor-origin
        parent: integrations-version-control
        weight: 6
---

Pulumi Cloud integrates with Cursor Origin through the Pulumi app for Cursor Origin. Once you install the app and link it to your Pulumi organization, Pulumi shows how each pull request would change your infrastructure. It adds a comment that summarizes the resources that would be created, updated, or deleted, and a check that links to the full results in Pulumi Cloud. You can keep running Pulumi from your existing workflow, or configure [Pulumi Deployments](/docs/deployments/) to run previews on pull requests, deploy commits pushed to a branch, and create review stacks. Pulumi Agents can also work in your Origin repositories and open pull requests for its changes.

## Installation and configuration

{{% notes type="info" %}}
To install the Pulumi app for Cursor Origin, you need workspace admin access in Origin and permission to manage your Pulumi organization's integrations.
{{% /notes %}}

1. [Sign in to your Pulumi account.](https://app.pulumi.com/signin)
1. Navigate to **Settings** > **Version control**.
1. Select **Add account**, choose **Cursor Origin**, and select **Next**.
1. Select **Install in Cursor Origin**.
1. In Origin, choose the namespace that owns your repositories. Grant access to all repositories or select individual repositories, then approve the requested permissions.
1. On the **Link your Cursor Origin installation** page, select the same Pulumi organization you used to start the installation.
1. Select **Link installation**.

The installation now appears under **Settings** > **Version control**. Open it to check that its status is **Connected**.

Each Origin installation can be linked to only one Pulumi organization. Use this integration for repositories hosted on Origin. For repositories mirrored from GitHub, use the [Pulumi GitHub integration](/docs/integrations/version-control/github-app/).

### Install from Origin

To start in Origin instead, open the [Pulumi app for Cursor Origin installation page](https://cursor.com/codebase/apps/install?client_id=app_01m6mm4qvvenxr4kzb73pk0zj2&source=app-metadata&returnTo=/codebase/settings/apps). Choose the namespace and repositories, and approve the permissions. When Origin redirects you to Pulumi Cloud, select the Pulumi organization to link and select **Link installation**.

## Report results from CI or the Pulumi CLI

You can keep running Pulumi through your existing workflow after you install the app. Pulumi posts results for updates run from CI and from a local Pulumi CLI. To post a result, Pulumi needs all of the following:

- The stack is in the Pulumi organization linked to the Origin installation, and uses Pulumi Cloud as its backend.
- The update's metadata identifies the Origin repository and the commit. The Pulumi CLI reads these values from the repository's git remote and current commit.
- The commit matches a push or pull request event that Pulumi received from Origin. If the update records a branch, the branch must also match the event.

## Configure Pulumi Deployments

Configure each stack with an Origin repository and branch. [Pulumi Deployments](/docs/deployments/) runs `pulumi preview` for pull requests that target that branch and `pulumi up` for commits pushed to it, according to the triggers you enable.

You need a stack in Pulumi Cloud, permission to edit its deployment settings, and a verified email address on your Pulumi account.

1. Open the stack and navigate to **Settings** > **Deploy**.
1. Under **Source control**, set **Source type** to **Version control account**. Select your Cursor Origin account, then select the **Repository** that contains your Pulumi program.
1. Select the **Branch** to deploy and enter the **Pulumi.yaml folder**, relative to the repository root.
1. Configure the [deployment environment](/docs/deployments/concepts/settings/) with the cloud credentials and other settings your program needs.
1. Enable **Run previews for pull requests** to preview changes before merging. Enable **Run updates for pushed commits** to apply changes when commits reach the selected branch. You can enable either option or both.
1. Select **Save**.

Repeat these steps for each stack you want to deploy from Origin.

### Review stacks

[Review stacks](/docs/deployments/concepts/review-stacks/) are ephemeral environments that Pulumi Deployments creates for each pull request. When a pull request is opened, Pulumi Deployments creates a stack with your changes and updates it on every new commit. When the pull request is merged or closed, Pulumi Deployments destroys the stack and frees its resources.

To enable review stacks, toggle **Use this stack as a template for pull request stacks** under **Settings** > **Deploy** on the stack you want to use as a template.

### Tag pushes and path filters

To deploy on tag pushes, such as every `v*` release tag, toggle **Run updates for pushed tags** and use [tag triggers](/docs/deployments/concepts/settings/tag-filtering/).

[Path filters](/docs/deployments/concepts/settings/path-filtering/) limit deployments to commits that change matching files, which helps when several programs share a repository. The Pulumi Cloud console shows path filters for GitHub stacks only. For an Origin stack, set them through the [Deployments REST API](/docs/reference/cloud-rest-api/deployments/).

### Environment variables

Pulumi injects the following environment variables during Origin-triggered deployments:

| Variable | Set when | Value |
|---|---|---|
| `PULUMI_CI_BRANCH_NAME` | Push, tag, and pull request events | Branch name, the pull request's head branch, or `refs/tags/<tag>` for a tag |
| `PULUMI_CI_PULL_REQUEST_SHA` | Push, tag, and pull request events | Full commit SHA |
| `PULUMI_PR_NUMBER` | Pull request events | Pull request number |
| `PULUMI_CI_TAG_NAME` | Tag events | Tag name |

Pulumi checks out the repository with a short-lived token and doesn't pass it to your program. If your program runs its own git commands against Origin, give it its own credentials.

## Pulumi Agents

[Pulumi Agents](/docs/ai/) works with the Origin repositories the app can access. It clones them, pushes branches, and opens pull requests for its changes. Select an Origin repository when you start a task, or name one in your request. Pulumi Agents can't create repositories in Origin.

## Integration settings

To change which repositories Pulumi can access, open the installed Pulumi app in [Origin Apps settings](https://cursor.com/codebase/settings/apps) and update its repository selection. Pulumi checks repository access before each deployment, so removing a repository stops deployments from it.

To change what Pulumi posts on pull requests, open the integration under **Settings** > **Version control** in Pulumi Cloud. You can turn **Pull request comments**, **Draft Pull request comments**, and **Detailed diff for pull request comments** on or off. Turning comments off leaves check reporting enabled.

## Remove the integration

In Pulumi Cloud, open the integration under **Settings** > **Version control**. Open **Actions**, choose **Remove integration**, and select the **Remove integration** button. In the confirmation dialog, select **Delete**. This uninstalls the app from Origin and removes the deployment settings of every stack that uses the integration.

You can instead uninstall the app in Origin Apps settings. When Pulumi receives the uninstall event, it removes the connection and the same deployment settings. To resume deployments, reinstall the app, link it to Pulumi, and configure the affected stacks again.

## Limitations

- **New project wizard and templates**: The [New Project Wizard](/docs/idp/concepts/new-project-wizard/) can't create or target Origin repositories, and Origin repositories can't be used as [template sources](/docs/idp/concepts/organization-templates/).
- **GitHub mirrors**: Origin repositories mirrored from GitHub keep their integrations on GitHub. Use the [Pulumi GitHub integration](/docs/integrations/version-control/github-app/) for them.
- **Path filters in the console**: Set path filters for Origin stacks through the REST API. See [Tag pushes and path filters](#tag-pushes-and-path-filters).

## Troubleshooting

### Installation cannot complete

If the page reports that the installation link is invalid or expired, restart the installation from **Settings** > **Version control** or Origin Apps settings. An installation started in Pulumi Cloud must be finished by the same Pulumi user, in the same Pulumi organization. Pulumi shows the same message for an expired link and for a different user or organization.

Check that your Pulumi user can manage the organization's integrations. An Origin installation already linked to another Pulumi organization can't be linked to yours.

### A repository is missing

Open the installed Pulumi app in [Origin Apps settings](https://cursor.com/codebase/settings/apps) and add the repository to its repository selection. In the stack's deployment settings, select the Origin account that owns that repository.

### A preview or update does not start

Open the stack's **Settings** > **Deploy** page and check the operation you expect:

- For a pull request preview, enable **Run previews for pull requests**. The pull request must target the configured branch.
- For an update, enable **Run updates for pushed commits**. The commit must be pushed to the configured branch.

If you configured path filters, the triggering commit must change at least one file that the filters include. Check that the app still has access to the repository in Origin Apps settings. If the integration shows **Suspended**, Pulumi doesn't run deployments or post results until Origin reactivates the installation.

### Checks appear without comments

Open the integration under **Settings** > **Version control** and enable **Pull request comments**. For a draft pull request, also enable **Draft Pull request comments**.

If Origin shows a permissions update for the installed Pulumi app, approve it. Origin grants comment and check permissions separately, so a successful check doesn't mean the app can post a comment.

## Learn more

- [Pulumi Deployments](/docs/deployments/concepts/): the deployment engine this integration triggers.
- [Version control integrations](/docs/integrations/version-control/): Pulumi's integrations with GitHub, GitLab, Bitbucket, Azure DevOps, and other providers.

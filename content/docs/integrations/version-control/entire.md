---
title_tag: "Entire Integration | Version Control"
meta_desc: Connect Entire to Pulumi Cloud to preview infrastructure changes on trails, deploy on push, create review stacks, and report checks and deployments.
title: Entire
h1: Entire
menu:
    integrations:
        name: Entire
        parent: integrations-version-control
        weight: 5
---

Pulumi Cloud integrates with [Entire](https://entire.com) through the Pulumi plugin for Entire. Once you install the plugin and link it to your Pulumi organization, Pulumi runs previews on trails, deploys infrastructure on push, creates ephemeral review stacks, and reports the results to Entire as checks and deployments. Neo can also work in your Entire repositories and open trails for its changes. In Entire, a trail is the equivalent of a pull request.

## Installation and configuration

{{% notes type="info" %}}
To link an Entire installation, you need permission to manage your Pulumi organization's integrations, and permission to install plugins on the Entire organization or project.
{{% /notes %}}

1. [Sign in to your Pulumi account.](https://app.pulumi.com/signin)
1. Navigate to **Settings** > **Version control**.
1. Select **Add account**, choose **Entire**, and select **Install in Entire**.
1. In Entire, choose the organization or project to install the plugin on, select the repositories Pulumi can access, and approve the plugin.
1. Back in Pulumi Cloud, confirm the organization and select **Link installation**.

If you start the installation from Entire instead, Entire sends you to the same page in Pulumi Cloud, where you choose the Pulumi organization to link before you select **Link installation**.

Pulumi receives events from Entire through the plugin, so there are no webhooks to configure. You choose the repositories Pulumi can access when you install the plugin. To change them later, manage the plugin's installation from the project's **Plugins** page in Entire.

### Repository identifiers

When you configure a stack's deployment settings, the repository is the Entire project and repository name, `project/repo`: the part of the repository's path after `et/`. For example, the repository at `entire.com/et/acme/infra` is `acme/infra`.

Entire projects that mirror GitHub repositories are supported. A mirror's path starts with `gh/` instead of `et/`, so the mirror at `entire.com/gh/acme/infra` is also `acme/infra`.

### Several Pulumi organizations

You can link one Entire installation to more than one Pulumi organization. Each organization approves the plugin through the installation flow and receives every event from the installation. The repositories and permissions of the installation are shared, so anyone who can configure deployments in a linked organization can deploy from any repository the installation covers.

## Managing the integration

The integration card under **Settings** > **Version control** shows the Entire organization or project the plugin is installed on, and whether the installation is connected or suspended. While Entire suspends an installation, Pulumi doesn't run deployments for it.

To remove the integration, open it under **Settings** > **Version control** and select **Remove integration**. This disconnects your Pulumi organization from the installation and removes the deployment settings of every stack that uses it. The plugin stays installed in Entire, and Pulumi ignores its events for your organization. To uninstall the plugin, remove it in Entire, which disconnects every Pulumi organization that uses the installation.

## Capabilities

### Checks

Pulumi reports each preview, update, and destroy to Entire as a check on the commit, with a link to the deployment in Pulumi Cloud. Each stack and operation gets its own check.

Entire can block a trail from merging while a check is failing. Merge gates are set per repository under **Settings** > **Gates** in Entire. When the Pulumi plugin's gate lists no required checks, any failing Pulumi check blocks the merge. To block only on some stacks or operations, list those checks under **Required checks**, or turn the gate off.

### Deployments

Pulumi also records updates and destroys as deployments in Entire, so the state of each stack shows in Entire alongside the commit. Review stacks are recorded as preview deployments. Previews appear as checks only.

### Trail previews

When a trail is opened or a new commit is pushed to it, Pulumi runs `pulumi preview` on every stack that previews trails for the trail's base branch, and reports the result as a check. To enable this, toggle **Run previews for trails** under **Stack** > **Settings** > **Deploy**.

A trail can include changes in several repositories or branches. Each change gets its own preview and checks.

Pulumi doesn't post comments on trails. The results appear in the trail's checks and deployments, and in Pulumi Cloud.

### Push-to-deploy

Push-to-deploy runs `pulumi up` when a commit is pushed to a configured branch. Enable it under **Stack** > **Settings** > **Deploy** by toggling **Run updates for pushed commits**. See the [push-to-deploy documentation](/docs/deployments/concepts/triggers/#push-to-deploy) for setup instructions.

You can use path filters to limit deployments to commits that change files matching specific glob patterns (for example, `infrastructure/**`). You can also deploy on tag pushes, such as every `v*` release tag, by toggling **Run updates for pushed tags** and using [tag triggers](/docs/deployments/concepts/settings/tag-filtering/).

### Review stacks

[Review stacks](/docs/deployments/concepts/review-stacks/) are ephemeral environments that Pulumi Deployments creates for each change on a trail. When a trail is opened, Pulumi Deployments creates a stack with your changes and updates it on every new commit. When the change is merged or the trail is closed, Pulumi Deployments destroys the stack and frees its resources.

To enable review stacks, toggle **Use this stack as a template for trail stacks** under **Stack** > **Settings** > **Deploy** on the stack you want to use as a template.

### Environment variables

Pulumi injects the following environment variables during Entire-triggered deployments:

| Variable | Set when | Value |
|---|---|---|
| `PULUMI_CI_BRANCH_NAME` | Push, tag, and trail events | Branch name, or `refs/tags/<tag>` for a tag |
| `PULUMI_CI_PULL_REQUEST_SHA` | Push, tag, and trail events | Full commit SHA |
| `PULUMI_PR_NUMBER` | Trail events | Trail number |
| `PULUMI_CI_TAG_NAME` | Tag events | Tag name |

### Credentials

When a deployment starts, Pulumi requests a short-lived token from Entire to check out the repository. The token is read-only and limited to the repository being deployed. [Neo](#neo) uses a token with the installation's permissions instead, so it can push branches, open trails, and create repositories.

### Pulumi Delivery

[Pulumi Delivery](/docs/delivery/) pipelines can use Entire repositories as sources with `EntireSource`, start runs on pushes to them, and run pipeline programs stored in Entire. See [Sources and triggers](/docs/delivery/concepts/sources-and-triggers/).

### Neo

[Neo](/docs/ai/) works with the Entire repositories the plugin can access. It clones them, pushes branches, opens trails for its changes, and creates new repositories. Select an Entire repository when you start a task, or name one in your request.

Neo creates repositories in the Entire project the plugin is installed on, so creating repositories requires an installation on a project.

## Limitations

- **Trail comments**: Pulumi reports results as checks and deployments, not as trail comments.
- **New project wizard and templates**: The [New Project Wizard](/docs/idp/concepts/new-project-wizard/) can't create or target Entire repositories, and Entire repositories can't be used as [template sources](/docs/idp/concepts/organization-templates/).
- **Renamed repositories**: Deployment settings store the repository's name, so renaming a repository in Entire stops its deployments until you update the stack's deployment settings.

## Troubleshooting

### Deployments not triggering

If deployments aren't triggering on push or trail events:

1. Verify that the integration shows as connected under **Settings** > **Version control**. Pulumi doesn't run deployments while the installation is suspended in Entire.
1. Check that the repository is one the plugin can access in Entire.
1. Verify the deployment settings under **Stack** > **Settings** > **Deploy**, and that the branch matches the branch you pushed to, or the trail's base branch.
1. If you use path filters, confirm that the changed files match your glob patterns.

### Trail is blocked from merging

A failing Pulumi check blocks the trail when the repository's gate for the Pulumi plugin is on. Open the check's link to see the failed deployment in Pulumi Cloud, or change the gate under the repository's **Settings** > **Gates** in Entire.

### Deployments don't appear in Entire

Pulumi records only updates, destroys, and review stacks as deployments in Entire. Previews appear as checks only. If an update or destroy shows in Pulumi Cloud but not in Entire, check that the integration is connected under **Settings** > **Version control**.

### Neo can't push to an Entire repository

If Neo reports that a push failed with `Token does not permit this request`, the installation hasn't granted Pulumi write access. Accept the Pulumi plugin's updated permissions in Entire, then ask Neo to retry.

## Learn more

- [Pulumi Deployments](/docs/deployments/concepts/): the deployment engine this integration triggers.
- [Version control integrations](/docs/integrations/version-control/): Pulumi's integrations with GitHub, GitLab, Bitbucket, Azure DevOps, and other providers.

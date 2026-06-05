---
title_tag: "Pulumi GitHub App | Version Control"
meta_desc: Pulumi's GitHub app integrates the results of Pulumi stack updates. It
           will show you any potential infrastructure changes on pull requests and commit checks.
title: Pulumi GitHub App
h1: Pulumi GitHub App
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    integrations:
        name: GitHub
        parent: integrations-version-control
        weight: 1
aliases:
- /docs/version-control/github-app/
- /docs/integrations/github-app/
- /docs/iac/integrations/github-app/
- /docs/iac/guides/continuous-delivery/github-app/
- /docs/iac/using-pulumi/continuous-delivery/github-app/
- /docs/reference/cd-github/
- /docs/console/continuous-delivery/github-app/
- /docs/guides/continuous-delivery/github-app/
- /docs/using-pulumi/continuous-delivery/github-app/
- /docs/iac/packages-and-automation/continuous-delivery/github-app/
---

Pulumi's GitHub app displays the results of Pulumi stack update previews in pull requests and enables automatic stack deployments via [Pulumi Deployments](/docs/deployments/deployments/). Once installed and configured, it will show any potential infrastructure changes on pull requests and commit checks. You can also configure workflows to update your stacks whenever a commit is pushed to a configured branch.

{{% notes type="info" %}}
The GitHub app requires [Pulumi Cloud](https://app.pulumi.com) as your stack's backend. It does not work with [self-managed backends](/docs/concepts/state/#using-a-diy-backend).
{{% /notes %}}

## Installation and configuration

{{% notes type="info" %}}
To install the GitHub app, you must have admin permissions in **both** the target GitHub organization and the Pulumi organization. This is required to establish the correct connection between the two platforms.
{{% /notes %}}

1. [Sign in to your Pulumi account.](https://app.pulumi.com/signin)
1. Select the Pulumi organization you wish to use from the Organization drop-down.
1. Navigate to **Management** > **Version control**.
1. Select **Add account** and choose **GitHub**, then follow the prompts.

### Multiple GitHub organizations

Multiple GitHub organizations can be connected to a single Pulumi organization. You can add each one via **Management** > **Version control** > **Add account**.

{{% notes type="info" %}}
Mapping a single GitHub organization to multiple Pulumi organizations requires contacting [Pulumi support](https://www.pulumi.com/support/). This option is only available for Enterprise and Business Critical customers.
{{% /notes %}}

### GitHub Enterprise Server support

GitHub Enterprise Server is supported for [Pulumi Business Critical Edition](https://www.pulumi.com/enterprise/). Only one GitHub Enterprise Server integration is supported per Pulumi organization.

### Individual user setup

Separately from the org-level GitHub app, individual users can complete an OAuth flow under **Management** > **Version control** to grant Pulumi access to their personal GitHub account. The integration card shows your status: "Individual access is authorized for this account" once you've connected, or "Individual access is recommended for this account" with an **Add Individual Account** button if you haven't.

Individual access lets Pulumi create repositories on your behalf — for example, cloning project templates into a new repository or letting [Neo](/docs/ai/) create a repository for you. It does not create webhooks. The org-level GitHub app continues to handle pull request comments, checks, and push-to-deploy regardless of whether you grant individual access. This option is not available for GitHub Enterprise Server.

{{% notes type="info" %}}
To remove your individual identity, select your identity on the integration card and choose **Remove Identity**.
{{% /notes %}}

## Integration settings

After installing the app, you can configure pull request behavior. Toggle these settings per integration under **Management** > **Version control**:

| Setting | Default | Description |
|---|---|---|
| Pull request comments | Enabled | Post deployment status and resource changes as comments on GitHub pull requests |
| Neo Code Reviews | Enabled | Include Neo's AI-generated review of infrastructure changes in pull request comments (requires [Pulumi Neo](/docs/ai/get-started/#enabling-and-disabling-neo) to be enabled for your organization) |
| Code access for AI reviews | Enabled | Let Neo read pull request code diffs when generating reviews instead of relying on Pulumi engine output alone |
| Detailed diff for pull request comments | Enabled | Show property-level before/after diffs for changed resources in pull request comments |

Changes save automatically. Neo Code Reviews and detailed diff require pull request comments to be enabled, and code access for AI reviews requires Neo Code Reviews. Code access for AI reviews is specific to the GitHub app and appears once the capability is enabled for your organization.

To remove an integration, see [Uninstallation](#uninstallation).

## Capabilities

### Pull request comments

The Pulumi GitHub app automatically adds comments to pull requests with the results of any stack changes. This includes a summary of how many resources were created, updated, and/or deleted. This allows you to quickly see the changes caused by your Pulumi program without needing to leave GitHub's pull request view, with a link to the richer details available on [Pulumi Cloud](https://app.pulumi.com/signin).

When you run `pulumi preview` or `pulumi up`, the Pulumi CLI examines the closest `.git` directory to extract commit metadata (such as the commit SHA, branch name, and repository information). This metadata is included with the update and sent to Pulumi Cloud, which uses it to identify the associated pull request and post comments.

{{% notes type="info" %}}
When you disable pull request comments in your [integration settings](#integration-settings), the GitHub app does not post comments on pull requests. However, it still reports check run statuses via [GitHub's Checks API](#checks), so preview results remain accessible in the pull request's **Checks** tab.
{{% /notes %}}

### Checks

Beyond pull request comments, the GitHub app also integrates with GitHub's [Checks API](https://blog.github.com/2018-05-07-introducing-checks-api/). This provides even more detail about any resource changes, including the full update log.

All Pulumi stack updates are reported to the GitHub Checks API. You can see the results of each commit check by going to the **Code** tab's **Commits** page, and then clicking the ✅ or ❌ icon. For pull requests, you can see the checks on the **Checks** tab as well.

### Push-to-deploy

Push-to-deploy automatically runs `pulumi up` when a commit is pushed to a configured branch, most commonly the main branch. See the [push-to-deploy documentation](/docs/deployments/deployments/using/triggers/#push-to-deploy) for setup instructions.

You can also deploy on git tag pushes — for example, on every `v*` release tag — using [tag triggers](/docs/deployments/deployments/using/settings/#tag-filtering).

### Review stacks

[Review stacks](/docs/deployments/deployments/review-stacks/) are dedicated cloud environments that get created automatically every time a pull request is opened, powered by Pulumi Deployments. Open a pull request, and Pulumi Deployments will stand up a stack with your changes and add a PR comment with the outputs from your deployment. Merge the PR and Pulumi Deployments will destroy the stack and free up the associated resources.

## CI integration

The GitHub app only requires that your code is hosted on GitHub and that you use pull requests to manage changes. It does not require GitHub Actions — any CI/CD system works, including GitHub Actions, CircleCI, Jenkins, Pulumi Deployments, or any other system.

Once installed in your organization, any `pulumi preview` or `pulumi up` run in CI will have its results reported back to GitHub. See [Continuous delivery](/docs/iac/operations/continuous-delivery/) for integration instructions, or the [GitHub Actions guide](/docs/iac/operations/continuous-delivery/github-actions/) if you run Pulumi in GitHub Actions.

## Uninstallation

The GitHub app can be uninstalled using either of the following methods:

- **From Pulumi Cloud**: Navigate to **Management** > **Version control**, select your GitHub organization, and select **Uninstall**. This automatically removes the app from GitHub as well.
- **From GitHub**: Follow [GitHub's instructions for reviewing and modifying installed GitHub Apps](https://docs.github.com/en/apps/using-github-apps/reviewing-and-modifying-installed-github-apps#navigating-to-the-github-app-you-want-to-review-or-modify).

{{% notes type="warning" %}}
Uninstalling the GitHub app will delete any push-to-deploy and review stack configurations you have set up.
{{% /notes %}}

## Troubleshooting

### App not appearing as installed

If you previously installed the GitHub app but Pulumi Cloud does not show it as connected to your desired organization, try the following:

1. Ensure you're a GitHub admin of the GitHub organization where you're installing the app.
1. Uninstall the app and re-install it following the steps above. See [Uninstallation](#uninstallation) for both methods.

### PR comments not appearing

If comments aren't appearing on your pull requests, verify that:

1. The `.git` folder is present in your Pulumi project directory during CI runs.
1. If you copy your Pulumi code into a container, you also include the `.git` folder.
1. The commit being built matches a commit in an open pull request.
1. The GitHub app has access to the repository — navigate to **Management** > **Version control**, select your GitHub organization, and check the **Repositories** tab. If the repository is not listed, select **Configure repository access** to update the app's permissions in GitHub.

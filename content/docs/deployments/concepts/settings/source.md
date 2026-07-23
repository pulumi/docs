---
title_tag: "Source Settings | Pulumi Deployments"
meta_desc: Configure where a Pulumi Deployment gets the program it runs, including version control integrations, Git URLs, and templates
title: "Source Settings"
h1: "Source Settings"
menu:
  deployments:
    name: Source Settings
    parent: deployments-concepts-settings
    identifier: deployments-concepts-settings-source
    weight: 10
---

The **Source** determines where a deployment gets the Pulumi program it runs. In the Pulumi Cloud console, open **Settings > Deploy** for the stack and choose a source. The dropdown lists the [version control integrations](/docs/integrations/version-control/) connected to your organization — for example **GitHub**, **GitLab**, **Bitbucket**, or **Azure DevOps** — along with **Git**, **No code**, and **None**. Only integrations that are installed appear, so the exact set of options depends on your organization.

## Version control integrations

Select a connected integration to deploy from a repository it manages. Every integration exposes the same source fields, though the repository identifier format varies by provider:

- **Repository** (required): the repository to deploy from. The format depends on the provider — for example `owner/repo` for GitHub, `group/project` for GitLab, `workspace/repo` for Bitbucket, and `organization/project/repository` for Azure DevOps.
- **Branch** (required): the branch to deploy.
- **Pulumi.yaml folder**: the path, relative to the repository root, to the directory that contains your `Pulumi.yaml`. Leave it blank when the project lives at the repository root.

A set of toggles controls which repository events trigger a deployment. (GitLab labels these in terms of "merge requests" where other providers say "pull requests"; the behavior is the same.)

- **Run previews for pull requests**: run a `pulumi preview` when a pull request is opened against the configured branch, and post the result as a comment on the request.
- **Run updates for pushed commits**: run a `pulumi up` when commits are pushed or merged to the configured branch.
- **Run updates for pushed tags**: run a `pulumi up` when a matching git tag is pushed. See [Tag Filtering](/docs/deployments/concepts/settings/tag-filtering/).
- **Use this stack as a template for pull request stacks**: use this stack as the template for the [review stacks](/docs/deployments/concepts/review-stacks/) created on each pull request.

These toggles depend on the version control integration, which also clones your repository and posts status comments. Custom VCS supports push-to-deploy only (no request previews or review stacks). In code, the toggles correspond to the provider object (`repository`, `deployCommits`, `previewPullRequests`, `pullRequestTemplate`) and `sourceContext.git` (`branch`, `repoDir`) on the [`pulumiservice.DeploymentSettings`](/registry/packages/pulumiservice/api-docs/deploymentsettings/) resource. See [Review stacks](/docs/deployments/concepts/review-stacks/) for complete examples.

## Git

Use the Git source to deploy from any Git repository by URL — for example a self-managed Git server, or a provider you have not connected as an integration. Provide the repository URL, a branch, and an optional `Pulumi.yaml` folder, along with the credentials a private repository requires (typically an access token or SSH key managed with [Pulumi ESC](/docs/esc/)).

The Git source only clones and deploys your program. To also get pull or merge request previews, push-to-deploy, and status comments, connect the matching [version control integration](/docs/integrations/version-control/) and select it as the source instead.

## No code

The **No code** source lets you base a stack's deployment on a [Pulumi template](/docs/idp/concepts/organization-templates/) instead of a connected repository — for example, when a stack is created from an organization template.

## None

Select **None** when the deployment has no source to fetch — typically because the Pulumi program is already present in a [custom executor image](/docs/deployments/concepts/settings/custom-executor-images/).

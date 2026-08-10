---
title_tag: "Azure DevOps Integration | Version Control"
meta_desc: Connect Azure DevOps repositories to Pulumi Cloud for pull request previews, push-to-deploy, review stacks, commit statuses, and automated deployments.
title: "Azure DevOps Integration"
h1: "Azure DevOps Integration"
menu:
    integrations:
        name: Azure DevOps
        parent: integrations-version-control
        weight: 4
aliases:
- /docs/version-control/azure-devops-integration/
- /docs/integrations/azure-devops-integration/
- /docs/deployments/deployments/azure-devops/
- /docs/iac/guides/continuous-delivery/azure-devops-integration/
---

Pulumi Cloud integrates with Azure DevOps to post pull request previews, deploy infrastructure on push, create ephemeral review stacks, and report commit statuses — the same capabilities available with [GitHub](/docs/integrations/version-control/github-app/), [GitLab](/docs/integrations/version-control/gitlab/), and [Bitbucket](/docs/integrations/version-control/bitbucket/). Once configured, Pulumi registers service hooks in your Azure DevOps project and manages authentication for you.

With the integration in place you can:

- **Preview pull requests.** Run `pulumi preview` when a pull request is opened or updated and post the resource changes back as a pull request comment, so reviewers see the infrastructure impact without leaving Azure DevOps. See [pull request comments](#pull-request-comments).
- **Deploy on push.** Run `pulumi up` automatically when commits land on a configured branch, or when a matching git tag is pushed. See [push-to-deploy](#push-to-deploy).
- **Report pass/fail on the commit.** Post the deployment's outcome as an Azure DevOps commit status — the green check or red X that appears on the pull request — so the result is visible without opening the comment. See [commit status checks](#commit-status-checks).
- **Stand up review stacks.** Create a real, ephemeral environment per pull request and tear it down on merge or close. See [review stacks](#review-stacks).
- **Create new projects from the developer portal.** Use the [New Project Wizard](/docs/idp/concepts/new-project-wizard/) to scaffold Pulumi projects and stacks into Azure DevOps repositories, and register Azure DevOps repositories as [template sources](#template-sources).

## Installation and configuration

{{% notes type="info" %}}
To set up the Azure DevOps integration you must be an org admin in Pulumi Cloud, and you need an Azure DevOps organization and project plus a Microsoft Entra ID (Azure AD) tenant.
{{% /notes %}}

1. [Sign in to your Pulumi account.](https://app.pulumi.com/signin)
1. Navigate to **Management** > **Version control**.
1. Select **Authorize Azure DevOps** and complete the Microsoft Entra ID sign-in.
1. Select the Azure DevOps organization and project you want to integrate with, then configure your [integration settings](#integration-settings).

Pulumi registers service hooks in your Azure DevOps project for the `git.push`, `git.pullrequest.created`, `git.pullrequest.updated`, and `git.pullrequest.merged` events. No manual webhook or pipeline configuration is required.

Each integration maps one Pulumi organization to one Azure DevOps organization and project pair. Create additional integrations if you use multiple Azure DevOps projects.

### Authentication

Authorization is a single Microsoft Entra ID flow that grants Pulumi two sets of scopes:

- **Microsoft Graph**: lets Pulumi discover your Entra tenant and manage the application registration it uses for this integration.
- **Azure DevOps**: grants access to repositories, projects, and service hooks.

{{% notes type="info" %}}
The Microsoft Graph consent requires the `Application.ReadWrite.All` permission. This is an admin-consented permission, so if your tenant restricts user consent, an Entra ID administrator must approve it before the integration can be created.
{{% /notes %}}

Once the integration exists, Pulumi authenticates to Azure DevOps for deployments using Microsoft Entra ID **federated credentials** rather than a stored access token, so no long-lived secret is kept. This is configured automatically when you connect the integration — there is nothing to set up, and no issuer, subject, or audience for you to supply.

#### What Pulumi creates in your tenant and project

Each integration provisions its own identity, scoped to the single Azure DevOps project it connects. In Microsoft Entra ID, Pulumi creates:

- An **application registration named `Pulumi`**, registered as single tenant (accounts in your directory only). Its description and notes record the Azure DevOps organization, project, and integration ID, so tenants with several integrations can tell the registrations apart.
- A **service principal** for that application, added to your Azure DevOps organization with the Basic access level.
- A **federated identity credential** on the application. No client secret or certificate is created.

In the connected Azure DevOps project, Pulumi creates a group named **Pulumi Service (`<your-pulumi-org>`)** that holds the service principal and carries only the permissions the integration needs:

| Area | Permissions |
|---|---|
| Service hooks | View, edit, and delete subscriptions |
| Git repositories | Read, contribute, create branch, create repository, contribute to pull requests |
| Project | View project-level information and test results |

During setup the service principal is temporarily added to **Project Administrators** so it can create that group and assign its permissions, then removed from Project Administrators once the scoped group is in place.

Deleting the integration removes the service hooks, the service principal and its group, and the Entra ID application registration.

### Individual user setup

Separately from the org-level integration, individual users can complete an OAuth flow under **Management** > **Version control** to grant Pulumi access to their Azure DevOps account.

Individual access lets Pulumi create repositories on your behalf — for example, cloning project templates into a new repository or letting [Neo](/docs/ai/) create a repository for you. It does not create service hooks. The org-level integration continues to handle pull request comments and deployments regardless of whether you grant individual access.

The integration card shows your status: "Individual access is authorized for this account" once you've connected, or "Individual access is recommended for this account" with an **Add Individual Account** button if you haven't.

{{% notes type="info" %}}
To remove your individual identity, select your identity on the integration card and choose **Remove Identity**. To disconnect the account entirely, delete all Azure DevOps integrations first, then select **Disconnect** from the identity dropdown.
{{% /notes %}}

## Integration settings

After creating an integration, you can configure pull request behavior. Toggle these settings per integration:

| Setting | Default | Description |
|---|---|---|
| Pull request comments | Enabled | Post deployment status and resource changes as comments on Azure DevOps pull requests |
| Detailed diff for pull request comments | Enabled | Show property-level before/after diffs for changed resources in pull request comments |

Detailed diff requires pull request comments to be enabled.

To delete an integration, select **Delete Integration** on the integration card. This removes the service hooks from Azure DevOps and disconnects all stacks using that integration.

## Capabilities

### Pull request comments

Pulumi automatically posts comments on pull requests with the results of any stack changes. This includes a summary of how many resources were created, updated, or deleted, with a link to the full details in [Pulumi Cloud](https://app.pulumi.com/signin). When enabled, comments also include a collapsible detailed diff.

For [review stacks](#review-stacks), comments show the review stack status and outputs instead of a standard preview summary.

Draft pull requests do not trigger deployments, so no preview runs and no comment is posted until the pull request is published. Azure DevOps is the exception here: [GitLab](/docs/integrations/version-control/gitlab/) and [Bitbucket](/docs/integrations/version-control/bitbucket/) treat drafts like any other request, and [GitHub](/docs/integrations/version-control/github-app/) makes draft comments a setting you can turn off.

These comments come from Pulumi Deployments. [Neo code reviews](/docs/ai/neo/code-reviews/), which analyze a pull request and leave inline feedback, are available on GitHub only — Neo does not comment on Azure DevOps pull requests.

### Commit status checks

A commit status is the pass/fail marker Azure DevOps attaches to a commit and displays on the pull request. Pulumi posts one for each pull request deployment, so reviewers can see whether the preview succeeded without reading the comment, and you can require it to pass by adding a status check [branch policy](https://learn.microsoft.com/en-us/azure/devops/repos/git/pr-status-policy) in Azure DevOps.

Statuses are posted under the genre `pulumi` and named after the project, stack, and operation — for example `my-project/dev - preview deployment`. Each one links back to the full deployment in Pulumi Cloud.

Azure DevOps commit statuses are additive: posting a new status with the same genre and name supersedes the previous one, so the latest result is what appears on the commit.

Push-to-deploy runs do not post a commit status. Statuses are tied to a pull request's head commit, so they're only produced by pull request deployments.

### Push-to-deploy

Push-to-deploy automatically runs `pulumi up` when a commit is pushed to a configured branch, most commonly the default branch. Enable this under **Stack** > **Settings** > **Deploy** by toggling **Deploy on push**. See the [push-to-deploy documentation](/docs/deployments/concepts/triggers/#push-to-deploy) for setup instructions.

You can use path filters to limit deployments to commits that change files matching specific glob patterns (e.g., `infra/**`).

You can also deploy on git tag pushes — for example, on every `v*` release tag — using [tag triggers](/docs/deployments/concepts/settings/tag-filtering/). Azure DevOps delivers tag pushes on the same `git.push` service hook as branch pushes, so no additional configuration is needed. Tag deletions do not trigger deployments.

#### Selecting a repository and branch

Configure the source under **Stack** > **Settings** > **Deploy**:

1. Choose the Azure DevOps integration (if multiple are configured).
1. Select a repository from the autocomplete dropdown. Azure DevOps repositories are identified as `organization/project/repository`.
1. Select the target branch.

See [Deployment settings: source](/docs/deployments/concepts/settings/source/) for the full set of source options and event toggles.

### Review stacks

[Review stacks](/docs/deployments/concepts/review-stacks/) are ephemeral cloud environments created automatically every time a pull request is opened, powered by Pulumi Deployments. Open a pull request, and Pulumi Deployments stands up a stack with your changes and posts a pull request comment with the outputs. Merge or abandon the pull request, and Pulumi Deployments destroys the stack and frees the associated resources.

Review stacks follow the naming convention `pr-{organization}-{repository}-{pullRequestId}` — for example, Azure DevOps organization `acme` with repository `infra` and pull request #42 produces stack `pr-acme-infra-42`. Stacks are automatically deleted after the destroy completes.

To enable review stacks, toggle **Pull request template** under **Stack** > **Settings** > **Deploy** on the stack you want to use as a template.

### Environment variables

Pulumi injects the following environment variables during Azure DevOps-triggered deployments:

| Variable | Set when | Value |
|---|---|---|
| `PULUMI_PR_NUMBER` | Pull request events | Pull request ID (number) |
| `PULUMI_CI_PULL_REQUEST_SHA` | Pull request events | Full commit SHA of the source branch |
| `PULUMI_CI_BRANCH_NAME` | Pull request and tag push events | Source branch name, or `refs/tags/<tag>` for a tag push |
| `PULUMI_CI_TAG_NAME` | Tag push events | The pushed tag |

On a tag push, `PULUMI_CI_BRANCH_NAME` carries `refs/tags/<tag>` rather than a branch name. This is intentional: the deployment runner clones by commit SHA, leaving a detached `HEAD` that the Pulumi engine can't read a ref from, so it falls back to `PULUMI_CI_BRANCH_NAME` and records that value as the update's `git.headName`. Use `PULUMI_CI_TAG_NAME` when you need the tag on its own.

Pulumi also injects an `AZURE_DEV_OPS_TOKEN` environment variable that your Pulumi program and [pre-run commands](/docs/deployments/concepts/settings/pre-run-commands/) can use to authenticate to Azure DevOps — for example, to install a private package or clone another repository. To supply your own value instead, set it through [custom environment variables](/docs/deployments/concepts/settings/environment-variables/); an explicit value always overrides the one Pulumi provides.

## New project wizard

The [New Project Wizard](/docs/idp/concepts/new-project-wizard/) supports Azure DevOps as a VCS provider. When the integration is configured and you have authorized your account, you can:

- Create new Azure DevOps repositories in your integrated project
- Select an existing Azure DevOps repository and branch
- Choose any deployment method: CLI, Pulumi Deployments (no-code), or Pulumi Deployments (VCS-backed)

Select **Azure DevOps** as the VCS provider during project setup. If only one provider is configured, it's selected automatically. When using the VCS-backed deployment method, the wizard turns on deploy-on-push and pull request previews for you. [Review stacks](#review-stacks) stay off — enable them afterward on the stack you want to use as a template.

## Template sources

Use Azure DevOps repositories as template sources for [Pulumi IDP](/docs/idp/concepts/organization-templates/). Pulumi scans registered repositories for subdirectories containing a `Pulumi.yaml` file, and each subdirectory becomes a selectable template. Private repositories are authenticated automatically via the integration.

Register a repository using its web URL, in the form:

```
https://dev.azure.com/<organization>/<project>/_git/<repository>
```

## CI integration

The Pulumi Azure DevOps integration posts results back to Azure DevOps regardless of which CI/CD system triggers the run. You can also run Pulumi commands directly in Azure Pipelines. See the [Azure DevOps guide](/docs/iac/operations/continuous-delivery/azure-devops/) for setup instructions and example pipeline configurations.

## Troubleshooting

### Pull request comments not appearing

If comments aren't appearing on your pull requests, verify that:

1. In the [Pulumi Cloud console](https://app.pulumi.com), the Azure DevOps integration is connected and shows a valid status under **Management** > **Version control**.
1. Pull request comments are enabled in your [integration settings](#integration-settings).
1. In Azure DevOps, the service hooks exist. Navigate to **Project Settings** > **Service hooks** and look for the Pulumi subscriptions.
1. In the Pulumi Cloud console, the stack is associated with the correct Azure DevOps repository and branch.
1. The pull request is not a draft — draft pull requests do not trigger deployments.

### Integration shows as disconnected

If the integration card shows an invalid or disconnected status, [delete the integration](#integration-settings) and re-create it by following the [installation steps](#installation-and-configuration). Confirm the service hooks were registered successfully in Azure DevOps afterward.

### Deployments not triggering

If deployments aren't triggering on push or pull request events:

1. Verify deployment settings are enabled under **Stack** > **Settings** > **Deploy**.
1. Check that the branch matches your configured deployment branch.
1. If using path filters, confirm that the changed files match your glob patterns.
1. Verify the service hooks exist under **Project Settings** > **Service hooks** in Azure DevOps.

### Authorization errors

| Issue | Resolution |
|---|---|
| "Azure DevOps not enabled for tenant" (AADSTS650052) | An Entra ID administrator must enable Azure DevOps access for your tenant |
| Consent error mentioning `Application.ReadWrite.All` | An Entra ID administrator must grant consent for the Microsoft Graph permission on the Pulumi application |
| "Remove all integrations before disconnecting" | Delete all Azure DevOps integrations before disconnecting your Azure DevOps identity |

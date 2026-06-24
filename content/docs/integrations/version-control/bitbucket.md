---
title_tag: "Bitbucket Integration | Version Control"
meta_desc: Connect Bitbucket Cloud workspaces to Pulumi Cloud for pull request previews, push-to-deploy, review stacks, commit statuses, and automated deployments.
title: Bitbucket
h1: Bitbucket
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    integrations:
        name: Bitbucket
        parent: integrations-version-control
        weight: 3
aliases:
- /docs/version-control/bitbucket/
- /docs/integrations/bitbucket/
---

Pulumi Cloud integrates with Bitbucket Cloud to post pull request previews, deploy infrastructure on push, create ephemeral review stacks, and report commit statuses — the same capabilities available with [GitHub](/docs/integrations/version-control/github-app/), [GitLab](/docs/integrations/version-control/gitlab/), and [Azure DevOps](/docs/integrations/version-control/azure-devops-integration/). Once configured, Pulumi automatically registers a webhook on each Bitbucket repository you wire up for deployments and manages authentication for you.

## Installation and configuration

{{% notes type="info" %}}
To set up the Bitbucket integration, you must be an org admin in Pulumi Cloud and have appropriate permissions in your Bitbucket workspace.
{{% /notes %}}

1. [Sign in to your Pulumi account.](https://app.pulumi.com/signin)
1. Navigate to **Management** > **Version control**.
1. Select **Add account** and choose **Bitbucket**, then follow the prompts to authorize with Bitbucket.
1. Select the Bitbucket workspace you want to integrate with and configure your [integration settings](#integration-settings).

Pulumi automatically registers a webhook on each Bitbucket repository the first time you save deployment settings on a stack that targets that repository. No manual webhook configuration is required.

### Authentication methods

Pulumi supports two authentication methods depending on your Bitbucket plan:

- **Personal OAuth** (all workspaces including Free): Uses the logged-in user's Bitbucket OAuth token. The user must have appropriate permissions in the target workspace. This is the default option for free Bitbucket workspaces.
- **Workspace Token** (Premium workspaces): An admin generates a workspace access token in Bitbucket and pastes it into Pulumi Cloud. The token requires the following scopes:

    | Scope | Purpose |
    |---|---|
    | `repository:admin` | Create new repositories from project templates |
    | `repository:write` | Push template code into repositories |
    | `pullrequest:write` | Post pull request comments |
    | `webhook` | Register webhooks for deployment triggers |

If your workspace does not support workspace access tokens, Pulumi Cloud prompts you to use personal OAuth for organization authentication instead.

### Individual user setup

Separately from the org-level integration, individual users can complete an OAuth flow under **Management** > **Version control** to grant Pulumi access to their Bitbucket account. The integration card shows your status: "Individual access is authorized for this account" once you've connected, or "Individual access is recommended for this account" with an **Add Individual Account** button if you haven't.

Individual access lets Pulumi create repositories on your behalf — for example, cloning project templates into a new repository or letting [Neo](/docs/ai/) create a repository for you. It does not create webhooks. The org-level integration continues to handle pull request comments and deployments regardless of whether you grant individual access.

{{% notes type="info" %}}
To remove your individual identity, select your identity on the integration card and choose **Remove Identity**.
{{% /notes %}}

## Integration settings

After creating an integration, you can configure pull request behavior. Toggle these settings per integration:

| Setting | Default | Description |
|---|---|---|
| Pull request comments | Enabled | Post deployment status and resource changes as comments on Bitbucket pull requests |
| Neo Code Reviews | Enabled | Include Neo's AI-generated review of infrastructure changes in pull request comments (requires [Pulumi Neo](/docs/ai/get-started/#enabling-and-disabling-neo) to be enabled for your organization) |
| Detailed diff for pull request comments | Enabled | Show property-level before/after diffs for changed resources in pull request comments |

To delete an integration, select **Delete Integration** on the integration card. This removes the webhooks Pulumi created on your Bitbucket repositories and disconnects all stacks using that integration.

## Capabilities

### Pull request comments

Pulumi automatically posts comments on pull requests with the results of any stack changes. This includes a summary of how many resources were created, updated, or deleted, with a link to the full details in [Pulumi Cloud](https://app.pulumi.com/signin). When enabled, comments also include a collapsible detailed diff and an AI-generated explanation from Neo.

Comments are idempotent: updates to the same stack edit the existing comment rather than creating a new one. Draft pull requests are treated identically to regular pull requests.

For [review stacks](#review-stacks), comments show the review stack status and outputs instead of a standard preview summary.

### Commit status checks

Pulumi posts commit status checks to Bitbucket on every deployment, for both push and pull request events. Statuses include a link back to the deployment in Pulumi Cloud.

### Push-to-deploy

Push-to-deploy automatically runs `pulumi up` when a commit is pushed to a configured branch, most commonly the default branch. Enable this under **Stack** > **Settings** > **Deploy** by toggling **Deploy on push**. See the [push-to-deploy documentation](/docs/deployments/concepts/triggers/#push-to-deploy) for setup instructions.

You can use path filters to limit deployments to commits that change files matching specific glob patterns (e.g., `infrastructure/**`).

You can also deploy on git tag pushes — for example, on every `v*` release tag — using [tag triggers](/docs/deployments/concepts/settings/#tag-filtering).

### Review stacks

[Review stacks](/docs/deployments/concepts/review-stacks/) are ephemeral cloud environments created automatically every time a pull request is opened, powered by Pulumi Deployments. Open a pull request, and Pulumi Deployments stands up a stack with your changes and posts a pull request comment with the outputs. Merge or close the pull request, and Pulumi Deployments destroys the stack and frees the associated resources.

To enable review stacks, toggle **Pull request template** under **Stack** > **Settings** > **Deploy** on the stack you want to use as a template.

### Environment variables

Pulumi injects the following environment variables during Bitbucket-triggered deployments:

| Variable | Set when | Value |
|---|---|---|
| `PULUMI_CI_BRANCH_NAME` | Push and pull request events | Branch name |
| `PULUMI_PR_NUMBER` | Pull request events | Pull request ID (number) |
| `PULUMI_CI_PULL_REQUEST_SHA` | Pull request events | Full commit SHA |

## New project wizard

The [New Project Wizard](/docs/idp/concepts/new-project-wizard/) supports Bitbucket as a VCS provider. When the Bitbucket integration is configured, you can:

- Create new Bitbucket repositories in your integrated workspace
- Select an existing Bitbucket repository and branch
- Choose any deployment method: CLI, Pulumi Deployments (no-code), or Pulumi Deployments (VCS-backed)

When using the VCS-backed deployment method, the wizard configures deploy-on-push, pull request previews, and review stacks automatically.

{{% notes type="info" %}}
Bitbucket repositories cannot be used as [template sources](/docs/idp/concepts/organization-templates/) at this time. You can still use templates from other configured VCS providers (such as [GitHub](/docs/integrations/version-control/github-app/) or [GitLab](/docs/integrations/version-control/gitlab/)) or from the [Pulumi private registry](/docs/idp/concepts/organization-templates/#registry-backed-templates).
{{% /notes %}}

## CI integration

The Pulumi Bitbucket integration posts results back to Bitbucket regardless of which CI/CD system triggers the run. You can also run Pulumi commands directly in Bitbucket Pipelines. See the [Bitbucket Pipelines guide](/docs/iac/operations/continuous-delivery/bitbucket/) for setup instructions and example pipeline configurations.

## OIDC authentication

Use Bitbucket Pipelines' built-in OIDC tokens to authenticate with Pulumi Cloud without storing long-lived credentials as pipeline variables. See [Configuring OpenID Connect for Pulumi](/docs/administration/access-identity/oidc-issuers/) for configuration details.

## Troubleshooting

### Pull request comments not appearing

If comments aren't appearing on your pull requests, verify that:

1. The Bitbucket integration is connected and shows a valid status under **Management** > **Version control**.
1. A stack targeting the repository has had its deployment settings saved at least once. Pulumi registers the per-repository webhook the first time deployment settings are saved with that repository configured, not at integration install time.
1. The webhook exists on the Bitbucket repository. In Bitbucket, open the repository and navigate to **Repository settings** > **Workflow** > **Webhooks** (under the repository, not the workspace). Look for an entry titled **Pulumi Deployments** in the **Repository hooks** section.
1. The stack is associated with the correct Bitbucket repository and branch.

### Integration shows as disconnected

If the integration card shows an invalid or disconnected status, [delete the integration](#integration-settings) and re-create it by following the [installation steps](#installation-and-configuration).

### Deployments not triggering

If deployments aren't triggering on push or pull request events:

1. Verify deployment settings are enabled under **Stack** > **Settings** > **Deploy**.
1. Check that the branch matches your configured deployment branch.
1. If using path filters, confirm that the changed files match your glob patterns.

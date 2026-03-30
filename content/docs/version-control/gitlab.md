---
title_tag: "GitLab Integration | Version Control"
meta_desc: Connect GitLab groups to Pulumi Cloud for merge request previews, push-to-deploy, review stacks, commit statuses, and automated deployments.
title: GitLab
h1: GitLab
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    version-control:
        name: GitLab
        parent: version-control-home
        weight: 2
aliases:
- /docs/integrations/gitlab/
- /docs/iac/integrations/gitlab-app/
- /docs/iac/guides/continuous-delivery/gitlab-app/
- /docs/iac/using-pulumi/continuous-delivery/gitlab-app/
- /docs/guides/continuous-delivery/gitlab-app/
- /docs/using-pulumi/continuous-delivery/gitlab-app/
- /docs/iac/packages-and-automation/continuous-delivery/gitlab-app/
---

Pulumi Cloud integrates with GitLab to post merge request previews, deploy infrastructure on push, create ephemeral review stacks, and report commit statuses. Once configured, the integration automatically registers webhooks on your GitLab group and manages authentication for you.

## Installation and configuration

{{% notes type="info" %}}
To set up the GitLab integration, you must be an org admin in Pulumi Cloud and have Owner access (for Group Access Token auth) or Reporter+ access (for User OAuth Token auth) in the target GitLab group.
{{% /notes %}}

1. [Sign in to your Pulumi account.](https://app.pulumi.com/signin)
1. Navigate to **Management** > **Version control**.
1. Select **Add account** and choose **GitLab**, then follow the prompts to authorize with GitLab.
1. Select the GitLab group you want to integrate with and configure your [integration settings](#integration-settings).

Pulumi automatically registers a group-level webhook on your GitLab group. No manual webhook or pipeline configuration is required.

### Authentication methods

Pulumi supports two authentication methods depending on your GitLab plan:

- **Group Access Token** (recommended, Premium/Ultimate): Pulumi auto-provisions a token named "Pulumi App Integration for org: {orgName}" with `api` scope and Owner access level. Tokens expire after 1 year and auto-rotate 6 months before expiration.
- **User OAuth Token** (all plans including Free): Uses the logged-in user's GitLab OAuth token with `api` and `read_user` scopes. Refresh tokens handle expiry automatically.

If the selected group does not support Group Access Tokens, Pulumi Cloud prompts you to use your personal GitLab account for organization authentication instead.

### Individual user setup

Separately from the org-level integration, individual users can complete a 3-step OAuth flow under **Management** > **Version control** to grant Pulumi access to their GitLab account. This is used for features like Neo Agent repository creation on the user's behalf and does not create webhooks.

{{% notes type="info" %}}
To remove your individual identity, select your identity on the integration card and choose **Remove Identity**.
{{% /notes %}}

## Integration settings

After creating an integration, you can configure merge request behavior. Toggle these settings per integration:

| Setting | Default | Description |
|---|---|---|
| Pull request comments | Enabled | Post deployment status and resource changes as comments on GitLab merge requests |
| Neo summaries for pull request comments | Enabled | Include AI-generated summaries of infrastructure changes in merge request comments (requires [AI Agents](/docs/ai/) to be enabled for your organization) |
| Detailed diff for pull request comments | Enabled | Show property-level before/after diffs for changed resources in merge request comments |

To delete an integration, select **Delete Integration** on the integration card. This removes the webhook from your GitLab group and disconnects all stacks using that integration.

## Capabilities

### Merge request comments

Pulumi automatically posts comments on merge requests with the results of any stack changes. This includes a summary of how many resources were created, updated, or deleted, with a link to the full details in [Pulumi Cloud](https://app.pulumi.com). When enabled, comments also include a collapsible detailed diff and an AI-generated explanation from Neo.

Comments are idempotent: updates to the same stack edit the existing comment rather than creating a new one. Draft and WIP merge requests are treated identically to regular merge requests.

For [review stacks](#review-stacks), comments show the review stack status and outputs instead of a standard preview summary.

### Commit status checks

Pulumi posts commit status checks to GitLab on every deployment, for both push and merge request events. Statuses map to GitLab's `pending`, `running`, `success`, and `failed` states and include a link back to the deployment in Pulumi Cloud.

### Push-to-deploy

Push-to-deploy automatically runs `pulumi up` when a commit is pushed to a configured branch, most commonly the default branch. Enable this under **Stack** > **Settings** > **Deploy** by toggling **Deploy on push**. See the [push-to-deploy documentation](/docs/deployments/deployments/using/triggers/#push-to-deploy) for setup instructions.

You can use path filters to limit deployments to commits that change files matching specific glob patterns (e.g., `infrastructure/**`).

### Review stacks

[Review stacks](/docs/deployments/deployments/review-stacks/) are ephemeral cloud environments created automatically every time a merge request is opened, powered by Pulumi Deployments. Open a merge request, and Pulumi Deployments stands up a stack with your changes and posts a merge request comment with the outputs. Merge or close the merge request, and Pulumi Deployments destroys the stack and frees the associated resources.

Review stacks follow the naming convention `pr-{group}-{project}-{mr-iid}` (for example, group `acme/infra` with merge request #42 produces stack `pr-acme-infra-42`). Configuration is copied from the template stack via `pulumi config cp`, and stacks are automatically deleted after the destroy completes.

To enable review stacks, toggle **Pull request template** under **Stack** > **Settings** > **Deploy** on the stack you want to use as a template.

### Environment variables

Pulumi injects the following environment variables during GitLab-triggered deployments:

| Variable | Set when | Value |
|---|---|---|
| `PULUMI_CI_BRANCH_NAME` | Push and merge request events | Branch name |
| `PULUMI_PR_NUMBER` | Merge request events | Merge request IID (number) |
| `PULUMI_CI_PULL_REQUEST_SHA` | Merge request events | Full commit SHA |

## New project wizard

The [New Project Wizard](/docs/idp/concepts/new-project-wizard/) supports GitLab as a VCS provider. When the GitLab integration is configured and you have a GitLab OAuth token, you can:

- Create new GitLab projects in your integrated group (created as private with a README)
- Select an existing GitLab repository and branch
- Choose any deployment method: CLI, Pulumi Deployments (no-code), or Pulumi Deployments (VCS-backed)

When using the VCS-backed deployment method, the wizard configures deploy-on-push, merge request previews, and review stacks automatically. If a template URL contains `gitlab.com`, GitLab is auto-selected as the VCS provider.

Organizations can register GitLab repositories as template sources. Pulumi scans registered repositories for subdirectories containing a `Pulumi.yaml` file, and each subdirectory becomes a selectable template. Private repositories are authenticated automatically via the integration's token.

## CI integration

The Pulumi GitLab integration posts results back to GitLab regardless of which CI/CD system triggers the run. You can also run Pulumi commands directly in GitLab CI/CD pipelines. See the [GitLab CI guide](/docs/iac/guides/continuous-delivery/gitlab-ci/) for setup instructions and example pipeline configurations.

## OIDC authentication

Use GitLab CI's built-in OIDC tokens to authenticate with Pulumi Cloud without storing long-lived credentials as CI variables. See [Configuring OpenID Connect for GitLab](/docs/administration/access-identity/oidc-client/gitlab/) for configuration details.

## Template sources

Use GitLab repositories as template sources for [Pulumi IDP](/docs/idp/concepts/organization-templates/). Your teams can reference GitLab-hosted Pulumi templates when creating new projects through the developer portal. For details on registering template repositories, see [New project wizard](#new-project-wizard).

## Troubleshooting

### Merge request comments not appearing

If comments aren't appearing on your merge requests, verify that:

1. The GitLab integration is connected and shows a valid status under **Management** > **Version control**.
1. The webhook exists on your GitLab group. Navigate to your group's **Settings** > **Webhooks** and look for the `https://api.pulumi.com/workflow/gitlab` endpoint.
1. The stack is associated with the correct GitLab repository and branch.

### Integration shows as disconnected

If the integration card shows an invalid or disconnected status, [delete the integration](#integration-settings) and re-create it by following the [installation steps](#installation-and-configuration).

### Deployments not triggering

If deployments aren't triggering on push or merge request events:

1. Verify deployment settings are enabled under **Stack** > **Settings** > **Deploy**.
1. Check that the branch matches your configured deployment branch.
1. If using path filters, confirm that the changed files match your glob patterns.

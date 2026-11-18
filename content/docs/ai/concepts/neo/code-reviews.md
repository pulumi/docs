---
title: Code reviews
title_tag: Code reviews | Pulumi Agents
h1: Code reviews
meta_desc: Review GitHub pull requests using Pulumi operation results and receive inline feedback on infrastructure changes.
aliases:
- /docs/pulumi-cloud/neo/code-reviews/
- /docs/iac/neo/code-reviews/
- /docs/ai/code-reviews/
- /docs/ai/integrations/github/
- /docs/ai/neo/code-reviews/
menu:
    ai:
        name: Code reviews
        parent: ai-agents-review
        weight: 30
        identifier: ai-code-reviews
pulumi_cloud_feature: neo-code-reviews
---

Enable code reviews to get inline feedback on infrastructure changes in GitHub.com pull requests. Each review uses the Pulumi operations recorded for the pull request's commit to identify changes that need attention. The review does not block merging.

## Setup

1. Open [organization AI settings](/docs/ai/concepts/neo/settings/#enable-neo-for-organization). On **General**, turn on **Enable AI features for this organization** and **Enable Pulumi Agents**, then select **Save changes**.
1. Install the [Pulumi GitHub App](/docs/integrations/version-control/github-app/) on the repositories you want to review.
1. Under **Agent Settings** > **Code reviews**, turn on **Enable code reviews for this organization** and select **Save changes**. Code reviews are on by default.
1. Grant Pulumi access to your GitHub account by completing the [individual OAuth flow](/docs/integrations/version-control/github-app/#individual-user-setup) under **Settings** > **Version control**.

## Automated reviews

Reviews run automatically for eligible pull requests by default, skipping drafts and pull requests opened by bots. The review uses completed Pulumi operations associated with that commit, such as previews run by your CI workflow or Pulumi Deployments. Those operations must be recorded in Pulumi Cloud.

Code reviews consume model usage billed under the same rules as other agent tasks. Review that usage under **Neo Code Reviews** on the usage page. See [Usage limits](/docs/ai/concepts/neo/usage-limits/) for billing and spending controls.

## Manual reviews

To run reviews only when requested, open **Agent Settings** > **Code reviews** > **Review settings**. Turn off **Automatically review new pull requests**, remove any labels under **Review when a label is added**, and select **Save changes**. Check **Repository overrides** for repositories with different settings.

Mention `@pulumi-neo` in a pull request description, a review comment (top-level or inline), or an issue, and the agent replies in the same thread. Ask it to walk through what a change does, including resources that change in stacks the pull request does not modify directly.

Pulumi matches your GitHub identity to your Pulumi user. If you signed in to Pulumi with GitHub, that link already exists; otherwise, [link a GitHub identity to your Pulumi account](/docs/administration/concepts/accounts/#adding-new-identities).

## Availability

Code reviews support GitHub.com. They do not support GitHub Enterprise Server, Azure DevOps, GitLab, or Bitbucket. On those providers, pull-request comments from the [version control integration](/docs/integrations/version-control/) are separate from agent reviews.

Code reviews replace AI preview summaries on pull requests where those summaries were enabled.

## Permissions

Automatic reviews use the Pulumi account linked to the pull request author's GitHub identity. A review requested with `@pulumi-neo` uses the account linked to the person who requested it. That account must belong to the Pulumi organization connected to the repository's GitHub App installation. If the GitHub user has no linked Pulumi account in that organization, the review does not run.

Reviews run in read-only permission mode with automatic approvals. The linked user's permissions control access to Pulumi Cloud resources. Read-only mode does not restrict credentials for connected tools. Give those connections only the access required for reviewing code. See [Permissions and approvals](/docs/ai/agents/permissions/).

To turn reviews off, open **Agent Settings** > **Code reviews**, turn off **Enable code reviews for this organization**, and select **Save changes**.

## Troubleshooting

If reviews do not run in a repository, confirm that the Pulumi GitHub App installation covering that repository is linked to your Pulumi organization. Installations created directly from the GitHub Marketplace can exist without a linked organization, and reviews do not run on their pull requests. When this happens, the Pulumi preview comment on the pull request includes a note with a link to finish connecting the installation. See [Link an existing installation](/docs/integrations/version-control/github-app/#link-an-existing-installation).

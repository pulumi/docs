---
title: Code reviews
title_tag: Neo code reviews
h1: Neo code reviews
meta_desc: Neo code reviews analyze pull requests against what Pulumi Cloud knows about your running infrastructure and leave feedback in the pull request.
aliases:
- /docs/pulumi-cloud/neo/code-reviews/
- /docs/iac/neo/code-reviews/
- /docs/ai/code-reviews/
- /docs/ai/integrations/github/
menu:
    ai:
        name: Code reviews
        parent: ai-neo
        weight: 35
        identifier: ai-code-reviews
pulumi_cloud_feature: neo-code-reviews
---

{{% notes type="info" %}}
Neo code reviews are currently in public preview and will be generally available on July 1, 2026.
{{% /notes %}}

Neo code reviews analyze pull requests against what Pulumi Cloud knows about your running infrastructure and leave feedback in the pull request. They read the `pulumi preview` output and comment inline on the specific lines that need attention. Neo does not block the merge.

## Automated reviews

By default, Neo reviews every pull request automatically, skipping drafts and pull requests opened by bots.

## Manual reviews

You can scope Neo to review only when someone mentions `@pulumi-neo`, instead of automatically. Mention it in a pull request description, a review comment (top-level or inline), or an issue, and Neo replies in the same thread. Ask it to walk through what a change does, including resources that change in stacks the pull request does not modify directly.

Neo matches your GitHub identity to your Pulumi user. If you signed in to Pulumi with GitHub, that link already exists; otherwise, [link a GitHub identity to your Pulumi account](/docs/administration/concepts/accounts/#adding-new-identities).

## Availability

Neo code reviews run on GitHub.com. They are not available on Azure DevOps, GitLab, or Bitbucket, where pull request comments come from the [version control integration](/docs/integrations/version-control/) rather than from Neo. GitHub Enterprise Server is not supported. Code reviews are enabled by default for organizations with [Pulumi Neo](/docs/ai/neo/get-started/#enabling-and-disabling-neo) turned on. If Neo already posts preview summaries on your pull requests, Neo code reviews replace them.

## Setup

1. Enable [Pulumi Neo](/docs/ai/neo/get-started/#enabling-and-disabling-neo) for your organization.
1. Install the [Pulumi GitHub App](/docs/integrations/version-control/github-app/) on the repositories you want Neo to analyze.
1. Confirm code reviews are enabled under **Settings** > **Neo settings** > **Code reviews**. They're on by default.
1. Grant Pulumi access to your GitHub account by completing the [individual OAuth flow](/docs/integrations/version-control/github-app/#individual-user-setup) under **Management** > **Version control**.

## Permissions

Neo code reviews run with the same governance as any other [Neo task](/docs/ai/neo/tasks/), including the [role-based access control](/docs/administration/concepts/rbac/), guardrails, and audit logging your organization has configured. To turn them off, disable code reviews under **Settings** > **Neo settings** > **Code reviews**.

## Troubleshooting

If Neo isn't reviewing pull requests in a repository, confirm that the Pulumi GitHub App installation covering that repository is linked to your Pulumi organization. Installations created directly from the GitHub Marketplace can exist without a linked organization, and Neo skips reviews on their pull requests. When this happens, the Pulumi preview comment on the pull request includes a note with a link to finish connecting the installation. See [Link an existing installation](/docs/integrations/version-control/github-app/#link-an-existing-installation).

---
title: Code reviews
title_tag: Neo code reviews
h1: Neo code reviews
meta_desc: Neo code reviews analyze pull requests against what Pulumi Cloud knows about your running infrastructure and leave feedback in the pull request.
aliases:
- /docs/pulumi-cloud/neo/code-reviews/
- /docs/iac/neo/code-reviews/
- /docs/ai/neo/code-reviews/
- /docs/ai/integrations/github/
menu:
    ai:
        name: Code reviews
        parent: ai-home
        weight: 35
        identifier: ai-code-reviews
---

{{% notes type="info" %}}
Neo code reviews are currently in public preview and will be generally available on July 1, 2026.
{{% /notes %}}

Neo code reviews analyze pull requests against what Pulumi Cloud knows about your running infrastructure and leave feedback in the pull request. They read the `pulumi preview` output and comment inline on the specific lines that need attention. Neo does not block the merge.

## Automated reviews

By default, Neo reviews every pull request automatically, skipping drafts and pull requests opened by bots.

## Manual reviews

You can scope Neo to review only when someone mentions `@pulumi-neo`, instead of automatically. Mention it in a pull request description, a review comment (top-level or inline), or an issue, and Neo replies in the same thread. Ask it to walk through what a change does, including resources that change in stacks the pull request does not modify directly.

Neo matches your GitHub identity to your Pulumi user. If you signed in to Pulumi with GitHub, that link already exists; otherwise, [link a GitHub identity to your Pulumi account](/docs/administration/organizations-teams/accounts/#adding-new-identities).

## Availability

Neo code reviews run on GitHub.com. GitHub Enterprise Server is not supported. Code reviews are enabled by default for organizations with [Pulumi Neo](/docs/ai/get-started/#enabling-and-disabling-neo) turned on. If Neo already posts preview summaries on your pull requests, Neo code reviews replace them.

## Setup

1. Enable [Pulumi Neo](/docs/ai/get-started/#enabling-and-disabling-neo) for your organization.
1. Install the [Pulumi GitHub App](/docs/integrations/version-control/github-app/) on the repositories you want Neo to analyze.
1. Confirm Neo code reviews are enabled in your [GitHub App integration settings](/docs/integrations/version-control/github-app/). They're on by default.
1. Grant Pulumi access to your GitHub account by completing the [individual OAuth flow](/docs/integrations/version-control/github-app/#individual-user-setup) under **Management** > **Version control**.

## Permissions

Neo code reviews run with the same governance as any other [Neo task](/docs/ai/tasks/), including the [role-based access control](/docs/administration/access-identity/rbac/), guardrails, and audit logging your organization has configured. To turn them off, disable Neo code reviews in your [GitHub App integration settings](/docs/integrations/version-control/github-app/).

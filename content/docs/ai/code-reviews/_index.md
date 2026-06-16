---
title: Code Reviews
title_tag: Neo Code Reviews
h1: Neo Code Reviews
meta_desc: Neo Code Reviews analyzes pull requests against what Pulumi Cloud knows about your running infrastructure and leaves its feedback in the pull request.
meta_image: /images/docs/meta-images/docs-meta.png
aliases:
- /docs/pulumi-cloud/neo/code-reviews/
- /docs/iac/neo/code-reviews/
- /docs/ai/neo/code-reviews/
- /docs/ai/integrations/github/
menu:
    ai:
        name: Code Reviews
        parent: ai-home
        weight: 35
        identifier: ai-code-reviews
---

{{% notes type="info" %}}
Neo Code Reviews is in public preview and becomes generally available on July 1, 2026.
{{% /notes %}}

Neo Code Reviews analyzes pull requests against what Pulumi Cloud knows about your running infrastructure and leaves its feedback in the pull request. It reads the `pulumi preview` output and comments inline on the specific lines that need attention. Neo does not block the merge.

## Automated reviews

By default, Neo reviews every pull request automatically, skipping drafts and pull requests opened by bots.

## Manual reviews

You can scope Neo to review only when someone mentions `@pulumi-neo`, instead of automatically. Mention it in a pull request description, a review comment (top-level or inline), or an issue, and Neo replies in the same thread. Ask it to walk through what a change does, including resources that change in stacks the pull request does not modify directly.

Neo matches your GitHub identity to your Pulumi user. If you signed in to Pulumi with GitHub, that link already exists; otherwise, [link a GitHub identity to your Pulumi account](/docs/administration/organizations-teams/accounts/#adding-new-identities).

## Availability

Neo Code Reviews runs on GitHub.com. GitHub Enterprise Server is not supported. It is enabled by default for organizations with [Pulumi Neo](/docs/ai/get-started/#enabling-and-disabling-neo) turned on. If Neo already posts preview summaries on your pull requests, Neo Code Reviews replaces them.

## Setup

1. Enable [Pulumi Neo](/docs/ai/get-started/#enabling-and-disabling-neo) for your organization.
1. Install the [Pulumi GitHub App](/docs/integrations/version-control/github-app/) on the repositories you want Neo to analyze.
1. Confirm Neo Code Reviews is enabled in your [GitHub App integration settings](/docs/integrations/version-control/github-app/). It is on by default.
1. Grant Pulumi access to your GitHub account by completing the [individual OAuth flow](/docs/integrations/version-control/github-app/#individual-user-setup) under **Management** > **Version control**.

## Permissions

Neo Code Reviews runs with the same governance as any other [Neo task](/docs/ai/tasks/): the [role-based access control](/docs/administration/access-identity/rbac/), guardrails, and audit logging your organization has configured. To turn it off, disable Neo Code Reviews in your [GitHub App integration settings](/docs/integrations/version-control/github-app/).

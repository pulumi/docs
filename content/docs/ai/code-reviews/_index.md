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

Neo code reviews analyze pull requests against what Pulumi Cloud knows about your running infrastructure and leave feedback in the pull request. They read the `pulumi preview` output and, when the GitHub App's [Code access for AI reviews](/docs/integrations/version-control/github-app/#integration-settings) setting is on (the default), the pull request's code changes. Neo comments inline on the specific lines that need attention and does not block the merge.

## Configuring reviews

Configure how Neo reviews pull requests under **Settings** > **Neo settings** > **Code reviews**. You set organization-wide defaults, and where a repository needs different behavior you add a per-repository override and change the fields that should differ from those defaults.

- **Enable code reviews.** Turn Neo code reviews on or off for the organization, or for a single repository in an override.
- **Automatically review new pull requests.** Start a review as soon as a pull request is opened, reopened, or marked ready for review. Turn this off to keep reviews on demand.
- **Review when a label is added.** Name one or more labels that trigger a review when they are applied to a pull request. This works independently of automatic review, so you can review only labeled pull requests.
- **Ignore draft pull requests.** Skip pull requests that are still in draft. This is on by default, and a draft is reviewed once marked ready for review.
- **Use Neo integrations.** Let Neo draw on your connected observability, incident, and issue-tracking tools for more context during a review.

Neo reviews a pull request when opened, not on every push. After you push new commits, mention `@pulumi-neo` to request a fresh review. Pull requests opened by bots are skipped.

## Manual reviews

Mention `@pulumi-neo` in a pull request description, a review comment (top-level or inline), or an issue, and Neo replies in the same thread. Manual review is always available regardless of the automatic and label settings; use it to request a re-review after pushing new commits. Ask Neo to walk through what a change does, including resources that change in stacks the pull request does not modify directly.

Neo matches your GitHub identity to your Pulumi user. If you signed in to Pulumi with GitHub, that link already exists; otherwise, [link a GitHub identity to your Pulumi account](/docs/administration/organizations-teams/accounts/#adding-new-identities).

## Availability

Neo code reviews run on GitHub.com. GitHub Enterprise Server is not supported. Code reviews are enabled by default for organizations with [Pulumi Neo](/docs/ai/get-started/#enabling-and-disabling-neo) turned on. If Neo already posts preview summaries on your pull requests, Neo code reviews replace them.

## Setup

1. Enable [Pulumi Neo](/docs/ai/get-started/#enabling-and-disabling-neo) for your organization.
1. Install the [Pulumi GitHub App](/docs/integrations/version-control/github-app/) on the repositories you want Neo to analyze.
1. Confirm Neo code reviews are enabled under **Settings** > **Neo settings** > **Code reviews**. They're on by default.
1. Grant Pulumi access to your GitHub account by completing the [individual OAuth flow](/docs/integrations/version-control/github-app/#individual-user-setup) under **Management** > **Version control**.

## Permissions

Neo code reviews run with the same governance as any other [Neo task](/docs/ai/tasks/), including the [role-based access control](/docs/administration/access-identity/rbac/), guardrails, and audit logging your organization has configured. To turn them off, or to change how they run, open **Settings** > **Neo settings** > **Code reviews**.

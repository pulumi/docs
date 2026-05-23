---
title: GitHub
title_tag: Neo GitHub Integration
h1: GitHub Integration
meta_desc: Mention @pulumi-neo in GitHub pull requests, review comments, and issues to bring Neo into the conversation.
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    ai:
        name: GitHub
        parent: ai-integrations
        weight: 2
        identifier: ai-integrations-github
---

Mention `@pulumi-neo` in a pull request description, a review comment (top-level or inline), or an issue, and Neo replies in the same thread.

## What you can do with `@pulumi-neo`

Neo sees the diff, the stacks linked to the repository, and their current state. Reviewers can ask it to walk through what a proposed change actually does, including resources that change downstream in stacks the PR doesn't touch directly. The responses land in the same thread, so analysis becomes part of the review record and follow-up clarifications happen in place.

## Setting up the integration

### 1. Install the Pulumi GitHub App

A GitHub organization admin installs the [Pulumi GitHub App](/docs/integrations/version-control/github-app/) on the organization or user account that owns the repositories you want Neo to access.

### 2. Link your Pulumi user to GitHub

When you mention `@pulumi-neo`, Neo identifies you by matching your GitHub identity to your Pulumi user. If you signed in to Pulumi with GitHub, that link is already in place. Otherwise, [link a GitHub identity to your Pulumi account](/docs/administration/organizations-teams/accounts/#adding-new-identities).

### 3. Mention `@pulumi-neo`

In a repository the app can see, open or comment on a pull request or issue and mention `@pulumi-neo` with what you want. Neo replies in the same thread.

## How permissions work

[Tasks](/docs/ai/tasks/) started from GitHub run with the [RBAC permissions](/docs/administration/access-identity/rbac/) of the corresponding Pulumi Cloud user.

## Limitations

- Supported on GitHub.com only. GitHub Enterprise Server is not supported.

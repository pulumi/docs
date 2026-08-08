---
title_tag: "Pulumi Version Control Integrations"
meta_desc: Connect Pulumi with your version control system using integrations for GitHub, GitLab, Azure DevOps, Bitbucket, and custom Git or Mercurial VCS providers.
title: Version Control
linktitle: Version Control
h1: Version Control
docs_home: true
notitle: true
norightnav: true
menu:
  integrations:
    name: Version Control
    identifier: integrations-version-control
    parent: integrations-home
    weight: 2
aliases:
- /docs/version-control/
description: |
  Pulumi version control integrations connect Pulumi with your VCS provider, enabling infrastructure previews on pull requests and automated deployment workflows. Use a native integration for GitHub, GitLab, Azure DevOps, or Bitbucket, or connect any Git or Mercurial server with a Custom VCS integration.

sections:
- type: flat
  heading: What every integration provides
  description_md: |
    The native integrations — GitHub, GitLab, Bitbucket, and Azure DevOps — all provide the same core set of capabilities. Whichever provider you connect, you get:

    - **Pull request previews and comments.** When a pull request is opened or updated, Pulumi runs `pulumi preview` and posts the resource changes back as a comment, so reviewers see the infrastructure impact of a change without leaving the pull request. Comments can include a collapsible property-level diff.
    - **Commit status checks.** Pull request deployment results are reported back to the provider as commit statuses, each linking to the full deployment in Pulumi Cloud. On GitHub, push-to-deploy runs report a check as well; on the other providers, statuses are posted for pull request deployments only.
    - **Push-to-deploy.** Pushing to a configured branch runs `pulumi up` automatically. Path filters limit deployments to commits that touch matching files, and [tag triggers](/docs/deployments/concepts/settings/tag-filtering/) let you deploy on release tags instead of every commit.
    - **[Review stacks](/docs/deployments/concepts/review-stacks/).** Each pull request gets a real, ephemeral environment, destroyed automatically when the pull request is merged or closed.
    - **Repository and branch discovery.** Pulumi lists your repositories and branches when you configure a stack's deployment settings, instead of making you type identifiers by hand.
    - **Managed credentials and webhooks.** Pulumi registers the necessary webhooks or service hooks and handles token issuance and rotation for you.
    - **New project creation.** The [New Project Wizard](/docs/idp/concepts/new-project-wizard/) can create a repository or target an existing one, and organization [templates](/docs/idp/concepts/organization-templates/) can be sourced from your repositories.

    [Custom VCS](/docs/integrations/version-control/custom-vcs/) is the exception: it connects any Git or Mercurial server via manually configured webhooks and supports push-to-deploy only — no pull request comments, commit statuses, or review stacks.

    Provider pages document the details that differ, such as authentication methods, repository identifier formats, and injected environment variables.

- type: flat
  heading: Multiple providers and accounts
  description_md: |
    You can connect multiple VCS providers to a single Pulumi organization simultaneously, for example GitHub, GitLab, Azure DevOps, Bitbucket, and Custom VCS all at once. You can also connect multiple accounts of the same provider, such as two separate GitHub organizations or two GitLab groups.

    GitHub Enterprise Server is currently limited to one connection per Pulumi organization.

- type: button-cards
  heading: VCS integrations
  cards:
  - image: /logos/tech/github.svg
    heading: GitHub App
    description: Surface Pulumi stack previews as PR comments and checks. Enable push-to-deploy via Pulumi Deployments.
    link: /docs/integrations/version-control/github-app/
  - image: /logos/tech/gitlab.svg
    heading: GitLab
    description: Surface Pulumi previews on merge requests, deploy on push, create review stacks, and use GitLab repos as template sources.
    link: /docs/integrations/version-control/gitlab/
  - image: /logos/tech/bitbucket.svg
    heading: Bitbucket
    description: Connect Bitbucket Cloud workspaces to Pulumi Cloud for pull request previews, push-to-deploy, review stacks, and automated deployments.
    link: /docs/integrations/version-control/bitbucket/
  - image: /logos/tech/ci-cd/azure-devops.svg
    heading: Azure DevOps Integration
    description: Connect Azure DevOps projects to Pulumi Cloud for pull request previews, push-to-deploy, review stacks, and commit statuses.
    link: /docs/integrations/version-control/azure-devops-integration/
  - image: /logos/tech/git.svg
    heading: Custom VCS
    description: Connect any Git or Mercurial VCS server to Pulumi Deployments using webhooks and ESC-managed credentials.
    link: /docs/integrations/version-control/custom-vcs/

- type: flat
  heading: Have questions?
  description: <p>For questions or feedback, reach out on <a href="https://slack.pulumi.com" target="_blank">community Slack</a>, <a href="https://github.com/pulumi" target="_blank">GitHub</a>, or <a href="/support/">contact support</a>.</p>
---

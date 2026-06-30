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
    description: Connect Azure DevOps repositories to Pulumi Cloud Deployments to deploy on push, preview pull requests, and post PR summaries.
    link: /docs/integrations/version-control/azure-devops-integration/
  - image: /logos/tech/git.svg
    heading: Custom VCS
    description: Connect any Git or Mercurial VCS server to Pulumi Deployments using webhooks and ESC-managed credentials.
    link: /docs/integrations/version-control/custom-vcs/

- type: flat
  heading: Have questions?
  description: <p>For questions or feedback, reach out on <a href="https://slack.pulumi.com" target="_blank">community Slack</a>, <a href="https://github.com/pulumi" target="_blank">GitHub</a>, or <a href="/support/">contact support</a>.</p>
---

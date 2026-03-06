---
title: "Pulumi Cloud Now Supports Azure DevOps and More"
date: 2026-03-03
draft: false
meta_desc: "Pulumi expands version control support with Azure DevOps and more. Connect your repos, configure deployments, and use Neo across your VCS providers."
meta_image: meta.png
authors:
    - luke-ward
    - michael-fallihee
    - boris-schlosser
    - dan-biwer
tags:
    - features
    - pulumi-cloud
    - azure
    - github
social:
    twitter:
    linkedin:
aliases:
    - /blog/pulumi-now-supports-azure-devops-in-the-new-project-wizard/
    - /blog/pulumi-now-supports-azure-devops-and-gitlab/
---

We've added Azure DevOps (ADO) as a VCS provider for Pulumi, and GitHub Enterprise Server and GitLab support are also now available. If your team uses ADO, you can now deploy infrastructure directly from your repositories, using the same git-backed workflow we've had for GitHub.

<!--more-->

Connecting your VCS unlocks the full Pulumi Cloud workflow: push-to-deploy pipelines, pull request previews, Neo-powered change summaries on PRs, and scheduled drift detection, all while managing through our new CI/CD integrations.

![Add account screen showing GitHub, GitLab, and Azure DevOps as VCS options](VCS.png)

## What's included

These features ship with Azure DevOps, and GitHub Enterprise Server and GitLab support is also included:

**Org and project discovery**: During setup, Pulumi lists your organizations and projects so you can pick where your infrastructure code lives.

**Repo and branch operations**: Browse, select, or create repositories within your project. Pick a branch and wire it up without leaving the wizard.

![New project wizard with Azure DevOps repository settings](ado-npw.png)

**OpenID Connect (OIDC) authentication (ADO)**: Exchange Pulumi's OIDC token for an Azure access token via Entra ID, so no long-lived secrets are stored.

**Neo on pull requests**: Neo posts summaries and infrastructure change explanations to your ADO pull requests, same as it does for GitHub.

![Neo PR comment showing resource changes on an Azure DevOps pull request](ado-prcomments.png)

**Neo tasks**: Neo works with your ADO repositories. Ask Neo to make changes, and it can open pull requests directly against your connected repos.

**Deployment**: Stacks connected to ADO support push-to-deploy, pull request previews, path filters, environment variables, secrets, and drift detection schedules.

**...and more.** Anything you could do with GitHub, you can do with all of these VCS providers.

## Getting started

1. An org admin configures the integration under **Settings** > **Version Control**.
1. Authorize with your VCS provider.
1. Deploy infrastructure with first-class workflows.

See the [Azure DevOps integration docs](/docs/integrations/azure-devops-integration/) for the full setup walkthrough. We also support [GitHub Enterprise Server](/docs/integrations/github-app/#github-enterprise-server-support) and [GitLab](/docs/integrations/gitlab/). If you're using GitHub.com, check out the [Pulumi GitHub App](/docs/integrations/github-app/).

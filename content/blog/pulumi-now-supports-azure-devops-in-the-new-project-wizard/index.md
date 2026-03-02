---
title: "Pulumi Now Supports Azure DevOps"
date: 2026-02-26
draft: false
meta_desc: "Pulumi Deployments now supports Azure DevOps as a VCS provider. Connect ADO repos, configure integrations, and deploy infrastructure."
meta_image: meta.png
authors:
    - luke-ward
    - michael-fallihee
tags:
    - features
    - pulumi-cloud
    - azure
social:
    twitter:
    linkedin:
---

We've added Azure DevOps (ADO) as a VCS provider for Pulumi Deployments. If your team uses ADO, you can now deploy infrastructure directly from your ADO repositories, the same git-backed workflow we've had for GitHub.

<!--more-->

## What's included

**OAuth integration**: Connect your ADO account through a standard OAuth flow with PKCE. Authorize once, and Pulumi handles token management from there.

**Org and project discovery**: During setup, Pulumi lists your Azure DevOps organizations and projects so you can pick where your infrastructure code lives.

**Repo and branch operations**: Browse, select, or create repositories within your ADO project. Pick a branch and wire it up without leaving the wizard.

**Per-project app OIDC**: Exchange Pulumi's OIDC token for an Azure DevOps access token via Microsoft Entra ID federated credentials. No long-lived secrets stored. Falls back to user OAuth tokens when not configured.

**VCS provider selector**: When both GitHub and ADO are configured, a dropdown in the wizard lets you pick which one to use.

**Integration management**: Admins can create, update, and delete ADO integrations per org. Configure PR comments, Neo summaries, and detailed diff settings, same controls as GitHub.

**Neo on ADO pull requests**: Neo posts PR summaries and infrastructure change explanations to your ADO pull requests, same as it does for GitHub.

**Deployment settings**: ADO-backed stacks support push-to-deploy, PR previews, path filters, environment variables, secrets, and drift detection schedules.

## Getting started

1. An org admin configures the Azure DevOps integration under **Settings > Integrations**.
1. Individual users authorize their ADO accounts via OAuth.
1. Open the New Project Wizard, select Azure DevOps as your VCS provider, choose a repo, and deploy.

See the [Azure DevOps integration docs](/docs/deployments/deployments/azure-devops/) for the full setup walkthrough.

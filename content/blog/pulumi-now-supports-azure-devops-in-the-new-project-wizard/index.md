---
title: "Pulumi Now Supports Azure DevOps"
date: 2026-02-26
draft: false
meta_desc: "Pulumi now supports Azure DevOps as a VCS provider. Connect ADO repos, configure integrations, and deploy infrastructure."
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

We've added Azure DevOps (ADO) as a VCS provider for Pulumi. If your team uses ADO, you can now deploy infrastructure directly from your ADO repositories, the same git-backed workflow we've had for GitHub.

<!--more-->

## What's included

**Org and project discovery**: During setup, Pulumi lists your Azure DevOps organizations and projects so you can pick where your infrastructure code lives.

**Repo and branch operations**: Browse, select, or create repositories within your ADO project. Pick a branch and wire it up without leaving the wizard.

**Per-project app OIDC**: Exchange Pulumi's OIDC token for an Azure DevOps access token via Microsoft Entra ID federated credentials. No long-lived secrets stored.

**Neo on ADO pull requests**: Neo posts PR summaries and infrastructure change explanations to your ADO pull requests, same as it does for GitHub.

**Deployment**: ADO-backed stacks support push-to-deploy, PR previews, path filters, environment variables, secrets, and drift detection schedules.

**...and more.  Anything you can do with GitHub, you can do with ADO.**

## Getting started

1. An org admin configures the Azure DevOps integration under **Settings > Integrations**.
1. Authorize via OAuth.
1. Enjoy deploying infrastructure directly from your ADO repositories.

See the [Azure DevOps integration docs](/docs/iac/guides/continuous-delivery/azure-devops-integration/) for the full setup walkthrough. If you're using GitHub, check out the [Pulumi GitHub App](/docs/iac/guides/continuous-delivery/github-app/).

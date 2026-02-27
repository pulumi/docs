---
title: "Pulumi Now Supports Azure DevOps"
date: 2026-02-26
draft: false
meta_desc: "Pulumi now supports Azure DevOps as a first-class VCS provider in the New Project Wizard. Connect repos, manage integrations, and deploy from ADO."
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

Pulumi Deployments now supports Azure DevOps (ADO) as a first-class VCS provider. Teams using Azure DevOps can create, deploy, and manage infrastructure directly from their ADO repositories, with the same experience GitHub users already enjoy.

<!--more-->

## Azure DevOps as a VCS-backed deployment target

Pulumi Deployments already supports GitHub repositories as a git-backed configuration store. Now, Azure DevOps repositories get the same treatment. Select an ADO repo in the [New Project Wizard](/docs/idp/concepts/new-project-wizard/), and Pulumi handles the rest: pushing configuration and triggering deployments.

## Feature highlights

### Full OAuth integration

Connect your Azure DevOps account through a standard OAuth flow with PKCE. Pulumi securely stores and manages your credentials so you can authorize once and deploy continuously.

### Organization and project discovery

During setup, Pulumi automatically discovers your Azure DevOps organizations and projects, so you can select where your infrastructure code should live.

### Repository and branch operations

Browse, select, or create repositories within your ADO project. List branches, pick a default, and wire everything up without leaving the wizard.

### Per-project app OIDC authentication

Use Microsoft Entra ID federated credentials to exchange Pulumi's OIDC token for an Azure DevOps access token. No long-lived secrets are stored in the database. When per-project app auth isn't configured, Pulumi falls back to user OAuth tokens.

### VCS provider selector

A provider selector in the wizard lets you switch between GitHub and Azure DevOps when both are configured.

### Integration management

Admins can create, list, update, and delete ADO integrations per organization. Configure PR comments, Neo summaries, and detailed diff settings, mirroring the controls already available for GitHub.

### Neo integration

Neo, Pulumi's AI-powered assistant, works with Azure DevOps pull requests just like it does with GitHub. Get automated PR summaries, infrastructure change explanations, and deployment insights posted directly to your ADO pull requests.

### Deployment settings parity

ADO-backed stacks support the same deployment configuration as GitHub: environment variables, secrets, drift detection schedules, PR comments, and more.

## Getting started

1. **Admin setup**: An org admin configures the Azure DevOps integration by connecting a specific ADO organization and project.
1. **User authorization**: Individual users authorize Pulumi to access their ADO repos via OAuth.
1. **Create a project**: Open the New Project Wizard, select "Azure DevOps" as your VCS provider, choose (or create) a repository, and deploy.

Ready to get started? Check out the [New Project Wizard documentation](/docs/idp/concepts/new-project-wizard/) or head to Pulumi Cloud and create your first ADO-backed project today.

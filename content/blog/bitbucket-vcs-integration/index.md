---
title: "Bitbucket Cloud Meets Pulumi Cloud"
date: 2026-04-13
draft: false
meta_desc: "Connect Bitbucket Cloud to Pulumi Cloud for automated deployments on push, pull request previews, review stacks, and AI-powered change summaries."
meta_image: meta.png
feature_image: feature.png
authors:
    - luke-ward
tags:
    - bitbucket
    - features
    - pulumi-cloud
social:
    twitter:
    linkedin:
---

Pulumi Cloud now supports Bitbucket Cloud as a first-class VCS integration, joining GitHub, GitLab, and Azure DevOps. Connect your Bitbucket workspace to deploy infrastructure on every push, preview changes on pull requests, spin up ephemeral review stacks, and get AI-powered change summaries — all without an external CI/CD pipeline.

<!--more-->

## Deploy infrastructure from Bitbucket

Connect a Bitbucket repository to a stack and infrastructure deploys automatically when you push to your configured branch. Configure path filters so only relevant file changes trigger deployments, and manage environment variables and secrets directly in Pulumi Cloud. No external CI/CD pipeline required.

Every pull request gets an infrastructure preview showing exactly what will change before merging. [Neo](/product/neo/) posts AI-generated summaries explaining what the changes mean in plain language, so reviewers can understand the impact without reading resource diffs.

<!-- TODO: Add screenshot of Bitbucket PR comment with Neo summary -->

## Two ways to connect

The integration supports two authentication methods depending on your Bitbucket plan:

- **Personal OAuth** works with every workspace, including free plans. Authorize through the standard OAuth flow and you're connected.
- **Workspace tokens** are available for Premium workspaces. Generate a token with the required scopes (`repository:admin`, `repository:write`, `pullrequest:write`, `webhook`) and paste it into Pulumi Cloud for a service-account-style connection that isn't tied to an individual user.

Both methods register webhooks automatically — no manual configuration required.

## Scaffold new projects from your repositories

The [new project wizard](/docs/idp/concepts/new-project-wizard/) discovers your Bitbucket workspace, repositories, and branches so you can scaffold and deploy a new stack without leaving Pulumi Cloud. Create a new repository directly from the wizard or select an existing one and configure VCS-backed deployments in a few clicks.

<!-- TODO: Add screenshot of new project wizard with Bitbucket selected -->

## Getting started

1. An org admin configures the integration under **Settings** > **Version control**.
1. Authorize with Bitbucket using personal OAuth or a workspace token.
1. Deploy infrastructure with first-class workflows.

For full setup details, see the [Bitbucket integration docs](/docs/version-control/bitbucket/).

{{< blog/cta-button "Connect your Bitbucket workspace" "https://app.pulumi.com/signin" "_blank" >}}

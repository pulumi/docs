---
title: "Connect Any Git or Mercurial Repo to Pulumi with Custom VCS"
date: 2026-05-04
draft: false
meta_desc: "Custom VCS integrations connect any Git or Mercurial version control system to Pulumi Deployments with webhook-driven push-to-deploy and ESC credentials."
meta_image: meta.png
feature_image: feature.png
authors:
    - michael-fallihee
tags:
    - features
    - pulumi-cloud
schema_type: auto

# Social media copy — auto-posted to X, LinkedIn, and Bluesky when merged to master.
# Character limits: X ~280, Bluesky 300, LinkedIn 3000. Leave blank to skip a platform.
social:
    twitter:
    linkedin:
    bluesky:
---

Custom VCS is a new Pulumi Cloud integration that connects any Git or Mercurial version control system to [Pulumi Deployments](/docs/deployments/deployments/) using webhooks and centrally managed credentials. Pulumi Cloud already has native integrations with [GitHub](/docs/integrations/version-control/github-app/), [GitLab](/docs/integrations/version-control/gitlab/), and [Azure DevOps](/docs/integrations/version-control/azure-devops-integration/), but if your team uses a self-hosted or third-party VCS, you've been limited to manually configuring credentials per stack with no webhook-driven automation. Custom VCS closes that gap.

<!--more-->

## The problem

Many teams run self-hosted or third-party Git servers that Pulumi Cloud doesn't have a native integration for, and some teams still use Mercurial. Until now, their only option was the raw git source approach: embedding credentials directly in each stack's deployment settings, with no way to trigger deployments automatically on push, and no support for Mercurial at all.

This meant:

- **No push-to-deploy**: Every deployment had to be triggered manually or through a separate CI pipeline.
- **Scattered credentials**: Each stack configured its own credentials independently, with no centralized management.
- **No org-level integration**: There was no shared configuration that multiple stacks could reference.

## How Custom VCS works

Custom VCS integrations introduce an org-level integration type that works with any Git or Mercurial server. The setup has three parts:

**Credentials through ESC**: Instead of OAuth flows, you store your VCS credentials (a personal access token, SSH key, or username/password) in a [Pulumi ESC](/docs/esc/) environment. The same credential structure works for both Git and Mercurial. The integration references this environment by name and resolves credentials at deployment time. Multiple stacks can share the same credentials without duplicating secrets.

**Manual repository registration**: You add repositories to the integration by name. Pulumi joins the repository name with the integration's base URL to form clone URLs. There's no auto-discovery, so you control exactly which repositories are available.

**Webhook-driven deployments**: Pulumi provides a webhook endpoint and an HMAC shared secret. You configure your VCS server to POST a JSON payload on push events, and Pulumi automatically triggers deployments for matching stacks. The webhook supports branch filtering and optional path filtering.

## What's supported

Custom VCS focuses on the deployment automation use case. Here's how it compares to native integrations:

| Capability | Native integrations | Custom VCS |
|---|---|---|
| Push-to-deploy | Yes | Yes |
| Path filtering | Yes | Yes |
| PR/MR previews | Yes | No |
| Commit status checks | Yes | No |
| PR comments | Yes | No |
| Review stacks | Yes | No |

Features like PR comments, commit statuses, and review stacks require deep API integration with each VCS platform, so they aren't available with Custom VCS. If your VCS provider is GitHub, GitLab, or Azure DevOps, we recommend using the native integration for the full feature set.

## Neo support

[Neo](/docs/ai/), Pulumi's AI assistant, works with Custom VCS integrations for repository operations that don't depend on VCS-specific APIs. Neo can clone and push to Git and Mercurial repositories registered with your Custom VCS integration using the credentials from the integration's ESC environment. Neo cannot open pull requests or create new repositories on Custom VCS servers at this time. Those operations require APIs unique to each VCS platform and are only available through native integrations.

## Get started

To set up a Custom VCS integration:

1. Navigate to **Management** > **Version control** in Pulumi Cloud.
1. Select **Add integration** and choose **Custom VCS**.
1. Provide a name, base URL, and ESC environment containing your credentials.
1. Add your repositories.
1. Configure your VCS server to send webhooks to the provided URL.

For the full setup guide including webhook payload format, HMAC signing, and credential configuration, see the [Custom VCS documentation](/docs/integrations/version-control/custom-vcs/).

## Learn more

- [Custom VCS documentation](/docs/integrations/version-control/custom-vcs/)
- [Pulumi ESC](/docs/esc/)
- [Pulumi Deployments](/docs/deployments/deployments/)
- [Push-to-deploy](/docs/deployments/deployments/using/triggers/#push-to-deploy)

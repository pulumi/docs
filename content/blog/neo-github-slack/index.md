---
title: "Neo Now Works in GitHub and Slack"
date: 2026-05-12
draft: true
meta_desc: "Mention @pulumi-neo in a pull request or @Neo in a Slack channel to start a Neo task without leaving the conversation."
authors:
    - neo-team
tags:
    - ai
    - ai-agents
    - features
    - pulumi-neo
    - github
    - slack

social:
    twitter: |
        You're reviewing a PR that touches three stacks. You want to know what actually changes downstream. Now you can mention @pulumi-neo in the PR and get the answer in the same thread.

        Neo also works in Slack. Here's what both look like.
    linkedin: |
        Infrastructure conversations happen in pull requests and Slack channels, not in a separate console. Starting today, you can mention @pulumi-neo in a GitHub PR or @Neo in Slack to start a Neo task right where the discussion is already happening.

        Neo sees the diff, the linked stacks, and their current state. The response lands in the same thread, so the analysis becomes part of the review record or the incident timeline.
    bluesky: |
        You're reviewing a PR that touches three stacks. Mention @pulumi-neo and Neo walks through what actually changes, right in the thread.

        Works in Slack too. Here's what both integrations look like.
---

[Pulumi Neo](/docs/ai/) is an AI infrastructure agent that can investigate failures, preview changes, and explain what a deployment will do. It's been available in the Pulumi Cloud console, and starting today you can reach it directly from GitHub and Slack. Mention Neo where the conversation is already happening and the analysis lands in the same thread.

<!--more-->

## GitHub: `@pulumi-neo` in pull requests and issues

Mention `@pulumi-neo` in a pull request description, a review comment, or an issue, and Neo replies in the same thread. Neo sees the diff, the stacks linked to the repository, and their current state. With that context, it can walk through what a proposed change actually does, including resources that change downstream in stacks the PR doesn't touch directly.

> **Reviewer:** @pulumi-neo This PR changes the VPC CIDR range. What else is affected?
>
> **Neo:** The `network` stack updates the VPC and its subnets. Three downstream stacks reference this VPC: `api-gateway`, `ecs-cluster`, and `rds-primary`. The subnet changes propagate to all three. The `ecs-cluster` stack will replace its ECS service because the new subnets change the network configuration on the tasks. The other two stacks update in place.

The response becomes part of the review record, and follow-up questions refine the analysis without anyone leaving the page.

**Setup** takes a few minutes. A GitHub org admin installs the Pulumi Neo GitHub App. If your team members sign in to Pulumi with GitHub, they're already linked; otherwise, each user connects their GitHub identity in their Pulumi account settings. After that, any repository the app can see is ready to go. See the [GitHub integration docs](/docs/ai/integrations/github/) for the full walkthrough.

## Slack: `@Neo` in channels

Mention `@Neo` in any Slack channel where the app has been added, and Neo starts a task in the same thread. It can check stack state, investigate failures, walk through what a change will do, and carry out actions the team has delegated to it (the same capabilities it has in the console or a PR thread).

> **On-call engineer:** @Neo The `checkout-service` stack failed its last deployment. What changed and what broke?
>
> **Neo:** The last update added a new Lambda function for image processing. The deployment failed because the function's unzipped package exceeds the 250 MB size limit. Looking at the stack's deployment history, the previous two deployments succeeded with a smaller dependency set. The `sharp` package added in this update pulls in native binaries for multiple platforms. Pinning the platform to `linux-x64` in the package config should bring it under the limit.

The rest of the channel has visibility into what was asked and what Neo found, so the full exchange stays where the discussion is already happening.

**Setup** has three steps: a Slack workspace admin installs the Pulumi Neo Slack app, each user connects their Slack identity in Pulumi Cloud (under **User account**, then **Neo Slack**), and someone adds Neo to the channel. See the [Slack integration docs](/docs/ai/integrations/slack/) for the step-by-step.

## Permissions follow the user

Both integrations run tasks with the [role-based access control (RBAC) permissions](/docs/administration/access-identity/rbac/) of the Pulumi Cloud user who mentioned Neo. The same access boundaries that apply in the console carry over to GitHub and Slack.

## Get started

Pick whichever integration fits the conversation you're already having.

- [Install the GitHub App](/docs/ai/integrations/github/) and mention `@pulumi-neo` in your next PR
- [Install the Slack App](/docs/ai/integrations/slack/) and mention `@Neo` in a channel
- [Read the integrations overview](/docs/ai/integrations/) for a full list of ways to connect Neo to your workflow

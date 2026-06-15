---
title: "Bringing Neo to GitHub and Slack"
date: 2026-05-21T08:00:00-07:00
meta_desc: "Mention @pulumi-neo in GitHub or @Neo in your Slack workspace to bring Pulumi Neo into the threads where your team works on infrastructure."
meta_image: meta.png
feature_image: feature.png
authors:
    - neo-team
tags:
    - ai
    - ai-agents
    - features
    - pulumi-neo
categories:
    - agentic-infrastructure

social:
    twitter: |
        A PR reviewer asks "what else does this change touch?" You can mention @pulumi-neo in the thread now and Neo answers. Same in Slack: @Neo in a channel starts a Pulumi task in the thread.
    linkedin: |
        Every PR review opens with the same question: what does this change actually do, and what else does it touch?

        You can answer that without leaving the thread. Mention @pulumi-neo in a GitHub pull request and Neo walks reviewers through the diff, including resources that change downstream in stacks the PR doesn't touch directly.

        Same agent shows up in Slack. Mention @Neo in a channel and start a Pulumi Neo task in the thread. The investigation, the findings, and the follow-up land where the rest of the team can already see them.

        Pulumi Neo is now in GitHub and Slack.
    bluesky: |
        Every PR review opens with the same question: what does this change actually do?

        Mention @pulumi-neo and you get the answer in the thread. Mention @Neo in Slack and you get the same agent there too, with the same context and permissions it has anywhere else.
---

This week, [Pulumi Neo](/blog/pulumi-neo/) started working in two more places: GitHub and Slack. The agent that already runs Pulumi tasks from the Cloud console and the [terminal](/blog/pulumi-neo-cli/) now participates in the threads where your team discusses changes.

Mention `@pulumi-neo` in a [pull request or issue](/docs/ai/integrations/github/) and Neo replies in the thread. Mention `@Neo` in a [Slack channel](/docs/ai/integrations/slack/) and Neo starts a [task](/docs/ai/tasks/), continuing the conversation as you reply.

<!--more-->

## Neo in GitHub

Mention `@pulumi-neo` in a pull request description, a top-level or inline review comment, or an issue. Neo sees the diff, the stacks linked to the repository, and their current state. Reviewers can ask Neo to walk through what a proposed change does, including resources that change in stacks the PR doesn't touch directly. Responses land in the same thread, so the analysis becomes part of the review record and any follow-up stays with it.

{{< video title="Delegating a GitHub issue to Neo" src="neo-github.mp4" autoplay="true" loop="true" controls="false" >}}

## Neo in Slack

Mention `@Neo` in any channel where Neo has been added, and Neo starts a task in the thread. The reply lands in the same thread, and follow-up messages continue the conversation there. The rest of the channel can see what was asked and what Neo found. Neo has the same capabilities here as in the Pulumi Cloud console or the terminal: check stack state, investigate failures, walk through what a change will do, or carry out actions the team has approved.

{{< video title="Tagging Neo for help with an issue in Slack" src="neo-slack.mp4" autoplay="true" loop="true" controls="false" >}}

## Integrations in action

A teammate posts in `#platform-engineering`: "API latency p95 has been climbing for two days, nobody can figure out why." You reply:

> **You:** @Neo check the production API stack. Anything change in the last 72 hours?

Neo starts a task in the thread, walks the stack history, and finds a configuration change to the load balancer's idle-timeout setting that landed Friday afternoon. It posts the change, who deployed it, and when. The rest of the channel sees the finding without you having to retell it.

> **You:** @Neo open a PR to revert idle-timeout to the previous value.

Neo edits the stack's Pulumi program, runs `pulumi preview` to confirm the change touches only the load balancer, and opens a pull request with the diff and the preview output. A reviewer pulls it up:

> **Reviewer:** @pulumi-neo what else does this change affect downstream?

Neo replies in the same review thread with the resources that change: the listener config and the target group health check. The reviewer reads, approves, and the change ships.

The investigation moved from Slack to GitHub, and both threads keep the record.

## Permissions and governance

Whether the conversation starts in GitHub or Slack, Neo runs with the [RBAC permissions](/docs/administration/access-identity/rbac/) of your Pulumi Cloud user. Stack-level controls, organization-level guardrails, and audit logging apply the same way they do for a task started from the console. Starting a conversation in a new place doesn't grant Neo new permissions; it just changes where the conversation happens.

## Try it out

Both integrations are available now for Neo-enabled organizations. The [GitHub integration docs](/docs/ai/integrations/github/) and [Slack integration docs](/docs/ai/integrations/slack/) cover the one-time setup. From there, every engineer with a linked Pulumi Cloud identity can mention Neo from the threads they already work in.

Today's launch is part of a [bigger story](/releases/agentic-infrastructure-era/). Read our launch-day piece on [the agentic infrastructure era](/blog/the-agentic-infrastructure-era/) for the broader vision, the [Neo CLI launch post](/blog/pulumi-neo-cli/) for Neo's new home in the terminal, and the [Neo Integrations post](/blog/neo-integrations/) for the MCP servers and cloud CLIs that ship with this release.

As always, we'd love to hear what you think — and if you have any suggestions for places we should put Neo next, file an issue in [pulumi-cloud-requests](https://github.com/pulumi/pulumi-cloud-requests/issues/new/choose).

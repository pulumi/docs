---
title: "Neo in Your Terminal"
date: 2026-05-12
draft: true
meta_desc: "Run pulumi neo from your project directory to start an interactive Neo session with access to your local files, shell, and Pulumi credentials."
authors:
    - neo-team
tags:
    - ai
    - ai-agents
    - features
    - pulumi-neo
    - pulumi-cli

social:
    twitter: |
        `pulumi neo` drops Neo into your terminal. It can read your Pulumi program, run previews, and iterate on changes with you. Ask it to investigate a failed preview, fix the issue, and verify the fix.
    linkedin: |
        Neo has been available in the Pulumi Cloud console, in GitHub PRs, and in Slack. Now it's in your terminal too.

        Run `pulumi neo` from your project directory and you get an interactive session where Neo can read your program, check stack state, run previews, and iterate on changes with you. Same agent, same context, but right where you're already working.
    bluesky: |
        `pulumi neo` is Neo in your terminal. Point it at a failed preview and it reads the error, checks your program, proposes a fix, and runs a new preview. Interactive, iterative, local.
---

[Pulumi Neo](/docs/ai/) is now in your terminal. Neo has been available in the Pulumi Cloud console, in [GitHub PRs](/blog/neo-github-slack/), and in [Slack](/blog/neo-github-slack/), and `pulumi neo` brings it to where you're actively writing code. Run the command from your project directory to start an interactive session where Neo can read and edit your Pulumi program, run previews, and use your existing Pulumi credentials.

<!--more-->

## What it looks like

You're working on a Pulumi program and a preview fails. You ask Neo what happened:

> **You:** That preview just failed. What went wrong?
>
> **Neo:** The preview failed because the `apiGateway` resource references a Lambda function ARN that doesn't exist yet. The function is defined in the program but depends on a role that's missing the `lambda:InvokeFunction` permission. I'll add the missing permission to the role and run a new preview.
>
> **Neo:** Preview succeeded. 3 resources to create, 1 to update. Ready to deploy when you are.

Because the session stays open, each follow-up builds on the last. Ask Neo to make further changes, verify them against a fresh preview, or walk through an unfamiliar stack without starting over.

## Plan mode

For quick investigations, Neo acts immediately. For larger changes where you want to review the approach first, press **Shift+Tab** before sending your first message to toggle plan mode. Neo investigates the task and produces a structured plan for you to approve or reject before execution begins. See [plan mode in the docs](/docs/ai/tasks/#plan-mode) for details.

## More than a coding assistant

Unlike a general-purpose AI coding tool, Neo has your Pulumi Cloud context: stack state, deployment history, and your organization's policies. When it investigates a failure, it reasons from what actually happened in your environment, not from generic documentation. And because it uses your existing [role-based access control (RBAC) permissions](/docs/administration/access-identity/rbac/), the console's access boundaries carry over to your terminal.

## Get started

- Authenticate to Pulumi Cloud with `pulumi login`
- Navigate to a directory containing a `Pulumi.yaml` file
- Run `pulumi neo`
- See the [`pulumi neo` docs](/docs/ai/pulumi-cli/) for details

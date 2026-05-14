---
title: Neo in the Pulumi CLI
title_tag: Neo in the Pulumi CLI
h1: Neo in the Pulumi CLI
meta_desc: Run pulumi neo to start an interactive Neo session in your terminal with access to your local project, credentials, and stacks.
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    ai:
        name: Pulumi CLI
        identifier: ai-pulumi-cli
        parent: ai-home
        weight: 15
---

`pulumi neo` is Neo in your terminal. Run the command from your project directory to start an interactive session that has access to your project files, your shell, and your Pulumi credentials.

## What you can do with `pulumi neo`

You can ask Neo to investigate a failed preview, make changes to your program and verify them against a fresh preview, read live stack state, or walk through what's happening in a stack you're unfamiliar with. The session is interactive, so follow-up messages refine the task in real time.

## Plan mode

Press **Shift+Tab** before sending your first message to toggle [plan mode](/docs/ai/tasks/#plan-mode). Neo investigates the task and produces a structured plan for you to approve or reject before it proceeds.

## How permissions work

`pulumi neo` uses your existing `pulumi login` and the [RBAC permissions](/docs/administration/access-identity/rbac/) of your Pulumi user.

## Requirements

- Authentication to Pulumi Cloud (`pulumi login`)

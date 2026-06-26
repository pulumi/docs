---
title: Neo in the Pulumi CLI
title_tag: Neo in the Pulumi CLI
h1: Neo in the Pulumi CLI
meta_desc: Run pulumi neo to start an interactive Neo session in your terminal with access to your local project, credentials, and stacks.
menu:
    ai:
        name: Pulumi CLI
        identifier: ai-pulumi-cli
        parent: ai-home
        weight: 15
---

`pulumi neo` is Neo in your terminal. Run the command from your project directory to start an interactive session.

## What local execution unlocks

Running locally means Neo inherits your setup: the CLIs you've authenticated, the environment variables and kubeconfigs you've configured, and the project you're editing. Neo can run the same commands you would, against the same systems you have access to, without any additional setup on your part.

You can ask Neo to investigate a failed preview, make changes to your program and verify them against a fresh preview, read live stack state, or walk through what's happening in a stack you're unfamiliar with. The session is interactive, so follow-up messages refine the task in real time.

## Controls

The controls you have in Pulumi Cloud apply in the terminal:

- **[Approval modes](/docs/ai/tasks/#task-modes)** (manual, balanced, auto) govern whether Neo asks before using tools
- **[Permission modes](/docs/ai/tasks/#task-modes)** (default, read-only) govern what Neo can change
- **[Plan mode](/docs/ai/tasks/#plan-mode)** lets Neo research and plan before executing (toggle with **Shift+Tab** before sending your first message)

## Integrations

[Integrations](/docs/ai/integrations/) carry over from Pulumi Cloud. GitHub, Slack, and the rest of the [integration catalog](/docs/ai/integrations/mcp/) work the same way from the terminal.

## Agent handoff

The [Neo handoff skill](https://github.com/pulumi/agent-skills/tree/main/delegation) lets other AI agents start a Neo task using `pulumi neo` under the hood. From Claude Code, Cursor, or any tool that supports agent skills, you can hand off infrastructure work to Neo without leaving your current session.

## How permissions work

`pulumi neo` uses your existing `pulumi login` and the [RBAC permissions](/docs/administration/access-identity/rbac/) of your Pulumi user. Identity, RBAC, and audit all run through your Pulumi Cloud login, the same way they do in the console.

## Get started

1. Authenticate to Pulumi Cloud with `pulumi login`
1. Run `pulumi neo` from a directory containing a `Pulumi.yaml` file

See the [`pulumi neo` command reference](/docs/iac/cli/commands/pulumi_neo/) for the full list of flags and options.

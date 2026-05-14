---
title: "Neo, Now in the Terminal"
date: 2026-05-13
draft: true
meta_desc: "Pulumi Neo runs as a CLI now. Over 4,500 organizations already delegate real infrastructure work to Neo; pulumi neo brings it to your terminal."
authors:
    - neo-team
meta_image: meta.png
feature_image: feature.png
tags:
    - ai
    - ai-agents
    - features
    - pulumi-neo
    - pulumi-cli

social:
    twitter: |
        Pulumi Neo runs as a CLI now. Over 4,500 orgs already delegate real infrastructure work to Neo: scaffolding, migrating, investigating, operationalizing. With pulumi neo, you can do it from the terminal where your tools and project already live.
    linkedin: |
        Pulumi Neo runs as a CLI now.

        Since launching Neo, over 4,500 organizations have used it to delegate real infrastructure work: scaffolding, migrating, investigating, operationalizing, and more. All of that has happened through Pulumi Cloud.

        A large portion of Pulumi users live in the terminal, and increasingly that's where AI tools run too. pulumi neo brings the same Neo experience into your terminal, with the same controls (approval modes, permission modes, Plan Mode) and the same governance through your Pulumi Cloud login. What's new is access to the tools, project, and environment you already have set up locally.
    bluesky: |
        Pulumi Neo runs as a CLI now. Over 4,500 orgs already delegate real infrastructure work to Neo; with pulumi neo, you can too, from the terminal where your tools and project already live.

        Same controls, same governance, with local access.
---

Since launching [Pulumi Neo](/blog/pulumi-neo/), over 4,500 organizations have used it to delegate real infrastructure work: scaffolding, migrating, investigating, operationalizing, and more. Though that usage has come entirely through Pulumi Cloud, we know a large portion of Pulumi users live in the terminal, and increasingly that's where AI tools run too. Now we're bringing Neo there.

`pulumi neo` brings the same Neo experience you've had in Pulumi Cloud to your terminal. Running locally means there's no separate branch to push, no credentials to provision, and no context to paste: Neo picks up the setup you already have.

![pulumi neo working through a Kubernetes cluster check, with Flux GitOps state verified and a TODO list in progress](tui.png)

<!--more-->

## What local execution unlocks

Neo inherits your setup when it runs locally. The CLIs you've authenticated, the environment variables and kubeconfigs you've configured, and the project you're editing right now are all available without any setup on your part. That means Neo can run the same commands you would, against the same systems you have access to.

The CLI also makes Neo reachable from other agent sessions. The [Neo handoff skill](https://github.com/pulumi/agent-skills/tree/main/delegation) takes the current thread (goal, repo pointers, conversation summary) and starts a Neo task using `pulumi neo` under the hood. From Claude Code, Cursor, or anywhere else that supports skills, you can launch Neo without leaving your current session.

## What carries over

Local tools and context are what's new. The full set of controls you have in Pulumi Cloud Neo applies in the terminal: approval modes (manual, balanced, auto) for tool calls, permission modes (default, read-only) for what Neo can change, [Plan Mode](/docs/ai/tasks/#plan-mode) for research and planning before execution, and task modes for Pulumi operations.

Integrations carry over too. GitHub, Slack, and the rest of the [integration catalog](/blog/neo-integration-catalog/) work the same way from the terminal. Identity, RBAC, and audit all run through your `pulumi login`, the same way they do in the console. See the [Pulumi Neo docs](/docs/ai/) for details.

## Get started

`pulumi neo` ships with the latest Pulumi CLI. To start a session:

1. Authenticate to Pulumi Cloud with `pulumi login`.
1. Run `pulumi neo`, or pass an initial prompt: `pulumi neo "what's in this stack?"`.

See the [`pulumi neo` command reference](/docs/iac/cli/commands/pulumi_neo/) and the [Pulumi Neo docs](/docs/ai/) for details. [10 things you can do with Neo](/blog/10-things-you-can-do-with-neo/) is a good starting point for tasks to try. The [Pulumi Community Slack](https://pulumi.com/slack/) is the place for questions and feedback.

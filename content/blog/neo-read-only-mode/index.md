---
title: "Introducing Read-Only Mode for Pulumi Neo"
date: 2026-03-18
draft: false
meta_desc: "Run Neo with confidence using read-only mode. Preview changes and create PRs without unwanted modifications to your infrastructure."
meta_image: meta.png
authors:
    - florian-stadler
tags:
    - pulumi-neo
    - ai
    - features
schema_type: auto

social:
    twitter:
    linkedin:
---

One of the most common questions we hear from teams evaluating Neo is: "How do I let Neo help without worrying about unintended changes?" Today, we're introducing read-only mode for Pulumi Neo, giving you a way to get value from Neo while keeping full control over what it can and cannot do.

<!--more-->

## Why read-only mode matters

Neo currently runs with the full permissions of the user who creates a task. That works well when you trust the outcome, but it can make teams hesitant to delegate work in sensitive environments. A platform engineer with broad access might want Neo to analyze infrastructure and suggest changes, but not actually apply them.

Read-only mode solves this by letting you cap Neo's permissions at task creation time. Neo can still read your infrastructure, run previews, and open pull requests, but it cannot deploy, update, or destroy resources. You get Neo's analysis and recommendations without the risk of unwanted modifications.

## How it works

When you create a Neo task, you now choose between two permission levels:

| Option | What Neo can do | Availability |
| :--- | :--- | :--- |
| **Use my permissions** | Full access (current default behavior) | All tiers |
| **Read-only** | Read, preview, and create PRs. No infrastructure mutations. | All tiers |

Read-only mode takes your existing permissions and removes the ability to make changes. Neo never gets more access than you have, only less. If you can view a stack but not a particular environment, Neo in read-only mode also cannot see that environment.

## What Neo can do in read-only mode

Read-only mode does not mean Neo becomes passive. Neo can still read your infrastructure state, run previews, write and refactor code, create branches, and open pull requests. It does the same work it always does, and hands off the result to your regular deployment process. The only difference is that Neo cannot trigger deployments or other write operations in Pulumi Cloud directly.

## Read-only mode and auto-approve

Neo's [operating modes](/docs/ai/) let you choose how much oversight you want: review mode for full approval at each step, balanced mode for approving only mutating operations, and auto mode for hands-off execution.

Read-only mode pairs well with auto-approve. Because Neo cannot perform write operations like deployments or destroys, you can let it run autonomously and trust that the output is a pull request, not a production change. Kick off a task, let Neo work in the background, and come back to a ready-to-review PR.

## Set defaults and enforce guardrails

You can configure your default permission level in your user settings so you do not have to choose every time you create a task. If you prefer to always start in read-only mode, set it once and override on a per-task basis when needed.

## Getting started

Read-only mode is available today for all Pulumi Cloud users.

- [Sign in to Pulumi Cloud](https://app.pulumi.com/signin) and select **Read-only** when creating your next Neo task
- [Read the Neo documentation](/docs/ai/) for detailed guides on permission levels
- [Join the Community Slack](https://slack.pulumi.com/) to share your feedback

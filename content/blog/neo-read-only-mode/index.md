---
title: "Introducing Read-Only Mode for Pulumi Neo"
date: 2026-03-18
draft: false
meta_desc: "Run Neo with confidence using read-only mode. Preview changes and create PRs without unwanted modifications to your infrastructure."
meta_image: meta.png
feature_image: feature.png
authors:
    - florian-stadler
tags:
    - pulumi-neo
    - ai
    - features
schema_type: auto

social:
    twitter: "Pulumi Neo now has read-only mode. Let Neo analyze your infrastructure, run previews, and open PRs without the risk of unwanted changes."
    linkedin: "Introducing read-only mode for Pulumi Neo. Teams told us they wanted Neo's analysis and recommendations without the risk of unintended infrastructure changes. Now when creating a Neo task, you can choose read-only mode to cap permissions. Neo can still read state, run previews, write code, and open PRs, but it cannot deploy, update, or destroy resources."
---

Platform teams want control over how much autonomy Neo has. With read-only mode, Neo does the heavy lifting and hands off a pull request. Your CI/CD pipeline takes it from there.

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

Neo's [operating modes](/docs/ai/tasks/#task-modes) let you choose how much oversight you want: review mode for full approval at each step, balanced mode for approving only mutating operations, and auto mode for hands-off execution.

Read-only mode pairs well with auto-approve. Because Neo cannot perform write operations like deployments or destroys, you can let it run autonomously and trust that the output is a pull request, not a production change. Kick off a task, let Neo work in the background, and come back to a ready-to-review PR.

## Getting started

Read-only mode is available today for all Pulumi Cloud users.

- [Sign in to Pulumi Cloud](https://app.pulumi.com/signin) and select **Read-only** when creating your next Neo task
- [Read the Neo documentation](/docs/ai/) for detailed guides on permission levels
- [Join the Community Slack](https://slack.pulumi.com/) to share your feedback

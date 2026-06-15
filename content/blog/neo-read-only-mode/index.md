---
title: "Introducing Read-Only Mode for Pulumi Neo"
date: 2026-04-01
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
categories:
    - agentic-infrastructure
schema_type: auto

social:
    twitter: "Pulumi Neo now has read-only mode. Run Neo with confidence knowing it can preview changes and create PRs without modifying your infrastructure."
    linkedin: "Introducing read-only mode for Pulumi Neo. Run Neo with confidence knowing it can analyze your infrastructure, run previews, and open pull requests without making unwanted modifications. Control how much autonomy Neo has on a per-task basis."
    bluesky: "Pulumi Neo now has read-only mode. Preview changes and create PRs without modifying your infrastructure."
---

A platform engineer with broad access might want Neo to analyze infrastructure and suggest changes, but include guarantees it won't actually apply them. Read-only mode makes that possible: Neo does the heavy lifting and hands off a pull request for your existing deployment process to pick up.

<!--more-->

## Control what Neo can change

Neo runs with the permissions of the user who creates a task, but you often want a tighter boundary. Read-only mode solves this by letting you cap Neo's permissions at task creation time. Neo can still read your infrastructure, run previews, and open pull requests, but it cannot deploy, update, or destroy resources.

## How it works

When you create a Neo task, you now choose between two permission levels:

| Option | What Neo can do | Availability |
| :--- | :--- | :--- |
| **Use my permissions** | Full access (current default behavior) | All tiers |
| **Read-only** | Read, preview, and create PRs. No infrastructure mutations. | All tiers |

Read-only mode takes your existing permissions and removes the ability to make changes. Neo remains fully active, meaning it can still read your infrastructure state, run previews, write and refactor code, create branches, and open pull requests. If Neo encounters an operation it can't perform in read-only mode, the operation fails and Neo reports what it would have done. The only difference is that Neo cannot trigger deployments or other write operations in Pulumi Cloud directly.

## Read-only mode and auto-approve

Neo's [operating modes](/docs/ai/tasks/#task-modes) let you choose how much oversight you want: review mode for full approval at each step, balanced mode for approving only mutating operations, and auto mode for hands-off execution.

Read-only mode pairs well with auto-approve. Because Neo cannot perform write operations like deployments or destroys, you can let it run autonomously and trust that the output is a pull request, not a production change. Kick off a task, let Neo work in the background, and come back to a ready-to-review PR.

## Getting started

Read-only mode is available today for all Pulumi Cloud users.

- [Sign in to Pulumi Cloud](https://app.pulumi.com/signin) and select **Read-only** when creating your next Neo task
- [Read the Neo documentation](/docs/ai/) for detailed guides on permission levels
- [Join the Community Slack](https://slack.pulumi.com/) to share your feedback

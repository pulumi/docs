---
title: "Turn Any Neo Task Into Recurring Work"
date: 2026-05-12
draft: true
meta_desc: "Schedule Neo tasks to run on a cadence and deliver results as pull requests. Drift detection, compliance scans, and dependency checks on autopilot."
authors:
    - neo-team
tags:
    - ai
    - ai-agents
    - features
    - pulumi-neo
    - automation

social:
    twitter: |
        Neo can now run on a schedule. Define a prompt, pick a cadence, and Neo delivers a pull request each time.

        Drift detection, compliance scans, and cost reviews: recurring work that teams routinely defer.
    linkedin: |
        Drift detection, compliance scans, dependency freshness checks. This is recurring work that teams routinely defer because it's tedious to do by hand.

        Neo automations let you schedule any Neo task to run on a cadence. Each run produces a pull request that goes through your normal review process. Same governance, no manual effort.
    bluesky: |
        Neo can now run on a schedule. Define a prompt, pick a cadence, and Neo delivers a PR each time it runs.

        Drift detection, compliance scans, and cost reviews, all on autopilot.
---

[Pulumi Neo](/docs/ai/) automations schedule any task to run on a cadence, producing a pull request each time that goes through your normal review process. Drift detection, compliance scans, and dependency freshness checks run on schedule without anyone remembering to kick them off.

<!--more-->

## How automations work

An automation is a prompt, a cadence, and a set of defaults. You define what you want Neo to do, choose how often (hourly, daily, weekdays, or weekly), and Neo runs the task at each interval. Every run produces a pull request, so the results go through the same branch protection rules and required reviewers as any other change.

Automations default to [auto mode](/docs/ai/tasks/#task-modes), meaning Neo proceeds through each step without waiting for your approval. They also default to read-only permissions, meaning Neo can read stack state and propose changes through pull requests but can't deploy directly to your infrastructure. You can override both defaults per automation.

## Neo in action

You create an automation called "Weekly encryption audit" with this prompt:

> Check all S3 buckets and RDS instances across our production stacks. Flag any that don't have encryption at rest enabled. Open a PR that adds encryption where it's missing.

Neo runs it every Monday morning. If it finds unencrypted resources, you get a pull request that adds `serverSideEncryption` configuration to the S3 bucket definitions and `storageEncrypted: true` to the RDS instances in your Pulumi program. If everything is clean, Neo reports that nothing needed updating. Either way, you have a record.

## Templates and custom prompts

Templates for common tasks like encryption audits and provider freshness checks give you a starting prompt to customize, or you can write your own from scratch. [Custom Instructions](/docs/ai/settings/), which are organization- or project-level directives you define in Pulumi Cloud, apply to scheduled tasks the same way they apply to interactive ones, so org-wide conventions carry over automatically.

Automations also inherit the organization's [MCP integrations](/docs/ai/integrations/mcp/) and [CLI integrations](/docs/ai/integrations/cli/), so a scheduled task can query Datadog metrics or check AWS resources just like an interactive one.

## Permissions and governance

A scheduled task runs with the [role-based access control (RBAC) permissions](/docs/administration/access-identity/rbac/) of the user who created it, evaluated at execution time. If that user's permissions change between scheduling and execution, Neo uses the updated permissions. The combination of read-only defaults and pull-request output means automations produce proposals, not production changes.

## Get started

- [Create your first automation](/docs/ai/automations/) from the Neo Automations tab
- [Read about task modes](/docs/ai/tasks/#task-modes) to understand the auto and read-only defaults
- [Set up CLI integrations](/docs/ai/integrations/cli/) if your automations need to query cloud infrastructure directly

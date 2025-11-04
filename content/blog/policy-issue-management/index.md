---
title: "Introducing the New Policy Findings Hub"
date: 2025-11-05
authors:
  - alejandro-cotroneo
  - arun-loganathan
meta_desc: "Move from alert fatigue to action. Announcing Pulumi's new Policy Findings hub, a collaborative workspace for triaging, managing, and fixing compliance issues."
allow_long_title: true
meta_image: "meta.png"
tags:
  - pulumi-service
  - policy-as-code
  - features
  - compliance
  - governance
  - pulumi-neo
  - ai
---

For platform and security teams, enabling robust cloud scanning often creates a new problem: an unmanageable firehose of policy alerts. Identifying a violation is only the first step. Without a system to manage the lifecycle of these findings, teams are quickly overwhelmed, leading to prioritization paralysis and a perpetually growing backlog.

Today, we're introducing the solution to this alert fatigue. The new **Policy Findings** hub is a purpose-built, collaborative workspace that transforms a noisy list of violations into an organized and actionable set of tasks. It guides your team from initial discovery all the way to a verified fix.

<!--more-->

## From Raw Data to Actionable Insights

The Policy Findings hub is designed with distinct views for every stakeholder involved in the governance lifecycle.

### 1. The Overview Tab: A Dashboard for Leaders

For a platform lead or security manager, the goal is to understand the big picture. The Overview tab provides a high-level dashboard of your organization's compliance health, answering key questions at a glance:

* What is our overall resource compliance score?
* Are we trending in the right direction?
* Which parts of our cloud infrastructure (stacks, accounts, etc.) carry the most risk?

This view helps leadership track progress and make data-driven decisions about where to focus engineering efforts.

### 2. The Compliance Tab: The Auditor and Infosec Workspace

For the infosec members and auditors, context is everything. Simply listing thousands of violations is not helpful. The Compliance tab provides a policy-centric view, grouping all findings by the specific control they violated (e.g., a specific rule within CIS or NIST).

This is crucial when preparing for an audit or assessing adherence to a specific security framework, as it allows you to see exactly where you are compliant and where you have gaps, control by control.

### 3. The Issues Tab: The Team's Daily Workspace

This is space where insight is turned into action. The Issues tab is a collaborative triage board designed for the day-to-day workflow of platform and development teams. It provides the full toolset needed to manage the lifecycle of an issue from start to finish:

* **Triage and Prioritize:** Filter issues by severity, resource type, or policy to focus on what matters most. Set a priority level from P0 (critical) to P4 (low).
* **Assign Ownership:** Assign issues to specific team members to ensure clear ownership and accountability.
* **Manage Lifecycle:** Mark an issue as "Ignored" with a justification. This is a critical workflow for acknowledging intentional exceptions, which cleans up your dashboard and allows the team to focus on legitimate issues.

And for the most critical part of the workflow—the fix itself—we've integrated our AI agent, **Pulumi Neo**, directly into this view.

After selecting one or more issues, your team can assign the task to Neo. It will analyze the violations and automatically generate a pull request with the necessary code changes. For unmanaged resources, Neo will even generate the code to import them into Pulumi and apply the fix. This turns a complex manual task into a simple review-and-merge process, allowing your team to finally burn down the backlog.

{{< video title="Managing policy findings in Pulumi Cloud" src="findingsclipblog.mp4" autoplay="false" controls="true" loop="true" >}}

## Conclusion

Effective governance requires more than just detection; it requires a robust system for managing, prioritizing, and resolving issues at scale. The new Policy Findings hub provides that end-to-end experience. It's a collaborative environment that brings clarity to your compliance posture and provides the tools—including AI-powered assistance—to take decisive action.

This powerful new experience is available today. Navigate to the **Policies > Findings** tab in the Pulumi Cloud to explore your new compliance dashboard and transform alert fatigue into action.

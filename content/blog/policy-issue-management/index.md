---
title: "Introducing the New Policy Findings Hub"
date: 2025-11-05T00:03:00
authors:
  - alejandro-cotroneo
  - arun-loganathan
meta_desc: "Move from alert fatigue to action. Announcing Pulumi's new Policy Findings hub, a collaborative workspace for triaging, managing, and fixing compliance issues."
allow_long_title: true
meta_image: "meta.png"
tags:
  - pulumi-service
  - policy-as-code
  - audit-policies
  - compliance
  - governance
  - pulumi-neo
  - infosec
---

For platform and security teams, enabling robust cloud scanning often creates a new problem: an unmanageable firehose of policy alerts. Identifying a violation is only the first step. Without a system to manage the lifecycle of these findings, teams are quickly overwhelmed, leading to prioritization paralysis and a perpetually growing backlog.

Today, we're introducing the solution to this alert fatigue. The new **[Policy Findings](https://www.pulumi.com/docs/insights/policy/policy-findings/)** hub is a purpose-built, collaborative workspace that transforms a noisy list of violations into an organized and actionable set of tasks. It guides your team from initial discovery all the way to a verified fix.

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

This is crucial when preparing for an audit or assessing adherence to a specific security framework, as it allows you to [see exactly where you are compliant and where you have gaps](https://www.pulumi.com/blog/policy-packs-cis-nist-pci/#more-than-just-detection-the-complete-governance-lifecycle), control by control.

### 3. The Issues Tab: The Team's Daily Workspace

This is the space where insight is turned into action. The Issues tab is a collaborative triage board designed for the day-to-day workflow of platform and development teams. It provides the full toolset needed to manage the lifecycle of an issue from start to finish:

* **Triage and Prioritize:** Filter issues by severity, resource type, or policy to focus on what matters most. Set a priority level from P0 (critical) to P4 (low).
* **Assign Ownership:** Assign issues to specific team members to ensure clear ownership and accountability.
* **Manage Lifecycle:** Mark an issue as "Ignored" with a justification. This is a critical workflow for acknowledging intentional exceptions, which cleans up your dashboard and allows the team to focus on legitimate issues.

And for the most critical part of the workflow — the fix itself — we've integrated our AI agent, **[Pulumi Neo](https://www.pulumi.com/product/neo/#video)**, directly into this view.

After selecting one or more issues, your team can assign the task to Neo. It will analyze the violations and automatically generate a pull request with the necessary code changes. For unmanaged resources, Neo will even generate the code to import them into Pulumi and apply the fix. This turns a complex manual task into a simple review-and-merge process, allowing your team to finally burn down the backlog.

{{< video title="Managing policy findings in Pulumi Cloud" src="findingsclipblog.mp4" autoplay="false" controls="true" loop="true" >}}

## Turning Alerts into Action

Effective governance goes beyond identifying violations. It requires a structured system that turns every finding into a clear and trackable path to resolution. The new Policy Findings hub provides that end-to-end workflow, from visibility to accountability to automated remediation.

By organizing policy data into meaningful views and integrating Pulumi Neo directly into the issue management process, teams can move past alert fatigue and focus on what matters most: fixing problems quickly and maintaining continuous compliance.

This new experience is available today. Navigate to the **Policies > Findings** tab in the Pulumi Cloud to explore your new compliance dashboard and start turning alerts into action.

## Try Pulumi Policies

**Ready to try these features?**

* [Sign up for Pulumi Cloud](https://app.pulumi.com/signup) and start a Neo task  
* [Read the Get Started guide](/docs/insights/policy/get-started/) to manage compliance across your cloud infrastructure
* [Join the Community Slack](https://slack.pulumi.com/) to share feedback on the new features

For complete documentation, visit our [Policies documentation](https://www.pulumi.com/docs/insights/policy/).

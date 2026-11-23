---
title: "New Pulumi Best Practices posture report"
date: 2026-11-30
draft: false
meta_desc: "The infrastructure posture report checks every IaC-managed stack against Pulumi Best Practices each month and shows where your risks are. Enable in one click."
feature_image: feature.png
authors:
    - tatiana-cooke
    - tom-king
tags:
    - policy-as-code
    - governance
    - security
    - pulumi-cloud
    - features
category: product
schema_type: auto
canonical_url: "https://www.pulumi.com/docs/discovery-governance/operations/posture-report/"
related_posts:
    - policy-exceptions
    - deployment-guardrails-with-policy-as-code
    - policy-issue-management
resource_links:
    - type: documentation
      url: /docs/discovery-governance/operations/posture-report/
      text: "Infrastructure posture report documentation"
    - type: slack
      url: https://slack.pulumi.com/

# Social media copy — auto-posted to X, LinkedIn, and Bluesky when merged to master.
# Character limits: X ~280, Bluesky 300, LinkedIn 3000. Leave blank to skip a platform.
social:
    twitter: |
        How does your infrastructure measure up against Pulumi Best Practices?

        The new infrastructure posture report checks every stack in your organization once a month and shows where the risks are. Enable now to understand more about possible risks.
    linkedin: |
        Teams often ask us how their infrastructure measures up against Pulumi's best practices. We've made it even easier to scan your infrastructure for risk with a simple configuration flow for this posture report.

        If you opt in, once a month Pulumi Cloud scans the latest state of every stack in your organization against the Pulumi Best Practices policy packs for AWS, Azure, and Google Cloud. The report shows findings by severity, the share of your resources impacted by these findings, and which issues affect the most resources.

        The scan is read-only and needs no new credentials. An organization admin turns it on with one click in the Pulumi Cloud console.

        It's available now in the Pro and Enterprise editions. Here's what the report covers and how to go from a monthly snapshot to continuous monitoring.
    bluesky: |
        How does your infrastructure measure up against Pulumi Best Practices?

        The new infrastructure posture report checks every stack in your organization once a month and shows where the risks are. Enable now to understand more about possible risks.
---

Pulumi IaC lets you define your cloud resources in code, and [Pulumi Policies](/docs/discovery-governance/concepts/policy-as-code/) checks those resources against policy as code, so you can see where your security and compliance stand. Today we're adding the infrastructure posture report: a monthly snapshot of how every stack in your organization measures up against the Pulumi Best Practices policy packs. An organization admin turns it on with one click in the Pulumi Cloud console, and it's available in the Pro and Enterprise editions.

<!--more-->

## Why a posture report?

Teams often ask us some version of the same question: how does our infrastructure measure up against Pulumi's best practices?

Until now, getting an answer took some setup. You chose policy packs, created a policy group, added stacks to it, and waited for the evaluations to run. That's the right path once you're ready to enforce policy, but it's a lot to ask when all you want is to know where you stand. The posture report gives you that answer before you've configured anything.

## What does the report check?

Once a month, Pulumi Cloud scans the latest state of every stack in your organization against the [Pulumi Best Practices](/docs/discovery-governance/guides/pre-built-policy-packs/) policy packs for AWS, Azure, and Google Cloud. You don't need to add the packs to a policy group first.

The scan is read-only. It changes nothing in your infrastructure or your stacks, and it uses no new credentials.

Two limits are worth knowing up front. The report covers resources managed in Pulumi stacks, so it doesn't include discovered resources that Pulumi IaC doesn't manage yet. And it summarizes policy findings against Pulumi's own best practices, which makes it a starting point for a conversation about risk and not a compliance audit.

## What's in the report?

Each report opens with what the scan covered: the stacks and resources it evaluated, and any stacks it couldn't evaluate. From there, it answers three questions:

- **How many findings are there, and how serious are they?** A finding is one resource failing one policy. The report counts findings by severity.
- **How much of your infrastructure is in good shape?** Coverage is the percentage of evaluated resources with no findings.
- **Where should you start?** Top issues group findings by policy and resource family, such as every `aws:s3` resource that fails the same policy. Groups are ranked by severity, then by how many resources they affect.

Each report is a snapshot. It doesn't change as you resolve findings, and from your second report on, you can see what changed since the month before. Past reports are kept for a year, and you can export any report as a CSV or a PDF to share with people who don't sign in to Pulumi Cloud.

## How do you turn it on?

Nothing is scanned until you opt in. To turn on the report:

1. Navigate to **Governance** > **Posture report** in the Pulumi Cloud console.
1. Review the preview, which shows how many stacks the scan covers and which packs it checks them against.
1. Select **Turn on**.

The first scan starts right away, and the report appears on the page when it finishes. After that, a new report arrives by the 1st of every month, and admins are notified in the console and by email when it's ready.

Organization admins turn the report on and off, and turning it on is recorded in your [audit logs](/docs/administration/concepts/audit-logs/). Once it's on, members who can already read policy results, stacks, and cloud accounts across the organization can see it. If the report isn't for you, an admin can turn it off at any time from the same page.

## How do you go from a monthly snapshot to continuous monitoring?

A monthly report tells you where you stand. It doesn't tell you when something new goes wrong on a Tuesday.

When you want that, select **Enable monitoring** on the report. This creates a Pulumi Best Practices audit [policy group](/docs/discovery-governance/concepts/policy-as-code/policy-groups/) that evaluates every stack against the same packs as your stacks are updated. Audit policy groups never block deployments. Findings appear in [policy findings](/docs/discovery-governance/operations/policy-findings/), where you can assign and resolve them, or hand a group of them to Pulumi Neo to draft a fix.

From there, you can go further at your own pace: move the policies that matter most into a preventative policy group so violations are stopped before they deploy, and use [policy exceptions](/blog/policy-exceptions/) for the resources that have a good reason to break a rule.

## Next steps

The infrastructure posture report is available now in the Pro and Enterprise editions of Pulumi Cloud, with no extra charge for the monthly scan.

- Turn it on from **Governance** > **Posture report** in the [Pulumi Cloud console](https://app.pulumi.com/).
- Read the [infrastructure posture report documentation](/docs/discovery-governance/operations/posture-report/) for how the numbers are calculated, who can see the report, and how to export it.
- Tell us what you'd like the report to cover next in the [Pulumi Community Slack](https://slack.pulumi.com/) or on [GitHub](https://github.com/pulumi/pulumi-cloud-requests/issues).

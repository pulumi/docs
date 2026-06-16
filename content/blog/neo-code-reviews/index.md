---
title: "Neo Code Reviews: AI code review built for infrastructure"
date: 2026-06-17T08:00:00-07:00
meta_desc: "Neo Code Reviews analyzes a pull request against what Pulumi Cloud knows about your running infrastructure and leaves its feedback right in the PR."
meta_image: meta.png
feature_image: feature.png
authors:
    - neo-team
tags:
    - ai
    - ai-agents
    - features
    - pulumi-neo

social:
    twitter: |
        A one-line edit to a database property. The diff says it's safe to approve.

        Run the preview and that line replaces your production database. Pulumi Neo Code Reviews reads the preview and flags it on the PR. Now in public preview on GitHub.
    linkedin: |
        A pull request changes one property on a production database. On GitHub the diff is a single edited line, and it looks safe to approve.

        Run the preview and the picture changes. That property can't be changed in place, so Pulumi will replace the database: destroy the running instance, create a new one with a new endpoint. The diff never showed it.

        The consequences of an infrastructure change aren't in the lines that changed; they're in what the change does to the running system.

        Pulumi Neo Code Reviews reads the preview output and leaves its feedback right on the pull request, down to the line. Now in public preview on GitHub.
    bluesky: |
        A one-line diff that quietly replaces your production database.

        The diff can't see it. The preview can. Neo Code Reviews reads the preview and leaves its feedback right on the PR, down to the line. Public preview on GitHub now.
---

Today we are introducing [Pulumi Neo Code Reviews](/docs/ai/code-reviews/), now in public preview. Neo Code Reviews analyzes pull request changes in conjunction with what Pulumi Cloud knows about your running infrastructure, providing both high-level and code-level feedback.

<!--more-->

Normal code review agents are effectively guessing at the impact an IaC change will have. This is because they do not have access to critical aspects of the IaC workflow: the potential impact the update will have, in this case the `pulumi preview` output; and the current state of the cloud infrastructure. Neo not only has access to both of those, but also to the entirety of your other cloud context, such as stack relationships and dependencies.

## Running reviews

Neo can review every pull request automatically, or only when someone mentions `@pulumi-neo`. Either way, it skips draft pull requests and those opened by bots by default.

A review is a comment, so it informs the person approving the merge and sits alongside the required checks and branch protection you already enforce. Neo Code Reviews runs inside the same governance as every other Neo task, with the [RBAC](/docs/administration/access-identity/rbac/), guardrails, and audit logging your organization has set.

## Enable code reviews

Neo Code Reviews is available on GitHub during public preview. It needs Pulumi Neo enabled for your organization, the [Pulumi GitHub App](/docs/integrations/version-control/github-app/) installed on the repositories you want reviewed, and each user to grant Pulumi access to their GitHub account once under **Management** > **Version control**. If Neo already posts preview summaries on your pull requests, Code Reviews is on, and its review takes the place of those summaries.

Neo Code Reviews is free while it is in public preview. On July 1, 2026, it becomes generally available, and reviews begin counting toward your organization's Neo token usage at the same per-token rate as any other Neo task. The [pricing page](/pricing/) shows that rate and the monthly token allotment included with each plan.

## Give it a try

Open a pull request against a stack Pulumi manages and see Neo's review. We want to hear what it catches and what it misses, so hop into the [Pulumi Community Slack](https://slack.pulumi.com/) and tell us.

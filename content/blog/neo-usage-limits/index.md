---
title: "Introducing Usage Limits for Pulumi Neo"
date: 2026-07-13T08:00:00-07:00
draft: true
meta_desc: "Pulumi Neo usage limits set a dollar boundary on monthly Neo spend. Neo pauses when it reaches your organization or per-member limit, with email alerts."
feature_image: feature.png
authors:
    - john-keiser
tags:
    - pulumi-neo
    - ai
    - ai-agents
    - features
category: product
schema_type: auto

# canonical_url: set to /docs/ai/usage-limits/ once that docs page is live (not merged yet).

social:
    twitter: "Pulumi Neo now supports usage limits. Set a dollar limit on Neo's monthly spend and it pauses when that's reached, with email alerts along the way."
    linkedin: "Introducing usage limits for Pulumi Neo. Set a monthly dollar limit for your organization or individual members, and Neo pauses when spend reaches it. Email alerts land at 50%, 80%, 95%, and 100%."
    bluesky: "Pulumi Neo now supports usage limits. Set a dollar limit on Neo's monthly spend; it pauses when it reaches the limit, and emails you along the way."
---

The more infrastructure work you hand [Pulumi Neo](/docs/ai/), the more its usage grows. Usage limits let you set a monthly dollar limit on that usage, so Neo pauses when your organization reaches the limit instead of running past it.

<!--more-->

## How usage limits work

Your organization limit is a single monthly dollar amount covering all Neo usage across the org. You set it in Pulumi Cloud. When usage reaches the limit, Neo pauses for the rest of the billing period and resumes automatically at the start of the next one. An Admin or Billing Manager can raise the limit to resume before then.

![The Manage token usage panel, where an admin sets the organization's monthly Neo limit and turns on email notifications.](manage-token-usage.png)

Enforcement happens at a natural boundary in Neo's work, so a task already in progress finishes its current step before pausing. A limit can therefore land a few dollars over, which is expected rather than a billing error.

## Per-member limits and alerts

You can also set separate limits for each individual member, which pauses Neo for them after they hit the limit, without affecting others. (The organization limit still applies, no matter what.)

![The per-member limits table, showing each member's amount used and effective limit for the billing period.](per-member-limits.png)

Turn on **Enable email notifications** to get a heads-up before you reach the limit. Billing admins are alerted at 50%, 80%, and 95% of the organization limit, with a final notice at 100% when Neo pauses.

## Get started

Neo usage limits are available today for organizations on a paid plan, and an **Admin** or **Billing Manager** can set them.

- [Sign in to Pulumi Cloud](https://app.pulumi.com/signin) and set your first organization limit
- [Read the Neo usage limits documentation](/docs/ai/usage-limits/) for per-member limits, alerts, and enforcement details
- [Join the Community Slack](https://slack.pulumi.com/) to share your feedback

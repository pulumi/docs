---
title: "Set Spending Limits for Pulumi Neo"
date: 2026-07-10T08:00:00-07:00
draft: true
meta_desc: "Give Neo a budget. Set a monthly dollar limit on Neo usage for your organization or per member, with email alerts as you approach it."
feature_image: feature.png
# NOTE (John): authors defaults to neo-team. Swap to `john-keiser` (or add yourself)
# if you'd rather own this one — the feature is yours.
authors:
    - neo-team
tags:
    - pulumi-neo
    - ai
    - ai-agents
    - features
category: product

social:
    twitter: |
        Pulumi Neo now has usage limits. Set a monthly dollar cap for your org or per member, get email alerts as usage climbs, and Neo pauses at 100% until the next billing period. Predictable spend for autonomous agents.
    linkedin: |
        **Set Spending Limits for Pulumi Neo**

        Agentic infrastructure work is powerful, but autonomous spend is hard to predict, and teams want a guardrail before they let an agent run on its own.

        Pulumi Neo now supports usage limits. Org admins set a monthly dollar cap on Neo usage for the whole organization, and optionally a separate cap per member. Email alerts land at 50%, 80%, 95%, and 100% as usage climbs, and Neo pauses when a limit is reached until the next billing period or until an admin raises it.

        Set it once in Pulumi Cloud, then let Neo work with confidence that spend stays inside the boundary you chose. Available now for organizations on a paid plan.
    bluesky: |
        Pulumi Neo now has usage limits. Set a monthly dollar cap for your org or per member, get email alerts as usage climbs, and Neo pauses at the limit until next billing period.
---

Handing infrastructure work to an autonomous agent is powerful, but agent spend is hard to predict, and most teams want a guardrail in place before they let Neo run on its own. Usage limits give you that guardrail: set a monthly budget once, and Neo stays inside it.

<!--more-->

## Give Neo a budget

Usage limits let an organization admin put a monthly dollar cap on Neo usage. You can set one limit for the whole organization, and optionally a separate limit for each member.

A member's effective limit is whichever is smaller: their per-member limit or the organization limit. So a generous individual cap never lets one person spend past the organization's total, and the organization cap acts as the ceiling for everyone.

Setting limits is an admin task. Anyone with the **Admin** or **Billing Manager** role can configure them; members see their usage but don't set the caps.

## Alerts as you approach, a pause at the limit

You don't have to watch a dashboard to stay ahead of the budget. As usage climbs, Neo emails your admins at **50%**, **80%**, **95%**, and **100%** of a limit, so there's time to react before anything stops.

When usage reaches 100%, Neo pauses. If the organization limit is hit, Neo pauses for the whole organization; if a member's limit is hit, it pauses just for that member. Work resumes automatically at the start of the next billing period, or as soon as an admin raises the limit.

The result is a predictable boundary. Enforcement happens at the edge of each Neo turn, so a limit is a dependable stopping point rather than a surprise on your next invoice.

## Get started

Usage limits are available now for organizations on a paid Pulumi plan.

- [Open Pulumi Cloud](https://app.pulumi.com/) and navigate to **Settings → Billing & usage → Neo token usage** to set your first limit
- [Read the usage limits documentation](/docs/ai/usage-limits/) for the full walkthrough
- [Explore Pulumi Neo](/docs/ai/) to see everything Neo can do
- [Join the Community Slack](https://slack.pulumi.com/) to share your feedback

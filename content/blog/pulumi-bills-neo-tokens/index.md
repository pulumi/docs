---
title: "Introducing Pulumi Bills and Neo Tokens: Simplified Billing for a Growing Platform"
date: 2026-05-08
draft: false
meta_desc: "Pulumi Bills unifies billing across all Pulumi capabilities with a single currency, and Neo Tokens bring transparent pricing to AI-powered infrastructure features."
meta_image: meta.png
authors:
    - meagan-cojocar
tags:
    - announcements
    - pulumi-neo
    - platform-engineering

social:
    twitter: "Introducing Pulumi Bills and Neo Tokens: one unified billing currency for IaC, ESC, Deployments, Insights, and Neo. 1 Pulumi Bill = $1 USD. Neo Tokens priced at $3/MTok. Changes effective June 1, 2026."
    linkedin: "We're simplifying how Pulumi billing works. Pulumi Bills gives you one unified currency across the entire platform — IaC, ESC, Deployments, Insights, and Neo all draw from the same pool. No more guessing fixed allocations per product or separate procurement for each new capability. Neo Tokens bring transparent, predictable pricing to AI-powered infrastructure features at $3 per million tokens. Changes are effective June 1, 2026."
---

Today, we're announcing an updated metering and billing approach to simplify purchasing and support Pulumi Neo usage. The goal of this change is straightforward: we want the billing model to get out of the way so you can adopt new capabilities when they're useful to you. These changes will be effective June 1, 2026.

Since we launched our consumption-based billing model for Pulumi IaC 5 years ago, our goal has been the same: let teams pay for what they use either monthly on a credit card or with right-sized agreements for our invoiced customers. Since then, our product portfolio has expanded significantly: Pulumi ESC, Pulumi Deployments, Pulumi Insights, and now Pulumi Neo. With these changes, billing has grown more complex. Teams managing multi-year contracts would find themselves pre-purchasing specific quantities of resource-hours, secret-hours, and workflow-minutes, then having to reconfigure those contracts to adopt a new product capability mid-term.

We're introducing two changes that address this directly: **Pulumi Bills** as a unified billing currency across all of Pulumi capabilities and **Neo Tokens** as the meter for LLM-powered features.

<!--more-->

## The Problem We're Solving

Under the previous model, adopting a new Pulumi capability during an existing contract often meant separate procurement processes. A team mid-way through a three-year agreement that wanted to start using Pulumi ESC without pre-purchased secret-hours would be billed in arrears monthly for that usage, even if they had unused budget allocated to other features. Self-serve customers faced a similar problem where the fixed allocation of resource-hours and secret-hours might not fit their specific needs.

## Pulumi Bills: One Currency for the Whole Platform

**One Pulumi Bill = $1 USD.**

Rather than pre-purchasing fixed quantities for each individual feature, customers can pre-purchase a pool of Pulumi Bills and let all usage draw from that pool. Resource-hours, secret-hours, workflow-minutes, Neo Tokens all draw from the same balance of Pulumi Bills. Once the pool is exhausted, additional usage is billed in arrears.

This means:

- **No more guessing specific service volumes upfront.** Buy what you expect to spend in total, not fixed allocations per product.
- **Start using new features immediately.** IaC, Neo, ESC, Deployments, Insights and future capabilities all draw from the same pool.
- **Volume pricing still applies.** Customers on annual and multi-year agreements can still save based on their overall commitment amount.

### For self-serve credit card customers

Your monthly upfront fee transitions from covering a fixed number of resource-hours, secret-hours, and workflow-minutes to providing an equivalent pool of Pulumi Bills. Usage draws from that pool, and any overage is charged to your card at the end of the month following the same cadence as today.

### For invoiced customers: your transition options

If you're currently on an invoiced Enterprise or Business Critical agreement, you have three paths forward:

1. **Contract amendment**: Convert the remaining dollar value of your current product purchases (resource-hours, secret-hours, workflow-minutes) into an equivalent pool of Pulumi Bills. From the effective date of the amendment, all usage, including Neo Tokens, draws from that pool.

2. **On-demand billing**: Do nothing. Under our standard Terms and Conditions, new feature usage (including Neo Tokens) can be billed monthly in arrears while your existing contract terms remain in place.

3. **Early renewal**: Work with your Pulumi representative to prepay for anticipated usage across the full product portfolio, including Neo.

Please contact your Pulumi representative to review the options available under your specific terms.

## Neo Tokens: Paying for AI That Does Real Work

Pulumi Neo has grown quickly. More than 3,000 organizations are now using our platform engineering agent to design infrastructure, troubleshoot deployments, migrate tooling, and remediate compliance issues. During preview, Neo has been provided at no cost. That changes on June 1.

**Neo Tokens are priced at $3 per Million Tokens (MTok).**

### What counts as a Neo Token?

Neo Tokens are a blended meter that captures the full cost of any Neo Activity (LLM-powered operation). The result is a single token count per Neo task or activity.

Any Neo Activity will consume Neo Tokens, including:

- **Neo Tasks**: agent-driven infrastructure design, troubleshooting, migration, and compliance remediation
- **Pull Request summaries**: automated summaries on pull requests
- **Natural language search** in Pulumi Insights

These features can be triggered from the Pulumi Console, Pulumi GitHub App, pull requests, the CLI, or API calls.

### Tracking your usage

The **Billing & Usage** page shows Neo Token consumption updated with views for the prior time periods. Usage data is downloadable as a CSV with breakdowns by activity type and owner, so you can answer questions like "how much did PR annotations cost us last month?" Activity metadata includes repo and stack where applicable.

### Managing your usage

Organization admins can disable Neo entirely at **Settings → Neo Settings** as well as control Neo-powered activities such as PR annotations. For customers on Pulumi Bills, Neo Token spend draws from the same pool as all other usage.

### Individual Edition

Pulumi Individual Edition remains free and will include a limited monthly allocation of Neo Tokens. When that allocation is exhausted, Neo-powered features will be unavailable until the following month. Upgrading to Pulumi Team Edition or higher enables continued access.

## What You Need to Do

| Your situation | Recommended action |
|---|---|
| Invoiced, standard Pulumi [Terms and Conditions](https://www.pulumi.com/terms-and-conditions/) | Contact your Pulumi representative if you'd like to shift to the Pulumi Bills model. |
| All other invoiced customers including cloud Marketplace customers | Contact your Pulumi representative to review options under your specific agreement. |
| Credit card (Team or Enterprise) | No action required. Your plan transitions automatically on your next billing cycle. |
| Individual Edition | No action required. Free Neo Token allocation included monthly. |

## Looking Ahead

Pulumi Bills aims to give customers maximum flexibility, and Neo Tokens give you a transparent way to track AI-powered infrastructure assistance costs.

If you have questions about how these changes affect your account, reach out to your Pulumi representative or contact [support@pulumi.com](mailto:support@pulumi.com).

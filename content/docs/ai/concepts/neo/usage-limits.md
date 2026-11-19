---
title: Usage limits
title_tag: Usage limits | Pulumi Agents
h1: Agent usage limits
meta_desc: "Set monthly limits for agent model usage across your organization and Neo tasks, with alerts as usage approaches the limit."
aliases:
- /docs/ai/usage-limits/
- /docs/ai/neo/usage-limits/
menu:
    ai:
        name: Usage limits
        parent: ai-agents
        weight: 85
        identifier: ai-usage-limits
---

Set a monthly limit for model usage billed by Pulumi. The organization limit applies to Neo tasks and tasks run by agents your team creates. Per-member limits apply only to Neo tasks.

Requests served through [your own model provider](/docs/ai/agents/model-providers/) can continue after you reach a Pulumi usage limit. To control spending on those requests, set budgets and rate limits with your provider.

These limits cover Neo tokens, the billing unit for model usage. They do not cover the time an agent spends running tools and commands on Pulumi-hosted machines, which is billed separately as [workflow minutes](/pricing/).

## Who can set limits

Members with the **Admin** or [**Billing Manager**](/docs/administration/concepts/billing-managers/) role can view and change usage limits. Other members do not see these controls.

## Set an organization limit

The organization limit covers model usage billed by Pulumi across your organization. Organizations on Pulumi Credits pricing enter a token limit; other organizations enter a dollar amount. Use the units shown beside the field.

1. In the Pulumi Cloud console, open **Settings**, then **Billing & usage**, then **Organization AI usage**.
1. In the **Manage agent usage** panel, enter an organization limit.
1. Save your changes.

Dollar limits range from $10 to $1,000,000. For token limits, the form shows the equivalent bounds at your organization's token price. See [What happens when a limit is reached](#what-happens-when-a-limit-is-reached) for how the limit affects running tasks.

## Set per-member limits

Set a per-member limit to restrict a member's Neo task usage. The task owner's limit applies even when another person contributes to the task. A task run by an agent your team creates is subject to the organization limit, not the limit of the person who started it.

1. On the organization's **AI usage** page, expand **Manage agent usage** and find **Per-member limits**.
1. Open the member's actions menu and select **Set agent usage limit**, or **Edit agent usage limit** to change an existing limit.
1. Enter the limit in the displayed units and select **Save limit**. The member's limit cannot exceed the organization limit.

To apply one limit to several members, select their rows and choose **Set agent usage limit**. To remove a member's limit, use **Remove limit** in their actions menu; the organization limit still applies.

A member's Neo task is blocked when either their own limit or the organization's shared limit is reached.

## Email alerts

Turn on **Enable email notifications** to notify organization admins and billing managers when someone sets or changes the organization limit and when usage reaches 50%, 80%, 95%, or 100% of that limit.

When a member reaches an enabled threshold for their own limit, Pulumi emails the member, organization admins, and billing managers. A member can receive this alert while the organization is still below its limit.

## What happens when a limit is reached

When a task reaches a limit, it displays a message and pauses further model requests billed by Pulumi. An admin or billing manager can raise the limit so work can continue. Otherwise, organization and per-member usage reset at 00:00 UTC on the first day of the next calendar month.

{{% notes type="info" %}}
Usage limits are checked before model requests. Requests already in progress can complete after the limit is reached, so a small overage may still be billed.
{{% /notes %}}

## Availability

Self-service usage limits are available to organizations on a paid subscription. The usage-limit controls do not appear for trial organizations or individual accounts.

<span id="next-steps"></span>

---
title: Usage limits
title_tag: Neo usage limits
h1: Neo usage limits
meta_desc: "Set dollar spend limits on Pulumi Neo for your organization and members, with email alerts as usage approaches the limit."
aliases:
- /docs/ai/usage-limits/
menu:
    ai:
        name: Usage limits
        parent: ai-neo
        weight: 55
        identifier: ai-usage-limits
---

A Neo usage limit caps what your organization spends on [Neo](/docs/ai/) in a monthly billing period. When usage reaches the limit, Neo pauses until the next period resets. You set a limit for the whole organization, and optionally a separate limit for individual members.

## Who can set limits

Members with the **Admin** or **Billing Manager** role can view and change Neo usage limits. Other members do not see the settings.

## Set an organization limit

The organization limit is a single monthly dollar amount that covers all Neo usage across your organization.

1. In the Pulumi Cloud console, navigate to **Settings → Billing & usage → Neo token usage**.
1. In the **Manage token usage** panel, enter an organization limit.
1. Save your changes.

The limit can be as low as **$10** and as high as **$1,000,000**. When the month's Neo usage reaches the limit, Neo pauses for the entire organization until usage resets at the start of the next billing period.

## Set per-member limits

You can also set a limit for an individual member, so no single person consumes the whole organization's budget. Per-member limits are optional; a member without one is still bound by the organization limit.

A member's Neo pauses at their **effective limit — the smaller of their per-member limit and the organization limit.** For example, a member with a $200 per-member limit under a $150 organization limit pauses at $150, because the organization limit is smaller.

The **Manage token usage** panel lists each member with these columns:

| Column | What it shows |
| :--- | :--- |
| **Name** | The member's name |
| **Amount used** | Neo spend so far this billing period |
| **Per-member limit** | The limit you set for this member, if any |
| **Effective limit** | The smaller of the per-member limit and the organization limit |

## Email alerts

Turn on **Enable email notifications** to be alerted by email as usage climbs toward the organization limit. Billing managers and admins receive the alerts.

Emails go out at these points:

- **50%, 80%, and 95%.** Early warnings that give you time to raise the limit before Neo pauses.
- **100%.** Neo has reached the organization limit and is now paused for the organization.

## What happens when a limit is reached

Neo pauses for the affected organization or member for the rest of the billing period. A member who tries to use paused Neo sees a message that usage has reached the monthly limit, and that they should ask an admin to raise it or wait for the next period.

To resume before the period ends, an admin or billing manager can **raise the limit**. Otherwise, Neo resumes automatically when usage **resets at the start of the next billing period**.

{{% notes type="info" %}}
Limits are enforced at the boundary of each Neo turn, so a task already in progress finishes its current step before Neo pauses. A small overage may still be billed as a result. If you set a $1,000 limit and see final usage of $1,003, that is expected, not a billing error.
{{% /notes %}}

## Availability

Neo usage limits are available to organizations on a paid plan. The **Manage token usage** panel does not appear for trial organizations or Individual accounts.

## Next steps

- [Neo settings](/docs/ai/neo/settings/) — configure Neo for your organization
- [Billing managers](/docs/administration/concepts/billing-managers/) — grant billing access without full admin rights

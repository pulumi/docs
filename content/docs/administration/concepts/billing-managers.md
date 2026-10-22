---
title_tag: "Pulumi Cloud: Billing managers"
meta_desc: The billing manager role gives customers the ability to have someone in their Pulumi organization manage billing operations. Learn more about this role here.
title: "Billing managers"
h1: "Billing managers"
menu:
  administration:
    name: Billing managers
    parent: administration-concepts
    weight: 7
aliases:
- /docs/pulumi-cloud/access-management/billing-managers/
- /docs/intro/pulumi-service/billing-managers/
- /docs/intro/pulumi-cloud/billing-managers/
- /docs/administration/organizations-teams/billing-managers/
pulumi_cloud_feature: billing-managers
---

The billing manager role gives customers the ability to have someone in their Pulumi organization manage billing operations without granting them any additional permissions to view or modify your stacks, policies, or other organizational settings.

Any organization admin can view, invite, and remove billing managers from their organization.

The Essentials, Pro, and Enterprise editions allow unlimited billing managers. Organizations still on the legacy Team Pro plan are limited to one billing manager at a time.

## Inviting a billing manager to an organization

Billing manager invitations work much the same way member invitations do, but they are managed on the Billing and Usage page.

{{% notes type="info" %}}
Billing managers, like members, must be members of the [organization identity provider](/docs/administration/concepts/identity-providers/) in order to gain access to the Pulumi organization.
{{% /notes %}}

To invite a new billing manager:

1. Select **Settings**.
1. Select **Billing & usage**.
1. To invite a new billing manager using their email address, select **Invite Billing Managers**. After the new billing manager is invited, they will receive an email allowing them to accept the invite.
1. To invite a new billing manager by sharing a link, select **Copy Billing Manager invite link**. This will copy a link to your clipboard that you can share directly.

As with member invitation links, new billing manager invitation links never expire and may only be used one time.

Billing managers are not included in an organization's member count. For example, if your organization has one admin, two members, and a billing manager, the total member count will be three, not four.

## Viewing billing managers

Billing managers and pending billing manager invitations can be viewed by going to the organization's Settings page, then selecting Billing & usage from the menu. As with the Members page, this table displays all billing managers belonging to your organization, their email address, and when they accepted the invite. For pending billing manager invitations, the invitation status column will include the date an invitation was sent, and will note if a potential billing manager encountered an error while attempting to accept an invitation.

Pending invites and billing manager emails and invite status are only viewable by organization admins. Billing managers will be able to see other billing managers, but only their names.

## Removing a billing manager from an organization

Billing managers can be removed by any organization admin at any time. The steps are similar to removing a member:

1. Select **Settings**.
1. Select **Billing & usage**.
1. Select the ellipsis button next to the billing manager you wish to remove.
1. Choose **Remove Billing Manager**. You will be prompted in a dialog to confirm your choice.

## Billing manager permissions

A billing manager has the ability to access and update billing information, and to view organization metrics, such as resource count and member count (but not member names). This includes setting [Neo usage limits](/docs/ai/concepts/neo/usage-limits/) to cap what the organization spends on Pulumi Neo.

| Resource | Permissions |
| --- | --- |
| Organization Members | List Members (API only) <br> View member count |
| Teams | List Teams (API only) |
| Tokens | None |
| Policy groups | None |
| Policy packs | None |
| Stacks | None |
| Audit Logs | None |
| Billing | View and Update credit card <br> View and Update subscription <br> View payments <br> View billing managers (name only) |
| Resources Under Management (RUM) | View resource count summary| |

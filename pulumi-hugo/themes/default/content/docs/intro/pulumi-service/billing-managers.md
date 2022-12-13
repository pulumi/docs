---
title_tag: "Pulumi Service: Billing Managers"
title: "Billing Managers"
meta_desc: The Billing Manager role gives customers the ability to have someone in their Pulumi Organization manage billing operations. Learn more about this role here.
menu:
  intro:
    parent: pulumi-service
    weight: 4
---

The Billing Manager role gives customers the ability to have someone in their Pulumi Organization manage billing operations without granting them any additional permissions to view or modify your stacks, policies, or other organizational settings.

Any Organization Admin can view, invite, and remove Billing Managers from their organization.

Team Editions of the Pulumi Service are limited to 1 Billing Manager at a time. Enterprise and Business Critical subscriptions can have unlimited Billing Managers in their organization. Visit our [Pricing page](https://www.pulumi.com/pricing) to learn more about Pulumi Service Editions.

## Inviting a Billing Manager to an Organization

Billing Manager invitations work much the same way member invitations do, but they are managed on the Billing and Usage page.

{{% notes "info" %}}
Billing Managers, like members, must be members of the [organization identity provider](/docs/intro/pulumi-service/organizations#organization-identity-providers) in order to gain access to the Pulumi organization.
{{% /notes %}}

To invite a new Billing Manager:

1. Select **Settings**.
1. Select **Billing & usage**.
1. To invite a new Billing Manager using their email address, select **Invite Billing Managers**. After the new Billing Manager is invited, they will receive an email allowing them to accept the invite.
1. To invite a new Billing Manager by sharing a link, select **Copy Billing Manager invite link**. This will copy a link to your clipboard that you can share directly.

As with member invitation links, new Billing Manager invitation links never expire and may only be used one time.

Billing Managers are not included in an organization's member count. For example, if your organization has one admin, two members, and a Billing Manager, the total member count will be three, not four.

## Viewing Billing Managers

Billing Managers and pending Billing Manager invitations can be viewed by going to the organization's Settings page, then selecting Billing & usage from the menu. As with the Members page, this table displays all Billing Managers belonging to your organization, their email address, and when they accepted the invite. For pending Billing Manager invitations, the invitation status column will include the date an invitation was sent, and will note if a potential Billing Manager encountered an error while attempting to accept an invitation.

Pending invites and Billing Manager emails and invite status are only viewable by Organization Admins. Billing Manager will be able to see other Billing Managers, but only their names.

## Removing a Billing Manager from an Organization

Billing Managers can be removed by any organization admin at any time. The steps are similar to removing a member:

1. Select **Settings**.
1. Select **Billing & usage**.
1. Select the ellipsis button next to the Billing Manager you wish to remove.
1. Choose **Remove Billing Manager**. You will be prompted in a dialog to confirm your choice.

## Billing Manager Permissions

A Billing Manager has the ability to access and update billing information, and to view organization metrics, such as resource count and member count (but not member names).

| Resource | Permissions |
| --- | --- |
| Organization Members | List Members (API only) <br> View member count |
| Teams | List Teams (API only) |
| Tokens | None |
| Policy groups | None |
| Policy packs | None |
| Stacks | None |
| Audit Logs | None |
| Billing | View and Update credit card <br> View and Update subscription <br> View payments <br> View Billing Managers (name only) |
| Resources Under Management (RUM) | View resource count summary| |

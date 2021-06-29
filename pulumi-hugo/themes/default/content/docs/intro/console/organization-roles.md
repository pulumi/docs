---
title: Organization Roles
meta_desc: An overview of Organization Roles within the Pulumi Cloud Service.
menu:
  intro:
    parent: console
    weight: 3
aliases: ["/docs/console/collaboration/organization-roles/"]
---

Stacks in the Pulumi Console are grouped by organizations. In order to access the
stacks within an organization, a Pulumi user must have a specific _role_ within that
organization.

## Organization Membership

To become a member of a Pulumi organization, you must be invited by an existing Pulumi
organization administrator, or you must submit a request to the administrator for approval.
In addition, depending on the [Pulumi edition]({{< ref "docs/intro/console#pulumi-plans" >}}),
you must also be a member of the third-party organization or group backing the Pulumi organization.

For example, to become a member of a Pulumi organization backed by a GitLab Group,
you must associate a GitLab identity with your Pulumi account, and also
be a member of that GitLab group.

## Organization Roles

There are several kinds of organization roles a user may be assigned.

**`Member`**

A member of a Pulumi organization can be added to [teams]({{< relref "teams" >}}), and
depending on organization settings, may be able to create or delete stacks.

**`Admin`**

Pulumi organization admins have `Admin` access to _all_ organization stacks,
and can manage organization settings and team memberships.

## Organization Settings{#organization-settings}

A Pulumi organization admin can change
the permissions available to members of the organization.

![Organization settings](/images/docs/reference/service/org-settings-card.png)

### Stack Permissions

Any organization member with the `Admin` role automatically has `Admin`
permissions for all of the organization's stacks. Regular organization members
are granted the organization's _base permissions_ instead.

For example, if the organization's base permissions is `Write`, then
any organization member can update any organization stack.

If the stack permission for all members is `None`, then organization members must be
granted access using [teams]({{< relref "teams" >}}) in order to update, or even [view the organization
stacks]({{< relref "project-and-stack-management#viewing-your-organization-stacks" >}}).

Additionally, organization admins can toggle whether organization members can create stacks, whether
stack admins can delete stacks, and whether stack admins can move stacks to other organizations.

### Team Permissions

By default only organization admins can create teams.

To allow all members to create teams:

1. Navigate to the organization's **Settings**.
1. Navigate to **Access Management**.
1. Use the toggle to turn on the **Allow organization members to create teams** setting.

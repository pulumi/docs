---
title: Organization Roles
meta_desc: An overview of Organization Roles within the Pulumi Cloud Service.
aliases: ["/docs/console/collaboration/organization-roles/"]
---

Stacks in the Pulumi Console are grouped by organizations. In order to access the
stacks within an organization, a Pulumi user must have a specific _role_ within that
organization.

## Organization Membership

> This only applies to newer organizations on the per-member subscription plan.
> Organizations billed per stack have slightly different rules regarding membership.

To become a member of a Pulumi organization, you must be added by an existing Pulumi
organization administrator. However, depending on the [organization type]({{< relref "/docs/intro/console/accounts-and-organizations/organizations#organization-kind" >}}), you must also be a member of the third-party organization or group backing the Pulumi
organization.

For example, to become a member of a Pulumi organization backed by a GitLab Group,
you must associate a GitLab identity with your Pulumi account, and also
be a member of that GitLab group.

## Organization Roles

There are several kinds of organization roles a user may be assigned.

`**MEMBER**`

A member of a Pulumi organization can be added to organization [teams]({{< relref "/docs/intro/console/collaboration/teams" >}}), and
depending on organization settings, may be able to create or delete stacks.

`**ADMIN**`

Pulumi organization admins have `ADMIN` access to _all_ organization stacks,
and can manage organization settings and team memberships.

## Organization Settings{#organization-settings}

A Pulumi organization administrator can change
the permissions available to members of the organization.

![Organization settings](/images/docs/reference/service/org-settings-card.png)

### Default Stack Permission

Any organization member with the `ADMIN` role automatically has `ADMIN`
permissions for all of the organization's stacks. Regular organization members
are granted the organization's _base permissions_ instead.

For example, if the organization's base permissions is `WRITE`, then
any organization member can update any organization stack.

If the default stack permission is `NONE`, then organization members must be
granted access using [teams]({{< relref "teams" >}}) in order to update, or even [view the organization
stacks]({{< relref "project-and-stack-management#viewing-your-organization-stacks" >}}).

### Stack Creation

Pulumi organization admins can configure whether or not members can create stacks.

If enabled, any organization member can create a new stack. Otherwise, only
organization admins can.

When a stack is created within an organization, the creator is given
`ADMIN` permissions to the stack. So even if the default
stack permission is `NONE`, the creator will be able to update the stack. Organization admins
can remove a creator's access to the stack.

### Stack Deletion

Similar to stack creation, Pulumi organization admins can configure whether
or not organization members can delete stacks.

If enabled, any organization member with `ADMIN` permission on the stack can delete
it. Otherwise, only Pulumi  organization admins can.

## Next Steps

* [Teams]({{< relref "teams" >}})

---
title: Organization Roles

menu:
    console:
        parent: collaboration
        weight: 2
---

Stacks in the Pulumi Cloud Console are grouped by organizations. And in order to access the
stacks within an organization, a Pulumi user must have a specific _role_ within that
organization.

## Organization Membership

> This only applies to newer organizations using the per-member subscription plan.
> Organizations billed per-stack have slightly different rules regarding membership.

To become a member of a Pulumi organization, a user must be added by an existing Pulumi
organization administrator. However, depending on the [organization kind]({{< relref "organizations#organization-kind" >}})
the user must also be member of a 3rd party organization or group.

For example, to become a member of a Pulumi organization backed by a GitLab Group,
a user must have associated a GitLab identity with their Pulumi account, and also
be a member of that GitLab group.

## Organization Roles

There are several kinds of organization roles a user may be assigned.

`**MEMBER**`

A member of a Pulumi organization can be added to organization [teams]({{< relref "teams" >}}), and
depending on organization settings, may be able to create or delete stacks.

`**ADMIN**`

Pulumi organization administrators have `ADMIN` access to _all_ organization stacks,
the ability to manage organization settings and team memberships.

## Organization Settings{#organization-settings}

Pulumi organizations can be configured by organization administrators to change
the permissions available to members of the organization.

![Organization settings](/images/docs/reference/service/org-settings-card.png)

### Default Stack Permission

Any organization member with the `ADMIN` role automatically has `ADMIN`
permission for all of the organization's stacks. Regular organization members
are granted the organization's _default stack permission_ instead.

For example, if the organization's default stack permission is `WRITE`, then
any organization member can update any organization stack.

If the default stack permission is `NONE`, then organization members must be
granted access using teams in order to update, or even view organization
stacks. (See [Teams]({{< relref "./teams.md" >}}) for more information.)

### Stack Creation

Pulumi organization admins can configure whether or not the organization
allows members to create new stacks.

If enabled, any organization member can create a new stack. Otherwise, only
organization admins can.

When a stack is created within an organization, the creating user is given
the `ADMIN` permission to that stack explicitly. So even if the default
stack permission is `NONE`, users who create stacks will be able to
update them.

### Stack Deletion

Similar to stack creation, Pulumi organization admins can configure whether
or not organization members can delete stacks.

If enabled, any organization with `ADMIN` permission on the stack can delete
it. Otherwise, only Pulumi  organization admins can.

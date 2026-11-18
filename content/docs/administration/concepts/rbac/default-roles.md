---
title_tag: "Pulumi Cloud: Default role"
meta_desc: Learn how the default role decides what members of a Pulumi Cloud organization can do, and how to choose one.
title: "Default role"
h1: "Default role"
menu:
  administration:
    name: Default role
    parent: administration-concepts-rbac
    weight: 5
    identifier: administration-concepts-rbac-default-roles
---

Every Pulumi Cloud organization has a default role. Members follow it unless an admin assigns them another role, and so do new members who accept an invite that doesn't name a role. When an admin changes the default role, every member who follows it moves to the new role at once, and members with an assigned role keep theirs.

On the **Members** tab, **Default role (Builder)** means the member uses the organization's default role, currently Builder. Changing the organization's default role also changes this member's role. **Builder** alone means the member was explicitly assigned Builder and keeps that role even if the organization's default changes. Pending invitations use the same labels.

## Built-in roles for the default role {#built-in-roles}

Three built-in roles are designed to be the default role. Each one includes everything the role before it allows.

| Role | What members can do |
|------|---------------------|
| `Reader` | Read the organization's stacks, environments, and cloud accounts. Members still manage what they own, such as resources they created under a previous role. |
| `Builder` | Everything Reader allows, plus create stacks, environments, cloud accounts, services, and Pulumi Neo tasks. Members manage what they create. |
| `Maintainer` | Everything Builder allows, plus change every stack, environment, cloud account, and service, and work with deployments, integrations, and Neo automations. |

Every organization also has `Admin` and `Billing Manager`, which admins assign to individual members. They can't be the default role. See [built-in roles](/docs/administration/concepts/rbac/roles/#pulumi-defined-roles). Managing members, teams, and organization settings stays with the `Admin` role. To give someone permissions on specific stacks, environments, or cloud accounts beyond what their role allows, [grant them a permission set on those entities](/docs/administration/concepts/rbac/entities/#entity-access) or add them to a [team](/docs/administration/concepts/rbac/teams) that has those permissions.

## Choosing a default role

New organizations start with `Builder` as the default role, and admins can change it.

In editions with [custom roles](/docs/administration/concepts/rbac/roles/#custom-roles) ({{< pulumi-cloud-editions "custom-roles" >}}), admins choose the default role and can assign individual members a different role. For most of these organizations, we recommend `Builder`: members create and manage their own infrastructure, and get permissions on everyone else's through [teams](/docs/administration/concepts/rbac/teams) or [grants on individual entities](/docs/administration/concepts/rbac/entities/#entity-access), so permissions on shared resources are something you grant on purpose. Choose `Reader` if most members only need to look, and `Maintainer` if every member should be able to change everything. A custom role can also be the default.

In other editions, members use the default role or are admins, and the console doesn't offer a choice of default role. You can still set a built-in role as the default through the REST API or the Pulumi Service provider's [`OrganizationDefaultRole`](/registry/packages/pulumiservice/api-docs/organizationdefaultrole/) resource.

## Changing the default role

You must be an organization admin, in an edition with custom roles, to change the default role, except to move off `Member (legacy)`, which any edition can do.

1. Navigate to **Settings** > **Access management** and select the **Roles** tab.
1. In **Default organization role**, choose the role you want as the default.
1. Confirm the change.

You can also open a role and choose **Actions** > **Set as default organization role**.

You can't delete a custom role while it's the default role. Change the default role first.

Switching the organization to the restricted [permission mode](/docs/administration/concepts/rbac/permission-modes/#what-happens-to-the-default-role) lowers a `Maintainer` or `Member (legacy)` default role to `Builder` or `Reader`. You can raise it again afterwards.

## Moving from the Member role {#moving-from-member}

This section applies to organizations created before November 2026. Organizations created since then start on `Builder` and never had a `Member` role.

Before November 2026, members who weren't admins or billing managers shared one configurable role, `Member`. Pulumi Cloud replaced it with Reader, Builder, and Maintainer, and nobody gained or lost permissions in the move:

- **Your default role** became the built-in role that matched what your members could already do. If none matched exactly, it became `Member (legacy)`, a copy of the permissions your members had. If you had already chosen a custom role as the default, you kept it.
- **Members** who held `Member` now use the default role.
- **Teams and organization access tokens** that held `Member` moved to the role with the same permissions.
- **Custom roles** are unchanged, except that one already named `Reader`, `Builder`, or `Maintainer` was renamed, for example to `Builder (custom)`.

To see where your organization landed, navigate to **Settings** > **Access management**, select the **Roles** tab, and check **Default organization role**. If it shows a built-in role or a custom role of yours, there's nothing more to do.

### Member (legacy) {#member-legacy}

If your default role is `Member (legacy)`, your members have exactly the permissions they had before. You can keep it, but you can't edit, rename, or delete it, and no other role can take its name. To move your organization to a built-in role, which any edition can do:

1. Open `Member (legacy)` and compare it with the built-in role you want, usually `Builder`. Note what members can do today that the built-in role doesn't cover, such as changing stacks or environments that other people created.
1. Give those permissions to the members who need them before you switch, for example through [teams](/docs/administration/concepts/rbac/teams) that own those stacks and environments.
1. [Change the default role](#changing-the-default-role) to the built-in role.
1. Sign in as a member, or ask one, to check that day-to-day work still succeeds.

If something stops working, switch the default role back to `Member (legacy)` while you sort out the missing permissions. `Member (legacy)` stays available for this as long as your organization is on the permissive [permission mode](/docs/administration/concepts/rbac/permission-modes/#before-you-switch-to-restricted).

### Pulumi Service provider {#pulumi-service-provider}

If you manage members with the Pulumi Service provider, use [version 1.7.0](https://github.com/pulumi/pulumi-pulumiservice/releases/tag/v1.7.0) or later. In versions 1.2 to 1.5, an `OrganizationMember` with `role: member` fails once your organization has moved off the `Member` role. Version 1.7.0 also accepts `reader`, `builder`, and `maintainer` as roles, and adds [`OrganizationDefaultRole`](/registry/packages/pulumiservice/api-docs/organizationdefaultrole/) to set the default role. An `OrganizationMember` with `role: member` follows the organization's default role.

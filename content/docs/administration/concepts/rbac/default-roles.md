---
title_tag: "Pulumi Cloud: Default roles"
meta_desc: Learn how the default role decides what members of a Pulumi Cloud organization can do, and how to choose one.
title: "Default roles"
h1: "Default roles"
menu:
  administration:
    name: Default roles
    parent: administration-concepts-rbac
    weight: 5
    identifier: administration-concepts-rbac-default-roles
---

Every Pulumi Cloud organization has a default role. Members follow it unless an admin assigns them another role, and so do new members who accept an invite that doesn't name a role. When an admin changes the default role, every member who follows it moves to the new role at once, and members with an assigned role keep theirs.

## Built-in roles

Three built-in roles are designed to be the default role. Each one includes everything the role before it allows.

| Role | What members can do |
|------|---------------------|
| `Reader` | Read the organization's stacks, environments, and cloud accounts. Members still manage what they own, such as resources they created under a previous role. |
| `Builder` | Everything Reader allows, plus create stacks, environments, cloud accounts, services, and Pulumi Neo tasks. Members manage what they create. |
| `Maintainer` | Everything Builder allows, plus change every stack, environment, cloud account, and service, and work with deployments, integrations, and Neo automations. |

Managing members, teams, and organization settings stays with the `Admin` role. To give someone permissions on specific stacks, environments, or cloud accounts beyond what their role allows, [grant them a permission set on those entities](/docs/administration/concepts/rbac/entities/#entity-access) or add them to a [team](/docs/administration/concepts/rbac/teams) that has those permissions.

## Choosing a default role

New organizations start with `Maintainer` as their default role.

In editions with [custom roles](/docs/administration/concepts/rbac/roles/#custom-roles) ({{< pulumi-cloud-editions "custom-roles" >}}), admins choose the default role and can assign individual members a different role. For most of these organizations, we recommend `Builder`: members create and manage their own infrastructure, and get permissions on everyone else's through [teams](/docs/administration/concepts/rbac/teams) or [grants on individual entities](/docs/administration/concepts/rbac/entities/#entity-access), so permissions on shared resources are something you grant on purpose. Choose `Reader` if most members only need to look, and `Maintainer` if every member should be able to change everything. A custom role can also be the default.

In other editions, the default role is `Maintainer`, and members follow it or are admins or billing managers.

## Changing the default role

You must be an organization admin, in an edition with custom roles, to change the default role.

1. Navigate to **Settings** > **Access management** and select the **Roles** tab.
1. In **Default organization role**, choose the role you want as the default.
1. Confirm the change.

You can also open a role and choose **Actions** > **Set as default organization role**.

## Moving from the Member role {#moving-from-member}

{{% notes type="info" %}}
Pulumi Cloud organizations moved from the `Member` role to Reader, Builder, and Maintainer in November 2026. [Self-hosted installations](#self-hosted) move when they upgrade.
{{% /notes %}}

Organizations used to give members a configurable `Member` role. They moved to Reader, Builder, and Maintainer without losing any permissions. Each one got the three roles, and its default role became the built-in role matching what members could already do. Where none matched, the default role became `Member (legacy)`, a copy of those permissions, and an organization that already had a custom default role kept it. Custom roles, teams, and access tokens kept their permissions, and a custom role that was already named `Reader`, `Builder`, or `Maintainer` was renamed, for example to `Builder (custom)`.

### Member (legacy) {#member-legacy}

`Member (legacy)` is read-only. To move your organization to a built-in role, which any edition can do:

1. Open `Member (legacy)` and compare it with the built-in role you want, usually `Builder`. Note what members can do today that the built-in role doesn't cover, such as changing stacks or environments that other people created.
1. Give those permissions to the members who need them before you switch, for example through [teams](/docs/administration/concepts/rbac/teams) that own those stacks and environments.
1. [Change the default role](#changing-the-default-role) to the built-in role.
1. Sign in as a member, or ask one, to check that day-to-day work still succeeds.

If something stops working, switch the default role back to `Member (legacy)` while you sort out the missing permissions.

### Self-hosted Pulumi Cloud {#self-hosted}

Self-hosted installations move to Reader, Builder, and Maintainer when they upgrade to the release that adds them. The upgrade finishes as usual, and organizations then move in the background, one at a time, as described in [Moving from the Member role](#moving-from-member). Each organization works exactly as before until it moves, and personal accounts stay as they are. To follow progress, a site admin can open **Site admin** > **Background activities** and select the **StoredDefaultRoles** activity, which lists any organization that couldn't move and why. Those organizations keep their permissions and are retried automatically.

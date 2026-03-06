---
title_tag: "Pulumi Cloud: Teams"
meta_desc: Learn about teams in Pulumi Cloud and how they help manage access to resources
title: "Teams"
h1: "Teams"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  administration:
    name: Teams
    parent: administration-access-identity-rbac
    weight: 1
    identifier: pulumi-cloud-access-management-rbac-teams
aliases:
- /docs/administration/access-identity/rbac/teams/
- /docs/pulumi-cloud/access-management/rbac/teams/
- /docs/pulumi-cloud/access-management/teams/
---

{{% notes "info" %}}
Teams are only available to organizations using Pulumi Enterprise Edition and Pulumi Business Critical Edition.
To learn more about editions visit the [pricing page](/pricing/).
{{% /notes %}}

The Pulumi Cloud offers role-based access control (RBAC) using teams. Teams allow organization admins to assign a set of stack permissions to a group of users. When your organization has custom roles enabled, teams can also be assigned **roles** (in addition to stack-level permissions), so that members receive the union of the team's roles and their own user role.

## Creating a Team{#creating-a-team}

By default, all organization admins can create new teams.

To create a team:

1. Navigate to **Settings** > **Teams**.
1. Select **Create team**.

To give members permission to create teams:

1. Navigate to **Settings** > **Access Management**.
1. Use the toggle to turn on the **Allow organization members to create teams** setting.

## Team role assignments {#team-role-assignments}

When your organization has custom roles enabled, teams can be assigned **roles** (default or custom). This is separate from [Team permissions](#team-permissions) (stack-level access) and [Team roles](#team-roles) (Team admin vs Team member).

- Each team can have **multiple role assignments**. Members of the team receive the permissions from all of those roles in addition to their own [organization role](/docs/administration/access-identity/rbac/roles#users).
- Only **team admins** can add or remove role assignments for the team. Additionally, to assign a role the team admin must themselves hold a role that grants the `role:create` and `role:update` scopes — you cannot assign a role that grants more permissions than you yourself hold (role escalation is not permitted).
- **Role-backed teams**: Create a team, assign it a custom role (e.g. with access only to certain stacks or [tag-based rules](/docs/administration/access-identity/rbac/roles#tag-based-abac-rules)), then add members; those members gain the team's roles in addition to their own user role.

## GitHub-based Teams

If your Pulumi organization is backed by GitHub, you can import your existing
GitHub teams into Pulumi.

For these teams, membership is managed on GitHub, while the set of stack
permissions and role assignments granted to team members is managed in the Pulumi Cloud.

## Team Permissions

By default only organization admins can create teams.

To allow all members to create teams:

1. Navigate to **Settings** > **Access Management**.
1. Use the toggle to turn on the Allow organization members to create teams setting.

### Granting Access to Stacks within Teams

Teams can be granted access to stacks, which grants all team members access to those stack based on the selected permission level.

![Editing team stacks and permissions](/images/docs/reference/service/editing-stack-permissions.png)

### Team Roles

Members of a team can be granted `Team admin` or `Team member` permissions. Team admins can add members to a
team. By default, any new team members will be assigned the team member role.

To change a team member's role:

1. Navigate to **Settings** > **Teams** and then the specific team.
1. In the **Members** section use the action menu item at the end of the table row and select **Change role to**.

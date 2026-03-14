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

{{% notes "info" %}}
To allow all organization members to create teams, navigate to **Settings** > **Access Management** and enable the **Allow organization members to create teams** toggle.
{{% /notes %}}

To create a team:

1. Navigate to **Settings** > **Teams**.
1. Select **Create team**.

## Team Access Types

Members of a team can be granted `Team admin` or `Team member` permissions. Team admins can add members to a
team. By default, any new team members will be assigned the team member role.

To change a team member's role:

1. Navigate to **Settings** > **Teams** and then the specific team.
1. In the **Members** section use the action menu item at the end of the table row and select **Change role to**.

## Role assignments {#role-assignments}

When your organization has custom roles enabled, teams can be assigned **roles** (default or custom). This is separate from [Team entity access grants](#team-entity-access-grants) (stack-level access) and [Team access types](#team-access-types) (Team admin vs Team member).

- Each team can have **multiple role assignments**. Members of the team receive the permissions from all of those roles in addition to their own [organization role](/docs/administration/access-identity/rbac/roles#users).
- To add or remove role assignments for a team, a user must hold a role that grants the `role:update` and `team:update` scopes — for example, an organization admin. Being a team admin is not sufficient on its own; a team admin without `role:update` access cannot modify role assignments. Team admins can, however, always manage the team's **Entity Access** grants directly, regardless of their role scopes.
- **Role-backed teams**: Create a team, assign it a custom role (e.g. with access only to certain stacks or [tag-based rules](/docs/administration/access-identity/rbac/roles#tag-based-abac-rules)), then add members; those members gain the team's roles in addition to their own user role.

To manage role assignments for a team, navigate to the team's **Access** tab. The **Role assignments** section lists the roles currently assigned to the team; use **Add role** to assign an additional role.

![Team Access tab showing Entity Access and Role assignments sections](/docs/administration/access-identity/rbac/1-team-role-assignment.png).

## GitHub-based Teams

If your Pulumi organization is backed by GitHub, you can import your existing
GitHub teams into Pulumi.

For these teams, membership is managed on GitHub, while the set of stack
permissions and role assignments granted to team members is managed in the Pulumi Cloud.

## Team Entity Access Grants

Team entity access grants allow team admins to manage their team's access to specific stacks, environments, and insights accounts directly, without requiring org-level role management permissions. This makes it possible for teams to self-manage their own entity access while keeping broader role administration centralized.

Teams can be granted direct access to stacks, environments, and insights accounts. All team members receive access to those entities at the selected permission level.

![Editing team stacks and permissions](/images/docs/reference/service/editing-stack-permissions.png)

---
title_tag: "Pulumi Service: Teams and RBAC"
title: "Teams and RBAC"
meta_desc: The Pulumi Service offers role-based access control (RBAC) using teams. Learn how how to create and manage teams in this guide.
menu:
  intro:
    parent: pulumi-service
    weight: 5
aliases:
- /docs/reference/service/teams/
- /docs/console/collaboration/teams/
- /docs/intro/console/collaboration/
- /docs/intro/console/collaboration/teams/
- /docs/intro/console/teams/
---

{{% notes "info" %}}
Teams are only available to organizations using Pulumi Enterprise Edition and Pulumi Business Critical Edition.
To learn more about editions visit the [pricing page](/pricing/).
{{% /notes %}}

The Pulumi Service offers role-based access control (RBAC) using teams. Teams allow organization admins to assign a set of stack permissions to a group of users.

## Creating a Team{#creating-a-team}

By default, all organization admins can create new teams.

To create a team:

1. Navigate to **Settings** > **Teams**.
1. Select **Create team**.

To give members permission to create teams:

1. Navigate to **Settings** > **Access Management**.
1. Use the toggle to turn on the **Allow organization members to create teams** setting.

## GitHub-based Teams

If your Pulumi organization is backed by GitHub, you can import your existing
GitHub teams into Pulumi.

For these teams, membership is managed on GitHub, while the set of stack
permissions granted to team members is managed in the Pulumi Service.

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

---
title: Teams
meta_desc: An overview of role-based access control (RBAC) using teams within the Pulumi Cloud Service.
menu:
  intro:
    parent: console
    weight: 6
aliases:
- /docs/reference/service/teams/
- /docs/console/collaboration/teams/
- /docs/intro/console/collaboration/
- /docs/intro/console/collaboration/teams/
---

{{% notes "info" %}}
Teams are only available to organizations using Pulumi Enterprise.
To learn more about our editions visit our [pricing page]({{< relref "/pricing" >}}).
{{% /notes %}}

The Pulumi Console offers role-based access control (RBAC) using teams. Teams allow organization admins to assign a set of stack permissions
to a group of users.

## Creating a Team{#creating-a-team}

By default, all organization admins can create new teams.

To create a team:

1. Navigate to **Teams**.
1. Select **Create team**.

To give members permission to create teams:

1. Navigate to the organization's **Settings**.
1. Navigate to **Access Management**.
1. Use the toggle to turn on the **Allow organization members to create teams** setting.

## GitHub-based Teams

If your Pulumi organization is backed by GitHub, you can import your existing
GitHub teams into Pulumi.

For these teams, membership is managed on GitHub, while the set of stack
permissions granted to team members is managed on the Pulumi Console.

## Team Permissions

By default only organization admins can create teams.

To allow all members to create teams:

1. Navigate to the organization’s Settings.
1. Navigate to Access Management.
1. Use the toggle to turn on the Allow organization members to create teams setting.

### Granting Access to Stacks within Teams

Teams can be granted access to stacks, which grants all team members access to those stack based on the selected permission level.

![Editing team stacks and permissions](/images/docs/reference/service/editing-stack-permissions.png)

### Team Roles

Members of a team can be granted `Team admin` or `Team member` permissions. Team admins can add members to a
team. By default, any new team members will be assigned the team member role.

To change a team member's role:

1. Navigate to **Teams** and then the specific team.
1. In the **Members** section use the ellipsis menu item at the end of the table row and select **Change role to**.

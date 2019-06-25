---
title: Teams
menu:
  reference:
    parent: teams
    identifier: teams-teams
    weight: 2
---

The Pulumi Cloud Console offers role-based access control using teams.

> Note: This feature is only available to organizations using the Pulumi Team Pro or
> Enterprise editions. To learn more about Pulumi editions, see [pulumi.com](https://www.pulumi.com/pricing/).

## Teams

Teams allow organization administrators to assign permissions for accessing stacks
to a group of users.

### Creating a Team

You can add a new team by going to the organization's TEAMS tab, and then
clicking the NEW button. Only organization administrators can create or update teams.

![Adding a new team](/images/docs/reference/service/new-team-card.png)

#### GitHub-based Teams

If your Pulumi organization is backed by GitHub, then you can import your existing
GitHub teams into Pulumi.

For these teams, membership is managed on GitHub, while the set of stack
permissions granted to team members is managed on the Pulumi Cloud Console.

![Importing a GitHub-based team](/images/docs/reference/service/add-github-team-card.png)

## Team / Stack Permissions

Membership within a team will grant a Pulumi user a specific permission level for each
stack in the team. For example, members of `network-team` may have `WRITE` access to the
`backend/production` stack, but only `READ` access to `datastore/production`.

![Editing team stacks and permissions](/images/docs/reference/service/editing-stack-permissions.png)

For more information about stack permissions see
[Roles and Access Controls]({{< relref "roles-and-access-controls.md" >}}).

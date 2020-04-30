---
title: Teams
meta_desc: An overview of role-based access control (RBAC) using teams within the Pulumi Cloud Service.
aliases:
- /docs/reference/service/teams/
- /docs/console/collaboration/teams/
---

The Pulumi Console offers role-based access control (RBAC) using teams.

> Note: This feature is only available to organizations using the Pulumi Team Pro or
> Enterprise editions. To learn more about Pulumi editions, see the [pricing page]({{< prelref "/pricing" >}}).

## Teams

Teams allow organization admins to assign a set of stack permissions
to a group of users.

### Creating a Team

You can add a new team by going to the organization's **Teams** tab, and then
clicking **New**. Only organization admins can create or update teams.

![Adding a new team](/images/docs/reference/service/new-team-card.png)

#### GitHub-based Teams

If your Pulumi organization is backed by GitHub, you can import your existing
GitHub teams into Pulumi.

For these teams, membership is managed on GitHub, while the set of stack
permissions granted to team members is managed on the Pulumi Console.

![Importing a GitHub-based team](/images/docs/reference/service/add-github-team-card.png)

## Team / Stack Permissions

Membership within a team will grant a Pulumi user a specific permission level for each
stack in the team. For example, members of `network-team` may have `WRITE` access to the
`backend/production` stack, but only `READ` access to `datastore/production`.

![Editing team stacks and permissions](/images/docs/reference/service/editing-stack-permissions.png)

## Next Steps

* [Stack Permissions]({{< prelref "stack-permissions" >}})

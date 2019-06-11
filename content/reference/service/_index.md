---
title: Teams & Collaboration
menu:
  reference:
    identifier: teams
    weight: 7
---

[The Pulumi Cloud Console](https://app.pulumi.com) allows you to manage your stacks online. It enables
you to to collaborate with multiple developers, protect against concurrent updates, store resource
history, integrate with your CI/CD system, and more!

## Getting Started

To get started using the Pulumi Cloud Console, simply navigate to [app.pulumi.com](https://app.pulumi.com) and sign up.

## Organizations

The Pulumi Cloud Console manages stacks by placing them within _Organizations_.

When you first log in, a Pulumi organization is created with the same name as your Pulumi user account.
That organization is implied whenever you run commands like `pulumi stack init` or
`pulumi stack select`. For example, `pulumi stack init my-devstack` will create a new stack in
the organization associated with your account. e.g. `octocruise/my-devstack`.

To create or select a stack in a different organization, prefix it with the organization's name
followed by a slash. For example, `pulumi stack init acmecorp/new-service`.

For more information on adding new organizations to Pulumi, see [Organizations]({{< relref "orgs.md" >}}).

## Teams

The Pulumi Cloud Console allows people to collaborate on stacks within
an organization, including role-based access control (RBAC).

For more information on the types of collaboration supported, see [Teams]({{< relref "teams.md" >}}).

## Roles and Access Controls

Pulumi organizations allow managing member access to stacks. For example,
enforcing policy on who can create new stacks within an organization, or who
can update existing stacks.

For more information about organization roles, stack permissions, and how they
are managed in the Pulumi Cloud Console, see [Roles and Access Controls]({{< relref "roles-and-access-controls.md" >}}).

## APIs and Integration

The Pulumi Cloud Console exposes REST APIs so you can build custom integrations
on top of Pulumi. See [Webhooks]({{< relref "webhooks.md" >}}) for more information.

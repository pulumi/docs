---
title: Collaboration

menu:
    console:
        identifier: collaboration
        weight: 2
---

The Pulumi Cloud Console offers ways to safely and securely work with other developers to
manage cloud application deployments.

> Collaboration features are found in the Pulumi Team and Enterprise editions. See
> [product editions]({{< relref "editions" >}}) for more information.

## Permissions

There are two permissions systems used when determining the access someone has to a stack.

First is the [organiation-role]({{< relref "organization-roles" >}}) the user has. Administrators
of the Pulumi organization have broad access to change organization settings, including configuring
the specific permissions for other organization members.

Second is the specific [stack permissions]({{< relref "stack-permissions" >}}) a user may
granted to a stack. For example, by being a member of a [team]({{< relref "teams" >}}).

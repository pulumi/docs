---
title: Organization Roles

menu:
    console:
        parent: collaboration
        weight: 2
---

The Pulumi Cloud Console provides fine-grained access controls for stacks.

A user's permission to access a stack is based first on their role within the containing
organization, and then on any additional permissions granted explicitly to that user.

> Note: This feature is only available on organizations using the Pulumi Team Edition.
> For more information, see [Organizations]({{< relref "organizations" >}}).

## Organization Roles

Each member of a Pulumi Cloud Console organization has either the `MEMBER` or
`ADMIN` role within an organization.

Pulumi organizations that have been imported from GitHub carry along each
member's GitHub role. Members of the GitHub organization with the _Owner_
role on GitHub will have the `ADMIN` role in the Pulumi organization.

Also "potential member" and NONE member.

And users being able to add/remove people.

> NOTE: Unless you are on the per-stack plan #LOL
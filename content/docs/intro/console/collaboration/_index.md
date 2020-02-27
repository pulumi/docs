---
title: Collaboration
meta_desc: An overview of developer collaboration features present in the Pulumi Cloud Service.
menu:
    intro:
        parent: console
        identifier: collaboration
        weight: 2

aliases: ["/docs/console/collaboration/"]
---

The Pulumi Console enables safe and secure collaboration between developers and operators. It protects
resource state against concurrent updates and offers detailed insights into stack updates and resources.

## Teams

Collaboration features are found in the Pulumi Team and Enterprise editions.
Some team features are only available on the Pro edition.
See [product editions]({{< relref "editions" >}}) for more information.

## Permissions

There are two permissions systems used when determining a user's access to a stack.

First is the user's [role in the organization]({{< relref "organization-roles" >}}). Administrators
of a Pulumi organization have broad access to the organization settings, including configuring
the specific permissions for other members of the organization.

Second is the specific [stack permissions]({{< relref "stack-permissions" >}}) a user may be
granted to a stack. For example, by being a member of a [team]({{< relref "teams" >}}), or
by being the stack creator.

## Project and Stack Management

Learn about the benefits of using the Pulumi Console to [manage your projects and stacks]({{< relref "project-and-stack-management" >}}).

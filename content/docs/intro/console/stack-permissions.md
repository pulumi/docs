---
title: Stack Permissions
meta_desc: An overview of Stack Permissions within the Pulumi Cloud Service.
menu:
  intro:
    parent: console
    weight: 5
aliases:
- /docs/reference/service/roles-and-access-controls/
- /docs/console/collaboration/stack-permissions/
---

The Pulumi Console provides fine-grained access controls for stacks.

A user's stack permissions is first based on their role within the containing
organization, and then on any additional permissions granted explicitly to that user.

## Stack Permission Levels

There are four types of permission levels available to users and teams
collaborating on Pulumi stacks.

- `None`
- `Read`
- `Write`
- `Admin`

These stack permissions allow users to perform the following actions:

| Action | None | Read | Write | Admin |
|--------|------|------|-------|-------|
| View update history | | ✅ | ✅ | ✅ |
| Decrypt secret configuration | | ✅ | ✅ | ✅ |
| Read stack resources | | ✅ | ✅ | ✅ |
| Preview stack changes | | ✅ | ✅ | ✅ |
| Update stack | | | ✅ | ✅ |
| Destroy stack (`pulumi destroy`) | |   | ✅ | ✅ |
| Export stack checkpoint | | ✅ | ✅ | ✅ |
| Import stack checkpoint |  | | ✅ | ✅ |
| Delete stack (`pulumi stack rm`) | | | | ✅ |
| Transfer to another organization | | | | ✅ |

## Assigning Stack Permissions

Stack permissions can be assigned in three different ways. The permissions granted
from these sources are merged together, granting the highest permission available.

- **Organization Settings**. An organization admin can configure [stack permissions for all members]({{< relref "organization-roles#organization-settings" >}}) for the organization's stacks, granting all members of the organization a minimum permission level.
- **Stack Creator**. The user who created the stack is given `Stack admin` permission, even if the organization's
  stack permissions for all members is `None`. An organization admin can remove the stack creator by navigating to **Stack > Settings > Access** and selecting **Remove**.
- **Team Membership**. Organization admins, and team members can grant members of a [team]({{< relref "teams" >}}) access to stacks and set their permissions.

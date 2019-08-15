---
title: Stack Permissions

menu:
    console:
        parent: collaboration
        weight: 1

aliases: [/docs/reference/service/roles-and-access-controls]
---

The Pulumi Cloud Console provides fine-grained access controls for stacks.

A user's permission to access a stack is based first on their role within the containing
organization, and then on any additional permissions granted explicitly to that user.

## Stack Permission Levels

There are four types of permission levels available to users and teams
collaborating on Pulumi stacks. For information on how to grant stack
permissions, see [Teams]({{< relref "teams.md" >}}).

- `NONE`
- `READ`
- `WRITE`
- `ADMIN`

These stack permissions allow users to perform the following actions:

| Action | NONE | READ | WRITE | ADMIN |
|--------|------|------|-------|-------|
| View update history | | ✅ | ✅ | ✅ |
| Decrypt secret configuration | | ✅ | ✅ | ✅ |
| Read stack resources | | ✅ | ✅ | ✅ |
| Preview stack changes | | ✅ | ✅ | ✅ |
| Update stack | | | ✅ | ✅ |
| Destroy stack (`pulumi destroy`) | |   | | ✅ |
| Export stack checkpoint | | ✅ | ✅ | ✅ |
| Import stack checkpoint |  | | ✅ | ✅ |
| Delete stack (`pulumi stack rm`) | | | | ✅ |

## Assigning Stack Permissions

Permissions to access a stack can be assigned three ways. The permissions granted
from these sources are merged together, granting the highest permission available.

- **Organization Settings** The [organization settings]({{< relref "organization-roles#organization-settings" >}})
  can configure a _Default Stack Permission_ level, granting all members of the organization a minimum permission
  to access a stack.
- **Stack Creator** The user who created the stack is given `ADMIN` permission, even if the organization's
  Default Stack Permission is `NONE`. (This special "creator" permission can be removed by visiting the stack's
  "SETTINGS" and "ACCESS" tab.)
- **Team Membership** A [team]({{< relref "teams" >}}) may grant permissions to access a stack
  to the team's members.
  

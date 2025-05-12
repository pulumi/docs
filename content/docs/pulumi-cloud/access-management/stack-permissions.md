---
title_tag: "Pulumi Cloud: Stack Permissions"
meta_desc: Learn how to manage fine-grained access controls for stacks in the Pulumi Cloud.
title: "Stack permissions"
h1: "Stack permissions"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  cloud:
    name: "Stack permissions"
    parent: pulumi-cloud-access-management
    weight: 2
    identifier: pulumi-cloud-access-management-stack-permissions
aliases:
- /docs/console/collaboration/stack-permissions/
- /docs/intro/console/stack-permissions/
search:
  keywords:
    - stack access control
    - rbac
    - stack security
---

The Pulumi Cloud provides fine-grained access controls for stacks. Stack permissions are
based on the member's role within the organization and their team membership.
Additionally, any member who creates a stack is granted admin permissions on that stack.

Organization admins can control the stack default permissions at the organization level from **Settings** > **Access Management**.
There are four types of stack permissions: `None`, `Read`, `Write`, and `Admin`.
[Team permissions](/docs/pulumi-cloud/access-management/teams#team-permissions) will expand these default permissions.

## Permission Levels

Stack permissions allow users to perform the following actions:

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
| Delete stack (`pulumi stack rm`) |   |   |   | ✅ |
| Transfer to another organization |   |   |   | ✅ |
| Search stack resources           |   |  ✅ |  ✅ | ✅ |

## Managing Stack Permissions

### Default Permissions

Organization admins can set default stack permissions for all members of the organization:

1. Navigate to **Settings** > **Access Management**.
2. Under **Stack Default Permissions**, select the desired permission level.
3. Click **Save** to apply the changes.

### Team-based Permissions

You can grant specific permissions to teams for better access control:

1. Navigate to **Settings** > **Teams**.
2. Select an existing team or create a new one.
3. Under **Stack Permissions**, set the permission level for the team.
4. Click **Save** to apply the changes.

For more information on team-based permissions, see [Team permissions](/docs/pulumi-cloud/access-management/teams#team-permissions).

### Stack Creator Permissions

By default, the user who creates a stack is granted admin permissions on that stack. This ensures that the creator can manage the stack they created regardless of default organization permissions.

## Related Resources

- [Teams](/docs/pulumi-cloud/access-management/teams)
- [Projects & Stacks](/docs/pulumi-cloud/projects-and-stacks)
- [Access Tokens](/docs/pulumi-cloud/access-management/access-tokens)
---
title_tag: "Pulumi Cloud: Permission modes"
meta_desc: Learn how the permissive and restricted permission modes decide what deployments and team tokens can access in a Pulumi Cloud organization.
title: "Permission modes"
h1: "Permission modes"
menu:
  administration:
    name: Permission modes
    parent: administration-concepts-rbac
    weight: 8
    identifier: administration-concepts-rbac-permission-modes
aliases:
  - /docs/pulumi-cloud/access-management/rbac/permission-modes/
---

An organization's permission mode decides how much access the work that runs on behalf of your organization, such as deployments, gets. Every organization is in one of two modes:

- **Permissive**: work that runs on behalf of your organization gets broader access than it was explicitly given.
- **Restricted**: work that runs on behalf of your organization gets only the access it was explicitly given.

The permission mode doesn't change what your members can do through their own roles, teams, and entity access. It applies to deployments and team access tokens, and it sets a ceiling on how broad the organization's default role starts.

## What each mode changes

| | Permissive | Restricted |
|---|---|---|
| **Deployments** | Run as the stack's [service principal or team](/docs/deployments/concepts/settings/pulumi-cloud-role/) if one is selected. Otherwise, manual runs use the permissions of whoever starts them, and automatic runs use the organization's background runner. | Every stack selects a service principal or a team, and every run uses that identity. A deployment of a stack without one is refused, including scheduled ones. |
| **`PULUMI_ACCESS_TOKEN` in deployment settings** | Allowed, unless the stack selects a service principal or a team. | Refused. |
| **[Team access tokens](/docs/administration/concepts/access-tokens/#team-access-tokens)** | Get the team's roles and entity access, plus the organization-wide default permissions on stacks, environments, and cloud accounts. | Get only the team's roles and entity access. |
| **Built-in default role** | `Maintainer`, unless an admin chooses another. | `Builder`, unless an admin chooses another. |

Organization access tokens, creator grants, and members' own roles work the same way in both modes.

In the Free edition, an organization has a single member, and deployments always run as that member. The only difference between the modes is that restricted refuses a `PULUMI_ACCESS_TOKEN` in a stack's deployment settings.

## Which mode your organization is in

- **New organizations** are created in the restricted mode, with `Builder` as the default role. The mode of these organizations can't be changed.
- **Existing organizations** stay in the permissive mode until an admin switches them, so nothing changes for them on its own.
- **Individual accounts** have no permission mode.

## Switching the permission mode

You must be an organization admin to switch the permission mode. Organizations that started in the permissive mode can switch in either direction at any time.

1. Navigate to **Settings** > **Access management** and select the **Other** tab.
1. Under **Permission mode**, choose **Permissive** or **Restricted**.
1. Select **Save permission mode**, read what the switch changes for your edition, and confirm.

### Before you switch to restricted

Switching takes effect immediately, so prepare the organization first:

1. **Give every stack that uses Pulumi Deployments a service principal or a team.** Select it under **Run as** in the stack's [deployment settings](/docs/deployments/concepts/settings/pulumi-cloud-role/). Stacks without one stop deploying once the organization is restricted, including their scheduled deployments.
1. **Remove `PULUMI_ACCESS_TOKEN` from deployment settings.** Deployments that set it fail until it's removed.
1. **Check what your team tokens rely on.** A team token that reads a stack or opens an environment only because every member can by default loses that access. Give the team a [role](/docs/administration/concepts/rbac/teams/#role-assignments) or [entity access](/docs/administration/concepts/rbac/teams/#team-entity-access-grants) that covers it.
1. **Review your default role.** See the next section.

### What happens to the default role

Switching to restricted lowers a default role that gives broad access:

| Default role before the switch | Default role after the switch |
|---|---|
| `Reader`, `Builder`, or a custom role | Unchanged |
| `Maintainer` | `Builder` |
| `Member (legacy)` | `Reader` if it grants exactly what `Reader` does, otherwise `Builder` |

`Member (legacy)` roles that nobody is assigned are removed. Members who hold a role of their own keep it; only members who follow the default role move with it. You can change the default role again afterwards, including back to `Maintainer`.

Switching back to permissive doesn't change roles. The default role stays as it is, and `Member (legacy)` isn't brought back. Stacks without a service principal can deploy again, stacks with one keep running as it, and team tokens get the default permissions again.

## Using the REST API

The organization's permission mode is the `permissionMode` field (`permissive` or `restricted`) of `GET /api/orgs/{orgName}/metadata`. To switch it, send `setPermissionMode` to `PATCH /api/orgs/{orgName}`, which requires the `organization:update` scope:

```bash
curl -s -X PATCH \
  "https://api.pulumi.com/api/orgs/{orgName}" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"setPermissionMode": "restricted"}'
```

Switching the permission mode is recorded in the [audit logs](/docs/administration/concepts/audit-logs/).

## Learn more

- [Service principals](/docs/administration/concepts/rbac/service-principals/): Non-human identities with their own roles and entity access.
- [Run as](/docs/deployments/concepts/settings/pulumi-cloud-role/): Choose the service principal or team a stack's deployments run as.
- [Default roles](/docs/administration/concepts/rbac/default-roles/): The role members follow unless an admin assigns them another one.
- [Access tokens](/docs/administration/concepts/access-tokens/): How organization and team tokens get their permissions.

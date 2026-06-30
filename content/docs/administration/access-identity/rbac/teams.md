---
title_tag: "Pulumi Cloud: Teams"
meta_desc: Learn about teams in Pulumi Cloud and how they help manage access to resources
title: "Teams"
h1: "Teams"
menu:
  administration:
    name: Teams
    parent: administration-access-identity-rbac
    weight: 5
    identifier: pulumi-cloud-access-management-rbac-teams
aliases:
- /docs/administration/access-identity/rbac/teams/
- /docs/pulumi-cloud/access-management/rbac/teams/
- /docs/pulumi-cloud/access-management/teams/
---

{{% notes "info" %}}
Teams are only available to organizations using Pulumi Enterprise Edition and Pulumi Business Critical Edition.
To learn more about editions visit the [pricing page](/pricing/).
{{% /notes %}}

The Pulumi Cloud offers role-based access control (RBAC) using teams. Teams allow organization admins to assign a set of stack permissions to a group of users. When your organization has custom roles enabled, teams can also be assigned **roles** (in addition to stack-level permissions), so that members receive the union of the team's roles and their own user role.

## Creating a Team{#creating-a-team}

By default, all organization admins can create new teams.

{{% notes "info" %}}
To allow all organization members to create teams, enable the **Allow organization members to create teams** toggle in [Organization-wide role settings](/docs/administration/access-identity/rbac/roles#organization-wide-role-settings).
{{% /notes %}}

To create a team:

1. Navigate to **Settings** > **Teams**.
1. Select **Create team**.

## Team Access Types

Members of a team can be granted `Team admin` or `Team member` permissions. Team admins can add members to a
team. By default, any new team members will be assigned the team member role.

To change a team member's role:

1. Navigate to **Settings** > **Teams** and then the specific team.
1. In the **Members** section use the action menu item at the end of the table row and select **Change role to**.

## Role assignments {#role-assignments}

When your organization has custom roles enabled, teams can be assigned **roles** (default or custom). This is separate from [Team entity access grants](#team-entity-access-grants) (stack-level access) and [Team access types](#team-access-types) (Team admin vs Team member).

- Each team can have **multiple role assignments**. Members of the team receive the permissions from all of those roles in addition to their own [organization role](/docs/administration/access-identity/rbac/roles#users).
- To add or remove role assignments for a team, a user must hold a role that grants the `role:update` and `team:update` scopes — for example, an organization admin. Being a team admin is not sufficient on its own; a team admin without `role:update` access cannot modify role assignments. Team admins can, however, always manage the team's **Entity Access** grants directly, regardless of their role scopes.
- **Role-backed teams**: Create a team, assign it a custom role (e.g. with access only to certain stacks or [tag-based rules](/docs/administration/access-identity/rbac/roles#tag-based-abac-rules)), then add members; those members gain the team's roles in addition to their own user role.

To manage role assignments for a team, navigate to the team's **Access** tab. The **Role assignments** section lists the roles currently assigned to the team; use **Add role** to assign an additional role.

![Team Access tab showing Entity Access and Role assignments sections](/docs/administration/access-identity/rbac/1-team-role-assignment.png).

## GitHub-based Teams

If your Pulumi organization is backed by GitHub, you can import your existing
GitHub teams into Pulumi.

For these teams, membership is managed on GitHub, while the set of stack
permissions and role assignments granted to team members is managed in the Pulumi Cloud.

## Team Entity Access Grants

Team entity access grants allow team admins to manage their team's access to specific stacks, environments, and insights accounts directly, without requiring org-level role management permissions. This makes it possible for teams to self-manage their own entity access while keeping broader role administration centralized.

Teams can be granted direct access to stacks, environments, and insights accounts. All team members receive access to those entities at the selected permission level.

![Editing team stacks and permissions](/images/docs/reference/service/editing-stack-permissions.png)

### Managing environment access via the REST API

Team environment grants can also be managed programmatically using the [Pulumi Cloud REST API](/docs/reference/cloud-rest-api/). This is useful for automated provisioning workflows where team permissions need to be applied consistently across many environments or as part of a broader infrastructure-as-code setup.

All three operations — adding, editing, and removing an environment permission — use the same endpoint:

```
PATCH https://api.pulumi.com/api/orgs/{orgName}/teams/{teamName}
Authorization: token {token}
Content-Type: application/json
```

**Add an environment permission:**

```bash
curl -s -X PATCH \
  "https://api.pulumi.com/api/orgs/{orgName}/teams/{teamName}" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "addEnvironmentPermission": {
      "projectName": "{projectName}",
      "envName": "{envName}",
      "permission": "read"
    }
  }'
```

Or equivalently using the `pulumi cloud api` command:

```bash
pulumi cloud api PATCH \
  /orgs/{orgName}/teams/{teamName} \
  -- --body '{"addEnvironmentPermission":{"projectName":"{projectName}","envName":"{envName}","permission":"read"}}'
```

The valid permission values are:

| Value   | Console label        | Description |
|---------|----------------------|-------------|
| `read`  | Environment reader   | Team members can view environment definitions but cannot decrypt secrets or retrieve dynamic credentials. |
| `open`  | Environment opener   | Team members can decrypt secrets and retrieve dynamic credentials from the environment. |
| `write` | Environment editor   | Team members can open and update the environment. |
| `admin` | Environment admin    | Team members can open, update, and delete the environment. |

**Edit an existing environment permission:**

```bash
curl -s -X PATCH \
  "https://api.pulumi.com/api/orgs/{orgName}/teams/{teamName}" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "editEnvironmentPermission": {
      "projectName": "{projectName}",
      "envName": "{envName}",
      "permission": "write"
    }
  }'
```

**Remove an environment permission:**

```bash
curl -s -X PATCH \
  "https://api.pulumi.com/api/orgs/{orgName}/teams/{teamName}" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "removeEnvironment": {
      "projectName": "{projectName}",
      "envName": "{envName}"
    }
  }'
```

The endpoint returns `204 No Content` on success. These operations require a Pulumi access token scoped to a user with team administration rights; organization admins always have this access. The `projectName` field refers to the ESC project in which the environment resides — this is the project specified when the environment was created (for example, `default` if no explicit project was given).

## Related resources

- [Roles](/docs/administration/access-identity/rbac/roles): Collections of permission sets applied to entities and combined with an organization access level. You can assign roles to a team so its members inherit them.
- [Permission sets](/docs/administration/access-identity/rbac/permission-sets): Reusable bundles of related scopes for a single entity type. You grant them on entities or use them to set a role's organization access level.
- [Entities and organization-level access](/docs/administration/access-identity/rbac/entities): The objects that permission sets are granted on (stacks, environments, and Insights accounts), plus the organization-level access that governs org-wide operations.
- [Scopes](/docs/administration/access-identity/rbac/scopes): The most granular access rights in Pulumi Cloud, written as `object:action`. Each scope belongs to one entity type and is the building block of permission sets.

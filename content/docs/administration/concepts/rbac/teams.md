---
title_tag: "Pulumi Cloud: Teams"
meta_desc: Learn about teams in Pulumi Cloud and how they help manage access to resources
title: "Teams"
h1: "Teams"
menu:
  administration:
    name: Teams
    parent: administration-concepts-rbac
    weight: 5
    identifier: pulumi-cloud-access-management-rbac-teams
aliases:
- /docs/administration/access-identity/rbac/teams/
- /docs/pulumi-cloud/access-management/rbac/teams/
- /docs/pulumi-cloud/access-management/teams/
- /docs/administration/organizations-teams/teams/
- /docs/reference/service/teams/
- /docs/console/collaboration/teams/
- /docs/intro/console/collaboration/
- /docs/intro/console/collaboration/teams/
- /docs/intro/console/teams/
- /docs/intro/pulumi-service/teams/
- /docs/intro/pulumi-cloud/teams/
pulumi_cloud_feature: teams
---

Pulumi Cloud offers role-based access control (RBAC) using teams. Teams let you give a group of users access to stacks, environments, and cloud accounts. When your organization has custom roles enabled, teams can also be assigned **roles** (in addition to access on individual entities), so that members receive the union of the team's roles and their own user role.

## Creating a Team{#creating-a-team}

By default, all organization admins can create new teams.

{{% notes type="info" %}}
To let other members create teams, give them a [custom role](/docs/administration/concepts/rbac/roles/#custom-roles) that includes the `team:create` scope.
{{% /notes %}}

To create a team:

1. Navigate to **Settings** > **Access management** and select the **Teams** tab.
1. Select **Create team**.

## The Everyone team {#the-everyone-team}

Every organization has a team named Everyone, in every edition. Its members are the organization's admins and members. Billing managers are not in it.

You can [grant Everyone access](#team-entity-access-grants) like any other team, and add it as an approver in an [approval ruleset](/docs/esc/concepts/approvals/#configuring-a-ruleset).

Membership of Everyone follows the organization, so you can't add or remove members. You also can't rename it, change its description, assign it roles or create team access tokens for it.

## Team Access Types

Members of a team can be granted `Team admin` or `Team member` permissions. Team admins can add members to a
team. By default, any new team members will be assigned the team member role.

To change a team member's role:

1. Navigate to **Settings** > **Access management**, select the **Teams** tab, and then select the specific team.
1. In the **Members** section use the action menu item at the end of the table row and select **Change role to**.

## Role assignments {#role-assignments}

When your organization has custom roles enabled, teams can be assigned **roles** (default or custom). This is separate from [Team entity access grants](#team-entity-access-grants) (access on individual stacks, environments, and cloud accounts) and [Team access types](#team-access-types) (Team admin vs Team member).

- Each team can have **multiple role assignments**. Members of the team receive the permissions from all of those roles in addition to their own [organization role](/docs/administration/concepts/rbac/roles#users).
- To add or remove role assignments for a team, a user must hold the `team:update` scope, and either the `role:update` scope or the role being assigned. An organization admin can assign any role; a team admin without `role:update` can give the team only roles they hold themselves.
- A team can't be assigned the built-in `Admin` role. To give a team broad access, assign it `Maintainer` or a custom role.
- **Role-backed teams**: Create a team, assign it a custom role (e.g. with access only to certain stacks or [tag-based rules](/docs/administration/concepts/rbac/roles#tag-based-abac-rules)), then add members; those members gain the team's roles in addition to their own user role.

To manage role assignments for a team, navigate to the team's **Access** tab. The **Role assignments** section lists the roles currently assigned to the team; use **Add role** to assign an additional role.

## Team access tokens

A team can have [team access tokens](/docs/administration/concepts/access-tokens/#team-access-tokens) for automation that should act with the team's permissions.
Those tokens authenticate as the team's [service principal](/docs/administration/concepts/access-tokens/#how-team-tokens-are-identified), a machine identity separate from the team's human members.
When a team token creates a stack, the team receives Stack Admin on it, so members of the team can manage it.

## GitHub-based Teams

If your Pulumi organization is backed by GitHub, you can import your existing
GitHub teams into Pulumi.

For these teams, membership is managed on GitHub, while the set of stack
permissions and role assignments granted to team members is managed in Pulumi Cloud.

## Team Entity Access Grants

Teams can be granted access directly on specific stacks, environments, and cloud accounts, without a role. All team members receive the permission set the team holds on those entities.

Team grants are managed where the access is: open the stack, environment, or cloud account's [access settings](/docs/administration/concepts/rbac/entities/#entity-access), select **Add Principal**, choose **Team**, and pick one of the built-in permission sets. The team's **Access** tab lists what the team was granted. Changing a team's access to an entity requires permission to change that entity's access.

With the Pulumi Service provider, use [`TeamStackPermission`](/registry/packages/pulumiservice/api-docs/teamstackpermission/) and [`TeamEnvironmentPermission`](/registry/packages/pulumiservice/api-docs/teamenvironmentpermission/). To grant access to the Everyone team, use the team name `everyone`.

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

## Learn more

- [Roles](/docs/administration/concepts/rbac/roles): Collections of permission sets applied to entities and combined with an organization access level. You can assign roles to a team so its members inherit them.
- [Permission sets](/docs/administration/concepts/rbac/permission-sets): Reusable bundles of related scopes for a single entity type. You grant them on entities or use them to set a role's organization access level.
- [Entities and organization-level access](/docs/administration/concepts/rbac/entities): The objects that permission sets are granted on (stacks, environments, and cloud accounts), plus the organization-level access that governs org-wide operations.
- [Scopes](/docs/administration/concepts/rbac/scopes): The most granular access rights in Pulumi Cloud, written as `object:action`. Each scope belongs to one entity type and is the building block of permission sets.

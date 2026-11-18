---
title_tag: "Pulumi Cloud: Entities and organization level access"
meta_desc: Learn about entities in Pulumi Cloud RBAC — the stacks, environments, and cloud accounts that permission sets are granted on — and organization-level access.
title: "Entities and Organization Level Access"
h1: "Entities and Organization Level Access"
menu:
  administration:
    name: Entities & Org Level
    parent: administration-concepts-rbac
    weight: 3
    identifier: administration-concepts-rbac-entities
pulumi_cloud_feature: rbac
aliases:
  - /docs/administration/access-identity/rbac/entities/
---

An entity is a Pulumi object that can have [permission sets](/docs/administration/concepts/rbac/permission-sets) granted on it.

In Pulumi Cloud's authorization model, we use the term "entity" instead of "resource" to refer to such objects. This is because "resource" already has a specific meaning within Pulumi (referring to cloud infrastructure resources). We use the term "entity" to avoid confusion when discussing authorization.

## Entity types

An entity type is a category of objects that can be protected by the RBAC system. Each entity type has its own set of associated permission sets and is managed independently.

When creating a permission set, it must be of a specific entity type, and can only include scopes of that same type.

Pulumi Cloud has three entity types:

* **[Stacks](/docs/iac/concepts/stacks/)**: All operations that affect stacks — updates, configuration, deployment settings, tags and annotations, webhooks, and schedules. See [stack scopes](/docs/administration/reference/rbac-scopes/stacks) for the full list.
* **[Environments](/docs/esc/concepts/environments/)** (Pulumi ESC): All operations that affect environments — configuration, secrets, schedules, webhooks, and versions. See [environment scopes](/docs/administration/reference/rbac-scopes/environments) for the full list.
* **[Cloud accounts](/docs/discovery-governance/)**: All operations that affect cloud accounts — accounts, policy evaluations, scan configurations, and results and reports. See [cloud account scopes](/docs/administration/reference/rbac-scopes/insights-accounts) for the full list.

## Giving someone permissions on an entity {#entity-access}

You can give a member, a team, or a [service principal](/docs/administration/concepts/rbac/service-principals/) a [permission set](/docs/administration/concepts/rbac/permission-sets) on a single stack, environment, or cloud account, on top of what their role allows. This is available in the Essentials, Pro, and Enterprise editions.

1. Open the entity's access settings. For a stack or an environment, select **Settings** > **Access**. For a cloud account, select the **Access** tab.
1. Choose **Add Principal**.
1. Choose **User**, **Team**, or **Service Principal**, then the member, team, or service principal.
1. Choose a permission set and confirm.

Each principal holds one permission set on an entity, so granting another one replaces it. To change a grant, pick a different permission set in the principal's row. To remove it, select **Remove**.

### Who has access

The access settings list everyone who was granted access on the entity:

* The **Owner**, the member or team that created the entity or was made its owner, has full access. Select **Reassign** to hand ownership to someone else.
* Members, teams, and service principals with a grant appear with their permission set.
* On some stacks, people are listed as a **Collaborator**. These are members who were given access to the stack before this page existed. They keep the access they had, shown as Stack Read, Stack Write, or Stack Admin, and you can remove them like anyone else. To change what a collaborator can do, add them again with **Add Principal** and choose a permission set.

Organization admins have full access through their role and aren't listed unless they also hold a grant. A member's page lists the stacks, environments, and cloud accounts they were granted under **Access**.

### Who can grant what

Anyone who can read the entity can see who has access to it. To change it, you need the entity's `stack_access:update`, `environment_access:update`, or `insights_account_access:update` scope, which the built-in Admin permission sets include.

You can only grant what you hold: you must have every scope in the permission set on that same entity, through your role, your teams, or a grant of your own. The console offers the permission sets your role is likely to hold: Readers and Builders can grant Read, Maintainers and members on `Member (legacy)` can grant every set except Admin, and organization admins, the entity's owner, and members with a custom role can grant any permission set, including [custom ones](/docs/administration/concepts/rbac/permission-sets/#custom-permission-sets).

Without permission to change access, the controls are disabled and say why. Access can't be changed while the organization is locked.

### How grants behave over time

* A grant stays in place when the member's role, or the organization's [default role](/docs/administration/concepts/rbac/default-roles/), changes. Removing a member from the organization removes their grants.
* A grant on a [cloud account](/docs/discovery-governance/concepts/discovery/cloud-accounts/) covers its regions and discovered child accounts, which have no access settings of their own.
* [Transferring a stack](/docs/administration/concepts/organizations/#transferring-stacks) to another organization removes every grant on it.

### Teams

Granting a team access requires the Pro or Enterprise edition. A team can hold one of the built-in permission sets on an entity. The [Everyone team](/docs/administration/concepts/rbac/teams/#the-everyone-team) can be granted access in every edition that has entity access. See [team entity access grants](/docs/administration/concepts/rbac/teams/#team-entity-access-grants).

### Using the REST API

Entity access for members and service principals uses two routes. Both identify the entity by its type and ID. For teams, see [managing environment access via the REST API](/docs/administration/concepts/rbac/teams/#managing-environment-access-via-the-rest-api).

List who has access and which permission sets you can grant:

```bash
curl -s -X POST \
  "https://api.pulumi.com/api/orgs/{orgName}/assignments/list" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "context": { "__type": "PermissionExpressionStack" },
    "id": "{stackId}"
  }'
```

Or equivalently using the `pulumi cloud api` command:

```bash
pulumi cloud api POST \
  /orgs/{orgName}/assignments/list \
  -- --body '{"context":{"__type":"PermissionExpressionStack"},"id":"{stackId}"}'
```

Grant, change, or revoke access:

```bash
curl -s -X POST \
  "https://api.pulumi.com/api/orgs/{orgName}/assignments/update" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "context": { "__type": "PermissionExpressionStack" },
    "id": "{stackId}",
    "userId": "{userLogin}",
    "permissionSetId": "{permissionSetId}"
  }'
```

Or equivalently using the `pulumi cloud api` command:

```bash
pulumi cloud api POST \
  /orgs/{orgName}/assignments/update \
  -- --body '{"context":{"__type":"PermissionExpressionStack"},"id":"{stackId}","userId":"{userLogin}","permissionSetId":"{permissionSetId}"}'
```

* `context.__type` is `PermissionExpressionStack`, `PermissionExpressionEnvironment`, or `PermissionExpressionInsightsAccount`.
* `userId` is a member's or service principal's login.
* Leave out `permissionSetId` to revoke the grant.

A request that grants more than you hold fails with `403` and names the scopes you're missing.

### Using the Pulumi Service provider

The [`OrganizationMemberEntityAccess`](/registry/packages/pulumiservice/api-docs/organizationmemberentityaccess/) resource, available from version 1.7.0, manages one member's permission set on one entity:

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
import * as pulumiservice from "@pulumi/pulumiservice";

const aliceOnDev = new pulumiservice.OrganizationMemberEntityAccess("alice-on-dev", {
    organizationName: "my-org",
    username: "alice",
    entityType: "stack",
    entityName: "my-project/dev",
    permission: "stack-write",
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_pulumiservice as pulumiservice

alice_on_dev = pulumiservice.OrganizationMemberEntityAccess(
    "alice-on-dev",
    organization_name="my-org",
    username="alice",
    entity_type="stack",
    entity_name="my-project/dev",
    permission="stack-write",
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-pulumiservice/sdk/go/pulumiservice"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		_, err := pulumiservice.NewOrganizationMemberEntityAccess(ctx, "alice-on-dev", &pulumiservice.OrganizationMemberEntityAccessArgs{
			OrganizationName: pulumi.String("my-org"),
			Username:         pulumi.String("alice"),
			EntityType:       pulumi.String("stack"),
			EntityName:       pulumi.String("my-project/dev"),
			Permission:       pulumi.String("stack-write"),
		})
		return err
	})
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using Pulumi;
using Pulumi.PulumiService;

return await Deployment.RunAsync(() =>
{
    var aliceOnDev = new OrganizationMemberEntityAccess("alice-on-dev", new OrganizationMemberEntityAccessArgs
    {
        OrganizationName = "my-org",
        Username = "alice",
        EntityType = "stack",
        EntityName = "my-project/dev",
        Permission = "stack-write",
    });
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
package myproject;

import com.pulumi.Pulumi;
import com.pulumi.pulumiservice.OrganizationMemberEntityAccess;
import com.pulumi.pulumiservice.OrganizationMemberEntityAccessArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            var aliceOnDev = new OrganizationMemberEntityAccess("alice-on-dev", OrganizationMemberEntityAccessArgs.builder()
                .organizationName("my-org")
                .username("alice")
                .entityType("stack")
                .entityName("my-project/dev")
                .permission("stack-write")
                .build());
        });
    }
}
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  aliceOnDev:
    type: pulumiservice:OrganizationMemberEntityAccess
    properties:
      organizationName: my-org
      username: alice
      entityType: stack
      entityName: my-project/dev
      permission: stack-write
```

{{% /choosable %}}

{{< /chooser >}}

`entityType` is `stack`, `environment`, or `insightsAccount`. Set `permission` to a built-in permission set such as `stack-read`, `environment-open`, or `insights-account-admin`, or set `permissionSetId` to a custom one.

## Organization-level access

Organization-level operations — billing, member management, audit logs, integrations, and other organization settings — are **not** an entity type. They aren't tied to individual objects, so you don't grant them through entity access rules. Instead, a role's **organization access level** governs them. See [Roles](/docs/administration/concepts/rbac/roles#custom-roles) for how organization access is configured.

Organization-level access also covers **meta-permissions**: actions that can't be attached to an existing entity because the entity doesn't exist yet. Creating a stack (`stack:create`), a team (`team:create`), or a cloud account (`insights_account:create`) is governed at the organization level rather than per-entity — there's no specific stack, team, or account to grant access on until it's created.

{{% notes type="info" %}}
**Organization-level scopes vs. org-wide capability toggles**: Organization-level scopes (e.g. `stack:create`, `team:create`) are granted through a role's organization access level. These are separate from the toggles in the [permissions for tokens without a role](/docs/administration/concepts/access-tokens/#organization-wide-role-settings) (e.g. "Allow these tokens to create stacks"), which apply only to organization tokens without a role.
{{% /notes %}}

## Learn more

* [Scopes](/docs/administration/concepts/rbac/scopes): The most granular access rights in Pulumi Cloud, written as `object:action`. Each scope belongs to one entity type and is the building block of permission sets.
* [Permission sets](/docs/administration/concepts/rbac/permission-sets): Reusable bundles of related scopes for a single entity type. You grant them on entities or use them to set a role's organization access level.
* [Roles](/docs/administration/concepts/rbac/roles): Collections of permission sets applied to entities and combined with an organization access level. You assign a role to users, teams, and machine tokens.
* [Teams](/docs/administration/concepts/rbac/teams): Groups of users that can be assigned roles and entity access. Each member inherits the union of the team's roles on top of their own role.

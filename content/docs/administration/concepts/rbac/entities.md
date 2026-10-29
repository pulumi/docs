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

You can give a member or a team a [permission set](/docs/administration/concepts/rbac/permission-sets) on a single stack, environment, or cloud account, on top of what their role allows. This works in every edition.

1. Open the entity's access settings. For a stack or an environment, select **Settings** > **Access**. For a cloud account, select the **Access** tab.
1. Choose **Add Principal**.
1. Choose **User** or **Team**, then the member or team.
1. Choose a permission set and confirm.

Anyone who can read the entity can see who has permissions on it. Readers and Builders can grant Read, Maintainers and members on `Member (legacy)` can grant every set except Admin, and organization admins, the entity's owner, and members with a custom role can grant any permission set. Each grant is still checked against your own permissions on the entity. To remove a grant, open the same access settings and remove the member or team from the list.

## Organization-level access

Organization-level operations — billing, member management, audit logs, integrations, and other organization settings — are **not** an entity type. They aren't tied to individual objects, so you don't grant them through entity access rules. Instead, a role's **organization access level** governs them. See [Roles](/docs/administration/concepts/rbac/roles#custom-roles) for how organization access is configured.

Organization-level access also covers **meta-permissions**: actions that can't be attached to an existing entity because the entity doesn't exist yet. Creating a stack (`stack:create`), a team (`team:create`), or a cloud account (`insights_account:create`) is governed at the organization level rather than per-entity — there's no specific stack, team, or account to grant access on until it's created.

{{% notes type="info" %}}
**Organization-level scopes vs. org-wide capability toggles**: Organization-level scopes (e.g. `stack:create`, `team:create`) are granted through a role's organization access level. These are separate from the toggles in the [permissions for tokens without a role](/docs/administration/concepts/access-tokens/#organization-wide-role-settings) (e.g. "Allow these tokens to create stacks"), which apply only to organization tokens without a role and to team tokens.
{{% /notes %}}

## Learn more

* [Scopes](/docs/administration/concepts/rbac/scopes): The most granular access rights in Pulumi Cloud, written as `object:action`. Each scope belongs to one entity type and is the building block of permission sets.
* [Permission sets](/docs/administration/concepts/rbac/permission-sets): Reusable bundles of related scopes for a single entity type. You grant them on entities or use them to set a role's organization access level.
* [Roles](/docs/administration/concepts/rbac/roles): Collections of permission sets applied to entities and combined with an organization access level. You assign a role to users, teams, and machine tokens.
* [Teams](/docs/administration/concepts/rbac/teams): Groups of users that can be assigned roles and entity access. Each member inherits the union of the team's roles on top of their own role.

---
title_tag: "Pulumi Cloud: Role-Based Access Control (RBAC)"
meta_desc: Learn about role-based access control in Pulumi Cloud and how it helps manage access to resources
title: "Role-Based Access Control (RBAC)"
h1: "Role-Based Access Control (RBAC)"
meta_image: /images/docs/meta-images/docs-meta.png
aliases:
  - /docs/pulumi-cloud/access-management/rbac/
menu:
  administration:
    parent: administration-access-identity
    weight: 2
    identifier: administration-access-identity-rbac
---

Role-Based Access Control (RBAC) in Pulumi Cloud provides a flexible and secure way to manage access to your organization's resources. This allows you to exercise fine-grained control over who can access what resources in your organization and what actions they can perform.

Leveraging Pulumi's RBAC features empower Enterprise organizations to follow best practices:

- **Granular Access Control**: Define precise access levels for different resources.
- **Simplified Management**: Easily manage access as they grow by building out reusable RBAC elements.
- **Security**: Enforce least privilege access to resources.

## Principals

Roles can be assigned to three kinds of principals in Pulumi Cloud:

- **Users**: Organization members can have a baseline organization role (Admin, Member, Billing Manager, or a custom role). When your organization has custom roles and "Assign custom roles to users" is enabled, admins can assign any custom role to individual members.
- **Teams**: Teams can be assigned one or more roles. Members of a team receive the union of the team's roles and their own user role. Team role assignments are available when the organization has custom roles enabled.
- **Organization access tokens**: Machine tokens can be assigned one role that defines the token's permissions across the organization.

## Where roles apply

- **User role**: Each member has a single baseline organization role (Admin, Member, Billing Manager, or a custom role). When "Assign custom roles to users" is enabled, admins can override this per user.
- **Organization default role**: When your organization has custom roles, you can set a **default role for members**. That custom role becomes the baseline for members who have the Member organization role and have not been given an explicit custom role.
- **Team roles**: Teams can have **role assignments** (one or more roles). Members of a team effectively get the union of those roles plus their own user role in the organization. See [Teams](/docs/administration/access-identity/rbac/teams#team-role-assignments) for details.

## How permissions accumulate

Access in Pulumi Cloud is built up progressively. A user's effective permissions are the union of every grant that applies to them — from the broadest organizational constraints down to the most resource-specific automatic grants.

### Organization-wide settings {#organization-wide-settings}

The outermost layer is a set of **organization-wide access settings** at **Settings** > **Access Management**. These on/off toggles cover capabilities such as creating or deleting stacks, creating teams, and creating Insights accounts. When a setting is **enabled**, that capability is granted to all members unconditionally, regardless of their role. When a setting is **disabled**, only members whose role explicitly includes the corresponding RBAC scope retain the capability. These settings are distinct from RBAC scopes: RBAC scopes (e.g. `stack:create`, `team:create`) are granted per-role, while org-wide settings apply to everyone when enabled.

### Team roles

Members who belong to teams inherit all roles assigned to those teams, on top of their own individual role. Users in multiple teams accumulate permissions from all of them. Team roles can include tag-based (ABAC) rules that automatically apply a permission set to any resource whose tags match specified conditions, without requiring per-resource grants.

### Organization role

Every member has a baseline organization role (Admin, Member, Billing Manager, or a custom role). Members with the Member organization role who have not been assigned an explicit custom role inherit the organization's default custom role, if one has been configured.

### Creator grants

Any user who creates a stack is automatically granted the Stack Admin permission set on that stack, regardless of their organization role or team memberships.

All grants are strictly **additive**: no grant can reduce what another provides.

## RBAC Constructs

Pulumi Cloud's RBAC system is built on these core concepts:

- [**Scopes**](/docs/administration/access-identity/rbac/scopes): Granular access rights that define specific actions on resources
- [**Permission sets**](/docs/administration/access-identity/rbac/permission-sets): Predefined bundles of scopes that are commonly used together
- [**Roles**](/docs/administration/access-identity/rbac/roles): Collections of permission sets applied to resources and assigned to principals
- [**Teams**](/docs/administration/access-identity/rbac/teams): Groups of users that can be assigned roles

Custom roles can also include **tag-based (ABAC) rules**: when resource tags match a rule's conditions, the role grants a chosen permission set on that resource. Details are in [Roles](/docs/administration/access-identity/rbac/roles#tag-based-abac-rules).

### Customization

Enterprise organizations have access to manage and create their own teams. They also can manage and create their own custom permission sets and roles, on top of the defaults available to every organization in Pulumi.

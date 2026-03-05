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

A user's effective permissions are the **union** of (1) their user role and (2) all roles assigned to the teams they belong to. Team role assignments add on top of the user's baseline role.

## RBAC Constructs

Pulumi Cloud's RBAC system is built on these core concepts:

- [**Scopes**](/docs/administration/access-identity/rbac/scopes): Granular access rights that define specific actions on resources
- [**Permission sets**](/docs/administration/access-identity/rbac/permission-sets): Predefined bundles of scopes that are commonly used together
- [**Roles**](/docs/administration/access-identity/rbac/roles): Collections of permission sets applied to resources and assigned to principals
- [**Teams**](/docs/administration/access-identity/rbac/teams): Groups of users that can be assigned roles

Custom roles can also include **tag-based (ABAC) rules**: when resource tags match a rule's conditions, the role grants a chosen permission set on that resource. Details are in [Roles](/docs/administration/access-identity/rbac/roles#tag-based-abac-rules) and [Scopes](/docs/administration/access-identity/rbac/scopes#tag-based-rules-and-scopes).

### Customization

Enterprise organizations have access to manage and create their own teams. They also can manage and create their own custom permission sets and roles, on top of the defaults available to every organization in Pulumi.

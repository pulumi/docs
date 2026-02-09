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

## RBAC Constructs

Pulumi Cloud's RBAC system is built on these core concepts:

- [**Scopes**](/docs/administration/access-identity/rbac/scopes): Granular access rights that define specific actions on resources
- [**Permission sets**](/docs/administration/access-identity/rbac/permission-sets): Predefined bundles of scopes that are commonly used together
- [**Roles**](/docs/administration/access-identity/rbac/roles): Collections of permission sets applied to resources and assigned to principals.
- [**Teams**](/docs/administration/access-identity/rbac/teams): Groups of users that can be assigned roles.

### Customization

Enterprise organizations have access to manage and create their own teams. They also can manage and create their own custom permission sets and roles, on top of the defaults available to every organization in Pulumi.

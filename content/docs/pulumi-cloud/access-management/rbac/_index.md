---
title_tag: "Pulumi Cloud: Role-Based Access Control (RBAC)"
meta_desc: Learn about role-based access control in Pulumi Cloud and how it helps manage access to resources
title: "Role-Based Access Control (RBAC)"
h1: "Role-Based Access Control (RBAC)"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  cloud:
    name: RBAC
    parent: pulumi-cloud-access-management
    weight: 2
    identifier: pulumi-cloud-access-management-rbac
---

Role-Based Access Control (RBAC) in Pulumi Cloud provides a flexible and secure way to manage access to your organization's resources. This allows you to exercise fine-grained control over who can access what resources in your organization and what actions they can perform.

Leveraging Pulumi's RBAC features empower Enterprise organizations to follow best practices:

- **Granular Access Control**: Define precise access levels for different resources.
- **Simplified Management**: Easily manage access as they grow by building out reusable RBAC elements.
- **Security**: Enforce least privilege access to resources.

## RBAC Constructs

Pulumi Cloud's RBAC system is built on these core concepts:

- [**Scopes**](/docs/pulumi-cloud/access-management/rbac/scopes): Granular access rights that define specific actions on resources
- [**Permissions**](/docs/pulumi-cloud/access-management/rbac/permissions): Predefined bundles of scopes that are commonly used together
- [**Roles**](/docs/pulumi-cloud/access-management/rbac/roles): Collections of permissions applied to resources and assigned to principals.
- [**Teams**](/docs/pulumi-cloud/access-management/rbac/teams): Groups of users that can be assigned roles.

### Customization

Enterprise organizations have access to manage and create their own Teams. They also can manage and create their own custom Permissions and Roles, on top of the defaults available to every organization in Pulumi.

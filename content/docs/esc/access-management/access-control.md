---
title: Access control
title_tag: Access control | Pulumi ESC
h1: Pulumi ESC access control
meta_desc: Pulumi ESC provides granular access control to manage permissions with roles like reader, opener, and editor.
menu:
  esc:
    parent: pulumi-esc-access-management
    weight: 1
aliases:
  - /docs/esc/environments/access-control/
---

Pulumi ESC allows you to enforce least-privileged access across your environments through role-based access controls (RBAC). By assigning precise permissions at the organization and team levels, you ensure that users only have access to the environments they need. All changes, including environment updates and access modifications, are fully logged to provide complete auditing and compliance tracking, helping your organization maintain security best practices.

## Setting up access to environments

{{% notes "info" %}}
Access controls and Teams are only available to organizations using Pulumi Enterprise Edition and Pulumi Business Critical Edition.To learn more about editions visit the [pricing page](/pricing/).
{{% /notes %}}

### Organization-wide permissions

Go to the `Access Management` page under Settings to set Organization-wide environment permissions. Members of the organization will receive these permissions. The default environment permission is `write`. There are four options:

* `none`: Members have access to none of the environments
* `read`: Members can view only plaintext key values (i.e., the definition of the environment). They won’t be able to see the secret values in plaintext, run any provider configurations to retrieve credentials or run any functions. They cannot perform any Pulumi IaC operations such as `refresh`, `up`, `destroy` on stacks that imports the environment
* `open`: Members with ‘open’ permissions can decrypt secrets and see them in plaintext. Additionally, they can get dynamic credentials using provider configurations and evaluate functions defined in the environment. They can perform any Pulumi IaC operation on stacks that import an environment as long as they have ‘write’ access to the stack and ‘open’ access to the environment
* `write`: Members will have permissions to `open` and `update` any environment

### Team permissions

You can grant environment-wise permissions to members of a Team. There are four roles:

* `Environment reader`: Team members will have `read` permissions
* `Environment opener`: Team members will have `open` permissions
* `Environment editor`: Team members will have `write` permissions
* `Environment admin`: Team members will have `write` and `delete` permissions

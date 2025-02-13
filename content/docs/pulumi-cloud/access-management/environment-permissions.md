---
title_tag: "Pulumi Cloud: Environment Permissions"
meta_desc: Learn how to set organization wide environment permissions for the Pulumi Cloud.
h1: Environment organization permissions
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  cloud:
    name: Environment permissions
    parent: pulumi-cloud-access-management
    weight: 3
---

Pulumi ESC provides role-based access control (RBAC) to manage access to environments and their secrets and configurations. This ensures that users and teams only have the necessary permissions to view, modify, or use specific environments in infrastructure deployments.

## Managing Access to Environments

Pulumi ESC permissions can be set at two levels allowing you to follow a least-privilege model to ensure sensitive information remain secure:

**Organization-wide permissions**: Define the default level of access for all members of an organization.

**Team-based permissions**: Assign specific access roles to teams for granular control over who can read, modify, or manage environments.

{{% notes "info" %}}
By default, organization-wide environment access is set to write, but this can be adjusted to restrict permissions.
{{% /notes %}}

To learn more about configuring ESC access controls, including organization wide permission levels and team based permissions see [Pulumi ESC Access Control](/docs/esc/environments/access-management/access-control/).
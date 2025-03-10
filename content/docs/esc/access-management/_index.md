---
title_tag: "Pulumi ESC: Identity & access Management"
meta_desc: Learn how to use tokens, role-based access control, and OIDC with Pulumi ESC
title: "Identity & access management"
h1: "Pulumi ESC: Identity & access management"
meta_image: /images/docs/meta-images/docs-meta.png

menu:
    esc:
        parent: esc-home
        identifier: pulumi-esc-access-management
        weight: 10
---

Pulumi ESC provides identity and access management (IAM) controls to secure your environments, secrets, and configurations. Using role-based access control (RBAC), teams can enforce least-privilege access across environments, ensuring that users only have the permissions they need. ESC also supports access tokens for programmatic authentication and OpenID Connect (OIDC) for integrating with external identity providers.

## Access controls in Pulumi ESC

- [Teams and Role-based access control(RBAC)](/docs/pulumi-cloud/access-management/teams/): Manage permissions at the organization and environment levels.
- [Access tokens](/docs/pulumi-cloud/access-management/access-tokens/): Securely authenticate and automate ESC operations.
- [OpenID Connect (OIDC)](/docs/esc/access-management/oidc/): Integrate with trusted third-party identity providers to authenticate users.
- [SAML single sign-on (SSO)](saml/): Configure SAML-based authentication for centralized access management.
- [SCIM](scim/): Simplify user provisioning with the SCIM protocol

For additional details on configuring environment-specific access controls, refer to the [Pulumi ESC access control](/docs/esc/access-management/access-control/) documentation.

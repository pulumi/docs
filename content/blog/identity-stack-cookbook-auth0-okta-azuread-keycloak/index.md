---
title: "Identity Stack Cookbook: Auth0, Okta, Entra ID, and Keycloak"
date: 2026-06-18
meta_desc: "Manage common identity platform patterns with Pulumi across Auth0, Okta, Microsoft Entra ID, and Keycloak, including SSO, apps, and groups."
meta_image: meta.png
feature_image: feature.png
authors:
    - pablo-seibelt
tags:
    - identity
    - sso
    - tutorial
social:
    twitter: |
        Identity platforms all model apps, groups, roles, and SSO differently.

        This Pulumi cookbook compares Auth0, Okta, Entra ID, and Keycloak patterns.
    linkedin: |
        Auth0, Okta, Microsoft Entra ID, and Keycloak solve similar identity problems with different resource models.

        This cookbook shows Pulumi patterns for SSO, apps, groups, and provider-specific prerequisites.
    bluesky: |
        Auth0, Okta, Entra ID, and Keycloak all model identity differently.

        This Pulumi cookbook compares practical IaC patterns.
---

Managing identity at scale requires more than a login box. Platform teams need consistent application access patterns across Auth0, Okta, Microsoft Entra ID, and Keycloak.

In this cookbook, we'll explore how to implement a portable identity pattern using Pulumi. We'll cover Auth0, Okta, Microsoft Entra ID, and Keycloak, focusing on a common requirement: one application and one provider-specific access container.

This post provides a common SSO application pattern across these providers for your own applications, rather than configuring Pulumi organization SSO. By the end, you will have implemented a portable identity pattern across Auth0, Okta, Microsoft Entra ID, and Keycloak.

<!--more-->

## Why a portable identity pattern matters

Identity providers (IdPs) are often treated as static infrastructure, but they are dynamic components of your security architecture. By defining your identity stack in code, you gain several advantages:

1. Consistency across environments (dev, staging, production).
1. Version-controlled security policies.
1. Rapid migration or multi-IdP support.
1. Automated user and group lifecycle management.

## The pattern

The goal is to create a reusable pattern that works across different providers. This pattern includes:

1. **An application**: The service or platform users will access.
1. **An access container**: A provider-specific organization, group, or role assignment that controls who should have access to the application.

## Auth0

Auth0 is known for its developer-friendly approach and extensibility. Auth0 does not model application access as a generic group assignment. A practical baseline is to define an application client that requires organization login, an organization as the access boundary, and a connection enabled for that client.

Prerequisites: an Auth0 tenant, a Machine-to-Machine application with Management API scopes for clients, organizations, connections, and connection clients, and the Pulumi Auth0 provider configured with the tenant domain, client ID, and client secret.

```typescript
import * as auth0 from "@pulumi/auth0";

const client = new auth0.Client("auth0-app", {
    name: "My Application",
    appType: "regular_web",
    callbacks: ["https://myapp.com/callback"],
    organizationUsage: "require",
    organizationRequireBehavior: "pre_login_prompt",
});

const organization = new auth0.Organization("auth0-organization", {
    name: "my-organization",
    displayName: "My Organization",
});

const connection = new auth0.Connection("auth0-connection", {
    name: "my-connection",
    strategy: "auth0",
});

const connectionClients = new auth0.ConnectionClients("auth0-connection-clients", {
    connectionId: connection.id,
    enabledClients: [client.clientId],
});

const organizationConnection = new auth0.OrganizationConnection("auth0-org-connection", {
    organizationId: organization.id,
    connectionId: connection.id,
});
```

## Okta

Okta is a leader in workforce identity. Its Pulumi provider offers deep integration for managing applications and group assignments.

Prerequisites: an Okta organization, an API token or OAuth service app with application and group management scopes, and the Pulumi Okta provider configured with the organization URL and credentials.

```typescript
import * as okta from "@pulumi/okta";

const app = new okta.app.OAuth("okta-app", {
    label: "My Application",
    type: "browser",
    grantTypes: ["authorization_code"],
    redirectUris: ["https://myapp.com/callback"],
    responseTypes: ["code"],
});

const group = new okta.group.Group("okta-group", {
    name: "My Group",
    description: "My Group Description",
});

const assignment = new okta.app.GroupAssignment("okta-assignment", {
    appId: app.id,
    groupId: group.id,
});
```

## Microsoft Entra ID

For organizations heavily invested in the Microsoft ecosystem, Microsoft Entra ID is the standard. Pulumi allows you to manage applications and service principals with ease. This minimal example focuses on the application, service principal, group, and assignment resources; add redirect URI and platform configuration for your specific application type before using it as a live SSO app.

Prerequisites: a Microsoft Entra tenant, permissions to create applications, service principals, groups, and app role assignments, and the Pulumi Microsoft Entra ID provider authenticated through your chosen Azure identity flow.

The default app role ID assigns the group to the application without requiring a custom app role. Replace it with an `appRoles[].id` value when your application defines custom roles.

```typescript
import * as azuread from "@pulumi/azuread";

const app = new azuread.Application("entra-app", {
    displayName: "My Application",
    signInAudience: "AzureADMyOrg",
});

const group = new azuread.Group("entra-group", {
    displayName: "My Group",
    mailEnabled: false,
    securityEnabled: true,
});

const servicePrincipal = new azuread.ServicePrincipal("entra-sp", {
    clientId: app.clientId,
});

const assignment = new azuread.AppRoleAssignment("entra-assignment", {
    appRoleId: "00000000-0000-0000-0000-000000000000",
    principalObjectId: group.objectId,
    resourceObjectId: servicePrincipal.objectId,
});
```

## Keycloak

Keycloak is the go-to open-source solution for identity management. It is highly flexible and can be self-hosted or run in a container.

Prerequisites: a Keycloak realm, an admin client or service account with realm-management permissions, and the Pulumi Keycloak provider configured with the server URL, realm, client ID, and credentials.

```typescript
import * as keycloak from "@pulumi/keycloak";

const realm = new keycloak.Realm("keycloak-realm", {
    realm: "my-realm",
    enabled: true,
});

const client = new keycloak.openid.Client("keycloak-app", {
    realmId: realm.id,
    clientId: "my-app",
    name: "My Application",
    enabled: true,
    accessType: "CONFIDENTIAL",
    validRedirectUris: ["https://myapp.com/callback"],
});

const group = new keycloak.Group("keycloak-group", {
    realmId: realm.id,
    name: "My Group",
});

const role = new keycloak.Role("keycloak-app-user-role", {
    realmId: realm.id,
    clientId: client.id,
    name: "app-user",
});

const groupRoles = new keycloak.GroupRoles("keycloak-group-roles", {
    realmId: realm.id,
    groupId: group.id,
    roleIds: [role.id],
    exhaustive: false,
});
```

## When to switch and how

Choosing an identity provider depends on your specific needs. Auth0 is a strong fit for external application authentication. Okta and Microsoft Entra ID are common choices for internal workforce management. Keycloak is ideal for teams that need full control over their identity infrastructure.

When switching providers, the key is to maintain the same logical structure. By using Pulumi, you can keep the same intent in code while mapping it to each provider's resource model. Auth0 organizations, Okta groups, Entra ID groups, and Keycloak groups are not identical, so migrations still require a provider-specific access review.

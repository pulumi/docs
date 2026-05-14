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

In this cookbook, we'll explore how to implement a portable identity pattern using Pulumi. We'll cover Auth0, Okta, Microsoft Entra ID, and Keycloak, focusing on a common requirement: one application and one access group.

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
1. **A group**: A collection of users who should have access to the application.

## Auth0

Auth0 is known for its developer-friendly approach and extensibility. While Auth0 handles SCIM through Enterprise Connections or Actions, the core setup involves defining a client and a connection.

Prerequisites: an Auth0 tenant, a Machine-to-Machine application with Management API scopes for clients, organizations, and connections, and the Pulumi Auth0 provider configured with the tenant domain, client ID, and client secret.

```typescript
import * as auth0 from "@pulumi/auth0";

const client = new auth0.Client("my-app", {
    name: "My Application",
    appType: "regular_web",
    callbacks: ["https://myapp.com/callback"],
});

const group = new auth0.Organization("my-group", {
    name: "my-group",
    displayName: "My Group",
});

const connection = new auth0.Connection("my-connection", {
    name: "my-connection",
    strategy: "auth0",
});
```

## Okta

Okta is a leader in workforce identity. Its Pulumi provider offers deep integration for managing applications and group assignments.

Prerequisites: an Okta organization, an API token or OAuth service app with application and group management scopes, and the Pulumi Okta provider configured with the organization URL and credentials.

```typescript
import * as okta from "@pulumi/okta";

const app = new okta.app.OAuth("my-app", {
    label: "My Application",
    type: "browser",
    grantTypes: ["authorization_code"],
    redirectUris: ["https://myapp.com/callback"],
    responseTypes: ["code"],
});

const group = new okta.group.Group("my-group", {
    name: "My Group",
    description: "My Group Description",
});

const assignment = new okta.app.GroupAssignment("my-assignment", {
    appId: app.id,
    groupId: group.id,
});
```

## Microsoft Entra ID

For organizations heavily invested in the Microsoft ecosystem, Microsoft Entra ID is the standard. Pulumi allows you to manage applications and service principals with ease.

Prerequisites: a Microsoft Entra tenant, permissions to create applications, service principals, groups, and app role assignments, and the Pulumi Microsoft Entra ID provider authenticated through your chosen Azure identity flow.

```typescript
import * as azuread from "@pulumi/azuread";

const app = new azuread.Application("my-app", {
    displayName: "My Application",
    signInAudience: "AzureADMyOrg",
});

const group = new azuread.Group("my-group", {
    displayName: "My Group",
    mailEnabled: false,
    securityEnabled: true,
    types: ["Unified"],
});

const servicePrincipal = new azuread.ServicePrincipal("my-sp", {
    clientId: app.clientId,
});

const assignment = new azuread.AppRoleAssignment("my-assignment", {
    appRoleId: "00000000-0000-0000-0000-000000000000", // Default access role; replace with an appRoles[].id for custom roles.
    principalObjectId: group.objectId,
    resourceObjectId: servicePrincipal.objectId,
});
```

## Keycloak

Keycloak is the go-to open-source solution for identity management. It is highly flexible and can be self-hosted or run in a container.

Prerequisites: a Keycloak realm, an admin client or service account with realm-management permissions, and the Pulumi Keycloak provider configured with the server URL, realm, client ID, and credentials.

```typescript
import * as keycloak from "@pulumi/keycloak";

const realm = new keycloak.Realm("my-realm", {
    realm: "my-realm",
    enabled: true,
});

const client = new keycloak.openid.Client("my-app", {
    realmId: realm.id,
    clientId: "my-app",
    name: "My Application",
    enabled: true,
    accessType: "CONFIDENTIAL",
    validRedirectUris: ["https://myapp.com/callback"],
});

const group = new keycloak.Group("my-group", {
    realmId: realm.id,
    name: "My Group",
});
```

## When to switch and how

Choosing an identity provider depends on your specific needs. Auth0 is a strong fit for external application authentication. Okta and Microsoft Entra ID are common choices for internal workforce management. Keycloak is ideal for teams that need full control over their identity infrastructure.

When switching providers, the key is to maintain the same logical structure. By using Pulumi, you can swap the provider-specific resources while keeping your application logic intact. This approach ensures that your identity stack remains as portable as your cloud infrastructure.

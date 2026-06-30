---
title: "Automate Azure App Secret Rotation with ESC"
date: 2026-04-06
draft: false
meta_desc: "Learn how to automate Azure app secret rotation using Pulumi ESC to keep your credentials secure and up to date."
meta_image: meta.png
feature_image: feature.png
authors:
    - sean-yeh
tags:
    - esc
    - azure
category: product
schema_type: auto
social:
    twitter: |
        Expired Azure app secrets cause outages. If you've ever scrambled to rotate one before it expires, you know the pain.

        Pulumi ESC's new azure-app-secret rotator handles rotation automatically. Set a lifetime, add a schedule, and credentials stay fresh.
    linkedin: |
        Expired Azure app registration secrets lead to broken authentication and unexpected outages. If you've ever scrambled to rotate a client secret before it expires, you know the pain.

        Pulumi ESC now has an azure-app-secret rotator that automates this. Set a lifetime, configure a rotation schedule, and ESC handles the rest.
---

[Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/fundamentals/whatis) (formerly Azure Active Directory) is Azure's identity and access management service. Any time your application needs to authenticate with Entra ID, you create an **app registration** and give it a [client secret](https://learn.microsoft.com/en-us/entra/identity-platform/how-to-add-credentials?tabs=client-secret) that proves its identity. But those secrets expire, and if you don't rotate them in time, your app loses access.

If you or your team manages Azure app registrations, you know that keeping track of client secrets is a constant hassle. Forgetting to rotate them before they expire can lead to broken authentication and unexpected outages. With [Pulumi ESC](/docs/esc)'s `azure-app-secret` rotator, you can automate client secret rotation for your Azure apps, so you never have to worry about expired credentials again.

<!--more-->

## Setup

### Prerequisites

- An Azure App Registration
- An [azure-login](/docs/esc/integrations/dynamic-login-credentials/azure-login/) environment
  - Note for OIDC users: Since Azure does not support wildcard subject matches, you will need to add a [federated credential](/docs/esc/guides/configuring-oidc/azure/#add-federated-credentials) for the azure-login environment as well as each environment that imports it.
  - The Azure identity used for rotation must have the `Application.ReadWrite.All` Graph API permission, or the identity must be added as an Owner of the specific app registration whose secrets will be rotated.

## How it works

Let's assume your azure-login environment looks like this:

```yaml
# my-org/logins/production
values:
  azure:
    login:
      fn::open::azure-login:
        clientId: <your-client-id>
        tenantId: <your-tenant-id>
        subscriptionId: <your-subscription-id>
        oidc: true
```

Create a new environment for your rotator. If you have the existing credentials, set them in the [state](/docs/esc/environments/syntax/builtin-functions/fn-rotate/#parameters) object so the rotator will treat them as the `current` credentials.

```yaml
# my-org/rotators/secret-rotator
values:
  appSecret:
    fn::rotate::azure-app-secret:
      inputs:
        login: ${environments.logins.production.azure.login}
        clientId: <target-app-client-id>
        lifetimeInDays: 180 # How long each new secret is valid (max 730 days)
      state:
        current:
          secretId: <secret-id>
          secretValue:
            fn::secret: <secret-value>
```

The `lifetimeInDays` field controls how long each generated secret remains valid before it expires. Azure allows a maximum of 730 days (two years), but shorter lifetimes are recommended for better security. Make sure to set a rotation [schedule](/docs/esc/environments/rotation/#schedule) that runs before the lifetime expires so your credentials are always fresh.

Azure app registrations can have at most two client secrets at any given time, so the rotator maintains a `current` and `previous` secret. When a rotation occurs, the existing `current` secret becomes the `previous` secret, and a new secret is created to take its place as the new `current`. This ensures a smooth rollover with no downtime, since the previous secret remains valid until the next rotation.

Once this is set up, you're ready to go! You never need to worry about your client secrets expiring, and you will always have the latest credentials in your ESC Environment.

## Learn more

The `fn::rotate::azure-app-secret` rotator is available now in all Pulumi ESC environments. For more information, check out the [fn::rotate::azure-app-secret documentation](/docs/esc/integrations/rotated-secrets/azure-app-secret/)!

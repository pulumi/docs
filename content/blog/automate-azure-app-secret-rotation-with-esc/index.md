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
    - pulumi-esc
    - azure
schema_type: auto
social:
    twitter: "Automate Azure app secret rotation with Pulumi ESC — never worry about expired credentials again."
    linkedin: "Automate Azure app secret rotation with Pulumi ESC — never worry about expired credentials again."
    bluesky: "Automate Azure app secret rotation with Pulumi ESC — never worry about expired credentials again."
---

Any time your application needs to authenticate with Azure Active Directory, you need an app registration with a client secret. But those secrets expire, and if you don't rotate them in time, your app loses access.

If you or your team manages Azure app registrations, you know that keeping track of client secrets is a constant hassle. Forgetting to rotate them before they expire can lead to broken authentication and unexpected outages. With [Pulumi ESC](/docs/esc)'s `azure-app-secret` rotator, you can automate client secret rotation for your Azure apps, so you never have to worry about expired credentials again!

<!--more-->

## Setup

Prerequisites:
- An Azure App Registration
- An [azure-login](/docs/esc/integrations/dynamic-login-credentials/azure-login/) environment
  - Note for OIDC users: Since Azure does not support wildcard subject matches, you will need to add a federated credential for the azure-login environment as well as each environment that imports it.

{{< notes type="info" >}}
The Azure identity used for rotation must have the `Application.ReadWrite.All` Graph API permission, or the identity must be added as an Owner of the specific app registration whose secrets will be rotated.
{{< /notes >}}

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

Create a new environment for your rotator. If you have the existing credentials, set them in the `state` object so the rotator will treat them as the `current` credentials.

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

Once this is set up, you're ready to go! You never need to worry about your client secrets expiring, and you will always have the latest credentials in your ESC Environment.

## Learn more

The `fn::rotate::azure-app-secret` rotator is available now in all Pulumi ESC environments. For more information, check out the [fn::rotate::azure-app-secret documentation](/docs/esc/integrations/rotated-secrets/azure-app-secret/)!

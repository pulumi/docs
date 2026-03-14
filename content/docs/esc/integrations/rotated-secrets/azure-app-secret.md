---
title: azure-app-secret
title_tag: azure-app-secret Pulumi ESC Rotator
meta_desc: The `azure-app-secret` rotator enables you to rotate client secrets for an Azure app registration.
h1: azure-app-secret
menu:
  esc:
    identifier: azure-app-secret-rotator
    parent: esc-rotated-secrets
    weight: 1
---

The `azure-app-secret` rotator enables you to rotate client secrets for an Azure app registration in your Environment. Check out the [azure-login documentation](/docs/esc/integrations/dynamic-login-credentials/azure-login/) to learn more about authenticating with Azure.

## Example

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

```yaml
# my-org/rotators/secret-rotator
values:
  appSecret:
    fn::rotate::azure-app-secret:
      inputs:
        login: ${environments.logins.production.azure.login}
        clientId: <target-app-client-id>
        lifetimeInDays: 180
```

If you have an existing client secret you want ESC to keep track of, you can optionally provide an initial `state`.

```yaml
# my-org/rotators/secret-rotator
values:
  appSecret:
    fn::rotate::azure-app-secret:
      inputs:
        login: ${environments.logins.production.azure.login}
        clientId: <target-app-client-id>
      state:
        current:
          secretValue:
            fn::secret: <secret-value>
          secretId: <key-id>
          createdAt: "2025-01-01T12:00:00Z"
          expiresAt: "2025-07-01T12:00:00Z"
```

## Configuring OIDC

To learn how to configure OpenID Connect (OIDC) between Pulumi Cloud and Azure, see the [OpenID Connect integration](/docs/esc/guides/configuring-oidc/azure/) documentation. Once you have completed these steps, you can validate that your configuration is working by running either of the following:

* `esc open <org>/<project>/<environment>` command of the [Pulumi ESC CLI](/docs/esc-cli/)
* `pulumi env open <org>/<project>/<environment>` command of the [Pulumi CLI](/docs/install/)

Make sure to replace `<org>`, `<project>`, and `<environment>` with the values of your Pulumi organization and environment identifier respectively. You should see output similar to the following:

```json
{
  "azure": {
    "login": {
      "clientId": "b537....",
      "clientSecret": "[secret]",
      "subscriptionId": "0282....",
      "tenantId": "7060...."
    }
  },
  "appSecret": {
    "current": {
      "secretValue": "[secret]",
      "secretId": "a1b2c3d4-...",
      "createdAt": "2025-01-01T12:00:00Z",
      "expiresAt": "2025-07-01T12:00:00Z"
    },
    "previous": {
      "secretValue": "[secret]",
      "secretId": "e5f6g7h8-...",
      "createdAt": "2024-07-01T12:00:00Z",
      "expiresAt": "2025-01-01T12:00:00Z"
    }
  }
}
```

### Permissions

The Azure identity used for rotation must have the following Microsoft Graph API permissions:

- `Application.ReadWrite.All` - to read applications and manage their client secrets

Alternatively, the identity can be added as an **Owner** of the specific app registration whose secrets will be rotated.

## Inputs

| Property         | Type                                              | Description                                                                                           |
|------------------|---------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| `login`          | [AzureLogin](#azurelogin)                         | The credentials to use to log in to Azure.                                                            |
| `clientId`       | string                                            | The Application (client) ID of the app registration whose secret should be rotated.                   |
| `lifetimeInDays` | number                                            | [Optional] - The number of days the secret should be valid. Defaults to 180. Maximum is 730.          |

## State (Optional)

| Property   | Type                                                          | Description                                                                                                            |
|------------|---------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| `current`  | [AzureAppSecretOutputs](#azureappsecretoutputs)               | [Optional] - Current credential information. These are the newest and recommended credentials.                         |
| `previous` | [AzureAppSecretOutputs](#azureappsecretoutputs)               | [Optional] - Previous credential information. These credentials are still valid, but will be phased out next rotation. |

### AzureLogin

| Property         | Type   | Description                                                     |
|------------------|--------|-----------------------------------------------------------------|
| `clientId`       | string | The client ID to use.                                           |
| `tenantId`       | string | The tenant ID to use.                                           |
| `subscriptionId` | string | The subscription ID to use.                                     |
| `clientSecret`   | string | [Optional] - The client secret to use for authentication.       |
| `oidc`           | object | [Optional] - OIDC-related data, if OIDC is used for authentication. |

## Outputs

| Property   | Type                                                          | Description                                                                                               |
|------------|---------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| `current`  | [AzureAppSecretOutputs](#azureappsecretoutputs)               | Current credential information. These are the newest and recommended credentials.                         |
| `previous` | [AzureAppSecretOutputs](#azureappsecretoutputs)               | Previous credential information. These credentials are still valid, but will be phased out next rotation. |

### AzureAppSecretOutputs

| Property      | Type   | Description                                         |
|---------------|--------|-----------------------------------------------------|
| `secretValue` | string | The client secret value, stored as a secret.        |
| `secretId`    | string | The key ID of the client secret.                    |
| `createdAt`   | string | The creation timestamp of the secret (RFC3339).     |
| `expiresAt`   | string | The expiration timestamp of the secret (RFC3339).   |

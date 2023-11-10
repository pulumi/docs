---
title_tag: azure-secrets Pulumi ESC Provider
meta_desc: The azure-secrets Pulumi ESC Provider enables you to dynamically import Secrets from Azure Key Vault into your Environment.
title: azure-secrets
h1: azure-secrets
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    pulumicloud:
        identifier: azure-secrets
        parent: esc-providers
        weight: 4
---

The `azure-secrets` provider enables you to dynamically import Secrets and Configuration from Azure Key Vault into your Environment. The provider will return a map of names to Secrets.

## Example

```yaml
  azure:
    login:
      fn::open::azure-login:
        clientId: aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee
        tenantId: aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee
        subscriptionId: /subscriptions/00000000-0000-0000-0000-000000000000
        oidc: true
    secrets:
      fn::open::azure-secrets:
        login: ${azure.login}
        vault: example-vault-name
        get:
          api-key:
            name: api-key
          app-secret:
            name: app-secret
```

## Configuring OIDC

To configure OIDC between Pulumi Cloud and Azure, see the [relevant Pulumi documentation](/docs/pulumi-cloud/oidc/azure/). Once you have completed these steps, you can validate that your configuration is working by running either of the following:

* `esc open <your-org>/<your-environment>` command of the [Pulumi ESC CLI](/docs/esc-cli/)
* `pulumi env open <your-org>/<your-environment>` command of the [Pulumi CLI](/docs/install/)

Make sure to replace `<your-org>` and `<your-environment>` with the values of your Pulumi organization and environment file respectively. You should see output similar to the following:

```bash
{
  "azure": {
    "login": {
      "clientId": "b537....",
      "oidc": {
        "token": "eyJh...."
      },
      "subscriptionId": "0282....",
      "tenantId": "7061...."
    },
    "secrets": {
      "api-key": "my-api-key",
      "app-secret": "my-app-secret"
    }
  }
}
```

## Inputs

| Property | Type                                           | Description                                                                                                              |
|----------|------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| `login`  | [AzureSecretsLogin](#azuresecretslogin)        | Credentials used to log in to Azure.                                                                                     |
| `vault`  | string                                         | The vault to read from.                                                                                                  |
| `get`    | map[string][AzureSecretsGet](#azuresecretsget) | A map from names to secrets to read from Azure Key Vault. The outputs will map each name to the secret's sensitive data. |

### AzureSecretsLogin

| Property         | Type                              | Description                                                         |
|------------------|-----------------------------------|---------------------------------------------------------------------|
| `clientId`       | string                            | The configured client ID                                            |
| `tenantId`       | string                            | The configured tenant ID                                            |
| `subscriptionId` | string                            | The configured subscription ID                                      |
| `clientSecret`   | string                            | [Optional] - The client secret used for authentication, if any.     |
| `oidc`           | [AzureLoginOIDC](#azureloginoidc) | [Optional] - OIDC-related data, if OIDC is used for authentication. |

### AzureLoginOIDC

| Property | Type     | Description                               |
|----------|----------|-------------------------------------------|
| `token`  | string   | The OIDC token to use for authentication. |

### AzureSecretsGet

| Property       | Type   | Description                                       |
|----------------|--------|---------------------------------------------------|
| `name`         | string | The name of the secret to import.                 |
| `version`      | string | [Optional] - The version of the secret to import. |

### Outputs

| Property | Type   | Description                         |
|----------|--------|-------------------------------------|
| N/A      | object | A map of names to imported Secrets. |

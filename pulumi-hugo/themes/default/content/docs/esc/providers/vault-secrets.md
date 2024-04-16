---
title_tag: vault-secrets Pulumi ESC Provider
meta_desc: The `vault-secrets` provider enables you to dynamically import Secrets from HashiCorp Vault into your Environment.
title: vault-secrets
h1: vault-secrets
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  pulumiesc:
    identifier: vault-secrets
    parent: esc-providers
    weight: 9
aliases:
- /docs/pulumi-cloud/esc/providers/vault-secrets/
---

The `vault-secrets` provider enables you to dynamically import Secrets from HashiCorp Vault into your Environment. The provider will return a map of names to Secrets.

## Example

```yaml
  vault:
    login:
      fn::open::vault-login:
        address: https://127.0.0.1:8200/
        jwt:
          role: example-role
    secrets:
      fn::open::vault-secrets:
        login: ${vault.login}
        read:
          api-key:
            path: api-key
          app-secret:
            path: app-secret
```

## Configuring OIDC

To learn how to configure OpenID Connect (OIDC) between Pulumi Cloud and Vault, see the [OpenID Connect integration](/docs/pulumi-cloud/oidc/provider/vault/) documentation. Once you have completed these steps, you can validate that your configuration is working by running either of the following:

* `esc open <your-org>/<your-environment>` command of the [Pulumi ESC CLI](/docs/esc-cli/)
* `pulumi env open <your-org>/<your-environment>` command of the [Pulumi CLI](/docs/install/)

Make sure to replace `<your-org>` and `<your-environment>` with the values of your Pulumi organization and environment file respectively. You should see output similar to the following:

```json
{
  "vault": {
    "login": {
      "address": "***",
      "token": "***"
    },
    "secrets": {
      "test1": {
        "data": {
          "keyA": "valA",
          "keyB": "valB"
        },
        "metadata": {
          "created_time": "2023-11-06T18:24:05.784222Z",
          "custom_metadata": null,
          "deletion_time": "",
          "destroyed": false,
          "version": 1
        }
      }
    }
  }
}
```

## Inputs

| Property | Type                                             | Description                                                                                                    |
|----------|--------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| `login`  | [VaultSecretsLogin](#vaultsecretslogin)          | Credentials used to log in to HashiCorp Vault.                                                                 |
| `read`   | map[string][VaultSecretsRead](#vaultsecretsread) | A map of names to paths to read from the server. The outputs will map each name to the raw data for the value. |

### VaultSecretsLogin

| Property    | Type   | Description                                                                   |
|-------------|--------|-------------------------------------------------------------------------------|
| `address`   | string | The URL of the vault server. Must contain a scheme and hostname, but no path. |
| `namespace` | string | [Optional] The namespace to use for the session.                              |
| `token`     | string | The token to use for authentication.                                          |

#### VaultSecretsRead

| Property | Type   | Description                                  |
|----------|--------|----------------------------------------------|
| `path`   | string | The path to read.                            |
| `field`  | string | [Optional] - The field of the value to read. |

### Outputs

| Property | Type   | Description                                             |
|----------|--------|---------------------------------------------------------|
| N/A      | object | A map from names to raw values as read from the server (`vault.secrets.<key-name>`). |

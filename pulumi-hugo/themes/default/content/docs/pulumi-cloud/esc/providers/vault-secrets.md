---
title_tag: vault-secrets Pulumi ESC Provider
meta_desc: The `vault-secrets` provider enables you to dynamically import Secrets from HashiCorp Vault into your Environment.
title: vault-secrets
h1: vault-secrets
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  pulumicloud:
    identifier: vault-secrets
    parent: esc-providers
    weight: 8
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

## Inputs

| Property | Type                                             | Description                                                                                                    |
|----------|--------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| `login`  | [VaultSecretsLogin](#vaultsecretslogin)          | Credentials used to log in to HashiCorp Vault.                                                                 |
| `read`   | map[string][VaultSecretsRead](#vaultsecretsread) | A map of names to paths to read from the server. The outputs will map each name to the raw data for the value. |

### VaultSecretsLogin

| Property  | Type   | Description                                                                   |
|-----------|--------|-------------------------------------------------------------------------------|
| `address` | string | The URL of the vault server. Must contain a scheme and hostname, but no path. |
| `token`   | string | The token to use for authentication.                                          |

#### VaultSecretsRead

| Property | Type   | Description                                  |
|----------|--------|----------------------------------------------|
| `path`   | string | The path to read.                            |
| `field`  | string | [Optional] - The field of the value to read. |

### Outputs

| Property | Type   | Description                                             |
|----------|--------|---------------------------------------------------------|
| N/A      | object | A map from names to raw values as read from the server. |

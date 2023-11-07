---
title_tag: vault-login Pulumi ESC Provider
meta_desc: The vault-login Pulumi ESC Provider enables you to log in to HashiCorp Vault using OpenID Connect or by providing static credentials.
title: vault-login
h1: vault-login
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  pulumicloud:
    identifier: vault-login
    parent: esc-providers
    weight: 7
---

The `vault-login` provider enables you to log in to HashiCorp Vault using OpenID Connect or by providing static credentials. The provider will return a set of credentials that can be used to fetch secrets using the `vault-secrets` provider.

Want to use this with OIDC? See [the docs](../../oidc/vault.md).

## Example

```yaml
  vault:
    login:
      fn::open::vault-login:
        address: https://127.0.0.1:8200/
        jwt:
          role: example-role
```

## Inputs

| Property  | Type                                | Description                                                                                                               |
|-----------|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| `address` | string                              | The URL of the Vault server. Must contain a scheme and hostname, but no path.                                             |
| `jwt`     | [VaultLoginJWT](#vaultloginjwt)     | [Optional] Options for JWT login. JWT login uses an OIDC token issued by the Pulumi Cloud to generate an ephemeral token. |
| `token`   | [VaultLoginToken](#vaultlogintoken) | [Optional] Options for token login. Token login creates an ephemeral child token.                                         |

### VaultLoginJWT

| Property | Type   | Description                                               |
|----------|--------|-----------------------------------------------------------|
| `role`   | string | The name of the role to use for login.                    |
| `mount`  | string | [Optional] - The name of the authentication engine mount. Defaults to `jwt`. |

### VaultLoginToken

| Property      | Type   | Description                                                                 |
|---------------|--------|-----------------------------------------------------------------------------|
| `token`       | string | The parent token.                                                           |
| `displayName` | string | [Optional] - The display name of the ephemeral token. Defaults to 'pulumi'. |
| `maxTtl`      | string | [Optional] - The maximum TTL of the ephemeral token.                        |

## Outputs

| Property    | Type   | Description                                    |
|-------------|--------|------------------------------------------------|
| `address`   | string | The URL of the vault server.                   |
| `token`     | string | The ephemeral token generated for the session. |

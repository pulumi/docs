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

## Example

```yaml
  vault:
    login:
      fn::open::vault-login:
        address: https://127.0.0.1:8200/
        jwt:
          role: example-role
```

## Configuring OIDC in Vault
To add Pulumi Cloud as an OIDC provider in Vault you'll need to do the following:
- Enable the [`JWT` auth method](https://developer.hashicorp.com/vault/docs/auth/jwt)
- Create an associated role

### Enable JWT Auth Method
To enable the [JWT auth method](https://developer.hashicorp.com/vault/docs/auth/jwt) in Vault:
```
$ vault auth enable -path=jwt jwt
Success! Enabled jwt auth method at: jwt/

$ vault write auth/jwt/config \
    oidc_discovery_url="https://api.pulumi.com/oidc" \
    bound_issuer="https://api.pulumi.com/oidc"
Success! Data written to: auth/jwt/config
```

### Create JWT Role
To create a [role](https://developer.hashicorp.com/vault/api-docs/auth/jwt#create-update-role) (assumes existing policy `myExamplePolicy`) using the CLI:
```
vault write auth/jwt/role/<role name> \
  bound_audiences="<org name>"
  user_claim="sub" \
  token_policies=myExamplePolicy \
  allowed_redirect_uris=<vault url>/jwt/callback \
  role_type=jwt
```

If you want to use `bound_claims` you'll need to specify the role configuration [as JSON](https://developer.hashicorp.com/vault/docs/auth/jwt#oidc-configuration-troubleshooting):
```
$ vault write auth/jwt/role/<role name> -<<EOF
{
  "user_claim": "sub",
  "bound_audiences": "<org name>",
  "role_type": "jwt",
  "policies": "myExamplePolicy",
  "bound_claims": { "env": ["<environment name>","<another environment name>"] },
  "allowed_redirect_uris": ["<vault url>/jwt/callback"]
}
EOF
```

Pulumi Cloud passes the following JWT structure to Vault:
```
{
  "aud": "<org name>",
  "env": "<environment name>",
  "exp": 1699300519,
  "iat": 1699296919,
  "iss": "https://api.pulumi.com/oidc",
  "nbf": 1699296919,
  "org": "<org name>",
  "sub": "pulumi:environments:org:<org name>:env:<environment name>"
}
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
| `mount`  | string | [Optional] - The name of the authentication engine mount. |

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

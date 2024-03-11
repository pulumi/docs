---
title_tag: vault-login Pulumi ESC Provider
meta_desc: The vault-login Pulumi ESC Provider enables you to log in to HashiCorp Vault using OpenID Connect or by providing static credentials.
title: vault-login
h1: vault-login
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  pulumiesc:
    identifier: vault-login
    parent: esc-providers
    weight: 8
aliases:
- /docs/pulumi-cloud/esc/providers/vault-login/
---

The `vault-login` provider enables you to log in to HashiCorp Vault using OpenID Connect or by providing static credentials. The provider will return a set of credentials that can be used to fetch secrets using the `vault-secrets` provider.

## Examples

```yaml
  vault:
    login:
      fn::open::vault-login:
        address: https://127.0.0.1:8200/
        jwt:
          role: example-role
```

```yaml
  vault:
    login:
      fn::open::vault-login:
        address: https://sample-cluster-public-vault-12345678.8ca2e2af.z1.hashicorp.cloud:8200
        namespace: admin/example
        token:
          displayName: esc-token
          token:
            fn::secret: redacted
          policies: [kv-read]
```

## Configuring OIDC

To learn how to configure OpenID Connect (OIDC) between Pulumi Cloud and Vault, see the [OpenID Connect integration](/docs/pulumi-cloud/oidc/vault/) documentation.

## Inputs

| Property    | Type                                | Description                                                                                                               |
|-------------|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| `address`   | string                              | The URL of the Vault server. Must contain a scheme and hostname, but no path.                                             |
| `namespace` | string                              | [Optional] The namespace to log in to. Only available for Vault Enterprise.                                               |
| `jwt`       | [VaultLoginJWT](#vaultloginjwt)     | [Optional] Options for JWT login. JWT login uses an OIDC token issued by the Pulumi Cloud to generate an ephemeral token. |
| `token`     | [VaultLoginToken](#vaultlogintoken) | [Optional] Options for token login. Token login creates an ephemeral child token.                                         |

### VaultLoginJWT

| Property | Type   | Description                                               |
|----------|--------|-----------------------------------------------------------|
| `role`   | string | The name of the role to use for login.                    |
| `mount`  | string | [Optional] - The name of the authentication engine mount. Defaults to `jwt`. |
| `subjectAttributes`  | string[] | [Optional] - Subject attributes to be included in the OIDC token. For more information see the see the [OpenID subject customization](/docs/pulumi-cloud/oidc/vault#subject-customization) documentation |

### VaultLoginToken

| Property      | Type     | Description                                                                 |
|---------------|----------|-----------------------------------------------------------------------------|
| `token`       | string   | The parent token.                                                           |
| `displayName` | string   | [Optional] - The display name of the ephemeral token. Defaults to 'pulumi'. |
| `maxTtl`      | string   | [Optional] - The maximum TTL of the ephemeral token.                        |
| `metadata`    | object   | [Optional] - Arbitrary metadata to associate with the ephemeral token.      |
| `policies`    | string[] | [Optional] - List of policies for the token.                                |

## Outputs

| Property      | Type   | Description                                        |
|---------------|--------|----------------------------------------------------|
| `address`     | string | The URL of the vault server.                       |
| `namespace`   | string | [Optional] - The namespace to use for the session. |
| `token`       | string | The ephemeral token generated for the session.     |

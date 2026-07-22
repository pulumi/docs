---
title_tag: vault-login Pulumi ESC Provider
meta_desc: The vault-login Pulumi ESC Provider enables you to log in to HashiCorp Vault using OpenID Connect or by providing static credentials.
title: vault-login
h1: vault-login
menu:
  esc:
    identifier: vault-login
    parent: esc-providers-login
    weight: 9
aliases:
    - /docs/pulumi-cloud/esc/providers/vault-login/
    - /docs/esc/providers/vault-login/
    - /docs/esc/integrations/dynamic-login-credentials/vault-login/
    - /docs/esc/concepts/providers/login/vault-login/
---

The `vault-login` provider enables you to log in to HashiCorp Vault using OpenID Connect or by providing static credentials. The provider will return a set of credentials that can be used to fetch secrets using the `vault-secrets` provider.

## Examples

```yaml
values:
  vault:
    login:
      fn::open::vault-login:
        address: https://127.0.0.1:8200/
        jwt:
          role: example-role
  environmentVariables:
    # Consumed by the Vault CLI and the Pulumi Vault provider
    VAULT_ADDR: ${vault.login.address}
    VAULT_TOKEN: ${vault.login.token}
```

```yaml
values:
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
  environmentVariables:
    # Consumed by the Vault CLI and the Pulumi Vault provider
    VAULT_ADDR: ${vault.login.address}
    VAULT_TOKEN: ${vault.login.token}
    VAULT_NAMESPACE: ${vault.login.namespace}
```

## Schema reference

{{< esc-schema-updated >}}

### Inputs

{{< esc-schema type="provider" name="vault-login" section="inputs" >}}

### Outputs

{{< esc-schema type="provider" name="vault-login" section="outputs" >}}

## Configuring OIDC

To learn how to configure OpenID Connect (OIDC) between Pulumi Cloud and Vault, see the [OpenID Connect integration](/docs/esc/guides/configuring-oidc/vault/) documentation.

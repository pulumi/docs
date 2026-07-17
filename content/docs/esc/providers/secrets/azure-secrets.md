---
title: azure-secrets
title_tag: azure-secrets Pulumi ESC provider
meta_desc: The azure-secrets Pulumi ESC Provider enables you to dynamically import secrets from Azure Key Vault into your environment.
h1: azure-secrets
menu:
  esc:
    identifier: azure-secrets
    parent: esc-providers-secrets
    weight: 1
aliases:
    - /docs/pulumi-cloud/esc/providers/azure-secrets/
    - /docs/esc/providers/azure-secrets/
    - /docs/esc/integrations/dynamic-secrets/azure-secrets/
    - /docs/esc/concepts/providers/secrets/azure-secrets/
---

The `azure-secrets` provider enables you to dynamically import Secrets and Configuration from Azure Key Vault into your Environment. The provider will return a map of names to Secrets.

## Example

```yaml
values:
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
  pulumiConfig:
    apiKey: ${azure.secrets.api-key}
    appSecret: ${azure.secrets.app-secret}
```

## Schema reference

{{< esc-schema-updated >}}

### Inputs

{{< esc-schema type="provider" name="azure-secrets" section="inputs" >}}

### Outputs

{{< esc-schema type="provider" name="azure-secrets" section="outputs" >}}

## Configuring OIDC

To learn how to configure OpenID Connect (OIDC) between Pulumi Cloud and Azure, see the [OpenID Connect integration](/docs/esc/guides/configuring-oidc/azure/) documentation. Once you have completed these steps, you can validate that your configuration is working by running either of the following:

* `pulumi env open <org>/<project>/<environment>` command of the [Pulumi CLI](/docs/iac/cli/commands/pulumi_env_open/)
* `pulumi env open <org>/<project>/<environment>` command of the [Pulumi CLI](/docs/install/)

Make sure to replace `<org>`, `<project>`, and `<environment>` with the values of your Pulumi organization and environment identifier respectively. You should see output similar to the following:

```json
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

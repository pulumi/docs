---
title: infisical-secrets
title_tag: infisical-secrets Pulumi ESC provider
meta_desc: The infisical-secrets Pulumi ESC Provider enables you to dynamically import secrets from Infisical into your environment.
h1: infisical-secrets
menu:
  esc:
    identifier: infisical-secrets
    parent: esc-providers-secrets
    weight: 1
aliases:
  - /docs/pulumi-cloud/esc/providers/infisical-secrets/
  - /docs/esc/providers/infisical-secrets/
  - /docs/esc/integrations/dynamic-secrets/infisical-secrets/
  - /docs/esc/concepts/providers/secrets/infisical-secrets/
---

The `infisical-secrets` provider enables you to dynamically import Secrets from Infisical Secrets into
your Environment. The provider will return a map of names to Secrets.

## Example

```yaml
values:
  infisical:
    login:
      fn::open::infisical-login:
        oidc:
          identityId: aaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee
    secrets:
      fn::open::infisical-secrets:
        login: ${infisical.login}
        get:
          api-key:
            projectId: xxxxxxx-bbbb-cccc-dddd-eeeeeeeeeeee
            environment: prod
            secretKey: api-key
          app-secret:
            projectId: xxxxxxx-bbbb-cccc-dddd-eeeeeeeeeeee
            environment: dev
            secretKey: app-secret
  pulumiConfig:
    apiKey: ${infisical.secrets.api-key}
    appSecret: ${infisical.secrets.app-secret}
```

## Schema reference

{{< esc-schema-updated >}}

### Inputs

{{< esc-schema type="provider" name="infisical-secrets" section="inputs" >}}

### Outputs

{{< esc-schema type="provider" name="infisical-secrets" section="outputs" >}}

## Configuring OIDC

To learn how to configure OpenID Connect (OIDC) between Pulumi Cloud and Infisical, see
the [OpenID Connect integration](/docs/esc/guides/configuring-oidc/infisical/) documentation. Once you have completed
these steps, you can validate that your configuration is working by running either of the following:

* `pulumi env open <org>/<project>/<environment>` command of the [Pulumi CLI](/docs/iac/cli/commands/pulumi_env_open/)
* `pulumi env open <org>/<project>/<environment>` command of the [Pulumi CLI](/docs/install/)

Make sure to replace `<org>`, `<project>`, and `<environment>` with the values of your Pulumi organization and
environment identifier respectively. You should see output similar to the following:

```json
{
  "infisical": {
    "login": {
      "accessToken": "eyJh...."
    },
    "secrets": {
      "api-key": "my-api-key",
      "app-secret": "my-app-secret"
    }
  }
}
```

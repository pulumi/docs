---
title: gcp-secrets
title_tag: gcp-secrets Pulumi ESC provider
meta_desc: The gcp-secrets Pulumi ESC provider enables you to dynamically import secrets from Google Cloud Secrets Manager into your environment.
h1: gcp-secrets
menu:
  esc:
    identifier: gcp-secrets
    parent: esc-providers-secrets
    weight: 1
aliases:
    - /docs/pulumi-cloud/esc/providers/gcp-secrets/
    - /docs/esc/providers/gcp-secrets/
    - /docs/esc/integrations/dynamic-secrets/gcp-secrets/
    - /docs/esc/concepts/providers/secrets/gcp-secrets/
---

The `gcp-secrets` provider enables you to dynamically import Secrets from Google Cloud Secrets Manager into your Environment. The provider will return a map of names to Secrets.

## Example

```yaml
values:
  gcp:
    login:
      fn::open::gcp-login:
        project: 123456789
        oidc:
          workloadPoolId: pulumi-esc
          providerId: pulumi-esc
          serviceAccount: pulumi-esc@foo-bar-123456.iam.gserviceaccount.com
    secrets:
      fn::open::gcp-secrets:
        login: ${gcp.login}
        access:
          api-key:
            name: api-key
          app-secret:
            name: app-secret
  pulumiConfig:
    apiKey: ${gcp.secrets.api-key}
    appSecret: ${gcp.secrets.app-secret}
```

## Schema reference

{{< esc-schema-updated >}}

### Inputs

{{< esc-schema type="provider" name="gcp-secrets" section="inputs" >}}

### Outputs

{{< esc-schema type="provider" name="gcp-secrets" section="outputs" >}}

## Configuring OIDC

To learn how to configure OpenID Connect (OIDC) between Pulumi Cloud and Google Cloud, see the [OpenID Connect integration](/docs/esc/guides/configuring-oidc/gcp/) documentation. Once you have completed these steps, you can validate that your configuration is working by running either of the following:

* `pulumi env open <org>/<project>/<environment>` command of the [Pulumi CLI](/docs/iac/cli/commands/pulumi_env_open/)
* `pulumi env open <org>/<project>/<environment>` command of the [Pulumi CLI](/docs/install/)

Make sure to replace `<org>`, `<project>`, and `<environment>` with the values of your Pulumi organization and environment identifier respectively. You should see output similar to the following:

```json
{
  "gcp": {
    "login": {
      "accessToken": "ya29.....",
      "expiry": "2023-11-09T11:12:41Z",
      "project": 123456789,
      "tokenType": "Bearer"
    },
    "secrets": {
      "api-key": "my-api-key",
      "app-secret": "my-app-secret"
    }
  }
}
```

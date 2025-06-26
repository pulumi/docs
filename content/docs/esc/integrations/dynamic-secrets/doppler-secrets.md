---
title: doppler-secrets
title_tag: doppler-secrets Pulumi ESC provider
meta_desc: The doppler-secrets Pulumi ESC Provider enables you to dynamically import secrets from Doppler into your environment.
h1: doppler-secrets
menu:
  esc:
    identifier: doppler-secrets
    parent: esc-dynamic-secrets
    weight: 5
aliases:
  - /docs/pulumi-cloud/esc/providers/doppler-secrets/
  - /docs/esc/providers/doppler-secrets/
---

The `doppler-secrets` provider enables you to dynamically import Secrets from Doppler into
your Environment. The provider will return a map of names to Secrets.

## Example

```yaml
values:
  doppler:
    login:
      fn::open::doppler-login:
        oidc:
          identityId: 00000000-0000-0000-0000-000000000000
    secrets:
      fn::open::doppler-secrets:
        login: ${doppler.login}
        project: example-project
        config: dev
        get:
          api-key:
            name: API_KEY
          app-secret:
            name: APP_SECRET
```

## Configuring OIDC

To learn how to configure OpenID Connect (OIDC) between Pulumi Cloud and Doppler, see
the [OpenID Connect integration](/docs/pulumi-cloud/oidc/provider/doppler/) documentation. Once you have completed
these steps, you can validate that your configuration is working by running either of the following:

* `esc open <org>/<project>/<environment>` command of the [Pulumi ESC CLI](/docs/esc-cli/)
* `pulumi env open <org>/<project>/<environment>` command of the [Pulumi CLI](/docs/install/)

Make sure to replace `<org>`, `<project>`, and `<environment>` with the values of your Pulumi organization and
environment identifier respectively. You should see output similar to the following:

```json
{
  "doppler": {
    "login": {
      "accessToken": "dp.said.XXX..."
    },
    "secrets": {
      "api-key": "my-api-key",
      "app-secret": "my-app-secret"
    }
  }
}
```

## Inputs

| Property | Type                                                   | Description                                                                                                                |
|----------|--------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| `login`  | [DopplerSecretsLogin](#dopplersecretslogin)        | Credentials to use to log in to Doppler.                                                                                 |
| `project`   | string | The project identifier in Doppler |
| `config`   | string | The config identifier in Doppler |
| `get`    | map[string][DopplerSecretsGet](#dopplersecretsget) | A map from names to secrets to read from Doppler Secrets. The outputs will map each name to the secret's sensitive data. |

### DopplerSecretsLogin

| Property      | Type   | Description |
|---------------|--------|---------------------------------------------------------------------------------------------------------------------------|
| `accessToken` | string | The access token to use for authentication.                                                                               |

### DopplerSecretsGet

| Property      | Type   | Description |
|---------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name`   | string | The secret name in Doppler |

### Outputs

| Property | Type   | Description                         |
|----------|--------|-------------------------------------|
| N/A      | object | A map of names to imported Secrets. |

---
title: infisical-secrets
title_tag: infisical-secrets Pulumi ESC provider
meta_desc: The infisical-secrets Pulumi ESC Provider enables you to dynamically import secrets from Infisical into your environment.
h1: infisical-secrets
menu:
  esc:
    identifier: infisical-secrets
    parent: esc-dynamic-secrets
    weight: 3
aliases:
  - /docs/pulumi-cloud/esc/providers/infisical-secrets/
  - /docs/esc/providers/infisical-secrets/
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
```

## Configuring OIDC

To learn how to configure OpenID Connect (OIDC) between Pulumi Cloud and Infisical, see
the [OpenID Connect integration](/docs/pulumi-cloud/oidc/provider/infisical/) documentation. Once you have completed
these steps, you can validate that your configuration is working by running either of the following:

* `esc open <org>/<project>/<environment>` command of the [Pulumi ESC CLI](/docs/esc-cli/)
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

## Inputs

| Property | Type                                                   | Description                                                                                                                |
|----------|--------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| `login`  | [InfisicalSecretsLogin](#infisicalsecretslogin)        | Credentials to use to log in to Infisical.                                                                                 |
| `get`    | map[string][InfisicalSecretsGet](#infisicalsecretsget) | A map from names to secrets to read from Infisical Secrets. The outputs will map each name to the secret's sensitive data. |

### InfisicalSecretsLogin

| Property      | Type   | Description                                                                                                               |
|---------------|--------|---------------------------------------------------------------------------------------------------------------------------|
| `siteUrl`     | string | [Optional] - The base URL of the Infisical instance you authenticated to. May be omitted if default US instance was used. |
| `accessToken` | string | The access token to use for authentication.                                                                               |

### InfisicalSecretsGet

| Property      | Type   | Description                                                                                                                                                                                                                                                                       |
|---------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `projectId`   | string | The projectId of the project the secret lives in. In the Infisical web app, navigate to your Secrets project, click on *Project Settings*, and click the *Copy Project ID* button.                                                                                                |
| `environment` | string | The environment slug of the environment the secret lives in. In the Infisical web app, navigate to your Secrets project, click on *Project Settings*, and find the slug in the *Environments* list. Default values are `dev`, `staging`, and `prod`                               |
| `secretKey`   | string | The name of the secret to import.                                                                                                                                                                                                                                                 |
| `secretPath`  | string | [Optional] - The path inside the environment where the secret lives. For example, if your secret `dbPassword` lives within `DatabaseDetails` folder. The path would be `/DatabaseDetails`. If secretPath is not specified, the default path is `/` - the root environment folder. |
| `type`        | string | [Optional] - The secret type, either `shared` or `personal`.                                                                                                                                                                                                                      |

### Outputs

| Property | Type   | Description                         |
|----------|--------|-------------------------------------|
| N/A      | object | A map of names to imported Secrets. |

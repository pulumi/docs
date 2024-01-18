---
title_tag: gcp-secrets Pulumi ESC Provider
meta_desc: The gcp-secrets Pulumi ESC Provider enables you to dynamically import Secrets from Google Cloud Secrets Manager into your Environment.
title: gcp-secrets
h1: gcp-secrets
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  pulumiesc:
    identifier: gcp-secrets
    parent: esc-providers
    weight: 6
aliases:
- /docs/pulumi-cloud/esc/providers/gcp-secrets/
---

The `gcp-secrets` provider enables you to dynamically import Secrets from Google Cloud Secrets Manager into your Environment. The provider will return a map of names to Secrets.

## Example

```yaml
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
```

## Configuring OIDC

To learn how to configure OpenID Connect (OIDC) between Pulumi Cloud and Google Cloud, see the [OpenID Connect integration](/docs/pulumi-cloud/oidc/gcp/) documentation. Once you have completed these steps, you can validate that your configuration is working by running either of the following:

* `esc open <your-org>/<your-environment>` command of the [Pulumi ESC CLI](/docs/esc-cli/)
* `pulumi env open <your-org>/<your-environment>` command of the [Pulumi CLI](/docs/install/)

Make sure to replace `<your-org>` and `<your-environment>` with the values of your Pulumi organization and environment file respectively. You should see output similar to the following:

```json
{
  "environmentVariables": {
    "GOOGLE_PROJECT": 111111111111
    "CLOUDSDK_AUTH_ACCESS_TOKEN": "ya29...."
  },
  "gcp": {
    "login": {
      "accessToken": "ya29.....",
      "expiry": "2023-11-09T11:12:41Z",
      "project": 111111111111,
      "tokenType": "Bearer"
    }
  },
  "pulumiConfig": {
    "gcp:accessToken": "ya29...."
  }
}
```

## Inputs

| Property | Type                                             | Description                                                                                                                           |
|----------|--------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| `login`  | [GCPSecretsLogin](#gcpsecretslogin)              | Credentials used to log in to Google Cloud.                                                                                           |
| `access` | map[string][GCPSecretsAccess](#gcpsecretsaccess) | A map from names to secrets to read from Google Cloud Secrets Manager. The outputs will map each name to the secret's sensitive data. |

### GCPSecretsLogin

| Property      | Type   | Description                                                                      |
|---------------|--------|----------------------------------------------------------------------------------|
| `project`     | string | The **numerical** ID of the GCP project, aka project number. (e.g. 951040570662) |
| `accessToken` | string | The access token used to authenticate with Google Cloud.                         |
| `tokenType`   | string | The type of the access token.                                                    |
| `expiry`      | string | [Optional] - The access token's expiry time.                                     |

#### GCPSecretsAccess

| Property       | Type   | Description                                       |
|----------------|--------|---------------------------------------------------|
| `name`         | string | The name of the secret to import.                 |
| `version`      | string | [Optional] - The version of the secret to import. |

### Outputs

| Property | Type   | Description                         |
|----------|--------|-------------------------------------|
| N/A      | object | A map of names to imported Secrets. |

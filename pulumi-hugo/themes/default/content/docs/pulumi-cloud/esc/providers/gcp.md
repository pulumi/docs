---
title_tag: Google Cloud ESC Providers
meta_desc: This page provides details of the Google Cloud ESC Providers.
title: Google Cloud
h1: Google Cloud Providers
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    pulumicloud:
        identifier: gcp
        parent: esc-providers
        weight: 3
---

The Google Cloud ESC Providers enable you to log in to Google Cloud using OIDC, as well as dynamically import Secrets from Google Cloud Secrets Manager into your Environment. They may be used in conjunction with each other or independently.

* [gcp-login](#gcp-login) - Log in to Google Cloud.
* [gcp-secrets](#gcp-secrets) - Import Secrets from Google Cloud Secrets Manager.

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

## gcp-login

The `gcp-login` provider enables you to log in to Google Cloud using OpenID Connect or by providing static credentials. The provider will return a set of credentials that can be used to access Google Cloud resources or fetch secrets using the `gcp-secrets` provider.

### Configuring OIDC

To create the Google Cloud Workload Identity Provider, see the [relevant Google Cloud documentation](https://cloud.google.com/iam/docs/workload-identity-federation-with-other-providers).

When following the instructions in the documentation:

* For the provider issuer, use `https://api.pulumi.com/oidc`
* For the audience, use the name of your organization
* Recall the [format of the subject claim](/docs/pulumi-cloud/esc/providers/#setting-up-oidc) when adding attribute conditions that check the value of the `google.subject` attribute

Make a note of the workload identity pool ID, provider ID, and service account email address as they will be necessary inputs to the `gcp-login` provider.

### Inputs

| Property      | Type                                        | Description                                                                      |
|---------------|---------------------------------------------|----------------------------------------------------------------------------------|
| `project`     | string                                      | The **numerical** ID of the GCP project, aka project number. (e.g. 951040570662) |
| `accessToken` | [GCPLoginAccessToken](#gcploginaccesstoken) | [Optional] Options for access token login.                                       |
| `oidc`        | [GCPLoginOIDC](#gcploginoidc)               | [Optional] Options for OIDC login.                                               |

#### GCPLoginAccessToken

| Property         | Type   | Description                                                                                  |
|------------------|--------|----------------------------------------------------------------------------------------------|
| `accessToken`    | string | The token used to authenticate with Google Cloud.                                            |
| `serviceAccount` | string | [Optional] - The service account to impersonate, if any.                                     |
| `tokenLifetime`  | string | [Optional] - The lifetime of the temporary credentials when impersonating a service account. |

#### GCPLoginOIDC

| Property         | Type   | Description                                                                |
|------------------|--------|----------------------------------------------------------------------------|
| `workloadPoolId` | string | The (short) ID of the workload pool to use.                                |
| `providerId`     | string | The (short) ID of the identity provider associated with the workload pool. |
| `serviceAccount` | string | The email address of the service account to use.                           |
| `region`         | string | [Optional] - The region of the GCP project.                                |
| `tokenLifetime`  | string | [Optional] - The lifetime of the temporary credentials.                    |

### Outputs

| Property      | Type   | Description                                                                      |
|---------------|--------|----------------------------------------------------------------------------------|
| `project`     | string | The **numerical** ID of the GCP project, aka project number. (e.g. 951040570662) |
| `accessToken` | string | The access token used to authenticate with Google Cloud.                         |
| `tokenType`   | string | The type of the access token.                                                    |
| `expiry`      | string | [Optional] - The access token's expiry time.                                     |

## gcp-secrets

The `gcp-secrets` provider enables you to dynamically import Secrets from Google Cloud Secrets Manager into your Environment. The provider will return a map of Secrets and/or Configuration.

### Inputs

| Property | Type                                       | Description                                                                                                                           |
|----------|--------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| `login`  | [GCPLoginOutputs](#outputs)                | Credentials used to log in to Google Cloud.                                                                                           |
| `access` | map[string][GCPSecretsGet](#gcpsecretsget) | A map from names to secrets to read from Google Cloud Secrets Manager. The outputs will map each name to the secret's sensitive data. |

#### GCPSecretsGet

| Property       | Type   | Description                                       |
|----------------|--------|---------------------------------------------------|
| `name`         | string | The name of the secret to import.                 |
| `version`      | string | [Optional] - The version of the secret to import. |

### Outputs

| Property | Type   | Description                         |
|----------|--------|-------------------------------------|
| N/A      | object | A map of names to imported Secrets. |

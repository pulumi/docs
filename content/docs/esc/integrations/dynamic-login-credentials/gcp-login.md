---
title_tag: gcp-login Pulumi ESC Provider
meta_desc: The gcp-login Pulumi ESC Provider enables you to log in to Google Cloud using OIDC or by providing static credentials.
title: gcp-login
h1: gcp-login
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  pulumiesc:
    identifier: gcp-login
    parent: esc-dynamic-login-credentials
    weight: 3
aliases:
    - /docs/pulumi-cloud/esc/providers/gcp-login/
    - /docs/esc/providers/gcp-login/
---

The `gcp-login` provider enables you to log in to Google Cloud using OpenID Connect or by providing static credentials. The provider will return a set of credentials that can be used to access Google Cloud resources or fetch secrets using the `gcp-secrets` provider.

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
```

## Configuring OIDC

To learn how to configure OpenID Connect (OIDC) between Pulumi Cloud and Google Cloud, see the [OpenID Connect integration](/docs/pulumi-cloud/oidc/provider/gcp/) documentation.

## Inputs

| Property      | Type                                        | Description                                                                      |
|---------------|---------------------------------------------|----------------------------------------------------------------------------------|
| `project`     | number                                      | The **numerical** ID of the GCP project, aka project number. (e.g. 951040570662) |
| `accessToken` | [GCPLoginAccessToken](#gcploginaccesstoken) | [Optional] Options for access token login.                                       |
| `oidc`        | [GCPLoginOIDC](#gcploginoidc)               | [Optional] Options for OIDC login.                                               |

### GCPLoginAccessToken

| Property         | Type   | Description                                                                                  |
|------------------|--------|----------------------------------------------------------------------------------------------|
| `accessToken`    | string | The token used to authenticate with Google Cloud.                                            |
| `serviceAccount` | string | [Optional] - The service account to impersonate, if any.                                     |
| `tokenLifetime`  | string | [Optional] - The lifetime of the temporary credentials when impersonating a service account. |

### GCPLoginOIDC

| Property         | Type   | Description                                                                |
|------------------|--------|----------------------------------------------------------------------------|
| `workloadPoolId` | string | The (short) ID of the workload pool to use.                                |
| `providerId`     | string | The (short) ID of the identity provider associated with the workload pool. |
| `serviceAccount` | string | The email address of the service account to use.                           |
| `region`         | string | [Optional] - The region of the GCP project.                                |
| `tokenLifetime`  | string | [Optional] - The lifetime of the temporary credentials.                    |
| `subjectAttributes`  | string[] | [Optional] - Subject attributes to be included in the OIDC token. For more information see the see the [OpenID subject customization](/docs/pulumi-cloud/oidc/provider/gcp#subject-customization) documentation |

## Outputs

| Property      | Type   | Description                                                                      |
|---------------|--------|----------------------------------------------------------------------------------|
| `project`     | string | The **numerical** ID of the GCP project, aka project number. (e.g. 951040570662) |
| `accessToken` | string | The access token used to authenticate with Google Cloud.                         |
| `tokenType`   | string | The type of the access token.                                                    |
| `expiry`      | string | [Optional] - The access token's expiry time.                                     |

---
title_tag: gcp-login Pulumi ESC Provider
meta_desc: The gcp-login Pulumi ESC Provider enables you to log in to Google Cloud using OIDC or by providing static credentials.
title: gcp-login
h1: gcp-login
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  esc:
    identifier: gcp-login
    parent: esc-providers-login
    weight: 5
aliases:
    - /docs/pulumi-cloud/esc/providers/gcp-login/
    - /docs/esc/providers/gcp-login/
    - /docs/esc/integrations/dynamic-login-credentials/gcp-login/
    - /docs/esc/concepts/providers/login/gcp-login/
---

The `gcp-login` provider enables you to log in to Google Cloud using OpenID Connect or by providing static credentials. The provider will return a set of credentials that can be used to access Google Cloud resources or fetch secrets using the `gcp-secrets` provider.

## Examples

### Using outputs with Pulumi IaC

The [Pulumi Google Cloud provider](https://www.pulumi.com/registry/packages/gcp/) reads the project and OAuth access token from the environment:

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
  environmentVariables:
    # The Pulumi Google Cloud provider reads the project (as a numeric ID) and the access token
    GOOGLE_CLOUD_PROJECT: ${gcp.login.project}
    GOOGLE_OAUTH_ACCESS_TOKEN: ${gcp.login.accessToken}
```

### Using outputs with the gcloud CLI

The `gcloud` CLI reads the project by name and the access token from its own `CLOUDSDK_*` environment variables, which differ from the ones the Pulumi provider uses:

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
  environmentVariables:
    # The gcloud CLI requires the project by name (not the numeric ID)
    # See: https://cloud.google.com/sdk/docs/properties#setting_properties_using_environment_variables
    CLOUDSDK_CORE_PROJECT: my-project-name
    CLOUDSDK_AUTH_ACCESS_TOKEN: ${gcp.login.accessToken}
```

## Configuring OIDC

To learn how to configure OpenID Connect (OIDC) between Pulumi Cloud and Google Cloud, see the [OpenID Connect integration](/docs/esc/guides/configuring-oidc/gcp/) documentation.

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
| `region`         | string | [Optional] - The location of the Workload Identity Pool. For standard Workload Identity Pools, this should be `global` (the default). Only specify a regional value if you have explicitly created a regional Workload Identity Pool. |
| `tokenLifetime`  | string | [Optional] - The lifetime of the temporary credentials.                    |
| `subjectAttributes`  | string[] | [Optional] - Subject attributes to be included in the OIDC token. For more information see the [OpenID subject customization](/docs/esc/guides/configuring-oidc/#custom-token-claim) documentation |

{{< notes type="info" >}}
If you encounter authentication errors with GCP OIDC, see the [GCP OIDC troubleshooting guide](/docs/esc/guides/configuring-oidc/gcp/#troubleshooting) for common issues and solutions.
{{< /notes >}}

## Outputs

| Property      | Type   | Description                                                                      |
|---------------|--------|----------------------------------------------------------------------------------|
| `project`     | string | The **numerical** ID of the GCP project, aka project number. (e.g. 951040570662) |
| `accessToken` | string | The access token used to authenticate with Google Cloud.                         |
| `tokenType`   | string | The type of the access token.                                                    |
| `expiry`      | string | [Optional] - The access token's expiry time.                                     |

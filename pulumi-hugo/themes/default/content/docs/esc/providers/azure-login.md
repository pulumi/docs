---
title_tag: azure-login Pulumi ESC Provider
meta_desc: The azure-login Pulumi ESC Provider enables you to log in to Azure using OIDC or static credentials.
title: azure-login
h1: azure-login
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    pulumiesc:
        identifier: azure-login
        parent: esc-providers
        weight: 3
aliases:
- /docs/pulumi-cloud/esc/providers/azure-login/
---

The `azure-login` provider enables you to log in to Azure using OpenID Connect or by providing static credentials. The provider will return a set of credentials that can be used to access Azure resources or fetch secrets using the `azure-secrets` provider.

## Example

```yaml
  azure:
    login:
      fn::open::azure-login:
        clientId: aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee
        tenantId: aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee
        subscriptionId: /subscriptions/00000000-0000-0000-0000-000000000000
        oidc: true
```

## Configuring OIDC

To learn how to configure OpenID Connect (OIDC) between Pulumi Cloud and Azure, see the [OpenID Connect integration](/docs/pulumi-cloud/oidc/azure/) documentation.

## Inputs

| Property         | Type   | Description                                                       |
|------------------|--------|-------------------------------------------------------------------|
| `clientId`       | string | The client ID to use                                              |
| `tenantId`       | string | The tenant ID to use                                              |
| `subscriptionId` | string | The subscription ID to use                                        |
| `clientSecret`   | string | [Optional] - The client secret to use for authentication, if any. |
| `oidc`           | bool   | [Optional] - Whether to use OIDC to log in. Defaults to `false`.  |
| `subjectAttributes`  | string[] | [Optional] - Subject attributes to be included in the OIDC token. For more information see the see the [OpenID subject customization](/docs/pulumi-cloud/oidc/azure#subject-customization) documentation |

## Outputs

| Property         | Type                              | Description                                                         |
|------------------|-----------------------------------|---------------------------------------------------------------------|
| `clientId`       | string                            | The configured client ID                                            |
| `tenantId`       | string                            | The configured tenant ID                                            |
| `subscriptionId` | string                            | The configured subscription ID                                      |
| `clientSecret`   | string                            | [Optional] - The client secret used for authentication, if any.     |
| `oidc`           | [AzureLoginOIDC](#azureloginoidc) | [Optional] - OIDC-related data, if OIDC is used for authentication. |

### AzureLoginOIDC

| Property | Type     | Description                               |
|----------|----------|-------------------------------------------|
| `token`  | string   | The OIDC token to use for authentication. |

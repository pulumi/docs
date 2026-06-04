---
title_tag: azure-login Pulumi ESC Provider
meta_desc: The azure-login Pulumi ESC Provider enables you to log in to Azure using OIDC or static credentials.
title: azure-login
h1: azure-login
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  esc:
    identifier: azure-login
    parent: esc-providers-login
    weight: 2
aliases:
    - /docs/pulumi-cloud/esc/providers/azure-login/
    - /docs/esc/providers/azure-login/
    - /docs/esc/integrations/dynamic-login-credentials/azure-login/
    - /docs/esc/concepts/providers/login/azure-login/
---

The `azure-login` provider enables you to log in to Azure using OpenID Connect or by providing static credentials. The provider will return a set of credentials that can be used to access Azure resources or fetch secrets using the `azure-secrets` provider.

## Example

The `azure-login` provider's outputs can be consumed by the Pulumi Azure providers ([azure-native](https://www.pulumi.com/registry/packages/azure-native/), [azure](https://www.pulumi.com/registry/packages/azure/), and [azuread](https://www.pulumi.com/registry/packages/azuread/)) and the Azure SDKs through the standard `ARM_*` environment variables:

```yaml
values:
  azure:
    login:
      fn::open::azure-login:
        clientId: aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee
        tenantId: aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee
        subscriptionId: /subscriptions/00000000-0000-0000-0000-000000000000
        oidc: true
  environmentVariables:
    # Consumed by the Pulumi Azure providers (azure-native, azure, azuread) and the Azure SDKs
    ARM_USE_OIDC: "true"
    ARM_CLIENT_ID: ${azure.login.clientId}
    ARM_TENANT_ID: ${azure.login.tenantId}
    ARM_SUBSCRIPTION_ID: ${azure.login.subscriptionId}
    ARM_OIDC_TOKEN: ${azure.login.oidc.token}
```

The [azuredevops](https://www.pulumi.com/registry/packages/azuredevops/) provider accepts the same `ARM_CLIENT_ID`, `ARM_TENANT_ID`, `ARM_OIDC_TOKEN`, and `ARM_USE_OIDC` credentials. It does not use `ARM_SUBSCRIPTION_ID`; instead, set your organization URL with the `AZDO_ORG_SERVICE_URL` environment variable.

## Configuring OIDC

To learn how to configure OpenID Connect (OIDC) between Pulumi Cloud and Azure, see the [OpenID Connect integration](/docs/esc/guides/configuring-oidc/azure/) documentation.

## Inputs

| Property         | Type   | Description                                                       |
|------------------|--------|-------------------------------------------------------------------|
| `clientId`       | string | The client ID to use                                              |
| `tenantId`       | string | The tenant ID to use                                              |
| `subscriptionId` | string | The subscription ID to use                                        |
| `clientSecret`   | string | [Optional] - The client secret to use for authentication, if any. |
| `oidc`           | bool   | [Optional] - Whether to use OIDC to log in. Defaults to `false`.  |
| `subjectAttributes`  | string[] | [Optional] - Subject attributes to be included in the OIDC token. For more information see the [OpenID subject customization](/docs/esc/guides/configuring-oidc/#custom-token-claim) documentation |

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

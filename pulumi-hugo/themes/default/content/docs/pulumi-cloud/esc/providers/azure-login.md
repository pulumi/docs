---
title_tag: azure-login Pulumi ESC Provider
meta_desc: The azure-login Pulumi ESC Provider enables you to log in to Azure using OIDC or static credentials.
title: azure-login
h1: azure-login
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    pulumicloud:
        identifier: azure-login
        parent: esc-providers
        weight: 3
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

### Creating the Azure Active Directory App

To create the Azure Active Directory App and service principal, see the [relevant Azure documentation](https://learn.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal).

After the AAD App has been created, take note of the Application (client) ID and Directory (tenant) ID. These values will be necessary when enabling OIDC for your Environment.

### Adding federated credentials

Navigate to the "Certificates & secrets" pane using the sidebar. Then, select the "Federated credentials" tab and click on the "Add credential" button.

In the wizard, select "Other Issuer" as the "Federated credential scenario".

Finally, fill in the "Issuer", "Subject Identifier", "Name", and "Audience" fields in the form.

* "Issuer" must be `https://api.pulumi.com/oidc`
* "Subject Identifier" must be a valid subject claim, for example, to target the `core` Environment, use:
  * `pulumi:environments:org:contoso:env:core`
* "Name" is an arbitrary name for the credential
* "Audience" must be the name of your Pulumi organization

## Inputs

| Property         | Type   | Description                                                       |
|------------------|--------|-------------------------------------------------------------------|
| `clientId`       | string | The client ID to use                                              |
| `tenantId`       | string | The tenant ID to use                                              |
| `subscriptionId` | string | The subscription ID to use                                        |
| `clientSecret`   | string | [Optional] - The client secret to use for authentication, if any. |
| `oidc`           | bool   | [Optional] - Whether to use OIDC to log in. Defaults to `false`.  |

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

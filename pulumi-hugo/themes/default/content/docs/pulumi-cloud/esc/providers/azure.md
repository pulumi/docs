---
title_tag: Azure ESC Provider
meta_desc: The Azure ESC Providers enable you to log in to Azure using OIDC, as well as dynamically import Secrets from Azure Key Vault into your Environment.
title: Azure
h1: Azure Provider
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    pulumicloud:
        identifier: azure
        parent: esc-providers
        weight: 2
---

The Azure ESC Providers enable you to log in to Azure using OIDC, as well as dynamically import Secrets from Azure Key Vault into your Environment. They may be used in conjunction with each other or independently.

* [azure-login](#azure-login) - Log in to Azure.
* [azure-secrets](#azure-secrets) - Import Secrets from Azure Key Vault.

## Example

```yaml
  azure:
    login:
      fn::open::azure-login:
        clientId: aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee
        tenantId: aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee
        subscriptionId: /subscriptions/00000000-0000-0000-0000-000000000000
        oidc: true
    secrets:
      fn::open::azure-secrets:
        login: ${azure.login}
        vault: example-vault-name
        get:
          api-key:
            name: api-key
          app-secret:
            name: app-secret
```

## azure-login

The `azure-login` provider enables you to log in to Azure using OpenID Connect or by providing static credentials. The provider will return a set of credentials that can be used to access Azure resources or fetch secrets using the `azure-secrets` provider.

### Configuring OIDC

#### Creating the Azure Active Directory App

To create the Azure Active Directory App and service principal, see the [relevant Azure documentation](https://learn.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal).

After the AAD App has been created, take note of the Application (client) ID and Directory (tenant) ID. These values will be necessary when enabling OIDC for your Environment.

#### Adding federated credentials

Navigate to the "Certificates & secrets" pane using the sidebar. Then, select the "Federated credentials" tab and click on the "Add credential" button.

In the wizard, select "Other Issuer" as the "Federated credential scenario".

Finally, fill in the "Issuer", "Subject Identifier", "Name", and "Audience" fields in the form.

* "Issuer" must be `https://api.pulumi.com/oidc`
* "Subject Identifier" must be a valid subject claim, for example, to target the `core` Environment, use:
  * `pulumi:environments:org:contoso:env:core`
* "Name" is an arbitrary name for the credential
* "Audience" must be the name of your Pulumi organization

### Inputs

| Property         | Type   | Description                                                       |
|------------------|--------|-------------------------------------------------------------------|
| `clientId`       | string | The client ID to use                                              |
| `tenantId`       | string | The tenant ID to use                                              |
| `subscriptionId` | string | The subscription ID to use                                        |
| `clientSecret`   | string | [Optional] - The client secret to use for authentication, if any. |
| `oidc`           | bool   | [Optional] - Whether to use OIDC to log in. Defaults to `false`.  |

### Outputs

| Property         | Type                              | Description                                                         |
|------------------|-----------------------------------|---------------------------------------------------------------------|
| `clientId`       | string                            | The configured client ID                                            |
| `tenantId`       | string                            | The configured tenant ID                                            |
| `subscriptionId` | string                            | The configured subscription ID                                      |
| `clientSecret`   | string                            | [Optional] - The client secret used for authentication, if any.     |
| `oidc`           | [AzureLoginOIDC](#azureloginoidc) | [Optional] - OIDC-related data, if OIDC is used for authentication. |

#### AzureLoginOIDC

| Property | Type     | Description                               |
|----------|----------|-------------------------------------------|
| `token`  | string   | The OIDC token to use for authentication. |

## azure-secrets

The `azure-secrets` provider enables you to dynamically import Secrets and Configuration from Azure Key Vault into your Environment. The provider will return a map of Secrets and/or Configuration.

### Inputs

| Property | Type                                           | Description                                                                                                              |
|----------|------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| `login`  | [AzureLoginOutputs](#outputs)                  | Credentials used to log in to Azure.                                                                                     |
| `vault`  | string                                         | The vault to read from.                                                                                                  |
| `get`    | map[string][AzureSecretsGet](#azuresecretsget) | A map from names to secrets to read from Azure Key Vault. The outputs will map each name to the secret's sensitive data. |

#### AzureSecretsGet

| Property       | Type   | Description                                       |
|----------------|--------|---------------------------------------------------|
| `name`         | string | The name of the secret to import.                 |
| `version`      | string | [Optional] - The version of the secret to import. |

### Outputs

| Property | Type   | Description                         |
|----------|--------|-------------------------------------|
| N/A      | object | A map of names to imported Secrets. |

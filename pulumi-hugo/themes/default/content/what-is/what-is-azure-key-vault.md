---
title: What is Azure Key Vault?
meta_desc: |
     Learn more about what Azure Key Vault is and how to use it.

type: what-is
page_title: "What is Azure Key Vault?"
---

Microsoft Azure is a leader in cloud computing, transforming the way organizations manage their digital infrastructure. An important aspect of Azure’s security framework is the management of sensitive data, commonly known as "[secrets](/what-is/what-is-secrets-management/)". Azure Key Vault is a service designed for the secure handling of these secrets, offering tools for storing, accessing, and managing confidential information in the cloud.

## What is Azure Key Vault?

Azure Key Vault is a cloud service for managing, retrieving, and storing sensitive information such as database credentials, API keys, and other secrets. It helps in securing access to applications, services, and IT resources without hard-coding sensitive information in plain text.

### Key features

- **Secure Storage**: Azure Key Vault offers highly secure storage for secrets, keys, and certificates, encrypted both in transit and at rest.
- **Seamless Integration*: It integrates effortlessly with other Azure services and applications, enhancing overall security architecture.
- **Access Control**: Azure Key Vault allows fine-grained access control with Microsoft Entra and access policies.

## Creating Azure Key Vault secrets

Azure Key Vault secrets can be created via the Azure CLI. Before creating secrets in Azure, you must first make sure you have the [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli) installed. Once you have installed the Azure CLI, run the `az login` command to [authenticate to your Azure account](https://learn.microsoft.com/en-us/cli/azure/authenticate-azure-cli).

```bash
$ az login
To sign in, use a web browser to open the page https://microsoft.com/devicelogin and enter the code LZURMHUR9 to authenticate.
[
  {
    "cloudName": "AzureCloud",
    "homeTenantId": "706….",
    "id": "028….",
    "isDefault": true,
    "managedByTenants": [],
    "name": "Subscription Name",
    "state": "Enabled",
    "tenantId": "706….",
    "user": {
      "name": "your@username.com",
      "type": "user"
    }
  }
]
```

### Create a secret via the CLI

Before creating a secret, you must first create both a resource group and a Key Vault resource.

You can create a resource group using the `az group create` command:

```bash
$ az group create --location westus --name MyResourceGroup
{
  "id": "/subscriptions/028…/resourceGroups/MyResourceGroup",
  "location": "westus",
  "managedBy": null,
  "name": "MyResourceGroup",
  "properties": {
    "provisioningState": "Succeeded"
  },
  "tags": null,
  "type": "Microsoft.Resources/resourceGroups"
}
```


You can create a Key Vault using the `az keyvault create` command. Note that Vault names are globally unique, so replace the value of `<YourVaultName>` below with a unique name for your resource:

```bash
# The example output has been truncated for easier visualization
$ az keyvault create --name <YourVaultName> --resource-group MyResourceGroup

{
  "id": "/subscriptions/028…/resourceGroups/MyResourceGroup/providers/Microsoft.KeyVault/vaults<<YourVaultName>",
  "location": "westus",
  "name": "<YourVaultName>",
  "properties": {
    ….
  },
  "resourceGroup": "MyResourceGroup",
  ….
  "tags": {},
  "type": "Microsoft.KeyVault/vaults"
}

```

Now that you have your resource group and Key Vault created, you can create a secret by running the `az keyvault secret set` command:

```bash
$ az keyvault secret set --vault-name <YourVaultName> --name MySecretName --value MySecretValue

{
  "attributes": {
    "created": "2023-11-28T19:01:35+00:00",
    "enabled": true,
    "expires": null,
    "notBefore": null,
    "recoveryLevel": "Recoverable+Purgeable",
    "updated": "2023-11-28T19:01:35+00:00"
  },
  "contentType": null,
  "id": "https://<YourVaultName>.vault.azure.net/secrets/MySecretName/88d5668ebe7447c0af796ed",
  "kid": null,
  "managed": null,
  "name": "MySecretName",
  "tags": {
    "file-encoding": "utf-8"
  },
  "value": "MySecretValue"
}
```

Verify the secret was created with the `az keyvault secret list` command.

```bash
$ az keyvault secret list --vault-name <YourVaultName>

[
  {
    "attributes": {
      "created": "2023-11-28T19:01:35+00:00",
      "enabled": true,
      "expires": null,
      "notBefore": null,
      "recoveryLevel": "Recoverable+Purgeable",
      "updated": "2023-11-28T19:01:35+00:00"
    },
    "contentType": null,
    "id": "https://<YourVaultName>.vault.azure.net/secrets/MySecretName",
    "managed": null,
    "name": "MySecretName",
    "tags": {
      "file-encoding": "utf-8"
    }
  }
]
```


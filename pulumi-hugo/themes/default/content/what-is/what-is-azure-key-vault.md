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
- **Seamless Integration**: It integrates effortlessly with other Azure services and applications, enhancing overall security architecture.
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


You can create a Key Vault using the `az keyvault create` command. Note that Key Vault names are [globally unique](https://learn.microsoft.com/en-us/azure/key-vault/general/about-keys-secrets-certificates), so you will need to replace the value of `<YourVaultName>` below with a unique name for your resource:

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

## Accessing Azure Key Vault secrets

Now that you have created an Azure Key Vault secret, you can access the value via the Azure CLI using the `az keyvault secret show` command.

```bash
$ az keyvault secret show --name MySecretName --vault-name <YourVaultName>
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

## Challenges and considerations

Azure Key Vault, while a powerful tool for managing secrets and cryptographic keys, does come with its own set of challenges, considerations, and limitations. Some of the key aspects to be aware of include:

- **Service Limits**: Azure Key Vault has specific service limits that apply to both Vaults and Managed HSMs (Hardware Security Modules). These limits include the maximum number of transactions allowed in a given time frame, such as key creation and retrieval operations. Exceeding these limits can result in throttling, indicated by a 429 HTTP status code​​.
- **Vault Management and Access Control**: Access to a Key Vault requires proper authentication and authorization. Authentication is done via Microsoft Entra ID, while authorization can be managed via Azure role-based access control (RBAC) or Key Vault access policy. This layered approach to security necessitates careful management to ensure that only authorized users or applications have access to the stored secrets​​.
- **Network Security Options**: Azure Key Vault allows for network security configurations to limit vault access by IP address or range, with further restrictions possible through firewall rules. These rules include options for trusted services, specific IP addresses and ranges, virtual networks using dynamic IP addresses, and private links. Such configurations require careful planning to ensure they align with an organization’s security policies​​.
- **Backup Limitations**: Azure Key Vault does not support the backup of an entire vault simultaneously. Instead, users must manually back up each key, secret, or certificate within the vault. This can be a significant consideration for organizations with extensive key and secret management needs, as it necessitates a more hands-on approach to backup and recovery processes​​.
- **Vault Segmentation Strategy**: It is recommended to use separate key vaults for each specific application or environment (development, pre-production, production) to reduce risk and limit the sharing of keys and secrets across different environments. This approach, while enhancing security, can add complexity to the management of multiple vaults, especially in larger organizations with numerous applications and environments​​.

These considerations highlight the importance of understanding Azure Key Vault's capabilities and limitations in order to effectively incorporate it into an organization's cloud security strategy. Proper planning, configuration, and management are essential to leverage the full benefits of Azure Key Vault while mitigating potential risks and challenges.

## Best practices

- **Regularly Rotate Secrets**: Implement a strategy for the regular rotation of secrets.
- **Provide Least-Privilege Access**: Minimize the number of entities with access to the Key Vault.
- **Monitor Access and Usage**: Use Azure Monitor and Azure Security Center to track access and activities.

## Conclusion

Azure Key Vault plays a vital role in securely managing secrets in Azure cloud environments. By effectively utilizing Azure Key Vault, organizations can significantly enhance the security and management of their sensitive data in the cloud.

Now that you’re equipped with the knowledge of Azure Key Vault, take your cloud infrastructure management to the next level with Pulumi. Explore these key resources to deepen your understanding and enhance your implementation strategies:

- **Provision Infrastructure as Code**: Learn about deploying and managing Azure Key Vault secrets as well as other Azure resources using Pulumi's Infrastructure as Code capabilities. For comprehensive insights, refer to [Pulumi's Azure Provider documentation for the Key Vault resource](/registry/packages/azure-native/api-docs/keyvault/vault/).
- **Advanced Secrets Management**: Explore Pulumi’s detailed guides on the centralized management of secrets in cloud applications, particularly with Pulumi ESC (Environments, Secrets, and Configurations). For more information, visit the [Pulumi ESC documentation for the Azure Secrets provider](/docs/pulumi-cloud/esc/providers/azure-secrets/).

Our [community on Slack](https://slack.pulumi.com/) is always open for discussions, questions, and sharing experiences. Join us there and become part of our growing community of cloud professionals!

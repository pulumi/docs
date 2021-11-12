---
title: Review the New Project | Azure
h1: Review the New Project
linktitle: Review the New Project
meta_desc: This page provides an overview on how to a review a new Azure project.
weight: 4
menu:
  getstarted:
    parent: azure
    identifier: azure-review-project

aliases: ["/docs/quickstart/azure/review-project/"]
---

Let's review some of the generated project files:

- `Pulumi.yaml` defines the [project]({{< relref "/docs/intro/concepts/project" >}}).
- `Pulumi.dev.yaml` contains [configuration]({{< relref "/docs/intro/concepts/config" >}}) values for the [stack]({{< relref "/docs/intro/concepts/stack" >}}) you initialized.

{{% choosable language csharp %}}

- `Program.cs` with a simple entry point.

{{% /choosable %}}

- {{< langfile >}} is the Pulumi program that defines your stack resources. Let's examine it.

{{< chooser language "typescript,python,go,csharp" / >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as resources from "@pulumi/azure-native/resources";
import * as storage from "@pulumi/azure-native/storage";

// Create an Azure Resource Group
const resourceGroup = new resources.ResourceGroup("resourceGroup");

// Create an Azure resource (Storage Account)
const storageAccount = new storage.StorageAccount("sa", {
    resourceGroupName: resourceGroup.name,
    sku: {
        name: storage.SkuName.Standard_LRS,
    },
    kind: storage.Kind.StorageV2,
});

// Export the primary key of the Storage Account
const storageAccountKeys = storage.listStorageAccountKeysOutput({
    resourceGroupName: resourceGroup.name,
    accountName: storageAccount.name
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
from pulumi_azure_native import storage
from pulumi_azure_native import resources

# Create an Azure Resource Group
resource_group = resources.ResourceGroup("resource_group")

# Create an Azure resource (Storage Account)
account = storage.StorageAccount('sa',
    resource_group_name=resource_group.name,
    sku=storage.SkuArgs(
        name=storage.SkuName.STANDARD_LRS,
    ),
    kind=storage.Kind.STORAGE_V2)

# Export the primary key of the Storage Account
primary_key = storage.list_storage_account_keys_output(
    resource_group_name=resource_group.name,
    account_name=account.name
).accountKeys.keys[0].value

pulumi.export("primary_storage_key", primary_key)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
    "github.com/pulumi/pulumi-azure-native/sdk/go/azure/resources"
	"github.com/pulumi/pulumi-azure-native/sdk/go/azure/storage"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        // Create an Azure Resource Group
        resourceGroup, err := resources.NewResourceGroup(ctx, "resourceGroup", nil)
        if err != nil {
            return err
        }

        // Create an Azure resource (Storage Account)
        account, err := storage.NewStorageAccount(ctx, "sa", &storage.StorageAccountArgs{
			ResourceGroupName: resourceGroup.Name,
			AccessTier:        storage.AccessTierHot,
			Sku: &storage.SkuArgs{
				Name: storage.SkuName_Standard_LRS,
			},
			Kind: storage.KindStorageV2,
        })
        if err != nil {
            return err
        }

        // Export the primary key of the Storage Account
		ctx.Export("primaryStorageKey", pulumi.All(resourceGroup.Name, account.Name).ApplyT(
			func(args []interface{}) (string, error) {
				resourceGroupName := args[0].(string)
				accountName := args[1].(string)
				accountKeys, err := storage.ListStorageAccountKeys(ctx, &storage.ListStorageAccountKeysArgs{
					ResourceGroupName: resourceGroupName,
					AccountName:       accountName,
				})
				if err != nil {
					return "", err
				}

				return accountKeys.Keys[0].Value, nil
			},
		))

        return nil
    })
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Threading.Tasks;
using Pulumi;
using Pulumi.AzureNative.Resources;
using Pulumi.AzureNative.Storage;
using Pulumi.AzureNative.Storage.Inputs;

class MyStack : Stack
{
    public MyStack()
    {
        // Create an Azure Resource Group
        var resourceGroup = new ResourceGroup("resourceGroup");

        // Create an Azure resource (Storage Account)
        var storageAccount = new StorageAccount("sa", new StorageAccountArgs
        {
            ResourceGroupName = resourceGroup.Name,
            Sku = new SkuArgs
            {
                Name = SkuName.Standard_LRS
            },
            Kind = Kind.StorageV2
        });

        // Export the primary key of the Storage Account
        this.PrimaryStorageKey = GetStorageAccountPrimaryKey(resourceGroup.Name, storageAccount.Name);
    }

    [Output]
    public Output<string> PrimaryStorageKey { get; set; }

    private static Output<string> GetStorageAccountPrimaryKey(Input<string> resourceGroupName, Input<string> accountName)
    {
        return ListStorageAccountKeys.Invoke(new ListStorageAccountKeysInvokeArgs
        {
            ResourceGroupName = resourceGroupName,
            AccountName = accountName
        }).Apply(accountKeys => Output.CreateSecret(accountKeys.Keys[0].Value));
    }
}
```

{{% /choosable %}}

This Pulumi program creates an Azure resource group and storage account and then exports the storage account's primary key.

**Note**: In this program, the location of the resource group is set in the configuration setting `azure-native:location` (check the `Pulumi.dev.yaml` file). This is an easy way to set a global location for your program so you don't have to specify the location for each resource manually. The location for the storage account is automatically derived from the location of the resource group. To override the location for a resource, simply set the location property to one of Azure's [supported locations](https://azure.microsoft.com/en-us/global-infrastructure/locations/).

Next, you'll deploy your stack, which will provision a resource group and your storage account.

{{< get-started-stepper >}}

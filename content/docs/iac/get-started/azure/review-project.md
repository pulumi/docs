---
title_tag: Review the Project | Azure
title: Review the project files
h1: "Review the project files"
meta_desc: This page walks through the files in a newly created Azure + Pulumi project.
weight: 5
menu:
    iac:
        name: Review the project
        identifier: azure-get-started.review-project
        parent: azure-get-started
        weight: 5
aliases:
    - /docs/get-started/azure/review-project/
    - /docs/quickstart/azure/review-project/
    - /docs/clouds/azure/get-started/review-project/
---

Your new project includes a few key files:

{{% choosable language "typescript,python,go,csharp" %}}

- <span>{{< langfile >}}</span> contains your program, which declares a resource group and storage account
- `Pulumi.yaml` is the [project file](/docs/iac/concepts/projects/project-file) with metadata like your project's name
- `Pulumi.dev.yaml` holds configuration for the stack you just created

{{% /choosable %}}
{{% choosable language java %}}

- `src/main/java/myproject` is the project's Java package root
- <span>{{< langfile >}}</span> contains your program, which declares a resource group and storage account
- `Pulumi.yaml` is the [project file](/docs/iac/concepts/projects/project-file) with metadata like your project's name
- `Pulumi.dev.yaml` holds configuration for the stack you just created

{{% /choosable %}}
{{% choosable language yaml %}}

- `Pulumi.yaml` is the [project file](/docs/iac/concepts/projects/project-file) with metadata like your project's name, as well as your program's resources
- `Pulumi.dev.yaml` holds configuration for the stack you just created

{{% /choosable %}}

Now open {{< langfile >}} and take a look:

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

// Export the storage account name
export const storageAccountName = storageAccount.name;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
from pulumi_azure_native import storage
from pulumi_azure_native import resources

# Create an Azure Resource Group
resource_group = resources.ResourceGroup("resource_group")

# Create an Azure Storage Account
account = storage.StorageAccount(
    "sa",
    resource_group_name=resource_group.name,
    sku={
        "name": storage.SkuName.STANDARD_LRS,
    },
    kind=storage.Kind.STORAGE_V2,
)

# Export the storage account name
pulumi.export("storage_account_name", account.name)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-azure-native-sdk/resources/v2"
	"github.com/pulumi/pulumi-azure-native-sdk/storage/v2"
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
		storageAccount, err := storage.NewStorageAccount(ctx, "sa", &storage.StorageAccountArgs{
			ResourceGroupName: resourceGroup.Name,
			Sku: &storage.SkuArgs{
				Name: pulumi.String("Standard_LRS"),
			},
			Kind: pulumi.String("StorageV2"),
		})
		if err != nil {
			return err
		}

		// Export the storage account name
		ctx.Export("storageAccountName", storageAccount.Name)
		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using Pulumi;
using Pulumi.AzureNative.Resources;
using Pulumi.AzureNative.Storage;
using Pulumi.AzureNative.Storage.Inputs;
using System.Collections.Generic;

return await Pulumi.Deployment.RunAsync(() =>
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

    // Export the storage account name
    return new Dictionary<string, object?>
    {
        ["storageAccountName"] = storageAccount.Name
    };
});
```

{{% /choosable %}}

{{% choosable language java %}}

```java
package myproject;

import com.pulumi.Pulumi;
import com.pulumi.azurenative.resources.ResourceGroup;
import com.pulumi.azurenative.storage.StorageAccount;
import com.pulumi.azurenative.storage.StorageAccountArgs;
import com.pulumi.azurenative.storage.enums.Kind;
import com.pulumi.azurenative.storage.enums.SkuName;
import com.pulumi.azurenative.storage.inputs.SkuArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            var resourceGroup = new ResourceGroup("resourceGroup");
            var storageAccount = new StorageAccount("sa", StorageAccountArgs.builder()
                    .resourceGroupName(resourceGroup.name())
                    .sku(SkuArgs.builder()
                            .name(SkuName.Standard_LRS)
                            .build())
                    .kind(Kind.StorageV2)
                    .build());

            ctx.export("storageAccountName", storageAccount.name());
        });
    }
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
name: quickstart
runtime: yaml
description: A minimal Azure Native Pulumi YAML program

resources:
  # Create an Azure Resource Group
  resourceGroup:
    type: azure-native:resources:ResourceGroup
  # Create an Azure Storage Account
  sa:
    type: azure-native:storage:StorageAccount
    properties:
      resourceGroupName: ${resourceGroup.name}
      sku:
        name: Standard_LRS
      kind: StorageV2

outputs:
  # Export the storage account name
  storageAccountName: ${sa.name}
```

{{% /choosable %}}

This program declares an Azure [Resource Group](/registry/packages/azure-native/api-docs/resources/resourcegroup/) and [Storage Account](/registry/packages/azure-native/api-docs/storage/storageaccount/) and exports the storage account's name as a [stack output](/docs/iac/concepts/stacks/#outputs). Resources are just objects with [properties](/docs/iac/concepts/inputs-outputs) that capture their inputs and outputs. Exporting the storage account's name makes it easy to reference later.

{{< get-started-stepper >}}

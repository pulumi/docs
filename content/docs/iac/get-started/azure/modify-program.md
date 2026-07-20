---
title_tag: Modify the Program | Azure
title: Modify the program
h1: "Modify the program"
meta_desc: This page provides an overview on how to update an Azure project from a Pulumi program.
weight: 7
menu:
    iac:
        name: Modify the program
        identifier: azure-get-started.modify-program
        parent: azure-get-started
        weight: 7
aliases:
    - /docs/quickstart/azure/modify-program/
    - /docs/clouds/azure/get-started/modify-program/
---

Now you'll turn the storage account into a static website.

In your project directory, create a file named `index.html` with the following content:

```html
<html>
    <body>
        <h1>Hello, Pulumi!</h1>
    </body>
</html>
```

To turn the storage account into a website, you'll need two new resources:

- A [`StorageAccountStaticWebsite`](/registry/packages/azure-native/api-docs/storage/storageaccountstaticwebsite/) to enable static website hosting on the storage account
- A [`Blob`](/registry/packages/azure-native/api-docs/storage/blob/) for the HTML file

Open {{< langfile >}} and replace it with the following code:

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as resources from "@pulumi/azure-native/resources";
import * as storage from "@pulumi/azure-native/storage";

// Create a resource group
const resourceGroup = new resources.ResourceGroup("resourceGroup");

// Create a storage account
const storageAccount = new storage.StorageAccount("sa", {
    resourceGroupName: resourceGroup.name,
    sku: {
        name: storage.SkuName.Standard_LRS,
    },
    kind: storage.Kind.StorageV2,
});

// Enable static website support on the storage account
const staticWebsite = new storage.StorageAccountStaticWebsite("staticWebsite", {
    accountName: storageAccount.name,
    resourceGroupName: resourceGroup.name,
    indexDocument: "index.html",
});

// Upload index.html to the storage container
const indexHtml = new storage.Blob("index.html", {
    resourceGroupName: resourceGroup.name,
    accountName: storageAccount.name,
    containerName: staticWebsite.containerName,
    source: new pulumi.asset.FileAsset("index.html"),
    contentType: "text/html",
});

// Export the storage account name and website URL
export const storageAccountName = storageAccount.name;
export const staticEndpoint = storageAccount.primaryEndpoints.web;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
from pulumi_azure_native import storage
from pulumi_azure_native import resources

# Create a resource group
resource_group = resources.ResourceGroup("resource_group")

# Create a storage account
account = storage.StorageAccount(
    "sa",
    resource_group_name=resource_group.name,
    sku={
        "name": storage.SkuName.STANDARD_LRS,
    },
    kind=storage.Kind.STORAGE_V2,
)

# Enable static website support on the storage account
static_website = storage.StorageAccountStaticWebsite(
    "staticWebsite",
    account_name=account.name,
    resource_group_name=resource_group.name,
    index_document="index.html",
)

# Upload index.html to the storage container
index_html = storage.Blob(
    "index.html",
    resource_group_name=resource_group.name,
    account_name=account.name,
    container_name=static_website.container_name,
    source=pulumi.FileAsset("index.html"),
    content_type="text/html",
)

# Export the storage account name and website URL
pulumi.export("storage_account_name", account.name)
pulumi.export("staticEndpoint", account.primary_endpoints.web)
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
		// Create a resource group
		resourceGroup, err := resources.NewResourceGroup(ctx, "resourceGroup", nil)
		if err != nil {
			return err
		}

		// Create a storage account
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

		// Enable static website support on the storage account
		staticWebsite, err := storage.NewStorageAccountStaticWebsite(ctx, "staticWebsite", &storage.StorageAccountStaticWebsiteArgs{
			AccountName:       storageAccount.Name,
			ResourceGroupName: resourceGroup.Name,
			IndexDocument:     pulumi.String("index.html"),
		})
		if err != nil {
			return err
		}

		// Upload index.html to the storage container
		_, err = storage.NewBlob(ctx, "index.html", &storage.BlobArgs{
			ResourceGroupName: resourceGroup.Name,
			AccountName:       storageAccount.Name,
			ContainerName:     staticWebsite.ContainerName,
			Source:            pulumi.NewFileAsset("index.html"),
			ContentType:       pulumi.String("text/html"),
		})
		if err != nil {
			return err
		}

		// Export the storage account name and website URL
		ctx.Export("storageAccountName", storageAccount.Name)
		ctx.Export("staticEndpoint", storageAccount.PrimaryEndpoints.Web())
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
    // Create a resource group
    var resourceGroup = new ResourceGroup("resourceGroup");

    // Create a storage account
    var storageAccount = new StorageAccount("sa", new StorageAccountArgs
    {
        ResourceGroupName = resourceGroup.Name,
        Sku = new SkuArgs
        {
            Name = SkuName.Standard_LRS
        },
        Kind = Kind.StorageV2
    });

    // Enable static website support on the storage account
    var staticWebsite = new StorageAccountStaticWebsite("staticWebsite", new StorageAccountStaticWebsiteArgs
    {
        AccountName = storageAccount.Name,
        ResourceGroupName = resourceGroup.Name,
        IndexDocument = "index.html",
    });

    // Upload index.html to the storage container
    var indexHtml = new Blob("index.html", new BlobArgs
    {
        ResourceGroupName = resourceGroup.Name,
        AccountName = storageAccount.Name,
        ContainerName = staticWebsite.ContainerName,
        Source = new FileAsset("./index.html"),
        ContentType = "text/html",
    });

    // Export the storage account name and website URL
    return new Dictionary<string, object?>
    {
        ["storageAccountName"] = storageAccount.Name,
        ["staticEndpoint"] = storageAccount.PrimaryEndpoints.Apply(primaryEndpoints => primaryEndpoints.Web)
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
import com.pulumi.azurenative.storage.StorageAccountStaticWebsite;
import com.pulumi.azurenative.storage.StorageAccountStaticWebsiteArgs;
import com.pulumi.azurenative.storage.Blob;
import com.pulumi.azurenative.storage.BlobArgs;
import com.pulumi.azurenative.storage.enums.Kind;
import com.pulumi.azurenative.storage.enums.SkuName;
import com.pulumi.azurenative.storage.inputs.SkuArgs;
import com.pulumi.azurenative.storage.outputs.EndpointsResponse;
import com.pulumi.asset.FileAsset;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            // Create a resource group
            var resourceGroup = new ResourceGroup("resourceGroup");

            // Create a storage account
            var storageAccount = new StorageAccount("sa", StorageAccountArgs.builder()
                    .resourceGroupName(resourceGroup.name())
                    .sku(SkuArgs.builder()
                            .name(SkuName.Standard_LRS)
                            .build())
                    .kind(Kind.StorageV2)
                    .build());

            // Enable static website support on the storage account
            var staticWebsite = new StorageAccountStaticWebsite("staticWebsite", StorageAccountStaticWebsiteArgs.builder()
                    .accountName(storageAccount.name())
                    .resourceGroupName(resourceGroup.name())
                    .indexDocument("index.html")
                    .build());

            // Upload index.html to the storage container
            var indexHtml = new Blob("index.html", BlobArgs.builder()
                    .resourceGroupName(resourceGroup.name())
                    .accountName(storageAccount.name())
                    .containerName(staticWebsite.containerName())
                    .source(new FileAsset("index.html"))
                    .contentType("text/html")
                    .build());

            // Export the storage account name and website URL
            ctx.export("storageAccountName", storageAccount.name());
            ctx.export("staticEndpoint", storageAccount.primaryEndpoints()
                    .applyValue(EndpointsResponse::web));
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
  # Create a resource group
  resourceGroup:
    type: azure-native:resources:ResourceGroup

  # Create a storage account
  sa:
    type: azure-native:storage:StorageAccount
    properties:
      resourceGroupName: ${resourceGroup.name}
      sku:
        name: Standard_LRS
      kind: StorageV2

  # Enable static website support on the storage account
  staticWebsite:
    type: azure-native:storage:StorageAccountStaticWebsite
    properties:
      accountName: ${sa.name}
      resourceGroupName: ${resourceGroup.name}
      indexDocument: index.html

  # Upload index.html to the storage container
  index-html:
    type: azure-native:storage:Blob
    properties:
      resourceGroupName: ${resourceGroup.name}
      accountName: ${sa.name}
      containerName: ${staticWebsite.containerName}
      source:
        fn::fileAsset: ./index.html
      contentType: text/html
      blobName: index.html
      type: Block

outputs:
  # Export the storage account name and website URL
  storageAccountName: ${sa.name}
  staticEndpoint: ${sa.primaryEndpoints.web}
```

{{% /choosable %}}

With Pulumi, property relationships between resources encode their dependencies. For example, the `Blob`'s references to the `StorageAccount` name and the `StorageAccountStaticWebsite` container name tell Pulumi that those two resources should be created first.

Next, you'll deploy your changes.

{{< get-started-stepper >}}

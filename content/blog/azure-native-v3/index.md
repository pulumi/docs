---
title: "Azure Native V3: A Leaner, Faster SDK for Microsoft Azure"
date: 2025-04-03
draft: false
meta_desc: Announcing Azure Native V3 with 75% smaller SDK size, improved default API versions, and simplified explicit version management for a better developer experience.
meta_image: meta.png
authors:
    - thomas-kappler
    - meagan-cojocar

tags:
    - azure-native
    - azure
    - features
    - releases

social:
    twitter:
    linkedin: 
---

Today we're excited to announce the release of Pulumi Azure Native V3, a major update to our Azure Native provider that dramatically improves developer experience through significant SDK size reduction, up-to-date default API versions, and a flexible approach to managing explicit API versions.

Pulumi Azure Native is our native provider for Microsoft Azure, offering direct access to the complete Azure resource management API. Unlike traditional providers that abstract away cloud APIs, Azure Native gives you more coverage of Azure resources, properties, and up-to-date features by directly mapping to Azure's native REST API. This allows you to provision and manage any Azure resource with Pulumi in your favorite programming language while taking advantage of all the latest Azure capabilities as soon as they're released.

These improvements came about through our community-driven [RFC process](https://github.com/pulumi/pulumi-azure-native/issues/4004), where we explored various options to balance SDK size with the flexibility needed by advanced users.

<!--more-->

## A Slimmer, More Efficient SDK

The most immediate benefit of Azure Native V3 is the dramatic 75% reduction in SDK size across all languages. By removing typed resources for alternate API versions from the default SDK, we've addressed one of the most common pain points reported by our users:

| Language | Before | After | Reduction |
|----------|--------|-------|-----------|
| .NET     | 73,134 files (74.19 MB) | 16,890 files (~17MB) | 76.9% |
| JS/TS    | 57,230 files (398 MB) | 13,880 files (~97MB) | 75.7% |
| Python   | 20,735 files (104.6 MB) | 4,926 files (~25MB) | 76.3% |

This significant reduction addresses issues that many users have faced, particularly in TypeScript projects where language servers would often crash or consume excessive memory due to the large type files. With Azure Native V3, you can expect:

- Faster IDE performance
- More responsive language servers
- Reduced memory consumption
- Quicker package installation

## Up-to-Date Default API Versions

Azure Native V3 includes refreshed default API versions across nearly all resources. This ensures you're working with the latest stable Azure features and capabilities without needing to manually specify versions. Key services like EventGrid (now 2025-02-15) and MachineLearningServices (now 2024-10-01) have been updated to reflect current Azure capabilities.

## Simplified Version Management

While most users stick with the default versions (about 95% of Azure Native resources in Pulumi Cloud use the default API versions), we understand that some scenarios require using specific Azure API versions. Azure Native V3 introduces a new approach to managing these cases.

Instead of bloating the main SDK with every possible API version, V3 provides a way to generate local packages for just the resources and versions you need:

### Step 1: Add the specific API version package

First, use the Pulumi CLI to add just the packages and versions you need:

```bash
pulumi package add azure-native storage v20240101
```

### Step 2: Import and use the versioned package

Once added, you can import and use the specific API version in your code:

{{< chooser language "typescript,python,csharp,go" >}}

{{% choosable language typescript %}}

```typescript
import * as resources from "@pulumi/azure-native/resources";
import * as storage_v20240101 from "@pulumi/azure-native_storage_v20240101";

const resourceGroup = new resources.ResourceGroup("resourceGroup");

const storageAccount = new storage_v20240101.storage.v20240101.StorageAccount("sa", {
    resourceGroupName: resourceGroup.name,
    sku: {
        name: storage_v20240101.storage.v20240101.SkuName.Standard_LRS,
    },
    kind: storage_v20240101.storage.v20240101.Kind.StorageV2,
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
from pulumi_azure_native import resources
import pulumi_azure_native_storage_v20240101 as storage_v20240101

resource_group = resources.ResourceGroup("resource_group")

storage_account = storage_v20240101.storage.v20240101.StorageAccount("sa",
    resource_group_name=resource_group.name,
    sku=storage_v20240101.storage.v20240101.SkuArgs(
        name=storage_v20240101.storage.v20240101.SkuName.STANDARD_LRS,
    ),
    kind=storage_v20240101.storage.v20240101.Kind.STORAGE_V2)
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using Pulumi;
using Pulumi.AzureNative.Resources;
using Storage_v20240101 = Pulumi.AzureNative_Storage_v20240101;

class MyStack : Stack
{
    public MyStack()
    {
        var resourceGroup = new ResourceGroup("resourceGroup");

        var storageAccount = new Storage_v20240101.Storage.V20240101.StorageAccount("sa", new()
        {
            ResourceGroupName = resourceGroup.Name,
            Sku = new Storage_v20240101.Storage.V20240101.SkuArgs
            {
                Name = Storage_v20240101.Storage.V20240101.SkuName.Standard_LRS,
            },
            Kind = Storage_v20240101.Storage.V20240101.Kind.StorageV2,
        });
    }
}
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi-azure-native/sdk/go/azure/resources"
	storage_v20240101 "github.com/pulumi-azure-native-storage-v20240101/sdk/go/azure/storage/v20240101"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		resourceGroup, err := resources.NewResourceGroup(ctx, "resourceGroup", nil)
		if err != nil {
			return err
		}

		storageAccount, err := storage_v20240101.NewStorageAccount(ctx, "sa", &storage_v20240101.StorageAccountArgs{
			ResourceGroupName: resourceGroup.Name,
			Sku: &storage_v20240101.SkuArgs{
				Name: storage_v20240101.SkuNameStandard_LRS,
			},
			Kind: storage_v20240101.KindStorageV2,
		})
		if err != nil {
			return err
		}

		return nil
	})
}
```

{{% /choosable %}}

{{< /chooser >}}

This approach gives you the best of both worlds - a slim, efficient SDK by default, with the option to add strongly-typed resources for specific API versions only when needed.

## Additional Improvements

Azure Native V3 also includes several other enhancements:

- **Reorganized module structure** better aligned with Azure SDK conventions
- **Improved resource naming** for clearer distinction between similar resources
- **Enhanced handling of nested properties** to avoid accidental overwriting
- **Better state management** with the removal of unnecessary `__inputs` fields

## Getting Started

Ready to get started with Azure Native V3? Update your dependencies to point to the latest v3.x version:

```typescript
"@pulumi/azure-native": "^3.0.0"
```

For a smooth upgrade experience, we recommend:

1. If you're using Azure Native v1, first upgrade to v2 using our [v1 to v2 upgrade guide](https://www.pulumi.com/registry/packages/azure-native/from-v1-to-v2/)
2. Then upgrade from v2 to v3 using our [v2 to v3 upgrade guide](https://www.pulumi.com/registry/packages/azure-native/from-v2-to-v3/)

This stepwise approach will help you resolve any deprecation warnings and make the migration process more manageable.

## Conclusion

Azure Native V3 represents a significant step forward in our mission to provide the best possible developer experience for cloud infrastructure. By dramatically reducing SDK size while maintaining flexibility for version management, we've made it easier than ever to build and deploy Azure resources with Pulumi.

We'd like to thank our community for their valuable feedback throughout the development of V3. Your input helped shape this release, and we're excited to see what you'll build with it.

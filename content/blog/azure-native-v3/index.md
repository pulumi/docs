---
title: "Azure Native V3: A Leaner, Faster SDK for Microsoft Azure"
date: 2025-04-03
draft: false
meta_desc: Azure Native V3 delivers 75% smaller SDK size, updated API versions, and flexible options for working with explicit API versions in Microsoft Azure.
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

Today we're excited to announce the release of Pulumi Azure Native V3, a major update to our Azure Native provider that improves developer experience through significant SDK size reduction, up-to-date default API versions, and a flexible approach to managing explicit API versions.

[Pulumi Azure Native](/registry/packages/azure-native/) is our native provider for Microsoft Azure, offering direct access to the  [Azure Resource Manager API](https://learn.microsoft.com/en-us/rest/api/resources/). Unlike traditional providers that abstract away cloud APIs, Azure Native gives you more coverage of Azure resources, properties, and up-to-date features by directly mapping to Azure's native REST API. This allows you to provision and manage any Azure resource with Pulumi in your favorite programming language while taking advantage of all the latest Azure capabilities as soon as they're released.

These improvements came about through our [RFC process](https://github.com/pulumi/pulumi-azure-native/issues/4004), where we explored various options to balance SDK size with the flexibility needed by advanced users.
<!--more-->

## A Slimmer, More Efficient SDK

The most significant improvement in Azure Native V3 is the dramatic 75% reduction in SDK size across all languages. By optimizing the SDK to include only the most commonly used API versions, we've solved one of the most frequent pain points reported by our users:

| Language | Before | After | Reduction | Build Time Before | Build Time After |
|----------|--------|-------|-----------|-------------------|------------------|
| .NET     | 77MB | 15MB | 80.5% | 7m 52s | 47s |
| JS/TS    | 494MB | 87MB | 82.4% | 166s | 25s |
| Python   | 104.6 MB | 25MB | 76.3% | - | - |

This transformation delivers immediate benefits that every developer will notice:

- Faster IDE performance with reduced load times
- More responsive language servers for better autocompletion and documentation
- Reduced memory consumption for resource-constrained development environments
- Significantly quicker package installation and project bootstrap times
- Improved CI/CD pipeline performance with faster dependency installation

## Additional Improvements

Azure Native V3 also includes several other enhancements:

- **Reorganized module structure** better aligned with Azure SDK conventions
- **Improved resource naming** for clearer distinction between similar resources
- **Enhanced handling of nested properties** to avoid accidental overwriting
- **Better state management** with the removal of unnecessary `__inputs` fields

## Understanding Azure Versioning

The Pulumi Azure Native provider needs to manage two different versioning systems:

1. **Pulumi's Semantic Versioning**: Our SDKs follow the traditional major.minor.patch format (e.g., 3.0.0)
   - Patch versions (3.0.1) contain bug fixes only
   - Minor versions (3.1.0) add new resources and non-breaking features
   - Major versions (3.0.0) may contain breaking changes

2. **Azure's Date-based API Versions**: Azure resources use date-based versions like "2024-01-01" or "2023-05-15-preview"
   - Each Azure service (resource provider) has its own set of API versions
   - Breaking changes can occur between different API versions
   - Preview versions (with "-preview" suffix) contain newer features that may not be stable yet

## Default API Versions

Azure Native V3 includes refreshed default API versions across nearly all resources, ensuring you're automatically working with the latest stable Azure features and capabilities without any extra configuration. The new default versions unlock powerful new Azure functionality out of the box, such as:

- EventGrid (now 2025-02-15): Support for advanced filtering, dead-lettering, and custom event schemas
- MachineLearningServices (now 2024-10-01): Enhanced compute instance capabilities and new model deployment options
- Storage (now 2024-01-01): Improved performance tiers and expanded security features
- KeyVault (now 2024-03-01): Enhanced certificate management and expanded access policy options

## Non-default API versions

Most users (approximately 95% based on our Pulumi Cloud data) will be perfectly served by these default API versions. However, there are situations where you might need to use a specific API version.

For these cases, Azure Native V3 provides two flexible approaches:

**Option 1: Accessing Explicit API Versions via Local Packages**

The most type-safe way to use explicit API versions is through local packages. This approach gives you the full SDK experience with strong typing, auto-completion, and documentation.

### Step 1: Add the specific API version package

Use the Pulumi CLI to add just the packages and versions you need:

```bash
pulumi package add azure-native storage v20240101
```

For more details on the `package add` command, see the [CLI documentation](/docs/cli/commands/pulumi_package_add/).

### Step 2: Import and use the versioned package

Once added, you can import and use the specific API version in your code:

{{< chooser language "typescript,python,csharp,go,yaml,java" >}}

{{% choosable language typescript %}}

```typescript
import * as resources from "@pulumi/azure-native/resources";
import * as storage_v20240101 from "@pulumi/azure-native_storage_v20240101";

const resourceGroup = new resources.ResourceGroup("resourceGroup");

const storageAccount = new storage_v20240101.storage.StorageAccount("sa", {
    resourceGroupName: resourceGroup.name,
    sku: {
        name: storage_v20240101.storage.SkuName.Standard_LRS,
    },
    kind: storage_v20240101.storage.Kind.StorageV2,
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
from pulumi_azure_native import resources
import pulumi_azure_native_storage_v20240101 as storage_v20240101

resource_group = resources.ResourceGroup("resource_group")

storage_account = storage_v20240101.storage.StorageAccount("sa",
    resource_group_name=resource_group.name,
    sku=storage_v20240101.storage.SkuArgs(
        name=storage_v20240101.storage.SkuName.STANDARD_LRS,
    ),
    kind=storage_v20240101.storage.Kind.STORAGE_V2)
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

        var storageAccount = new Storage_v20240101.Storage.StorageAccount("sa", new()
        {
            ResourceGroupName = resourceGroup.Name,
            Sku = new Storage_v20240101.Storage.SkuArgs
            {
                Name = Storage_v20240101.Storage.SkuName.Standard_LRS,
            },
            Kind = Storage_v20240101.Storage.Kind.StorageV2,
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
	storage_v20240101 "github.com/pulumi-azure-native-storage-v20240101/sdk/go/azure/storage"
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

{{% choosable language yaml %}}

```yaml
name: azure-native-example
runtime: yaml
description: A minimal Azure Native Pulumi YAML program
resources:
  resourceGroup:
    type: azure-native:resources:ResourceGroup
    properties:
      location: westus2
  
  # Using specific API version package
  storageAccount:
    type: azure-native_storage_v20240101:storage:StorageAccount
    properties:
      resourceGroupName: ${resourceGroup.name}
      sku:
        name: Standard_LRS
      kind: StorageV2
```

{{% /choosable %}}

{{% choosable language java %}}

```java
package myproject;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.azurenative.resources.ResourceGroup;
import com.pulumi.azurenative.resources.ResourceGroupArgs;
import com.pulumi.azurenative_storage_v20240101.storage.StorageAccount;
import com.pulumi.azurenative_storage_v20240101.storage.StorageAccountArgs;
import com.pulumi.azurenative_storage_v20240101.storage.enums.Kind;
import com.pulumi.azurenative_storage_v20240101.storage.enums.SkuName;
import com.pulumi.azurenative_storage_v20240101.storage.inputs.SkuArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    private static void stack(Context ctx) {
        var resourceGroup = new ResourceGroup("resourceGroup");

        var storageAccount = new StorageAccount("sa", StorageAccountArgs.builder()
            .resourceGroupName(resourceGroup.name())
            .sku(SkuArgs.builder()
                .name(SkuName.Standard_LRS)
                .build())
            .kind(Kind.StorageV2)
            .build());
    }
}
```

{{% /choosable %}}

{{< /chooser >}}

**Option 2: Using the Generic Resource**

An alternative approach is to use the generic `azure-native.resources.Resource`. This special resource allows you to access any Azure resource at any API version, including older versions that might not be available through local packages.

While not as type-safe as the local package approach, the generic resource offers maximum flexibility and is useful when you need to access a resource that is not yet supported by the Pulumi provider or when an issue prevents you from using a specific resource.

Here's how to use the generic resource alongside a standard resource for comparison:

{{< chooser language "typescript,python,csharp,go,yaml,java" >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as azure_native from "@pulumi/azure-native";

const resourceGroup = new azure_native.resources.ResourceGroup("resourceGroup", {});

// Create a Storage Account using the typed resource
const sa = new azure_native.storage.StorageAccount("sa", {
    resourceGroupName: resourceGroup.name,
    sku: {
        name: azure_native.storage.SkuName.Standard_LRS,
    },
    kind: azure_native.storage.Kind.StorageV2,
});

// Create another Storage Account using the generic resource
const generic = new azure_native.resources.Resource("generic", {
    resourceGroupName: resourceGroup.name,
    resourceProviderNamespace: "Microsoft.Storage",
    resourceType: "storageAccounts",
    apiVersion: "2022-09-01",
    // This property is required even when empty.
    parentResourcePath: "",

    // These properties are optional and are defined on the generic resource because many resources have a kind or a SKU.
    kind: "StorageV2",
    sku: {
        name: "Standard_LRS",
    },

    // This is a generic property bag for all other properties of the targeted resource.
    properties: {
        allowBlobPublicAccess: false,
    },
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
from pulumi_azure_native import resources, storage

resource_group = resources.ResourceGroup("resource_group")

# Create a Storage Account using the typed resource
sa = storage.StorageAccount("sa",
    resource_group_name=resource_group.name,
    sku=storage.SkuArgs(
        name=storage.SkuName.STANDARD_LRS,
    ),
    kind=storage.Kind.STORAGE_V2)

# Create another Storage Account using the generic resource
generic = resources.Resource("generic",
    resource_group_name=resource_group.name,
    resource_provider_namespace="Microsoft.Storage",
    resource_type="storageAccounts",
    api_version="2022-09-01",
    # This property is required even when empty
    parent_resource_path="",

    # These properties are optional and are defined on the generic resource
    kind="StorageV2",
    sku={
        "name": "Standard_LRS",
    },

    # This is a generic property bag for all other properties
    properties={
        "allowBlobPublicAccess": False,
    })
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using Pulumi;
using Pulumi.AzureNative.Resources;
using Pulumi.AzureNative.Storage;

class MyStack : Stack
{
    public MyStack()
    {
        var resourceGroup = new ResourceGroup("resourceGroup");

        // Create a Storage Account using the typed resource
        var sa = new StorageAccount("sa", new StorageAccountArgs
        {
            ResourceGroupName = resourceGroup.Name,
            Sku = new SkuArgs
            {
                Name = SkuName.Standard_LRS,
            },
            Kind = Kind.StorageV2,
        });

        // Create another Storage Account using the generic resource
        var generic = new Resource("generic", new ResourceArgs
        {
            ResourceGroupName = resourceGroup.Name,
            ResourceProviderNamespace = "Microsoft.Storage",
            ResourceType = "storageAccounts",
            ApiVersion = "2022-09-01",
            // This property is required even when empty
            ParentResourcePath = "",

            // These properties are optional
            Kind = "StorageV2",
            Sku = new Dictionary<string, object>
            {
                { "name", "Standard_LRS" },
            },

            // This is a generic property bag for all other properties
            Properties = new Dictionary<string, object>
            {
                { "allowBlobPublicAccess", false },
            },
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
	"github.com/pulumi/pulumi-azure-native/sdk/go/azure/storage"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		resourceGroup, err := resources.NewResourceGroup(ctx, "resourceGroup", nil)
		if err != nil {
			return err
		}

		// Create a Storage Account using the typed resource
		_, err = storage.NewStorageAccount(ctx, "sa", &storage.StorageAccountArgs{
			ResourceGroupName: resourceGroup.Name,
			Sku: &storage.SkuArgs{
				Name: storage.SkuNameStandard_LRS,
			},
			Kind: storage.KindStorageV2,
		})
		if err != nil {
			return err
		}

		// Create another Storage Account using the generic resource
		properties := pulumi.Map{
			"allowBlobPublicAccess": pulumi.Bool(false),
		}

		_, err = resources.NewResource(ctx, "generic", &resources.ResourceArgs{
			ResourceGroupName:        resourceGroup.Name,
			ResourceProviderNamespace: pulumi.String("Microsoft.Storage"),
			ResourceType:             pulumi.String("storageAccounts"),
			ApiVersion:               pulumi.String("2022-09-01"),
			// This property is required even when empty
			ParentResourcePath:       pulumi.String(""),

			// These properties are optional
			Kind:                     pulumi.String("StorageV2"),
			Sku: pulumi.Map{
				"name": pulumi.String("Standard_LRS"),
			},

			// This is a generic property bag for all other properties
			Properties:               properties,
		})
		if err != nil {
			return err
		}

		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
name: azure-native-example
runtime: yaml
description: A minimal Azure Native Pulumi YAML program
resources:
  resourceGroup:
    type: azure-native:resources:ResourceGroup
    properties:
      location: westus2
  
  # Using the typed resource
  storageAccount:
    type: azure-native:storage:StorageAccount
    properties:
      resourceGroupName: ${resourceGroup.name}
      sku:
        name: Standard_LRS
      kind: StorageV2
  
  # Using the generic resource
  genericStorage:
    type: azure-native:resources:Resource
    properties:
      resourceGroupName: ${resourceGroup.name}
      resourceProviderNamespace: Microsoft.Storage
      resourceType: storageAccounts
      apiVersion: 2022-09-01
      # This property is required even when empty
      parentResourcePath: ""

      # These properties are optional
      kind: StorageV2
      sku:
        name: Standard_LRS

      # This is a generic property bag for all other properties
      properties:
        allowBlobPublicAccess: false
```

{{% /choosable %}}

{{% choosable language java %}}

```java
package myproject;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.azurenative.resources.ResourceGroup;
import com.pulumi.azurenative.resources.ResourceGroupArgs;
import com.pulumi.azurenative.resources.Resource;
import com.pulumi.azurenative.resources.ResourceArgs;
import com.pulumi.azurenative.storage.StorageAccount;
import com.pulumi.azurenative.storage.StorageAccountArgs;
import com.pulumi.azurenative.storage.enums.Kind;
import com.pulumi.azurenative.storage.enums.SkuName;
import com.pulumi.azurenative.storage.inputs.SkuArgs;

import java.util.Map;
import java.util.HashMap;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    private static void stack(Context ctx) {
        var resourceGroup = new ResourceGroup("resourceGroup");

        // Create a Storage Account using the typed resource
        var sa = new StorageAccount("sa", StorageAccountArgs.builder()
            .resourceGroupName(resourceGroup.name())
            .sku(SkuArgs.builder()
                .name(SkuName.Standard_LRS)
                .build())
            .kind(Kind.StorageV2)
            .build());

        // Create a Storage Account using the generic resource
        Map<String, Object> sku = new HashMap<>();
        sku.put("name", "Standard_LRS");

        Map<String, Object> properties = new HashMap<>();
        properties.put("allowBlobPublicAccess", false);

        var generic = new Resource("generic", ResourceArgs.builder()
            .resourceGroupName(resourceGroup.name())
            .resourceProviderNamespace("Microsoft.Storage")
            .resourceType("storageAccounts")
            .apiVersion("2022-09-01")
            // This property is required even when empty
            .parentResourcePath("")

            // These properties are optional
            .kind("StorageV2")
            .sku(sku)

            // This is a generic property bag for all other properties
            .properties(properties)
            .build());
    }
}
```

{{% /choosable %}}

{{< /chooser >}}

In most cases, we recommend using the local packages approach when you need a specific API version, and only falling back to the generic resource for special cases or resources not yet supported by the Pulumi provider.

## Getting Started

Firstly you will want to update your dependencies to point to the latest v3.x version.

For a smooth upgrade experience, we recommend if you're using Azure Native v1, first upgrade to v2 using our [v1 to v2 upgrade guide](/registry/packages/azure-native/from-v1-to-v2/). Then upgrade from v2 to v3 using our [v2 to v3 migration guide](/registry/packages/azure-native/from-v2-to-v3/). If you are on v2 now, just follow the [v2 to v3 migration guide](/registry/packages/azure-native/from-v2-to-v3/). This stepwise approach will help you resolve any deprecation warnings and make the migration process more manageable.

For language-specific installation instructions, see our [Azure Native setup guide](/registry/packages/azure-native/installation-configuration/).

## Conclusion

Azure Native V3 represents a significant step forward in our mission to provide the best possible developer experience for cloud infrastructure. By dramatically reducing SDK size while maintaining flexibility for version management, it now easier to build and deploy Azure resources with Pulumi.

We'd like to thank our community for their valuable feedback throughout the development of V3. Your input helped shape this release, and we're excited to see what you'll build with it.

Have feedback or issues? [Open an issue on GitHub](https://github.com/pulumi/pulumi-azure-native/issues), join our [Community Slack](https://slack.pulumi.com/) and post in the #azure channel, or reach out to us on [Twitter/X @PulumiCorp](https://twitter.com/PulumiCorp).

---
title: Get Started with Pulumi and Azure
meta_desc: Deploy your first Azure resources with Pulumi in under 5 minutes
type: page
layout: cloud-unified
no_on_this_page: true

cloud_name: Azure
subtitle: Deploy your first Azure resources in under 5 minutes
---

## Quick Setup

### 1. Sign up for Pulumi (Free)

Get started with Pulumi Cloud for free. Includes state management, secrets, and more.

<a href="https://app.pulumi.com/signup" class="btn-primary">Create Free Account</a>

### 2. Install Pulumi CLI

{{< chooser os "macos,linux,windows" >}}

{{% choosable os macos %}}

```bash
brew install pulumi/tap/pulumi
```

{{% /choosable %}}

{{% choosable os linux %}}

```bash
curl -fsSL https://get.pulumi.com | sh
```

{{% /choosable %}}

{{% choosable os windows %}}

```powershell
choco install pulumi
```

{{% /choosable %}}

{{< /chooser >}}

### 3. Configure Azure Credentials

```bash
az login
```

Or use a service principal:

```bash
export ARM_CLIENT_ID=<YOUR_CLIENT_ID>
export ARM_CLIENT_SECRET=<YOUR_CLIENT_SECRET>
export ARM_TENANT_ID=<YOUR_TENANT_ID>
export ARM_SUBSCRIPTION_ID=<YOUR_SUBSCRIPTION_ID>
```

### 4. Deploy Your First Resource

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language typescript %}}

Create a new project:

```bash
mkdir my-azure-app && cd my-azure-app
pulumi new azure-typescript
```

Example: Create a Storage Account

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as azure from "@pulumi/azure-native";

// Create a Resource Group
const resourceGroup = new azure.resources.ResourceGroup("myResourceGroup");

// Create a Storage Account
const storageAccount = new azure.storage.StorageAccount("mystorageacct", {
    resourceGroupName: resourceGroup.name,
    sku: {
        name: azure.storage.SkuName.Standard_LRS,
    },
    kind: azure.storage.Kind.StorageV2,
});

// Export the primary storage key
export const primaryStorageKey = pulumi.secret(storageAccount.primaryAccessKey);
```

Deploy your infrastructure:

```bash
pulumi up
```

{{% /choosable %}}

{{% choosable language python %}}

Create a new project:

```bash
mkdir my-azure-app && cd my-azure-app
pulumi new azure-python
```

Example: Create a Storage Account

```python
import pulumi
from pulumi_azure_native import resources, storage

# Create a Resource Group
resource_group = resources.ResourceGroup("myResourceGroup")

# Create a Storage Account
storage_account = storage.StorageAccount(
    "mystorageacct",
    resource_group_name=resource_group.name,
    sku=storage.SkuArgs(
        name=storage.SkuName.STANDARD_LRS
    ),
    kind=storage.Kind.STORAGE_V2
)

# Export the primary storage key
pulumi.export("primary_storage_key",
              pulumi.Output.secret(storage_account.primary_access_key))
```

Deploy your infrastructure:

```bash
pulumi up
```

{{% /choosable %}}

{{% choosable language go %}}

Create a new project:

```bash
mkdir my-azure-app && cd my-azure-app
pulumi new azure-go
```

Example: Create a Storage Account

```go
package main

import (
    "github.com/pulumi/pulumi-azure-native/sdk/v2/go/azure/resources"
    "github.com/pulumi/pulumi-azure-native/sdk/v2/go/azure/storage"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        // Create a Resource Group
        resourceGroup, err := resources.NewResourceGroup(ctx, "myResourceGroup", nil)
        if err != nil {
            return err
        }

        // Create a Storage Account
        storageAccount, err := storage.NewStorageAccount(ctx, "mystorageacct", &storage.StorageAccountArgs{
            ResourceGroupName: resourceGroup.Name,
            Sku: &storage.SkuArgs{
                Name: pulumi.String("Standard_LRS"),
            },
            Kind: pulumi.String("StorageV2"),
        })
        if err != nil {
            return err
        }

        // Export the primary storage key
        ctx.Export("primaryStorageKey", pulumi.ToSecret(storageAccount.PrimaryAccessKey))
        return nil
    })
}
```

Deploy your infrastructure:

```bash
pulumi up
```

{{% /choosable %}}

{{% choosable language csharp %}}

Create a new project:

```bash
mkdir my-azure-app && cd my-azure-app
pulumi new azure-csharp
```

Example: Create a Storage Account

```csharp
using Pulumi;
using Pulumi.AzureNative.Resources;
using Pulumi.AzureNative.Storage;
using Pulumi.AzureNative.Storage.Inputs;

class MyStack : Stack
{
    public MyStack()
    {
        // Create a Resource Group
        var resourceGroup = new ResourceGroup("myResourceGroup");

        // Create a Storage Account
        var storageAccount = new StorageAccount("mystorageacct", new StorageAccountArgs
        {
            ResourceGroupName = resourceGroup.Name,
            Sku = new SkuArgs
            {
                Name = SkuName.Standard_LRS
            },
            Kind = Kind.StorageV2
        });

        // Export the primary storage key
        this.PrimaryStorageKey = Output.CreateSecret(storageAccount.PrimaryAccessKey);
    }

    [Output]
    public Output<string> PrimaryStorageKey { get; set; }
}
```

Deploy your infrastructure:

```bash
pulumi up
```

{{% /choosable %}}

{{% choosable language java %}}

Create a new project:

```bash
mkdir my-azure-app && cd my-azure-app
pulumi new azure-java
```

Example: Create a Storage Account

```java
package myproject;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.azurenative.resources.ResourceGroup;
import com.pulumi.azurenative.storage.StorageAccount;
import com.pulumi.azurenative.storage.StorageAccountArgs;
import com.pulumi.azurenative.storage.inputs.SkuArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        // Create a Resource Group
        var resourceGroup = new ResourceGroup("myResourceGroup");

        // Create a Storage Account
        var storageAccount = new StorageAccount("mystorageacct", StorageAccountArgs.builder()
            .resourceGroupName(resourceGroup.name())
            .sku(SkuArgs.builder()
                .name("Standard_LRS")
                .build())
            .kind("StorageV2")
            .build());

        // Export the primary storage key
        ctx.export("primaryStorageKey",
                  storageAccount.primaryAccessKey().applyValue(key -> key));
    }
}
```

Deploy your infrastructure:

```bash
pulumi up
```

{{% /choosable %}}

{{% choosable language yaml %}}

Create a new project:

```bash
mkdir my-azure-app && cd my-azure-app
pulumi new azure-yaml
```

Example: Create a Storage Account

```yaml
name: my-azure-app
runtime: yaml

resources:
  # Create a Resource Group
  myResourceGroup:
    type: azure-native:resources:ResourceGroup

  # Create a Storage Account
  myStorageAccount:
    type: azure-native:storage:StorageAccount
    properties:
      resourceGroupName: ${myResourceGroup.name}
      sku:
        name: Standard_LRS
      kind: StorageV2

outputs:
  # Export the primary storage key
  primaryStorageKey:
    value: ${myStorageAccount.primaryAccessKey}
    secret: true
```

Deploy your infrastructure:

```bash
pulumi up
```

{{% /choosable %}}

## What's Next?

- [**View your stack in Pulumi Cloud →**](https://app.pulumi.com/stacks)
  Explore resource details, deployment history, and manage your infrastructure

- [**Follow the complete Azure tutorial →**](/docs/iac/get-started/azure/)
  Learn how to build and deploy applications on Azure

- [**Explore Azure examples →**](https://github.com/pulumi/examples#azure)
  Browse production-ready examples for common Azure architectures

- [**Learn Pulumi concepts →**](/docs/iac/concepts/)
  Understand stacks, state, configuration, and more

- [**Join the community →**](https://slack.pulumi.com)
  Get help and share knowledge with other Pulumi users

---
title: Get Started with Pulumi and Azure
meta_desc: Deploy Azure infrastructure with Pulumi using your favorite programming language
type: page
layout: cloud-progressive
no_on_this_page: true

cloud_name: Azure
subtitle: Choose your language and deploy Azure infrastructure in minutes
---

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language typescript %}}

## Get Started with TypeScript

Build Azure infrastructure using TypeScript's type safety and modern JavaScript features.

### Prerequisites

- [Node.js](https://nodejs.org/) version 14 or later
- [Azure Account](https://azure.microsoft.com/free/)
- Azure CLI configured (`az login`)

### Quick Start

#### 1. Sign up for Pulumi Cloud (Free)

<a href="https://app.pulumi.com/signup" class="btn-primary">Create Free Account</a>

Pulumi Cloud provides free state management, secrets encryption, and deployment history.

#### 2. Install Pulumi

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

#### 3. Create Your First Project

```bash
mkdir azure-quickstart && cd azure-quickstart
pulumi new azure-typescript
```

This creates a new Pulumi project with TypeScript configured for Azure.

#### 4. Deploy Infrastructure

Your project includes example code to create a Storage Account:

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

Deploy it:

```bash
pulumi up
```

### Next Steps

- [**View your stack in Pulumi Cloud →**](https://app.pulumi.com/stacks)
  Explore resource details, deployment history, and manage your infrastructure
- [Complete Azure TypeScript Tutorial →](/docs/iac/get-started/azure/)
- [Browse Azure TypeScript Examples →](https://github.com/pulumi/examples#typescript)
- [Learn Pulumi TypeScript Concepts →](/docs/iac/concepts/languages/javascript/)

{{% /choosable %}}

{{% choosable language python %}}

## Get Started with Python

Build Azure infrastructure using Python's simplicity and extensive ecosystem.

### Prerequisites

- [Python](https://www.python.org/) 3.8 or later
- [Azure Account](https://azure.microsoft.com/free/)
- Azure CLI configured (`az login`)

### Quick Start

#### 1. Sign up for Pulumi Cloud (Free)

<a href="https://app.pulumi.com/signup" class="btn-primary">Create Free Account</a>

Pulumi Cloud provides free state management, secrets encryption, and deployment history.

#### 2. Install Pulumi

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

#### 3. Create Your First Project

```bash
mkdir azure-quickstart && cd azure-quickstart
pulumi new azure-python
```

This creates a new Pulumi project with Python configured for Azure.

#### 4. Deploy Infrastructure

Your project includes example code to create a Storage Account:

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

Deploy it:

```bash
pulumi up
```

### Next Steps

- [**View your stack in Pulumi Cloud →**](https://app.pulumi.com/stacks)
  Explore resource details, deployment history, and manage your infrastructure
- [Complete Azure Python Tutorial →](/docs/iac/get-started/azure/)
- [Browse Azure Python Examples →](https://github.com/pulumi/examples#python)
- [Learn Pulumi Python Concepts →](/docs/iac/concepts/languages/python/)

{{% /choosable %}}

{{% choosable language go %}}

## Get Started with Go

Build Azure infrastructure using Go's performance and strong typing.

### Prerequisites

- [Go](https://golang.org/) 1.20 or later
- [Azure Account](https://azure.microsoft.com/free/)
- Azure CLI configured (`az login`)

### Quick Start

#### 1. Sign up for Pulumi Cloud (Free)

<a href="https://app.pulumi.com/signup" class="btn-primary">Create Free Account</a>

Pulumi Cloud provides free state management, secrets encryption, and deployment history.

#### 2. Install Pulumi

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

#### 3. Create Your First Project

```bash
mkdir azure-quickstart && cd azure-quickstart
pulumi new azure-go
```

This creates a new Pulumi project with Go configured for Azure.

#### 4. Deploy Infrastructure

Your project includes example code to create a Storage Account:

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

Deploy it:

```bash
pulumi up
```

### Next Steps

- [**View your stack in Pulumi Cloud →**](https://app.pulumi.com/stacks)
  Explore resource details, deployment history, and manage your infrastructure
- [Complete Azure Go Tutorial →](/docs/iac/get-started/azure/)
- [Browse Azure Go Examples →](https://github.com/pulumi/examples#go)
- [Learn Pulumi Go Concepts →](/docs/iac/concepts/languages/go/)

{{% /choosable %}}

{{% choosable language csharp %}}

## Get Started with C\#

Build Azure infrastructure using C# and the .NET ecosystem.

### Prerequisites

- [.NET](https://dotnet.microsoft.com/) 6.0 or later
- [Azure Account](https://azure.microsoft.com/free/)
- Azure CLI configured (`az login`)

### Quick Start

#### 1. Sign up for Pulumi Cloud (Free)

<a href="https://app.pulumi.com/signup" class="btn-primary">Create Free Account</a>

Pulumi Cloud provides free state management, secrets encryption, and deployment history.

#### 2. Install Pulumi

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

#### 3. Create Your First Project

```bash
mkdir azure-quickstart && cd azure-quickstart
pulumi new azure-csharp
```

This creates a new Pulumi project with C# configured for Azure.

#### 4. Deploy Infrastructure

Your project includes example code to create a Storage Account:

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

Deploy it:

```bash
pulumi up
```

### Next Steps

- [**View your stack in Pulumi Cloud →**](https://app.pulumi.com/stacks)
  Explore resource details, deployment history, and manage your infrastructure
- [Complete Azure C# Tutorial →](/docs/iac/get-started/azure/)
- [Browse Azure C# Examples →](https://github.com/pulumi/examples#dotnet)
- [Learn Pulumi C# Concepts →](/docs/iac/concepts/languages/dotnet/)

{{% /choosable %}}

{{% choosable language java %}}

## Get Started with Java

Build Azure infrastructure using Java's maturity and enterprise ecosystem.

### Prerequisites

- [Java](https://www.oracle.com/java/) 11 or later
- [Maven](https://maven.apache.org/) 3.6.1 or later
- [Azure Account](https://azure.microsoft.com/free/)
- Azure CLI configured (`az login`)

### Quick Start

#### 1. Sign up for Pulumi Cloud (Free)

<a href="https://app.pulumi.com/signup" class="btn-primary">Create Free Account</a>

Pulumi Cloud provides free state management, secrets encryption, and deployment history.

#### 2. Install Pulumi

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

#### 3. Create Your First Project

```bash
mkdir azure-quickstart && cd azure-quickstart
pulumi new azure-java
```

This creates a new Pulumi project with Java configured for Azure.

#### 4. Deploy Infrastructure

Your project includes example code to create a Storage Account:

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

Deploy it:

```bash
pulumi up
```

### Next Steps

- [**View your stack in Pulumi Cloud →**](https://app.pulumi.com/stacks)
  Explore resource details, deployment history, and manage your infrastructure
- [Complete Azure Java Tutorial →](/docs/iac/get-started/azure/)
- [Browse Azure Java Examples →](https://github.com/pulumi/examples#java)
- [Learn Pulumi Java Concepts →](/docs/iac/concepts/languages/java/)

{{% /choosable %}}

{{% choosable language yaml %}}

## Get Started with YAML

Build Azure infrastructure using simple, declarative YAML configuration.

### Prerequisites

- [Azure Account](https://azure.microsoft.com/free/)
- Azure CLI configured (`az login`)

### Quick Start

#### 1. Sign up for Pulumi Cloud (Free)

<a href="https://app.pulumi.com/signup" class="btn-primary">Create Free Account</a>

Pulumi Cloud provides free state management, secrets encryption, and deployment history.

#### 2. Install Pulumi

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

#### 3. Create Your First Project

```bash
mkdir azure-quickstart && cd azure-quickstart
pulumi new azure-yaml
```

This creates a new Pulumi project with YAML configured for Azure.

#### 4. Deploy Infrastructure

Your project includes example YAML to create a Storage Account:

```yaml
name: azure-quickstart
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

Deploy it:

```bash
pulumi up
```

### Next Steps

- [**View your stack in Pulumi Cloud →**](https://app.pulumi.com/stacks)
  Explore resource details, deployment history, and manage your infrastructure
- [Complete Azure YAML Tutorial →](/docs/iac/get-started/azure/)
- [Browse Azure YAML Examples →](https://github.com/pulumi/examples#yaml)
- [Learn Pulumi YAML Concepts →](/docs/iac/concepts/languages/yaml/)

{{% /choosable %}}

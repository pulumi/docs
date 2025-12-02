---
title_tag: Create a New Project | Azure
title: Create project
h1: "Get started with Pulumi and Azure"
meta_desc: This page provides an overview of how to create a new Azure + Pulumi project.
weight: 4
menu:
    iac:
        name: Create project
        identifier: azure-get-started.create-project
        parent: azure-get-started
        weight: 4
aliases:
    - /docs/quickstart/azure/create-project/
    - /docs/clouds/azure/get-started/create-project/
    - /docs/quickstart/azure/review-project/
    - /docs/clouds/azure/get-started/review-project/
---

## Create a new project

A [**project**](/docs/iac/concepts/projects) is a program in your chosen language that defines a collection of related cloud resources. In this step, you will create a new project.

### Initializing your project

Each project lives in its own directory. Create a new one:

{{% choosable os "linux,macos" %}}

```bash
$ mkdir quickstart
```

{{% /choosable %}}
{{% choosable os "windows" %}}

```powershell
> mkdir quickstart
```

{{% /choosable %}}

Change into the new directory:

{{% choosable os "linux,macos" %}}

```bash
$ cd quickstart
```

{{% /choosable %}}
{{% choosable os "windows" %}}

```powershell
> cd quickstart
```

{{% /choosable %}}

Now initialize a new Pulumi project for Azure using the `pulumi new` command:

{{% choosable language typescript %}}

{{% choosable os "linux,macos" %}}

```bash
$ pulumi new azure-typescript
```

{{% /choosable %}}
{{% choosable os "windows" %}}

```powershell
> pulumi new azure-typescript
```

{{% /choosable %}}

{{% /choosable %}}
{{% choosable language python %}}

{{% choosable os "linux,macos" %}}

```bash
$ pulumi new azure-python
```

{{% /choosable %}}
{{% choosable os "windows" %}}

```powershell
> pulumi new azure-python
```

{{% /choosable %}}

{{% /choosable %}}
{{% choosable language csharp %}}

{{% choosable os "linux,macos" %}}

```bash
$ pulumi new azure-csharp
```

{{% /choosable %}}
{{% choosable os "windows" %}}

```powershell
> pulumi new azure-csharp
```

{{% /choosable %}}

{{% /choosable %}}
{{% choosable language go %}}

{{% choosable os "linux,macos" %}}

```bash
$ pulumi new azure-go
```

{{% /choosable %}}
{{% choosable os "windows" %}}

```powershell
> pulumi new azure-go
```

{{% /choosable %}}

{{% /choosable %}}

{{% choosable language java %}}

{{% choosable os "linux,macos" %}}

```bash
$ pulumi new azure-java
```

{{% /choosable %}}
{{% choosable os "windows" %}}

```powershell
> pulumi new azure-java
```

{{% /choosable %}}

{{% /choosable %}}

{{% choosable language yaml %}}

{{% choosable os "linux,macos" %}}

```bash
$ pulumi new azure-yaml
```

{{% /choosable %}}
{{% choosable os "windows" %}}

```powershell
> pulumi new azure-yaml
```

{{% /choosable %}}

{{% /choosable %}}

The `pulumi new` command interactively walks through initializing a new project, as well as creating a
[**stack**](/docs/iac/concepts/stacks) and [**configuring**](/docs/iac/concepts/config) it. A stack is an instance of your
project and you may have many of them -- like `dev`, `staging`, and `prod` -- each with different configuration settings.

You will be prompted for configuration values such as an Azure location. You can hit ENTER to accept the default of `WestUS2`,
or can type in another value such as `eastus`:

```
azure-native:location: The Azure location to use: (WestUS2) eastus
```

{{< cli-note >}}

{{% choosable language "typescript" %}}

After some dependency installations from `npm`, the project and stack will be ready.

{{% /choosable %}}

{{% choosable language python %}}

After the command completes, the project and stack will be ready.

{{% /choosable %}}

{{% choosable language go %}}

After the command completes, the project and stack will be ready.

{{% /choosable %}}

{{% choosable language "csharp,fsharp,visualbasic" %}}

After the command completes, the project and stack will be ready.

{{% /choosable %}}

{{% choosable language java %}}

After the command completes, the project and stack will be ready.

{{% /choosable %}}

{{% choosable language yaml %}}

After the command completes, the project and stack will be ready.

{{% /choosable %}}

### Review your new project's contents

If you list the contents of your directory, you'll see some key files:

{{% choosable language java %}}

- `src/main/java/myproject` is the project's Java package root

{{% /choosable %}}

{{% choosable language "typescript,python,go,csharp,java" %}}

- <span>{{< langfile >}}</span> contains your project's main code that declares an Azure resource group and storage account
- `Pulumi.yaml` is a [project file](/docs/iac/concepts/projects/project-file) containing metadata about your project like its name

{{% /choosable %}}
{{% choosable language "yaml" %}}

- `Pulumi.yaml` is a [project file](/docs/iac/concepts/projects/project-file) containing metadata about your project, like its name, as well as declaring your project's resources

{{% /choosable %}}

- `Pulumi.dev.yaml` contains configuration values for the stack you just initialized

Now examine the code in {{< langfile >}}:

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

const storageAccountKeys = storage.listStorageAccountKeysOutput({
    resourceGroupName: resourceGroup.name,
    accountName: storageAccount.name
});

// Export the primary key of the Storage Account
export const primaryStorageKey = pulumi.secret(storageAccountKeys.keys[0].value);
```

{{% /choosable %}}
{{% choosable language python %}}

```python
"""An Azure RM Python Pulumi program"""

import pulumi
from pulumi_azure_native import storage
from pulumi_azure_native import resources

# Create an Azure Resource Group
resource_group = resources.ResourceGroup("resource_group")

# Create an Azure resource (Storage Account)
account = storage.StorageAccount(
    "sa",
    resource_group_name=resource_group.name,
    sku={
        "name": storage.SkuName.STANDARD_LRS,
    },
    kind=storage.Kind.STORAGE_V2,
)

# Export the primary key of the Storage Account
primary_key = (
    pulumi.Output.all(resource_group.name, account.name)
    .apply(
        lambda args: storage.list_storage_account_keys(
            resource_group_name=args[0], account_name=args[1]
        )
    )
    .apply(lambda accountKeys: accountKeys.keys[0].value)
)

pulumi.export("primary_storage_key", primary_key)
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
        account, err := storage.NewStorageAccount(ctx, "sa", &storage.StorageAccountArgs{
			ResourceGroupName: resourceGroup.Name,
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

    var storageAccountKeys = ListStorageAccountKeys.Invoke(new ListStorageAccountKeysInvokeArgs
    {
        ResourceGroupName = resourceGroup.Name,
        AccountName = storageAccount.Name
    });

    var primaryStorageKey = storageAccountKeys.Apply(accountKeys =>
    {
        var firstKey = accountKeys.Keys[0].Value;
        return Output.CreateSecret(firstKey);
    });

    // Export the primary key of the Storage Account
    return new Dictionary<string, object?>
    {
        ["primaryStorageKey"] = primaryStorageKey
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
import com.pulumi.azurenative.storage.StorageFunctions;
import com.pulumi.azurenative.storage.enums.Kind;
import com.pulumi.azurenative.storage.enums.SkuName;
import com.pulumi.azurenative.storage.inputs.ListStorageAccountKeysArgs;
import com.pulumi.azurenative.storage.inputs.SkuArgs;
import com.pulumi.azurenative.storage.outputs.EndpointsResponse;
import com.pulumi.core.Either;
import com.pulumi.core.Output;
import com.pulumi.deployment.InvokeOptions;

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

            var primaryStorageKey = getStorageAccountPrimaryKey(
                    resourceGroup.name(),
                    storageAccount.name());

            ctx.export("primaryStorageKey", primaryStorageKey);
        });
    }

    private static Output<String> getStorageAccountPrimaryKey(Output<String> resourceGroupName,
                                                              Output<String> accountName) {
        return Output.tuple(resourceGroupName, accountName).apply(tuple -> {
            var actualResourceGroupName = tuple.t1;
            var actualAccountName = tuple.t2;
            var invokeResult = StorageFunctions.listStorageAccountKeys(ListStorageAccountKeysArgs.builder()
                    .resourceGroupName(actualResourceGroupName)
                    .accountName(actualAccountName)
                    .build(), InvokeOptions.Empty);
            return Output.of(invokeResult)
                    .applyValue(r -> r.keys().get(0).value())
                    .asSecret();
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
  # Create an Azure resource (Storage Account)
  sa:
    type: azure-native:storage:StorageAccount
    properties:
      resourceGroupName: ${resourceGroup.name}
      sku:
        name: Standard_LRS
      kind: StorageV2

variables:
  storageAccountKeys:
    fn::azure-native:storage:listStorageAccountKeys:
      resourceGroupName: ${resourceGroup.name}
      accountName: ${sa.name}

outputs:
  # Export the primary key of the Storage Account
  primaryStorageKey: ${storageAccountKeys.keys[0].value}
```

{{% /choosable %}}

The program declares an Azure Resource Group and Storage Account
[resources](/docs/iac/concepts/resources) and exports the storage account's primary key as a [stack output](/docs/iac/concepts/stacks/#outputs).
The primary key is marked as a secret to protect sensitive credential data. To demonstrate working with outputs,
you'll add a non-secret output that exports the storage account's name for convenient reference.

{{% choosable language typescript %}}

After the line that exports the primary key, add the following export to also export the storage account name:

```typescript
// Export the primary key of the Storage Account
export const primaryStorageKey = pulumi.secret(storageAccountKeys.keys[0].value);
export const storageAccountName = storageAccount.name;  // Add this line
```

{{% /choosable %}}

{{% choosable language python %}}

After the line that exports the primary key, add the following export to also export the storage account name:

```python
pulumi.export("primary_storage_key", primary_key)
pulumi.export("storage_account_name", account.name)  # Add this line
```

{{% /choosable %}}

{{% choosable language go %}}

After the `ctx.Export("primaryStorageKey", ...)` statement, add the following export to also export the storage account name:

```go
// Export the primary key of the Storage Account
ctx.Export("primaryStorageKey", pulumi.All(resourceGroup.Name, account.Name).ApplyT(
    func(args []interface{}) (string, error) {
        // ... existing code removed for brevity ...
    },
))
ctx.Export("storageAccountName", account.Name)  // Add this line

return nil
```

{{% /choosable %}}

{{% choosable language csharp %}}

Update the returned Dictionary to also export the storage account name:

```csharp
return new Dictionary<string, object?>
{
    ["primaryStorageKey"] = primaryStorageKey,
    ["storageAccountName"] = storageAccount.Name  // Add this line
};
```

{{% /choosable %}}

{{% choosable language java %}}

After `ctx.export("primaryStorageKey", ...)`, add the following export to also export the storage account name:

```java
ctx.export("primaryStorageKey", primaryStorageKey);
ctx.export("storageAccountName", storageAccount.name());  // Add this line
```

{{% /choosable %}}

{{% choosable language yaml %}}

In the `outputs` section, add the following line to also export the storage account name:

```yaml
outputs:
  # Export the primary key of the Storage Account
  primaryStorageKey: ${storageAccountKeys.keys[0].value}
  storageAccountName: ${sa.name}  # Add this line
```

{{% /choosable %}}

Now you're ready for your first deployment!

{{< get-started-stepper >}}

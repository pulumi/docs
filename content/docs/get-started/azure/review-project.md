---
title: Review the New Project | Azure
h1: Review the New Project
linktitle: Review the New Project
meta_desc: This page provides an overview on how to a review a new Azure project.
weight: 6
menu:
  getstarted:
    parent: azure
    identifier: azure-review-project

aliases: ["/docs/quickstart/azure/review-project/"]
---

Let's review some of the generated project files:

- `Pulumi.yaml` defines the [project]({{< prelref "/docs/intro/concepts/project" >}}).
- `Pulumi.dev.yaml` contains [configuration]({{< prelref "/docs/intro/concepts/config" >}}) values for the [stack]({{< prelref "/docs/intro/concepts/stack" >}}) we initialized.

{{% choosable language csharp %}}

- `Program.cs` with a simple entry point.

{{% /choosable %}}

- {{< langfile >}} is the Pulumi program that defines our stack resources. Let's examine it.

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language javascript %}}

```javascript
"use strict";
const pulumi = require("@pulumi/pulumi");
const azure = require("@pulumi/azure");

// Create an Azure Resource Group
const resourceGroup = new azure.core.ResourceGroup("resourceGroup");

// Create an Azure resource (Storage Account)
const account = new azure.storage.Account("storage", {
    resourceGroupName: resourceGroup.name,
    accountTier: "Standard",
    accountReplicationType: "LRS",
});

// Export the connection string for the storage account
exports.connectionString = account.primaryConnectionString;
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as azure from "@pulumi/azure";

// Create an Azure Resource Group
const resourceGroup = new azure.core.ResourceGroup("resourceGroup");

// Create an Azure resource (Storage Account)
const account = new azure.storage.Account("storage", {
    resourceGroupName: resourceGroup.name,
    accountTier: "Standard",
    accountReplicationType: "LRS",
});

// Export the connection string for the storage account
export const connectionString = account.primaryConnectionString;
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
from pulumi_azure import core, storage

# Create an Azure Resource Group
resource_group = core.ResourceGroup("resource_group")

# Create an Azure resource (Storage Account)
account = storage.Account("storage",
    resource_group_name=resource_group.name,
    account_tier='Standard',
    account_replication_type='LRS')

# Export the connection string for the storage account
pulumi.export('connection_string', account.primary_connection_string)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
    "github.com/pulumi/pulumi-azure/sdk/v3/go/azure/core"
    "github.com/pulumi/pulumi-azure/sdk/v3/go/azure/storage"
    "github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        // Create an Azure Resource Group
        resourceGroup, err := core.NewResourceGroup(ctx, "resourceGroup", &core.ResourceGroupArgs{
            Location: pulumi.String("WestUS"),
        })
        if err != nil {
            return err
        }

        // Create an Azure resource (Storage Account)
        account, err := storage.NewAccount(ctx, "storage", &storage.AccountArgs{
            ResourceGroupName:      resourceGroup.Name,
            AccountTier:            pulumi.String("Standard"),
            AccountReplicationType: pulumi.String("LRS"),
        })
        if err != nil {
            return err
        }

        // Export the connection string for the storage account
        ctx.Export("connectionString", account.PrimaryConnectionString)
        return nil
    })
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using Pulumi;
using Pulumi.Azure.Core;
using Pulumi.Azure.Storage;

class MyStack : Stack
{
    public MyStack()
    {
        // Create an Azure Resource Group
        var resourceGroup = new ResourceGroup("resourceGroup");

        // Create an Azure Storage Account
        var storageAccount = new Account("storage", new AccountArgs
        {
            ResourceGroupName = resourceGroup.Name,
            AccountReplicationType = "LRS",
            AccountTier = "Standard"
        });

        // Export the connection string for the storage account
        this.ConnectionString = storageAccount.PrimaryConnectionString;
    }

    [Output]
    public Output<string> ConnectionString { get; set; }
}
```

{{% /choosable %}}

This Pulumi program creates an Azure resource group and storage account and exports the storage account's connection string.

**Note**: In this program, the location of the resource group is set in the configuration setting `azure:location` (check the `Pulumi.dev.yaml` file). This is an easy way to set a global location for your program so you don't have to specify the location for each resource manually. The location for the storage account is automatically derived from the location of the resource group. To override the location for a resource, simply set the location property to one of Azure's [supported locations](https://azure.microsoft.com/en-us/global-infrastructure/locations/).

{{% choosable language python %}}

{{< python-venv >}}

{{% /choosable %}}

Next, we'll deploy the stack.

{{< get-started-stepper >}}

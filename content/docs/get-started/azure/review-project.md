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

- `Pulumi.yaml` defines the [project]({{< relref "/docs/intro/concepts/project" >}}).
- `Pulumi.dev.yaml` contains [configuration]({{< relref "/docs/intro/concepts/config" >}}) values for the [stack]({{< relref "/docs/intro/concepts/stack" >}}) we initialized.
- {{< langfile >}} is the Pulumi program that defines our stack resources. Let's examine it.

{{< langchoose nogo csharp >}}

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

```csharp
using System.Collections.Generic;
using System.Threading.Tasks;
using Pulumi;
using Pulumi.Azure;

class Program
{
    static Task Main()
    {
        return Deployment.RunAsync(() => {
            // Create an Azure Resource Group
            var resourceGroup = new Azure.Core.ResourceGroup("resourceGroup");

            // Create an Azure resource (Storage Account)
            var account = new Azure.Storage.Account("storage", new Azure.Storage.AccountArgs
            {
                ResourceGroupName = resourceGroup.Name,
                AccountTier = "Standard",
                AccountReplicationType = "LRS",
            });

            // Export the connection string for the storage account
            return new Dictionary<string, object> {
                { "connectionString", account.PrimaryConnectionString },
            };
        });
    }
}
```

This Pulumi program creates an Azure resource group and storage account and exports the storage account's connection string.

**Note**: In this program, the location of the resource group is set in the configuration setting `azure:location` (check the `Pulumi.dev.yaml` file). This is an easy way to set a global location for your program so you don't have to specify the location for each resource manually. The location for the storage account is automatically derived from the location of the resource group. To override the location for a resource, simply set the location property to one of Azure's [supported locations](https://azure.microsoft.com/en-us/global-infrastructure/locations/).

{{% lang python %}}
For Python, before we deploy the stack, the following commands need to be run to create a virtual environment, activate it, and install dependencies:

```bash
$ virtualenv -p python3 venv
```

```bash
$ source venv/bin/activate
```

```bash
$ pip3 install -r requirements.txt
```

{{% /lang %}}

Next, we'll deploy the stack.

{{< get-started-stepper >}}

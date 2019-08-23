---
title: Modify the Program
weight: 8
menu:
  getstarted:
    parent: azure
    identifier: azure-modify-program

aliases: ["/docs/quickstart/azure/modify-program/"]
---

Now that we have an instance of our Pulumi program deployed, let's enforce HTTPS-only communication for our storage account. This means, when making requests to this storage account only HTTPS traffic is allowed.

Replace the entire contents of {{< langfile >}} with the following:

{{< langchoose nogo >}}

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
    enableHttpsTrafficOnly: true,
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
    enableHttpsTrafficOnly: true,
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
    account_replication_type='LRS',
    enable_https_traffic_only=True)

# Export the connection string for the storage account
pulumi.export('connection_string', account.primary_connection_string)
```

Next, we'll deploy the changes.

{{< get-started-stepper >}}

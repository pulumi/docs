---
title: Modify the Program
weight: 8
menu:
  quickstart:
    parent: azure
    identifier: azure-modify-program
---

Let's update our program to do something a little more interesting.

Replace the entire contents of {{< langfile >}} with the following:

{{< langchoose nogo >}}

```javascript
"use strict";
const pulumi = require("@pulumi/pulumi");
const azure = require("@pulumi/azure");

// Create an Azure Resource Group
const resourceGroup = new azure.core.ResourceGroup("resourceGroup", {
    location: "WestUS",
});

// Create an Azure Container Group
const container = new azure.containerservice.Group("nginx", {
    containers: [{
        name: "nginx",
        image: "nginx",
        memory: 1,
        cpu: 1,
        ports: [{
            port: 80,
            protocol: "TCP"
        }],
    }],
    osType: "Linux",
    resourceGroupName: resourceGroup.name,
    location: resourceGroup.location,
});

// Export the public IP of the container
exports.ip = container.ipAddress;
```

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as azure from "@pulumi/azure";

// Create an Azure Resource Group
const resourceGroup = new azure.core.ResourceGroup("resourceGroup", {
    location: "WestUS",
});

// Create an Azure Container Group
const container = new azure.containerservice.Group("nginx", {
    containers: [{
        name: "nginx",
        image: "nginx",
        memory: 1,
        cpu: 1,
        ports: [{
            port: 80,
            protocol: "TCP"
        }],
    }],
    osType: "Linux",
    resourceGroupName: resourceGroup.name,
    location: resourceGroup.location,
});

// Export the public IP of the container
export const ip = container.ipAddress;
```

```python
import pulumi
from pulumi_azure import core, containerservice

# Create an Azure Resource Group
resource_group = core.ResourceGroup("resource_group",
    location='WestUS')

# Create an Azure Container Group
container = containerservice.Group("nginx",
    containers=[{
        name: "nginx",
        image: "nginx",
        memory: 1,
        cpu: 1,
        ports: [{
            port: 80,
            protocol: "TCP"
        }],
    }],
    os_type="Linux",
    resource_group_name=resource_group.name,
    location=resource_group.location)

# Export the public IP of the container
pulumi.export('ip', container.ip_address)
```

Our program now creates a simple NGINX container to Azure Container Instance (ACI).

Next, we'll deploy the changes.

{{< get-started-stepper >}}

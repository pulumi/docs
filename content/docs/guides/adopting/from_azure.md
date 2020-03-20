---
title: "From Azure Resource Manager (ARM)"
meta_desc: Migrate your existing Azure Resource Manager (ARM) templates and/or coexist with existing deployments.
menu:
  userguides:
    parent: adopting
    weight: 4
---

<img src="/logos/tech/azure_arm.png" align="right" class="h-32 px-8 pb-4">

If your team has already provisioned infrastructure using Azure Resource Manager (ARM) Templates, and you'd like to adopt Pulumi, you have three primary strategies you can take:

* [**Coexist**](#referencing-deployment-outputs) with resources provisioned by ARM by referencing deployment outputs.
* [**Import**]({{< relref "import" >}}) existing resources into Pulumi in the usual way.
* [**Convert**](#converting-deployments-and-resources) your deployments to use Pulumi and then incrementally migrate resources.

## Referencing Stack Outputs

It is possible to reference existing Azure Resource Manager (ARM) template deployments from your program. It doesn't mattter how these templates and deployments were created. This lets you read properties of a deployment for use within your Pulumi program. This includes output values computed from resources provisioned that stack.

For instance, let's say your infrastructure team has provisioned your Azure storage account using ARM and you need to use the Storage Account name to provision something new from your Pulumi program. One approach is to hardcode the name but this is brittle and, if it ever changes, you'd need to go and manually update the hardcoded value.

Instead, you can look up that ARM deployment by name and use one of its output values. The following example reads a deployment by its fully qualified ID and then uses the exported `storageAccountName` value to upload a private zipfile to blob storage, containing a `wwwroot/` directory locally:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
let azure = require("@pulumi/azure");
let pulumi = require("@pulumi/pulumi");

// Read the deployment and the storage account name.
let deployment = azure.core.TemplateDeployment.get("myStorageDeployment",
    "/subscriptions/0292631f-7a9b-4142-90b2-96badd5eafa8/resourceGroups/myrg8fd69ec2/providers/Microsoft.Resources/deployments/myStorageDeployment62ba53a3");
let storageAccountName = deployment.outputs["storageAccountName"];

// Create a blob for our own deployment.
let blob = new azure.storage.ZipBlob("myBlob", {
    storageAccountName: storageAccountName,
    storageContainerName: new azure.storage.Container("myStorageContainer", {
        storageAccountName: storageAccountName,
        containerAccessType: "private",
    }).name,
    type: "block",
    content: new pulumi.asset.FileArchive("wwwroot"),
});

module.exports = {
    blobUrl: blob.url,
};
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as azure from "@pulumi/azure";
import * as pulumi from "@pulumi/pulumi";

// Read the deployment and the storage account name.
const deployment = azure.core.TemplateDeployment.get("myStorageDeployment",
    "/subscriptions/0292631f-7a9b-4142-90b2-96badd5eafa8/resourceGroups/myrg8fd69ec2/providers/Microsoft.Resources/deployments/myStorageDeployment62ba53a3");
const storageAccountName = deployment.outputs["storageAccountName"];

// Create a blob for our own deployment.
const blob = new azure.storage.ZipBlob("myBlob", {
    storageAccountName: storageAccountName,
    storageContainerName: new azure.storage.Container("myStorageContainer", {
        storageAccountName: storageAccountName,
        containerAccessType: "private",
    }).name,
    type: "block",
    content: new pulumi.asset.FileArchive("wwwroot"),
});

export const blobUrl = blob.url;
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
import pulumi_azure as azure

# Read the deployment and the storage account name.
deployment = azure.core.TemplateDeployment.get('myStorageDeployment',
    '/subscriptions/0292631f-7a9b-4142-90b2-96badd5eafa8/resourceGroups/myrg8fd69ec2/providers/Microsoft.Resources/deployments/myStorageDeployment62ba53a3')
storage_account_name = deployment.outputs['storageAccountName']

# Create a blob for our own deployment.
blob = azure.storage.ZipBlob('myBlob',
    storage_account_name=storage_account_name,
    storage_container_name=azure.storage.Container('myStorageContainer',
        storage_account_name=storage_account_name,
        container_access_type='private',
    ).name,
    type='block',
    content=pulumi.asset.FileArchive('wwwroot'),
)

pulumi.export('blob_url', blob.url)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
    "github.com/pulumi/pulumi-azure/sdk/go/azure/core"
    "github.com/pulumi/pulumi-azure/sdk/go/azure/storage"
    "github.com/pulumi/pulumi/sdk/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        // Read the deployment and the storage account name.
        deployment, err := core.GetTemplateDeployment(ctx, "myStorageDeployment",
            "/subscriptions/0292631f-7a9b-4142-90b2-96badd5eafa8/resourceGroups/myrg8fd69ec2/providers/Microsoft.Resources/deployments/myStorageDeployment62ba53a3",
            nil)
        if err != nil {
            return nil
        }
        storageAccountName := deployment.Outputs["storageAccountName"].(string)

        // Create a blob for our own deployment.
        cont, err := storage.NewContainer(ctx, "myStorageContainer", &storage.ContainerArgs{
            StorageAccountName: pulumi.String(storageAccountName),
            ContainerAccessType: pulumui.String("private"),
        })
        if err != nil {
            return err
        }
        blob, err := storage.NewZipBlob(ctx, "myBlob", &storage.ZipBlobArgs{
            StorageAccountName: pulumi.String(storageAccountName),
            StorageContainerName: cont.Name,
            Type: pulumi.String("block"),
            Content: pulumi.NewFileArchive("wwwroot"),
        })
        if err != nil {
            return err
        }

        ctx.Export("blobUrl", blob.Url)
        return nil
    })
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using System.Threading.Tasks;

using Pulumi;
using Core = Pulumi.Azure.Core;
using Storage = Pulumi.Azure.Storage;

class Program
{
    static Task<int> Main()
    {
        return Deployment.RunAsync(async () =>
        {
            // Read the deployment and the storage account name.
            var deployment = Core.TemplateDeployment.Get("myStorageDeployment",
                "/subscriptions/0292631f-7a9b-4142-90b2-96badd5eafa8/resourceGroups/myrg8fd69ec2/providers/Microsoft.Resources/deployments/myStorageDeployment62ba53a3");
            var storageAccountName = (string)deployment.Outputs["storageAccountName"];

            // Create a blob for our own deployment.
            var blob = new Storage.ZipBlob("myBlob", new Storage.ZipBlobArgs
            {
                StorageAccountName = storageAccountName,
                StorageContainerName = new Storage.Container("myStorageContainer", new Storage.ContainerArgs
                {
                    StorageAccountName = storageAccountName,
                    ContainerAccessType = "private",
                }.Name,
                Type = "block",
                Content = new FileArchive("wwwroot"),
            });

            return new Dictionary<string, object?>({
                { "blobUrl", blob.Url },
            });
        });
    }
}
```

{{% /choosable %}}

{{< /chooser >}}

All we need to do is run `pulumi up` and the Pulumi runtime will know how to query the ARM deployment to retrieve its output values. In this case, the deployment and all of its resources are treated entirely as read-only, and Pulumi will never attempt to modify any of them.

Notice that the ID is of the format: `/subscriptions/<YOUR-SUBSCRIPTION-ID>/resourceGroups/<DEPLOYMENT-RG-ID>/providers/Microsoft.Resources/deployments/<DEPLOYMENT-ID>`. Please consult the Azure CLI or portal to find this ID.

> Although we've hard-coded the ARM deployment ID here, it's common to dynamically compute a name using unique per-stack information, like the stack name, Azure location, or other configuration variables.

## Converting Stacks and Resources

Let's say you want to migrate from ARM to Pulumi and that simply co-existing side-by-side as shown above isn't sufficient. There are two approaches:

1. Deploy your ARM template using Pulumi.
2. Migrate resources from your ARM deployments to Pulumi code.

Depending on what you're trying to accomplish, you may prefer to start with (1) and move to (2) incrementally, or simply jump straight to (2) directly.

### Deploy Templates Using Pulumi

The Pulumi Azure package [provides an ARM TemplateDeployment]({{< relref "/docs/reference/pkg/nodejs/pulumi/azure/core#TemplateDeployment" >}}) resource type. Using this type, you can deploy an existing ARM template written in JSON without needing to make any edits to it.

For instance, this code deploys a simple ARM template using the given parameters, and exports the resulting Storage Account name:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
let pulumi = require("@pulumi/pulumi");
let azure = require("@pulumi/azure");

let resourceGroup = new azure.core.ResourceGroup("myRG");

let template = `{
  "$schema": "https://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#",
  "contentVersion": "1.0.0.0",
  "parameters": {
    "storageAccountType": {
      "type": "string",
      "defaultValue": "Standard_LRS",
      "allowedValues": [
        "Standard_LRS",
        "Standard_GRS",
        "Standard_ZRS"
      ],
      "metadata": {
        "description": "Storage Account type"
      }
    }
  },
  "variables": {
    "location": "[resourceGroup().location]",
    "storageAccountName": "[concat(uniquestring(resourceGroup().id), 'storage')]",
    "apiVersion": "2015-06-15"
  },
  "resources": [
    {
      "type": "Microsoft.Storage/storageAccounts",
      "name": "[variables('storageAccountName')]",
      "apiVersion": "[variables('apiVersion')]",
      "location": "[variables('location')]",
      "properties": {
        "accountType": "[parameters('storageAccountType')]"
      }
    }
  ],
  "outputs": {
    "storageAccountName": {
      "type": "string",
      "value": "[variables('storageAccountName')]"
    }
  }
}
`;

let deployment = new azure.core.TemplateDeployment("myStorageDeployment", {
    resourceGroupName: resourceGroup.name,
    templateBody: template,
    parameters: {
        "storageAccountType": "Standard_GRS",
    },
    deploymentMode: "Incremental",
});

module.exports = {
    storageAccountName = deployment.outputs["storageAccountName"],
};
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as azure from "@pulumi/azure";

const resourceGroup = new azure.core.ResourceGroup("myRG");

const template = `{
  "$schema": "https://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#",
  "contentVersion": "1.0.0.0",
  "parameters": {
    "storageAccountType": {
      "type": "string",
      "defaultValue": "Standard_LRS",
      "allowedValues": [
        "Standard_LRS",
        "Standard_GRS",
        "Standard_ZRS"
      ],
      "metadata": {
        "description": "Storage Account type"
      }
    }
  },
  "variables": {
    "location": "[resourceGroup().location]",
    "storageAccountName": "[concat(uniquestring(resourceGroup().id), 'storage')]",
    "apiVersion": "2015-06-15"
  },
  "resources": [
    {
      "type": "Microsoft.Storage/storageAccounts",
      "name": "[variables('storageAccountName')]",
      "apiVersion": "[variables('apiVersion')]",
      "location": "[variables('location')]",
      "properties": {
        "accountType": "[parameters('storageAccountType')]"
      }
    }
  ],
  "outputs": {
    "storageAccountName": {
      "type": "string",
      "value": "[variables('storageAccountName')]"
    }
  }
}
`;

const deployment = new azure.core.TemplateDeployment("myStorageDeployment", {
    resourceGroupName: resourceGroup.name,
    templateBody: template,
    parameters: {
        "storageAccountType": "Standard_GRS",
    },
    deploymentMode: "Incremental",
});

export const storageAccountName = deployment.outputs["storageAccountName"];
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
import pulumi_azure as azure

resource_group = azure.core.ResourceGroup('myRG')

template = """{
  "$schema": "https://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#",
  "contentVersion": "1.0.0.0",
  "parameters": {
    "storageAccountType": {
      "type": "string",
      "defaultValue": "Standard_LRS",
      "allowedValues": [
        "Standard_LRS",
        "Standard_GRS",
        "Standard_ZRS"
      ],
      "metadata": {
        "description": "Storage Account type"
      }
    }
  },
  "variables": {
    "location": "[resourceGroup().location]",
    "storageAccountName": "[concat(uniquestring(resourceGroup().id), 'storage')]",
    "apiVersion": "2015-06-15"
  },
  "resources": [
    {
      "type": "Microsoft.Storage/storageAccounts",
      "name": "[variables('storageAccountName')]",
      "apiVersion": "[variables('apiVersion')]",
      "location": "[variables('location')]",
      "properties": {
        "accountType": "[parameters('storageAccountType')]"
      }
    }
  ],
  "outputs": {
    "storageAccountName": {
      "type": "string",
      "value": "[variables('storageAccountName')]"
    }
  }
}
"""

deployment = azure.core.TemplateDeployment('myStorageDeployment',
    resource_group_name=resource_group.name,
    template_body=template,
    parameters={
        'storageAccountType': 'Standard_GRS',
    },
    deployment_mode='Incremental',
)

pulumi.export('storage_account_name', deployment.outputs["storageAccountName"])
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
    "github.com/pulumi/pulumi-azure/sdk/go/azure/core"
    "github.com/pulumi/pulumi/sdk/go/pulumi"
)

const (
    template = `{
  "$schema": "https://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#",
  "contentVersion": "1.0.0.0",
  "parameters": {
    "storageAccountType": {
      "type": "string",
      "defaultValue": "Standard_LRS",
      "allowedValues": [
        "Standard_LRS",
        "Standard_GRS",
        "Standard_ZRS"
      ],
      "metadata": {
        "description": "Storage Account type"
      }
    }
  },
  "variables": {
    "location": "[resourceGroup().location]",
    "storageAccountName": "[concat(uniquestring(resourceGroup().id), 'storage')]",
    "apiVersion": "2015-06-15"
  },
  "resources": [
    {
      "type": "Microsoft.Storage/storageAccounts",
      "name": "[variables('storageAccountName')]",
      "apiVersion": "[variables('apiVersion')]",
      "location": "[variables('location')]",
      "properties": {
        "accountType": "[parameters('storageAccountType')]"
      }
    }
  ],
  "outputs": {
    "storageAccountName": {
      "type": "string",
      "value": "[variables('storageAccountName')]"
    }
  }
}
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        resourceGroup, err := core.NewResourceGroup(ctx, "myRG", nil)
        if err != nil {
            return err
        }

        deployment, err := core.NewTemplateDeployment(ctx, "myStorageDeployment", &core.TemplateDeploymentArgs{
            ResourceGroupName: resourceGroup.Name,
            TemplateBody: pulumi.String(template),
            Parameters: pulumi.Map{
                "storageAccountType": pulumi.String("Standard_GRS"),
            },
            DeploymentMode: pulumi.String("Incremental"),
        })
        if err != nil {
            return err
        }

        ctx.Export("storageAccountName", network.Outputs.MapIndex(pulumi.String("storageAccountName")))
        return nil
    })
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using System.Threading.Tasks;

using Pulumi;

class Program
{
    static Task<int> Main()
    {
        return Deployment.RunAsync(() => {
            var template = @""{
  ""$schema"": ""https://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#"",
  ""contentVersion"": ""1.0.0.0"",
  ""parameters"": {
    ""storageAccountType"": {
      ""type"": ""string"",
      ""defaultValue"": ""Standard_LRS"",
      ""allowedValues"": [
        ""Standard_LRS"",
        ""Standard_GRS"",
        ""Standard_ZRS""
      ],
      ""metadata"": {
        ""description"": ""Storage Account type""
      }
    }
  },
  ""variables"": {
    ""location"": ""[resourceGroup().location]"",
    ""storageAccountName"": ""[concat(uniquestring(resourceGroup().id), 'storage')]"",
    ""apiVersion"": ""2015-06-15""
  },
  ""resources"": [
    {
      ""type"": ""Microsoft.Storage/storageAccounts"",
      ""name"": ""[variables('storageAccountName')]"",
      ""apiVersion"": ""[variables('apiVersion')]"",
      ""location"": ""[variables('location')]"",
      ""properties"": {
        ""accountType"": ""[parameters('storageAccountType')]""
      }
    }
  ],
  ""outputs"": {
    ""storageAccountName"": {
      ""type"": ""string"",
      ""value"": ""[variables('storageAccountName')]""
    }
  }
}"";

            var resourceGroup = new Core.ResourceGroup("myRG")

            var deployent = new Core.TemplateDeployment("myStorageDeployment", new Core.TemplateDeploymentArgs
            {
                ResourceGroupName = resourceGroup.Name,
                TemplateBody = template,
                Parameters = new Dictionary<string, object?>
                {
                    { "storageAccountType", "Standard_GRS" },
                },
                DeploymentMode = "Incremental",
            })

            return new Dictionary<string, object?>
            {
                { "storageAccountName", network.Outputs.Apply(nw => nw["storageAccountName"]) },
            };
        });
    }
}
```

{{% /choosable %}}

{{< /chooser >}}

> We could have just as well read the template off disk, instead of putting it right in the source code.

Notice here that Pulumi is actually deploying the resource group itself which the ARM template deployment then uses, since the deployment itself needs its own resource group. This demonstrates the ability to mix resources in the same Pulumi program. We could have used an existing ID instead if we wanted.

After deploying this, Pulumi will see the ARM deployment as an opaque single resource. That is, it won't assume control of individual resources inside of the stack. For that, you will need to migrate and/or import individual resources, per the following section:

```bash
$ pulumi up
Updating (dev):
     Type                              Name                 Status
 +   pulumi:pulumi:Stack               arm-tmpl-dev         created
 +   ├─ azure:core:ResourceGroup       myRG                 created
 +   └─ azure:core:TemplateDeployment  myStorageDeployment  created

Outputs:
    storageAccountName: "e9ejbnipspvecstorage"

Resources:
 + 3 created
```

From here, you can change the template body and/or surrounding code, rerun `pulumi up`, and the right incremental changes will take place.

### Migrate Resources into Code

Now let's see how to actually migrate your ARM-managed resources fully to Pulumi. This requires rewriting the ARM template JSON as real code, either entirely, or one resource at a time. Because you can query deployment outputs and provide parameters in code, you can more easily intermingle ARM-managed resources alongside Pulumi ones. Cyclic dependencies, of course, cannot be expressed, since the entire ARM deployment is seen as one opaque resource to Pulumi.

> Because Pulumi's Azure resource model doesn't match ARM's resource projections exactly, there is no tool currently available to automate this translation. A good apraoch is to copy the ARM template definition into your code and then rewrite it to your language of choice, translating resource and property names as appropriate.

Note that you can always skip the intermediate step of deploying your ARM template using Pulumi and go straight to migrating your resources. For deployments with many resources, however, doing this in multiple incremental steps can help minimize disruption and allow you to do this migration more slowly over time.

Our example below will result in a Pulumi program that creates a Storage Account equivalent to the above ARM template example. The example will also use [import]({{< relref "import" >}}) to adopt resources on-the-fly from ARM deployments to Pulumi rather than recreating them.

> This requires that we are using ARM's "incremental" deployment mode. This is the default mode, however, if you've specified that your ARM deployment should use "complete" mode, the import flow below will be complicated because ARM prefers to delete any resources it doesn't recognize as belonging to the template. [Read more about ARM deployment modes here](https://docs.microsoft.com/en-us/azure/azure-resource-manager/templates/deployment-modes).

To adopt the ARM resources under Pulumi's control, we will rewrite the ARM template in code, and use `import` IDs. For this example, recall that our Storage Account name was `"e9ejbnipspvecstorage"`. Also, in this example, there is just one resource, so we can simply delete the ARM template and deployment in its entirety and replace it with a Pulumi definition of the Storage Account. In cases where multiple resources exist, you can delete them one by one, until the ARM deployment is eventually empty.

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
let azure = require("@pulumi/azure");

let resourceGroup = new azure.core.ResourceGroup("myRG");

let storageAccount = new azure.storage.Account("myStorageAccount", {
    resourceGroupName: resourceGroup.name,
    name: "e9ejbnipspvecstorage",
    accountTier: "Standard",
    accountReplicationType: "GRS",
}, { import: "/subscriptions/0292631f-7a9b-4142-90b2-96badd5eafa8/resourceGroups/myrg8fd69ec2/providers/Microsoft.Storage/storageAccounts/e9ejbnipspvecstorage" });

module.exports = {
    storageAccountName: storageAccount.name,
};
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as azure from "@pulumi/azure";

const resourceGroup = new azure.core.ResourceGroup("myRG");

const storageAccount = new azure.storage.Account("myStorageAccount", {
    resourceGroupName: resourceGroup.name,
    name: "e9ejbnipspvecstorage",
    accountTier: "Standard",
    accountReplicationType: "GRS",
}, { import: "/subscriptions/0292631f-7a9b-4142-90b2-96badd5eafa8/resourceGroups/myrg8fd69ec2/providers/Microsoft.Storage/storageAccounts/e9ejbnipspvecstorage" });

export const storageAccountName = storageAccount.name;
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
import pulumi_azure as azure

resource_group = azure.core.ResourceGroup('myRG')

storage_account = azure.storage.Account('myStorageAccount'
    resource_group_name=resource_group.name,
    name='e9ejbnipspvecstorage',
    accountTier: 'Standard',
    accountReplicationType: 'GRS',
    opts=ResourceOptions(import_='/subscriptions/0292631f-7a9b-4142-90b2-96badd5eafa8/resourceGroups/myrg8fd69ec2/providers/Microsoft.Storage/storageAccounts/e9ejbnipspvecstorage')
)

pulumi.export('storage_account_name', storage_account.name)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
    "github.com/pulumi/pulumi-azure/sdk/go/azure/core"
    "github.com/pulumi/pulumi-azure/sdk/go/azure/storage"
    "github.com/pulumi/pulumi/sdk/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        resourceGroup, err := core.NewResourceGroup(ctx, "myRG", nil)
        if err != nil {
            return err
        }

        storageAccount, err := storage.NewAccount(ctx, "myStorageAccount",
            &storage.AccountArgs{
                ResourceGroupName: resourceGroup.Name,
                Name: pulumi.String("e9ejbnipspvecstorage"),
                AccountTier: pulumi.String("Standard"),
                AccountReplicationType: pulumi.String("GRS"),
            },
            pulumi.Import(pulumi.ID("/subscriptions/0292631f-7a9b-4142-90b2-96badd5eafa8/resourceGroups/myrg8fd69ec2/providers/Microsoft.Storage/storageAccounts/e9ejbnipspvecstorage")),
        })
        if err != nil {
            return err
        }

        ctx.Export("storageAccountName", storageAccount.Name)
        return nil
    })
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using System.Threading.Tasks;

using Pulumi;
using Core = Pulumi.Azure.Core;
using Storage = Pulumi.Azure.Storage;

class Program
{
    static Task<int> Main()
    {
        return Deployment.RunAsync(() => {
            var resourceGroup = new Core.ResourceGroup("myRG");

            var storageAccount = new Storage.Account("myStorageAccount",
                new Storage.AccountArgs
                {
                    ResourceGroupName = resourceGroup.Name,
                    Name = "e9ejbnipspvecstorage",
                    AccountTier = "Standard",
                    AccountReplicationType = "GRS",
                },
                new CustomResourceOptions {
                    ImportId = "/subscriptions/0292631f-7a9b-4142-90b2-96badd5eafa8/resourceGroups/myrg8fd69ec2/providers/Microsoft.Storage/storageAccounts/e9ejbnipspvecstorage",
                },
            );

            return new Dictionary<string, object?>
            {
                { "storageAccountName", storageAccount.Name },
            };
        });
    }
}
```

{{% /choosable %}}

{{< /chooser >}}

> Notice here that we've used the fully qualified resource ID for the import, `"/subscriptions/0292631f-7a9b-4142-90b2-96badd5eafa8/resourceGroups/myrg8fd69ec2/providers/Microsoft.Storage/storageAccounts/e9ejbnipspvecstorage"`. If you're having trouble locating this, please consult the Azure CLI or console.

After running `pulumi up`, your storage account will become under the control of Pulumi without any disruption, and you can then delete the import directives from your code. All subsequent infrastructure changes you'd like to be made can happen within Pulumi instead of ARM template deployments.

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

* [**Coexist**](#referencing-stack-outputs) with resources provisioned by ARM by referencing deployment outputs.
* [**Import**]({{< relref "import" >}}) existing resources into Pulumi in the usual way.
* [**Convert**](#converting-stacks-and-resources) your deployments to use Pulumi and then incrementally migrate resources.

## Referencing Stack Outputs

It is possible to reference existing Azure Resource Manager (ARM) template deployments from your program. It doesn't mattter how these templates and deployments were created. This lets you read properties of a deployment for use within your Pulumi program. This includes output values computed from resources provisioned that stack.

For instance, let's say your infrastructure team has provisioned your Azure storage account using ARM and you need to use the Storage Account name to provision something new from your Pulumi program. One approach is to hardcode the name but this is brittle and, if it ever changes, you'd need to go and manually update the hardcoded value.

Instead, you can look up that ARM deployment by name and use one of its output values. The following example reads a deployment by its fully qualified ID and then uses the exported `storageAccountName` value to upload a private zipfile to blob storage, containing a `wwwroot/` directory locally:

{{< chooser language "typescript,python,go,csharp" >}}

{{% choosable language typescript %}}

```typescript
import * as resources from "@pulumi/azure-native/resources";
import * as storage from "@pulumi/azure-native/storage";
import * as pulumi from "@pulumi/pulumi";

// Read the deployment and the storage account name.
const deployment = resources.Deployment.get("myStorageDeployment",
    "/subscriptions/0292631f-7a9b-4142-90b2-96badd5eafa8/resourceGroups/myrg/providers/Microsoft.Resources/deployments/myStorageDeployment62ba53a3");
const storageAccountName = deployment.properties.outputs["storageAccountName"].value;

// Create a blob for our own deployment.
const blob = new storage.Blob("zip", {
    resourceGroupName: "myrg",
    accountName: storageAccountName,
    containerName: new storage.BlobContainer("myStorageContainer", {
        resourceGroupName: "myrg",
        accountName: storageAccountName,
        containerName: "files",
    }).name,
    source: new pulumi.asset.FileArchive("wwwroot"),
});

export const blobUrl = blob.url;
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
from pulumi_azure_native import storage
from pulumi_azure_native import resources

# Read the deployment and the storage account name.
deployment = resources.Deployment.get('myStorageDeployment',
    '/subscriptions/0292631f-7a9b-4142-90b2-96badd5eafa8/resourceGroups/myrg/providers/Microsoft.Resources/deployments/myStorageDeployment62ba53a3')
storage_account_name = deployment.properties.outputs['storageAccountName'].value

# Create a blob for our own deployment.
blob = storage.Blob('zip',
    resource_group_name='myrg',
    account_name=storage_account_name,
    container_name=storage.BlobContainer('myStorageContainer',
        resource_group_name='myrg',
        account_name=storage_account_name,
        container_name='files'
    ).name,
    source=pulumi.asset.FileArchive('wwwroot'),
)

pulumi.export('blob_url', blob.url)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
    resources "github.com/pulumi/pulumi-azure-native/sdk/go/azure/resources"
	  storage "github.com/pulumi/pulumi-azure-native/sdk/go/azure/storage"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        // Read the deployment and the storage account name.
        deployment, err := resources.GetDeployment(ctx, "myStorageDeployment",
            "/subscriptions/0292631f-7a9b-4142-90b2-96badd5eafa8/resourceGroups/myrg/providers/Microsoft.Resources/deployments/myStorageDeployment62ba53a3",
            nil)
        if err != nil {
            return nil
        }
        storageAccountName := deployment.Properties.Outputs["storageAccountName"].Value.(string)

        // Create a blob for our own deployment.
        cont, err := storage.NewBlobContainer(ctx, "myStorageContainer", &storage.BlobContainerArgs{
            ResourceGroupName: pulumi.String("myrg"),
            AccountName: pulumi.String(storageAccountName),
            ContainerName: pulumi.String("files"),
        })
        if err != nil {
            return err
        }
        blob, err := storage.NewBlob(ctx, "zip", &storage.BlobArgs{
            ResourceGroupName: pulumi.String("myrg"),
            AccountName: pulumi.String(storageAccountName),
            ContainerName: cont.Name,
            Source: pulumi.NewFileArchive("wwwroot"),
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
using Pulumi;

using Pulumi.AzureNative.Storage;
using TemplateDeployment = Pulumi.AzureNative.Resources.Deployment;

class MyStack : Stack
{
    public MyStack()
    {
        // Read the deployment and the storage account name.
        var deployment = TemplateDeployment.Get("myStorageDeployment",
            "/subscriptions/0292631f-7a9b-4142-90b2-96badd5eafa8/resourceGroups/myrg/providers/Microsoft.Resources/deployments/myStorageDeployment62ba53a3");
        var storageAccountName = deployment.Properties
            .Apply(v => ((IDictionary<string, object>)v.Outputs)["storageAccountName"])
            .Apply(v => (string)((IDictionary<string, object>)v)["value"]);

        // Create a blob for our own deployment.
        var blob = new Blob("zip", new BlobArgs
        {
            ResourceGroupName = "myrg",
            AccountName = storageAccountName,
            ContainerName = new BlobContainer("myStorageContainer", new BlobContainerArgs
            {
                ResourceGroupName = "myrg",
                AccountName = storageAccountName,
                ContainerName = "files",
            }).Name,
            Source = new FileArchive("wwwroot"),
        });

        this.BlobUrl = blob.Url;
    }

    [Output] public Output<string> BlobUrl { get; set; }
}

```

{{% /choosable %}}

{{< /chooser >}}

All we need to do is run `pulumi up` and the Pulumi runtime will know how to query the ARM deployment to retrieve its output values. In this case, the deployment and all of its resources are treated entirely as read-only, and Pulumi will never attempt to modify any of them.

Notice that the ID is of the format: `/subscriptions/<YOUR-SUBSCRIPTION-ID>/resourceGroups/<DEPLOYMENT-RG-NAME>/providers/Microsoft.Resources/deployments/<DEPLOYMENT-NAME>`. Consult the Azure CLI or portal to find this ID.

> Although we've hard-coded the ARM deployment ID here, it's common to dynamically compute a name using unique per-stack information, like the stack name, subscription ID, or other configuration variables.

## Converting Stacks and Resources

Let's say you want to migrate from ARM to Pulumi and that simply co-existing side-by-side as shown above isn't sufficient.

Let's see how to actually migrate your ARM-managed resources fully to Pulumi. This requires rewriting the ARM template JSON as your favorite programming language code, either entirely, or one resource at a time. Because you can query deployment outputs and provide parameters in code, you can more easily intermingle ARM-managed resources alongside Pulumi ones. Cyclic dependencies, of course, cannot be expressed, since the entire ARM deployment is seen as one opaque resource to Pulumi.

Our example below will result in a Pulumi program that creates a Storage Account equivalent to the above ARM template example. The example will also use [import]({{< relref "import" >}}) to adopt resources on-the-fly from ARM deployments to Pulumi rather than recreating them.

### Generate Code with Arm2Pulumi

With the Next Generation Pulumi Azure Provider, it's possible to convert ARM templates into Pulumi program code using [arm2pulumi]({{< relref "/arm2pulumi" >}}). Simply provide your ARM template
and get back a Pulumi program in C#, TypeScript, Python, Go, Java, or YAML.

Let's say you have an existing ARM Template shown below.

```json
{
    "$schema": "http://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#",
    "contentVersion": "1.0.0.0",
    "resources": [
        {
            "type": "Microsoft.Storage/storageAccounts",
            "apiVersion": "2019-06-01",
            "name": "storagecreatedbyarm",
            "location": "westeurope",
            "sku": {
                "name": "Standard_LRS"
            },
            "kind": "StorageV2"
        }
    ]
}
```

Navigate to the [`arm2pulumi`](https://www.pulumi.com/arm2pulumi/) page, select the Custom tab, paste your template to the editor, select the desired language, and click the Convert button. You will receive the Pulumi program that is equivalent to the ARM template.

{{< chooser language "typescript,python,go,csharp" >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as azure_native from "@pulumi/azure-native";

const config = new pulumi.Config();
const resourceGroupNameParam = config.require("resourceGroupNameParam");
const storagecreatedbyarm = new azure_native.storage.StorageAccount("storagecreatedbyarm", {
    accountName: "storagecreatedbyarm",
    kind: "StorageV2",
    location: "westeurope",
    resourceGroupName: resourceGroupNameParam,
    sku: {
        name: "Standard_LRS",
    },
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
import pulumi_azure_native as azure_native

config = pulumi.Config()
resource_group_name_param = config.require("resourceGroupNameParam")
storagecreatedbyarm = azure_native.storage.StorageAccount("storagecreatedbyarm",
    account_name="storagecreatedbyarm",
    kind="StorageV2",
    location="westeurope",
    resource_group_name=resource_group_name_param,
    sku=azure_native.storage.SkuArgs(
        name="Standard_LRS",
    ))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-azure-native/sdk/go/azure/storage"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		cfg := config.New(ctx, "")
		resourceGroupNameParam := cfg.Require("resourceGroupNameParam")
		_, err := storage.NewStorageAccount(ctx, "storagecreatedbyarm", &storage.StorageAccountArgs{
			AccountName:       pulumi.String("storagecreatedbyarm"),
			Kind:              pulumi.String("StorageV2"),
			Location:          pulumi.String("westeurope"),
			ResourceGroupName: pulumi.String(resourceGroupNameParam),
			Sku: &storage.SkuArgs{
				Name: pulumi.String("Standard_LRS"),
			},
		})
		if err != nil {
			return err
		}
		return nil
	})
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using Pulumi;
using AzureNative = Pulumi.AzureNative;

class MyStack : Stack
{
    public MyStack()
    {
        var config = new Config();
        var resourceGroupNameParam = config.Require("resourceGroupNameParam");
        var storagecreatedbyarm = new AzureNative.Storage.StorageAccount("storagecreatedbyarm", new AzureNative.Storage.StorageAccountArgs
        {
            AccountName = "storagecreatedbyarm",
            Kind = "StorageV2",
            Location = "westeurope",
            ResourceGroupName = resourceGroupNameParam,
            Sku = new AzureNative.Storage.Inputs.SkuArgs
            {
                Name = "Standard_LRS",
            },
        });
    }
}
```

{{% /choosable %}}

{{< /chooser >}}

Next, we will adjust the code to adopt the existing resource instead of creating a new one.

### Import The Resource

To adopt the ARM resources under Pulumi's control, we will rewrite the code generated by the tool, and use the `import` ID. For this example, recall that our Storage Account name was `"storagecreatedbyarm"`.

Create a new Pulumi project, if you don't have one yet, and copy-paste the program from the `arm2pulumi` window. Adjust the code to specify the `import` ID for the storage account.

{{< chooser language "typescript,python,go,csharp" >}}

{{% choosable language typescript %}}

```typescript
import * as azure_native from "@pulumi/azure-native";

const storagecreatedbyarm = new azure_native.storage.StorageAccount("storagecreatedbyarm", {
    accountName: "storagecreatedbyarm",
    kind: "StorageV2",
    location: "westeurope",
    resourceGroupName: "existing-rg",
    sku: {
        name: "Standard_LRS",
    },
}, { import: "/subscriptions/0292631f-7a9b-4142-90b2-96badd5eafa8/resourceGroups/existing-rg/providers/Microsoft.Storage/storageAccounts/storagecreatedbyarm" });
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
import pulumi_azure_native as azure_native

config = pulumi.Config()
resource_group_name_param = config.require("resourceGroupNameParam")
storagecreatedbyarm = azure_native.storage.StorageAccount("storagecreatedbyarm",
    account_name="storagecreatedbyarm",
    kind="StorageV2",
    location="westeurope",
    resource_group_name=resource_group_name_param,
    sku=azure_native.storage.SkuArgs(
        name="Standard_LRS",
    ),
    opts=ResourceOptions(import_='/subscriptions/0292631f-7a9b-4142-90b2-96badd5eafa8/resourceGroups/existing-rg/providers/Microsoft.Storage/storageAccounts/storagecreatedbyarm')
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-azure-native/sdk/go/azure/storage"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		cfg := config.New(ctx, "")
		resourceGroupNameParam := cfg.Require("resourceGroupNameParam")
		_, err := storage.NewStorageAccount(ctx, "storagecreatedbyarm", &storage.StorageAccountArgs{
			AccountName:       pulumi.String("storagecreatedbyarm"),
			Kind:              pulumi.String("StorageV2"),
			Location:          pulumi.String("westeurope"),
			ResourceGroupName: pulumi.String(resourceGroupNameParam),
			Sku: &storage.SkuArgs{
				Name: pulumi.String("Standard_LRS"),
			},
		},
    pulumi.Import(pulumi.ID("/subscriptions/0292631f-7a9b-4142-90b2-96badd5eafa8/resourceGroups/existing-rg/providers/Microsoft.Storage/storageAccounts/storagecreatedbyarm")))
		if err != nil {
			return err
		}
		return nil
	})
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using Pulumi;
using AzureNative = Pulumi.AzureNative;

class MyStack : Stack
{
    public MyStack()
    {
        var config = new Config();
        var resourceGroupNameParam = config.Require("resourceGroupNameParam");
        var storagecreatedbyarm = new AzureNative.Storage.StorageAccount("storagecreatedbyarm", new AzureNative.Storage.StorageAccountArgs
        {
            AccountName = "storagecreatedbyarm",
            Kind = "StorageV2",
            Location = "westeurope",
            ResourceGroupName = resourceGroupNameParam,
            Sku = new AzureNative.Storage.Inputs.SkuArgs
            {
                Name = "Standard_LRS",
            },
        },
        new CustomResourceOptions {
            ImportId = "/subscriptions/0292631f-7a9b-4142-90b2-96badd5eafa8/resourceGroups/existing-rg/providers/Microsoft.Storage/storageAccounts/storagecreatedbyarm",
        });
    }
}
```

{{% /choosable %}}

{{< /chooser >}}

> Notice here that we've used the fully qualified resource ID for the import, `"/subscriptions/0292631f-7a9b-4142-90b2-96badd5eafa8/resourceGroups/existing-rg/providers/Microsoft.Storage/storageAccounts/storagecreatedbyarm"`. If you're having trouble locating this, consult the Azure CLI or the Azure portal.

While running `pulumi up` with the code above, you will likely see a warning

```
  Type                                     Name                 Plan   Info
  pulumi:pulumi:Stack                      proj-dev
 =└─ azure-native:storage:StorageAccount  storagecreatedbyarm  import [diff: -accessTier,enableHttpsTrafficOnly,encryption,networkRuleSet

Diagnostics:
  azure-native:storage:StorageAccount (storagecreatedbyarm):
    warning: inputs to import do not match the existing resource; importing this resource will fail
```

This is because the import operation requires explicit definitions for all properties that may have been auto-populated by Azure during the resource creation. You can supress the warning by setting the [`ignoreChanges`](https://pulumi.com/docs/intro/concepts/resources/#ignorechanges) option to `["accessTier","enableHttpsTrafficOnly","encryption","networkRuleSet"]`.

After running `pulumi up` again, your storage account will become under the control of Pulumi without any disruption. All subsequent infrastructure changes you'd like to be made can happen within Pulumi instead of ARM template deployments.

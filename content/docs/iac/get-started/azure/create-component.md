---
title_tag: Create a component | Azure
title: Create a component
h1: "Get started with Pulumi and Azure"
meta_desc: This page provides an overview on how to create infrastructure abstractions with Pulumi.
weight: 7
menu:
    iac:
        name: Create a component
        identifier: azure-get-started.create-component
        parent: azure-get-started
        weight: 7

aliases:
    - /docs/quickstart/azure/create-component/
    - /docs/clouds/azure/get-started/create-component/
---

## Create a component

[**Components**](/docs/iac/concepts/resources/components/) are infrastructure abstractions that encapsulate
complexity and enable sharing and reuse. Instead of copy-pasting common patterns, you can encode them as components.

You will now create your first component that packages up your Azure static website so you can easily stamp out
entire websites in just a few lines of code:

{{% choosable language typescript %}}

```typescript
const website = new AzureStaticWebsite("my-website", {
    files: [ "index.html" ],
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
website = AzureStaticWebsite('my-website', files=['index.html'])
```

{{% /choosable %}}

{{% choosable language go %}}

```go
website, err := NewAzureStaticWebsite(ctx, "my-website", AzureStaticWebsiteArgs{
    Files: []string{"index.html"},
})
if err != nil {
    return err
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
var website = new AzureStaticWebsite("my-website", new AzureStaticWebsiteArgs()
{
    Files = new[] { "index.html" }
});
```

{{% /choosable %}}

{{% choosable language java %}}

```java
var website = new AzureStaticWebsite("my-website",
    new AzureStaticWebsiteArgs(new String[] { "index.html" }));
```

{{% /choosable %}}

{{% choosable language yaml %}}

{{% notes type="warning" %}}

Unfortunately, YAML lacks the language facilities to author components. Feel free to [skip ahead](/docs/iac/get-started/azure/destroy-stack/).

{{% /notes %}}

{{% /choosable %}}

Using components here also has the benefit that, as the requirements for Azure static websites changes, you can
update the one component definition and have all uses of it benefit.

### Define a new component

To define a new component, create a class called `AzureStaticWebsite` that derives from `ComponentResource`. It'll have a mostly-empty
constructor to start with but you will add the Azure resources to it in the next step. You'll also define the inputs for the
component -- the `files` to add to the website -- and outputs -- a single property with the website `url`.

To get going, create a new file {{< compfile >}} alongside {{< langfile >}} and add the following:

{{% choosable language typescript %}}

```typescript
import * as azure from "@pulumi/azure-native";
import * as pulumi from "@pulumi/pulumi";

// Arguments for the Azure hosted static website component.
export interface AzureStaticWebsiteArgs {
    files: string[]; // a list of files to serve.
}

// A component that encapsulates creating an Azure hosted static website.
export class AzureStaticWebsite extends pulumi.ComponentResource {
    public readonly url: pulumi.Output<string>; // the website url.

    constructor(name: string, args: AzureStaticWebsiteArgs, opts?: pulumi.ComponentResourceOptions) {
        super("quickstart:index:AzureStaticWebsite", name, args, opts);

        // Component initialization will go here next...

        this.registerOutputs({}); // Signal component completion.
    }
}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
from pulumi_azure_native import storage, resources
from typing import List

# A component that encapsulates creating an Azure hosted static website.
class AzureStaticWebsite(pulumi.ComponentResource):
    def __init__(self, name: str, files: List[str] = None, opts = None):
        super().__init__('quickstart:index:AzureStaticWebsite', name, { 'files': files }, opts)

        # Component initialization will go here next...

        self.register_outputs({}) # Signal component completion.
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

type AzureStaticWebsite struct {
    pulumi.ResourceState
    Url pulumi.StringOutput // the website url.
}

type AzureStaticWebsiteArgs struct {
    Files []string // a list of files to serve.
}

func NewAzureStaticWebsite(ctx *pulumi.Context, name string, args AzureStaticWebsiteArgs, opts ...pulumi.ResourceOption) (*AzureStaticWebsite, error) {
    self := &AzureStaticWebsite{}
    err := ctx.RegisterComponentResource("quickstart:index:AzureStaticWebsite", name, self, opts...)
    if err != nil {
        return nil, err
    }

    // Component initialization will go here next...

    ctx.RegisterResourceOutputs(self, pulumi.Map{}) // Signal component completion.
    return self, nil
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

public class AzureStaticWebsiteArgs
{
    public string[]? Files { get; set; }
}

public class AzureStaticWebsite : Pulumi.ComponentResource
{
    public Output<string> Url { get; private set; }

    public AzureStaticWebsite(string name, AzureStaticWebsiteArgs args, ComponentResourceOptions? opts = null)
        : base("quickstart:index:AzureStaticWebsite", name, opts)
    {
        // Component initialization will go here next...

        this.RegisterOutputs(new Dictionary<string, object>{}); // Signal component completion.
    }
}
```

{{% /choosable %}}

{{% choosable language java %}}

```java
package myproject;

import com.pulumi.Pulumi;
import com.pulumi.azurenative.resources.ResourceGroup;
import com.pulumi.azurenative.storage.StorageAccount;
import com.pulumi.resources.ComponentResource;
import com.pulumi.resources.ComponentResourceOptions;

public class AzureStaticWebsiteArgs {
    public String[] files;
    public AzureStaticWebsiteArgs(String[] files) {
        this.files = files;
    }
}

public class AzureStaticWebsite extends ComponentResource {
    public Output<String> url;

    public AzureStaticWebsite(String name, AzureStaticWebsiteArgs args, ComponentResourceOptions opts) {
        super("quickstart:index:AzureStaticWebsite", name, args, opts);

        // Component initialization will go here next...

        this.registerOutputs(Map.of());
    }
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

{{% notes type="warning" %}}

Unfortunately, YAML lacks the language facilities to author components. Feel free to [skip ahead](/docs/iac/get-started/azure/destroy-stack/).

{{% /notes %}}

{{% /choosable %}}

This defines a component but it doesn't do much yet.

### Refactor your code into the component

Next, make four changes:

1. Move all resources from {{< langfile >}} into the component's constructor
1. Change each resource to use the component [as the `parent`](/docs/iac/concepts/options/parent/)
1. Generalize the creation of blobs by looping over the list of `files`
1. Assign the resulting website URL to the `url` property of the component

The resulting {{< compfile >}} file will look like this; you can make each edit one at a time if preferred
to get a feel for things, or simply paste the contents of this into {{< compfile >}}:

{{% choosable language typescript %}}

```typescript
import * as azure from "@pulumi/azure-native";
import * as pulumi from "@pulumi/pulumi";

// Arguments for the Azure hosted static website component.
export interface AzureStaticWebsiteArgs {
    files: string[]; // a list of files to serve.
}

// A component that encapsulates creating an Azure hosted static website.
export class AzureStaticWebsite extends pulumi.ComponentResource {
    public readonly url: pulumi.Output<string>; // the website url.

    constructor(name: string, args: AzureStaticWebsiteArgs, opts?: pulumi.ComponentResourceOptions) {
        super("quickstart:index:AzureStaticWebsite", name, args, opts);

        // Create a resource group
        const resourceGroup = new azure.resources.ResourceGroup("my-group", {}, {
            // Set the parent to the component (step #2) above.
            // Also, do the same for all other resources below.
            parent: this,
        });

        // Create a storage account
        const storageAccount = new azure.storage.StorageAccount("myaccount", {
            resourceGroupName: resourceGroup.name,
            kind: azure.storage.Kind.StorageV2,
            sku: {
                name: azure.storage.SkuName.Standard_LRS,
            },
        }, { parent: this });

        // Enable static website support
        const staticWebsite = new azure.storage.StorageAccountStaticWebsite("static-website", {
            accountName: storageAccount.name,
            resourceGroupName: resourceGroup.name,
            indexDocument: "index.html",
        }, { parent: this });

        // Upload each file as a blob:
        for (const file of args.files) {
            new azure.storage.Blob(file, {
                accountName: storageAccount.name,
                containerName: staticWebsite.containerName,
                resourceGroupName: resourceGroup.name,
                source: new pulumi.asset.FileAsset(file),
                contentType: "text/html",
            }, { parent: this });
        }

        // Capture the URL and make it available as a component property and output:
        this.url = storageAccount.primaryEndpoints.apply(pe => pe.web);
        this.registerOutputs({ url: this.url }); // Signal component completion.
    }
}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
from pulumi_azure_native import storage, resources
from typing import List

# A component that encapsulates creating an Azure hosted static website.
class AzureStaticWebsite(pulumi.ComponentResource):
    def __init__(self, name: str, files: List[str] = None, opts = None):
        super().__init__('quickstart:index:AzureStaticWebsite', name, { 'files': files }, opts)

        # Create a resource group
        resource_group = resources.ResourceGroup('my-group',
            # Set the parent to the component (step #2) above.
            # Also, do the same for all other resources below.
            opts=pulumi.ResourceOptions(parent=self),
        )

        # Create a storage account
        storage_account = storage.StorageAccount('myaccount',
            resource_group_name=resource_group.name,
            kind=storage.Kind.STORAGE_V2,
            sku={
                'name': storage.SkuName.STANDARD_LRS,
            },
            opts=pulumi.ResourceOptions(parent=self),
        )

        # Enable static website support
        static_website = storage.StorageAccountStaticWebsite('static-website',
            account_name=storage_account.name,
            resource_group_name=resource_group.name,
            index_document='index.html',
            opts=pulumi.ResourceOptions(parent=self),
        )

        # Upload each file as a blob:
        for file in files:
            storage.Blob(
                file,
                account_name=storage_account.name,
                container_name=static_website.container_name,
                resource_group_name=resource_group.name,
                source=pulumi.FileAsset(file),
                content_type='text/html',
                opts=pulumi.ResourceOptions(parent=self),
            )

        # Capture the URL and make it available as a component property and output:
        self.url = storage_account.primary_endpoints.apply(lambda pe: pe.web)
        self.register_outputs({ 'url': self.url }) # Signal component completion.
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

type AzureStaticWebsite struct {
	pulumi.ResourceState
	Url pulumi.StringOutput // the website url.
}

type AzureStaticWebsiteArgs struct {
	Files []string // a list of files to serve.
}

func NewAzureStaticWebsite(ctx *pulumi.Context, name string, args AzureStaticWebsiteArgs, opts ...pulumi.ResourceOption) (*AzureStaticWebsite, error) {
	self := &AzureStaticWebsite{}
	err := ctx.RegisterComponentResource("quickstart:index:AzureStaticWebsite", name, self, opts...)
	if err != nil {
		return nil, err
	}

	// Create a resource group
	resourceGroup, err := resources.NewResourceGroup(ctx, "my-group", nil,
		// Set the parent to the component (step #2) above.
		// Also, do the same for all other resources below.
		pulumi.Parent(self))
	if err != nil {
		return nil, err
	}

	// Create a storage account
	storageAccount, err := storage.NewStorageAccount(ctx, "myaccount", &storage.StorageAccountArgs{
		ResourceGroupName: resourceGroup.Name,
		Kind:              pulumi.String("StorageV2"),
		Sku: &storage.SkuArgs{
			Name: pulumi.String("Standard_LRS"),
		},
	}, pulumi.Parent(self))
	if err != nil {
		return nil, err
	}

	// Enable static website support
	staticWebsite, err := storage.NewStorageAccountStaticWebsite(ctx, "static-website", &storage.StorageAccountStaticWebsiteArgs{
		AccountName:       storageAccount.Name,
		ResourceGroupName: resourceGroup.Name,
		IndexDocument:     pulumi.String("index.html"),
	}, pulumi.Parent(self))
	if err != nil {
		return nil, err
	}

	// Upload each file as a blob:
	for _, file := range args.Files {
		_, err = storage.NewBlob(ctx, file, &storage.BlobArgs{
			AccountName:       storageAccount.Name,
			ContainerName:     staticWebsite.ContainerName,
			ResourceGroupName: resourceGroup.Name,
			Source:            pulumi.NewFileAsset(file),
			ContentType:       pulumi.String("text/html"),
		}, pulumi.Parent(self))
		if err != nil {
			return nil, err
		}
	}

	// Capture the URL and make it available as a component property and output:
	self.Url = storageAccount.PrimaryEndpoints.ApplyT(func(pe storage.EndpointsResponse) string {
		return *pe.Web
	}).(pulumi.StringOutput)

	ctx.RegisterResourceOutputs(self, pulumi.Map{"url": self.Url}) // Signal component completion.
	return self, nil
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

public class AzureStaticWebsiteArgs
{
    public string[]? Files { get; set; }
}

public class AzureStaticWebsite : Pulumi.ComponentResource
{
    public Output<string> Url { get; private set; }

    public AzureStaticWebsite(string name, AzureStaticWebsiteArgs args, ComponentResourceOptions? opts = null)
        : base("quickstart:index:AzureStaticWebsite", name, opts)
    {
        // Create a resource group
        var resourceGroup = new ResourceGroup("my-group", new(), new CustomResourceOptions
        {
            // Set the parent to the component (step #2) above.
            // Also, do the same for all other resources below.
            Parent = this,
        });

        // Create a storage account
        var storageAccount = new StorageAccount("myaccount", new()
        {
            ResourceGroupName = resourceGroup.Name,
            Kind = Kind.StorageV2,
            Sku = new SkuArgs
            {
                Name = SkuName.Standard_LRS,
            },
        }, new CustomResourceOptions
        {
            Parent = this,
        });

        // Enable static website support
        var staticWebsite = new StorageAccountStaticWebsite("static-website", new()
        {
            AccountName = storageAccount.Name,
            ResourceGroupName = resourceGroup.Name,
            IndexDocument = "index.html",
        }, new CustomResourceOptions
        {
            Parent = this,
        });

        // Upload each file as a blob:
        foreach (var file in args.Files ?? []) {
            new Blob(file, new()
            {
                AccountName = storageAccount.Name,
                ContainerName = staticWebsite.ContainerName,
                ResourceGroupName = resourceGroup.Name,
                Source = new FileAsset(file),
                ContentType = "text/html",
            }, new CustomResourceOptions
            {
                Parent = this,
            });
        }

        // Capture the URL and make it available as a component property and output:
        this.Url = storageAccount.PrimaryEndpoints.Apply(pe => pe.Web);
        this.RegisterOutputs(new Dictionary<string, object?>{
            ["url"] = this.Url
        });
    }
}
```

{{% /choosable %}}

{{% choosable language java %}}

```java
package myproject;

import com.pulumi.*;
import com.pulumi.core.*;
import com.pulumi.asset.FileAsset;
import com.pulumi.resources.*;

import com.pulumi.azurenative.resources.*;
import com.pulumi.azurenative.storage.*;
import com.pulumi.azurenative.storage.inputs.*;

import java.util.Map;

class AzureStaticWebsiteArgs extends ResourceArgs {
    public String[] files;
    public AzureStaticWebsiteArgs(String[] files) {
        this.files = files;
    }
}

class AzureStaticWebsite extends ComponentResource {
    public Output<String> url;

    public AzureStaticWebsite(String name, AzureStaticWebsiteArgs args) {
        this(name, args, null);
    }

    public AzureStaticWebsite(String name, AzureStaticWebsiteArgs args, ComponentResourceOptions opts) {
        super("quickstart:index:AzureStaticWebsite", name, args, opts);

        // Create a resource group
        var resourceGroup = new ResourceGroup("my-group", null,
            // Set the parent to the component (step #2) above.
            // Also, do the same for all other resources below.
            CustomResourceOptions.builder().parent(this).build());

        // Create a storage account
        var storageAccount = new StorageAccount("myaccount", StorageAccountArgs.builder()
            .resourceGroupName(resourceGroup.name())
            .kind("StorageV2")
            .sku(SkuArgs.builder()
                .name("Standard_LRS")
                .build())
            .build(), CustomResourceOptions.builder().parent(this).build());

        // Enable static website support
        var staticWebsite = new StorageAccountStaticWebsite("static-website", StorageAccountStaticWebsiteArgs.builder()
            .accountName(storageAccount.name())
            .resourceGroupName(resourceGroup.name())
            .indexDocument("index.html")
            .build(), CustomResourceOptions.builder().parent(this).build());

        // Upload each file as a blob:
        for (var file : args.files) {
            new Blob(file, BlobArgs.builder()
                .accountName(storageAccount.name())
                .containerName(staticWebsite.containerName())
                .resourceGroupName(resourceGroup.name())
                .source(new FileAsset(file))
                .contentType("text/html")
                .build(), CustomResourceOptions.builder()
                    .parent(this)
                    .build());
        }

        // Capture the URL and make it available as a component property and output:
        this.url = storageAccount.primaryEndpoints().applyValue(pe -> pe.web().get());
        this.registerOutputs(Map.of("url", this.url));
    }
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

{{% notes type="warning" %}}

Unfortunately, YAML lacks the language facilities to author components. Feel free to [skip ahead](/docs/iac/get-started/azure/destroy-stack/).

{{% /notes %}}

{{% /choosable %}}

### Instantiate the component

Now go back to your original file {{< langfile >}}. Now that you have moved all of the resources, you can start over with a clean slate.
Ensure the file is empty and we will build it back up by simply importing and instantiating our new component.

Add this to your now-empty {{< langfile >}}:

{{% choosable language typescript %}}

```typescript
// Import from our new component module:
import { AzureStaticWebsite } from "./website";

// Create an instance of our component with the same files as before:
const website = new AzureStaticWebsite("my-website", {
    files: [ "index.html" ],
});

// And export its autoassigned URL:
export const url = website.url;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi

# Import from our new component module:
from website import AzureStaticWebsite

# Create an instance of our component with the same files as before:
website = AzureStaticWebsite('my-website', files=['index.html'])

# And export its autoassigned URL:
pulumi.export("url", website.url)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        // Create an instance of our component with the same files as before:
        website, err := NewAzureStaticWebsite(ctx, "my-website", AzureStaticWebsiteArgs{
            Files: []string{"index.html"},
        })
        if err != nil {
            return err
        }

        // And export its autoassigned URL:
        ctx.Export("url", website.Url)
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
using System.Collections.Generic;

return await Pulumi.Deployment.RunAsync(() =>
{
    // Create an instance of our component with the same files as before:
    var website = new AzureStaticWebsite("my-website", new AzureStaticWebsiteArgs()
    {
        Files = new[] { "index.html" }
    });

   // And export its autoassigned URL:
   return new Dictionary<string, object?>
   {
      ["url"] = website.Url
   };
});
```

{{% /choosable %}}

{{% choosable language java %}}

```java
package myproject;

import com.pulumi.Pulumi;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            // Create an instance of our component with the same files as before:
            var website = new AzureStaticWebsite("my-website",
                new AzureStaticWebsiteArgs(new String[] { "index.html" }));

            // And export its autoassigned URL:
            ctx.export("url", website.url);
        });
    }
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

{{% notes type="warning" %}}

Unfortunately, YAML lacks the language facilities to author components. Feel free to [skip ahead](/docs/iac/get-started/azure/destroy-stack/).

{{% /notes %}}

{{% /choosable %}}

### Deploy the component

Now deploy the resulting component instantiation. To do so, run `pulumi up` as usual:

```
$ pulumi up
Previewing update (dev)

     Type                                            Name                 Plan
     pulumi:pulumi:Stack                             quickstart-dev
 +   ├─ quickstart:index:AzureStaticWebsite          my-site              create
 +   │  ├─ azure-native:resources:ResourceGroup      my-group             create
 +   │  ├─ azure-native:storage:StorageAccount       myaccount            create
 +   │  ├─ azure-native:storage:StorageAccountStaticWebsite  static-website   create
 +   │  └─ azure-native:storage:Blob                 index.html           create
 -   ├─ azure-native:storage:Blob                    index.html           delete
 -   ├─ azure-native:storage:StorageAccountStaticWebsite  static-website   delete
 -   ├─ azure-native:storage:StorageAccount          myaccount            delete
 -   └─ azure-native:resources:ResourceGroup         my-group             delete

Resources:
    + 5 to create
    - 4 to delete
    9 changes. 1 unchanged

Do you want to perform this update?  [Use arrows to move, type to filter]
  yes
> no
  details
```

This preview shows you a few things. First, you'll see our `AzureStaticWebsite` component with all of its children
resources neatly parented underneath it. This helps to see what resources relate to which components. Next,
you'll see that your old resources are being destroyed.

{{% notes type="info" %}}

If you're wondering why Pulumi didn't simply update the resources in place, it's because certain changes -- like
refactoring resources into a component -- fundamentally change a resource's identity. Many changes like updating
properties or moving resources between files are not disruptive like this. In such cases, you can assign
[aliases](/docs/iac/concepts/options/aliases/) to prevent deletions from happening.

{{% /notes %}}

Accept the changes by selecting `yes` and the deployment will occur:

```
Updating (dev)

     Type                                            Name                 Status
     pulumi:pulumi:Stack                             pu-quickstart-dev
 +   ├─ quickstart:index:AzureStaticWebsite          my-site              created (0.16s)
 +   │  ├─ azure-native:resources:ResourceGroup      my-group             created (1s)
 +   │  ├─ azure-native:storage:StorageAccount       myaccount            created (2s)
 +   │  ├─ azure-native:storage:StorageAccountStaticWebsite  static-website   created (0.24s)
 +   │  └─ azure-native:storage:Blob                 index.html           created (0.19s)
 -   ├─ azure-native:storage:Blob                    index.html           deleted (0.18s)
 -   ├─ azure-native:storage:StorageAccountStaticWebsite  static-website   deleted (0.27s)
 -   ├─ azure-native:storage:StorageAccount          myaccount            deleted (0.51s)
 -   └─ azure-native:resources:ResourceGroup         my-group             deleted (0.58s)

Outputs:
  ~ url: "https://myaccountabc123.z13.web.core.windows.net/" => "https://myaccountxyz789.z13.web.core.windows.net/"

Resources:
    + 5 created
    - 4 deleted
    9 changes. 1 unchanged

Duration: 10s
```

Now test out your new website -- it works like before, just with a tidier codebase now!

{{% choosable os "linux,macos" %}}

```bash
$ curl $(pulumi stack output url)
<html>
    <body>
        <h1>Hello, Pulumi!</h1>
    </body>
</html>
```

{{% /choosable %}}

{{% choosable os "windows" %}}

```powershell
> curl (pulumi stack output url)
<html>
    <body>
        <h1>Hello, Pulumi!</h1>
    </body>
</html>
```

{{% /choosable %}}

Once you are ready to move on, let's destroy everything we've spun up in this tutorial.

{{< get-started-stepper >}}

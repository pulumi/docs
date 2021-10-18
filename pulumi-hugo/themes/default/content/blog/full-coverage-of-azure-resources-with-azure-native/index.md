---
title: "Full Coverage of Azure Resources with Azure-Native"
date: 2021-03-02
meta_desc: "Pulumi’s Azure-Native provider is the most comprehensive IaC solution for Microsoft Azure"
meta_image: azure-native.png
authors:
  - mikhail-shilkov
tags:
  - azure
---

Last September, we [announced the beta release of Pulumi Azure NextGen]({{< relref "/blog/announcing-nextgen-azure-provider" >}}): a new Microsoft Azure provider for Pulumi that combines same-day access to the entire [Azure API surface](https://docs.microsoft.com/en-us/rest/api/azure/) with the excellent Pulumi experience you know and love, including version-less resources, auto-naming, and auto-location.

Today, we’re excited to announce that this new provider is now the default way to manage Azure resources with Pulumi. We’re also excited to announce its final name: the native Azure provider for Pulumi, or “Azure-Native” for short. You can get started with the new provider using our newly-updated [getting started guide]({{< relref "/docs/get-started/azure" >}}).

<!--more-->

Already use the [classic Pulumi-Azure provider](https://www.pulumi.com/docs/reference/pkg/azure/)? You can migrate to Azure-Native now using the [migration guide]({{< relref "/registry/packages/azure-native/from-classic" >}}). If you prefer to wait until general availability, stay tuned for updates: we expect to reach general availability in the spring of this year.

Alongside this announcement, we’re also formalizing a new concept: a Pulumi “native provider”. A native provider provides functionality mapped directly from the underlying API; in the case of the new Azure Provider, functionality is mapped directly from the Azure Resource Manager API surface. Going forward, you’ll be able to find these next-generation Pulumi providers directly from the name by looking for the “-Native” suffix.

## Native to Azure

The native Azure provider implements the best possible support for the Azure platform in Pulumi. It exposes the entire API surface of Azure to developers and operators, now and forever. As of today, the native provider supports 1,010 resource types, 120 of them added since the initial preview in September 2020. Every property of each resource is always represented in the SDKs.

Unlike the classic Azure provider, which requires manual work to keep updated, we designed the native provider to stay always up-to-date with Azure API additions and changes. We generate Pulumi SDKs for the native Azure provider automatically from Azure API specifications published by Microsoft. We publish daily builds of the provider and have published 210 versions of the provider in the last six months.

## Native to Pulumi

The native Azure provider comes with several significant improvements over the Azure NextGen preview. These changes bring more features of the Pulumi experience to the native Azure provider.

### Top-level Resources

Every resource is now available in the top-level (versionless) module of its resource provider. You don't have to choose the API version explicitly: we will apply the default for you.

{{< chooser language "typescript,python,csharp,go" >}}

{{% choosable language typescript %}}

```typescript
import * as azure from "@pulumi/azure-native";

const resourceGroup = new azure.resources.ResourceGroup("resourceGroup");

const storageAccount = new azure.storage.StorageAccount("sa", {
   resourceGroupName: resourceGroup.name,
   sku: {
       name: azure.storage.SkuName.Standard_LRS,
   },
   kind: azure.storage.Kind.StorageV2,
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_azure_native as azure

resource_group = azure.resources.ResourceGroup('resource_group')

account = azure.storage.StorageAccount('sa',
   resource_group_name=resource_group.name,
   sku=storage.SkuArgs(
       name=azure.storage.SkuName.STANDARD_LRS,
   ),
   kind=azure.storage.Kind.STORAGE_V2)
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using Pulumi;
using Pulumi.AzureNative.Resources;
using Pulumi.AzureNative.Storage;
using Pulumi.AzureNative.Storage.Inputs;

class MyStack : Stack
{
   public MyStack()
   {
       var resourceGroup = new ResourceGroup("resourceGroup");

       var storageAccount = new StorageAccount("sa", new StorageAccountArgs
       {
           ResourceGroupName = resourceGroup.Name,
           Sku = new SkuArgs
           {
               Name = SkuName.Standard_LRS
           },
           Kind = Kind.StorageV2
       });
   }
}
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
   "github.com/pulumi/pulumi-azure-native/sdk/go/azure/resources"
   "github.com/pulumi/pulumi-azure-native/sdk/go/azure/storage"
   "github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

func main() {
   pulumi.Run(func(ctx *pulumi.Context) error {
       resourceGroup, err := resources.NewResourceGroup(ctx, "resourceGroup", nil)
       if err != nil {
           return err
       }

       account, err := storage.NewStorageAccount(ctx, "sa", &storage.StorageAccountArgs{
           ResourceGroupName: resourceGroup.Name,
           Sku: &storage.SkuArgs{
               Name: storage.SkuName_Standard_LRS,
           },
           Kind: storage.KindStorageV2,
       })

       return err
   })
}
```

{{% /choosable %}}
{{< /chooser >}}

The top-level resources will use stable API versions and take no arbitrary breaking changes within a given major version of the package once we reach general availability; during the preview, breaking changes may appear in `0.x` minor versions.

We still provide access to every version of every ARM API if you want to use the latest version or a specific version from the past. Each API version is mapped to its own module or namespace within the resource provider.

### Auto-Naming

The original preview of the native Azure provider (then called “Azure NextGen”) didn’t yet support auto-naming, a common feature of other Pulumi providers. Now, it provides full support for auto-naming. Azure resources will get a random suffix in the name by default. In the following example, Pulumi will create a resource group called, for instance, `rg53acf911`.

{{< chooser language "typescript,python,csharp,go" >}}

{{% choosable language typescript %}}

```typescript
import * as azure from "@pulumi/azure-native";
const resourceGroup = new azure.resources.ResourceGroup("rg");
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_azure_native as azure
resource_group = azure.resources.ResourceGroup('rg')
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using Pulumi;
using Pulumi.AzureNative.Resources;
class MyStack : Stack
{
   public MyStack()
   {
       var resourceGroup = new ResourceGroup("rg");
   }
}
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
   resources "github.com/pulumi/pulumi-azure-native/sdk/go/azure/resources"
   "github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

func main() {
   pulumi.Run(func(ctx *pulumi.Context) error {
       _, err := resources.NewResourceGroup(ctx, "resourceGroup", nil)
       return err
   })
}
```

{{% /choosable %}}
{{< /chooser >}}

Pass an explicit value to the `resourceGroupName` property if you want to control the resource's exact name.

However, suppose you create a sub-resource, e.g., a container under a storage account, a database under a database account, or a slot under a web app. In that case, Pulumi will not append a random suffix because those resources names don’t have to be globally unique.

You can also apply [transformations](https://www.pulumi.com/docs/intro/concepts/resources/#transformations) to define your own naming schemas: see [this example](https://github.com/matwilko/Pulumi.AzureNextGen.Ambient/blob/434c4beccffdd8d1180e385ff5fe298867a285af/AutoNaming.cs) from our community.

### Auto-Location

Like the classic Azure provider, all resources' `location` property is now optional in the native Azure provider. In the examples above, we did not have to specify the location of resources. Instead, we can run the following command to configure it for the whole stack:

```
pulumi config set azure-native:location WestUS2
```

You can also specify the location explicitly for a resource group but leave it out for resources under that resource group: the resources will deploy to the same region by default. Of course, you are free to override the defaults at any time.

### Beyond ARM API

Unfortunately, some Azure capabilities aren’t yet available via the Azure Resource Manager APIs used by the native Azure provider. To ensure that you can still use some of the missing capabilities, we’ve introduced several resources that go beyond what's currently possible with ARM (and ARM templates):

- Exposing Azure Storage as a static website.
- Uploading files and directories as Azure Storage Blobs.
- Managing Azure KeyVault secrets and keys.

By combining full support for the ARM APIs with these additional extensions, Pulumi's native Azure provider provides the broadest support for managing Azure resources with infrastructure-as-code.

## Open-Source

The native Azure provider for Pulumi is fully open-source. The code is available on GitHub at [pulumi-azure-native](https://github.com/pulumi/pulumi-azure-native).

## Migrate from Azure NextGen to Azure-Native

Migration from Azure NextGen to Azure-Native is simple and non-disruptive:

- Reference the [`pulumi-azure-native`](https://github.com/pulumi/pulumi-azure-native) package from your program.
- Update all import/using statements from `nextgen` to `native`.
- Run `pulumi up` and make sure the program ran successfully. The preview should show no changes.
- If so, choose `yes` to run the update that will overwrite the state to the native provider.

Note that the Azure resources are not affected by this migration.

## Getting Started

If you are new to Pulumi, follow our [Get Started]({{< relref "/docs/get-started/azure" >}}) guide.

From now on, the `azure-*` templates will reference the native Azure provider. It's easier to get started than ever:

{{< chooser language "typescript,python,csharp,go" >}}

{{% choosable language typescript %}}

```sh
$ pulumi new azure-typescript
```

{{% /choosable %}}
{{% choosable language python %}}

```sh
$ pulumi new azure-python
```

{{% /choosable %}}
{{% choosable language csharp %}}

```sh
$ pulumi new azure-csharp
```

{{% /choosable %}}
{{% choosable language go %}}

```sh
$ pulumi new azure-go
```

{{% /choosable %}}
{{< /chooser >}}

Several more extensive examples are available in the Pulumi Examples repo:

- Web Applications with Azure App Service and Docker: [TypeScript](https://github.com/pulumi/examples/tree/master/azure-ts-appservice-docker), [C#](https://github.com/pulumi/examples/tree/master/azure-cs-appservice-docker), [Python](https://github.com/pulumi/examples/tree/master/azure-py-appservice-docker), [Go](https://github.com/pulumi/examples/tree/master/azure-go-appservice-docker)
- Azure AKS cluster: [TypeScript](https://github.com/pulumi/examples/tree/master/azure-ts-aks), [C#](https://github.com/pulumi/examples/tree/master/azure-cs-aks), [Python](https://github.com/pulumi/examples/tree/master/azure-py-aks), [Go](https://github.com/pulumi/examples/tree/master/azure-go-aks)
- Web Application with Azure Container Instances: [TypeScript](https://github.com/pulumi/examples/tree/master/azure-ts-aci), [C#](https://github.com/pulumi/examples/tree/master/azure-cs-aci), [Python](https://github.com/pulumi/examples/tree/master/azure-py-aci), [Go](https://github.com/pulumi/examples/tree/master/azure-go-aci)
- Web Server Using Azure Virtual Machine: [TypeScript](https://github.com/pulumi/examples/tree/master/azure-ts-webserver), [Python](https://github.com/pulumi/examples/tree/master/azure-py-webserver)

You can browse [API reference docs](https://www.pulumi.com/docs/reference/pkg/azure-native/) with inline examples or explore the [Pulumi Azure-Native SDKs](https://github.com/pulumi/pulumi-azure-native) repository.

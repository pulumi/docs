---
title: "Announcing Pulumi Azure Provider 2.0"
date: 2020-03-12
meta_desc: "Announcing the 2.0 release of Pulumi Azure provider and what's new in it."
meta_image: azure20.png
authors:
    - mikhail-shilkov
tags:
    - Azure
---

We are happy to announce the release of a new major version of the Pulumi Azure provider. Pulumi Azure 2.0 is based on the [2.0 release](https://www.terraform.io/docs/providers/azurerm/guides/2.0-upgrade-guide.html) of the upstream provider and brings several improvements and breaking changes.

<!--more-->

This article outlines the most significant changes:

- Improvements in Azure Storage resources
- New resources for VMs & VM Scale Sets
- Removed deprecated resources and fields
- Latest versions in Callback Functions
- Configuring custom timeouts
- How to migrate and where to get help if needed

The provider release is not directly related to our [Pulumi 2.0 plans]({{< relref "/blog/pulumi-2020-update" >}}).

## Improvements in Azure Storage

We streamlined the experience of working with Azure Storage resources.

The Storage `Account` resource has finally received native support for static website provisioning: it's as simple as declaring a `staticWebsite` property:

``` ts
const storageAccount = new azure.storage.Account("mywebsite", {
    resourceGroupName: resourceGroup.name,
    accountReplicationType: "LRS",
    accountKind: "StorageV2",
    staticWebsite: {
        indexDocument: "index.html",
    },
});
```

In version 1.x, the `Blob` resource could upload a file to a storage container, while the `ZipBlob` would take a local directory, zip it, and upload the archive file to a storage container. In 2.0, we deprecated the `ZipBlob` resource and combined both capabilities in `Blob`.

`Blob` can now accept an instance of the `FileAsset` class. `FileAsset` watches the contents of the file on disk, so if the file changes, Pulumi re-uploads the file on the next update.

The following snippet uploads a list of files from a local disk to the newly created static website:

``` ts
foreach (let file in files)
    new azure.storage.Blob(file, {
        storageAccountName: storageAccount.name,
        storageContainerName: "$web",
        type: "Block",
        source: new pulumi.asset.FileAsset(`./wwwroot/${file}`),
        contentType: "text/html",
    }),
);
```

Note that `resourceGroupName` properties were removed from all storage resources except the account: blobs or queues can't belong to a resource group on their own.

## New Resources for Virtual Machine & Virtual Machine Scale Set

There are four new resources for Virtual Machine & Virtual Machine Scale Set separated by operating system: `LinuxVirtualMachine`, `WindowsVirtualMachine`, `LinuxVirtualMachineScaleSet`, `WindowsVirtualMachineScaleSet`. The old-style generic `VirtualMachine` and `VirtualMachineScaleSet` are still available, so you can take your time before migrating existing stacks.

Here is a snippet that defines an Ubuntu VM:

``` ts
const vm = new azure.compute.LinuxVirtualMachine("server-vm", {
    resourceGroupName,
    networkInterfaceIds: [networkInterface.id],
    size: "Standard_A0",
    sourceImageReference: {
        publisher: "Canonical",
        offer: "UbuntuServer",
        sku: "16.04-LTS",
        version: "latest",
    },
    osDisk: {
        caching: "ReadWrite",
        storageAccountType: "Standard_LRS",
    },
    computerName: "hostname",
    adminUsername: username,
    adminPassword: password,
    disablePasswordAuthentication: false,
);
```

## Removing Deprecated Resources, Invokes, and Fields

Azure Active Directory has its [own Pulumi provider](https://github.com/pulumi/pulumi-azuread/), so all the AD resources were now removed from the `AD` namespace of the Azure provider 2.0.

A number of other resources, invokes, and fields were removed too, following the changes in the upstream provider. You can see the full list in [this upgrade guide](https://www.terraform.io/docs/providers/azurerm/guides/2.0-upgrade-guide.html).

## Default Versions in Callback Functions

[Serverless as Callbacks](https://www.pulumi.com/blog/serverless-as-simple-callbacks-with-pulumi-and-azure-functions/) running on Azure Functions have bumped the default version of the Azure Functions runtime to `~3` and `Node.js` to `~12`. As always, you can override the default to set the versions that you require.

Callback Functions also moved from `ZipBlob` to `Blob` deploy as described above, so expect another replacement operation while upgrading.

## Custom Timeouts

Some types of resources take longer to create than others. For instance, provisioning a new Cosmos DB account may take from 10 minutes to over an hour depending on the number of geo locations and other factors.

If the creation of a target resource times out, you can override the default timeout using resource options:

``` ts
const cosmosdbAccount = new azure.cosmosdb.Account("cosmosdb", {
    resourceGroupName: resourceGroup.name,
    offerType: "Standard",
    geoLocations: manyLocations,
    consistencyPolicy: { consistencyLevel: "Session" },
}, {
    customTimeouts: {
        create: "30m",
        update: "60m",
    },
});
```

You shouldn't need this ability often, but it can be a lifesaver when you do.

## Getting Started with Migration

To get started with Azure provider 2.0, update the versions in your package manager:

{{< langchoose csharp >}}

```typescript
// package.json
"@pulumi/azure": "^2.0.0",
```

```csharp
// csproj/fsproj/vbproj
<PackageReference Include="Pulumi.Azure" Version="2.1.0-preview" />
```

```python
# requirements.txt
pulumi-azure>=2.0.0
```

```go
// Gopkg.toml
[constraint]]
  version = "v2.0.0"
  name = "github.com/pulumi/pulumi-azure"
```

There are quite a few breaking changes, so you may need to adjust your code before you can run the program successfully again. Check [the upgrade guide](https://www.terraform.io/docs/providers/azurerm/guides/2.0-upgrade-guide.html) for details.

To help with this process, we upgraded all our Azure [templates](https://github.com/pulumi/templates/) and [examples](https://github.com/pulumi/examples/) to 2.0.

If you want to stay with the 1.x version, please pin your version to `^1.0.0` or `1.14.0` in the package manager.

If you have issues or questions, reach out to us on [Pulumi Community Slack](https://slack.pulumi.com/), and we'll help you through migration.

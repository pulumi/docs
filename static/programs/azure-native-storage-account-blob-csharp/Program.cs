using Pulumi;
using Pulumi.AzureNative.Resources;
using Pulumi.AzureNative.Storage;
using Pulumi.AzureNative.Storage.Inputs;
using System.Collections.Generic;

return await Pulumi.Deployment.RunAsync(() =>
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

    var blobContainer = new BlobContainer("blobContainer", new()
    {
        AccountName = resourceGroup.Name,
        ResourceGroupName = storageAccount.Name,
    });

    var resourceGroupName = resourceGroup.Name;
    var storageAccountName = storageAccount.Name;
    var blobContainerName = blobContainer.Name;

    var blobResource = new Blob("blobResource", new()
    {
        AccountName = storageAccountName,
        ContainerName = blobContainerName,
        ResourceGroupName = resourceGroupName,
        AccessTier = BlobAccessTier.Hot,
        Source = new StringAsset("content"),
        Type = BlobType.Block,
    });

    return new Dictionary<string, object?>
    {
        ["resourceGroupName"] = resourceGroup.Name,
        ["storageAccountName"] = storageAccount.Name,
        ["blobContainerName"] = blobContainer.Name
    };
});
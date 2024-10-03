using Pulumi;
using Pulumi.AzureNative.Resources;
using Pulumi.AzureNative.Storage;
using Pulumi.AzureNative.Storage.Inputs;
using System.Collections.Generic;

return await Pulumi.Deployment.RunAsync(() =>
{
    var path = "./wwwroot";
    var indexDocument = "index.html";
    var errorDocument = "error.html";

    // Steps:
    // [1] Create a resource group.
    // [2] Create a blob storage account.
    // [3] Configure the storage account as a website.

    // [1] Create a resource group.
    var resourceGroup = new ResourceGroup("website-resource-group");

    // [2] Create a blob storage account.
    var storageAccount = new StorageAccount("websiteblob", new StorageAccountArgs
    {
        ResourceGroupName = resourceGroup.Name,
        Sku = new SkuArgs
        {
            Name = SkuName.Standard_LRS
        },
        Kind = Kind.StorageV2
    });

    // [3] Configure the storage account as a website.
    var website = new Storage.StorageAccountStaticWebsite("website", new Storage.StorageAccountStaticWebsiteArgs
    {
        AccountName = storageAccount.Name,
        ResourceGroupName = resourceGroup.Name,
        IndexDocument = indexDocument,
        Error404Document = errorDocument,
    });

    // Upload the website files
    var index_html = new Storage.Blob("index.html", new Storage.BlobArgs
    {
        ResourceGroupName = resourceGroup.Name,
        AccountName = storageAccount.Name,
        ContainerName = website.ContainerName,
        Source = new FileAsset($"./{path}/{indexDocument}"),
        ContentType = "text/html",
    });

    var notfound_html = new Storage.Blob("404.html", new Storage.BlobArgs
    {
        ResourceGroupName = resourceGroup.Name,
        AccountName = storageAccount.Name,
        ContainerName = website.ContainerName,
        Source = new FileAsset($"./{path}/{errorDocument}"),
        ContentType = "text/html",
    });

    staticEndpoint = storageAccount.PrimaryEndpoints.Apply(primaryEndpoints => primaryEndpoints.Web);

    // Export the URL of the website.
    return new Dictionary<string, object?>
    {
        ["staticEndpoint"] = staticEndpoint
    };
});
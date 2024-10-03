using Pulumi;
using Resources = Pulumi.AzureNative.Resources;
using Storage = Pulumi.AzureNative.Storage;
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
    var resourceGroup = new Resources.ResourceGroup("website-resource-group", new()
    {
        Location = "eastus",
    });

    // [2] Create a blob storage account.
    var storageAccount = new Storage.StorageAccount("websiteblob", new()
    {
        ResourceGroupName = resourceGroup.Name,
        Sku = new Storage.Inputs.SkuArgs
        {
            Name = Storage.SkuName.Standard_LRS
        },
        Kind = Storage.Kind.StorageV2
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

    var staticEndpoint = storageAccount.PrimaryEndpoints.Apply(primaryEndpoints => primaryEndpoints.Web);

    // Export the URL of the website.
    return new Dictionary<string, object?>
    {
        ["staticEndpoint"] = staticEndpoint
    };
});
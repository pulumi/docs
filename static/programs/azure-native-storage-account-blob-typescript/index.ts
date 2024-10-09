import * as pulumi from "@pulumi/pulumi";
import * as resources from "@pulumi/azure-native/resources";
import * as storage from "@pulumi/azure-native/storage";

const resourceGroup = new resources.ResourceGroup("resourceGroup");

const storageAccount = new storage.StorageAccount("sa", {
    resourceGroupName: resourceGroup.name,
    sku: {
        name: "Standard_LRS",
    },
    kind: "StorageV2",
});

const blobContainer = new storage.BlobContainer("blobContainer", {
    accountName: storageAccount.name,
    resourceGroupName: resourceGroup.name,
});

const blobResource = new storage.Blob("blobResource", {
    accountName: storageAccount.name,
    containerName: blobContainer.name,
    resourceGroupName: resourceGroup.name,
    accessTier: storage.BlobAccessTier.Hot,
    source: new pulumi.asset.StringAsset("content"),
    type: storage.BlobType.Block,
});

export const resourceGroupName = resourceGroup.name;
export const storageAccountName = storageAccount.name;
export const blobContainerName = blobContainer.name;

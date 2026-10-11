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

const resourceGroupName2 = resourceGroup.name;
const storageAccountName2 = storageAccount.name;
const blobContainerName2 = blobContainer.name;

const blobResource = new storage.Blob("blobResource", {
    accountName: storageAccountName2,
    containerName: blobContainerName2,
    resourceGroupName: resourceGroupName2,
    accessTier: storage.BlobAccessTier.Hot,
    source: new pulumi.asset.StringAsset("content"),
    type: storage.BlobType.Block,
});

export const resourceGroupName = resourceGroup.name;
export const storageAccountName = storageAccount.name;
export const blobContainerName = blobContainer.name;

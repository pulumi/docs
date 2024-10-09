"use strict";
const pulumi = require("@pulumi/pulumi");
const resources = require("@pulumi/azure-native/resources");
const storage = require("@pulumi/azure-native/storage");

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

const resourceGroupName = resourceGroup.name;
const storageAccountName = storageAccount.name;
const blobContainerName = blobContainer.name;

const blobResource = new storage.Blob("blobResource", {
    accountName: storageAccountName,
    containerName: blobContainerName,
    resourceGroupName: resourceGroupName,
    accessTier: storage.BlobAccessTier.Hot,
    source: new pulumi.asset.StringAsset("content"),
    type: storage.BlobType.Block,
});

exports.resourceGroupName = resourceGroup.name;
exports.storageAccountName = storageAccount.name;
exports.blobContainerName = blobContainer.name;

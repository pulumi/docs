"use strict";
const pulumi = require("@pulumi/pulumi");
const resources = require("@pulumi/azure-native/resources");
const storage = require("@pulumi/azure-native/storage");

const path = "./wwwroot";
const indexDocument = "index.html";
const errorDocument = "error.html";

// Steps:
// [1] Create a resource group.
// [2] Create a blob storage account.
// [3] Configure the storage account as a website.

// [1] Create a resource group.
const resourceGroup = new resources.ResourceGroup("website-resource-group", {
    location: "eastus",
});

// [2] Create a blob storage account.
const storageAccount = new storage.StorageAccount("websiteblob", {
    resourceGroupName: resourceGroup.name,
    kind: "StorageV2",
    sku: {
        name: "Standard_LRS",
    },
});

// [3] Configure the storage account as a website.
const website = new storage.StorageAccountStaticWebsite("website", {
    accountName: storageAccount.name,
    resourceGroupName: resourceGroup.name,
    indexDocument: indexDocument,
    error404Document: errorDocument,
});

// Upload the website files
[indexDocument, errorDocument].map(
    name =>
        new storage.Blob(name, {
            resourceGroupName: resourceGroup.name,
            accountName: storageAccount.name,
            containerName: website.containerName,
            source: new pulumi.asset.FileAsset(`./${path}/${name}`),
            contentType: "text/html",
        }),
);

// Export the URL of the website.
exports.staticEndpoint = storageAccount.primaryEndpoints.web;

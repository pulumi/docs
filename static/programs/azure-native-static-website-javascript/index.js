"use strict";
const pulumi = require("@pulumi/pulumi");
const resources = require("@pulumi/azure-native/resources");
const storage = require("@pulumi/azure-native/storage");

// Create an Azure Resource Group
const resourceGroup = new resources.ResourceGroup("resourceGroup");

// Create an Azure resource (Storage Account)
const storageAccount = new storage.StorageAccount("sa", {
    resourceGroupName: resourceGroup.name,
    sku: {
        name: "Standard_LRS",
    },
    kind: "StorageV2",
});

// Export the primary key of the Storage Account
const storageAccountKeys = storage.listStorageAccountKeysOutput({
    resourceGroupName: resourceGroup.name,
    accountName: storageAccount.name,
});

// Export the primary storage key for the storage account
exports.primaryStorageKey = storageAccountKeys.keys[0].value;

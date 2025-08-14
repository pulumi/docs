import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import * as azure from "@pulumi/azure-native";
import * as gcp from "@pulumi/gcp";

// The same TypeScript patterns work across all clouds
const config = new pulumi.Config();
const environment = config.get("environment") || "test";

// AWS S3 Bucket
const awsStorage = new aws.s3.Bucket("my-storage", {
    tags: {
        Environment: environment,
        ManagedBy: "Pulumi",
    },
    versioning: {
        enabled: true,
    },
    serverSideEncryptionConfiguration: {
        rule: {
            applyServerSideEncryptionByDefault: {
                sseAlgorithm: "AES256",
            },
        },
    },
});

// Azure Storage Account - same patterns, different provider
const resourceGroup = new azure.resources.ResourceGroup("my-rg");
const azureStorage = new azure.storage.StorageAccount("mystorage", {
    resourceGroupName: resourceGroup.name,
    location: "East US",
    tags: {
        Environment: environment,
        ManagedBy: "Pulumi",
    },
    sku: {
        name: azure.storage.SkuName.Standard_LRS,
    },
    kind: azure.storage.Kind.StorageV2,
});

// Google Cloud Storage - consistent programming model
const gcpStorage = new gcp.storage.Bucket("my-storage", {
    location: "US",
    labels: {
        environment: environment.toLowerCase(),
        managed_by: "pulumi",
    },
    versioning: {
        enabled: true,
    },
    uniformBucketLevelAccess: true,
});

// Export URLs from all three clouds using the same pattern
export const awsUrl = pulumi.interpolate`s3://${awsStorage.id}`;
export const azureUrl = pulumi.interpolate`https://${azureStorage.name}.blob.core.windows.net/`;
export const gcpUrl = pulumi.interpolate`gs://${gcpStorage.name}`;
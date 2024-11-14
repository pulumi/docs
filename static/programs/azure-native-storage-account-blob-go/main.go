package main

import (
	"github.com/pulumi/pulumi-azure-native-sdk/resources/v2"
	"github.com/pulumi/pulumi-azure-native-sdk/storage/v2"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		resourceGroup, err := resources.NewResourceGroup(ctx, "resourceGroup", nil)
		if err != nil {
			return err
		}

		storageAccount, err := storage.NewStorageAccount(ctx, "sa", &storage.StorageAccountArgs{
			ResourceGroupName: resourceGroup.Name,
			Sku: &storage.SkuArgs{
				Name: pulumi.String("Standard_LRS"),
			},
			Kind: pulumi.String("StorageV2"),
		})
		if err != nil {
			return err
		}

		blobContainer, err := storage.NewBlobContainer(ctx, "blobContainer", &storage.BlobContainerArgs{
			AccountName:                 storageAccount.Name,
			ResourceGroupName:           resourceGroup.Name,
		})
		if err != nil {
			return err
		}

		resourceGroupName := resourceGroup.Name
		storageAccountName := storageAccount.Name
		blobContainerName := blobContainer.Name

		_, err = storage.NewBlob(ctx, "blobResource", &storage.BlobArgs{
			AccountName:       storageAccountName,
			ContainerName:     blobContainerName,
			ResourceGroupName: resourceGroupName,
			AccessTier:        storage.BlobAccessTierHot,
			Source: pulumi.NewStringAsset("content"),
			Type:   storage.BlobTypeBlock,
		})

		ctx.Export("resourceGroupName", resourceGroup.Name)
		ctx.Export("storageAccountName", storageAccount.Name)
		ctx.Export("blobContainerName", blobContainer.Name)

		return nil
	})
}

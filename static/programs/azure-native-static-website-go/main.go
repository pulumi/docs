package main

import (
	"github.com/pulumi/pulumi-azure-native-sdk/resources/v2"
	"github.com/pulumi/pulumi-azure-native-sdk/storage/v2"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		path := "./wwwroot";
		indexDocument := "index.html";
		errorDocument := "error.html";
	
		// Steps:
		// [1] Create a resource group.
		// [2] Create a blob storage account.
		// [3] Configure the storage account as a website.
	
		// [1] Create a resource group.
		resourceGroup, err := resources.NewResourceGroup(ctx, "website-resource-group", &resources.ResourceGroupArgs{
			Location:          pulumi.String("eastus"),
		})
		if err != nil {
			return err
		}

		// [2] Create a blob storage account.
		storageAccount, err := storage.NewStorageAccount(ctx, "websiteblob", &storage.StorageAccountArgs{
			ResourceGroupName: resourceGroup.Name,
			Sku: &storage.SkuArgs{
				Name: pulumi.String("Standard_LRS"),
			},
			Kind: pulumi.String("StorageV2"),
		})
		if err != nil {
			return err
		}

		//[3] Configure the storage account as a website.
		website, err := storage.NewStorageAccountStaticWebsite(ctx, "staticWebsite", &storage.StorageAccountStaticWebsiteArgs{
			AccountName:       storageAccount.Name,
			ResourceGroupName: resourceGroup.Name,
			IndexDocument:     pulumi.String("index.html"),
			Error404Document:  pulumi.String("404.html"),
		})
		if err != nil {
			return err
		}

		_, err = storage.NewBlob(ctx, "index.html", &storage.BlobArgs{
			ResourceGroupName: resourceGroup.Name,
			AccountName:       storageAccount.Name,
			ContainerName:     website.ContainerName,
			Source:            pulumi.NewFileAsset("./" + path + "/" + indexDocument),
			ContentType:       pulumi.String("text/html"),
		})
		if err != nil {
			return err
		}
		_, err = storage.NewBlob(ctx, "404.html", &storage.BlobArgs{
			ResourceGroupName: resourceGroup.Name,
			AccountName:       storageAccount.Name,
			ContainerName:     website.ContainerName,
			Source:            pulumi.NewFileAsset("./" + path + "/" + errorDocument),
			ContentType:       pulumi.String("text/html"),
		})
		if err != nil {
			return err
		}

		// Export the URL of the website.
		ctx.Export("staticEndpoint", storageAccount.PrimaryEndpoints.Web())
		return nil
	})
}

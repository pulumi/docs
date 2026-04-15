package main

import (
	"github.com/pulumi/pulumi-gcp/sdk/v8/go/gcp/cloudrunv2"
	"github.com/pulumi/pulumi-gcp/sdk/v8/go/gcp/storage"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Create a Cloud Storage bucket using the GCP Classic provider.
		bucket, err := storage.NewBucket(ctx, "my-bucket", &storage.BucketArgs{
			Location:                 pulumi.String("US"),
			UniformBucketLevelAccess: pulumi.Bool(true),
			ForceDestroy:             pulumi.Bool(true),
		})
		if err != nil {
			return err
		}

		// Create a Cloud Run service.
		service, err := cloudrunv2.NewService(ctx, "my-service", &cloudrunv2.ServiceArgs{
			Location:           pulumi.String("us-central1"),
			DeletionProtection: pulumi.Bool(false),
			Template: &cloudrunv2.ServiceTemplateArgs{
				Containers: cloudrunv2.ServiceTemplateContainerArray{
					&cloudrunv2.ServiceTemplateContainerArgs{
						Image: pulumi.String("us-docker.pkg.dev/cloudrun/container/hello"),
					},
				},
			},
		})
		if err != nil {
			return err
		}

		ctx.Export("bucketName", bucket.Name)
		ctx.Export("serviceUrl", service.Uri)
		return nil
	})
}

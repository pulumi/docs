package main

import (
	"fmt"

	"github.com/pulumi/pulumi-gcp/sdk/v8/go/gcp/projects"
	"github.com/pulumi/pulumi-gcp/sdk/v8/go/gcp/storage"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		bucket, err := storage.NewBucket(ctx, "bucket", &storage.BucketArgs{
			Location:     pulumi.String("US"),
			ForceDestroy: pulumi.Bool(true),
		})
		if err != nil {
			return err
		}
		
		role, err := projects.NewIAMCustomRole(ctx, "role", &projects.IAMCustomRoleArgs{
			RoleId: pulumi.String("bucketViewerRole"),
			Title:  pulumi.String("Bucket Viewer Role"),
			Permissions: pulumi.StringArray{
				pulumi.String("storage.objects.get"),
				pulumi.String("storage.objects.list"),
			},
			Stage: pulumi.String("GA"),
		})
		if err != nil {
			return err
		}
		
		_, err = storage.NewBucketIAMMember(ctx, "bucketViewerRoleAssignment", &storage.BucketIAMMemberArgs{
			Bucket: bucket.Name,
			Role:   role.Name,
			Member: pulumi.String("allAuthenticatedUsers"),
		})
		if err != nil {
			return err
		}

		bucketName := bucket.Name.ApplyT(func(name string) string {
			return name
		}).(pulumi.StringOutput)

		roleName := role.RoleId.ApplyT(func(name string) string {
			return name
		}).(pulumi.StringOutput)

		_, err = storage.NewBucketObject(ctx, "bucketObject", &storage.BucketObjectArgs{
			Bucket: bucketName,
			Content: roleName.ApplyT(func(roleName string) (string, error) {
				return fmt.Sprintf("My bucket role name is: %v", roleName), nil
			}).(pulumi.StringOutput),
			ContentType: pulumi.String("text/plain"),
		})
		if err != nil {
			return err
		}
		
		ctx.Export("roleName", role.RoleId)
		ctx.Export("bucketName", bucket.Name)
		return nil
	})
}

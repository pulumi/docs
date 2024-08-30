package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/s3"
	"github.com/pulumi/pulumi-random/sdk/v4/go/random"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Create an AWS resource (S3 Bucket)
		petName, err := random.NewRandomPet(ctx, "my-pet-name", nil)
		if err != nil {
			return err
		}

		bucket, err := s3.NewBucket(ctx, "b", nil)
		if err != nil {
			return err
		}

		_, err = s3.NewBucketObject(ctx, "index.html", &s3.BucketObjectArgs{
			Bucket:  bucket.ID(),
			Content: pulumi.String("Thanks for using Pulumi!"),
		}, pulumi.Parent(bucket))
		if err != nil {
			return err
		}

		_, err = s3.NewBucketObject(ctx, "random.html", &s3.BucketObjectArgs{
			Bucket:  bucket.ID(),
			Content: petName.ID(),
		}, pulumi.Parent(bucket))
		if err != nil {
			return err
		}

		// Export the name of the bucket
		ctx.Export("PetName", petName.ID())
		return nil
	})
}

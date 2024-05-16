package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v4/go/aws/s3"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		bucket, err := s3.NewBucket(ctx, "bucket", nil)
		if err != nil {
			return err
		}

		file, err := s3.NewBucketObject(ctx, "bucket-object", &s3.BucketObjectArgs{
			Bucket:  bucket.ID(),
			Key:     pulumi.String("some-file.txt"),
			Content: pulumi.String("some-content"),
		})
		if err != nil {
			return err
		}

		s3Url := pulumi.Sprintf("s3://%s/%s", bucket.ID(), file.Key)
		ctx.Export("s3Url", s3Url)

		return nil
	})
}

package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v7/go/aws/s3"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {

		// Create an S3 bucket.
		bucket, err := s3.NewBucket(ctx, "my-bucket", nil)
		if err != nil {
			return err
		}

		// Create an S3 bucket policy that grants read access to all objects in the bucket.
		// The Resource field uses pulumi.Sprintf to append "/*" to the bucket ARN,
		// targeting individual objects rather than the bucket itself.
		_, err = s3.NewBucketPolicy(ctx, "my-bucket-policy", &s3.BucketPolicyArgs{
			Bucket: bucket.ID(),
			Policy: pulumi.JSONMarshal(map[string]interface{}{
				"Version": pulumi.ToOutput("2012-10-17"),
				"Statement": pulumi.ToOutput([]interface{}{
					pulumi.ToMapOutput(map[string]pulumi.Output{
						"Effect":    pulumi.ToOutput("Allow"),
						"Principal": pulumi.ToOutput("*"),
						"Action":    pulumi.ToOutput("s3:GetObject"),
						"Resource":  pulumi.Sprintf("%s/*", bucket.Arn),
					}),
				}),
			}),
		})
		if err != nil {
			return err
		}

		// Export the name of the bucket.
		ctx.Export("bucketName", bucket.ID())
		return nil
	})
}

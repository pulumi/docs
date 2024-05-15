package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws"
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/s3"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {

		// Get the account ID of the current user as a Pulumi Output.
		callerIdentity, err := aws.GetCallerIdentity(ctx, nil, nil)
		if err != nil {
			return err
		}
		accountID := callerIdentity.AccountId

		// Create an AWS resource (S3 Bucket)
		bucket, err := s3.NewBucket(ctx, "my-bucket", nil)
		if err != nil {
			return err
		}

		// Create an S3 bucket policy allowing anyone in the account to list the contents of the bucket.
		_, err = s3.NewBucketPolicy(ctx, "my-bucket-policy", &s3.BucketPolicyArgs{
			Bucket: bucket.ID(),
			Policy: pulumi.JSONMarshal(map[string]interface{}{
				"Version": pulumi.ToOutput("2012-10-17"),
				"Statement": pulumi.ToOutput([]interface{}{
					pulumi.ToMapOutput(map[string]pulumi.Output{
						"Effect": pulumi.ToOutput("Allow"),
						"Principal": pulumi.ToMapOutput(map[string]pulumi.Output{
							"AWS": pulumi.Sprintf("arn:aws:iam::%s:root", accountID),
						}),
						"Action":   pulumi.ToOutput("s3:ListBucket"),
						"Resource": bucket.Arn,
					}),
				}),
			}),
		})
		if err != nil {
			return err
		}

		// Export the name of the bucket
		ctx.Export("bucketName", bucket.ID())
		return nil
	})
}

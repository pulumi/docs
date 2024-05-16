package main

import (
	"fmt"

	"github.com/pulumi/pulumi-aws/sdk/v4/go/aws/s3"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Create an S3 bucket
		s3Bucket, err := s3.NewBucket(ctx, "myBucket", nil)
		if err != nil {
			return err
		}

		// IAM Policy Document that allows the Lambda service to write to the S3 bucket
		s3Bucket.Arn.ApplyT(func(arn string) (string, error) {
			policy := fmt.Sprintf(`{
				"Version": "2012-10-17",
				"Statement": [{
					"Effect": "Allow",
					"Principal": {"Service": "lambda.amazonaws.com"},
					"Action": ["s3:PutObject", "s3:PutObjectAcl"],
					"Resource": "%s/*"
				}]
			}`, arn)

			// Attach the policy to the bucket
			_, err := s3.NewBucketPolicy(ctx, "myBucketPolicy", &s3.BucketPolicyArgs{
				Bucket: s3Bucket.ID(),
				Policy: pulumi.String(policy),
			})
			if err != nil {
				return "", err
			}

			return "", nil
		})

		// Export the names and ARNs of the created resources
		ctx.Export("bucketName", s3Bucket.ID())
		ctx.Export("bucketArn", s3Bucket.Arn)

		return nil
	})
}

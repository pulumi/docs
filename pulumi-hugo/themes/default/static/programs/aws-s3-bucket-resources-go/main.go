package main

import (
	"encoding/json"
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/s3"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		bucket, err := s3.NewBucket(ctx, "my-bucket", nil)
		if err != nil {
			return err
		}

		ownershipControls, err := s3.NewBucketOwnershipControls(ctx, "ownership-controls", &s3.BucketOwnershipControlsArgs{
			Bucket: bucket.ID(),
			Rule: &s3.BucketOwnershipControlsRuleArgs{
				ObjectOwnership: pulumi.String("ObjectWriter"),
			},
		})
		if err != nil {
			return err
		}

		publicAccessBlock, err := s3.NewBucketPublicAccessBlock(ctx, "public-access-block", &s3.BucketPublicAccessBlockArgs{
			Bucket:          bucket.ID(),
			BlockPublicAcls: pulumi.Bool(false),
		})
		if err != nil {
			return err
		}

		_, err = s3.NewBucketMetric(ctx, "my-bucket-metric", &s3.BucketMetricArgs{
			Bucket: bucket.ID(),
		})
		if err != nil {
			return err
		}

		_, err = s3.NewBucketNotification(ctx, "my-bucket-notification", &s3.BucketNotificationArgs{
			Bucket: bucket.ID(),
		})
		if err != nil {
			return err
		}

		_, err = s3.NewBucketObject(ctx, "my-bucket-object", &s3.BucketObjectArgs{
			Bucket:  bucket.ID(),
			Content: pulumi.String("hello world"),
		}, pulumi.DependsOn([]pulumi.Resource{
			publicAccessBlock,
			ownershipControls,
		}))
		if err != nil {
			return err
		}

		_, err = s3.NewBucketPolicy(ctx, "my-bucket-policy", &s3.BucketPolicyArgs{
			Bucket: bucket.ID(),
			Policy: bucket.ID().ToStringOutput().ApplyT(func(bucketName string) (string, error) {
				policy := map[string]interface{}{
					"Version": "2012-10-17",
					"Statement": []interface{}{
						map[string]interface{}{
							"Effect":    "Allow",
							"Principal": "*",
							"Action":    "s3:GetObject",
							"Resource":  "arn:aws:s3:::" + bucketName + "/*",
						},
					},
				}
				policyJSON, err := json.Marshal(policy)
				return string(policyJSON), err
			}).(pulumi.StringOutput),
		})
		if err != nil {
			return err
		}

		return nil
	})
}

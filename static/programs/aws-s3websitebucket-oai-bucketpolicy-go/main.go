/*
The Pulumi Go SDK does not currently support serializing or deserializing maps with unknown values.
It is tracked here: https://github.com/pulumi/pulumi/issues/12460

The following is a simplified example of using `pulumi.JSONMarshal` in Go.
*/

package main

import (
	"encoding/json"
	"github.com/pulumi/pulumi-aws/sdk/v7/go/aws/cloudfront"
	"github.com/pulumi/pulumi-aws/sdk/v7/go/aws/s3"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		bucket, err := s3.NewBucket(ctx, "content-bucket", nil)
		if err != nil {
			return err
		}

		bucketOwnership, err := s3.NewBucketOwnershipControls(ctx, "content-bucket",
			&s3.BucketOwnershipControlsArgs{
				Bucket: bucket.Bucket,
				Rule: s3.BucketOwnershipControlsRuleArgs{
					ObjectOwnership: pulumi.String("BucketOwnerPreferred"),
				},
			})
		if err != nil {
			return err
		}

		_, err = s3.NewBucketAcl(ctx, "content-bucket",
			&s3.BucketAclArgs{
				Bucket: bucket.Bucket,
				Acl:    pulumi.String("private"),
			}, pulumi.DependsOn([]pulumi.Resource{bucketOwnership}))
		if err != nil {
			return err
		}

		_, err = s3.NewBucketWebsiteConfiguration(ctx, "content-bucket",
			&s3.BucketWebsiteConfigurationArgs{
				Bucket: bucket.Bucket,
				IndexDocument: s3.BucketWebsiteConfigurationIndexDocumentArgs{
					Suffix: pulumi.String("index.html"),
				},
				ErrorDocument: s3.BucketWebsiteConfigurationErrorDocumentArgs{
					Key: pulumi.String("404.html"),
				},
			})
		if err != nil {
			return err
		}

		originAccessIdentity, err := cloudfront.NewOriginAccessIdentity(ctx, "cloudfront", &cloudfront.OriginAccessIdentityArgs{
			Comment: pulumi.Sprintf("OAI-%s", bucket.ID()),
		})
		if err != nil {
			return err
		}

		_, err = s3.NewBucketPolicy(ctx, "cloudfront-bucket-policy", &s3.BucketPolicyArgs{
			Bucket: bucket.ID(),
			Policy: pulumi.All(bucket.Arn, originAccessIdentity.IamArn).ApplyT(
				func(args []interface{}) (pulumi.StringOutput, error) {
					bucketArn := args[0].(string)
					iamArn := args[1].(string)

					policy, err := json.Marshal(map[string]interface{}{
						"Version": "2012-10-17",
						"Statement": []map[string]interface{}{
							{
								"Sid":    "CloudfrontAllow",
								"Effect": "Allow",
								"Principal": map[string]interface{}{
									"AWS": iamArn,
								},
								"Action":   "s3:GetObject",
								"Resource": bucketArn + "/*",
							},
						},
					})

					if err != nil {
						return pulumi.StringOutput{}, err
					}
					return pulumi.String(policy).ToStringOutput(), nil
				}).(pulumi.StringOutput),
		}, pulumi.Parent(bucket))
		if err != nil {
			return err
		}
		return nil
	})
}

/*
The Pulumi Go SDK does not currently support serializing or deserializing maps with unknown values.
It is tracked here: https://github.com/pulumi/pulumi/issues/12460

The following is a simplified example of using `pulumi.JSONMarshal` in Go.
*/

package main

import (
	"encoding/json"
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/cloudfront"
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/s3"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		bucket, err := s3.NewBucket(ctx, "content-bucket", &s3.BucketArgs{
			Acl: pulumi.String("private"),
			Website: &s3.BucketWebsiteArgs{
				IndexDocument: pulumi.String("index.html"),
				ErrorDocument: pulumi.String("404.html"),
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

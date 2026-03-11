package staticpagecomponent

import (
	"encoding/json"
	"fmt"

	"github.com/pulumi/pulumi-aws/sdk/v7/go/aws/s3"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type StaticPageArgs struct {
	IndexContent pulumi.StringInput `pulumi:"indexContent"`
}

type StaticPage struct {
	pulumi.ResourceState
	Endpoint pulumi.StringOutput `pulumi:"endpoint"`
}

func NewStaticPage(ctx *pulumi.Context, name string, args *StaticPageArgs, opts ...pulumi.ResourceOption) (*StaticPage, error) {
	comp := &StaticPage{}
	err := ctx.RegisterComponentResource("sample-components:index:StaticPage", name, comp, opts...)
	if err != nil {
		return nil, err
	}

	bucket, err := s3.NewBucket(ctx, fmt.Sprintf("%s-bucket", name), &s3.BucketArgs{},
		pulumi.Parent(comp))
	if err != nil {
		return nil, err
	}

	bucketWebsite, err := s3.NewBucketWebsiteConfiguration(ctx, fmt.Sprintf("%s-website", name),
		&s3.BucketWebsiteConfigurationArgs{
			Bucket: bucket.Bucket,
			IndexDocument: s3.BucketWebsiteConfigurationIndexDocumentArgs{
				Suffix: pulumi.String("index.html"),
			},
		},
		pulumi.Parent(comp))
	if err != nil {
		return nil, err
	}

	_, err = s3.NewBucketObject(ctx, fmt.Sprintf("%s-index-object", name), &s3.BucketObjectArgs{
		Bucket:      bucket.Bucket,
		Key:         pulumi.String("index.html"),
		Content:     args.IndexContent,
		ContentType: pulumi.String("text/html"),
	}, pulumi.Parent(comp))
	if err != nil {
		return nil, err
	}

	publicAccessBlock, err := s3.NewBucketPublicAccessBlock(ctx, fmt.Sprintf("%s-public-access-block", name),
		&s3.BucketPublicAccessBlockArgs{
			Bucket:          bucket.ID(),
			BlockPublicAcls: pulumi.Bool(false),
		}, pulumi.Parent(comp))
	if err != nil {
		return nil, err
	}

	allowGetObjectPolicy := func(bucketName string) (string, error) {
		policy := map[string]interface{}{
			"Version": "2012-10-17",
			"Statement": []map[string]interface{}{
				{
					"Effect":    "Allow",
					"Principal": "*",
					"Action":    []string{"s3:GetObject"},
					"Resource":  []string{fmt.Sprintf("arn:aws:s3:::%s/*", bucketName)},
				},
			},
		}
		policyJSON, err := json.Marshal(policy)
		if err != nil {
			return "", err
		}
		return string(policyJSON), nil
	}

	_, err = s3.NewBucketPolicy(ctx, fmt.Sprintf("%s-bucket-policy", name), &s3.BucketPolicyArgs{
		Bucket: bucket.ID(),
		Policy: bucket.Bucket.ApplyT(func(bucketName string) (string, error) {
			return allowGetObjectPolicy(bucketName)
		}).(pulumi.StringOutput),
	}, pulumi.Parent(comp), pulumi.DependsOn([]pulumi.Resource{publicAccessBlock}))
	if err != nil {
		return nil, err
	}

	comp.Endpoint = bucketWebsite.WebsiteEndpoint

	return comp, nil
}

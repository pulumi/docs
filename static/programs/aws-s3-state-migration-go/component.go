package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v7/go/aws/s3"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type VersionedBucket struct {
	pulumi.ResourceState

	BucketName pulumi.StringOutput
	BucketID   pulumi.IDOutput
	BucketURN  pulumi.URNOutput
}

func NewVersionedBucket(
	ctx *pulumi.Context,
	name string,
	bucketName string,
	opts ...pulumi.ResourceOption,
) (*VersionedBucket, error) {
	opts = append(opts, pulumi.StateMigrations([]pulumi.StateMigration{
		migrateBucketState,
	}))

	component := &VersionedBucket{}
	if err := ctx.RegisterComponentResource(componentType, name, component, opts...); err != nil {
		return nil, err
	}
	childOpts := []pulumi.ResourceOption{pulumi.Parent(component)}
	tags := pulumi.StringMap{
		"example":    pulumi.String("s3-bucket-state-migration"),
		"managed-by": pulumi.String("pulumi"),
	}
	bucket, err := s3.NewBucket(ctx, name, &s3.BucketArgs{
		Bucket:       pulumi.String(bucketName),
		ForceDestroy: pulumi.Bool(true),
		Tags:         tags,
		Versioning: s3.BucketVersioningTypeArgs{
			Enabled: pulumi.Bool(true),
		},
	}, childOpts...)
	if err != nil {
		return nil, err
	}
	component.BucketName = bucket.Bucket
	component.BucketID = bucket.ID()
	component.BucketURN = bucket.URN()

	if err := ctx.RegisterResourceOutputs(component, pulumi.Map{
		"bucketName": component.BucketName,
	}); err != nil {
		return nil, err
	}
	return component, nil
}

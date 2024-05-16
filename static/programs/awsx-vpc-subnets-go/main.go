package main

import (
	"github.com/pulumi/pulumi-awsx/sdk/v2/go/awsx/ec2"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {

		vpc, err := ec2.NewVpc(ctx, "vpc", &ec2.VpcArgs{
			SubnetSpecs: []ec2.SubnetSpecArgs{
				{
					Type:     ec2.SubnetTypePublic,
					CidrMask: pulumi.IntRef(22),
				},
				{
					Type:     ec2.SubnetTypePrivate,
					CidrMask: pulumi.IntRef(20),
				},
			},
		})
		if err != nil {
			return err
		}

		ctx.Export("vpcId", vpc.VpcId)
		return nil
	})
}

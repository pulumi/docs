package main

import (
	"github.com/pulumi/pulumi-awsx/sdk/v2/go/awsx/ec2"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {

		// Allocate a new VPC with a custom CIDR block.
		vpc, err := ec2.NewVpc(ctx, "vpc", &ec2.VpcArgs{
			CidrBlock: pulumi.StringRef("172.16.8.0/24"),
		})
		if err != nil {
			return err
		}

		ctx.Export("vpcId", vpc.VpcId)
		return nil
	})
}

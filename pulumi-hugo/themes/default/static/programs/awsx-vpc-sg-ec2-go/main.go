package main

import (
	awsec2 "github.com/pulumi/pulumi-aws/sdk/v6/go/aws/ec2"
	"github.com/pulumi/pulumi-awsx/sdk/v2/go/awsx/ec2"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {

		vpc, err := ec2.NewVpc(ctx, "vpc", nil)
		if err != nil {
			return err
		}

		securityGroup, err := awsec2.NewSecurityGroup(ctx, "group", &awsec2.SecurityGroupArgs{
			VpcId: vpc.VpcId,
		})
		if err != nil {
			return err
		}

		ami, err := awsec2.LookupAmi(ctx, &awsec2.LookupAmiArgs{
			Filters: []awsec2.GetAmiFilter{
				{
					Name:   "name",
					Values: []string{"amzn2-ami-hvm-*"},
				},
			},
			Owners:     []string{"amazon"},
			MostRecent: pulumi.BoolRef(true),
		})
		if err != nil {
			return err
		}

		awsec2.NewInstance(ctx, "instance", &awsec2.InstanceArgs{
			Ami:                 pulumi.String(ami.Id),
			InstanceType:        pulumi.String("t2.micro"),
			VpcSecurityGroupIds: pulumi.StringArray{securityGroup.ID()},
			SubnetId:            vpc.PublicSubnetIds.Index(pulumi.Int(0)),
		})
		if err != nil {
			return err
		}

		ctx.Export("vpcId", vpc.VpcId)
		return nil
	})
}

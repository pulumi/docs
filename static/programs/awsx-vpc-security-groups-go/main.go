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

		_, err = awsec2.NewSecurityGroup(ctx, "group", &awsec2.SecurityGroupArgs{
			VpcId: vpc.VpcId,
			Ingress: awsec2.SecurityGroupIngressArray{
				&awsec2.SecurityGroupIngressArgs{
					FromPort: pulumi.Int(22),
					ToPort:   pulumi.Int(22),
					Protocol: pulumi.String("tcp"),
					CidrBlocks: pulumi.StringArray{
						pulumi.String("203.0.113.25/32"),
					},
				},
				&awsec2.SecurityGroupIngressArgs{
					FromPort: pulumi.Int(443),
					ToPort:   pulumi.Int(443),
					Protocol: pulumi.String("tcp"),
					CidrBlocks: pulumi.StringArray{
						pulumi.String("0.0.0.0/0"),
					},
				},
			},
			Egress: awsec2.SecurityGroupEgressArray{
				&awsec2.SecurityGroupEgressArgs{
					FromPort: pulumi.Int(0),
					ToPort:   pulumi.Int(0),
					Protocol: pulumi.String("-1"),
					CidrBlocks: pulumi.StringArray{
						pulumi.String("0.0.0.0/0"),
					},
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

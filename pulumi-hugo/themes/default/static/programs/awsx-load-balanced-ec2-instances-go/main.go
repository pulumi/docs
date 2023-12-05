package main

import (
	"fmt"

	awsec2 "github.com/pulumi/pulumi-aws/sdk/v6/go/aws/ec2"
	"github.com/pulumi/pulumi-awsx/sdk/v2/go/awsx/ec2"
	"github.com/pulumi/pulumi-awsx/sdk/v2/go/awsx/lb"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {

		// Get the default VPC for the current region.
		vpc, err := ec2.NewDefaultVpc(ctx, "default-vpc", nil)
		if err != nil {
			return err
		}

		// Create a security group to allow traffic to and from the virtual machine.
		securityGroup, err := awsec2.NewSecurityGroup(ctx, "web-sg", &awsec2.SecurityGroupArgs{
			VpcId: vpc.VpcId,
			Ingress: awsec2.SecurityGroupIngressArray{
				&awsec2.SecurityGroupIngressArgs{
					Protocol:   pulumi.String("tcp"),
					FromPort:   pulumi.Int(80),
					ToPort:     pulumi.Int(80),
					CidrBlocks: pulumi.StringArray{pulumi.String("0.0.0.0/0")},
				},
			},
			Egress: awsec2.SecurityGroupEgressArray{
				&awsec2.SecurityGroupEgressArgs{
					Protocol:   pulumi.String("-1"),
					FromPort:   pulumi.Int(0),
					ToPort:     pulumi.Int(0),
					CidrBlocks: pulumi.StringArray{pulumi.String("0.0.0.0/0")},
				},
			},
		})
		if err != nil {
			return err
		}

		// Create an ALB in the default VPC listening on port 80.
		alb, err := lb.NewApplicationLoadBalancer(ctx, "lb", &lb.ApplicationLoadBalancerArgs{
			Listener: &lb.ListenerArgs{
				Port: pulumi.Int(80),
			},
			SecurityGroups: pulumi.StringArray{securityGroup.ID()},
		})
		if err != nil {
			return err
		}

		// In each VPC subnet, create an EC2 instance and attach it to the ALB.
		vpc.PublicSubnetIds.ApplyT(func(subnetIds []string) error {
			for i, subnetId := range subnetIds {
				suffix := fmt.Sprintf("web-%d", i)

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

				vm, err := awsec2.NewInstance(ctx, suffix, &awsec2.InstanceArgs{
					Ami:                 pulumi.String(ami.Id),
					InstanceType:        pulumi.String("t2.micro"),
					SubnetId:            pulumi.String(subnetId),
					VpcSecurityGroupIds: alb.LoadBalancer.SecurityGroups(),
					UserData: pulumi.Sprintf(`#!/bin/bash
						echo "Hello World, from Server %d!" > index.html
						nohup python -m SimpleHTTPServer 80 &`, i+1),
				})
				if err != nil {
					return err
				}

				_, err = lb.NewTargetGroupAttachment(ctx, suffix, &lb.TargetGroupAttachmentArgs{
					TargetGroup: alb.DefaultTargetGroup,
					Instance:    vm,
				})
				if err != nil {
					return err
				}
			}

			return nil
		})

		// Export the resulting URL so that it's easy to access.
		ctx.Export("endpoint", alb.LoadBalancer.DnsName())
		return nil
	})
}

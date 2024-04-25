package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/ec2"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Create a VPC.
		vpc, err := ec2.NewVpc(ctx, "vpc", &ec2.VpcArgs{
			CidrBlock: pulumi.String("10.0.0.0/16"),
		})
		if err != nil {
			return err
		}

		// Create an internet gateway.
		gateway, err := ec2.NewInternetGateway(ctx, "gateway", &ec2.InternetGatewayArgs{
			VpcId: vpc.ID(),
		})
		if err != nil {
			return err
		}

		// Create a subnet that automatically assigns new instances a public IP address.
		subnet, err := ec2.NewSubnet(ctx, "subnet", &ec2.SubnetArgs{
			VpcId:               vpc.ID(),
			CidrBlock:           pulumi.String("10.0.1.0/24"),
			MapPublicIpOnLaunch: pulumi.Bool(true),
		})
		if err != nil {
			return err
		}

		// Create a route table.
		routes, err := ec2.NewRouteTable(ctx, "routes", &ec2.RouteTableArgs{
			VpcId: vpc.ID(),
			Routes: ec2.RouteTableRouteArray{
				&ec2.RouteTableRouteArgs{
					CidrBlock: pulumi.String("0.0.0.0/0"),
					GatewayId: gateway.ID(),
				},
			},
		})
		if err != nil {
			return err
		}

		// Associate the route table with the public subnet.
		_, err = ec2.NewRouteTableAssociation(ctx, "route-table-association", &ec2.RouteTableAssociationArgs{
			SubnetId:     subnet.ID(),
			RouteTableId: routes.ID(),
		})
		if err != nil {
			return err
		}

		// Create a security group allowing inbound access over port 80 and outbound access to anywhere.
		securityGroup, err := ec2.NewSecurityGroup(ctx, "security-group", &ec2.SecurityGroupArgs{
			VpcId: vpc.ID(),
			Ingress: ec2.SecurityGroupIngressArray{
				&ec2.SecurityGroupIngressArgs{
					CidrBlocks: pulumi.StringArray{
						pulumi.String("0.0.0.0/0"),
					},
					Protocol: pulumi.String("tcp"),
					FromPort: pulumi.Int(80),
					ToPort:   pulumi.Int(80),
				},
			},
			Egress: ec2.SecurityGroupEgressArray{
				&ec2.SecurityGroupEgressArgs{
					CidrBlocks: pulumi.StringArray{
						pulumi.String("0.0.0.0/0"),
					},
					FromPort: pulumi.Int(0),
					ToPort:   pulumi.Int(0),
					Protocol: pulumi.String("-1"),
				},
			},
		})
		if err != nil {
			return err
		}

		// Find the latest Amazon Linux 2 AMI.
		ami, err := ec2.LookupAmi(ctx, &ec2.LookupAmiArgs{
			Owners:     []string{"amazon"},
			MostRecent: pulumi.BoolRef(true),
			Filters: []ec2.GetAmiFilter{
				{
					Name:   "description",
					Values: []string{"Amazon Linux 2 *"},
				},
			},
		})
		if err != nil {
			return err
		}

		// Create and launch an Amazon Linux EC2 instance into the public subnet.
		instance, err := ec2.NewInstance(ctx, "instance", &ec2.InstanceArgs{
			Ami:                 pulumi.String(ami.Id),
			InstanceType:        pulumi.String("t3.nano"),
			SubnetId:            subnet.ID(),
			VpcSecurityGroupIds: pulumi.StringArray{securityGroup.ID()},
			UserData: pulumi.String(`
				#!/bin/bash
				sudo yum update -y
				sudo yum upgrade -y
				sudo amazon-linux-extras install nginx1 -y
				sudo systemctl enable nginx
				sudo systemctl start nginx;
			`),
		})
		if err != nil {
			return err
		}

		// Export the instance's publicly accessible URL.
		ctx.Export("instanceURL", pulumi.Sprintf("http://%s", instance.PublicIp))
		return nil
	})
}

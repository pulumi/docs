package main

import (
	"encoding/json"
	"os"

	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/ec2"
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/iam"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// IAM Role for EC2 instances
		rolePolicy, err := json.Marshal(map[string]interface{}{
			"Version": "2012-10-17",
			"Statement": []map[string]interface{}{
				{
					"Action":    "sts:AssumeRole",
					"Effect":    "Allow",
					"Principal": map[string]interface{}{"Service": "ec2.amazonaws.com"},
				},
			},
		})
		if err != nil {
			return err
		}

		role, err := iam.NewRole(ctx, "deepSeekRole", &iam.RoleArgs{
			Name:             pulumi.String("deepseek-role"),
			AssumeRolePolicy: pulumi.String(rolePolicy),
		})
		if err != nil {
			return err
		}

		// Attach S3 read-only policy to the IAM Role
		_, err = iam.NewRolePolicyAttachment(ctx, "deepSeekS3Policy", &iam.RolePolicyAttachmentArgs{
			PolicyArn: pulumi.String("arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess"),
			Role:      role.Name,
		})
		if err != nil {
			return err
		}

		// Instance Profile containing the IAM Role
		instanceProfile, err := iam.NewInstanceProfile(ctx, "deepSeekProfile", &iam.InstanceProfileArgs{
			Name: pulumi.String("deepseek-profile"),
			Role: role.Name,
		})
		if err != nil {
			return err
		}

		// Create a VPC
		vpc, err := ec2.NewVpc(ctx, "deepSeekVpc", &ec2.VpcArgs{
			CidrBlock:          pulumi.String("10.0.0.0/16"),
			EnableDnsHostnames: pulumi.Bool(true),
			EnableDnsSupport:   pulumi.Bool(true),
		})
		if err != nil {
			return err
		}

		// Create a subnet
		subnet, err := ec2.NewSubnet(ctx, "deepSeekSubnet", &ec2.SubnetArgs{
			VpcId:               vpc.ID(),
			CidrBlock:           pulumi.String("10.0.48.0/20"),
			AvailabilityZone:    pulumi.String("eu-central-1a"),
			MapPublicIpOnLaunch: pulumi.Bool(true),
		})
		if err != nil {
			return err
		}

		// Create an internet gateway
		internetGateway, err := ec2.NewInternetGateway(ctx, "deepSeekInternetGateway", &ec2.InternetGatewayArgs{
			VpcId: vpc.ID(),
		})
		if err != nil {
			return err
		}

		// Create a route table and route table association
		routeTable, err := ec2.NewRouteTable(ctx, "deepSeekRouteTable", &ec2.RouteTableArgs{
			VpcId: vpc.ID(),
			Routes: ec2.RouteTableRouteArray{
				&ec2.RouteTableRouteArgs{
					CidrBlock: pulumi.String("0.0.0.0/0"),
					GatewayId: internetGateway.ID(),
				},
			},
		})
		if err != nil {
			return err
		}

		_, err = ec2.NewRouteTableAssociation(ctx, "deepSeekRouteTableAssociation", &ec2.RouteTableAssociationArgs{
			SubnetId:     subnet.ID(),
			RouteTableId: routeTable.ID(),
		})
		if err != nil {
			return err
		}

		// Create a security group
		securityGroup, err := ec2.NewSecurityGroup(ctx, "deepSeekSecurityGroup", &ec2.SecurityGroupArgs{
			VpcId: vpc.ID(),
			Egress: ec2.SecurityGroupEgressArray{
				&ec2.SecurityGroupEgressArgs{
					FromPort:   pulumi.Int(0),
					ToPort:     pulumi.Int(0),
					Protocol:   pulumi.String("-1"),
					CidrBlocks: pulumi.StringArray{pulumi.String("0.0.0.0/0")},
				},
			},
			Ingress: ec2.SecurityGroupIngressArray{
				&ec2.SecurityGroupIngressArgs{
					FromPort:   pulumi.Int(22),
					ToPort:     pulumi.Int(22),
					Protocol:   pulumi.String("tcp"),
					CidrBlocks: pulumi.StringArray{pulumi.String("0.0.0.0/0")},
				},
				&ec2.SecurityGroupIngressArgs{
					FromPort:   pulumi.Int(3000),
					ToPort:     pulumi.Int(3000),
					Protocol:   pulumi.String("tcp"),
					CidrBlocks: pulumi.StringArray{pulumi.String("0.0.0.0/0")},
				},
				&ec2.SecurityGroupIngressArgs{
					FromPort:   pulumi.Int(11434),
					ToPort:     pulumi.Int(11434),
					Protocol:   pulumi.String("tcp"),
					CidrBlocks: pulumi.StringArray{pulumi.String("0.0.0.0/0")},
				},
			},
		})
		if err != nil {
			return err
		}

		// Key pair for SSH access
		publicKey, err := os.ReadFile("deepseek.rsa")
		if err != nil {
			return err
		}

		keyPair, err := ec2.NewKeyPair(ctx, "deepSeekKey", &ec2.KeyPairArgs{
			PublicKey: pulumi.String(string(publicKey)),
		})
		if err != nil {
			return err
		}

		// Get the latest Amazon Linux 2 AMI
		mostRecent := true
		ami, err := ec2.LookupAmi(ctx, &ec2.LookupAmiArgs{
			Filters: []ec2.GetAmiFilter{
				{
					Name:   "name",
					Values: []string{"amzn2-ami-hvm-2.0.*-x86_64-gp2"},
				},
				{
					Name:   "architecture",
					Values: []string{"x86_64"},
				},
			},
			Owners:     []string{"137112412989"},
			MostRecent: &mostRecent,
		})
		if err != nil {
			return err
		}

		// Create an EC2 instance
		userData, err := os.ReadFile("cloud-init.yaml")
		if err != nil {
			return err
		}

		instance, err := ec2.NewInstance(ctx, "deepSeekInstance", &ec2.InstanceArgs{
			Ami:          pulumi.String(ami.Id),
			InstanceType: pulumi.String("g4dn.xlarge"),
			KeyName:      keyPair.KeyName,
			RootBlockDevice: &ec2.InstanceRootBlockDeviceArgs{
				VolumeSize: pulumi.Int(100),
				VolumeType: pulumi.String("gp3"),
			},
			SubnetId:            subnet.ID(),
			VpcSecurityGroupIds: pulumi.StringArray{securityGroup.ID()},
			IamInstanceProfile:  instanceProfile.Name,
			UserData:            pulumi.String(string(userData)),
			Tags: pulumi.StringMap{
				"Name": pulumi.String("deepSeek-server"),
			},
		})
		if err != nil {
			return err
		}

		ctx.Export("amiId", pulumi.String(ami.Id))
		ctx.Export("instanceId", instance.ID())
		ctx.Export("instancePublicDns", instance.PublicIp)

		return nil
	})
}

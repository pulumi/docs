package main

import (
	awsec2 "github.com/pulumi/pulumi-aws/sdk/v6/go/aws/ec2"
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/ecs"
	"github.com/pulumi/pulumi-awsx/sdk/v2/go/awsx/ec2"
	awsxecs "github.com/pulumi/pulumi-awsx/sdk/v2/go/awsx/ecs"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {

		vpc, err := ec2.NewVpc(ctx, "vpc", nil)
		if err != nil {
			return err
		}

		securityGroup, err := awsec2.NewSecurityGroup(ctx, "securityGroup", &awsec2.SecurityGroupArgs{
			VpcId: vpc.VpcId,
			Egress: awsec2.SecurityGroupEgressArray{
				&awsec2.SecurityGroupEgressArgs{
					FromPort: pulumi.Int(0),
					ToPort:   pulumi.Int(0),
					Protocol: pulumi.String("-1"),
					CidrBlocks: pulumi.StringArray{
						pulumi.String("0.0.0.0/0"),
					},
					Ipv6CidrBlocks: pulumi.StringArray{
						pulumi.String("::/0"),
					},
				},
			},
		})
		if err != nil {
			return err
		}

		cluster, err := ecs.NewCluster(ctx, "cluster", nil)
		if err != nil {
			return err
		}

		_, err = awsxecs.NewFargateService(ctx, "service", &awsxecs.FargateServiceArgs{
			Cluster: cluster.Arn,
			NetworkConfiguration: &ecs.ServiceNetworkConfigurationArgs{
				Subnets: vpc.PrivateSubnetIds,
				SecurityGroups: pulumi.StringArray{
					securityGroup.ID(),
				},
			},
			DesiredCount: pulumi.Int(2),
			TaskDefinitionArgs: &awsxecs.FargateServiceTaskDefinitionArgs{
				Container: &awsxecs.TaskDefinitionContainerDefinitionArgs{
					Name:      pulumi.String("my-service"),
					Image:     pulumi.String("nginx:latest"),
					Cpu:       pulumi.Int(128),
					Memory:    pulumi.Int(512),
					Essential: pulumi.Bool(true),
				},
			},
		})
		if err != nil {
			return err
		}

		return nil
	})
}

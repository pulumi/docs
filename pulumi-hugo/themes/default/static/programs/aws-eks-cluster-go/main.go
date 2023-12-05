package main

import (
	"github.com/pulumi/pulumi-awsx/sdk/v2/go/awsx/ec2"
	"github.com/pulumi/pulumi-eks/sdk/v2/go/eks"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {

		// Create a VPC for the Kubernetes cluster.
		eksVpc, err := ec2.NewVpc(ctx, "eks-vpc", &ec2.VpcArgs{
			EnableDnsHostnames: pulumi.Bool(true),
			CidrBlock:          pulumi.StringRef("10.0.0.0/16"),
		})
		if err != nil {
			return err
		}

		// Create the EKS cluster itself.
		eksCluster, err := eks.NewCluster(ctx, "eks-cluster", &eks.ClusterArgs{
			VpcId:            eksVpc.VpcId,
			PublicSubnetIds:  eksVpc.PublicSubnetIds,
			PrivateSubnetIds: eksVpc.PrivateSubnetIds,
			InstanceType:     pulumi.String("t3.medium"),
			DesiredCapacity:  pulumi.Int(3),
			MinSize:          pulumi.Int(3),
			MaxSize:          pulumi.Int(6),
		})
		if err != nil {
			return err
		}

		// Export the cluster's kubeconfig.
		ctx.Export("kubeconfig", eksCluster.Kubeconfig)
		return nil
	})
}

package main

import (
	"github.com/pulumi/pulumi-awsx/sdk/v3/go/awsx/ec2"
	"github.com/pulumi/pulumi-eks/sdk/v4/go/eks"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Create a VPC for our cluster.
		vpc, err := ec2.NewVpc(ctx, "vpc", nil)
		if err != nil {
			return err
		}

		// Create an EKS cluster inside of the VPC.
		cluster, err := eks.NewCluster(ctx, "cluster", &eks.ClusterArgs{
			VpcId:                        vpc.VpcId,
			PublicSubnetIds:              vpc.PublicSubnetIds,
			PrivateSubnetIds:             vpc.PrivateSubnetIds,
			NodeAssociatePublicIpAddress: pulumi.BoolRef(false),
		})
		if err != nil {
			return err
		}

		// Export the cluster's kubeconfig.
		ctx.Export("kubeconfig", cluster.Kubeconfig)
		return nil
	})
}

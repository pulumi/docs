package main

import (
	"encoding/json"

	"github.com/pulumi/pulumi-aws/sdk/v7/go/aws/iam"
	"github.com/pulumi/pulumi-eks/sdk/v4/go/eks"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		managedPolicyArns := []string{
			"arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy",
			"arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy",
			"arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly",
		}
		tmpJSON0, err := json.Marshal(map[string]interface{}{
			"Version": "2012-10-17",
			"Statement": []map[string]interface{}{
				map[string]interface{}{
					"Action": "sts:AssumeRole",
					"Effect": "Allow",
					"Sid":    nil,
					"Principal": map[string]interface{}{
						"Service": "ec2.amazonaws.com",
					},
				},
			},
		})
		if err != nil {
			return err
		}
		json0 := string(tmpJSON0)
		assumeRolePolicy := json0
		role1, err := iam.NewRole(ctx, "role1", &iam.RoleArgs{
			AssumeRolePolicy:  pulumi.String(assumeRolePolicy),
			ManagedPolicyArns: pulumi.ToStringArray(managedPolicyArns),
		})
		if err != nil {
			return err
		}
		role2, err := iam.NewRole(ctx, "role2", &iam.RoleArgs{
			AssumeRolePolicy:  pulumi.String(assumeRolePolicy),
			ManagedPolicyArns: pulumi.ToStringArray(managedPolicyArns),
		})
		if err != nil {
			return err
		}
		instanceProfile1, err := iam.NewInstanceProfile(ctx, "instanceProfile1", &iam.InstanceProfileArgs{
			Role: role1.Name,
		})
		if err != nil {
			return err
		}
		instanceProfile2, err := iam.NewInstanceProfile(ctx, "instanceProfile2", &iam.InstanceProfileArgs{
			Role: role2.Name,
		})
		if err != nil {
			return err
		}
		cluster, err := eks.NewCluster(ctx, "cluster", &eks.ClusterArgs{
			SkipDefaultNodeGroup: pulumi.BoolRef(true),
			InstanceRoles:        iam.RoleArray{
				role1,
				role2,
			},
		})
		if err != nil {
			return err
		}
		_, err = eks.NewNodeGroupV2(ctx, "fixedNodeGroup", &eks.NodeGroupV2Args{
			Cluster:         cluster,
			InstanceType:    pulumi.String("t2.medium"),
			DesiredCapacity: pulumi.Int(2),
			MinSize:         pulumi.Int(1),
			MaxSize:         pulumi.Int(3),
			SpotPrice:       pulumi.String("1"),
			Labels: pulumi.StringMap{
				"ondemand": pulumi.String("true"),
			},
			InstanceProfile: instanceProfile1,
		})
		if err != nil {
			return err
		}
		_, err = eks.NewNodeGroupV2(ctx, "spotNodeGroup", &eks.NodeGroupV2Args{
			Cluster:         cluster,
			InstanceType:    pulumi.String("t2.medium"),
			DesiredCapacity: pulumi.Int(1),
			MinSize:         pulumi.Int(1),
			MaxSize:         pulumi.Int(2),
			Labels: pulumi.StringMap{
				"preemptible": pulumi.String("true"),
			},
			InstanceProfile: instanceProfile2,
		})
		if err != nil {
			return err
		}
		ctx.Export("kubeconfig", cluster.Kubeconfig)
		return nil
	})
}

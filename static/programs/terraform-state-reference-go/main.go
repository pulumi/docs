package main

import (
	"github.com/pulumi/pulumi-eks/sdk/v2/go/eks"
	"github.com/pulumi/pulumi-terraform/sdk/v6/go/terraform/state"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		tfState := state.GetLocalReferenceOutput(ctx, state.GetLocalReferenceOutputArgs{
			Path: pulumi.String("../terraform/terraform.tfstate"),
		})

		outputs := tfState.Outputs()

		vpcId := outputs.ApplyT(func(outputs map[string]interface{}) string {
			return outputs["vpc_id"].(string)
		}).(pulumi.StringOutput)

		publicSubnetIds := outputs.ApplyT(func(outputs map[string]interface{}) []string {
			ids := outputs["public_subnet_ids"].([]interface{})
			result := make([]string, len(ids))
			for i, id := range ids {
				result[i] = id.(string)
			}
			return result
		}).(pulumi.StringArrayOutput)

		privateSubnetIds := outputs.ApplyT(func(outputs map[string]interface{}) []string {
			ids := outputs["private_subnet_ids"].([]interface{})
			result := make([]string, len(ids))
			for i, id := range ids {
				result[i] = id.(string)
			}
			return result
		}).(pulumi.StringArrayOutput)

		_, err := eks.NewCluster(ctx, "my-cluster", &eks.ClusterArgs{
			VpcId:            vpcId,
			PublicSubnetIds:  publicSubnetIds,
			PrivateSubnetIds: privateSubnetIds,
		})
		if err != nil {
			return err
		}

		return nil
	})
}

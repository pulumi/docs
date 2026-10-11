package main

import (
	"encoding/json"

	"github.com/pulumi/pulumi-eks/sdk/v4/go/eks"
	k8s "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes"
	k8syaml "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/yaml/v2"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Create an EKS cluster.
		cluster, err := eks.NewCluster(ctx, "my-cluster", nil)
		if err != nil {
			return err
		}

		// Create a Kubernetes provider using the new cluster's Kubeconfig.
		prov, err := k8s.NewProvider(ctx, "my-provider", &k8s.ProviderArgs{
			Kubeconfig: cluster.Kubeconfig.ApplyT(
				func(config interface{}) (string, error) {
					b, err := json.Marshal(config)
					if err != nil {
						return "", err
					}
					return string(b), nil
				}).(pulumi.StringOutput),
		})
		if err != nil {
			return err
		}

		// Create resources from standard Kubernetes guestbook YAML example.
		_, err = k8syaml.NewConfigGroup(ctx, "guestbook", &k8syaml.ConfigGroupArgs{
			Files: pulumi.StringArray{pulumi.String("yaml/*.yaml")},
		}, pulumi.Provider(prov))
		if err != nil {
			return err
		}

		// Export the cluster's kubeconfig.
		ctx.Export("kubeconfig", cluster.Kubeconfig)
		return nil
	})
}

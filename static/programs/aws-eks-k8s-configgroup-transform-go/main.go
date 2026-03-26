package main

import (
	"context"

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

		namespaceName := "guestbook"

		// Create a Kubernetes provider using the new cluster's Kubeconfig.
		prov, err := k8s.NewProvider(ctx, "my-provider", &k8s.ProviderArgs{
			Kubeconfig: cluster.KubeconfigJson,
		})
		if err != nil {
			return err
		}

		_, err = k8syaml.NewConfigGroup(ctx, "guestbook", &k8syaml.ConfigGroupArgs{
			Files: pulumi.StringArray{pulumi.String("yaml/*.yaml")},
		}, pulumi.Provider(prov), pulumi.Transforms([]pulumi.ResourceTransform{
			func(_ context.Context, args *pulumi.ResourceTransformArgs) *pulumi.ResourceTransformResult {
				props := args.Props
				// Make every service private to the cluster.
				if args.Type == "kubernetes:core/v1:Service" {
					if spec, ok := props["spec"].(map[string]interface{}); ok {
						if t, ok := spec["type"].(string); ok && t == "LoadBalancer" {
							spec["type"] = "ClusterIP"
						}
					}
				}
				// Put every resource in the created namespace.
				if meta, ok := props["metadata"].(map[string]interface{}); ok {
					meta["namespace"] = namespaceName
				}
				return &pulumi.ResourceTransformResult{
					Props: props,
					Opts:  args.Opts,
				}
			},
		}))
		return err
	})
}

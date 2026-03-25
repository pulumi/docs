package main

import (
	"context"

	"github.com/pulumi/pulumi-eks/sdk/v4/go/eks"
	k8s "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes"
	k8syaml "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/yaml/v2"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/common/resource"
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

		guestbook, err := k8syaml.NewConfigGroup(ctx, "guestbook", &k8syaml.ConfigGroupArgs{
			Files: pulumi.StringArray{pulumi.String("yaml/*.yaml")},
		}, pulumi.Provider(prov), pulumi.Transforms([]pulumi.ResourceTransform{
			func(ctx context.Context, args *pulumi.ResourceTransformArgs) *pulumi.ResourceTransformResult {
				props := args.Props.ObjectValue()
				// Make every service private to the cluster.
				if args.Type == "kubernetes:core/v1:Service" {
					if spec, ok := props["spec"]; ok {
						specMap := spec.ObjectValue()
						if specMap["type"].StringValue() == "LoadBalancer" {
							specMap["type"] = resource.NewStringProperty("ClusterIP")
							props["spec"] = resource.NewObjectProperty(specMap)
						}
					}
				}
				// Put every resource in the created namespace.
				meta := props["metadata"].ObjectValue()
				meta["namespace"] = resource.NewStringProperty(namespaceName)
				props["metadata"] = resource.NewObjectProperty(meta)
				return &pulumi.ResourceTransformResult{
					Props: resource.NewObjectProperty(props),
					Opts:  args.Opts,
				}
			},
		}))
		_ = guestbook
		return err
	})
}

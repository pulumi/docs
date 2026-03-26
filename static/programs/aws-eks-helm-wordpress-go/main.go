package main

import (
	"github.com/pulumi/pulumi-eks/sdk/v4/go/eks"
	"github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes"
	helmv3 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/helm/v3"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		cluster, err := eks.NewCluster(ctx, "cluster", nil)
		if err != nil {
			return err
		}
		eksProvider, err := kubernetes.NewProvider(ctx, "eks-provider", &kubernetes.ProviderArgs{
			Kubeconfig: cluster.KubeconfigJson,
		})
		if err != nil {
			return err
		}
		_, err = helmv3.NewRelease(ctx, "wordpress", &helmv3.ReleaseArgs{
			RepositoryOpts: &helmv3.RepositoryOptsArgs{
				Repo: pulumi.String("https://charts.bitnami.com/bitnami"),
			},
			Chart: pulumi.String("wordpress"),
			Values: pulumi.Map{
				"wordpressBlogName": pulumi.String("My Cool Kubernetes Blog!"),
			},
		}, pulumi.Provider(eksProvider))
		if err != nil {
			return err
		}
		ctx.Export("kubeconfig", cluster.Kubeconfig)
		return nil
	})
}

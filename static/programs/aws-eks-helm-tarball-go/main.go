package main

import (
	helmv3 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/helm/v3"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		_, err := helmv3.NewRelease(ctx, "helm", &helmv3.ReleaseArgs{
			Chart: pulumi.String("https://charts.bitnami.com/bitnami/wordpress-15.2.17.tgz"),
		})
		if err != nil {
			return err
		}
		return nil
	})
}

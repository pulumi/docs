package main

import (
	corev1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/core/v1"
	helmv3 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/helm/v3"
	metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/meta/v1"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		cfg := config.New(ctx, "")
		k8sNamespace, err := cfg.Try("k8sNamespace")
		if err != nil {
			k8sNamespace = "nginx-ingress"
		}
		appLabels := pulumi.StringMap{
			"app": pulumi.String("nginx-ingress"),
		}

		// Create a new namespace (user supplies the name of the namespace)
		ingressNs, err := corev1.NewNamespace(ctx, "ingressns", &corev1.NamespaceArgs{
			Metadata: &metav1.ObjectMetaArgs{
				Labels: pulumi.StringMap(appLabels),
				Name:   pulumi.String(k8sNamespace),
			},
		})
		if err != nil {
			return err
		}

		// Use Helm to install the Nginx ingress controller
		ingresscontroller, err := helmv3.NewRelease(ctx, "ingresscontroller", &helmv3.ReleaseArgs{
			Chart:     pulumi.String("nginx-ingress"),
			Namespace: ingressNs.Metadata.Name(),
			RepositoryOpts: &helmv3.RepositoryOptsArgs{
				Repo: pulumi.String("https://helm.nginx.com/stable"),
			},
			SkipCrds: pulumi.Bool(true),
			Values: pulumi.Map{
				"controller": pulumi.Map{
					"enableCustomResources": pulumi.Bool(false),
					"appprotect": pulumi.Map{
						"enable": pulumi.Bool(false),
					},
					"appprotectdos": pulumi.Map{
						"enable": pulumi.Bool(false),
					},
					"service": pulumi.Map{
						"extraLabels": appLabels,
					},
				},
			},
			Version: pulumi.String("0.14.1"),
		})
		if err != nil {
			return err
		}

		// Export some values for use elsewhere
		ctx.Export("name", ingresscontroller.Name)
		return nil
	})
}

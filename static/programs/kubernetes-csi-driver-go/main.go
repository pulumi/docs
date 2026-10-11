package main

import (
	k8s "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes"
	"github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/apiextensions"
	appv1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/apps/v1"
	corev1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/core/v1"
	chartv4 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/helm/v4"
	metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/meta/v1"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		secretsStoreCsiDriver, err := chartv4.NewChart(ctx, "secrets-store-csi-driver", &chartv4.ChartArgs{
			Chart:     pulumi.String("secrets-store-csi-driver"),
			Namespace: pulumi.String("kube-system"),
			RepositoryOpts: chartv4.RepositoryOptsArgs{
				Repo: pulumi.String("https://kubernetes-sigs.github.io/secrets-store-csi-driver/charts"),
			},
			Values: pulumi.Map{
				"nodeSelector": pulumi.Map{
					"kubernetes.io/os": pulumi.String("linux"),
				},
			},
		})
		if err != nil {
			return err
		}

		secretsStoreCsiPulumiEscProvider, err := chartv4.NewChart(ctx, "secrets-store-csi-pulumi-esc-provider", &chartv4.ChartArgs{
			Chart:     pulumi.String("oci://ghcr.io/pulumi/helm-charts/pulumi-esc-csi-provider"),
			Namespace: pulumi.String("kube-system"),
			Values: pulumi.Map{
				"nodeSelector": pulumi.Map{
					"kubernetes.io/os": pulumi.String("linux"),
				},
			},
		}, pulumi.DependsOn([]pulumi.Resource{secretsStoreCsiDriver}))
		if err != nil {
			return err
		}

		pulumiPAT := config.Get(ctx, "pulumi-pat")

		mySecret, err := corev1.NewSecret(ctx, "my-secret", &corev1.SecretArgs{
			Metadata: &metav1.ObjectMetaArgs{
				Namespace: pulumi.String("default"),
				Name:      pulumi.String("pulumi-access-token"),
			},
			StringData: pulumi.StringMap{
				"pulumi-access-token": pulumi.String(pulumiPAT),
			},
			Type: pulumi.String("Opaque"),
		}, pulumi.DependsOn([]pulumi.Resource{secretsStoreCsiPulumiEscProvider}))
		if err != nil {
			return err
		}

		secretProviderClass, err := apiextensions.NewCustomResource(ctx, "example-provider-pulumi-esc", &apiextensions.CustomResourceArgs{
			ApiVersion: pulumi.String("secrets-store.csi.x-k8s.io/v1"),
			Kind:       pulumi.String("SecretProviderClass"),
			Metadata: &metav1.ObjectMetaArgs{
				Name:      pulumi.String("example-provider-pulumi-esc"),
				Namespace: pulumi.String("default"),
			},
			OtherFields: k8s.UntypedArgs{
				"provider": pulumi.String("pulumi"),
				"parameters": pulumi.Map{
					"apiUrl":              pulumi.String("https://api.pulumi.com/api/esc"),
					"organization":        pulumi.String("dirien"),
					"project":             pulumi.String("esc-secrets-store-csi-driver-demo"),
					"environment":         pulumi.String("csi-secrets-store-app"),
					"authSecretName":      mySecret.Metadata.Name().Elem(),
					"authSecretNamespace": mySecret.Metadata.Namespace().Elem(),
					"secrets": pulumi.String(`- secretPath: "/"
  fileName: "hello"
  secretKey: "app.hello"
`),
				},
			},
		}, pulumi.DependsOn([]pulumi.Resource{secretsStoreCsiPulumiEscProvider}))
		if err != nil {
			return err
		}

		deployment, err := appv1.NewDeployment(ctx, "example-provider-pulumi-esc", &appv1.DeploymentArgs{
			Metadata: &metav1.ObjectMetaArgs{
				Name:      pulumi.String("example-provider-pulumi-esc"),
				Namespace: pulumi.String("default"),
				Labels: pulumi.StringMap{
					"app": pulumi.String("example-provider-pulumi-esc"),
				},
			},
			Spec: &appv1.DeploymentSpecArgs{
				Replicas: pulumi.Int(1),
				Selector: &metav1.LabelSelectorArgs{
					MatchLabels: pulumi.StringMap{
						"app": pulumi.String("example-provider-pulumi-esc"),
					},
				},
				Template: &corev1.PodTemplateSpecArgs{
					Metadata: &metav1.ObjectMetaArgs{
						Labels: pulumi.StringMap{
							"app": pulumi.String("example-provider-pulumi-esc"),
						},
					},
					Spec: &corev1.PodSpecArgs{
						Containers: corev1.ContainerArray{
							&corev1.ContainerArgs{
								Name:  pulumi.String("client"),
								Image: pulumi.String("busybox:latest"),
								Command: pulumi.StringArray{
									pulumi.String("sh"),
									pulumi.String("-c"),
								},
								Args: pulumi.StringArray{
									pulumi.String(`set -eux
                            ls /run/secrets
                            find /run/secrets/ -mindepth 1 -maxdepth 1 -not -name '.*' | xargs -t -I {} sh -c 'echo "$(cat "{}")"'
                            tail -f /dev/null`),
								},
								VolumeMounts: &corev1.VolumeMountArray{
									&corev1.VolumeMountArgs{
										Name:      pulumi.String("data"),
										MountPath: pulumi.String("/run/secrets"),
									},
								},
							},
						},
						Volumes: &corev1.VolumeArray{
							&corev1.VolumeArgs{
								Name: pulumi.String("data"),
								Csi: corev1.CSIVolumeSourceArgs{
									Driver:   pulumi.String("secrets-store.csi.k8s.io"),
									ReadOnly: pulumi.Bool(true),
									VolumeAttributes: pulumi.StringMap{
										"secretProviderClass": secretProviderClass.Metadata.Name().Elem(),
									},
								},
							},
						},
					},
				},
			},
		}, pulumi.DependsOn([]pulumi.Resource{secretProviderClass}))
		if err != nil {
			return err
		}

		ctx.Export("deploymentName", deployment.Metadata.Name())

		return nil
	})
}

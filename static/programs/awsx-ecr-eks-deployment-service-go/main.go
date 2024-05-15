package main

import (
	"github.com/pulumi/pulumi-awsx/sdk/v2/go/awsx/ecr"
	"github.com/pulumi/pulumi-eks/sdk/v2/go/eks"
	"github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes"
	appsv1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/apps/v1"
	corev1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/core/v1"
	metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/meta/v1"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		appName := "my-app"

		repository, err := ecr.NewRepository(ctx, "repository", &ecr.RepositoryArgs{
			ForceDelete: pulumi.Bool(true),
		})
		if err != nil {
			return err
		}

		image, err := ecr.NewImage(ctx, "image", &ecr.ImageArgs{
			RepositoryUrl: repository.Url,
			Context:       pulumi.String("./app"),
			Platform:      pulumi.String("linux/amd64"),
		})
		if err != nil {
			return err
		}

		cluster, err := eks.NewCluster(ctx, "cluster", nil)
		if err != nil {
			return err
		}

		clusterProvider, err := kubernetes.NewProvider(ctx, "clusterProvider", &kubernetes.ProviderArgs{
			Kubeconfig:            cluster.KubeconfigJson,
			EnableServerSideApply: pulumi.Bool(true),
		})
		if err != nil {
			return err
		}

		_, err = appsv1.NewDeployment(ctx, "deployment", &appsv1.DeploymentArgs{
			Metadata: &metav1.ObjectMetaArgs{
				Labels: pulumi.StringMap{
					"appClass": pulumi.String(appName),
				},
			},
			Spec: &appsv1.DeploymentSpecArgs{
				Replicas: pulumi.Int(2),
				Selector: &metav1.LabelSelectorArgs{
					MatchLabels: pulumi.StringMap{
						"appClass": pulumi.String(appName),
					},
				},
				Template: &corev1.PodTemplateSpecArgs{
					Metadata: &metav1.ObjectMetaArgs{
						Labels: pulumi.StringMap{
							"appClass": pulumi.String(appName),
						},
					},
					Spec: &corev1.PodSpecArgs{
						Containers: corev1.ContainerArray{
							&corev1.ContainerArgs{
								Name:  pulumi.String(appName),
								Image: image.ImageUri,
								Ports: corev1.ContainerPortArray{
									&corev1.ContainerPortArgs{
										Name:          pulumi.String("http"),
										ContainerPort: pulumi.Int(80),
									},
								},
							},
						},
					},
				},
			},
		}, pulumi.Provider(clusterProvider))
		if err != nil {
			return err
		}

		service, err := corev1.NewService(ctx, "service", &corev1.ServiceArgs{
			Metadata: &metav1.ObjectMetaArgs{
				Labels: pulumi.StringMap{
					"appClass": pulumi.String(appName),
				},
			},
			Spec: &corev1.ServiceSpecArgs{
				Type: pulumi.String("LoadBalancer"),
				Selector: pulumi.StringMap{
					"appClass": pulumi.String(appName),
				},
				Ports: corev1.ServicePortArray{
					&corev1.ServicePortArgs{
						Port:       pulumi.Int(80),
						TargetPort: pulumi.Any("http"),
					},
				},
			},
		}, pulumi.Provider(clusterProvider))
		if err != nil {
			return err
		}

		hostname := service.Status.LoadBalancer().Ingress().Index(pulumi.Int(0)).Hostname().Elem()
		ctx.Export("url", pulumi.Sprintf("http://%s", hostname))

		return nil
	})
}

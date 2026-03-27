package main

import (
	"github.com/pulumi/pulumi-eks/sdk/v4/go/eks"
	"github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes"
	appsv1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/apps/v1"
	corev1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/core/v1"
	metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/meta/v1"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Create an EKS cluster with the default configuration.
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
		// Deploy a small canary service (NGINX), to test that the cluster is working.
		_, err = appsv1.NewDeployment(ctx, "my-deployment", &appsv1.DeploymentArgs{
			Metadata: &metav1.ObjectMetaArgs{
				Labels: pulumi.StringMap{
					"appClass": pulumi.String("my-deployment"),
				},
			},
			Spec: &appsv1.DeploymentSpecArgs{
				Replicas: pulumi.Int(2),
				Selector: &metav1.LabelSelectorArgs{
					MatchLabels: pulumi.StringMap{
						"appClass": pulumi.String("my-deployment"),
					},
				},
				Template: &corev1.PodTemplateSpecArgs{
					Metadata: &metav1.ObjectMetaArgs{
						Labels: pulumi.StringMap{
							"appClass": pulumi.String("my-deployment"),
						},
					},
					Spec: &corev1.PodSpecArgs{
						Containers: corev1.ContainerArray{
							&corev1.ContainerArgs{
								Name:  pulumi.String("my-deployment"),
								Image: pulumi.String("nginx"),
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
		}, pulumi.Provider(eksProvider))
		if err != nil {
			return err
		}
		myService, err := corev1.NewService(ctx, "my-service", &corev1.ServiceArgs{
			Metadata: &metav1.ObjectMetaArgs{
				Labels: pulumi.StringMap{
					"appClass": pulumi.String("my-deployment"),
				},
			},
			Spec: &corev1.ServiceSpecArgs{
				Type: pulumi.String("LoadBalancer"),
				Ports: corev1.ServicePortArray{
					&corev1.ServicePortArgs{
						Port:       pulumi.Int(80),
						TargetPort: pulumi.Any("http"),
					},
				},
				Selector: pulumi.StringMap{
					"appClass": pulumi.String("my-deployment"),
				},
			},
		}, pulumi.Provider(eksProvider))
		if err != nil {
			return err
		}
		// Export the cluster's kubeconfig.
		ctx.Export("kubeconfig", cluster.Kubeconfig)
		// Export the URL for the load balanced service.
		ctx.Export("url", myService.Status.ApplyT(func(status interface{}) (string, error) {
			return *status.(*corev1.ServiceStatus).LoadBalancer.Ingress[0].Hostname, nil
		}).(pulumi.StringOutput))
		return nil
	})
}

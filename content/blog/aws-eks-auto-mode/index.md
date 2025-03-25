---
title: "Getting Started with Amazon EKS Auto Mode in Pulumi"
date: 2024-12-16T23:26:21+01:00
draft: false
meta_desc: "Learn how to use Amazon EKS Auto Mode with Pulumi to streamline your Kubernetes
  cluster management"
meta_image: meta.png
authors:
  - florian-stadler
tags:
  - aws
  - eks
  - kubernetes
search:
  keywords:
    - mode
    - eks
    - auto
    - amazon
    - kubernetes
    - metadata
    - getting
---

AWS recently announced [Amazon EKS Auto Mode](https://aws.amazon.com/eks/auto-mode/), a significant enhancement to Amazon EKS that streamlines cluster management by automating infrastructure decisions and operations. Today, we are excited to announce that Pulumi fully supports EKS Auto Mode across our AWS provider ecosystem, enabling you to leverage this powerful feature through infrastructure as code.

<!--more-->

## What is EKS Auto Mode?

EKS Auto Mode extends AWS management beyond the Kubernetes control plane to the underlying infrastructure that powers your workloads. While traditional EKS requires you to make numerous infrastructure decisions and maintain various components, Auto Mode simplifies this by automating these choices based on AWS's operational expertise.

Instead of manually configuring and managing cluster add-ons, node groups, and infrastructure components, Auto Mode handles:

- **Compute Management**: Automatically provisions and scales EC2 instances based on your workload demands while selecting optimal instance types and sizes. It also handles node lifecycle management, including OS updates and security patches.
- **Storage Automation**: Eliminates the need to manually set up and configure the EBS CSI driver for block storage. Auto Mode manages volume provisioning, attachment, and cleanup for your persistent workloads.
- **Networking Simplification**: Automatically configures and manages core networking components like Load Balancers.

This significantly reduces the operational overhead of running Kubernetes clusters. Instead of spending time on infrastructure decisions and maintenance, teams can now focus on their applications. For example, deploying a stateful application with load balancing no longer requires setting up and maintaining multiple add-ons and configurations - Auto Mode handles this automatically while following AWS best practices.

Common tasks that previously required significant expertise and time are now managed by AWS, making it simpler to run production-grade Kubernetes workloads. This includes:

- Setting up and maintaining cluster autoscaling
- Configuring and updating networking plugins
- Managing storage drivers and volume provisioning
- Handling node updates and security patches
- Optimizing instance selection and placement

## Pulumi Support for EKS Auto Mode

We have added EKS Auto Mode support across our AWS provider ecosystem:

- [Pulumi AWS Provider](/registry/packages/aws/) (v6.63.0+)
- [Pulumi AWS Cloud Control Provider](/registry/packages/aws-native/) (previously known as Pulumi AWS Native) (v1.13.0+)
- [Pulumi EKS Provider](/registry/packages/eks/) (v3.5.0+)

## Creating an EKS Auto Mode Cluster

Let's explore how to leverage EKS Auto Mode with Pulumi by deploying an example.
You can enable EKS Auto Mode by setting `autoMode.enabled` to true.

First, we'll create a new EKS cluster with Auto Mode enabled. This requires properly configured networking and authentication settings:

- VPC subnets are tagged appropriately for EKS Auto Mode load balancer discovery
- Authentication Mode supports Access Entries (`Api` or `ApiAndConfigMap` mode) as required by EKS Auto Mode
- Default node groups and security groups are skipped as Auto Mode manages these

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as awsx from "@pulumi/awsx";
import * as eks from "@pulumi/eks";
import * as k8s from "@pulumi/kubernetes";
import { SubnetType } from "@pulumi/awsx/ec2";

const config = new pulumi.Config();
const clusterName = config.require("clusterName");

const eksVpc = new awsx.ec2.Vpc("eks-auto-mode", {
    enableDnsHostnames: true,
    cidrBlock: "10.0.0.0/16",
    subnetSpecs: [
        // Necessary tags for EKS Auto Mode to identify the subnets for the load balancers.
        // See: https://kubernetes-sigs.github.io/aws-load-balancer-controller/v2.1/deploy/subnet_discovery/
        {type: SubnetType.Public, tags: {[`kubernetes.io/cluster/${clusterName}`]: "shared", "kubernetes.io/role/elb": "1"}},
        {type: SubnetType.Private, tags: {[`kubernetes.io/cluster/${clusterName}`]: "shared", "kubernetes.io/role/internal-elb": "1"}},
    ],
    subnetStrategy: "Auto"
});

const cluster = new eks.Cluster("eks-auto-mode", {
    name: clusterName,
    // EKS Auto Mode requires Access Entries, use either the `Api` or `ApiAndConfigMap` authentication mode.
    authenticationMode: eks.AuthenticationMode.Api,
    vpcId: eksVpc.vpcId,
    publicSubnetIds: eksVpc.publicSubnetIds,
    privateSubnetIds: eksVpc.privateSubnetIds,
    // Enables compute, storage and load balancing for the cluster.
    autoMode: {
        enabled: true,
    }
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_awsx as awsx
import pulumi_eks as eks
import pulumi_kubernetes as kubernetes

eks_vpc = awsx.ec2.Vpc("eksVpc",
    enable_dns_hostnames=True,
    cidr_block="10.0.0.0/16",
    # Necessary tags for EKS Auto Mode to identify the subnets for the load balancers.
    # See: https://kubernetes-sigs.github.io/aws-load-balancer-controller/v2.1/deploy/subnet_discovery/
    subnet_specs=[
        {
            "type": awsx.ec2.SubnetType.PUBLIC,
            "tags": {
                "kubernetes_io_cluster_eks_auto_mode_demo": "shared",
                "kubernetes_io_role_elb": "1",
            },
        },
        {
            "type": awsx.ec2.SubnetType.PRIVATE,
            "tags": {
                "kubernetes_io_cluster_eks_auto_mode_demo": "shared",
                "kubernetes_io_role_internal_elb": "1",
            },
        },
    ],
    subnet_strategy=awsx.ec2.SubnetAllocationStrategy.AUTO)
cluster = eks.Cluster("cluster",
    name="eks-auto-mode-demo",
    # EKS Auto Mode requires Access Entries, use either the `Api` or `ApiAndConfigMap` authentication mode.
    authentication_mode=eks.AuthenticationMode.API,
    vpc_id=eks_vpc.vpc_id,
    public_subnet_ids=eks_vpc.public_subnet_ids,
    private_subnet_ids=eks_vpc.private_subnet_ids,
    # Enables compute, storage and load balancing for the cluster.
    auto_mode={
        "enabled": True,
    })
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-awsx/sdk/v2/go/awsx/ec2"
	"github.com/pulumi/pulumi-eks/sdk/v3/go/eks"
	"github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes"
	appsv1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/apps/v1"
	corev1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/core/v1"
	metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/meta/v1"
	networkingv1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/networking/v1"
	storagev1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/storage/v1"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		eksVpc, err := ec2.NewVpc(ctx, "eksVpc", &ec2.VpcArgs{
			EnableDnsHostnames: pulumi.Bool(true),
			CidrBlock:          "10.0.0.0/16",
            // Necessary tags for EKS Auto Mode to identify the subnets for the load balancers.
            // See: https://kubernetes-sigs.github.io/aws-load-balancer-controller/v2.1/deploy/subnet_discovery/
			SubnetSpecs: []ec2.SubnetSpecArgs{
				{
					Type: ec2.SubnetTypePublic,
					Tags: {
						"kubernetes.io/cluster/eks-auto-mode-demo": pulumi.String("shared"),
						"kubernetes.io/role/elb":                   pulumi.String("1"),
					},
				},
				{
					Type: ec2.SubnetTypePrivate,
					Tags: {
						"kubernetes.io/cluster/eks-auto-mode-demo": pulumi.String("shared"),
						"kubernetes.io/role/internal-elb":          pulumi.String("1"),
					},
				},
			},
			SubnetStrategy: ec2.SubnetAllocationStrategyAuto,
		})
		if err != nil {
			return err
		}
		cluster, err := eks.NewCluster(ctx, "cluster", &eks.ClusterArgs{
			Name:                      pulumi.String("eks-auto-mode-demo"),
            // EKS Auto Mode requires Access Entries, use either the `Api` or `ApiAndConfigMap` authentication mode.
			AuthenticationMode:        eks.AuthenticationModeApi,
			VpcId:                     eksVpc.VpcId,
			PublicSubnetIds:           eksVpc.PublicSubnetIds,
			PrivateSubnetIds:          eksVpc.PrivateSubnetIds,
            // Enables compute, storage and load balancing for the cluster.
			AutoMode: &eks.AutoModeOptionsArgs{
				Enabled: true,
			},
		})
		if err != nil {
			return err
		}
        return nil
	})
}

```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using System.Linq;
using Pulumi;
using Awsx = Pulumi.Awsx;
using Eks = Pulumi.Eks;
using Kubernetes = Pulumi.Kubernetes;

return await Deployment.RunAsync(() =>
{
    var eksVpc = new Awsx.Ec2.Vpc("eksVpc", new()
    {
        EnableDnsHostnames = true,
        CidrBlock = "10.0.0.0/16",
        // Necessary tags for EKS Auto Mode to identify the subnets for the load balancers.
        // See: https://kubernetes-sigs.github.io/aws-load-balancer-controller/v2.1/deploy/subnet_discovery/
        SubnetSpecs = new()
        {
            new Awsx.Ec2.Inputs.SubnetSpecArgs
            {
                Type = Awsx.Ec2.SubnetType.Public,
                Tags =
                {
                    { "kubernetes.io/cluster/eks-auto-mode-demo", "shared" },
                    { "kubernetes.io/role/elb", "1" },
                },
            },
            new Awsx.Ec2.Inputs.SubnetSpecArgs
            {
                Type = Awsx.Ec2.SubnetType.Private,
                Tags =
                {
                    { "kubernetes.io/cluster/eks-auto-mode-demo", "shared" },
                    { "kubernetes.io/role/internal-elb", "1" },
                },
            },
        },
        SubnetStrategy = Awsx.Ec2.SubnetAllocationStrategy.Auto,
    });

    var cluster = new Eks.Cluster("cluster", new()
    {
        Name = "eks-auto-mode-demo",
        // EKS Auto Mode requires Access Entries, use either the `Api` or `ApiAndConfigMap` authentication mode.
        AuthenticationMode = Eks.AuthenticationMode.Api,
        VpcId = eksVpc.VpcId,
        PublicSubnetIds = eksVpc.PublicSubnetIds,
        PrivateSubnetIds = eksVpc.PrivateSubnetIds,
        // Enables compute, storage and load balancing for the cluster.
        AutoMode = new Eks.Inputs.AutoModeOptionsArgs
        {
            Enabled = true,
        },
    });
});


```

{{% /choosable %}}

{{% choosable language java %}}

```java
import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.pulumi.awsx.ec2.Vpc;
import com.pulumi.awsx.ec2.VpcArgs;
import com.pulumi.awsx.ec2.inputs.SubnetSpecArgs;
import com.pulumi.eks.Cluster;
import com.pulumi.eks.ClusterArgs;
import com.pulumi.eks.inputs.AutoModeOptionsArgs;
import com.pulumi.resources.CustomResourceOptions;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        var eksVpc = new Vpc("eksVpc", VpcArgs.builder()
            .enableDnsHostnames(true)
            .cidrBlock("10.0.0.0/16")
            // Necessary tags for EKS Auto Mode to identify the subnets for the load balancers.
            // See: https://kubernetes-sigs.github.io/aws-load-balancer-controller/v2.1/deploy/subnet_discovery/
            .subnetSpecs(
                SubnetSpecArgs.builder()
                    .type("Public")
                    .tags(Map.ofEntries(
                        Map.entry("kubernetes.io/cluster/eks-auto-mode-demo", "shared"),
                        Map.entry("kubernetes.io/role/elb", "1")
                    ))
                    .build(),
                SubnetSpecArgs.builder()
                    .type("Private")
                    .tags(Map.ofEntries(
                        Map.entry("kubernetes.io/cluster/eks-auto-mode-demo", "shared"),
                        Map.entry("kubernetes.io/role/internal-elb", "1")
                    ))
                    .build())
            .subnetStrategy("Auto")
            .build());

        var cluster = new Cluster("cluster", ClusterArgs.builder()
            .name("eks-auto-mode-demo")
            // EKS Auto Mode requires Access Entries, use either the `Api` or `ApiAndConfigMap` authentication mode.
            .authenticationMode("API")
            .vpcId(eksVpc.vpcId())
            .publicSubnetIds(eksVpc.publicSubnetIds())
            .privateSubnetIds(eksVpc.privateSubnetIds())
            // Enables compute, storage and load balancing for the cluster.
            .autoMode(AutoModeOptionsArgs.builder()
                .enabled(true)
                .build())
            .build());
    }
}

```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
name: eks-auto-mode-demo
description: A demo of EKS Auto Mode
runtime: yaml
resources:
  eksVpc:
    type: awsx:ec2:Vpc
    properties:
      enableDnsHostnames: true
      cidrBlock: "10.0.0.0/16"
      # Necessary tags for EKS Auto Mode to identify the subnets for the load balancers.
      # See: https://kubernetes-sigs.github.io/aws-load-balancer-controller/v2.1/deploy/subnet_discovery/
      subnetSpecs:
        - type: "Public"
          tags:
            kubernetes.io/cluster/eks-auto-mode-demo: shared
            kubernetes.io/role/elb: "1"
        - type: "Private"
          tags:
            kubernetes.io/cluster/eks-auto-mode-demo: shared
            kubernetes.io/role/internal-elb: "1"
      subnetStrategy: "Auto"
  cluster:
    type: eks:Cluster
    properties:
      name: eks-auto-mode-demo
      # EKS Auto Mode requires Access Entries, use either the `Api` or `ApiAndConfigMap` authentication mode.
      authenticationMode: API
      vpcId: ${eksVpc.vpcId}
      publicSubnetIds: ${eksVpc.publicSubnetIds}
      privateSubnetIds: ${eksVpc.privateSubnetIds}
      # Enables compute, storage and load balancing for the cluster.
      autoMode:
        enabled: true
```

{{% /choosable %}}

{{< /chooser >}}

## Deploying a Load-Balanced Application

Now that we have provisioned an EKS cluster with Auto Mode enabled, let's deploy a web application fronted by an Application Load Balancer.
EKS Auto Mode will automatically provision appropriately sized nodes for your workload, set up the Application Load Balancer according
to the Ingress configuration, and manage ongoing maintenance and updates.

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
//...
const appName = "nginx";
const ns = new k8s.core.v1.Namespace(appName, {
    metadata: { name: appName },
}, { provider: cluster.provider });

const configMap = new k8s.core.v1.ConfigMap(appName, {
    metadata: {
        namespace: ns.metadata.name,
    },
    data: {
        "index.html": "<html><body><h1>Hello, Pulumi!</h1></body></html>",
    },
}, { provider: cluster.provider });

const deployment = new k8s.apps.v1.Deployment(appName, {
    metadata: {
        namespace: ns.metadata.name
    },
    spec: {
        selector: { matchLabels: { app: appName } },
        replicas: 3,
        template: {
            metadata: { labels: { app: appName } },
            spec: {
                containers: [{
                    name: appName,
                    image: appName,
                    ports: [{ containerPort: 80 }],
                    volumeMounts: [{ name: "nginx-index", mountPath: "/usr/share/nginx/html" }],
                }],
                volumes: [{
                    name: "nginx-index",
                    configMap: { name: configMap.metadata.name },
                }],
            },
        },
    },
}, { provider: cluster.provider });

const service = new k8s.core.v1.Service(appName, {
    metadata: {
        name: appName,
        namespace: ns.metadata.name
    },
    spec: {
        selector: { app: appName },
        ports: [{ port: 80, targetPort: 80 }],
    },
}, { provider: cluster.provider, dependsOn: [deployment] });

const ingressClass = new k8s.networking.v1.IngressClass("alb", {
    metadata: {
        namespace: ns.metadata.name,
        labels: {
            "app.kubernetes.io/name": "LoadBalancerController",
        },
        name: "alb",
    },
    spec: {
        controller: "eks.amazonaws.com/alb",
    }
}, { provider: cluster.provider });

const ingress = new k8s.networking.v1.Ingress(appName, {
    metadata: {
        namespace: ns.metadata.name,
        // Annotations for EKS Auto Mode to identify the Ingress as internet-facing and target-type as IP.
        annotations: {
            "alb.ingress.kubernetes.io/scheme": "internet-facing",
            "alb.ingress.kubernetes.io/target-type": "ip",
        }
    },
    spec: {
        ingressClassName: ingressClass.metadata.name,
        rules: [{
            http: {
                paths: [{
                    path: "/",
                    pathType: "Prefix",
                    backend: {
                        service: {
                            name: service.metadata.name,
                            port: {
                                number: 80,
                            },
                        },
                    },
                }],
            },
        }],
    }
}, { provider: cluster.provider });

export const url = ingress.status.apply(status => status?.loadBalancer?.ingress?.[0]?.hostname);
```

{{% /choosable %}}

{{% choosable language python %}}

```python
# ...
k8s_provider = kubernetes.Provider("k8sProvider", kubeconfig=cluster.kubeconfig)
ns = kubernetes.core.v1.Namespace("ns", metadata={
    "name": "nginx",
},
opts = pulumi.ResourceOptions(provider=k8s_provider))
index_content = kubernetes.core.v1.ConfigMap("index-content",
    metadata={
        "namespace": ns.metadata.name,
    },
    data={
        "index.html": "<html><body><h1>Hello, Pulumi!</h1></body></html>",
    },
    opts = pulumi.ResourceOptions(provider=k8s_provider))
deployment = kubernetes.apps.v1.Deployment("deployment",
    metadata={
        "namespace": ns.metadata.name,
    },
    spec={
        "selector": {
            "match_labels": {
                "app": "nginx",
            },
        },
        "replicas": 3,
        "template": {
            "metadata": {
                "labels": {
                    "app": "nginx",
                },
            },
            "spec": {
                "containers": [{
                    "name": "nginx",
                    "image": "nginx",
                    "ports": [{
                        "container_port": 80,
                    }],
                    "volume_mounts": [{
                        "name": "nginx-index",
                        "mount_path": "/usr/share/nginx/html",
                    }],
                }],
                "volumes": [{
                    "name": "nginx-index",
                    "config_map": {
                        "name": index_content.metadata.name,
                    },
                }],
            },
        },
    },
    opts = pulumi.ResourceOptions(provider=k8s_provider))
service = kubernetes.core.v1.Service("service",
    metadata={
        "name": "nginx",
        "namespace": ns.metadata.name,
    },
    spec={
        "selector": {
            "app": "nginx",
        },
        "ports": [{
            "port": 80,
            "target_port": 80,
        }],
    },
    opts = pulumi.ResourceOptions(provider=k8s_provider,
        depends_on=[deployment]))
ingress_class = kubernetes.networking.v1.IngressClass("ingressClass",
    metadata={
        "namespace": ns.metadata.name,
        "labels": {
            "app_kubernetes_io_name": "LoadBalancerController",
        },
        "name": "alb",
    },
    spec={
        "controller": "eks.amazonaws.com/alb",
    },
    opts = pulumi.ResourceOptions(provider=k8s_provider))
ingress = kubernetes.networking.v1.Ingress("ingress",
    metadata={
        "namespace": ns.metadata.name,
        "annotations": {
            "alb_ingress_kubernetes_io_scheme": "internet-facing",
            "alb_ingress_kubernetes_io_target_type": "ip",
        },
    },
    spec={
        "ingress_class_name": ingress_class.metadata.name,
        "rules": [{
            "http": {
                "paths": [{
                    "path": "/",
                    "path_type": "Prefix",
                    "backend": {
                        "service": {
                            "name": service.metadata.name,
                            "port": {
                                "number": 80,
                            },
                        },
                    },
                }],
            },
        }],
    },
    opts = pulumi.ResourceOptions(provider=k8s_provider))

pulumi.export("url", ingress.status.load_balancer.ingress[0].hostname)

```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-awsx/sdk/v2/go/awsx/ec2"
	"github.com/pulumi/pulumi-eks/sdk/v3/go/eks"
	"github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes"
	appsv1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/apps/v1"
	corev1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/core/v1"
	metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/meta/v1"
	networkingv1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/networking/v1"
	storagev1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/storage/v1"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// ...
		k8sProvider, err := kubernetes.NewProvider(ctx, "k8sProvider", &kubernetes.ProviderArgs{
			Kubeconfig: cluster.Kubeconfig,
		})
		if err != nil {
			return err
		}
		ns, err := corev1.NewNamespace(ctx, "ns", &corev1.NamespaceArgs{
			Metadata: &metav1.ObjectMetaArgs{
				Name: pulumi.String("nginx"),
			},
		}, pulumi.Provider(k8sProvider))
		if err != nil {
			return err
		}
		indexContent, err := corev1.NewConfigMap(ctx, "index-content", &corev1.ConfigMapArgs{
			Metadata: &metav1.ObjectMetaArgs{
				Namespace: ns.Metadata.ApplyT(func(metadata metav1.ObjectMeta) (*string, error) {
					return &metadata.Name, nil
				}).(pulumi.StringPtrOutput),
			},
			Data: pulumi.StringMap{
				"index.html": pulumi.String("<html><body><h1>Hello, Pulumi!</h1></body></html>"),
			},
		}, pulumi.Provider(k8sProvider))
		if err != nil {
			return err
		}
		deployment, err := appsv1.NewDeployment(ctx, "deployment", &appsv1.DeploymentArgs{
			Metadata: &metav1.ObjectMetaArgs{
				Namespace: ns.Metadata.ApplyT(func(metadata metav1.ObjectMeta) (*string, error) {
					return &metadata.Name, nil
				}).(pulumi.StringPtrOutput),
			},
			Spec: &appsv1.DeploymentSpecArgs{
				Selector: &metav1.LabelSelectorArgs{
					MatchLabels: pulumi.StringMap{
						"app": pulumi.String("nginx"),
					},
				},
				Replicas: pulumi.Int(3),
				Template: &corev1.PodTemplateSpecArgs{
					Metadata: &metav1.ObjectMetaArgs{
						Labels: pulumi.StringMap{
							"app": pulumi.String("nginx"),
						},
					},
					Spec: &corev1.PodSpecArgs{
						Containers: corev1.ContainerArray{
							&corev1.ContainerArgs{
								Name:  pulumi.String("nginx"),
								Image: pulumi.String("nginx"),
								Ports: corev1.ContainerPortArray{
									&corev1.ContainerPortArgs{
										ContainerPort: pulumi.Int(80),
									},
								},
								VolumeMounts: corev1.VolumeMountArray{
									&corev1.VolumeMountArgs{
										Name:      pulumi.String("nginx-index"),
										MountPath: pulumi.String("/usr/share/nginx/html"),
									},
								},
							},
						},
						Volumes: corev1.VolumeArray{
							&corev1.VolumeArgs{
								Name: pulumi.String("nginx-index"),
								ConfigMap: &corev1.ConfigMapVolumeSourceArgs{
									Name: indexContent.Metadata.ApplyT(func(metadata metav1.ObjectMeta) (*string, error) {
										return &metadata.Name, nil
									}).(pulumi.StringPtrOutput),
								},
							},
						},
					},
				},
			},
		}, pulumi.Provider(k8sProvider))
		if err != nil {
			return err
		}
		service, err := corev1.NewService(ctx, "service", &corev1.ServiceArgs{
			Metadata: &metav1.ObjectMetaArgs{
				Name: pulumi.String("nginx"),
				Namespace: ns.Metadata.ApplyT(func(metadata metav1.ObjectMeta) (*string, error) {
					return &metadata.Name, nil
				}).(pulumi.StringPtrOutput),
			},
			Spec: &corev1.ServiceSpecArgs{
				Selector: pulumi.StringMap{
					"app": pulumi.String("nginx"),
				},
				Ports: corev1.ServicePortArray{
					&corev1.ServicePortArgs{
						Port:       pulumi.Int(80),
						TargetPort: pulumi.Any(80),
					},
				},
			},
		}, pulumi.Provider(k8sProvider), pulumi.DependsOn([]pulumi.Resource{
			deployment,
		}))
		if err != nil {
			return err
		}
		ingressClass, err := networkingv1.NewIngressClass(ctx, "ingressClass", &networkingv1.IngressClassArgs{
			Metadata: &metav1.ObjectMetaArgs{
				Namespace: ns.Metadata.ApplyT(func(metadata metav1.ObjectMeta) (*string, error) {
					return &metadata.Name, nil
				}).(pulumi.StringPtrOutput),
				Labels: pulumi.StringMap{
					"app.kubernetes.io/name": pulumi.String("LoadBalancerController"),
				},
				Name: pulumi.String("alb"),
			},
			Spec: &networkingv1.IngressClassSpecArgs{
				Controller: pulumi.String("eks.amazonaws.com/alb"),
			},
		}, pulumi.Provider(k8sProvider))
		if err != nil {
			return err
		}
		ingress, err := networkingv1.NewIngress(ctx, "ingress", &networkingv1.IngressArgs{
			Metadata: &metav1.ObjectMetaArgs{
				Namespace: ns.Metadata.ApplyT(func(metadata metav1.ObjectMeta) (*string, error) {
					return &metadata.Name, nil
				}).(pulumi.StringPtrOutput),
				Annotations: pulumi.StringMap{
					"alb.ingress.kubernetes.io/scheme":      pulumi.String("internet-facing"),
					"alb.ingress.kubernetes.io/target-type": pulumi.String("ip"),
				},
			},
			Spec: &networkingv1.IngressSpecArgs{
				IngressClassName: ingressClass.Metadata.ApplyT(func(metadata metav1.ObjectMeta) (*string, error) {
					return &metadata.Name, nil
				}).(pulumi.StringPtrOutput),
				Rules: networkingv1.IngressRuleArray{
					&networkingv1.IngressRuleArgs{
						Http: &networkingv1.HTTPIngressRuleValueArgs{
							Paths: networkingv1.HTTPIngressPathArray{
								&networkingv1.HTTPIngressPathArgs{
									Path:     pulumi.String("/"),
									PathType: pulumi.String("Prefix"),
									Backend: &networkingv1.IngressBackendArgs{
										Service: &networkingv1.IngressServiceBackendArgs{
											Name: service.Metadata.ApplyT(func(metadata metav1.ObjectMeta) (*string, error) {
												return &metadata.Name, nil
											}).(pulumi.StringPtrOutput),
											Port: &networkingv1.ServiceBackendPortArgs{
												Number: pulumi.Int(80),
											},
										},
									},
								},
							},
						},
					},
				},
			},
		}, pulumi.Provider(k8sProvider))
		if err != nil {
			return err
		}
		
		ctx.Export("url", ingress.Status.ApplyT(func(status networkingv1.IngressStatus) (*string, error) {
			return &status.LoadBalancer.Ingress[0].Hostname, nil
		}).(pulumi.StringPtrOutput))
		return nil
	})
}

```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using System.Linq;
using Pulumi;
using Awsx = Pulumi.Awsx;
using Eks = Pulumi.Eks;
using Kubernetes = Pulumi.Kubernetes;

return await Deployment.RunAsync(() =>
{
    // ...
    var k8sProvider = new Kubernetes.Provider.Provider("k8sProvider", new()
    {
        KubeConfig = cluster.Kubeconfig,
    });

    var ns = new Kubernetes.Core.V1.Namespace("ns", new()
    {
        Metadata = new Kubernetes.Types.Inputs.Meta.V1.ObjectMetaArgs
        {
            Name = "nginx",
        },
    }, new CustomResourceOptions
    {
        Provider = k8sProvider,
    });

    var indexContent = new Kubernetes.Core.V1.ConfigMap("index-content", new()
    {
        Metadata = new Kubernetes.Types.Inputs.Meta.V1.ObjectMetaArgs
        {
            Namespace = ns.Metadata.Apply(metadata => metadata.Name),
        },
        Data =
        {
            { "index.html", "<html><body><h1>Hello, Pulumi!</h1></body></html>" },
        },
    }, new CustomResourceOptions
    {
        Provider = k8sProvider,
    });

    var deployment = new Kubernetes.Apps.V1.Deployment("deployment", new()
    {
        Metadata = new Kubernetes.Types.Inputs.Meta.V1.ObjectMetaArgs
        {
            Namespace = ns.Metadata.Apply(metadata => metadata.Name),
        },
        Spec = new Kubernetes.Types.Inputs.Apps.V1.DeploymentSpecArgs
        {
            Selector = new Kubernetes.Types.Inputs.Meta.V1.LabelSelectorArgs
            {
                MatchLabels =
                {
                    { "app", "nginx" },
                },
            },
            Replicas = 3,
            Template = new Kubernetes.Types.Inputs.Core.V1.PodTemplateSpecArgs
            {
                Metadata = new Kubernetes.Types.Inputs.Meta.V1.ObjectMetaArgs
                {
                    Labels =
                    {
                        { "app", "nginx" },
                    },
                },
                Spec = new Kubernetes.Types.Inputs.Core.V1.PodSpecArgs
                {
                    Containers = new[]
                    {
                        new Kubernetes.Types.Inputs.Core.V1.ContainerArgs
                        {
                            Name = "nginx",
                            Image = "nginx",
                            Ports = new[]
                            {
                                new Kubernetes.Types.Inputs.Core.V1.ContainerPortArgs
                                {
                                    ContainerPortValue = 80,
                                },
                            },
                            VolumeMounts = new[]
                            {
                                new Kubernetes.Types.Inputs.Core.V1.VolumeMountArgs
                                {
                                    Name = "nginx-index",
                                    MountPath = "/usr/share/nginx/html",
                                },
                            },
                        },
                    },
                    Volumes = new[]
                    {
                        new Kubernetes.Types.Inputs.Core.V1.VolumeArgs
                        {
                            Name = "nginx-index",
                            ConfigMap = new Kubernetes.Types.Inputs.Core.V1.ConfigMapVolumeSourceArgs
                            {
                                Name = indexContent.Metadata.Apply(metadata => metadata.Name),
                            },
                        },
                    },
                },
            },
        },
    }, new CustomResourceOptions
    {
        Provider = k8sProvider,
    });

    var service = new Kubernetes.Core.V1.Service("service", new()
    {
        Metadata = new Kubernetes.Types.Inputs.Meta.V1.ObjectMetaArgs
        {
            Name = "nginx",
            Namespace = ns.Metadata.Apply(metadata => metadata.Name),
        },
        Spec = new Kubernetes.Types.Inputs.Core.V1.ServiceSpecArgs
        {
            Selector =
            {
                { "app", "nginx" },
            },
            Ports = new[]
            {
                new Kubernetes.Types.Inputs.Core.V1.ServicePortArgs
                {
                    Port = 80,
                    TargetPort = 80,
                },
            },
        },
    }, new CustomResourceOptions
    {
        Provider = k8sProvider,
        DependsOn =
        {
            deployment,
        },
    });

    var ingressClass = new Kubernetes.Networking.V1.IngressClass("ingressClass", new()
    {
        Metadata = new Kubernetes.Types.Inputs.Meta.V1.ObjectMetaArgs
        {
            Namespace = ns.Metadata.Apply(metadata => metadata.Name),
            Labels =
            {
                { "app.kubernetes.io/name", "LoadBalancerController" },
            },
            Name = "alb",
        },
        Spec = new Kubernetes.Types.Inputs.Networking.V1.IngressClassSpecArgs
        {
            Controller = "eks.amazonaws.com/alb",
        },
    }, new CustomResourceOptions
    {
        Provider = k8sProvider,
    });

    var ingress = new Kubernetes.Networking.V1.Ingress("ingress", new()
    {
        Metadata = new Kubernetes.Types.Inputs.Meta.V1.ObjectMetaArgs
        {
            Namespace = ns.Metadata.Apply(metadata => metadata.Name),
            Annotations =
            {
                { "alb.ingress.kubernetes.io/scheme", "internet-facing" },
                { "alb.ingress.kubernetes.io/target-type", "ip" },
            },
        },
        Spec = new Kubernetes.Types.Inputs.Networking.V1.IngressSpecArgs
        {
            IngressClassName = ingressClass.Metadata.Apply(metadata => metadata.Name),
            Rules = new[]
            {
                new Kubernetes.Types.Inputs.Networking.V1.IngressRuleArgs
                {
                    Http = new Kubernetes.Types.Inputs.Networking.V1.HTTPIngressRuleValueArgs
                    {
                        Paths = new[]
                        {
                            new Kubernetes.Types.Inputs.Networking.V1.HTTPIngressPathArgs
                            {
                                Path = "/",
                                PathType = "Prefix",
                                Backend = new Kubernetes.Types.Inputs.Networking.V1.IngressBackendArgs
                                {
                                    Service = new Kubernetes.Types.Inputs.Networking.V1.IngressServiceBackendArgs
                                    {
                                        Name = service.Metadata.Apply(metadata => metadata.Name),
                                        Port = new Kubernetes.Types.Inputs.Networking.V1.ServiceBackendPortArgs
                                        {
                                            Number = 80,
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }, new CustomResourceOptions
    {
        Provider = k8sProvider,
    });

    return new Dictionary<string, object?>
    {
        ["url"] = ingress.Status.Apply(status => status?.LoadBalancer?.Ingress[0]?.Hostname),
    };
});


```

{{% /choosable %}}

{{% choosable language java %}}

```java
package generated_program;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.pulumi.awsx.ec2.Vpc;
import com.pulumi.awsx.ec2.VpcArgs;
import com.pulumi.awsx.ec2.inputs.SubnetSpecArgs;
import com.pulumi.eks.Cluster;
import com.pulumi.eks.ClusterArgs;
import com.pulumi.eks.inputs.AutoModeOptionsArgs;
import com.pulumi.kubernetes.Provider;
import com.pulumi.kubernetes.ProviderArgs;
import com.pulumi.kubernetes.core_v1.Namespace;
import com.pulumi.kubernetes.core_v1.NamespaceArgs;
import com.pulumi.kubernetes.meta_v1.inputs.ObjectMetaArgs;
import com.pulumi.kubernetes.core_v1.ConfigMap;
import com.pulumi.kubernetes.core_v1.ConfigMapArgs;
import com.pulumi.kubernetes.apps_v1.Deployment;
import com.pulumi.kubernetes.apps_v1.DeploymentArgs;
import com.pulumi.kubernetes.apps_v1.inputs.DeploymentSpecArgs;
import com.pulumi.kubernetes.meta_v1.inputs.LabelSelectorArgs;
import com.pulumi.kubernetes.core_v1.inputs.PodTemplateSpecArgs;
import com.pulumi.kubernetes.core_v1.inputs.PodSpecArgs;
import com.pulumi.kubernetes.core_v1.Service;
import com.pulumi.kubernetes.core_v1.ServiceArgs;
import com.pulumi.kubernetes.core_v1.inputs.ServiceSpecArgs;
import com.pulumi.kubernetes.networking.k8s.io_v1.IngressClass;
import com.pulumi.kubernetes.networking.k8s.io_v1.IngressClassArgs;
import com.pulumi.kubernetes.networking.k8s.io_v1.inputs.IngressClassSpecArgs;
import com.pulumi.kubernetes.networking.k8s.io_v1.Ingress;
import com.pulumi.kubernetes.networking.k8s.io_v1.IngressArgs;
import com.pulumi.kubernetes.networking.k8s.io_v1.inputs.IngressSpecArgs;
import com.pulumi.kubernetes.storage.k8s.io_v1.StorageClass;
import com.pulumi.kubernetes.storage.k8s.io_v1.StorageClassArgs;
import com.pulumi.kubernetes.core_v1.PersistentVolumeClaim;
import com.pulumi.kubernetes.core_v1.PersistentVolumeClaimArgs;
import com.pulumi.kubernetes.core_v1.inputs.PersistentVolumeClaimSpecArgs;
import com.pulumi.kubernetes.core_v1.inputs.VolumeResourceRequirementsArgs;
import com.pulumi.resources.CustomResourceOptions;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.io.File;
import java.nio.file.Files;
import java.nio.file.Paths;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        // ...
        var k8sProvider = new Provider("k8sProvider", ProviderArgs.builder()
            .kubeconfig(cluster.kubeconfig())
            .build());

        var ns = new Namespace("ns", NamespaceArgs.builder()
            .metadata(ObjectMetaArgs.builder()
                .name("nginx")
                .build())
            .build(), CustomResourceOptions.builder()
                .provider(k8sProvider)
                .build());

        var indexContent = new ConfigMap("indexContent", ConfigMapArgs.builder()
            .metadata(ObjectMetaArgs.builder()
                .namespace(ns.metadata().applyValue(metadata -> metadata.name()))
                .build())
            .data(Map.of("index.html", "<html><body><h1>Hello, Pulumi!</h1></body></html>"))
            .build(), CustomResourceOptions.builder()
                .provider(k8sProvider)
                .build());

        var deployment = new Deployment("deployment", DeploymentArgs.builder()
            .metadata(ObjectMetaArgs.builder()
                .namespace(ns.metadata().applyValue(metadata -> metadata.name()))
                .build())
            .spec(DeploymentSpecArgs.builder()
                .selector(LabelSelectorArgs.builder()
                    .matchLabels(Map.of("app", "nginx"))
                    .build())
                .replicas(3)
                .template(PodTemplateSpecArgs.builder()
                    .metadata(ObjectMetaArgs.builder()
                        .labels(Map.of("app", "nginx"))
                        .build())
                    .spec(PodSpecArgs.builder()
                        .containers(ContainerArgs.builder()
                            .name("nginx")
                            .image("nginx")
                            .ports(ContainerPortArgs.builder()
                                .containerPort(80)
                                .build())
                            .volumeMounts(VolumeMountArgs.builder()
                                .name("nginx-index")
                                .mountPath("/usr/share/nginx/html")
                                .build())
                            .build())
                        .volumes(VolumeArgs.builder()
                            .name("nginx-index")
                            .configMap(ConfigMapVolumeSourceArgs.builder()
                                .name(indexContent.metadata().applyValue(metadata -> metadata.name()))
                                .build())
                            .build())
                        .build())
                    .build())
                .build())
            .build(), CustomResourceOptions.builder()
                .provider(k8sProvider)
                .build());

        var service = new Service("service", ServiceArgs.builder()
            .metadata(ObjectMetaArgs.builder()
                .name("nginx")
                .namespace(ns.metadata().applyValue(metadata -> metadata.name()))
                .build())
            .spec(ServiceSpecArgs.builder()
                .selector(Map.of("app", "nginx"))
                .ports(ServicePortArgs.builder()
                    .port(80)
                    .targetPort(80)
                    .build())
                .build())
            .build(), CustomResourceOptions.builder()
                .provider(k8sProvider)
                .dependsOn(deployment)
                .build());

        var ingressClass = new IngressClass("ingressClass", IngressClassArgs.builder()
            .metadata(ObjectMetaArgs.builder()
                .namespace(ns.metadata().applyValue(metadata -> metadata.name()))
                .labels(Map.of("app.kubernetes.io/name", "LoadBalancerController"))
                .name("alb")
                .build())
            .spec(IngressClassSpecArgs.builder()
                .controller("eks.amazonaws.com/alb")
                .build())
            .build(), CustomResourceOptions.builder()
                .provider(k8sProvider)
                .build());

        var ingress = new Ingress("ingress", IngressArgs.builder()
            .metadata(ObjectMetaArgs.builder()
                .namespace(ns.metadata().applyValue(metadata -> metadata.name()))
                .annotations(Map.ofEntries(
                    Map.entry("alb.ingress.kubernetes.io/scheme", "internet-facing"),
                    Map.entry("alb.ingress.kubernetes.io/target-type", "ip")
                ))
                .build())
            .spec(IngressSpecArgs.builder()
                .ingressClassName(ingressClass.metadata().applyValue(metadata -> metadata.name()))
                .rules(IngressRuleArgs.builder()
                    .http(HTTPIngressRuleValueArgs.builder()
                        .paths(HTTPIngressPathArgs.builder()
                            .path("/")
                            .pathType("Prefix")
                            .backend(IngressBackendArgs.builder()
                                .service(IngressServiceBackendArgs.builder()
                                    .name(service.metadata().applyValue(metadata -> metadata.name()))
                                    .port(ServiceBackendPortArgs.builder()
                                        .number(80)
                                        .build())
                                    .build())
                                .build())
                            .build())
                        .build())
                    .build())
                .build())
            .build(), CustomResourceOptions.builder()
                .provider(k8sProvider)
                .build());

        ctx.export("url", ingress.status().applyValue(status -> status.loadBalancer().ingress()[0].hostname()));
    }
}

```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
name: eks-auto-mode-yaml
description: A Pulumi YAML program to deploy a Kubernetes cluster on AWS
runtime: yaml
resources:
  # ...
  k8sProvider:
    type: pulumi:providers:kubernetes
    properties:
      kubeconfig: ${cluster.kubeconfig}
  ns:
    type: kubernetes:core/v1:Namespace
    properties:
      metadata:
        name: nginx
    options:
      provider: ${k8sProvider}
  index-content:
    type: kubernetes:core/v1:ConfigMap
    properties:
      metadata:
        namespace: ${ns.metadata.name}
      data:
        "index.html": "<html><body><h1>Hello, Pulumi!</h1></body></html>"
    options:
      provider: ${k8sProvider}
  deployment:
    type: kubernetes:apps/v1:Deployment
    properties:
      metadata:
        namespace: ${ns.metadata.name}
      spec:
        selector:
          matchLabels:
            app: nginx
        replicas: 3
        template:
          metadata:
            labels:
              app: nginx
          spec:
            containers:
              - name: nginx
                image: nginx
                ports:
                  - containerPort: 80
                volumeMounts:
                  - name: nginx-index
                    mountPath: /usr/share/nginx/html
            volumes:
              - name: nginx-index
                configMap:
                  name: ${index-content.metadata.name}
    options:
      provider: ${k8sProvider}
  service:
    type: kubernetes:core/v1:Service
    properties:
      metadata:
        name: nginx
        namespace: ${ns.metadata.name}
      spec:
        selector:
          app: nginx
        ports:
          - port: 80
            targetPort: 80
    options:
      provider: ${k8sProvider}
      dependsOn:
        - ${deployment}
  ingressClass:
    type: kubernetes:networking.k8s.io/v1:IngressClass
    properties:
      metadata:
        namespace: ${ns.metadata.name}
        labels:
          app.kubernetes.io/name: LoadBalancerController
        name: alb
      spec:
        controller: eks.amazonaws.com/alb
    options:
      provider: ${k8sProvider}
  ingress:
    type: kubernetes:networking.k8s.io/v1:Ingress
    properties:
      metadata:
        namespace: ${ns.metadata.name}
        annotations:
          alb.ingress.kubernetes.io/scheme: internet-facing
          alb.ingress.kubernetes.io/target-type: ip
      spec:
        ingressClassName: ${ingressClass.metadata.name}
        rules:
          - http:
              paths:
                - path: /
                  pathType: Prefix
                  backend:
                    service:
                      name: ${service.metadata.name}
                      port:
                        number: 80
    options:
      provider: ${k8sProvider}
outputs:
  url: ${ingress.status.loadBalancer.ingress[0].hostname}
```

{{% /choosable %}}

{{< /chooser >}}

After deploying this with `pulumi up`, you can access your application with `curl` once the Load Balancer has been provisioned:

```bash
~ curl $(pulumi stack output url)
Hello, Pulumi!
```

## Deploying a Stateful Workload

EKS Auto Mode simplifies persistent storage management by automatically handling EBS volume provisioning for your stateful workloads. To leverage this feature, you can create a `StorageClass` that uses the EBS CSI driver (`ebs.csi.eks.amazonaws.com`) as its provisioner. EKS Auto Mode will then automatically manage the lifecycle of your persistent volumes, including provisioning, attaching, and cleanup.

This is how you'd configure persistent storage for a sample application:

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
// ...
const storageClass = new k8s.storage.v1.StorageClass("storage-class", {
    metadata: {
        name: "auto-ebs-sc",
        annotations: {
            "storageclass.kubernetes.io/is-default-class": "true",
        },
    },
    provisioner: "ebs.csi.eks.amazonaws.com",
    volumeBindingMode: "WaitForFirstConsumer",
    parameters: {
        type: "gp3",
        encrypted: "true",
    },
}, {
    provider: cluster.provider,
});
const pvc = new k8s.core.v1.PersistentVolumeClaim("pvc", {
    metadata: {
        name: "auto-ebs-claim",
        namespace: ns.metadata.apply(metadata => metadata.name),
    },
    spec: {
        accessModes: ["ReadWriteOnce"],
        storageClassName: storageClass.metadata.apply(metadata => metadata.name),
        resources: {
            requests: {
                storage: "8Gi",
            },
        },
    },
}, {
    provider: cluster.provider,
});
const statefulWorkload = new k8s.apps.v1.Deployment("stateful-workload", {
    metadata: {
        name: "inflate-stateful",
        namespace: ns.metadata.apply(metadata => metadata.name),
    },
    spec: {
        replicas: 1,
        selector: {
            matchLabels: {
                app: "inflate-stateful",
            },
        },
        template: {
            metadata: {
                labels: {
                    app: "inflate-stateful",
                },
            },
            spec: {
                terminationGracePeriodSeconds: 0,
                nodeSelector: {
                    "eks.amazonaws.com/compute-type": "auto",
                },
                containers: [{
                    name: "bash",
                    image: "public.ecr.aws/docker/library/bash:4.4",
                    command: ["/usr/local/bin/bash"],
                    args: [
                        "-c",
                        "while true; do echo $(date -u) >> /data/out.txt; sleep 60; done",
                    ],
                    resources: {
                        requests: {
                            cpu: "1",
                        },
                    },
                    volumeMounts: [{
                        name: "persistent-storage",
                        mountPath: "/data",
                    }],
                }],
                volumes: [{
                    name: "persistent-storage",
                    persistentVolumeClaim: {
                        claimName: pvc.metadata.name,
                    },
                }],
            },
        },
    },
}, {
    provider: cluster.provider,
});

export const url = ingress.status.loadBalancer.ingress[0].hostname.apply(h => `http://${h}:80`);


```

{{% /choosable %}}

{{% choosable language python %}}

```python
# ...
storage_class = kubernetes.storage.v1.StorageClass("storage-class",
    metadata={
        "name": "auto-ebs-sc",
        "annotations": {
            "storageclass_kubernetes_io_is_default_class": "true",
        },
    },
    provisioner="ebs.csi.eks.amazonaws.com",
    volume_binding_mode="WaitForFirstConsumer",
    parameters={
        "type": "gp3",
        "encrypted": "true",
    },
    opts = pulumi.ResourceOptions(provider=k8_s_provider))
pvc = kubernetes.core.v1.PersistentVolumeClaim("pvc",
    metadata={
        "name": "auto-ebs-claim",
        "namespace": ns.metadata.name,
    },
    spec={
        "access_modes": ["ReadWriteOnce"],
        "storage_class_name": storage_class.metadata.name,
        "resources": {
            "requests": {
                "storage": "8Gi",
            },
        },
    },
    opts = pulumi.ResourceOptions(provider=k8_s_provider))
stateful_workload = kubernetes.apps.v1.Deployment("stateful-workload",
    metadata={
        "name": "inflate-stateful",
        "namespace": ns.metadata.name,
    },
    spec={
        "replicas": 1,
        "selector": {
            "match_labels": {
                "app": "inflate-stateful",
            },
        },
        "template": {
            "metadata": {
                "labels": {
                    "app": "inflate-stateful",
                },
            },
            "spec": {
                "termination_grace_period_seconds": 0,
                "node_selector": {
                    "eks_amazonaws_com_compute_type": "auto",
                },
                "containers": [{
                    "name": "bash",
                    "image": "public.ecr.aws/docker/library/bash:4.4",
                    "command": ["/usr/local/bin/bash"],
                    "args": [
                        "-c",
                        "while true; do echo $(date -u) >> /data/out.txt; sleep 60; done",
                    ],
                    "resources": {
                        "requests": {
                            "cpu": "1",
                        },
                    },
                    "volume_mounts": [{
                        "name": "persistent-storage",
                        "mount_path": "/data",
                    }],
                }],
                "volumes": [{
                    "name": "persistent-storage",
                    "persistent_volume_claim": {
                        "claim_name": pvc.metadata.name,
                    },
                }],
            },
        },
    },
    opts = pulumi.ResourceOptions(provider=k8_s_provider))

```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-awsx/sdk/v2/go/awsx/ec2"
	"github.com/pulumi/pulumi-eks/sdk/v3/go/eks"
	"github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes"
	appsv1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/apps/v1"
	corev1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/core/v1"
	metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/meta/v1"
	networkingv1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/networking/v1"
	storagev1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/storage/v1"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// ...
		storageClass, err := storagev1.NewStorageClass(ctx, "storage-class", &storagev1.StorageClassArgs{
			Metadata: &metav1.ObjectMetaArgs{
				Name: pulumi.String("auto-ebs-sc"),
				Annotations: pulumi.StringMap{
					"storageclass.kubernetes.io/is-default-class": pulumi.String("true"),
				},
			},
			Provisioner:       pulumi.String("ebs.csi.eks.amazonaws.com"),
			VolumeBindingMode: pulumi.String("WaitForFirstConsumer"),
			Parameters: pulumi.StringMap{
				"type":      pulumi.String("gp3"),
				"encrypted": pulumi.String("true"),
			},
		}, pulumi.Provider(k8SProvider))
		if err != nil {
			return err
		}
		pvc, err := corev1.NewPersistentVolumeClaim(ctx, "pvc", &corev1.PersistentVolumeClaimArgs{
			Metadata: &metav1.ObjectMetaArgs{
				Name: pulumi.String("auto-ebs-claim"),
				Namespace: ns.Metadata.ApplyT(func(metadata metav1.ObjectMeta) (*string, error) {
					return &metadata.Name, nil
				}).(pulumi.StringPtrOutput),
			},
			Spec: &corev1.PersistentVolumeClaimSpecArgs{
				AccessModes: pulumi.StringArray{
					pulumi.String("ReadWriteOnce"),
				},
				StorageClassName: storageClass.Metadata.ApplyT(func(metadata metav1.ObjectMeta) (*string, error) {
					return &metadata.Name, nil
				}).(pulumi.StringPtrOutput),
				Resources: &corev1.VolumeResourceRequirementsArgs{
					Requests: pulumi.StringMap{
						"storage": pulumi.String("8Gi"),
					},
				},
			},
		}, pulumi.Provider(k8SProvider))
		if err != nil {
			return err
		}
		_, err = appsv1.NewDeployment(ctx, "stateful-workload", &appsv1.DeploymentArgs{
			Metadata: &metav1.ObjectMetaArgs{
				Name: pulumi.String("inflate-stateful"),
				Namespace: ns.Metadata.ApplyT(func(metadata metav1.ObjectMeta) (*string, error) {
					return &metadata.Name, nil
				}).(pulumi.StringPtrOutput),
			},
			Spec: &appsv1.DeploymentSpecArgs{
				Replicas: pulumi.Int(1),
				Selector: &metav1.LabelSelectorArgs{
					MatchLabels: pulumi.StringMap{
						"app": pulumi.String("inflate-stateful"),
					},
				},
				Template: &corev1.PodTemplateSpecArgs{
					Metadata: &metav1.ObjectMetaArgs{
						Labels: pulumi.StringMap{
							"app": pulumi.String("inflate-stateful"),
						},
					},
					Spec: &corev1.PodSpecArgs{
						TerminationGracePeriodSeconds: pulumi.Int(0),
						NodeSelector: pulumi.StringMap{
							"eks.amazonaws.com/compute-type": pulumi.String("auto"),
						},
						Containers: corev1.ContainerArray{
							&corev1.ContainerArgs{
								Name:  pulumi.String("bash"),
								Image: pulumi.String("public.ecr.aws/docker/library/bash:4.4"),
								Command: pulumi.StringArray{
									pulumi.String("/usr/local/bin/bash"),
								},
								Args: pulumi.StringArray{
									pulumi.String("-c"),
									pulumi.String("while true; do echo $(date -u) >> /data/out.txt; sleep 60; done"),
								},
								Resources: &corev1.ResourceRequirementsArgs{
									Requests: pulumi.StringMap{
										"cpu": pulumi.String("1"),
									},
								},
								VolumeMounts: corev1.VolumeMountArray{
									&corev1.VolumeMountArgs{
										Name:      pulumi.String("persistent-storage"),
										MountPath: pulumi.String("/data"),
									},
								},
							},
						},
						Volumes: corev1.VolumeArray{
							&corev1.VolumeArgs{
								Name: pulumi.String("persistent-storage"),
								PersistentVolumeClaim: &corev1.PersistentVolumeClaimVolumeSourceArgs{
									ClaimName: pvc.Metadata.ApplyT(func(metadata metav1.ObjectMeta) (*string, error) {
										return &metadata.Name, nil
									}).(pulumi.StringPtrOutput),
								},
							},
						},
					},
				},
			},
		}, pulumi.Provider(k8SProvider))
		if err != nil {
			return err
		}
		return nil
	})
}

```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using System.Linq;
using Pulumi;
using Awsx = Pulumi.Awsx;
using Eks = Pulumi.Eks;
using Kubernetes = Pulumi.Kubernetes;

return await Deployment.RunAsync(() =>
{
    // ...
    var storageClass = new Kubernetes.Storage.V1.StorageClass("storage-class", new()
    {
        Metadata = new Kubernetes.Types.Inputs.Meta.V1.ObjectMetaArgs
        {
            Name = "auto-ebs-sc",
            Annotations =
            {
                { "storageclass.kubernetes.io/is-default-class", "true" },
            },
        },
        Provisioner = "ebs.csi.eks.amazonaws.com",
        VolumeBindingMode = "WaitForFirstConsumer",
        Parameters =
        {
            { "type", "gp3" },
            { "encrypted", "true" },
        },
    }, new CustomResourceOptions
    {
        Provider = k8SProvider,
    });

    var pvc = new Kubernetes.Core.V1.PersistentVolumeClaim("pvc", new()
    {
        Metadata = new Kubernetes.Types.Inputs.Meta.V1.ObjectMetaArgs
        {
            Name = "auto-ebs-claim",
            Namespace = ns.Metadata.Apply(metadata => metadata.Name),
        },
        Spec = new Kubernetes.Types.Inputs.Core.V1.PersistentVolumeClaimSpecArgs
        {
            AccessModes = new[]
            {
                "ReadWriteOnce",
            },
            StorageClassName = storageClass.Metadata.Apply(metadata => metadata.Name),
            Resources = new Kubernetes.Types.Inputs.Core.V1.VolumeResourceRequirementsArgs
            {
                Requests =
                {
                    { "storage", "8Gi" },
                },
            },
        },
    }, new CustomResourceOptions
    {
        Provider = k8SProvider,
    });

    var statefulWorkload = new Kubernetes.Apps.V1.Deployment("stateful-workload", new()
    {
        Metadata = new Kubernetes.Types.Inputs.Meta.V1.ObjectMetaArgs
        {
            Name = "inflate-stateful",
            Namespace = ns.Metadata.Apply(metadata => metadata.Name),
        },
        Spec = new Kubernetes.Types.Inputs.Apps.V1.DeploymentSpecArgs
        {
            Replicas = 1,
            Selector = new Kubernetes.Types.Inputs.Meta.V1.LabelSelectorArgs
            {
                MatchLabels =
                {
                    { "app", "inflate-stateful" },
                },
            },
            Template = new Kubernetes.Types.Inputs.Core.V1.PodTemplateSpecArgs
            {
                Metadata = new Kubernetes.Types.Inputs.Meta.V1.ObjectMetaArgs
                {
                    Labels =
                    {
                        { "app", "inflate-stateful" },
                    },
                },
                Spec = new Kubernetes.Types.Inputs.Core.V1.PodSpecArgs
                {
                    TerminationGracePeriodSeconds = 0,
                    NodeSelector =
                    {
                        { "eks.amazonaws.com/compute-type", "auto" },
                    },
                    Containers = new[]
                    {
                        new Kubernetes.Types.Inputs.Core.V1.ContainerArgs
                        {
                            Name = "bash",
                            Image = "public.ecr.aws/docker/library/bash:4.4",
                            Command = new[]
                            {
                                "/usr/local/bin/bash",
                            },
                            Args = new[]
                            {
                                "-c",
                                "while true; do echo $(date -u) >> /data/out.txt; sleep 60; done",
                            },
                            Resources = new Kubernetes.Types.Inputs.Core.V1.ResourceRequirementsArgs
                            {
                                Requests =
                                {
                                    { "cpu", "1" },
                                },
                            },
                            VolumeMounts = new[]
                            {
                                new Kubernetes.Types.Inputs.Core.V1.VolumeMountArgs
                                {
                                    Name = "persistent-storage",
                                    MountPath = "/data",
                                },
                            },
                        },
                    },
                    Volumes = new[]
                    {
                        new Kubernetes.Types.Inputs.Core.V1.VolumeArgs
                        {
                            Name = "persistent-storage",
                            PersistentVolumeClaim = new Kubernetes.Types.Inputs.Core.V1.PersistentVolumeClaimVolumeSourceArgs
                            {
                                ClaimName = pvc.Metadata.Apply(metadata => metadata.Name),
                            },
                        },
                    },
                },
            },
        },
    }, new CustomResourceOptions
    {
        Provider = k8SProvider,
    });
});


```

{{% /choosable %}}

{{% choosable language java %}}

```java
package generated_program;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.pulumi.awsx.ec2.Vpc;
import com.pulumi.awsx.ec2.VpcArgs;
import com.pulumi.awsx.ec2.inputs.SubnetSpecArgs;
import com.pulumi.eks.Cluster;
import com.pulumi.eks.ClusterArgs;
import com.pulumi.eks.inputs.AutoModeOptionsArgs;
import com.pulumi.kubernetes.Provider;
import com.pulumi.kubernetes.ProviderArgs;
import com.pulumi.kubernetes.core_v1.Namespace;
import com.pulumi.kubernetes.core_v1.NamespaceArgs;
import com.pulumi.kubernetes.meta_v1.inputs.ObjectMetaArgs;
import com.pulumi.kubernetes.core_v1.ConfigMap;
import com.pulumi.kubernetes.core_v1.ConfigMapArgs;
import com.pulumi.kubernetes.apps_v1.Deployment;
import com.pulumi.kubernetes.apps_v1.DeploymentArgs;
import com.pulumi.kubernetes.apps_v1.inputs.DeploymentSpecArgs;
import com.pulumi.kubernetes.meta_v1.inputs.LabelSelectorArgs;
import com.pulumi.kubernetes.core_v1.inputs.PodTemplateSpecArgs;
import com.pulumi.kubernetes.core_v1.inputs.PodSpecArgs;
import com.pulumi.kubernetes.core_v1.Service;
import com.pulumi.kubernetes.core_v1.ServiceArgs;
import com.pulumi.kubernetes.core_v1.inputs.ServiceSpecArgs;
import com.pulumi.kubernetes.networking.k8s.io_v1.IngressClass;
import com.pulumi.kubernetes.networking.k8s.io_v1.IngressClassArgs;
import com.pulumi.kubernetes.networking.k8s.io_v1.inputs.IngressClassSpecArgs;
import com.pulumi.kubernetes.networking.k8s.io_v1.Ingress;
import com.pulumi.kubernetes.networking.k8s.io_v1.IngressArgs;
import com.pulumi.kubernetes.networking.k8s.io_v1.inputs.IngressSpecArgs;
import com.pulumi.kubernetes.storage.k8s.io_v1.StorageClass;
import com.pulumi.kubernetes.storage.k8s.io_v1.StorageClassArgs;
import com.pulumi.kubernetes.core_v1.PersistentVolumeClaim;
import com.pulumi.kubernetes.core_v1.PersistentVolumeClaimArgs;
import com.pulumi.kubernetes.core_v1.inputs.PersistentVolumeClaimSpecArgs;
import com.pulumi.kubernetes.core_v1.inputs.VolumeResourceRequirementsArgs;
import com.pulumi.resources.CustomResourceOptions;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        // ...
        var storageClass = new StorageClass("storageClass", StorageClassArgs.builder()
            .metadata(ObjectMetaArgs.builder()
                .name("auto-ebs-sc")
                .annotations(Map.of("storageclass.kubernetes.io/is-default-class", "true"))
                .build())
            .provisioner("ebs.csi.eks.amazonaws.com")
            .volumeBindingMode("WaitForFirstConsumer")
            .parameters(Map.ofEntries(
                Map.entry("type", "gp3"),
                Map.entry("encrypted", "true")
            ))
            .build(), CustomResourceOptions.builder()
                .provider(k8SProvider)
                .build());

        var pvc = new PersistentVolumeClaim("pvc", PersistentVolumeClaimArgs.builder()
            .metadata(ObjectMetaArgs.builder()
                .name("auto-ebs-claim")
                .namespace(ns.metadata().applyValue(metadata -> metadata.name()))
                .build())
            .spec(PersistentVolumeClaimSpecArgs.builder()
                .accessModes("ReadWriteOnce")
                .storageClassName(storageClass.metadata().applyValue(metadata -> metadata.name()))
                .resources(VolumeResourceRequirementsArgs.builder()
                    .requests(Map.of("storage", "8Gi"))
                    .build())
                .build())
            .build(), CustomResourceOptions.builder()
                .provider(k8SProvider)
                .build());

        var statefulWorkload = new Deployment("statefulWorkload", DeploymentArgs.builder()
            .metadata(ObjectMetaArgs.builder()
                .name("inflate-stateful")
                .namespace(ns.metadata().applyValue(metadata -> metadata.name()))
                .build())
            .spec(DeploymentSpecArgs.builder()
                .replicas(1)
                .selector(LabelSelectorArgs.builder()
                    .matchLabels(Map.of("app", "inflate-stateful"))
                    .build())
                .template(PodTemplateSpecArgs.builder()
                    .metadata(ObjectMetaArgs.builder()
                        .labels(Map.of("app", "inflate-stateful"))
                        .build())
                    .spec(PodSpecArgs.builder()
                        .terminationGracePeriodSeconds(0)
                        .nodeSelector(Map.of("eks.amazonaws.com/compute-type", "auto"))
                        .containers(ContainerArgs.builder()
                            .name("bash")
                            .image("public.ecr.aws/docker/library/bash:4.4")
                            .command("/usr/local/bin/bash")
                            .args(
                                "-c",
                                "while true; do echo $(date -u) >> /data/out.txt; sleep 60; done")
                            .resources(ResourceRequirementsArgs.builder()
                                .requests(Map.of("cpu", "1"))
                                .build())
                            .volumeMounts(VolumeMountArgs.builder()
                                .name("persistent-storage")
                                .mountPath("/data")
                                .build())
                            .build())
                        .volumes(VolumeArgs.builder()
                            .name("persistent-storage")
                            .persistentVolumeClaim(PersistentVolumeClaimVolumeSourceArgs.builder()
                                .claimName(pvc.metadata().applyValue(metadata -> metadata.name()))
                                .build())
                            .build())
                        .build())
                    .build())
                .build())
            .build(), CustomResourceOptions.builder()
                .provider(k8SProvider)
                .build());
    }
}

```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
name: eks-auto-mode-yaml
description: A Pulumi YAML program to deploy a Kubernetes cluster on AWS
runtime: yaml
resources:
  # ...
  storage-class:
    type: kubernetes:storage.k8s.io/v1:StorageClass
    properties:
      metadata:
        name: auto-ebs-sc
        annotations:
          storageclass.kubernetes.io/is-default-class: "true"
      provisioner: ebs.csi.eks.amazonaws.com
      volumeBindingMode: WaitForFirstConsumer
      parameters:
        type: gp3
        encrypted: "true"
    options:
      provider: ${k8sProvider}
  pvc:
    type: kubernetes:core/v1:PersistentVolumeClaim
    properties:
      metadata:
        name: auto-ebs-claim
        namespace: ${ns.metadata.name}
      spec:
        accessModes:
          - ReadWriteOnce
        storageClassName: ${storage-class.metadata.name}
        resources:
          requests:
            storage: 8Gi
    options:
      provider: ${k8sProvider}
  stateful-workload:
    type: kubernetes:apps/v1:Deployment
    properties:
      metadata:
        name: inflate-stateful
        namespace: ${ns.metadata.name}
      spec:
        replicas: 1
        selector:
          matchLabels:
            app: inflate-stateful
        template:
          metadata:
            labels:
              app: inflate-stateful
          spec:
            terminationGracePeriodSeconds: 0
            nodeSelector:
              eks.amazonaws.com/compute-type: auto
            containers:
              - name: bash
                image: public.ecr.aws/docker/library/bash:4.4
                command: ["/usr/local/bin/bash"]
                args: ["-c", "while true; do echo $(date -u) >> /data/out.txt; sleep 60; done"]
                resources:
                  requests:
                    cpu: "1"
                volumeMounts:
                  - name: persistent-storage
                    mountPath: /data
            volumes:
              - name: persistent-storage
                persistentVolumeClaim:
                  claimName: ${pvc.metadata.name}
    options:
      provider: ${k8sProvider}
outputs:
  url: ${ingress.status.loadBalancer.ingress[0].hostname}
```

{{% /choosable %}}

{{< /chooser >}}

## Summary

EKS Auto Mode represents a significant step forward in simplifying Kubernetes operations on AWS. Pulumi's support for this feature allows you
to define EKS Auto Mode clusters using your favorite programming language and integrate them with your existing infrastructure code.

To get started with EKS Auto Mode in Pulumi:

1. Update your AWS providers to the latest versions
2. Check out our [EKS documentation](/registry/packages/eks/)
3. Join our [Community Slack](https://slack.pulumi.com/) for support and discussions

We are excited to see what you build with EKS Auto Mode and Pulumi!

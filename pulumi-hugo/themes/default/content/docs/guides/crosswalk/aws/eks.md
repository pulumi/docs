---
title_tag: "Using AWS Elastic Kubernetes Service (EKS) | Crosswalk"
title: Using AWS Elastic Kubernetes Service (EKS)
meta_desc: Pulumi Crosswalk for AWS simplifies the creation, configuration, and management of EKS clusters
           offering a single programming model and deployment workflow.
linktitle: Elastic Kubernetes Service (EKS)
menu:
  userguides:
    parent: crosswalk-aws
    weight: 6

aliases:
    - "/docs/reference/crosswalk/aws/eks/"
    - "/eks"
---

<a href="./">
    <img src="/images/docs/reference/crosswalk/aws/logo.svg" align="right" width="280" style="margin: 0 0 32px 16px;">
</a>

[Amazon Elastic Kubernetes Service (Amazon EKS)](https://aws.amazon.com/eks) makes it easy to deploy,
manage, and scale containerized applications using Kubernetes on AWS. Amazon EKS runs the Kubernetes management
infrastructure for you across multiple AWS availability zones to eliminate a single point of failure. Amazon EKS is
certified Kubernetes conformant so you can use existing tooling and plugins from partners and the Kubernetes
community. Applications running on any standard Kubernetes environment are fully compatible and can be easily migrated
to Amazon EKS.

## Overview

Pulumi Crosswalk for AWS simplifies the creation, configuration, and management of EKS clusters, in addition to
offering a single programming model and deployment workflow that works for your Kubernetes application configuration,
in addition to infrastructure. This support ensures your EKS resources are fully integrated properly with the
related AWS services. This includes

* [ECR](/docs/guides/crosswalk/aws/ecr/) for private container images
* [ELB](/docs/guides/crosswalk/aws/elb/) for load balancing
* [IAM](/docs/guides/crosswalk/aws/iam/) for security
* [VPC](/docs/guides/crosswalk/aws/vpc/) for network isolation
* [CloudWatch](/docs/guides/crosswalk/aws/cloudwatch/) for monitoring

Amazon EKS runs up-to-date versions of the open-source Kubernetes software, so you can use all the existing plugins and
tooling from the Kubernetes community, including Pulumi's support for deploying Helm charts. Applications running on
Amazon EKS are fully compatible with applications running on any standard Kubernetes environment, whether running in
on-premises data centers or public clouds, easing porting from other Kubernetes environments to EKS.

Expressing your infrastructure and Kubernetes configuration in code using Pulumi Crosswalk for AWS ensures your
resulting system is ready for production using built-in best practices.

## Prerequisites

Before getting started, you will need to install some pre-requisites:

* [`aws-iam-authenticator`](https://docs.aws.amazon.com/eks/latest/userguide/install-aws-iam-authenticator.html):
  Amazon EKS uses IAM to provide secure authentication to your Kubernetes cluster.

These are not required but are recommended if you plan on interacting with your Kubernetes cluster:

* [`kubectl`](https://kubernetes.io/docs/tasks/tools/install-kubectl/): the standard Kubernetes command line interface.
* [`helm`](https://helm.sh/docs/using_helm/): if you plan on deploying Helm charts to your cluster.

## Provisioning a New EKS Cluster

To create a new EKS cluster, allocate an instance of an `eks.Cluster` class in your Pulumi program:

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as eks from "@pulumi/eks";

// Create an EKS cluster with the default configuration.
const cluster = new eks.Cluster("cluster", {});

// Export the cluster's kubeconfig.
export const kubeconfig = cluster.kubeconfig;
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
import pulumi_eks as eks

# Create an EKS cluster with the default configuration.
cluster = eks.Cluster("cluster")

# Export the cluster's kubeconfig.
pulumi.export("kubeconfig", cluster.kubeconfig)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-eks/sdk/go/eks"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Create an EKS cluster with the default configuration.
		cluster, err := eks.NewCluster(ctx, "cluster", nil)
		if err != nil {
			return err
		}
		// Export the cluster's kubeconfig.
		ctx.Export("kubeconfig", cluster.Kubeconfig)
		return nil
	})
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using Pulumi;
using Eks = Pulumi.Eks;

return await Deployment.RunAsync(() =>
{
    // Create an EKS cluster with the default configuration.
    var cluster = new Eks.Cluster("cluster");

    return new Dictionary<string, object?>
    {
        // Export the cluster's kubeconfig.
        ["kubeconfig"] = cluster.Kubeconfig,
    };
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.pulumi.eks.Cluster;
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
        // Create an EKS cluster with the default configuration.
        var cluster = new Cluster("cluster");

        // Export the cluster's kubeconfig.
        ctx.export("kubeconfig", cluster.kubeconfig());
    }
}
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  # Create an EKS cluster with the default configuration.
  cluster:
    type: eks:Cluster
outputs:
  # Export the cluster's kubeconfig.
  kubeconfig: ${cluster.kubeconfig}

```

{{% /choosable %}}

This cluster uses reasonable defaults, like placing the cluster into your default VPC with a CNI interface, using
AWS IAM Authenticator to leverage IAM for secure access to your cluster, and using two `t2.medium` nodes.

After running `pulumi up`, we will see the resulting cluster's `kubeconfig` file exported for easy access:

```bash
$ pulumi up
Updating (dev):

     Type                       Name                            Status
 +   pulumi:pulumi:Stack        crosswalk-aws-dev               created
 +   └─ eks:index:Cluster       my-cluster                      created
     ... dozens of resources omitted ...

Outputs:
    kubeconfig: {
        apiVersion     : "v1"
        clusters       : [
            [0]: {
                cluster: {
                    certificate-authority-data: "...",
                    server                    : "https://D34E7144F46CB.sk1.us-west-2.eks.amazonaws.com"
                }
                name   : "kubernetes"
            }
        ]
        contexts       : [
            [0]: {
                context: {
                    cluster: "kubernetes"
                    user   : "aws"
                }
                name   : "aws"
            }
        ]
        current-context: "aws"
        kind           : "Config"
        users          : [
            [0]: {
                name: "aws"
                user: {
                    exec: {
                        apiVersion: "client.authentication.k8s.io/v1alpha1"
                        args      : [
                            [0]: "token"
                            [1]: "-i"
                            [2]: "my-cluster-eksCluster-22c2275"
                        ]
                        command   : "aws-iam-authenticator"
                    }
                }
            }
        ]
    }

Resources:
    + 43 created

Duration: 11m26s
```

It is easy to take this file and use it with the `kubectl` CLI:

```bash
$ pulumi stack output kubeconfig > kubeconfig.yml
$ KUBECONFIG=./kubeconfig.yml kubectl get nodes
NAME                                         STATUS    ROLES     AGE       VERSION
ip-172-31-29-62.us-west-2.compute.internal   Ready     <none>    1m       v1.12.7
ip-172-31-40-32.us-west-2.compute.internal   Ready     <none>    2m       v1.12.7
```

By default, Pulumi targets clusters based on your local kubeconfig, just like `kubectl` does. So if your `kubectl`
client is set up to talk to your EKS cluster, deployments will target it. We saw earlier in
[Provisioning a New EKS Cluster](#provisioning-a-new-eks-cluster), however, that you can deploy into any
Kubernetes cluster created in your Pulumi program. This is because each Kubernetes object specification accepts
an optional "provider" that can programmatically specify a kubeconfig to use.

This is done by instantiating a new `kubernetes.Provider` object, and providing one or many of these properties:

* `cluster`: A cluster name to target, if there are many in your kubeconfig to choose from.
* `context`: The name of the kubeconfig context to use, if there are many to choose from.
* `kubeconfig`: A stringified JSON representing a full kubeconfig to use instead of your local machine's.

From here, we have a fully functioning EKS cluster in Amazon, which we can deploy Kubernetes applications to.
Any existing tools will work here, including `kubectl`, Helm, and other CI/CD products. Pulumi offers the ability
to define Kubernetes application-level objects and configuration in code too. For instance, we can deploy a canary
to our EKS cluster in the same program if we want to test that it is working as part of `pulumi up`:

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as eks from "@pulumi/eks";
import * as kubernetes from "@pulumi/kubernetes";

// Create an EKS cluster with the default configuration.
const cluster = new eks.Cluster("cluster", {});
const eksProvider = new kubernetes.Provider("eks-provider", {kubeconfig: cluster.kubeconfigJson});

// Deploy a small canary service (NGINX), to test that the cluster is working.
const myDeployment = new kubernetes.apps.v1.Deployment("my-deployment", {
    metadata: {
        labels: {
            appClass: "my-deployment",
        },
    },
    spec: {
        replicas: 2,
        selector: {
            matchLabels: {
                appClass: "my-deployment",
            },
        },
        template: {
            metadata: {
                labels: {
                    appClass: "my-deployment",
                },
            },
            spec: {
                containers: [{
                    name: "my-deployment",
                    image: "nginx",
                    ports: [{
                        name: "http",
                        containerPort: 80,
                    }],
                }],
            },
        },
    },
}, {
    provider: eksProvider,
});
const myService = new kubernetes.core.v1.Service("my-service", {
    metadata: {
        labels: {
            appClass: "my-deployment",
        },
    },
    spec: {
        type: "LoadBalancer",
        ports: [{
            port: 80,
            targetPort: "http",
        }],
        selector: {
            appClass: "my-deployment",
        },
    },
}, {
    provider: eksProvider,
});

// Export the cluster's kubeconfig.
export const kubeconfig = cluster.kubeconfig;
// Export the URL for the load balanced service.
export const url = myService.status.apply(status => status?.loadBalancer?.ingress[0]?.hostname);
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
import pulumi_eks as eks
import pulumi_kubernetes as kubernetes

# Create an EKS cluster with the default configuration.
cluster = eks.Cluster("cluster")
eks_provider = kubernetes.Provider("eks-provider", kubeconfig=cluster.kubeconfig_json)
# Deploy a small canary service (NGINX), to test that the cluster is working.
my_deployment = kubernetes.apps.v1.Deployment("my-deployment",
    metadata=kubernetes.meta.v1.ObjectMetaArgs(
        labels={
            "appClass": "my-deployment",
        },
    ),
    spec=kubernetes.apps.v1.DeploymentSpecArgs(
        replicas=2,
        selector=kubernetes.meta.v1.LabelSelectorArgs(
            match_labels={
                "appClass": "my-deployment",
            },
        ),
        template=kubernetes.core.v1.PodTemplateSpecArgs(
            metadata=kubernetes.meta.v1.ObjectMetaArgs(
                labels={
                    "appClass": "my-deployment",
                },
            ),
            spec=kubernetes.core.v1.PodSpecArgs(
                containers=[kubernetes.core.v1.ContainerArgs(
                    name="my-deployment",
                    image="nginx",
                    ports=[kubernetes.core.v1.ContainerPortArgs(
                        name="http",
                        container_port=80,
                    )],
                )],
            ),
        ),
    ),
    opts=pulumi.ResourceOptions(provider=eks_provider))
my_service = kubernetes.core.v1.Service("my-service",
    metadata=kubernetes.meta.v1.ObjectMetaArgs(
        labels={
            "appClass": "my-deployment",
        },
    ),
    spec=kubernetes.core.v1.ServiceSpecArgs(
        type="LoadBalancer",
        ports=[kubernetes.core.v1.ServicePortArgs(
            port=80,
            target_port="http",
        )],
        selector={
            "appClass": "my-deployment",
        },
    ),
    opts=pulumi.ResourceOptions(provider=eks_provider))

# Export the cluster's kubeconfig.
pulumi.export("kubeconfig", cluster.kubeconfig)
# Export the URL for the load balanced service.
pulumi.export("url", my_service.status.load_balancer.ingress[0].hostname)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-eks/sdk/go/eks"
	"github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes"
	appsv1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/apps/v1"
	corev1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/core/v1"
	metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/meta/v1"
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
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using Pulumi;
using Eks = Pulumi.Eks;
using Kubernetes = Pulumi.Kubernetes;

return await Deployment.RunAsync(() =>
{
    // Create an EKS cluster with the default configuration.
    var cluster = new Eks.Cluster("cluster");

    var eksProvider = new Kubernetes.Provider("eks-provider", new()
    {
        KubeConfig = cluster.KubeconfigJson,
    });

    // Deploy a small canary service (NGINX), to test that the cluster is working.
    var myDeployment = new Kubernetes.Apps.V1.Deployment("my-deployment", new()
    {
        Metadata = new Kubernetes.Types.Inputs.Meta.V1.ObjectMetaArgs
        {
            Labels =
            {
                { "appClass", "my-deployment" },
            },
        },
        Spec = new Kubernetes.Types.Inputs.Apps.V1.DeploymentSpecArgs
        {
            Replicas = 2,
            Selector = new Kubernetes.Types.Inputs.Meta.V1.LabelSelectorArgs
            {
                MatchLabels =
                {
                    { "appClass", "my-deployment" },
                },
            },
            Template = new Kubernetes.Types.Inputs.Core.V1.PodTemplateSpecArgs
            {
                Metadata = new Kubernetes.Types.Inputs.Meta.V1.ObjectMetaArgs
                {
                    Labels =
                    {
                        { "appClass", "my-deployment" },
                    },
                },
                Spec = new Kubernetes.Types.Inputs.Core.V1.PodSpecArgs
                {
                    Containers = new[]
                    {
                        new Kubernetes.Types.Inputs.Core.V1.ContainerArgs
                        {
                            Name = "my-deployment",
                            Image = "nginx",
                            Ports = new[]
                            {
                                new Kubernetes.Types.Inputs.Core.V1.ContainerPortArgs
                                {
                                    Name = "http",
                                    ContainerPortValue = 80,
                                },
                            },
                        },
                    },
                },
            },
        },
    }, new CustomResourceOptions
    {
        Provider = eksProvider,
    });

    var myService = new Kubernetes.Core.V1.Service("my-service", new()
    {
        Metadata = new Kubernetes.Types.Inputs.Meta.V1.ObjectMetaArgs
        {
            Labels =
            {
                { "appClass", "my-deployment" },
            },
        },
        Spec = new Kubernetes.Types.Inputs.Core.V1.ServiceSpecArgs
        {
            Type = "LoadBalancer",
            Ports = new[]
            {
                new Kubernetes.Types.Inputs.Core.V1.ServicePortArgs
                {
                    Port = 80,
                    TargetPort = "http",
                },
            },
            Selector =
            {
                { "appClass", "my-deployment" },
            },
        },
    }, new CustomResourceOptions
    {
        Provider = eksProvider,
    });

    return new Dictionary<string, object?>
    {
        // Export the cluster's kubeconfig.
        ["kubeconfig"] = cluster.Kubeconfig,
        // Export the URL for the load balanced service.
        ["url"] = myService.Status.Apply(status => status?.LoadBalancer?.Ingress[0]?.Hostname),
    };
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.pulumi.eks.Cluster;
import com.pulumi.kubernetes.Provider;
import com.pulumi.kubernetes.ProviderArgs;
import com.pulumi.kubernetes.apps.v1.Deployment;
import com.pulumi.kubernetes.apps.v1.DeploymentArgs;
import com.pulumi.kubernetes.meta.v1.inputs.ObjectMetaArgs;
import com.pulumi.kubernetes.apps.v1.inputs.DeploymentSpecArgs;
import com.pulumi.kubernetes.meta.v1.inputs.LabelSelectorArgs;
import com.pulumi.kubernetes.core.v1.inputs.PodTemplateSpecArgs;
import com.pulumi.kubernetes.core.v1.inputs.ServicePortArgs;
import com.pulumi.kubernetes.core.v1.inputs.ContainerArgs;
import com.pulumi.kubernetes.core.v1.inputs.ContainerPortArgs;
import com.pulumi.kubernetes.core.v1.inputs.PodSpecArgs;
import com.pulumi.kubernetes.core.v1.Service;
import com.pulumi.kubernetes.core.v1.ServiceArgs;
import com.pulumi.kubernetes.core.v1.inputs.ServiceSpecArgs;
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
        // Create an EKS cluster with the default configuration.
        var cluster = new Cluster("cluster");

        var eksProvider = new Provider("eksProvider", ProviderArgs.builder()
            .kubeconfig(cluster.kubeconfigJson())
            .build());

        // Deploy a small canary service (NGINX), to test that the cluster is working.
        var myDeployment = new Deployment("myDeployment", DeploymentArgs.builder()
            .metadata(ObjectMetaArgs.builder()
                .labels(Map.of("appClass", "my-deployment"))
                .build())
            .spec(DeploymentSpecArgs.builder()
                .replicas(2)
                .selector(LabelSelectorArgs.builder()
                    .matchLabels(Map.of("appClass", "my-deployment"))
                    .build())
                .template(PodTemplateSpecArgs.builder()
                    .metadata(ObjectMetaArgs.builder()
                        .labels(Map.of("appClass", "my-deployment"))
                        .build())
                    .spec(PodSpecArgs.builder()
                        .containers(ContainerArgs.builder()
                            .name("my-deployment")
                            .image("nginx")
                            .ports(ContainerPortArgs.builder()
                                .name("http")
                                .containerPort(80)
                                .build())
                            .build())
                        .build())
                    .build())
                .build())
            .build(), CustomResourceOptions.builder()
                .provider(eksProvider)
                .build());

        var myService = new Service("myService", ServiceArgs.builder()
            .metadata(ObjectMetaArgs.builder()
                .labels(Map.of("appClass", "my-deployment"))
                .build())
            .spec(ServiceSpecArgs.builder()
                .type("LoadBalancer")
                .ports(ServicePortArgs.builder()
                    .port(80)
                    .targetPort("http")
                    .build())
                .selector(Map.of("appClass", "my-deployment"))
                .build())
            .build(), CustomResourceOptions.builder()
                .provider(eksProvider)
                .build());

        // Export the cluster's kubeconfig.
        ctx.export("kubeconfig", cluster.kubeconfig());
        // Export the URL for the load balanced service.
        ctx.export("url", myService.status()
            .applyValue(status -> status.orElseThrow().loadBalancer().orElseThrow())
            .applyValue(status -> status.ingress().get(0).hostname().orElseThrow()));
    }
}
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  # Create an EKS cluster with the default configuration.
  cluster:
    type: eks:Cluster
  eks-provider:
    type: pulumi:providers:kubernetes
    properties:
      kubeconfig: ${cluster.kubeconfigJson}
  # Deploy a small canary service (NGINX), to test that the cluster is working.
  my-deployment:
    type: kubernetes:apps/v1:Deployment
    properties:
      metadata:
        labels:
          appClass: my-deployment
      spec:
        replicas: 2
        selector:
          matchLabels:
            appClass: my-deployment
        template:
          metadata:
            labels:
              appClass: my-deployment
          spec:
            containers:
              - name: my-deployment
                image: nginx
                ports:
                  - name: http
                    containerPort: 80
    options:
      provider: ${eks-provider}
  my-service:
    type: kubernetes:core/v1:Service
    properties:
      metadata:
        labels:
          appClass: my-deployment
      spec:
        type: LoadBalancer
        ports:
          - port: 80
            targetPort: http
        selector:
          appClass: my-deployment
    options:
      provider: ${eks-provider}
outputs:
  # Export the cluster's kubeconfig.
  kubeconfig: ${cluster.kubeconfig}
  # Export the URL for the load balanced service.
  url: ${my-service.status.loadBalancer.ingress[0].hostname}
```

{{% /choosable %}}

If we deploy this on top of our existing EKS cluster, we will see the diff is just the creation of Kubernetes
Deployment and Service objects, and the resulting URL for the load balanced service will be printed out. We
can see that Pods have been spun up and we can use this URL to check the health of our cluster:

```bash
$ pulumi stack output kubeconfig > kubeconfig.yml
$ KUBECONFIG=./kubeconfig.yml kubectl get po
NAME                                 READY     STATUS    RESTARTS   AGE
my-app-de-6gfz4ap5-dc8c6584f-6xmcl   1/1       Running   0          3m
my-app-de-6gfz4ap5-dc8c6584f-wzlf9   1/1       Running   0          3m
$ curl http://$(pulumi stack output url)
<html>
<head>
<title>Welcome to nginx!</title>
</head>
<body>
<h1>Welcome to nginx!</h1>
</body>
</html>
```

For more detail on how to deploy Kubernetes applications using Pulumi, refer to one of these sections:

* [Deploying Kubernetes Apps to Your EKS Cluster](#deploying-kubernetes-apps-to-your-eks-cluster)
* [Deploying Existing Kubernetes YAML Config to Your EKS Cluster](#deploying-existing-kubernetes-yaml-config-to-your-eks-cluster)
* [Deploying Existing Helm Charts to Your EKS Cluster](#deploying-existing-helm-charts-to-your-eks-cluster)

## Changing the Default Settings on an EKS Cluster

The above example showed using the default settings for your EKS cluster. It is easy to override them by passing
arguments to the constructor. For instance, this example changes the desired capacity and enables certain cluster
logging types:

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as eks from "@pulumi/eks";

// Create an EKS cluster with a modified configuration.
const cluster = new eks.Cluster("cluster", {
    desiredCapacity: 5,
    minSize: 3,
    maxSize: 5,
    enabledClusterLogTypes: [
        "api",
        "audit",
        "authenticator",
    ],
});

// Export the cluster's kubeconfig.
export const kubeconfig = cluster.kubeconfig;
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
import pulumi_eks as eks

# Create an EKS cluster with a modified configuration.
cluster = eks.Cluster("cluster",
    desired_capacity=5,
    min_size=3,
    max_size=5,
    enabled_cluster_log_types=[
        "api",
        "audit",
        "authenticator",
    ])

# Export the cluster's kubeconfig.
pulumi.export("kubeconfig", cluster.kubeconfig)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-eks/sdk/go/eks"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Create an EKS cluster with a modified configuration.
		cluster, err := eks.NewCluster(ctx, "cluster", &eks.ClusterArgs{
			DesiredCapacity: pulumi.Int(5),
			MinSize:         pulumi.Int(3),
			MaxSize:         pulumi.Int(5),
			EnabledClusterLogTypes: pulumi.StringArray{
				pulumi.String("api"),
				pulumi.String("audit"),
				pulumi.String("authenticator"),
			},
		})
		if err != nil {
			return err
		}

		// Export the cluster's kubeconfig.
		ctx.Export("kubeconfig", cluster.Kubeconfig)
		return nil
	})
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using Pulumi;
using Eks = Pulumi.Eks;

return await Deployment.RunAsync(() =>
{
    // Create an EKS cluster with a modified configuration.
    var cluster = new Eks.Cluster("cluster", new()
    {
        DesiredCapacity = 5,
        MinSize = 3,
        MaxSize = 5,
        EnabledClusterLogTypes = new[]
        {
            "api",
            "audit",
            "authenticator",
        },
    });

    return new Dictionary<string, object?>
    {
        // Export the cluster's kubeconfig.
        ["kubeconfig"] = cluster.Kubeconfig,
    };
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.pulumi.eks.Cluster;
import com.pulumi.eks.ClusterArgs;
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
        // Create an EKS cluster with a modified configuration.
        var cluster = new Cluster("cluster", ClusterArgs.builder()
            .desiredCapacity(5)
            .minSize(3)
            .maxSize(5)
            .enabledClusterLogTypes(
                "api",
                "audit",
                "authenticator")
            .build());

        // Export the cluster's kubeconfig.
        ctx.export("kubeconfig", cluster.kubeconfig());
    }
}
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  # Create an EKS cluster with a modified configuration.
  cluster:
    type: eks:Cluster
    properties:
      desiredCapacity: 5
      minSize: 3
      maxSize: 5
      enabledClusterLogTypes:
      - api
      - audit
      - authenticator
outputs:
  # Export the cluster's kubeconfig.
  kubeconfig: ${cluster.kubeconfig}
```

{{% /choosable %}}

For a full list of options that you may set on your cluster, see the [API documentation](/registry/packages/eks/api-docs/cluster/#inputs). Many common cases are described below.

## Configuring Your EKS Cluster's Networking

By default, your EKS cluster is put into your region's default VPC. This is a reasonable default, however this is
configurable if you want specific network isolation or to place your cluster work nodes on private subnets. This works
in conjunction with [Pulumi Crosswalk for AWS VPC](/docs/guides/crosswalk/aws/vpc/) which makes configuring VPCs easier.

This example creates a new VPC with private subnets only and creates our EKS cluster inside of it:

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as awsx from "@pulumi/awsx";
import * as eks from "@pulumi/eks";

// Create a VPC for our cluster.
const vpc = new awsx.ec2.Vpc("vpc", {});

// Create an EKS cluster inside of the VPC.
const cluster = new eks.Cluster("cluster", {
    vpcId: vpc.vpcId,
    publicSubnetIds: vpc.publicSubnetIds,
    privateSubnetIds: vpc.privateSubnetIds,
    nodeAssociatePublicIpAddress: false,
});

// Export the cluster's kubeconfig.
export const kubeconfig = cluster.kubeconfig;
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
import pulumi_awsx as awsx
import pulumi_eks as eks

# Create a VPC for our cluster.
vpc = awsx.ec2.Vpc("vpc")

# Create an EKS cluster inside of the VPC.
cluster = eks.Cluster("cluster",
    vpc_id=vpc.vpc_id,
    public_subnet_ids=vpc.public_subnet_ids,
    private_subnet_ids=vpc.private_subnet_ids,
    node_associate_public_ip_address=False)

# Export the cluster's kubeconfig.
pulumi.export("kubeconfig", cluster.kubeconfig)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-awsx/sdk/go/awsx/ec2"
	"github.com/pulumi/pulumi-eks/sdk/go/eks"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Create a VPC for our cluster.
		vpc, err := ec2.NewVpc(ctx, "vpc", nil)
		if err != nil {
			return err
		}

		// Create an EKS cluster inside of the VPC.
		cluster, err := eks.NewCluster(ctx, "cluster", &eks.ClusterArgs{
			VpcId:                        vpc.VpcId,
			PublicSubnetIds:              vpc.PublicSubnetIds,
			PrivateSubnetIds:             vpc.PrivateSubnetIds,
			NodeAssociatePublicIpAddress: pulumi.BoolRef(false),
		})
		if err != nil {
			return err
		}

		// Export the cluster's kubeconfig.
		ctx.Export("kubeconfig", cluster.Kubeconfig)
		return nil
	})
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using Pulumi;
using Awsx = Pulumi.Awsx;
using Eks = Pulumi.Eks;

return await Deployment.RunAsync(() =>
{
    // Create a VPC for our cluster.
    var vpc = new Awsx.Ec2.Vpc("vpc");

    // Create an EKS cluster inside of the VPC.
    var cluster = new Eks.Cluster("cluster", new()
    {
        VpcId = vpc.VpcId,
        PublicSubnetIds = vpc.PublicSubnetIds,
        PrivateSubnetIds = vpc.PrivateSubnetIds,
        NodeAssociatePublicIpAddress = false,
    });

    // Export the cluster's kubeconfig.
    return new Dictionary<string, object?>
    {
        ["kubeconfig"] = cluster.Kubeconfig,
    };
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.pulumi.awsx.ec2.Vpc;
import com.pulumi.eks.Cluster;
import com.pulumi.eks.ClusterArgs;
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
        // Create a VPC for our cluster.
        var vpc = new Vpc("vpc");

        // Create an EKS cluster inside of the VPC.
        var cluster = new Cluster("cluster", ClusterArgs.builder()
            .vpcId(vpc.vpcId())
            .publicSubnetIds(vpc.publicSubnetIds())
            .privateSubnetIds(vpc.privateSubnetIds())
            .nodeAssociatePublicIpAddress(false)
            .build());

        // Export the cluster's kubeconfig.
        ctx.export("kubeconfig", cluster.kubeconfig());
    }
}
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  # Create a VPC for our cluster.
  vpc:
    type: awsx:ec2:Vpc
  # Create an EKS cluster within the VPC.
  cluster:
    type: eks:Cluster
    properties:
      vpcId: ${vpc.vpcId}
      publicSubnetIds: ${vpc.publicSubnetIds}
      privateSubnetIds: ${vpc.privateSubnetIds}
      nodeAssociatePublicIpAddress: false
outputs:
  # Export the cluster's kubeconfig.
  kubeconfig: ${cluster.kubeconfig}

```

{{% /choosable %}}

When you create an Amazon EKS cluster, you specify the Amazon VPC subnets for your cluster to use. These must be
in at least two Availability Zones. We recommend a network architecture that uses private subnets for your
worker nodes and public subnets for Kubernetes to create Internet-facing load balancers within. When you create your
cluster, specify all of the subnets that will host resources for your cluster (including workers and load balancers).

In the above example, we passed both the private and public subnets from our VPC. The EKS package
figures out which ones are public and which ones are private -- and creates the worker nodes inside
only the private subnets if any are specified. EKS will tag the provided subnets so that Kubernetes
can discover them.   If additional control is needed over how load balancers are allocated to
subnets, users can attach additional subnet tags themselves as outlined in
[Cluster VPC Considerations](https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html).

> Note that by default the `eks.Cluster` will do the same as what is described here, just inside of the default
> VPC inside of your account, rather than a custom VPC as shown in this example.

## Configuring Your EKS Cluster's Worker Nodes and Node Groups

Worker machines in Kubernetes are called nodes. Amazon EKS worker nodes run in your AWS account and connect to your
cluster's control plane via the cluster API server endpoint. These are standard Amazon EC2 instances, and you are
billed for them based on normal EC2 On-Demand prices. By default, an AMI using Amazon Linux 2 is used as the base
image for EKS worker nodes, and includes Docker, kubelet, and the AWS IAM Authenticator.

Nodes exist in groups and you can create multiple groups for workloads that require it. By default, your EKS cluster
is given a default node group, with the instance sizes and counts that you specify (or the defaults of two `t2.medium`
instances otherwise). The latest version of Kubernetes available is used by default.

If you would like to disable the creation of a default node group, and instead rely on creating your own, pass
[`skipDefaultNodeGroup`](/registry/packages/eks/api-docs/cluster/#skipdefaultnodegroup_nodejs)
as `true` to the `eks.Cluster` constructor. Additional node groups may then be created by
[creating an `eks.NodeGroupV2`](/registry/packages/eks/api-docs/nodegroupv2) explicitly. In both cases, you
are likely to want to configure IAM roles for your worker nodes explicitly, which can besupplied to your EKS cluster
using the [`instanceRole`](/registry/packages/eks/api-docs/cluster/#instancerole_nodejs) or
[`instanceRoles`](/registry/packages/eks/api-docs/cluster/#instanceroles_nodejs) properties.

For instance, let's say we want to have two node groups: one for our fixed, known workloads, and another that is
burstable and might use more expensive compute, but which can be scaled down when possible (possibly to zero).
We would skip the default node group, and create our own node groups:

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import * as eks from "@pulumi/eks";

const managedPolicyArns = [
    "arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy",
    "arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy",
    "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly",
];
const assumeRolePolicy = JSON.stringify({
    Version: "2012-10-17",
    Statement: [{
        Action: "sts:AssumeRole",
        Effect: "Allow",
        Sid: undefined,
        Principal: {
            Service: "ec2.amazonaws.com",
        },
    }],
});
const role1 = new aws.iam.Role("role1", {
    assumeRolePolicy: assumeRolePolicy,
    managedPolicyArns: managedPolicyArns,
});
const role2 = new aws.iam.Role("role2", {
    assumeRolePolicy: assumeRolePolicy,
    managedPolicyArns: managedPolicyArns,
});
const instanceProfile1 = new aws.iam.InstanceProfile("instanceProfile1", {role: role1.name});
const instanceProfile2 = new aws.iam.InstanceProfile("instanceProfile2", {role: role2.name});
const cluster = new eks.Cluster("cluster", {
    skipDefaultNodeGroup: true,
    instanceRoles: undefined,
});
const fixedNodeGroup = new eks.NodeGroupV2("fixedNodeGroup", {
    cluster: cluster,
    instanceType: "t2.medium",
    desiredCapacity: 2,
    minSize: 1,
    maxSize: 3,
    spotPrice: "1",
    labels: {
        ondemand: "true",
    },
    instanceProfile: instanceProfile1,
});
const spotNodeGroup = new eks.NodeGroupV2("spotNodeGroup", {
    cluster: cluster,
    instanceType: "t2.medium",
    desiredCapacity: 1,
    minSize: 1,
    maxSize: 2,
    labels: {
        preemptible: "true",
    },
    instanceProfile: instanceProfile2,
});
export const kubeconfig = cluster.kubeconfig;
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
import json
import pulumi_aws as aws
import pulumi_eks as eks

managed_policy_arns = [
    "arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy",
    "arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy",
    "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly",
]
assume_role_policy = json.dumps({
    "Version": "2012-10-17",
    "Statement": [{
        "Action": "sts:AssumeRole",
        "Effect": "Allow",
        "Sid": None,
        "Principal": {
            "Service": "ec2.amazonaws.com",
        },
    }],
})
role1 = aws.iam.Role("role1",
    assume_role_policy=assume_role_policy,
    managed_policy_arns=managed_policy_arns)
role2 = aws.iam.Role("role2",
    assume_role_policy=assume_role_policy,
    managed_policy_arns=managed_policy_arns)
instance_profile1 = aws.iam.InstanceProfile("instanceProfile1", role=role1.name)
instance_profile2 = aws.iam.InstanceProfile("instanceProfile2", role=role2.name)
cluster = eks.Cluster("cluster",
    skip_default_node_group=True,
    instance_roles=None)
fixed_node_group = eks.NodeGroupV2("fixedNodeGroup",
    cluster=cluster,
    instance_type="t2.medium",
    desired_capacity=2,
    min_size=1,
    max_size=3,
    spot_price="1",
    labels={
        "ondemand": "true",
    },
    instance_profile=instance_profile1)
spot_node_group = eks.NodeGroupV2("spotNodeGroup",
    cluster=cluster,
    instance_type="t2.medium",
    desired_capacity=1,
    min_size=1,
    max_size=2,
    labels={
        "preemptible": "true",
    },
    instance_profile=instance_profile2)
pulumi.export("kubeconfig", cluster.kubeconfig)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
	"encoding/json"

	"github.com/pulumi/pulumi-aws/sdk/v5/go/aws/iam"
	"github.com/pulumi/pulumi-eks/sdk/go/eks"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		managedPolicyArns := []string{
			"arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy",
			"arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy",
			"arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly",
		}
		tmpJSON0, err := json.Marshal(map[string]interface{}{
			"Version": "2012-10-17",
			"Statement": []map[string]interface{}{
				map[string]interface{}{
					"Action": "sts:AssumeRole",
					"Effect": "Allow",
					"Sid":    nil,
					"Principal": map[string]interface{}{
						"Service": "ec2.amazonaws.com",
					},
				},
			},
		})
		if err != nil {
			return err
		}
		json0 := string(tmpJSON0)
		assumeRolePolicy := json0
		role1, err := iam.NewRole(ctx, "role1", &iam.RoleArgs{
			AssumeRolePolicy:  pulumi.String(assumeRolePolicy),
			ManagedPolicyArns: pulumi.ToStringArray(managedPolicyArns),
		})
		if err != nil {
			return err
		}
		role2, err := iam.NewRole(ctx, "role2", &iam.RoleArgs{
			AssumeRolePolicy:  pulumi.String(assumeRolePolicy),
			ManagedPolicyArns: pulumi.ToStringArray(managedPolicyArns),
		})
		if err != nil {
			return err
		}
		instanceProfile1, err := iam.NewInstanceProfile(ctx, "instanceProfile1", &iam.InstanceProfileArgs{
			Role: role1.Name,
		})
		if err != nil {
			return err
		}
		instanceProfile2, err := iam.NewInstanceProfile(ctx, "instanceProfile2", &iam.InstanceProfileArgs{
			Role: role2.Name,
		})
		if err != nil {
			return err
		}
		cluster, err := eks.NewCluster(ctx, "cluster", &eks.ClusterArgs{
			SkipDefaultNodeGroup: pulumi.BoolRef(true),
			InstanceRoles:        nil,
		})
		if err != nil {
			return err
		}
		_, err = eks.NewNodeGroupV2(ctx, "fixedNodeGroup", &eks.NodeGroupV2Args{
			Cluster:         cluster,
			InstanceType:    pulumi.String("t2.medium"),
			DesiredCapacity: pulumi.Int(2),
			MinSize:         pulumi.Int(1),
			MaxSize:         pulumi.Int(3),
			SpotPrice:       pulumi.String("1"),
			Labels: map[string]string{
				"ondemand": "true",
			},
			InstanceProfile: instanceProfile1,
		})
		if err != nil {
			return err
		}
		_, err = eks.NewNodeGroupV2(ctx, "spotNodeGroup", &eks.NodeGroupV2Args{
			Cluster:         cluster,
			InstanceType:    pulumi.String("t2.medium"),
			DesiredCapacity: pulumi.Int(1),
			MinSize:         pulumi.Int(1),
			MaxSize:         pulumi.Int(2),
			Labels: map[string]string{
				"preemptible": "true",
			},
			InstanceProfile: instanceProfile2,
		})
		if err != nil {
			return err
		}
		ctx.Export("kubeconfig", cluster.Kubeconfig)
		return nil
	})
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using System.Text.Json;
using Pulumi;
using Aws = Pulumi.Aws;
using Eks = Pulumi.Eks;

return await Deployment.RunAsync(() =>
{
    var managedPolicyArns = new[]
    {
        "arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy",
        "arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy",
        "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly",
    };

    var assumeRolePolicy = JsonSerializer.Serialize(new Dictionary<string, object?>
    {
        ["Version"] = "2012-10-17",
        ["Statement"] = new[]
        {
            new Dictionary<string, object?>
            {
                ["Action"] = "sts:AssumeRole",
                ["Effect"] = "Allow",
                ["Sid"] = null,
                ["Principal"] = new Dictionary<string, object?>
                {
                    ["Service"] = "ec2.amazonaws.com",
                },
            },
        },
    });

    var role1 = new Aws.Iam.Role("role1", new()
    {
        AssumeRolePolicy = assumeRolePolicy,
        ManagedPolicyArns = managedPolicyArns,
    });

    var role2 = new Aws.Iam.Role("role2", new()
    {
        AssumeRolePolicy = assumeRolePolicy,
        ManagedPolicyArns = managedPolicyArns,
    });

    var instanceProfile1 = new Aws.Iam.InstanceProfile("instanceProfile1", new()
    {
        Role = role1.Name,
    });

    var instanceProfile2 = new Aws.Iam.InstanceProfile("instanceProfile2", new()
    {
        Role = role2.Name,
    });

    var cluster = new Eks.Cluster("cluster", new()
    {
        SkipDefaultNodeGroup = true,
        InstanceRoles = null,
    });

    var fixedNodeGroup = new Eks.NodeGroupV2("fixedNodeGroup", new()
    {
        Cluster = cluster,
        InstanceType = "t2.medium",
        DesiredCapacity = 2,
        MinSize = 1,
        MaxSize = 3,
        SpotPrice = "1",
        Labels =
        {
            { "ondemand", "true" },
        },
        InstanceProfile = instanceProfile1,
    });

    var spotNodeGroup = new Eks.NodeGroupV2("spotNodeGroup", new()
    {
        Cluster = cluster,
        InstanceType = "t2.medium",
        DesiredCapacity = 1,
        MinSize = 1,
        MaxSize = 2,
        Labels =
        {
            { "preemptible", "true" },
        },
        InstanceProfile = instanceProfile2,
    });

    return new Dictionary<string, object?>
    {
        ["kubeconfig"] = cluster.Kubeconfig,
    };
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.pulumi.aws.iam.Role;
import com.pulumi.aws.iam.RoleArgs;
import com.pulumi.aws.iam.InstanceProfile;
import com.pulumi.aws.iam.InstanceProfileArgs;
import com.pulumi.eks.Cluster;
import com.pulumi.eks.ClusterArgs;
import com.pulumi.eks.NodeGroupV2;
import com.pulumi.eks.NodeGroupV2Args;
import static com.pulumi.codegen.internal.Serialization.*;
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
        final var managedPolicyArns = List.of(
            "arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy",
            "arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy",
            "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly"
        );

        final var assumeRolePolicy = serializeJson(
            jsonObject(
                jsonProperty("Version", "2012-10-17"),
                jsonProperty("Statement", jsonArray(jsonObject(
                    jsonProperty("Action", "sts:AssumeRole"),
                    jsonProperty("Effect", "Allow"),
                    jsonProperty("Sid", null),
                    jsonProperty("Principal", jsonObject(
                        jsonProperty("Service", "ec2.amazonaws.com")
                    ))
                )))
            ));

        var role1 = new Role("role1", RoleArgs.builder()
            .assumeRolePolicy(assumeRolePolicy)
            .managedPolicyArns(managedPolicyArns)
            .build());

        var role2 = new Role("role2", RoleArgs.builder()
            .assumeRolePolicy(assumeRolePolicy)
            .managedPolicyArns(managedPolicyArns)
            .build());

        var instanceProfile1 = new InstanceProfile("instanceProfile1", InstanceProfileArgs.builder()
            .role(role1.name())
            .build());

        var instanceProfile2 = new InstanceProfile("instanceProfile2", InstanceProfileArgs.builder()
            .role(role2.name())
            .build());

        var cluster = new Cluster("cluster", ClusterArgs.builder()
            .skipDefaultNodeGroup(true)
            .instanceRoles(List.of(role1, role2))
            .build());

        var fixedNodeGroup = new NodeGroupV2("fixedNodeGroup", NodeGroupV2Args.builder()
            .cluster(cluster)
            .instanceType("t2.medium")
            .desiredCapacity(2)
            .minSize(1)
            .maxSize(3)
            .spotPrice("1")
            .labels(Map.of("ondemand", "true"))
            .instanceProfile(instanceProfile1)
            .build());

        var spotNodeGroup = new NodeGroupV2("spotNodeGroup", NodeGroupV2Args.builder()
            .cluster(cluster)
            .instanceType("t2.medium")
            .desiredCapacity(1)
            .minSize(1)
            .maxSize(2)
            .labels(Map.of("preemptible", "true"))
            .instanceProfile(instanceProfile2)
            .build());

        ctx.export("kubeconfig", cluster.kubeconfig());
    }
}
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
variables:
  managedPolicyArns:
  - arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy
  - arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy
  - arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly
  assumeRolePolicy:
    fn::toJSON:
      Version: 2012-10-17
      Statement:
        - Action: sts:AssumeRole
          Effect: Allow
          Sid:
          Principal:
            Service: ec2.amazonaws.com
resources:
  # Create instance profiles for the two node groups.
  role1:
    type: aws:iam:Role
    properties:
      assumeRolePolicy: ${assumeRolePolicy}
      managedPolicyArns: ${managedPolicyArns}
  role2:
    type: aws:iam:Role
    properties:
      assumeRolePolicy: ${assumeRolePolicy}
      managedPolicyArns: ${managedPolicyArns}
  instanceProfile1:
    type: aws:iam:InstanceProfile
    properties:
      role: ${role1.name}
  instanceProfile2:
    type: aws:iam:InstanceProfile
    properties:
      role: ${role2.name}
  # Create an EKS cluster with the IAM roles, and with no default node group.
  cluster:
    type: eks:Cluster
    properties:
      skipDefaultNodeGroup: true
      instanceRoles:
  # Create a node group for fixed compute.
  fixedNodeGroup:
    type: eks:NodeGroupV2
    properties:
      cluster: ${cluster}
      instanceType: t2.medium
      desiredCapacity: 2
      minSize: 1
      maxSize: 3
      spotPrice: "1"
      labels:
        ondemand: true
      instanceProfile: ${instanceProfile1}
  # Create a preemptible node group using spot pricing for our ephemeral workloads.
  spotNodeGroup:
    type: eks:NodeGroupV2
    properties:
      cluster: ${cluster}
      instanceType: t2.medium
      desiredCapacity: 1
      minSize: 1
      maxSize: 2
      labels:
        preemptible: 'true'
      instanceProfile: ${instanceProfile2}
outputs:
  # Export the cluster's kubeconfig.
  kubeconfig: ${cluster.kubeconfig}
```

{{% /choosable %}}

After configuring such a cluster, we would then want to ensure our workload's pods are scheduled correctly on the
right nodes. To do so, you will use a combination of node selectors, taints, and/or tolerances. For more information,
see [Assigning Pods to Nodes](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/) and
[Taints and Tolerances](https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/).

## Managing EKS Cluster Authentication with IAM

When you create an Amazon EKS cluster, the IAM entity user or role (for example, for federated users) that creates the
cluster is automatically granted `system:masters` permissions in the cluster's RBAC configuration. To grant additional
AWS users or roles the ability to interact with your cluster, you must edit the `aws-auth` ConfigMap within Kubernetes.

The [`roleMappings` property](https://www.pulumi.com/registry/packages/eks/api-docs/cluster/#rolemappings_nodejs)
for your EKS cluster lets you configure custom IAM roles. For example, you can create different IAM roles for cluster
admins, automation accounts (for CI/CD), and production roles, and supply them to `roleMappings`; this has the effect of
placing them in the `aws-auth` ConfigMap for your cluster automatically. Pulumi also lets you configure Kubernetes
objects, so that can also then create the RBAC cluster role bindings in your cluster to tie everything together.

For a complete example of this in action, see
[Simplifying Kubernetes RBAC in Amazon EKS](/blog/simplify-kubernetes-rbac-in-amazon-eks-with-open-source-pulumi-packages/).

## Deploying Kubernetes Apps to Your EKS Cluster

Pulumi supports the entire Kubernetes object model in the [@pulumi/kubernetes](/registry/packages/kubernetes/api-docs)
package. For more information on these object types, including Deployments, Services, and Pods, see
[Understanding Kubernetes Objects](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/).

With Pulumi, you describe your desired Kubernetes configuration, and `pulumi up` will diff between the current
state and what is desired, and then drive the API server to bring your desired state into existence.

For example, this program creates a simple load balanced NGINX service, exporting its URL:

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as kubernetes from "@pulumi/kubernetes";

// Create an NGINX Deployment and load balanced Service.
const myDeployment = new kubernetes.apps.v1.Deployment("my-deployment", {
    metadata: {
        labels: {
            appClass: "my-deployment",
        },
    },
    spec: {
        replicas: 2,
        selector: {
            matchLabels: {
                appClass: "my-deployment",
            },
        },
        template: {
            metadata: {
                labels: {
                    appClass: "my-deployment",
                },
            },
            spec: {
                containers: [{
                    name: "my-deployment",
                    image: "nginx",
                    ports: [{
                        name: "http",
                        containerPort: 80,
                    }],
                }],
            },
        },
    },
});
const myService = new kubernetes.core.v1.Service("my-service", {
    metadata: {
        labels: {
            appClass: "my-deployment",
        },
    },
    spec: {
        type: "LoadBalancer",
        ports: [{
            port: 80,
            targetPort: "http",
        }],
        selector: {
            appClass: "my-deployment",
        },
    },
});

// Export the URL for the load balanced service.
export const url = myService.status.apply(status => status?.loadBalancer?.ingress[0]?.hostname);

```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
import pulumi_kubernetes as kubernetes

# Create an NGINX Deployment and load balanced Service.
my_deployment = kubernetes.apps.v1.Deployment("my-deployment",
    metadata=kubernetes.meta.v1.ObjectMetaArgs(
        labels={
            "appClass": "my-deployment",
        },
    ),
    spec=kubernetes.apps.v1.DeploymentSpecArgs(
        replicas=2,
        selector=kubernetes.meta.v1.LabelSelectorArgs(
            match_labels={
                "appClass": "my-deployment",
            },
        ),
        template=kubernetes.core.v1.PodTemplateSpecArgs(
            metadata=kubernetes.meta.v1.ObjectMetaArgs(
                labels={
                    "appClass": "my-deployment",
                },
            ),
            spec=kubernetes.core.v1.PodSpecArgs(
                containers=[kubernetes.core.v1.ContainerArgs(
                    name="my-deployment",
                    image="nginx",
                    ports=[kubernetes.core.v1.ContainerPortArgs(
                        name="http",
                        container_port=80,
                    )],
                )],
            ),
        ),
    ))
my_service = kubernetes.core.v1.Service("my-service",
    metadata=kubernetes.meta.v1.ObjectMetaArgs(
        labels={
            "appClass": "my-deployment",
        },
    ),
    spec=kubernetes.core.v1.ServiceSpecArgs(
        type="LoadBalancer",
        ports=[kubernetes.core.v1.ServicePortArgs(
            port=80,
            target_port="http",
        )],
        selector={
            "appClass": "my-deployment",
        },
    ))

# Export the URL for the load balanced service.
pulumi.export("url", my_service.status.load_balancer.ingress[0].hostname)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
	appsv1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/apps/v1"
	corev1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/core/v1"
	metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/meta/v1"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Create an NGINX Deployment and load balanced Service.
		_, err := appsv1.NewDeployment(ctx, "my-deployment", &appsv1.DeploymentArgs{
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
		})
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
		})
		if err != nil {
			return err
		}
		// Export the URL for the load balanced service.
		ctx.Export("url", myService.Status.ApplyT(func(status interface{}) (string, error) {
			return *status.(*corev1.ServiceStatus).LoadBalancer.Ingress[0].Hostname, nil
		}).(pulumi.StringOutput))
		return nil
	})
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using Pulumi;
using Kubernetes = Pulumi.Kubernetes;

return await Deployment.RunAsync(() =>
{
    // Create an NGINX Deployment and load balanced Service.
    var myDeployment = new Kubernetes.Apps.V1.Deployment("my-deployment", new()
    {
        Metadata = new Kubernetes.Types.Inputs.Meta.V1.ObjectMetaArgs
        {
            Labels =
            {
                { "appClass", "my-deployment" },
            },
        },
        Spec = new Kubernetes.Types.Inputs.Apps.V1.DeploymentSpecArgs
        {
            Replicas = 2,
            Selector = new Kubernetes.Types.Inputs.Meta.V1.LabelSelectorArgs
            {
                MatchLabels =
                {
                    { "appClass", "my-deployment" },
                },
            },
            Template = new Kubernetes.Types.Inputs.Core.V1.PodTemplateSpecArgs
            {
                Metadata = new Kubernetes.Types.Inputs.Meta.V1.ObjectMetaArgs
                {
                    Labels =
                    {
                        { "appClass", "my-deployment" },
                    },
                },
                Spec = new Kubernetes.Types.Inputs.Core.V1.PodSpecArgs
                {
                    Containers = new[]
                    {
                        new Kubernetes.Types.Inputs.Core.V1.ContainerArgs
                        {
                            Name = "my-deployment",
                            Image = "nginx",
                            Ports = new[]
                            {
                                new Kubernetes.Types.Inputs.Core.V1.ContainerPortArgs
                                {
                                    Name = "http",
                                    ContainerPortValue = 80,
                                },
                            },
                        },
                    },
                },
            },
        },
    });

    var myService = new Kubernetes.Core.V1.Service("my-service", new()
    {
        Metadata = new Kubernetes.Types.Inputs.Meta.V1.ObjectMetaArgs
        {
            Labels =
            {
                { "appClass", "my-deployment" },
            },
        },
        Spec = new Kubernetes.Types.Inputs.Core.V1.ServiceSpecArgs
        {
            Type = "LoadBalancer",
            Ports = new[]
            {
                new Kubernetes.Types.Inputs.Core.V1.ServicePortArgs
                {
                    Port = 80,
                    TargetPort = "http",
                },
            },
            Selector =
            {
                { "appClass", "my-deployment" },
            },
        },
    });

    // Export the URL for the load balanced service.
    return new Dictionary<string, object?>
    {
        ["url"] = myService.Status.Apply(status => status?.LoadBalancer?.Ingress[0]?.Hostname),
    };
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.pulumi.kubernetes.apps.v1.Deployment;
import com.pulumi.kubernetes.apps.v1.DeploymentArgs;
import com.pulumi.kubernetes.meta.v1.inputs.ObjectMetaArgs;
import com.pulumi.kubernetes.apps.v1.inputs.DeploymentSpecArgs;
import com.pulumi.kubernetes.meta.v1.inputs.LabelSelectorArgs;
import com.pulumi.kubernetes.core.v1.inputs.PodTemplateSpecArgs;
import com.pulumi.kubernetes.core.v1.inputs.ServicePortArgs;
import com.pulumi.kubernetes.core.v1.inputs.ContainerArgs;
import com.pulumi.kubernetes.core.v1.inputs.ContainerPortArgs;
import com.pulumi.kubernetes.core.v1.inputs.PodSpecArgs;
import com.pulumi.kubernetes.core.v1.Service;
import com.pulumi.kubernetes.core.v1.ServiceArgs;
import com.pulumi.kubernetes.core.v1.inputs.ServiceSpecArgs;
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
        // Create an NGINX Deployment and load balanced Service.
        var myDeployment = new Deployment("myDeployment", DeploymentArgs.builder()
            .metadata(ObjectMetaArgs.builder()
                .labels(Map.of("appClass", "my-deployment"))
                .build())
            .spec(DeploymentSpecArgs.builder()
                .replicas(2)
                .selector(LabelSelectorArgs.builder()
                    .matchLabels(Map.of("appClass", "my-deployment"))
                    .build())
                .template(PodTemplateSpecArgs.builder()
                    .metadata(ObjectMetaArgs.builder()
                        .labels(Map.of("appClass", "my-deployment"))
                        .build())
                    .spec(PodSpecArgs.builder()
                        .containers(ContainerArgs.builder()
                            .name("my-deployment")
                            .image("nginx")
                            .ports(ContainerPortArgs.builder()
                                .name("http")
                                .containerPort(80)
                                .build())
                            .build())
                        .build())
                    .build())
                .build())
            .build());

        var myService = new Service("myService", ServiceArgs.builder()
            .metadata(ObjectMetaArgs.builder()
                .labels(Map.of("appClass", "my-deployment"))
                .build())
            .spec(ServiceSpecArgs.builder()
                .type("LoadBalancer")
                .ports(ServicePortArgs.builder()
                    .port(80)
                    .targetPort("http")
                    .build())
                .selector(Map.of("appClass", "my-deployment"))
                .build())
            .build());

        // Export the URL for the load balanced service.
        ctx.export("url", myService.status()
            .applyValue(status -> status.orElseThrow().loadBalancer().orElseThrow())
            .applyValue(status -> status.ingress().get(0).hostname().orElseThrow()));
    }
}
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  # Deploy an NGINX deployment and load balanced service.
  my-deployment:
    type: kubernetes:apps/v1:Deployment
    properties:
      metadata:
        labels:
          appClass: my-deployment
      spec:
        replicas: 2
        selector:
          matchLabels:
            appClass: my-deployment
        template:
          metadata:
            labels:
              appClass: my-deployment
          spec:
            containers:
              - name: my-deployment
                image: nginx
                ports:
                  - name: http
                    containerPort: 80
  my-service:
    type: kubernetes:core/v1:Service
    properties:
      metadata:
        labels:
          appClass: my-deployment
      spec:
        type: LoadBalancer
        ports:
          - port: 80
            targetPort: http
        selector:
          appClass: my-deployment
outputs:
  # Export the URL for the load balanced service.
  url: ${my-service.status.loadBalancer.ingress[0].hostname}
```

{{% /choosable %}}

Running `pulumi up` deploys these Kubernetes objects, providing rich status updates along the way:

```bash
Updating (dev):

     Type                           Name               Status
     pulumi:pulumi:Stack            crosswalk-aws-dev
 +   ├─ kubernetes:core:Service     my-app-svc         created
 +   └─ kubernetes:apps:Deployment  my-app-dep         created

Outputs:
 + url       : "a2861638e011e98a329401e61c-1335818318.us-west-2.elb.amazonaws.com"

Resources:
    + 2 created

Duration: 22s
```

## Deploying Existing Kubernetes YAML Config to Your EKS Cluster

Specifying your Kubernetes object configurations in Pulumi lets you take advantage of programming language features,
like variables, loops, conditionals, functions, and classes. It is possible, however, to deploy existing Kubernetes
YAML. The two approaches can be mixed, which is useful when converting an existing project.

The [`ConfigFile` class](/registry/packages/kubernetes/api-docs/yaml/configfile) can be
used to deploy a single YAML file, whereas the [`ConfigGroup` class](
/registry/packages/kubernetes/api-docs/yaml/configgroup) can deploy
a collection of files, either from a set of files or in-memory representations.

For example, imagine we have a directory, `yaml/`, containing the full YAML for the [Kubernetes Guestbook application](
https://kubernetes.io/docs/tutorials/stateless-application/guestbook/), perhaps across multiple files. We can deploy
it using Pulumi into our EKS cluster with the following code and by running `pulumi up`:

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}
{{% choosable language typescript %}}

```typescript
import * as eks from "@pulumi/eks";
import * as k8s from "@pulumi/kubernetes";

// Create an EKS cluster.
const cluster = new eks.Cluster("my-cluster");

// Create resources from standard Kubernetes guestbook YAML example.
const guestbook = new k8s.yaml.ConfigGroup("guestbook",
    { files: "yaml/*.yaml" },
    { provider: cluster.provider },
);

// Export the (cluster-private) IP address of the Guestbook frontend.
export const frontendIp = guestbook.getResource("v1/Service", "frontend", "").spec.clusterIP;
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
import pulumi_eks as eks
import pulumi_kubernetes as k8s

# Create an EKS cluster.
cluster = eks.Cluster('my-cluster')

# Create resources from standard Kubernetes guestbook YAML example.
guestbook = k8s.yaml.ConfigGroup('guestbook',
    files = ['yaml/*.yaml'],
    opts = pulumi.ResourceOptions(provider = cluster.provider)
)

# Export the (cluster-private) IP address of the Guestbook frontend.
pulumi.export('frontendIp',
    guestbook.get_resource('v1/Service', 'frontend', '').spec.cluster_ip)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
	"encoding/json"
	"fmt"

	"github.com/pulumi/pulumi-eks/sdk/go/eks"
	k8s "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes"
	corev1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/core/v1"
	k8syaml "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/yaml"
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
		guestbook, err := k8syaml.NewConfigGroup(ctx, "guestbook", &k8syaml.ConfigGroupArgs{
			Files: []string{"yaml/*.yaml"},
		}, pulumi.Provider(prov))

		// Export the (cluster-private) IP address of the Guestbook frontend.
		if frontend := guestbook.GetResource("v1/Service", "frontend", ""); frontend != nil {
			ctx.Export("frontendIp", frontend.(*corev1.Service).Spec.ClusterIP())
		}
		return nil
	})
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using K8s = Pulumi.Kubernetes;
using K8sCore = Pulumi.Kubernetes.Core.V1;
using K8sYaml = Pulumi.Kubernetes.Yaml;
using Newtonsoft.Json;
using Pulumi;
using Pulumi.Eks;

class MyStack : Stack
{
    public MyStack()
    {
        // Create an EKS cluster.
        var cluster = new Cluster("my-cluster");

		// Create a Kubernetes provider using the new cluster's Kubeconfig.
        var eksProvider = new K8s.Provider("eksProvider", new K8s.ProviderArgs {
            KubeConfig = cluster.Kubeconfig.Apply(JsonConvert.SerializeObject)
        });

        // Create resources from standard Kubernetes guestbook YAML.
        var guestbook = new K8sYaml.ConfigGroup("guestbook",
            new K8sYaml.ConfigGroupArgs {
                Files = new[] { "yaml/*.yaml" },
            },
            new ComponentResourceOptions { Provider = eksProvider }
        );

		// Export the (cluster-private) IP address of the Guestbook frontend.
        this.FrontendIp = guestbook.GetResource<K8sCore.Service>(
            "frontend").Apply((svc) => svc.Spec.Apply((spec) => spec.ClusterIP));
    }

    [Output]
    public Output<string> FrontendIp { get; set; }
}
```

{{% /choosable %}}
{{% choosable language java %}}
{{% notes type="info" %}}
This functionality is currently not available in Java.
{{% /notes %}}
{{% /choosable %}}
{{% choosable language yaml %}}
{{% notes type="info" %}}
This functionality is currently not available in YAML.
{{% /notes %}}
{{% /choosable %}}

The `ConfigFile` and `ConfigGroup` classes both support a [`transformations` property](
/registry/packages/kubernetes#transformations_nodejs) which can be used to ['monkey patch'](
https://en.wikipedia.org/wiki/Monkey_patch) Kubernetes configuration on the fly. This can be used to rewrite
configuration to include additional services (like Envoy sidecars), inject tags, and so on.

For example, a transformation like the following can make all services private to a cluster, by
changing `LoadBalancer` specs into `ClusterIPs`, in addition to placing objects into a desired namespace:

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language typescript %}}

```typescript
const guestbook = new k8s.yaml.ConfigGroup("guestbook",
    {
        files: "yaml/*.yaml",
        transformations: [
            (obj: any) => {
                // Make every service private to the cluster.
                if (obj.kind == "Service" && obj.apiVersion == "v1") {
                    if (obj.spec && obj.spec.type && obj.spec.type == "LoadBalancer") {
                        obj.spec.type = "ClusterIP";
                    }
                }
            },
            // Put every resource in the created namespace.
            (obj: any) => {
                if (obj.metadata !== undefined) {
                    obj.metadata.namespace = namespaceName
                } else {
                    obj.metadata = {namespace: namespaceName}
                }
            }
        ],
    },
);
```

{{% /choosable %}}
{{% choosable language python %}}

```python
def xform_service_private(obj):
    """Make every service private to the cluster."""
    if (isinstance(obj, k8s.core.v1.Service) and
            obj.kind == 'Service' and obj.api_version == 'v1' and
            obj.spec and obj.spec.type and obj.spec.type == 'LoadBalancer'):
        obj.spec.type = 'ClusterIP'

def xform_resource_ns(obj):
    """Put every resource in the created namespace."""
    if (hasattr(obj, 'metadata')):
        if (obj.metadata is not None):
            obj.metadata.namespace = namespaceName
        else:
            obj.metadata = k8s.meta.v1.ObjectMetaArgs(namespace = namespaceName)

guestbook = k8s.yaml.ConfigGroup('guestbook',
    files = ['yaml/*.yaml'],
    opts = pulumi.ResourceOptions(
        provider = cluster.provider,
        transformations = [
            xform_service_private,
            xform_resource_ns,
        ]
    )
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
guestbook, err := k8syaml.NewConfigGroup(ctx, "guestbook", &k8syaml.ConfigGroupArgs{
    Files: []string{"yaml/*.yaml"},
    Transformations: []k8syaml.Transformation{
        // Make every service private to the cluster.
        func(state map[string]interface{}, opts ...pulumi.ResourceOption) {
            if state["kind"] == "Service" && state["apiVersion"] == "v1" {
                spec := state["spec"].(map[string]interface{})
                spec["type"] = "ClusterIP"
            }
        },
        // Put every resource in the created namespace.
        func(state map[string]interface{}, opts ...pulumi.ResourceOption) {
            if state["metadata"] != nil {
                meta := state["metadata"].(map[string]interface{})
                meta["namespace"] = namespaceName
            } else {
                state["metadata"] = map[string]interface{}{
                    "namespace": namespaceName,
                }
            }
        },
    },
})
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var guestbook = new K8sYaml.ConfigGroup("guestbook",
    new K8sYaml.ConfigGroupArgs {
        Files = new[] { "yaml/*.yaml" },
        Transformations = {
            // Make every service private to the cluster.
            (state, opts) => {
                if (state["kind"] != null && state["kind"].Equals("Service") &&
                        state["apiVersion"] != null && state["apiVersion"].Equals("v1")) {
                    var spec = (ImmutableDictionary<string, object>)state["spec"];
                    return state.SetItem("spec", spec.SetItem("type", "ClustertIP"));
                }
                return state;
            },
            // Put every resource in the created namespace.
            (state, opts) => {
                if (state["metadata"] != null) {
                    var meta = (ImmutableDictionary<string, object>)state["metadata"];
                    return state.SetItem("metadata", meta.SetItem("namespace", namespaceName));
                }
                return state.SetItem("metadata", new Dictionary<string, object> {
                    { "namespace", namespaceName }
                }.ToImmutableDictionary());
            }
        }
    },
    new ComponentResourceOptions { Provider = eksProvider }
);
```

{{% /choosable %}}
{{% choosable language java %}}
{{% notes type="info" %}}
This functionality is currently not available in Java.
{{% /notes %}}
{{% /choosable %}}
{{% choosable language yaml %}}
{{% notes type="info" %}}
This functionality is currently not available in YAML.
{{% /notes %}}
{{% /choosable %}}

Of course, it is easy to create invalid transformations that break your applications, by changing settings the
application or configuration did not expect, so this capability must be used with care.

## Deploying Existing Helm Charts to Your EKS Cluster

Pulumi can deploy [Helm charts](https://helm.sh/) through a variety of means. This includes deploying a chart
by name from any Helm repository (over the Internet or on-premises), or from a tarball directly.

> For these examples to work, you will need to [install Helm](https://helm.sh/docs/using_helm/#installing-helm)
> and, once installed, initialize it with `helm init --client-only`.

This program installs the Wordpress chart into our EKS cluster, using the [Release resource type](/registry/packages/kubernetes/api-docs/helm/v3/release/):

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as eks from "@pulumi/eks";
import * as kubernetes from "@pulumi/kubernetes";

const cluster = new eks.Cluster("cluster", {});
const eksProvider = new kubernetes.Provider("eks-provider", {kubeconfig: cluster.kubeconfigJson});
const wordpress = new kubernetes.helm.v3.Release("wordpress", {
    repositoryOpts: {
        repo: "https://charts.bitnami.com/bitnami",
    },
    chart: "wordpress",
    values: {
        wordpressBlogName: "My Cool Kubernetes Blog!",
    },
}, {
    provider: eksProvider,
});
export const kubeconfig = cluster.kubeconfig;
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
import pulumi_eks as eks
import pulumi_kubernetes as kubernetes

cluster = eks.Cluster("cluster")
eks_provider = kubernetes.Provider("eks-provider", kubeconfig=cluster.kubeconfig_json)
wordpress = kubernetes.helm.v3.Release("wordpress",
    repository_opts=kubernetes.helm.v3.RepositoryOptsArgs(
        repo="https://charts.bitnami.com/bitnami",
    ),
    chart="wordpress",
    values={
        "wordpressBlogName": "My Cool Kubernetes Blog!",
    },
    opts=pulumi.ResourceOptions(provider=eks_provider))
pulumi.export("kubeconfig", cluster.kubeconfig)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-eks/sdk/go/eks"
	"github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes"
	helmv3 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/helm/v3"
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
			Values: pulumi.AnyMap{
				"wordpressBlogName": pulumi.Any("My Cool Kubernetes Blog!"),
			},
		}, pulumi.Provider(eksProvider))
		if err != nil {
			return err
		}
		ctx.Export("kubeconfig", cluster.Kubeconfig)
		return nil
	})
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using Pulumi;
using Eks = Pulumi.Eks;
using Kubernetes = Pulumi.Kubernetes;

return await Deployment.RunAsync(() =>
{
    var cluster = new Eks.Cluster("cluster");

    var eksProvider = new Kubernetes.Provider("eks-provider", new()
    {
        KubeConfig = cluster.KubeconfigJson,
    });

    var wordpress = new Kubernetes.Helm.V3.Release("wordpress", new()
    {
        RepositoryOpts = new Kubernetes.Types.Inputs.Helm.V3.RepositoryOptsArgs
        {
            Repo = "https://charts.bitnami.com/bitnami",
        },
        Chart = "wordpress",
        Values =
        {
            { "wordpressBlogName", "My Cool Kubernetes Blog!" },
        },
    }, new CustomResourceOptions
    {
        Provider = eksProvider,
    });

    return new Dictionary<string, object?>
    {
        ["kubeconfig"] = cluster.Kubeconfig,
    };
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.pulumi.eks.Cluster;
import com.pulumi.kubernetes.Provider;
import com.pulumi.kubernetes.ProviderArgs;
import com.pulumi.kubernetes.helm.sh_v3.Release;
import com.pulumi.kubernetes.helm.sh_v3.ReleaseArgs;
import com.pulumi.kubernetes.helm.sh_v3.inputs.RepositoryOptsArgs;
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
        var cluster = new Cluster("cluster");

        var eksProvider = new Provider("eksProvider", ProviderArgs.builder()
            .kubeconfig(cluster.kubeconfigJson())
            .build());

        var wordpress = new Release("wordpress", ReleaseArgs.builder()
            .repositoryOpts(RepositoryOptsArgs.builder()
                .repo("https://charts.bitnami.com/bitnami")
                .build())
            .chart("wordpress")
            .values(Map.of("wordpressBlogName", "My Cool Kubernetes Blog!"))
            .build(), CustomResourceOptions.builder()
                .provider(eksProvider)
                .build());

        ctx.export("kubeconfig", cluster.kubeconfig());
    }
}
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  eks-provider:
    type: pulumi:providers:kubernetes
    properties:
      kubeconfig: ${cluster.kubeconfigJson}
  cluster:
    type: eks:Cluster
  wordpress:
    type: kubernetes:helm.sh/v3:Release
    properties:
      repositoryOpts:
        repo: https://charts.bitnami.com/bitnami
      chart: wordpress
      values:
        wordpressBlogName: My Cool Kubernetes Blog!
    options:
      provider: ${eks-provider}
outputs:
  kubeconfig: ${cluster.kubeconfig}
```

{{% /choosable %}}

The `values` array provides the configurable parameters for the chart. If we leave off the `version`, the latest
available chart will be fetched from the repository (including on subsequent updates, which may trigger an upgrade).

The `getResourceProperty` function on a chart can be used to get an internal resource provisioned by the chart.
Sometimes this is needed to discover attributes such as a provisioned load balancer's address. Be careful when
depending on this, however, as it is an implementation detail of the chart and will change as the chart evolves.

> Note that Pulumi support for Helm does not use Tiller. There are known problems, particularly around security,
> with Tiller, and so the Helm project is discouraging its use and
> [deprecating it as part of Helm](https://helm.sh/docs/faq/#removal-of-tiller). As a result of this, certain
> charts that depend on Tiller being present will not work with Pulumi. This is by design, affects only a
> small number of charts, and given Helm's direction, this should be considered a bug in the chart itself.

Alternatively, we can use a tarball fetched from a web URL:

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}
{{% choosable language typescript %}}

```typescript
const helm = new kubernetes.helm.v3.Release("helm", {
    chart: "https://charts.bitnami.com/bitnami/wordpress-15.2.17.tgz"
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
helm = kubernetes.helm.v3.Release("helm", chart="https://charts.bitnami.com/bitnami/wordpress-15.2.17.tgz")
```

{{% /choosable %}}
{{% choosable language go %}}

```go
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
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
return await Deployment.RunAsync(() =>
{
    var helm = new Kubernetes.Helm.V3.Release("helm", new()
    {
        Chart = "https://charts.bitnami.com/bitnami/wordpress-15.2.17.tgz",
    });

});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        var helm = new Release("helm", ReleaseArgs.builder()
            .chart("https://charts.bitnami.com/bitnami/wordpress-15.2.17.tgz")
            .build());

    }
}
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  helm:
    type: kubernetes:helm.sh/v3:Release
    properties:
      chart: https://charts.bitnami.com/bitnami/wordpress-15.2.17.tgz

```

{{% /choosable %}}

## Using an ECR Container Image from an EKS Kubernetes Deployment

[Pulumi Crosswalk for AWS ECR](/docs/guides/crosswalk/aws/ecr/) enables you to build, publish, and consume private Docker
images easily using Amazon's Elastic Container Registry (ECR). In the following example, creating an `Image` resource will
build an image from the "./app" directory (relative to the project and containing Dockerfile), and publish it to the
provisioned ECR repository.

> *Note:* for more complete examples of building and publishing to _any_ private container registry, including AWS, Azure,
> Google Cloud, and the Docker Hub, please refer to the article [Build and publish container images to any cloud with
> Infrastructure as Code](/blog/build-publish-containers-iac/).

For example, let's say we have an `app/` directory containing a fully Dockerized application (including a
`Dockerfile`), and would like to deploy that as a Deployment and Service running in our EKS cluster. This program
accomplishes this with a single `pulumi up` command:

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as awsx from "@pulumi/awsx";
import * as eks from "@pulumi/eks";
import * as kubernetes from "@pulumi/kubernetes";

const appName = "my-app";
const repository = new awsx.ecr.Repository("repository", {});
const image = new awsx.ecr.Image("image", {
    repositoryUrl: repository.url,
    path: "./app",
});
const cluster = new eks.Cluster("cluster", {});
const clusterProvider = new kubernetes.Provider("clusterProvider", {
    kubeconfig: cluster.kubeconfig,
    enableServerSideApply: true,
});
const deployment = new kubernetes.apps.v1.Deployment("deployment", {
    metadata: {
        labels: {
            appClass: appName,
        },
    },
    spec: {
        replicas: 2,
        selector: {
            matchLabels: {
                appClass: appName,
            },
        },
        template: {
            metadata: {
                labels: {
                    appClass: appName,
                },
            },
            spec: {
                containers: [{
                    name: appName,
                    image: image.imageUri,
                    ports: [{
                        name: "http",
                        containerPort: 80,
                    }],
                }],
            },
        },
    },
}, {
    provider: clusterProvider,
});
const service = new kubernetes.core.v1.Service("service", {
    metadata: {
        labels: {
            appClass: appName,
        },
    },
    spec: {
        type: "LoadBalancer",
        selector: {
            appClass: appName,
        },
        ports: [{
            port: 80,
            targetPort: "http",
        }],
    },
}, {
    provider: clusterProvider,
});
export const url = service.status.apply(status => status?.loadBalancer?.ingress?.[0]?.hostname);
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
import pulumi_awsx as awsx
import pulumi_eks as eks
import pulumi_kubernetes as kubernetes

app_name = "my-app"
repository = awsx.ecr.Repository("repository")
image = awsx.ecr.Image("image",
    repository_url=repository.url,
    path="./app")
cluster = eks.Cluster("cluster")
cluster_provider = kubernetes.Provider("clusterProvider",
    kubeconfig=cluster.kubeconfig,
    enable_server_side_apply=True)
deployment = kubernetes.apps.v1.Deployment("deployment",
    metadata=kubernetes.meta.v1.ObjectMetaArgs(
        labels={
            "appClass": app_name,
        },
    ),
    spec=kubernetes.apps.v1.DeploymentSpecArgs(
        replicas=2,
        selector=kubernetes.meta.v1.LabelSelectorArgs(
            match_labels={
                "appClass": app_name,
            },
        ),
        template=kubernetes.core.v1.PodTemplateSpecArgs(
            metadata=kubernetes.meta.v1.ObjectMetaArgs(
                labels={
                    "appClass": app_name,
                },
            ),
            spec=kubernetes.core.v1.PodSpecArgs(
                containers=[kubernetes.core.v1.ContainerArgs(
                    name=app_name,
                    image=image.image_uri,
                    ports=[kubernetes.core.v1.ContainerPortArgs(
                        name="http",
                        container_port=80,
                    )],
                )],
            ),
        ),
    ),
    opts=pulumi.ResourceOptions(provider=cluster_provider))
service = kubernetes.core.v1.Service("service",
    metadata=kubernetes.meta.v1.ObjectMetaArgs(
        labels={
            "appClass": app_name,
        },
    ),
    spec=kubernetes.core.v1.ServiceSpecArgs(
        type="LoadBalancer",
        selector={
            "appClass": app_name,
        },
        ports=[kubernetes.core.v1.ServicePortArgs(
            port=80,
            target_port="http",
        )],
    ),
    opts=pulumi.ResourceOptions(provider=cluster_provider))
pulumi.export("url", service.status.load_balancer.ingress[0].hostname)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-awsx/sdk/go/awsx/ecr"
	"github.com/pulumi/pulumi-eks/sdk/go/eks"
	"github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes"
	appsv1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/apps/v1"
	corev1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/core/v1"
	metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/meta/v1"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		appName := "my-app"
		repository, err := ecr.NewRepository(ctx, "repository", nil)
		if err != nil {
			return err
		}
		image, err := ecr.NewImage(ctx, "image", &ecr.ImageArgs{
			RepositoryUrl: repository.Url,
			Path:          pulumi.String("./app"),
		})
		if err != nil {
			return err
		}
		cluster, err := eks.NewCluster(ctx, "cluster", nil)
		if err != nil {
			return err
		}
		clusterProvider, err := kubernetes.NewProvider(ctx, "clusterProvider", &kubernetes.ProviderArgs{
			Kubeconfig:            cluster.Kubeconfig.AsStringPtrOutput(),
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
		ctx.Export("url", service.Status.ApplyT(func(status corev1.ServiceStatus) (*string, error) {
			return status.LoadBalancer.Ingress[0].Hostname, nil
		}).(pulumi.StringPtrOutput))
		return nil
	})
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using Pulumi;
using Awsx = Pulumi.Awsx;
using Eks = Pulumi.Eks;
using Kubernetes = Pulumi.Kubernetes;

return await Deployment.RunAsync(() =>
{
    var appName = "my-app";

    var repository = new Awsx.Ecr.Repository("repository");

    var image = new Awsx.Ecr.Image("image", new()
    {
        RepositoryUrl = repository.Url,
        Path = "./app",
    });

    var cluster = new Eks.Cluster("cluster");

    var clusterProvider = new Kubernetes.Provider("clusterProvider", new()
    {
        KubeConfig = cluster.Kubeconfig,
        EnableServerSideApply = true,
    });

    var deployment = new Kubernetes.Apps.V1.Deployment("deployment", new()
    {
        Metadata = new Kubernetes.Types.Inputs.Meta.V1.ObjectMetaArgs
        {
            Labels =
            {
                { "appClass", appName },
            },
        },
        Spec = new Kubernetes.Types.Inputs.Apps.V1.DeploymentSpecArgs
        {
            Replicas = 2,
            Selector = new Kubernetes.Types.Inputs.Meta.V1.LabelSelectorArgs
            {
                MatchLabels =
                {
                    { "appClass", appName },
                },
            },
            Template = new Kubernetes.Types.Inputs.Core.V1.PodTemplateSpecArgs
            {
                Metadata = new Kubernetes.Types.Inputs.Meta.V1.ObjectMetaArgs
                {
                    Labels =
                    {
                        { "appClass", appName },
                    },
                },
                Spec = new Kubernetes.Types.Inputs.Core.V1.PodSpecArgs
                {
                    Containers = new[]
                    {
                        new Kubernetes.Types.Inputs.Core.V1.ContainerArgs
                        {
                            Name = appName,
                            Image = image.ImageUri,
                            Ports = new[]
                            {
                                new Kubernetes.Types.Inputs.Core.V1.ContainerPortArgs
                                {
                                    Name = "http",
                                    ContainerPortValue = 80,
                                },
                            },
                        },
                    },
                },
            },
        },
    }, new CustomResourceOptions
    {
        Provider = clusterProvider,
    });

    var service = new Kubernetes.Core.V1.Service("service", new()
    {
        Metadata = new Kubernetes.Types.Inputs.Meta.V1.ObjectMetaArgs
        {
            Labels =
            {
                { "appClass", appName },
            },
        },
        Spec = new Kubernetes.Types.Inputs.Core.V1.ServiceSpecArgs
        {
            Type = "LoadBalancer",
            Selector =
            {
                { "appClass", appName },
            },
            Ports = new[]
            {
                new Kubernetes.Types.Inputs.Core.V1.ServicePortArgs
                {
                    Port = 80,
                    TargetPort = "http",
                },
            },
        },
    }, new CustomResourceOptions
    {
        Provider = clusterProvider,
    });

    return new Dictionary<string, object?>
    {
        ["url"] = service.Status.Apply(status => status?.LoadBalancer?.Ingress[0]?.Hostname),
    };
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.pulumi.awsx.ecr.Repository;
import com.pulumi.awsx.ecr.Image;
import com.pulumi.awsx.ecr.ImageArgs;
import com.pulumi.eks.Cluster;
import com.pulumi.kubernetes.Provider;
import com.pulumi.kubernetes.ProviderArgs;
import com.pulumi.kubernetes.apps_v1.Deployment;
import com.pulumi.kubernetes.apps_v1.DeploymentArgs;
import com.pulumi.kubernetes.meta_v1.inputs.ObjectMetaArgs;
import com.pulumi.kubernetes.apps_v1.inputs.DeploymentSpecArgs;
import com.pulumi.kubernetes.meta_v1.inputs.LabelSelectorArgs;
import com.pulumi.kubernetes.core_v1.inputs.PodTemplateSpecArgs;
import com.pulumi.kubernetes.core_v1.inputs.PodSpecArgs;
import com.pulumi.kubernetes.core_v1.Service;
import com.pulumi.kubernetes.core_v1.ServiceArgs;
import com.pulumi.kubernetes.core_v1.inputs.ServiceSpecArgs;
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
        final var appName = "my-app";

        var repository = new Repository("repository");

        var image = new Image("image", ImageArgs.builder()
            .repositoryUrl(repository.url())
            .path("./app")
            .build());

        var cluster = new Cluster("cluster");

        var clusterProvider = new Provider("clusterProvider", ProviderArgs.builder()
            .kubeconfig(cluster.kubeconfig())
            .enableServerSideApply(true)
            .build());

        var deployment = new Deployment("deployment", DeploymentArgs.builder()
            .metadata(ObjectMetaArgs.builder()
                .labels(Map.of("appClass", appName))
                .build())
            .spec(DeploymentSpecArgs.builder()
                .replicas(2)
                .selector(LabelSelectorArgs.builder()
                    .matchLabels(Map.of("appClass", appName))
                    .build())
                .template(PodTemplateSpecArgs.builder()
                    .metadata(ObjectMetaArgs.builder()
                        .labels(Map.of("appClass", appName))
                        .build())
                    .spec(PodSpecArgs.builder()
                        .containers(ContainerArgs.builder()
                            .name(appName)
                            .image(image.imageUri())
                            .ports(ContainerPortArgs.builder()
                                .name("http")
                                .containerPort(80)
                                .build())
                            .build())
                        .build())
                    .build())
                .build())
            .build(), CustomResourceOptions.builder()
                .provider(clusterProvider)
                .build());

        var service = new Service("service", ServiceArgs.builder()
            .metadata(ObjectMetaArgs.builder()
                .labels(Map.of("appClass", appName))
                .build())
            .spec(ServiceSpecArgs.builder()
                .type("LoadBalancer")
                .selector(Map.of("appClass", appName))
                .ports(ServicePortArgs.builder()
                    .port(80)
                    .targetPort("http")
                    .build())
                .build())
            .build(), CustomResourceOptions.builder()
                .provider(clusterProvider)
                .build());

        ctx.export("url", service.status().applyValue(status -> status.loadBalancer().ingress()[0].hostname()));
    }
}
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
variables:
  appName: my-app
resources:
  repository:
    type: awsx:ecr:Repository
  image:
    type: awsx:ecr:Image
    properties:
      repositoryUrl: ${repository.url}
      path: "./app"
  cluster:
    type: eks:Cluster
  clusterProvider:
    type: pulumi:providers:kubernetes
    properties:
      kubeconfig: ${cluster.kubeconfig}
      enableServerSideApply: true
  deployment:
    type: kubernetes:apps/v1:Deployment
    properties:
      metadata:
        labels:
          appClass: ${appName}
      spec:
        replicas: 2
        selector:
          matchLabels:
            appClass: ${appName}
        template:
          metadata:
            labels:
              appClass: ${appName}
          spec:
            containers:
              - name: ${appName}
                image: ${image.imageUri}
                ports:
                  - name: http
                    containerPort: 80
    options:
      provider: ${clusterProvider}
  service:
    type: kubernetes:core/v1:Service
    properties:
      metadata:
        labels:
          appClass: ${appName}
      spec:
        type: LoadBalancer
        selector:
          appClass: ${appName}
        ports:
          - port: 80
            targetPort: http
    options:
      provider: ${clusterProvider}
outputs:
  url: ${service.status.loadBalancer.ingress[0].hostname}
```

{{% /choosable %}}

For more information about ECR, see [the Pulumi Crosswalk for AWS ECR documentation](/docs/guides/crosswalk/aws/ecr/).

## Additional EKS Resources

For more information about Kubernetes and EKS, see the following:

* [Pulumi Kubernetes API Documentation](/registry/packages/kubernetes/api-docs/)
* [Pulumi EKS API Documentation](/registry/packages/eks/api-docs/)
* [Amazon Elastic Kubernetes Service homepage](https://aws.amazon.com/eks/)
* [Kubernetes Documentation](https://kubernetes.io)

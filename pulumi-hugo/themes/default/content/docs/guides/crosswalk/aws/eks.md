---
title: "AWS Elastic Kubernetes Service (EKS)"
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

<a href="{{< relref "./" >}}">
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

* [ECR]({{< relref "ecr" >}}) for private container images
* [ELB]({{< relref "elb" >}}) for load balancing
* [IAM]({{< relref "iam" >}}) for security
* [VPC]({{< relref "vpc" >}}) for network isolation
* [CloudWatch]({{< relref "cloudwatch" >}}) for monitoring

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

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language javascript %}}

```javascript
const aws = require("@pulumi/eks");

// Create an EKS cluster with the default configuration.
const cluster = new eks.Cluster("my-cluster");

// Export the cluster's kubeconfig.
module.exports = {
    kubeconfig: cluster.kubeconfig,
};
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as eks from "@pulumi/eks";

// Create an EKS cluster with the default configuration.
const cluster = new eks.Cluster("my-cluster");

// Export the cluster's kubeconfig.
export const kubeconfig = cluster.kubeconfig;
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
import pulumi_eks as eks

# Create an EKS cluster with the default configuration.
cluster = eks.Cluster('my-cluster')

# Export the cluster's kubeconfig.
pulumi.export('kubeconfig', cluster.kubeconfig)
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
		cluster, err := eks.NewCluster(ctx, "my-cluster", nil)
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
using Pulumi;
using Pulumi.Eks;

class MyStack : Stack
{
    public MyStack()
    {
        // Create an EKS cluster with the default configuration.
        var cluster = new Cluster("my-cluster");

        // Export the cluster's kubeconfig.
        this.Kubeconfig = cluster.Kubeconfig;
    }

    [Output]
    public Output<object> Kubeconfig { get; set; }
}
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

From here, we have a fully functioning EKS cluster in Amazon, which we can deploy Kubernetes applications to.
Any existing tools will work here, including `kubectl`, Helm, and other CI/CD products. Pulumi offers the ability
to define Kubernetes application-level objects and configuration in code too. For instance, we can deploy a canary
to our EKS cluster in the same program if we want to test that it is working as part of `pulumi up`:

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language javascript %}}

```javascript
const eks = require("@pulumi/eks");
const k8s = require("@pulumi/kubernetes");

// Create an EKS cluster with the default configuration.
const cluster = new eks.Cluster("my-cluster");

// Deploy a small canary service (NGINX), to test that the cluster is working.
const appName = "my-app";
const appLabels = { appClass: appName };
const deployment = new k8s.apps.v1.Deployment(`${appName}-dep`, {
    metadata: { labels: appLabels },
    spec: {
        replicas: 2,
        selector: { matchLabels: appLabels },
        template: {
            metadata: { labels: appLabels },
            spec: {
                containers: [{
                    name: appName,
                    image: "nginx",
                    ports: [{ name: "http", containerPort: 80 }]
                }],
            }
        }
    },
}, { provider: cluster.provider });
const service = new k8s.core.v1.Service(`${appName}-svc`, {
    metadata: { labels: appLabels },
    spec: {
        type: "LoadBalancer",
        ports: [{ port: 80, targetPort: "http" }],
        selector: appLabels,
    },
}, { provider: cluster.provider });

module.exports = {
    // Export the URL for the load balanced service.
    url: service.status.loadBalancer.ingress[0].hostname,
    // Export the cluster's kubeconfig.
    kubeconfig: cluster.kubeconfig,
};
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as eks from "@pulumi/eks";
import * as k8s from "@pulumi/kubernetes";

// Create an EKS cluster with the default configuration.
const cluster = new eks.Cluster("my-cluster");

// Deploy a small canary service (NGINX), to test that the cluster is working.
const appName = "my-app";
const appLabels = { appClass: appName };
const deployment = new k8s.apps.v1.Deployment(`${appName}-dep`, {
    metadata: { labels: appLabels },
    spec: {
        replicas: 2,
        selector: { matchLabels: appLabels },
        template: {
            metadata: { labels: appLabels },
            spec: {
                containers: [{
                    name: appName,
                    image: "nginx",
                    ports: [{ name: "http", containerPort: 80 }]
                }],
            }
        }
    },
}, { provider: cluster.provider });
const service = new k8s.core.v1.Service(`${appName}-svc`, {
    metadata: { labels: appLabels },
    spec: {
        type: "LoadBalancer",
        ports: [{ port: 80, targetPort: "http" }],
        selector: appLabels,
    },
}, { provider: cluster.provider });

// Export the URL for the load balanced service.
export const url = service.status.loadBalancer.ingress[0].hostname;

// Export the cluster's kubeconfig.
export const kubeconfig = cluster.kubeconfig;
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
import pulumi_eks as eks
import pulumi_kubernetes as k8s

# Create an EKS cluster with the default configuration.
cluster = eks.Cluster('my-cluster');

# Deploy a small canary service (NGINX), to test that the cluster is working.
app_name = 'my-app'
app_labels = { 'app': app_name }
deployment = k8s.apps.v1.Deployment(f'{app_name}-dep',
    spec = k8s.apps.v1.DeploymentSpecArgs(
        selector = k8s.meta.v1.LabelSelectorArgs(match_labels = app_labels),
        replicas = 2,
        template = k8s.core.v1.PodTemplateSpecArgs(
            metadata = k8s.meta.v1.ObjectMetaArgs(labels = app_labels),
            spec = k8s.core.v1.PodSpecArgs(containers = [
                k8s.core.v1.ContainerArgs(name = appName, image = 'nginx')
            ]),
        ),
    ), opts = pulumi.ResourceOptions(provider = cluster.provider)
)
service = k8s.core.v1.Service(f'{app_name}-svc',
    spec = k8s.core.v1.ServiceSpecArgs(
        type = 'LoadBalancer',
        selector = app_labels,
        ports = [ k8s.core.v1.ServicePortArgs(port = 80) ],
    ), opts = pulumi.ResourceOptions(provider = cluster.provider)
)

# Export the URL for the load balanced service.
pulumi.export('url', service.status.load_balancer.ingress[0].hostname)

# Export the cluster's kubeconfig.
pulumi.export('kubeconfig', cluster.kubeconfig)
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
	appsv1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/apps/v1"
	corev1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/core/v1"
	metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/meta/v1"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Create an EKS cluster with the default configuration.
		cluster, err := eks.NewCluster(ctx, "my-cluster", nil)
		if err != nil {
			return err
		}

		// Create a Kubernetes provider using the new cluster's Kubeconfig.
		prov, err := k8s.NewProvider(ctx, "eksProvider", &k8s.ProviderArgs{
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

		// Deploy a small canary service (NGINX), to test that the cluster is working.
		appName := "my-app"
		appLabels := pulumi.StringMap{"app": pulumi.String(appName)}
		_, err = appsv1.NewDeployment(ctx,
			fmt.Sprintf("%s-dep", appName),
			&appsv1.DeploymentArgs{
				Spec: &appsv1.DeploymentSpecArgs{
					Selector: &metav1.LabelSelectorArgs{MatchLabels: appLabels},
					Replicas: pulumi.Int(2),
					Template: &corev1.PodTemplateSpecArgs{
						Metadata: &metav1.ObjectMetaArgs{Labels: appLabels},
						Spec: &corev1.PodSpecArgs{
							Containers: corev1.ContainerArray{
								&corev1.ContainerArgs{
									Name:  pulumi.String(appName),
									Image: pulumi.String("nginx"),
								},
							},
						},
					},
				},
			},
			pulumi.Provider(prov),
		)
		if err != nil {
			return nil
		}
		service, err := corev1.NewService(ctx,
			fmt.Sprintf("%s-svc", appName),
			&corev1.ServiceArgs{
				Spec: &corev1.ServiceSpecArgs{
					Type:     pulumi.String("LoadBalancer"),
					Selector: appLabels,
					Ports: corev1.ServicePortArray{
						&corev1.ServicePortArgs{
							Port: pulumi.Int(80),
						},
					},
				},
			},
			pulumi.Provider(prov),
		)
		if err != nil {
			return err
		}

		// Export the URL for the load balanced service.
		ctx.Export("url", service.Status.ApplyT(func(status interface{}) string {
			return *status.(*corev1.ServiceStatus).LoadBalancer.Ingress[0].Hostname
		}))

		// Export the cluster's kubeconfig.
		ctx.Export("kubeconfig", cluster.Kubeconfig)
		return nil
	})
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using K8s = Pulumi.Kubernetes;
using K8sApps = Pulumi.Kubernetes.Apps.V1;
using K8sAppsArgs = Pulumi.Kubernetes.Types.Inputs.Apps.V1;
using K8sCore = Pulumi.Kubernetes.Core.V1;
using K8sCoreArgs = Pulumi.Kubernetes.Types.Inputs.Core.V1;
using K8sMeta = Pulumi.Kubernetes.Meta.V1;
using K8sMetaArgs = Pulumi.Kubernetes.Types.Inputs.Meta.V1;
using Newtonsoft.Json;
using Pulumi;
using Pulumi.Eks;
using System;
using System.Collections.Generic;
using System.Collections.Immutable;

class MyStack : Stack
{
    public MyStack()
    {
        // Create an EKS cluster with the default configuration.
        var cluster = new Cluster("my-cluster");

		// Create a Kubernetes provider using the new cluster's Kubeconfig.
        var eksProvider = new K8s.Provider("eksProvider", new K8s.ProviderArgs {
            KubeConfig = cluster.Kubeconfig.Apply(JsonConvert.SerializeObject)
        });

		// Deploy a small canary service (NGINX), to test that the cluster is working.
        var appName = "my-app";
        var appLabels = new Dictionary<string, string>{ { "app", appName } }.ToImmutableDictionary();
        var deployment = new K8sApps.Deployment(
            String.Format("{0}-dep", appName),
            new K8sAppsArgs.DeploymentArgs {
                Spec = new K8sAppsArgs.DeploymentSpecArgs {
                    Selector = new K8sMetaArgs.LabelSelectorArgs { MatchLabels = appLabels },
                    Replicas = 2,
                    Template = new K8sCoreArgs.PodTemplateSpecArgs {
                        Metadata = new K8sMetaArgs.ObjectMetaArgs { Labels = appLabels },
                        Spec = new K8sCoreArgs.PodSpecArgs {
                            Containers = {
                                new K8sCoreArgs.ContainerArgs {
                                    Name = appName,
                                    Image = "nginx",
                                },
                            },
                        },
                    },
                },
            },
            new CustomResourceOptions { Provider = eksProvider }
        );
        var service = new K8sCore.Service(
            String.Format("{0}-svc", appName),
            new K8sCoreArgs.ServiceArgs {
                Spec = new K8sCoreArgs.ServiceSpecArgs {
                    Type = "LoadBalancer",
                    Selector = appLabels,
                    Ports = {
                        new K8sCoreArgs.ServicePortArgs { Port = 80 },
                    },
                },
            },
            new CustomResourceOptions { Provider = eksProvider }
        );

		// Export the URL for the load balanced service.
        this.Url = service.Status.Apply((status) =>
            status.LoadBalancer.Ingress[0].Hostname);

        // Export the cluster's kubeconfig.
        this.Kubeconfig = cluster.Kubeconfig;
    }

    [Output]
    public Output<string> Url { get; set; }
    [Output]
    public Output<object> Kubeconfig { get; set; }
}
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

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language javascript %}}

```javascript
const eks = require("@pulumi/eks");

// Create an EKS cluster with the default configuration.
const cluster = new eks.Cluster("my-cluster", {
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
module.exports = {
    kubeconfig: cluster.kubeconfig,
};
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as eks from "@pulumi/eks";

// Create an EKS cluster with the default configuration.
const cluster = new eks.Cluster("my-cluster", {
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

# Create an EKS cluster with the default configuration.
cluster = eks.Cluster('my-cluster',
    eks.ClusterArgs(
        desired_capacity = 5,
        min_size = 3,
        max_size = 5,
        enabled_cluster_log_types = [
            'api',
            'audit',
            'authenticator'
        ]
    )
)

# Export the cluster's kubeconfig.
pulumi.export('kubeconfig', cluster.kubeconfig)
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
		cluster, err := eks.NewCluster(ctx, "my-cluster", &eks.ClusterArgs{
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
using Pulumi;
using Pulumi.Eks;

class MyStack : Stack
{
    public MyStack()
    {
        // Create an EKS cluster with the default configuration.
        var cluster = new Cluster("my-cluster", new ClusterArgs {
            DesiredCapacity = 5,
            MinSize = 3,
            MaxSize = 5,
            EnabledClusterLogTypes = {
                "api",
                "audit",
                "authenticator",
            },
        });

        // Export the cluster's kubeconfig.
        this.Kubeconfig = cluster.Kubeconfig;
    }

    [Output]
    public Output<object> Kubeconfig { get; set; }
}
```

{{% /choosable %}}

For a full list of options that you may set on your cluster, see the [API documentation](
{{< relref "/docs/reference/pkg/nodejs/pulumi/eks#ClusterOptions" >}}). Many common cases are described below.

## Configuring Your EKS Cluster's Networking

By default, your EKS cluster is put into your region's default VPC. This is a reasonable default, however this is
configurable if you want specific network isolation or to place your cluster work nodes on private subnets. This works
in conjunction with [Pulumi Crosswalk for AWS VPC]({{< relref "vpc" >}}) which makes configuring VPCs easier.

This example creates a new VPC with private subnets only and creates our EKS cluster inside of it:

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language javascript %}}

```javascript
const awsx = require("@pulumi/awsx");
const eks = require("@pulumi/eks");

// Create a VPC for our cluster.
const vpc = new awsx.ec2.Vpc("my-vpc", {});

// Create an EKS cluster inside of the VPC.
const cluster = new eks.Cluster("my-cluster", {
    vpcId: vpc.id,
    publicSubnetIds: vpc.publicSubnetIds,
    privateSubnetIds: vpc.privateSubnetIds,
    nodeAssociatePublicIpAddress: false,
});

// Export the cluster's kubeconfig.
module.exports = {
    cluster.kubeconfig,
};
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as awsx from "@pulumi/awsx";
import * as eks from "@pulumi/eks";

// Create a VPC for our cluster.
const vpc = new awsx.ec2.Vpc("my-vpc", {});

// Create an EKS cluster inside of the VPC.
const cluster = new eks.Cluster("my-cluster", {
    vpcId: vpc.id,
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
import pulumi_eks as eks

# Create or lookup a VPC for our cluster.
vpc = ...

# Create an EKS cluster inside of our VPC.
cluster = eks.Cluster('my-cluster',
    eks.ClusterArgs(
        vpc_id = vpc.id,
        public_subnet_ids = vpc.public_subnet_ids,
        private_subnet_ids = vpc.private_subnet_ids,
        node_associate_public_ip_address = False,
    )
)

# Export the cluster's kubeconfig.
pulumi.export('kubeconfig', cluster.kubeconfig)
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
		// Create or lookup a VPC for our cluster.
		vpc := ...

		// Create an EKS cluster with the default configuration.
		cluster, err := eks.NewCluster(ctx, "my-cluster", &eks.ClusterArgs{
			VpcId:                        vpc.ID,
			PublicSubnetIds:              vpc.PublicSubnetIds,
			PrivateSubnetIds:             vpc.PrivateSubnetIds,
			NodeAssociatePublicIpAddress: pulumi.Bool(false),
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
using Pulumi;
using Pulumi.Eks;

class MyStack : Stack
{
    public MyStack()
    {
        // Create or lookup a VPC for our cluster.
        var vpc = ...;

        // Create an EKS cluster with the default configuration.
        var cluster = new Cluster("my-cluster", new ClusterArgs {
            VpcId = vpc.Id,
            PublicSubnetIds = vpc.PublicSubnetIds,
            PrivateSubnetIds = vpc.PrivateSubnetIds,
            NodeAssociatePublicIpAddress = false,
        });

        // Export the cluster's kubeconfig.
        this.Kubeconfig = cluster.Kubeconfig;
    }

    [Output]
    public Output<object> Kubeconfig { get; set; }
}
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

If you would like to disable the creation of a default node group, and instead rely on creating your own, simply pass
[`skipDefaultNodeGroup`]({{< relref "/docs/reference/pkg/nodejs/pulumi/eks#ClusterOptions-skipDefaultNodeGroup" >}})
as `true` to the `eks.Cluster` constructor. Additional node groups may then be created by calling
[the `createNodeGroup` function]({{< relref "/docs/reference/pkg/nodejs/pulumi/eks#Cluster-createNodeGroup" >}}) on
your EKS cluster, or by [creating an `eks.NodeGroup`]({{< relref "/docs/reference/pkg/nodejs/pulumi/eks#NodeGroup" >}})
explicitly. In both cases, you are likely to want to configure IAM roles for your worker nodes explicitly, which can be
supplied to your EKS cluster using the
[`instanceRole`]({{< relref "/docs/reference/pkg/nodejs/pulumi/eks#ClusterOptions-instanceRole" >}}) or
[`instanceRoles`]({{< relref "/docs/reference/pkg/nodejs/pulumi/eks#ClusterOptions-instanceRoles" >}}) properties.

For instance, let's say we want to have two node groups: one for our fixed, known workloads, and another that is
burstable and might use more expensive compute, but which can be scaled down when possible (possibly to zero).
We would skip the default node group, and create our own node groups:

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language javascript %}}

```javascript
const aws = require("@pulumi/aws");
const eks = require("@pulumi/eks");

/**
 * Per NodeGroup IAM: each NodeGroup will bring its own, specific instance role and profile.
 */

const managedPolicyArns: string[] = [
    "arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy",
    "arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy",
    "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly",
];

// Creates a role and attaches the EKS worker node IAM managed policies. Used a few times below,
// to create multiple roles, so we use a function to avoid repeating ourselves.
export function createRole(name: string): aws.iam.Role {
    const role = new aws.iam.Role(name, {
        assumeRolePolicy: aws.iam.assumeRolePolicyForPrincipal({
            Service: "ec2.amazonaws.com",
        }),
    });

    let counter = 0;
    for (const policy of managedPolicyArns) {
        // Create RolePolicyAttachment without returning it.
        const rpa = new aws.iam.RolePolicyAttachment(`${name}-policy-${counter++}`,
            { policyArn: policy, role: role },
        );
    }

    return role;
}

// Now create the roles and instance profiles for the two worker groups.
const role1 = createRole("my-worker-role1");
const role2 = createRole("my-worker-role2");
const instanceProfile1 = new aws.iam.InstanceProfile("my-instance-profile1", {role: role1});
const instanceProfile2 = new aws.iam.InstanceProfile("my-instance-profile2", {role: role2});

// Create an EKS cluster with many IAM roles to register with the cluster auth.
const cluster = new eks.Cluster("my-cluster", {
    skipDefaultNodeGroup: true,
    instanceRoles: [ role1, role2 ],
});

// Now create multiple node groups, each using a different instance profile for each role.

// First, create a node group for fixed compute.
const fixedNodeGroup = cluster.createNodeGroup("my-cluster-ng1", {
    instanceType: "t2.medium",
    desiredCapacity: 2,
    minSize: 1,
    maxSize: 3,
    labels: {"ondemand": "true"},
    instanceProfile: instanceProfile1,
});

// Now create a preemptible node group, using spot pricing, for our variable, ephemeral workloads.
const spotNodeGroup = new eks.NodeGroup("my-cluster-ng2", {
    cluster: cluster,
    instanceType: "t2.medium",
    desiredCapacity: 1,
    spotPrice: "1",
    minSize: 1,
    maxSize: 2,
    labels: {"preemptible": "true"},
    taints: {
        "special": {
            value: "true",
            effect: "NoSchedule",
        },
    },
    instanceProfile: instanceProfile2,
}, {
    providers: { kubernetes: cluster.provider},
});

// Export the cluster's kubeconfig.
module.exports = {
    kubeconfig: cluster.kubeconfig,
};
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as aws from "@pulumi/aws";
import * as eks from "@pulumi/eks";

/**
 * Per NodeGroup IAM: each NodeGroup will bring its own, specific instance role and profile.
 */

const managedPolicyArns: string[] = [
    "arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy",
    "arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy",
    "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly",
];

// Creates a role and attaches the EKS worker node IAM managed policies. Used a few times below,
// to create multiple roles, so we use a function to avoid repeating ourselves.
export function createRole(name: string): aws.iam.Role {
    const role = new aws.iam.Role(name, {
        assumeRolePolicy: aws.iam.assumeRolePolicyForPrincipal({
            Service: "ec2.amazonaws.com",
        }),
    });

    let counter = 0;
    for (const policy of managedPolicyArns) {
        // Create RolePolicyAttachment without returning it.
        const rpa = new aws.iam.RolePolicyAttachment(`${name}-policy-${counter++}`,
            { policyArn: policy, role: role },
        );
    }

    return role;
}

// Now create the roles and instance profiles for the two worker groups.
const role1 = createRole("my-worker-role1");
const role2 = createRole("my-worker-role2");
const instanceProfile1 = new aws.iam.InstanceProfile("my-instance-profile1", {role: role1});
const instanceProfile2 = new aws.iam.InstanceProfile("my-instance-profile2", {role: role2});

// Create an EKS cluster with many IAM roles to register with the cluster auth.
const cluster = new eks.Cluster("my-cluster", {
    skipDefaultNodeGroup: true,
    instanceRoles: [ role1, role2 ],
});

// Now create multiple node groups, each using a different instance profile for each role.

// First, create a node group for fixed compute.
const fixedNodeGroup = cluster.createNodeGroup("my-cluster-ng1", {
    instanceType: "t2.medium",
    desiredCapacity: 2,
    minSize: 1,
    maxSize: 3,
    labels: {"ondemand": "true"},
    instanceProfile: instanceProfile1,
});

// Now create a preemptible node group, using spot pricing, for our variable, ephemeral workloads.
const spotNodeGroup = new eks.NodeGroup("my-cluster-ng2", {
    cluster: cluster,
    instanceType: "t2.medium",
    desiredCapacity: 1,
    spotPrice: "1",
    minSize: 1,
    maxSize: 2,
    labels: {"preemptible": "true"},
    taints: {
        "special": {
            value: "true",
            effect: "NoSchedule",
        },
    },
    instanceProfile: instanceProfile2,
}, {
    providers: { kubernetes: cluster.provider},
});

// Export the cluster's kubeconfig.
export const kubeconfig = cluster.kubeconfig;
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
import pulumi_aws as aws
import pulumi_eks as eks

# Per NodeGroup IAM: each NodeGroup will bring its own, specific instance role and profile.
managed_policy_arns = [
    'arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy',
    'arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy',
    'arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly',
]

# Creates a role and attaches the EKS worker node IAM managed policies. Used a few times below,
# to create multiple roles, so we use a function to avoid repeating ourselves.
def create_role(name):
    role = aws.iam.Role(name, aws.iam.RoleArgs(
        assume_role_policy = """{
    "Version": "2012-10-17",
    "Statement": [{
        "Sid": "AllowAssumeRole",
        "Effect": "Allow",
        "Principal": "ec2.amazonaws.com",
        "Action": "sts:AssumeRole"
    }]
}""",
    ))
    counter = 0
    for policy in managed_policy_arns:
        rpa = aws.iam.RolePolicyAttachment(f'{name}-policy-{counter}',
            aws.iam.RolePolicyAttachmentArgs(
                policy_arn = policy,
                role = role,
            )
        )
        counter = counter + 1
    return role

# Now create the roles and instance profiles for the two worker groups.
role1 = create_role('my-worker-role1')
role2 = create_role('my-worker-role2')
instance_profile_1 = aws.iam.InstanceProfile('my-instance-profile1',
    aws.iam.InstanceProfileArgs(role = role1))
instance_profile_2 = aws.iam.InstanceProfile('my-instance-profile2',
    aws.iam.InstanceProfileArgs(role = role2))

# Create an EKS cluster with many IAM roles to register with the cluster auth.
cluster = eks.Cluster('my-cluster',
    eks.ClusterArgs(
        skip_default_node_group = True,
        instance_roles = [ role1, role2 ],
    )
)

# Now create multiple node groups, each using a different instance profile for each role.

# First, create a node group for fixed compute.
fixed_node_group = eks.NodeGroup('my-cluster-ng1',
    cluster = cluster.core,
    instance_type = 't2.medium',
    desired_capacity = 2,
    min_size = 1,
    max_size = 3,
    labels = {'ondemand': 'true'},
    instance_profile = instance_profile_1,
    opts = pulumi.ResourceOptions(
        parent = cluster,
        providers = {
            'kubernetes': cluster.provider,
        }
    )
)

# Now create a preemptible node group, using spot pricing, for our variable, ephemeral workloads.
spot_node_group = eks.NodeGroup('my-cluster-ng2',
    cluster = cluster.core,
    instance_type = 't2.medium',
    desired_capacity = 1,
    spot_price = '1',
    min_size = 1,
    max_size = 2,
    labels = {'preemptible': 'true'},
    taints = {
        'special': {
            'value': 'true',
            'effect': 'NoSchedule',
        },
    },
    instance_profile = instance_profile_2,
    opts = pulumi.ResourceOptions(
        parent = cluster,
        providers = {
            'kubernetes': cluster.provider,
        }
    )
)

# Export the cluster's kubeconfig.
pulumi.export('kubeconfig', cluster.kubeconfig)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
	"encoding/json"
	"fmt"

	"github.com/pulumi/pulumi-aws/sdk/v4/go/aws/iam"
	"github.com/pulumi/pulumi-eks/sdk/go/eks"
	k8s "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Per NodeGroup IAM: each NodeGroup will bring its own, specific instance role and profile.
		managedPolicyArns := []string{
			"arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy",
			"arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy",
			"arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly",
		}

		// Creates a role and attaches the EKS worker node IAM managed policies. Used a few times below,
		// to create multiple roles, so we use a function to avoid repeating ourselves.
		createRole := func(name string) (*iam.Role, error) {
			role, err := iam.NewRole(ctx, name, &iam.RoleArgs{
				AssumeRolePolicy: pulumi.String(`{
    "Version": "2012-10-17",
    "Statement": [{
        "Sid": "AllowAssumeRole",
        "Effect": "Allow",
        "Principal": "ec2.amazonaws.com",
		"Action": "sts:AssumeRole"
    }]
}
`),
			})
			if err != nil {
				return nil, err
			}

			counter := 0
			for _, policy := range managedPolicyArns {
				// Create RolePolicyAttachment without returning it.
				_, err := iam.NewRolePolicyAttachment(ctx,
					fmt.Sprintf("%s-policy-%d", name, counter),
					&iam.RolePolicyAttachmentArgs{
						PolicyArn: pulumi.String(policy),
						Role:      role.Arn,
					},
				)
				if err != nil {
					return nil, err
				}
				counter++
			}

			return role, nil
		}

		// Now create the roles and instance profiles for the two worker groups.
		role1, err := createRole("my-worker-role1")
		if err != nil {
			return err
		}
		role2, err := createRole("my-worker-role2")
		if err != nil {
			return err
		}
		instanceProfile1, err := iam.NewInstanceProfile(ctx, "my-instance-profile1",
			&iam.InstanceProfileArgs{Role: role1})
		if err != nil {
			return err
		}
		instanceProfile2, err := iam.NewInstanceProfile(ctx, "my-instance-profile2",
			&iam.InstanceProfileArgs{Role: role2})
		if err != nil {
			return err
		}

		// Create an EKS cluster with the many IAM roles to register with the cluster auth.
		cluster, err := eks.NewCluster(ctx, "my-cluster", &eks.ClusterArgs{
			SkipDefaultNodeGroup: pulumi.Bool(true),
			InstanceRoles:        iam.RoleArray{role1, role2},
		})
		if err != nil {
			return err
		}

		// Create a Kubernetes provider using the new cluster's Kubeconfig.
		eksProvider, err := k8s.NewProvider(ctx, "eksProvider", &k8s.ProviderArgs{
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
		eksProviders := pulumi.ProviderMap(map[string]pulumi.ProviderResource{
			"kubernetes": eksProvider,
		})

		// Now create multiple node groups, each using a different instance profile for each role.

		// First, create a node group for fixed compute.
		_, err = eks.NewNodeGroup(ctx, "my-cluster-ng1", &eks.NodeGroupArgs{
			Cluster:         cluster.Core,
			InstanceType:    pulumi.String("t2.medium"),
			DesiredCapacity: pulumi.Int(2),
			MinSize:         pulumi.Int(1),
			MaxSize:         pulumi.Int(3),
			Labels: pulumi.StringMap{
				"ondemand": pulumi.String("true"),
			},
			InstanceProfile: instanceProfile1,
		}, eksProviders)
		if err != nil {
			return err
		}

		// Now create a preemptible node group, using spot pricing, for our variable, ephemeral workloads.
		_, err = eks.NewNodeGroup(ctx, "my-cluster-ng2", &eks.NodeGroupArgs{
			Cluster:         cluster.Core,
			InstanceType:    pulumi.String("t2.medium"),
			DesiredCapacity: pulumi.Int(1),
			SpotPrice:       pulumi.String("1"),
			MinSize:         pulumi.Int(1),
			MaxSize:         pulumi.Int(2),
			Labels: pulumi.StringMap{
				"preemptible": pulumi.String("true"),
			},
			Taints: eks.TaintMap{
				"special": eks.TaintArgs{
					Value:  pulumi.String("true"),
					Effect: pulumi.String("NoSchedule"),
				},
			},
			InstanceProfile: instanceProfile2,
		}, eksProviders)
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
using K8s = Pulumi.Kubernetes;
using Newtonsoft.Json;
using Pulumi;
using Pulumi.Aws.Iam;
using Pulumi.Eks;
using Pulumi.Eks.Inputs;
using System;

class MyStack : Stack
{
    public MyStack()
    {
		// Per NodeGroup IAM: each NodeGroup will bring its own, specific instance role and profile.
		string[] managedPolicyArns = {
			"arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy",
			"arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy",
			"arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly",
		};

		// Creates a role and attaches the EKS worker node IAM managed policies. Used a few times below,
		// to create multiple roles, so we use a function to avoid repeating ourselves.
		Func<string, Role> createRole = (name) => {
            var role = new Role(name, new RoleArgs {
                AssumeRolePolicy = @"{
    ""Version"": ""2012-10-17"",
    ""Statement"": [{
        ""Sid"": ""AllowAssumeRole"",
        ""Effect"": ""Allow"",
        ""Principal"": ""ec2.amazonaws.com"",
		""Action"": ""sts:AssumeRole""
    }]
}
"
            });

            var counter = 0;
            foreach (var policy in managedPolicyArns) {
                new RolePolicyAttachment(
                    String.Format("{0}-policy-{1}", name, counter),
                    new RolePolicyAttachmentArgs {
                        PolicyArn = policy,
                        Role = role.Arn,
                    }
                );
            }

            return role;
        };

		// Now create the roles and instance profiles for the two worker groups.
        var role1 = createRole("my-worker-role1");
        var role2 = createRole("my-worker-role2");
        var instanceProfile1 = new InstanceProfile("my-instance-profile1",
            new InstanceProfileArgs { Role = role1.Arn });
        var instanceProfile2 = new InstanceProfile("my-instance-profile2",
            new InstanceProfileArgs { Role = role2.Arn });

		// Create an EKS cluster with the many IAM roles to register with the cluster auth.
        var cluster = new Cluster("my-cluster", new ClusterArgs {
            SkipDefaultNodeGroup = true,
            InstanceRoles = { role1, role2 },
        });

		// Create a Kubernetes provider using the new cluster's Kubeconfig.
        var eksProvider = new K8s.Provider("eksProvider", new K8s.ProviderArgs {
            KubeConfig = cluster.Kubeconfig.Apply(JsonConvert.SerializeObject)
        });

		// Now create multiple node groups, each using a different instance profile for each role.

		// First, create a node group for fixed compute.
        var fixedNodeGroup = new NodeGroup("my-cluster-ng1",
            new NodeGroupArgs {
                Cluster = cluster.Core,
                InstanceType = "t2.medium",
                DesiredCapacity = 2,
                MinSize = 1,
                MaxSize = 3,
                Labels = {
                    { "ondemand", "true" }
                },
                InstanceProfile = instanceProfile1,
            },
            new ComponentResourceOptions {
                Providers = { eksProvider }
            }
        );

        // Now create a preemptible node group, using spot pricing, for our variable, ephemeral workloads.
        var spotNodeGroup = new NodeGroup("my-cluster-ng2",
            new NodeGroupArgs {
                Cluster = cluster.Core,
                InstanceType = "t2.medium",
                DesiredCapacity = 1,
                SpotPrice = "1",
                MinSize = 1,
                MaxSize = 2,
                Labels = {
                    { "preemptible", "true" }
                },
                Taints = {
                    {
                        "special",
                        new TaintArgs {
                            Value = "true",
                            Effect = "NoSchedule"
                        }
                    }
                },
                InstanceProfile = instanceProfile2,
            },
            new ComponentResourceOptions {
                Providers = { eksProvider }
            }
        );

        // Export the cluster's kubeconfig.
        this.Kubeconfig = cluster.Kubeconfig;
    }

    [Output]
    public Output<object> Kubeconfig { get; set; }
}
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

The [`roleMappings` property]({{< relref "/docs/reference/pkg/nodejs/pulumi/eks#ClusterOptions-roleMappings" >}})
for your EKS cluster lets you configure custom IAM roles. For example, you can create different IAM roles for cluster
admins, automation accounts (for CI/CD), and production roles, and supply them to `roleMappings`; this has the effect of
placing them in the `aws-auth` ConfigMap for your cluster automatically. Pulumi also lets you configure Kubernetes
objects, so that can also then create the RBAC cluster role bindings in your cluster to tie everything together.

For a complete example of this in action, see
[Simplifying Kubernetes RBAC in Amazon EKS]({{< relref "simplify-kubernetes-rbac-in-amazon-eks-with-open-source-pulumi-packages" >}}).

## Deploying Kubernetes Apps to Your EKS Cluster

Pulumi supports the entire Kubernetes object model in the [@pulumi/kubernetes]({{< relref "/docs/reference/pkg/kubernetes" >}})
package. For more information on these object types, including Deployments, Services, and Pods, see
[Understanding Kubernetes Objects](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/).

With Pulumi, you describe your desired Kubernetes configuration, and `pulumi up` will diff between the current
state and what is desired, and then drive the API server to bring your desired state into existence.

For example, this program creates a simple load balanced NGINX service, exporting its URL:

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language javascript %}}

```javascript
const k8s = require("@pulumi/kubernetes");

// Create an NGINX Deployment and load balanced Service.
const appName = "my-app";
const appLabels = { appClass: appName };
const deployment = new k8s.apps.v1.Deployment(`${appName}-dep`, {
    metadata: { labels: appLabels },
    spec: {
        replicas: 2,
        selector: { matchLabels: appLabels },
        template: {
            metadata: { labels: appLabels },
            spec: {
                containers: [{
                    name: appName,
                    image: "nginx",
                    ports: [{ name: "http", containerPort: 80 }]
                }],
            }
        }
    },
});
const service = new k8s.core.v1.Service(`${appName}-svc`, {
    metadata: { labels: appLabels },
    spec: {
        type: "LoadBalancer",
        ports: [{ port: 80, targetPort: "http" }],
        selector: appLabels,
    },
});

// Export the URL for the load balanced service.
module.exports = {
    url: service.status.loadBalancer.ingress[0].hostname,
};
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as k8s from "@pulumi/kubernetes";

// Create an NGINX Deployment and load balanced Service.
const appName = "my-app";
const appLabels = { appClass: appName };
const deployment = new k8s.apps.v1.Deployment(`${appName}-dep`, {
    metadata: { labels: appLabels },
    spec: {
        replicas: 2,
        selector: { matchLabels: appLabels },
        template: {
            metadata: { labels: appLabels },
            spec: {
                containers: [{
                    name: appName,
                    image: "nginx",
                    ports: [{ name: "http", containerPort: 80 }]
                }],
            }
        }
    },
});
const service = new k8s.core.v1.Service(`${appName}-svc`, {
    metadata: { labels: appLabels },
    spec: {
        type: "LoadBalancer",
        ports: [{ port: 80, targetPort: "http" }],
        selector: appLabels,
    },
});

// Export the URL for the load balanced service.
export const url = service.status.loadBalancer.ingress[0].hostname;
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
import pulumi_kubernetes as k8s

# Create an NGINX Deployment and load balanced Service.
app_name = 'my-app'
app_labels = { 'app': app_name }
deployment = k8s.apps.v1.Deployment(f'{app_name}-dep',
    spec = k8s.apps.v1.DeploymentSpecArgs(
        selector = k8s.meta.v1.LabelSelectorArgs(match_labels = app_labels),
        replicas = 2,
        template = k8s.core.v1.PodTemplateSpecArgs(
            metadata = k8s.meta.v1.ObjectMetaArgs(labels = app_labels),
            spec = k8s.core.v1.PodSpecArgs(containers = [
                k8s.core.v1.ContainerArgs(name = 'nginx', image = 'nginx')
            ]),
        ),
    )
)
service = k8s.core.v1.Service(f'{app_name}-svc',
    spec = k8s.core.v1.ServiceSpecArgs(
        type = 'LoadBalancer',
        selector = app_labels,
        ports = [ k8s.core.v1.ServicePortArgs(port = 80) ],
    )
)

# Export the URL for the load balanced service.
pulumi.export('url', service.status.load_balancer.ingress[0].hostname)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
	"fmt"

	k8s "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes"
	appsv1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/apps/v1"
	corev1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/core/v1"
	metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/meta/v1"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
        // Create an NGINX Deployment and load balanced Service.
		appName := "my-app"
		appLabels := pulumi.StringMap{"app": pulumi.String(appName)}
		_, err = appsv1.NewDeployment(ctx,
			fmt.Sprintf("%s-dep", appName),
			&appsv1.DeploymentArgs{
				Spec: &appsv1.DeploymentSpecArgs{
					Selector: &metav1.LabelSelectorArgs{MatchLabels: appLabels},
					Replicas: pulumi.Int(2),
					Template: &corev1.PodTemplateSpecArgs{
						Metadata: &metav1.ObjectMetaArgs{Labels: appLabels},
						Spec: &corev1.PodSpecArgs{
							Containers: corev1.ContainerArray{
								&corev1.ContainerArgs{
									Name:  pulumi.String("nginx"),
									Image: pulumi.String("nginx"),
								},
							},
						},
					},
				},
			},
		)
		if err != nil {
			return nil
		}
		service, err := corev1.NewService(ctx,
			fmt.Sprintf("%s-svc", appName),
			&corev1.ServiceArgs{
				Spec: &corev1.ServiceSpecArgs{
					Type:     pulumi.String("LoadBalancer"),
					Selector: appLabels,
					Ports: corev1.ServicePortArray{
						&corev1.ServicePortArgs{
							Port: pulumi.Int(80),
						},
					},
				},
			},
		)
		if err != nil {
			return err
		}

		// Export the URL for the load balanced service.
		ctx.Export("url", service.Status.ApplyT(func(status interface{}) string {
			return *status.(*corev1.ServiceStatus).LoadBalancer.Ingress[0].Hostname
		}))
	})
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using K8sApps = Pulumi.Kubernetes.Apps.V1;
using K8sAppsArgs = Pulumi.Kubernetes.Types.Inputs.Apps.V1;
using K8sCore = Pulumi.Kubernetes.Core.V1;
using K8sCoreArgs = Pulumi.Kubernetes.Types.Inputs.Core.V1;
using K8sMetaArgs = Pulumi.Kubernetes.Types.Inputs.Meta.V1;
using Pulumi;
using System;
using System.Collections.Generic;
using System.Collections.Immutable;

class MyStack : Stack
{
    public MyStack()
    {
        // Create an NGINX Deployment and load balanced Service.
        var appName = "my-app";
        var appLabels = new Dictionary<string, string>{ { "app", appName } }.ToImmutableDictionary();
        var deployment = new K8sApps.Deployment(
            String.Format("{0}-dep", appName),
            new K8sAppsArgs.DeploymentArgs {
                Spec = new K8sAppsArgs.DeploymentSpecArgs {
                    Selector = new K8sMetaArgs.LabelSelectorArgs { MatchLabels = appLabels },
                    Replicas = 2,
                    Template = new K8sCoreArgs.PodTemplateSpecArgs {
                        Metadata = new K8sMetaArgs.ObjectMetaArgs { Labels = appLabels },
                        Spec = new K8sCoreArgs.PodSpecArgs {
                            Containers = {
                                new K8sCoreArgs.ContainerArgs {
                                    Name = appName,
                                    Image = "nginx",
                                },
                            },
                        },
                    },
                },
            }
        );
        var service = new K8sCore.Service(
            String.Format("{0}-svc", appName),
            new K8sCoreArgs.ServiceArgs {
                Spec = new K8sCoreArgs.ServiceSpecArgs {
                    Type = "LoadBalancer",
                    Selector = appLabels,
                    Ports = {
                        new K8sCoreArgs.ServicePortArgs { Port = 80 },
                    },
                },
            }
        );

		// Export the URL for the load balanced service.
        this.Url = service.Status.Apply((status) =>
            status.LoadBalancer.Ingress[0].Hostname);
    }

    [Output]
    public Output<string> Url { get; set; }
}
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

### Deploying to Specific Clusters

By default, Pulumi targets clusters based on your local kubeconfig, just like `kubectl` does. So if your `kubectl`
client is set up to talk to your EKS cluster, deployments will target it. We saw earlier in
[Provisioning a New EKS Cluster](#provisioning-a-new-eks-cluster), however, that you can deploy into any
Kubernetes cluster created in your Pulumi program. This is because each Kubernetes object specification accepts
an optional "provider" that can programmatically specify a kubeconfig to use.

This is done by instantiating a new `kubernetes.Provider` object, and providing one or many of these properties:

* `cluster`: A cluster name to target, if there are many in your kubeconfig to choose from.
* `context`: The name of the kubeconfig context to use, if there are many to choose from.
* `kubeconfig`: A stringified JSON representing a full kubeconfig to use instead of your local machine's.

For example, to deploy an NGINX Deployment into a cluster whose kubeconfig our program has access to:

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language javascript %}}

```javascript
const k8s = require("@pulumi/kubernetes");

// Create a provider using our Kubernetes config:
const provider = new k8s.Provider("custom-provider", { kubeconfig: "..." });

// Declare a deployment that targets this provider:
const appName = "my-app";
const appLabels = { appClass: appName };
const deployment = new k8s.apps.v1.Deployment(`${appName}-dep`,
    {
        metadata: { labels: appLabels },
        spec: {
            replicas: 2,
            selector: { matchLabels: appLabels },
            template: {
                metadata: { labels: appLabels },
                spec: {
                    containers: [{
                        name: appName,
                        image: "nginx",
                        ports: [{ name: "http", containerPort: 80 }]
                    }],
                }
            }
        },
    },
    {
        // Use our custom provider for this object.
        provider: provider,
    },
);
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as k8s from "@pulumi/kubernetes";

// Create a provider using our Kubernetes config:
const provider = new k8s.Provider("custom-provider", { kubeconfig: "..." });

// Declare a deployment that targets this provider:
const appName = "my-app";
const appLabels = { appClass: appName };
const deployment = new k8s.apps.v1.Deployment(`${appName}-dep`,
    {
        metadata: { labels: appLabels },
        spec: {
            replicas: 2,
            selector: { matchLabels: appLabels },
            template: {
                metadata: { labels: appLabels },
                spec: {
                    containers: [{
                        name: appName,
                        image: "nginx",
                        ports: [{ name: "http", containerPort: 80 }]
                    }],
                }
            }
        },
    },
    {
        // Use our custom provider for this object.
        provider: provider,
    },
);
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
import pulumi_kubernetes as k8s

# Create a provider using our Kubernetes config:
provider = k8s.Provider('custom-provider',
    k8s.ProviderArgs(kubeconfig = '...')
)

# Declare a deployment that targets this provider:
app_name = 'my-app'
app_labels = { 'app': app_name }
deployment = k8s.apps.v1.Deployment(f'{app_name}-dep',
    spec = k8s.apps.v1.DeploymentSpecArgs(
        selector = k8s.meta.v1.LabelSelectorArgs(match_labels = app_labels),
        replicas = 2,
        template = k8s.core.v1.PodTemplateSpecArgs(
            metadata = k8s.meta.v1.ObjectMetaArgs(labels = app_labels),
            spec = k8s.core.v1.PodSpecArgs(containers = [
                k8s.core.v1.ContainerArgs(name = 'nginx', image = 'nginx')
            ]),
        ),
    ),
    # Use our custom provider for this object.
    opts = pulumi.ResourceOptions(provider = provider)
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
	"fmt"

	k8s "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes"
	appsv1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/apps/v1"
	corev1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/core/v1"
	metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/meta/v1"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Create a provider using our Kubernetes config:
		provider, err := k8s.NewProvider(ctx, "custom-provider", &k8s.ProviderArgs{
			Kubeconfig: pulumi.String(""), // ...
		})
		if err != nil {
			return err
		}

		// Declare a deployment that targets this provider:
		appName := "my-app"
		appLabels := pulumi.StringMap{"app": pulumi.String(appName)}
		_, err = appsv1.NewDeployment(ctx,
			fmt.Sprintf("%s-dep", appName),
			&appsv1.DeploymentArgs{
				Spec: &appsv1.DeploymentSpecArgs{
					Selector: &metav1.LabelSelectorArgs{MatchLabels: appLabels},
					Replicas: pulumi.Int(2),
					Template: &corev1.PodTemplateSpecArgs{
						Metadata: &metav1.ObjectMetaArgs{Labels: appLabels},
						Spec: &corev1.PodSpecArgs{
							Containers: corev1.ContainerArray{
								&corev1.ContainerArgs{
									Name:  pulumi.String("nginx"),
									Image: pulumi.String("nginx"),
								},
							},
						},
					},
				},
			},
			// Use our custom provider for this object.
			pulumi.Provider(provider),
		)
		if err != nil {
			return nil
		}

		return nil
	})
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using K8s = Pulumi.Kubernetes;
using K8sApps = Pulumi.Kubernetes.Apps.V1;
using K8sAppsArgs = Pulumi.Kubernetes.Types.Inputs.Apps.V1;
using K8sCore = Pulumi.Kubernetes.Core.V1;
using K8sCoreArgs = Pulumi.Kubernetes.Types.Inputs.Core.V1;
using K8sMetaArgs = Pulumi.Kubernetes.Types.Inputs.Meta.V1;
using Pulumi;
using System;
using System.Collections.Generic;
using System.Collections.Immutable;

class MyStack : Stack
{
    public MyStack()
    {
        // Create a provider using our Kubernetes config:
        var provider = new K8s.Provider("custom-provider", new K8s.ProviderArgs {
            KubeConfig = "..."
        });

        // Declare a deployment that targets this provider:
        var appName = "my-app";
        var appLabels = new Dictionary<string, string>{ { "app", appName } }.ToImmutableDictionary();
        var deployment = new K8sApps.Deployment(
            String.Format("{0}-dep", appName),
            new K8sAppsArgs.DeploymentArgs {
                Spec = new K8sAppsArgs.DeploymentSpecArgs {
                    Selector = new K8sMetaArgs.LabelSelectorArgs { MatchLabels = appLabels },
                    Replicas = 2,
                    Template = new K8sCoreArgs.PodTemplateSpecArgs {
                        Metadata = new K8sMetaArgs.ObjectMetaArgs { Labels = appLabels },
                        Spec = new K8sCoreArgs.PodSpecArgs {
                            Containers = {
                                new K8sCoreArgs.ContainerArgs {
                                    Name = appName,
                                    Image = "nginx",
                                    Ports = {
                                        new K8sCoreArgs.ContainerPortArgs {
                                            Name = "http",
                                            ContainerPortValue = 80,
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
            // Use our custom provider for this object.
            new CustomResourceOptions { Provider = provider }
        );
    }
}
```

{{% /choosable %}}

To ease doing this against an EKS cluster just created, the cluster object itself offers a [`provider` property](
{{< relref "/docs/reference/pkg/nodejs/pulumi/eks#Cluster-provider" >}}) of type `kubernetes.Provider`, already pre-configured.

For more information about configuring access to multiple clusters, see [Configure Access to Multiple Clusters](
https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/) and the
[Pulumi Kubernetes Setup documentation]({{< relref "/docs/intro/cloud-providers/kubernetes/setup" >}}).

## Deploying Existing Kubernetes YAML Config to Your EKS Cluster

Specifying your Kubernetes object configurations in Pulumi lets you take advantage of programming language features,
like variables, loops, conditionals, functions, and classes. It is possible, however, to deploy existing Kubernetes
YAML. The two approaches can be mixed, which is useful when converting an existing project.

The [`ConfigFile` class]({{< relref "/docs/reference/pkg/kubernetes/yaml/configfile" >}}) can be
used to deploy a single YAML file, whereas the [`ConfigGroup` class](
{{< relref "/docs/reference/pkg/kubernetes/yaml/configgroup" >}}) can deploy
a collection of files, either from a set of files or in-memory representations.

For example, imagine we have a directory, `yaml/`, containing the full YAML for the [Kubernetes Guestbook application](
https://kubernetes.io/docs/tutorials/stateless-application/guestbook/), perhaps across multiple files. We can deploy
it using Pulumi into our EKS cluster with the following code and by running `pulumi up`:

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language javascript %}}

```javascript
const eks = require("@pulumi/eks");
const k8s = require("@pulumi/kubernetes");

// Create an EKS cluster.
const cluster = new eks.Cluster("my-cluster");

// Create resources from standard Kubernetes guestbook YAML example.
const guestbook = new k8s.yaml.ConfigGroup("guestbook",
    { files: "yaml/*.yaml" },
    { provider: cluster.provider },
);

// Export the (cluster-private) IP address of the Guestbook frontend.
module.exports = {
    frontendIp: guestbook.getResource("v1/Service", "frontend", "").spec.clusterIP,
};
```

{{% /choosable %}}
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

The `ConfigFile` and `ConfigGroup` classes both support a [`transformations` property](
{{< relref "/docs/reference/pkg/kubernetes#transformations_nodejs" >}}) which can be used to ["monkey patch"](
https://en.wikipedia.org/wiki/Monkey_patch) Kubernetes configuration on the fly. This can be used to rewrite
configuration to include additional services (like Envoy sidecars), inject tags, and so on.

For example, a transformation like the following can make all services private to a cluster, by
changing `LoadBalancer` specs into `ClusterIPs`, in addition to placing objects into a desired namespace:

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language javascript %}}

```javascript
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

Of course, it is easy to create invalid transformations that break your applications, by changing settings the
application or configuration did not expect, so this capability must be used with care.

## Deploying Existing Helm Charts to Your EKS Cluster

Pulumi can deploy [Helm charts](https://helm.sh/) through a variety of means. This includes deploying a chart
by name from the [default Helm "stable charts" repository](https://github.com/helm/charts), from a custom Helm
repository (over the Internet or on-premises), or from a tarball directly.

> For these examples to work, you will need to [install Helm](https://helm.sh/docs/using_helm/#installing-helm)
> and, once installed, initialize it with `helm init --client-only`.

This program installs the stable Wordpress chart into our EKS cluster:

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language javascript %}}

```javascript
const eks = require("@pulumi/eks");
const k8s = require("@pulumi/kubernetes");

// Create an EKS cluster.
const cluster = new eks.Cluster("my-cluster");

// Deploy Wordpress into our cluster.
const wordpress = new k8s.helm.v3.Chart("wordpress", {
    repo: "stable",
    chart: "wordpress",
    values: {
        wordpressBlogName: "My Cool Kubernetes Blog!",
    },
}, { providers: { "kubernetes": cluster.provider } });

// Export the cluster's kubeconfig.
module.exports = {
    kubeconfig: cluster.kubeconfig,
};
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as eks from "@pulumi/eks";
import * as k8s from "@pulumi/kubernetes";

// Create an EKS cluster.
const cluster = new eks.Cluster("my-cluster");

// Deploy Wordpress into our cluster.
const wordpress = new k8s.helm.v3.Chart("wordpress", {
    repo: "stable",
    chart: "wordpress",
    values: {
        wordpressBlogName: "My Cool Kubernetes Blog!",
    },
}, { providers: { "kubernetes": cluster.provider } });

// Export the cluster's kubeconfig.
export const kubeconfig = cluster.kubeconfig;
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
import pulumi_eks as eks
import pulumi_kubernetes as k8s

# Create an EKS cluster.
cluster = eks.Cluster('my-cluster')

# Deploy Wordpress into our cluster.
wordpress = k8s.helm.v3.Chart('wordpress',
    k8s.helm.v3.ChartOpts(
        repo = 'stable',
        chart = 'wordpress',
        values = {
            'wordpressBlogName': 'My Cool Kubernetes Blog!'
        },
    ),
    opts = pulumi.ResourceOptions(
        providers = {
            'kubernetes': cluster.provider,
        }
    )
)

# Export the cluster's kubeconfig.
pulumi.export('kubeconfig', cluster.kubeconfig)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
	"encoding/json"

	"github.com/pulumi/pulumi-eks/sdk/go/eks"
	k8s "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes"
	helm "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/helm/v3"
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
		eksProvider, err := k8s.NewProvider(ctx, "my-provider", &k8s.ProviderArgs{
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

		// Deploy Wordpress into our cluster.
		_, err = helm.NewChart(ctx, "wordpress",
			helm.ChartArgs{
				Repo:  pulumi.String("stable"),
				Chart: pulumi.String("wordpress"),
				Values: pulumi.Map{
					"wordpressBlogName": pulumi.String("My Cool Kubernetes Blog!"),
				},
			},
			pulumi.ProviderMap(map[string]pulumi.ProviderResource{
				"kubernetes": eksProvider,
			}),
		)
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
using Helm = Pulumi.Kubernetes.Helm;
using K8s = Pulumi.Kubernetes;
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

        // Deploy Wordpress into our cluster.
        var wordpress = new Helm.V3.Chart("wordpress",
            new Helm.ChartArgs {
                Repo = "stable",
                Chart = "wordpress",
                Values = {
                    { "wordpressBlogName", "My Cool Kubernetes Blog!" },
                },
            },
            new ComponentResourceOptions { Provider = eksProvider }
        );

        // Export the cluster's kubeconfig.
        this.Kubeconfig = cluster.Kubeconfig;
    }

    [Output]
    public Output<object> Kubeconfig { get; set; }
}
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

As mentioned, there are other ways to fetch the chart's contents. For example, we can use a custom repo:

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language javascript %}}

```javascript
const chart = new k8s.helm.v3.Chart("empty", {
    chart: "raw",
    version: "0.1.0",
    fetchOpts: {
        repo: "https://charts.helm.sh/incubator",
    },
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
const chart = new k8s.helm.v3.Chart("empty", {
    chart: "raw",
    version: "0.1.0",
    fetchOpts: {
        repo: "https://charts.helm.sh/incubator",
    },
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
chart = k8s.helm.v3.Chart('empty',
    k8s.helm.v3.ChartOpts(
        chart = 'raw',
        version = '0.1.0',
        fetch_opts = {
            'repo': 'https://charts.helm.sh/incubator'
        }
    )
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
_, err = helm.NewChart(ctx, "empty",
    helm.ChartArgs{
        Chart:   pulumi.String("raw"),
        Version: pulumi.String("0.1.0"),
        FetchArgs: helm.FetchArgs{
            Repo: pulumi.String("https://charts.helm.sh/incubator"),
        },
    },
)
if err != nil {
    return err
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var chart = new Helm.V3.Chart("empty",
    new Helm.ChartArgs {
        Chart = "raw",
        Version = "0.1.0",
        FetchOptions = new Helm.ChartFetchArgs {
            Repo = "https://charts.helm.sh/incubator",
        },
    }
);
```

{{% /choosable %}}

Or, we can use a tarball fetched from a web URL:

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language javascript %}}

```javascript
const chart = new k8s.helm.v3.Chart("empty1", {
    chart: "https://charts.helm.sh/incubatorraw-0.1.0.tgz",
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
const chart = new k8s.helm.v3.Chart("empty1", {
    chart: "https://charts.helm.sh/incubatorraw-0.1.0.tgz",
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
chart = k8s.helm.v3.Chart('empty1',
    k8s.helm.v3.LocalChartOpts(
        chart = 'https://charts.helm.sh/incubatorraw-0.1.0.tgz',
    )
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
_, err = helm.NewChart(ctx, "empty",
    helm.ChartArgs{
        Chart:   pulumi.String("https://charts.helm.sh/incubatorraw-0.1.0.tgz"),
    },
)
if err != nil {
    return err
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var chart = new Helm.V3.Chart("empty",
    new Helm.ChartArgs {
        Chart = "https://charts.helm.sh/incubatorraw-0.1.0.tgz",
    }
);
```

{{% /choosable %}}

## Using an ECR Container Image from an EKS Kubernetes Deployment

[Pulumi Crosswalk for AWS ECR]({{< relref "ecr" >}}) enables you to build, publish, and consume private Docker
images easily using Amazon's Elastic Container Registry (ECR). The [`aws.ecr.buildAndPushImage` function](
{{< relref "/docs/reference/pkg/nodejs/pulumi/awsx/ecr#buildAndPushImage" >}}) takes a name and a relative location on disk, and will

* Provision a private ECR registry using that name
* Build the `Dockerfile` found at the relative location supplied
* Push the resulting image to that registry
* Return the repository image information, including an image name your Kubernetes objects can use

This makes it easy to version your container images alongside the Kubernetes specifications that consume them.

> *Note:* for more complete examples of building and publishing to _any_ private container registry, including AWS, Azure, Google Cloud, and the Docker Hub, please refer to the article [Build and publish container images to any cloud with Infrastructure as Code]({{< relref "/blog/build-publish-containers-iac" >}}).

For example, let's say we have an `app/` directory containing a fully Dockerized application (including a
`Dockerfile`), and would like to deploy that as a Deployment and Service running in our EKS cluster. This program
accomplishes this with a single `pulumi up` command:

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language javascript %}}

```javascript
const awsx = require("@pulumi/awsx");
const eks = require("@pulumi/eks");
const k8s = require("@pulumi/kubernetes");

// Create a new EKS cluster.
const cluster = new eks.Cluster("cluster");

// Build and publish our app's container image.
const image = awsx.ecr.buildAndPushImage("my-repo", "./app");

// Create a NGINX Deployment and load balanced Service, running our app.
const appName = "my-app";
const appLabels = { appClass: appName };
const deployment = new k8s.apps.v1.Deployment(`${appName}-dep`, {
    metadata: { labels: appLabels },
    spec: {
        replicas: 2,
        selector: { matchLabels: appLabels },
        template: {
            metadata: { labels: appLabels },
            spec: {
                containers: [{
                    name: appName,
                    image: image.image(),
                    ports: [{ name: "http", containerPort: 80 }]
                }],
            }
        }
    },
}, { provider: cluster.provider });
const service = new k8s.core.v1.Service(`${appName}-svc`, {
    metadata: { labels: appLabels },
    spec: {
        type: "LoadBalancer",
        ports: [{ port: 80, targetPort: "http" }],
        selector: appLabels,
    },
}, { provider: cluster.provider });

// Export the URL for the load balanced service.
module.exports = {
    url: service.status.loadBalancer.ingress[0].hostname,
};
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as awsx from "@pulumi/awsx";
import * as eks from "@pulumi/eks";
import * as k8s from "@pulumi/kubernetes";

// Create a new EKS cluster.
const cluster = new eks.Cluster("cluster");

// Build and publish our app's container image.
const image = awsx.ecr.buildAndPushImage("my-repo", "./app");

// Create a NGINX Deployment and load balanced Service, running our app.
const appName = "my-app";
const appLabels = { appClass: appName };
const deployment = new k8s.apps.v1.Deployment(`${appName}-dep`, {
    metadata: { labels: appLabels },
    spec: {
        replicas: 2,
        selector: { matchLabels: appLabels },
        template: {
            metadata: { labels: appLabels },
            spec: {
                containers: [{
                    name: appName,
                    image: image.image(),
                    ports: [{ name: "http", containerPort: 80 }]
                }],
            }
        }
    },
}, { provider: cluster.provider });
const service = new k8s.core.v1.Service(`${appName}-svc`, {
    metadata: { labels: appLabels },
    spec: {
        type: "LoadBalancer",
        ports: [{ port: 80, targetPort: "http" }],
        selector: appLabels,
    },
}, { provider: cluster.provider });

// Export the URL for the load balanced service.
export const url = service.status.loadBalancer.ingress[0].hostname;
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import base64
import pulumi
import pulumi_aws as aws
import pulumi_docker as docker
import pulumi_eks as eks
import pulumi_kubernetes as k8s

# Create an EKS cluster with the default configuration.
cluster = eks.Cluster('my-cluster');

# Build and publish our app's container image:

# ...1) Create a private ECR repository.
repo = aws.ecr.Repository('my-repo')
image_name = repo.repository_url

# ...2) Get registry info (creds and endpoint).
def get_registry_info(rid):
    """Get registry info (creds and endpoint)."""
    creds = aws.ecr.get_credentails(registry_id=rid)
    decoded = base64.b64decode(creds.authorization_token).decode()
    parts = decoded.split(':')
    if len(parts) != 2:
        raise Exception('Invalid credentials')
    return docker.ImageRegistry(creds.proxy_endpoint, parts[0], parts[1])
registry_info = repo.registry_id.apply(get_registry_info)

# ...3) Build and publish the container image.
image = docker.Image('my-app-image',
    build='app',
    image_name=image_name,
    registry=registry_info
)

# Create a NGINX Deployment and load balanced Service, running our app.
app_name = 'my-app'
app_labels = { 'app': app_name }
deployment = k8s.apps.v1.Deployment(f'{app_name}-dep',
    spec = k8s.apps.v1.DeploymentSpecArgs(
        selector = k8s.meta.v1.LabelSelectorArgs(match_labels = app_labels),
        replicas = 2,
        template = k8s.core.v1.PodTemplateSpecArgs(
            metadata = k8s.meta.v1.ObjectMetaArgs(labels = app_labels),
            spec = k8s.core.v1.PodSpecArgs(containers = [
                k8s.core.v1.ContainerArgs(
                    name = app_name,
                    image = image.image_name
                )
            ]),
        ),
    ), opts = pulumi.ResourceOptions(provider = cluster.provider)
)
service = k8s.core.v1.Service(f'{app_name}-svc',
    spec = k8s.core.v1.ServiceSpecArgs(
        type = 'LoadBalancer',
        selector = app_labels,
        ports = [ k8s.core.v1.ServicePortArgs(port = 80) ],
    ), opts = pulumi.ResourceOptions(provider = cluster.provider)
)

# Export the URL for the load balanced service.
pulumi.export('ingress_ip', service.status.load_balancer.ingress[0].ip)

# Export the cluster's kubeconfig.
pulumi.export('kubeconfig', cluster.kubeconfig)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
	"encoding/base64"
	"encoding/json"
	"errors"
	"fmt"
	"strings"

	"github.com/pulumi/pulumi-aws/sdk/v4/go/aws/ecr"
	"github.com/pulumi/pulumi-docker/sdk/v3/go/docker"
	"github.com/pulumi/pulumi-eks/sdk/go/eks"
	k8s "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes"
	appsv1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/apps/v1"
	corev1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/core/v1"
	metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/meta/v1"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Create an EKS cluster with the default configuration.
		cluster, err := eks.NewCluster(ctx, "my-cluster", nil)
		if err != nil {
			return err
		}

		// Create a Kubernetes provider using the new cluster's Kubeconfig.
		prov, err := k8s.NewProvider(ctx, "eksProvider", &k8s.ProviderArgs{
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

		// Build and publish our app's container image:

        // ...1) Create a private ECR repository.
		repo, err := ecr.NewRepository(ctx, "my-repo", nil)
		if err != nil {
			return err
		}

		// ...2) Get registry info (creds and endpoint).
		imageName := repo.RepositoryUrl
		registryInfo := repo.RegistryId.ApplyT(func(id string) (docker.ImageRegistry, error) {
			creds, err := ecr.GetCredentials(ctx, &ecr.GetCredentialsArgs{RegistryId: id})
			if err != nil {
				return docker.ImageRegistry{}, err
			}
			decoded, err := base64.StdEncoding.DecodeString(creds.AuthorizationToken)
			if err != nil {
				return docker.ImageRegistry{}, err
			}
			parts := strings.Split(string(decoded), ":")
			if len(parts) != 2 {
				return docker.ImageRegistry{}, errors.New("Invalid credentials")
			}
			return docker.ImageRegistry{
				Server:   creds.ProxyEndpoint,
				Username: parts[0],
				Password: parts[1],
			}, nil
		}).(docker.ImageRegistryOutput)

		// ...3) Build and publish the container image.
		image, err := docker.NewImage(ctx, "my-app-image", &docker.ImageArgs{
			Build:     &docker.DockerBuildArgs{Context: pulumi.String("app")},
			ImageName: imageName,
			Registry:  registryInfo,
		})

		// Create a NGINX Deployment and load balanced Service, running our app.
		appName := "my-app"
		appLabels := pulumi.StringMap{"app": pulumi.String(appName)}
		_, err = appsv1.NewDeployment(ctx,
			fmt.Sprintf("%s-dep", appName),
			&appsv1.DeploymentArgs{
				Spec: &appsv1.DeploymentSpecArgs{
					Selector: &metav1.LabelSelectorArgs{MatchLabels: appLabels},
					Replicas: pulumi.Int(2),
					Template: &corev1.PodTemplateSpecArgs{
						Metadata: &metav1.ObjectMetaArgs{Labels: appLabels},
						Spec: &corev1.PodSpecArgs{
							Containers: corev1.ContainerArray{
								&corev1.ContainerArgs{
									Name:  pulumi.String(appName),
									Image: image.ImageName,
								},
							},
						},
					},
				},
			},
			pulumi.Provider(prov),
		)
		if err != nil {
			return nil
		}
		service, err := corev1.NewService(ctx,
			fmt.Sprintf("%s-svc", appName),
			&corev1.ServiceArgs{
				Spec: &corev1.ServiceSpecArgs{
					Type:     pulumi.String("LoadBalancer"),
					Selector: appLabels,
					Ports: corev1.ServicePortArray{
						&corev1.ServicePortArgs{
							Port: pulumi.Int(80),
						},
					},
				},
			},
			pulumi.Provider(prov),
		)
		if err != nil {
			return err
		}

		// Export the URL for the load balanced service.
		ctx.Export("url", service.Status.ApplyT(func(status interface{}) string {
			return *status.(*corev1.ServiceStatus).LoadBalancer.Ingress[0].Hostname
		}))
		return nil
	})
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using Pulumi.Docker;
using Ecr = Pulumi.Aws.Ecr;
using K8s = Pulumi.Kubernetes;
using K8sApps = Pulumi.Kubernetes.Apps.V1;
using K8sAppsArgs = Pulumi.Kubernetes.Types.Inputs.Apps.V1;
using K8sCore = Pulumi.Kubernetes.Core.V1;
using K8sCoreArgs = Pulumi.Kubernetes.Types.Inputs.Core.V1;
using K8sMetaArgs = Pulumi.Kubernetes.Types.Inputs.Meta.V1;
using Newtonsoft.Json;
using Pulumi;
using Pulumi.Eks;
using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Text;

class MyStack : Stack
{
    public MyStack()
    {
        // Create an EKS cluster with the default configuration.
        var cluster = new Cluster("my-cluster");

		// Create a Kubernetes provider using the new cluster's Kubeconfig.
        var eksProvider = new K8s.Provider("eksProvider", new K8s.ProviderArgs {
            KubeConfig = cluster.Kubeconfig.Apply(JsonConvert.SerializeObject)
        });

        // Build and publish our app's container image:

        // ...1) Create a private ECR repository.
        var repo = new Ecr.Repository("my-repo");
        var imageName = repo.RepositoryUrl;

        // ...2) Get registry info (creds and endpoint).
        var registryInfo = repo.RegistryId.Apply(async (id) =>
        {
            var creds = await Ecr.GetCredentials.InvokeAsync(new Ecr.GetCredentialsArgs { RegistryId = id });
            var decodedData = Convert.FromBase64String(creds.AuthorizationToken);
            var decoded = ASCIIEncoding.ASCII.GetString(decodedData);

            var parts = decoded.Split(':');
            if (parts.Length != 2)
            {
                throw new Exception("Invalid credentials");
            }

            return new ImageRegistry
            {
                Server = creds.ProxyEndpoint,
                Username = parts[0],
                Password = parts[1],
            };
        });

        // ...3) Build and publish the container image.
        var image = new Image("my-image", new ImageArgs
        {
            Build = new DockerBuild { Context = "app" },
            ImageName = imageName,
            Registry = registryInfo,
        });

		// Create a NGINX Deployment and load balanced Service, running our app.
        var appName = "my-app";
        var appLabels = new Dictionary<string, string>{ { "app", appName } }.ToImmutableDictionary();
        var deployment = new K8sApps.Deployment(
            String.Format("{0}-dep", appName),
            new K8sAppsArgs.DeploymentArgs {
                Spec = new K8sAppsArgs.DeploymentSpecArgs {
                    Selector = new K8sMetaArgs.LabelSelectorArgs { MatchLabels = appLabels },
                    Replicas = 2,
                    Template = new K8sCoreArgs.PodTemplateSpecArgs {
                        Metadata = new K8sMetaArgs.ObjectMetaArgs { Labels = appLabels },
                        Spec = new K8sCoreArgs.PodSpecArgs {
                            Containers = {
                                new K8sCoreArgs.ContainerArgs {
                                    Name = appName,
                                    Image = image.ImageName,
                                },
                            },
                        },
                    },
                },
            },
            new CustomResourceOptions { Provider = eksProvider }
        );
        var service = new K8sCore.Service(
            String.Format("{0}-svc", appName),
            new K8sCoreArgs.ServiceArgs {
                Spec = new K8sCoreArgs.ServiceSpecArgs {
                    Type = "LoadBalancer",
                    Selector = appLabels,
                    Ports = {
                        new K8sCoreArgs.ServicePortArgs { Port = 80 },
                    },
                },
            },
            new CustomResourceOptions { Provider = eksProvider }
        );

		// Export the URL for the load balanced service.
        this.Url = service.Status.Apply((status) =>
            status.LoadBalancer.Ingress[0].Hostname);
    }

    [Output]
    public Output<string> Url { get; set; }
}
```

{{% /choosable %}}

For more information about ECR, see [the Pulumi Crosswalk for AWS ECR documentation]({{< relref "ecr" >}}).

## Additional EKS Resources

For more information about Kubernetes and EKS, see the following:

* [Pulumi Kubernetes API Documentation]({{< relref "/docs/reference/pkg/kubernetes" >}})
* [Pulumi EKS API Documentation]({{< relref "/docs/reference/pkg/nodejs/pulumi/eks" >}})
* [Amazon Elastic Kubernetes Service homepage](https://aws.amazon.com/eks/)
* [Kubernetes Documentation](https://kubernetes.io)

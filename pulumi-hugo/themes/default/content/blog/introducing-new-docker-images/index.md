---
title: "Introducing New Slimmer Docker Images"
date: 2020-06-25
draft: false
meta_image: docker.png
meta_desc: "Introducing new language specific Docker images which are smaller and more flexible than before"
authors:
    - lee-briggs
tags:
    - features
    - docker

---

One of the most exciting aspects of using Pulumi can also present some interesting engineering challenges.
Pulumi supports three operating systems, multiple programming languages, and almost 40 different providers. This means creating tooling that works effortlessly across all possible user scenarios can often throw unexpected challenges our way.

Nowhere are these challenges more prevalent than in the Pulumi Docker containers.

The [pulumi/pulumi Docker container](https://hub.docker.com/r/pulumi/pulumi) is almost 3Gb uncompressed, which is generally considered large for a Docker image.
In this post, I'll examine why this container has grown to the size that it is, and talk about how we hope to solve it.

<!--more-->

## Anatomy of a Pulumi Program

Pulumi has the unique ability to interact with cloud providers across many boundaries. As an example, you might want to provision a Kubernetes cluster and install a Helm chart onto that cluster. Pulumi lets you do that from a single "Pulumi program", here's an example:

{{< chooser language "typescript,python,go" >}}

{{% choosable language typescript %}}

```typescript
import * as digitalocean from "@pulumi/digitalocean";
import * as k8s from "@pulumi/kubernetes";
import * as pulumi from "@pulumi/pulumi";

const config = new pulumi.Config();
const nodeCount = config.getNumber("nodeCount") || 1;

// Create a Kubernetes Cluster in DigitalOcean
const cluster = new digitalocean.KubernetesCluster("do-cluster", {
  region: digitalocean.Regions.SFO2,
  version: digitalocean.getKubernetesVersions({versionPrefix: "1.16"}).then(p => p.latestVersion),
  nodePool: {
      name: "default",
      size: "s-1vcpu-2gb",
      nodeCount: nodeCount,
  },
});

// configure a kubernetes provider
const provider = new k8s.Provider("k8s", { kubeconfig: cluster.kubeConfigs[0].rawConfig })

const namespace = new k8s.core.v1.Namespace("ns", {
    metadata: {
        name: "nginx-ingress",
    }
}, { provider: provider });

// deploy nginx-ingress with helm
const nginx = new k8s.helm.v2.Chart("nginx-ingress",
    {
        namespace: namespace.metadata.name,
        chart: "nginx-ingress",
        version: "1.33.5",
        fetchOpts: { repo: "https://charts.helm.sh/stable/" },
        values: {
            controller: {
                replicaCount: 1,
                service: {
                    type: "LoadBalancer",
                },
                publishService: {
                    enabled: true,
                },
            },
        }
    },
    { providers: { kubernetes: provider } },
)
```

{{% /choosable %}}

{{% choosable language python %}}

```python
"""A DigitalOcean Python Pulumi program"""

import pulumi
import pulumi_kubernetes as k8s
import pulumi_digitalocean as do
import pulumi_kubernetes.helm.v3 as helm
from pulumi_kubernetes.core.v1 import Namespace

config = pulumi.Config()
node_count = config.get_float("nodeCount") or 1


# Create a Kubernetes Cluster in DigitalOcean
cluster = do.KubernetesCluster(
    "do-cluster",
    region="sfo2",
    version="1.16",
    node_pool={
        "name": "default",
        "size": "s-1vcpu-2gb",
        "nodeCount": node_count
    }

)

# Use the Kubeconfig output to create a k8s provider
k8s_provider = k8s.Provider("k8s", kubeconfig=cluster.kube_configs[0]["rawConfig"])

# Create a namespace using the previously retrieved kubernetes provider
namespace = Namespace(
    "ns",
    metadata={
        "name": "nginx-ingress"
    }, opts=pulumi.ResourceOptions(provider=k8s_provider))

chart = helm.Chart(
    "nginx-ingress",
    helm.ChartOpts(namespace="nginx-ingress",
    chart="nginx-ingress",
    version="1.33.5",
    fetch_opts=k8s.helm.v3.FetchOpts(
        repo="https://charts.helm.sh/stable/"
    ),
    values={
        "controller": {
            "replicaCount": 1,
            "service": {
                "type": "LoadBalancer"
            },
            "publishService": {
                "enabled": True,
            }
        }
    }), pulumi.ResourceOptions(provider=k8s_provider)
)

```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"fmt"
	"github.com/pulumi/pulumi-digitalocean/sdk/v2/go/digitalocean"
	"github.com/pulumi/pulumi-kubernetes/sdk/v2/go/kubernetes"
	corev1 "github.com/pulumi/pulumi-kubernetes/sdk/v2/go/kubernetes/core/v1"
	"github.com/pulumi/pulumi-kubernetes/sdk/v2/go/kubernetes/helm/v2"
	metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v2/go/kubernetes/meta/v1"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {

		// Create a Kubernetes cluster in DigitalOcean
		cluster, err := digitalocean.NewKubernetesCluster(ctx, "do-cluster", &digitalocean.KubernetesClusterArgs{
			Region:  pulumi.String("sfo2"),
			Version: pulumi.String("1.16"),
			NodePool: &digitalocean.KubernetesClusterNodePoolArgs{
				Name: pulumi.String("default"),
				Size: pulumi.String("s-1vcpu-2gb"),
			},
		})

		if err != nil {
			return fmt.Errorf("Error creating cluster: ", err)
		}

		// Instantiate a Kubernetes provider
		provider, err := kubernetes.NewProvider(ctx, "k8s", &kubernetes.ProviderArgs{
			Kubeconfig: cluster.KubeConfigs.Index(pulumi.Int(0)).RawConfig(),
		})

		if err != nil {
			return fmt.Errorf("Error instantating Kubernetes provider: ", err)
		}

		// Create a namespace
		ns, err := corev1.NewNamespace(ctx, "nginx-ingress", &corev1.NamespaceArgs{
			Metadata: &metav1.ObjectMetaArgs{
				Name: pulumi.String("nginx-ingress"),
			},
		}, pulumi.Provider(provider))

		if err != nil {
			return fmt.Errorf("Error creating Kubernetes namespace: ", err)
		}

		// Deploy nginx-ingress using the helm chart
		_, err = helm.NewChart(ctx, "nginx-ingress", helm.ChartArgs{
			Chart:     pulumi.String("nginx-ingress"),
			Version:   pulumi.String("1.33.5"),
			Namespace: ns.Metadata.Name().Elem(),
			FetchArgs: &helm.FetchArgs{
				Repo: pulumi.String("https://charts.helm.sh/stable/"),
			},
			Values: pulumi.Map{
				"controller": pulumi.Map{
					"replicaCount": pulumi.Int(1),
					"service": pulumi.Map{
						"type": pulumi.String("LoadBalancer"),
					},
					"publishService": pulumi.Map{
						"enabled": pulumi.Bool(true),
					},
				},
			},
		}, pulumi.Provider(provider))

		return nil
	})
}
```

{{% /choosable %}}

{{< /chooser >}}

To achieve this level of interoperability, however, we need to have some dependencies installed locally. These are:

- the Pulumi binary
- the Pulumi language runtime for our chosen language
- the language binary (e.g., node, python, DotNet or Go)
- the languages' dependency management tool (e.g., npm, yarn, PipEnv, etc.)
- the Helm CLI for rendering the Helm chart to a template that Pulumi can then install

This list of requirements is already getting lengthy, and we're only provisioning one piece of infrastructure. Alongside this, if you're using this container in your CI/CD pipeline, you might _also_ need to acquire credentials during the pulumi up process. When you consider that Pulumi's users could be using _any_ of our featured programming languages as well as one or many of our supported cloud providers, you'll begin to imagine how many dependencies are needed.

To provide a seamless experience for our users, our existing [pulumi/pulumi Docker image](https://github.com/pulumi/pulumi/tree/master/docker/pulumi) contains every possible dependency a user might need when provisioning cloud infrastructure. We install everything from the [Helm CLI](https://helm.sh/) to the [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/get-started-with-azure-cli?view=azure-cli-latest) to ensure you can use the container for any Pulumi program. Unfortunately, as we began to support more cloud providers and more languages, the size of the image has grown considerably.

We've received [fantastic feedback from the community](https://github.com/pulumi/pulumi/issues/3789) that while this Docker image meets their needs, providing smaller images is desirable.  Not only do our users want to see images that are smaller in size, but they also want a less opinionated image that provides the flexibility and customization needed to suit the complex workflows people can create with Pulumi.

## Introducing new Language Specific Images

Starting from Pulumi version 2.4.0, we'll be [publishing new, slimmer images in the DockerHub](https://hub.docker.com/u/pulumi) that contain fewer dependencies and are focused on individual specific languages. We've built these images to be usable from day 1, and many of our pioneering users have been using them successfully.
Each image contains everything you need to use Pulumi for your programming language of choice, including the Pulumi CLI, the Pulumi language runtime, and the language binary and dependency manager).

## Reduced Size

Removing many dependencies and only installing a single language SDK means we've seen a dramatic decrease in the uncompressed size of the images:

As you can see below, the uncompressed images are up to six times smaller than the pulumi/pulumi container, which means a much smaller surface area and considerably quicker pull times.

 Image Name | Compressed Size | Uncompressed Size
------------|-----------------|------------------
[pulumi/pulumi:v2.4.0](https://hub.docker.com/layers/pulumi/pulumi/v2.4.0/images/sha256-f17b021acf977809287afbd096f95b35009d8dfc0da90051953acfd58a0447f6?context=explore) | 856.33 MB  | 2.97GB
[pulumi/pulumi-go:2.4.0](https://hub.docker.com/layers/pulumi/pulumi-go/2.4.0/images/sha256-5374f4e78ec0c3bfb2e31aa40de647186a4ed3ec5447503bb99853d4ebf32d99?context=explore) | 208.7MB | 592MB
[pulumi/pulumi-go:2.4.0-ubi](https://hub.docker.com/layers/pulumi/pulumi-go/2.4.0-ubi/images/sha256-e039133008638c3300a1b518383906e6bb832010b3f5f6c30b4386f95169e904?context=explore) | 255.07MB | 701MB
[pulumi/pulumi-nodejs:2.4.0](https://hub.docker.com/layers/pulumi/pulumi-nodejs/2.4.0/images/sha256-e8b2be79dd4f0ed67251265fa3c803d3bb4df220351a23ba6be1226cbca12549?context=explore) | 121MB | 341MB
[pulumi/pulumi-nodejs:2.4.0-ubi](https://hub.docker.com/layers/pulumi/pulumi-nodejs/2.4.0-ubi/images/sha256-1ceca8ba7f48460456d11b525355cc98e42356f60c955aafef244e17bfe176b2?context=explore) | 149.37MB | 439MB
[pulumi/pulumi-dotnet:2.4.0](https://hub.docker.com/layers/pulumi/pulumi-dotnet/2.4.0/images/sha256-fe989abf02b01569f3fa01a4553f271dbbde71a550eb826c1ee19e45efa6ca96?context=explore) | 213.08MB |  598MB
[pulumi/pulumi-dotnet:2.4.0-ubi](https://hub.docker.com/layers/pulumi/pulumi-dotnet/2.4.0-ubi/images/sha256-b8512a747a7fb7a0d94ec30d1dde822264946fced7a46da717ce7e001589b6af?context=explore) | 241.39MB | 677MB
[pulumi/pulumi-python:2.4.0](https://hub.docker.com/layers/pulumi/pulumi-python/2.4.0/images/sha256-831e33017d4d9f49df846b603abe6214ce059b3141c42dfc9d53b447215eccd1?context=explore) | 106.48MB | 308MB
[pulumi/pulumi-python:2.4.0-ubi](https://hub.docker.com/layers/pulumi/pulumi-python/2.4.0-ubi/images/sha256-d4b1ed1a441626687ed6ebed6a509c6e6d60479c3eafe6158268ae8c2e8943a3?context=explore) | 150.18MB | 385MB

## Using the Images

Using the new Pulumi images looks very similar to how you might use the CLI locally. Here's an example of running Pulumi for a typescript project, and the Pulumi SaaS backend:

```bash
docker run -e PULUMI_ACCESS_TOKEN=<PULUMI_ACCESS_TOKEN> -v "$(pwd)":/pulumi/projects pulumi-nodejs:latest /bin/bash -c "npm ci && pulumi preview -s dev"
```

If you're using one of our cloud backends, you'll need to specify your cloud provider credentials and login to your selected backend:

```bash
docker run -e AWS_REGION=<AWS_REGION> -e AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY> -e AWS_SECRET_ACCESS_KEY=<AWS_ACCESS_SECRET_ACCESS_KEY> -v "$(pwd)":/pulumi/projects pulumi/pulumi-nodejs:2.4.0 /bin/bash -c "pulumi login s3://<s3-bucket> && npm ci && pulumi preview -s <stack-name>"
```

Pulumi's intelligent plugin acquisition should find and detect the required resource plugins so you can run your Pulumi program.
If you need additional CLI tools like Helm as part of your workflow, we recommend installing these tools as part of your CI/CD pipeline or using these images as a base image to build your own Docker images. Here's an example of installing Helm in our Go-based Docker image.

```dockerfile
# Build container
FROM debian:latest AS build

RUN apt-get update && apt-get install curl -y && \
    curl -L https://get.helm.sh/helm-v3.2.4-linux-amd64.tar.gz |tar xvz && \
    mv linux-amd64/helm /usr/bin/helm && \
    chmod +x /usr/bin/helm

# Runtime container
FROM pulumi/pulumi-go:latest

COPY --from=build /usr/bin/helm /usr/bin/helm
```

## Multiple Base Images

The default operating system for these new images is [Debian Buster](https://www.debian.org/releases/buster/), but we also publish Images based on [RedHat's Universal Base Image](https://access.redhat.com/articles/4238681). These images are small and lightweight but also benefit from RedHat's exceptional security focus. We scanned these images with [synk.io](https://snyk.io) and found zero vulnerabilities, which should provide peace of mind when running these Pulumi images.

## A Note about Alpine Linux

Many users are fans of [Alpine Linux's](https://alpinelinux.org/) small, lightweight footprint and its Docker focused design; however, we've made the decision not to publish Alpine based images at this moment.
Alpine's usage of [musl libc](https://alpinelinux.org/posts/Alpine-Linux-has-switched-to-musl-libc.html) rather than [glibc](https://www.gnu.org/software/libc/) means that Pulumi doesn't run without adding additional dependencies, which made it hard to justify introducing this extra source of potential bugs into our already broad surface area.
If you're interested in building and maintaining an Alpine based Pulumi image, we have skeleton Docker files available in the [Pulumi GitHub repo](https://github.com/pulumi/pulumi/tree/master/docker).

## Give them a spin!

The new images are available from [DockerHub](https://hub.docker.com/u/pulumi); we'd love for you to give them a try! As always, if you find any issues, don't hesitate to open an [issue](https://github.com/pulumi/pulumi/issues)!

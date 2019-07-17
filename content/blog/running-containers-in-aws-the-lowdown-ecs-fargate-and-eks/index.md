---
title: "Running Containers in AWS, the Lowdown: ECS, Fargate, and EKS"
authors: ["joe-duffy"]
tags: ["AWS","Containers","Kubernetes","EKS"]
date: "2019-06-20"

meta_image: "pulumi-crosswalk-for-aws.webp"
---


Amazon offers multiple solutions for running containers in AWS, through
its managed Elastic Container Service (ECS). This includes three major
approaches: ECS managed automatically with Fargate, ECS backed by EC2
instances, and Elastic Kubernetes Service (EKS), delivering the full
power of Kubernetes. It's not always easy to choose between these, so in
this article we provide some basic guidance on the tradeoffs you'll
encounter when choosing.
<!--more-->

## The Options

At Pulumi, we work with customers to deploy AWS applications all the
time, from early development to scaling production environments
worldwide, using infrastructure as code and often continuous delivery.
During this, we've run across a breadth of container workloads and
requirements, and developed best practices, which this article distills
into some basic advice. As with any advice, the right answer depends on
your scenario's specific requirements.

Here are the three major options, roughly speaking from easiest to
hardest:

## Option 1 - ECS Fargate

[Amazon ECS with Fargate launch type](https://aws.amazon.com/fargate) allows you to deploy and scale
your containerized workloads, automatically, without needing to manage
clusters of EC2 instances by hand. You focus on your Dockerized
applications, with minimal extra declarative metadata about the
requirements of those applications, and not the details of the
underlying compute itself. One could say this is "serverless
containers." Of course, there are servers running your containers,
however the ECS control plane makes informed decisions on your behalf
about when to add capacity, where, and by how much.

To run a workload in ECS, you use a standard Dockerfile to author,
build, and publish your container image, and then run that image inside
your ECS cluster. Tasks and services are authored using ECS definitions,
which specify the container image to run, instance count, and any CPU,
memory, networking, and disk requirements your workload has.

Using Pulumi, these definitions can be easily expressed declaratively in
code, like so:

```typescript
import * as awsx from "@pulumi/awsx";

// Create a load balancer on port 80 and spin up two instances of Nginx.
const lb = new awsx.elasticloadbalancingv2.ApplicationListener("nginx", { port: 80 });
const nginx = new awsx.ecs.FargateService("nginx", {
    taskDefinitionArgs: {
        containers: {
            nginx: {
                image: "nginx",
                memory: 128,
                portMappings: [ lb ],
            },
        },
    },
    desiredCount: 2,
});

// Export the load balancer's address so that it's easy to access.
export const url = lb.endpoint.hostname;
```

This example runs 2 load balanced instances of an NGINX web server using
ECS Fargate.

ECS Fargate is often a great choice when getting started, when you don't
have stringent requirements around cost, and/or if you're a small to
medium sized organization who prefers simpler solutions. Many teams are
successful running it scale too, however Fargate doesn't give you as
much control over persistent storage, privileged containers, custom
scheduling, or special VM types like GPUs or FPGAs. For those, EC2
backed ECS is a better choice.

## Option 2 - ECS Backed by EC2 Instances

[Amazon ECS with EC2 launch type](https://aws.amazon.com/ecs) gives you
similar capabilities to ECS managed by Fargate -- in that you can
deploy containerized workloads, declaratively specify their
requirements, and let ECS do the placement and overall scheduling of
them -- but with full control over the compute environment those
containers run in. That includes control over the precise numbers of
servers, AMIs they are running, and their auto-scaling policies.

To use an EC2 backed cluster, you will need to
[create a cluster and configure the EC2 launch and autoscaling configurations]({{< ref "/docs/reference/crosswalk/aws/ecs#creating-an-auto-scaling-group-for-ecs-cluster-instances" >}}),
and then simply use the awsx.ecs.EC2Service class to create your service
instead. Other than these differences, the resulting code would look
very similar to Option 1 - ECS Fargate above.

For sophisticated AWS organizations who already know how to fine tune
and run compute at scale efficiently and cost effectively, managing your
ECS cluster's EC2 instances explicitly is often a good choice. The good
news is that you can easily start with Fargate, and then over time,
shift to managing the EC2 compute by hand if you prefer. Managing your
cluster amounts to managing fleets of EC2 instances, CloudWatch logging,
and standard AWS services.

## Option 3 - Elastic Kubernetes Service (EKS)

[Amazon Elastic Kubernetes Service (EKS)](https://aws.amazon.com/eks)
offers a very different approach to running containerized workloads than
ECS Fargate or EC2. EKS is a fully managed offering that runs Kubernetes
inside of your AWS account, making it easier to operate Kubernetes, in
addition to integrating with many AWS services like ELB for load
balancing, IAM for cluster authentication, and CloudWatch for logging
and diagnostics. Using EKS, you don't need to explicitly provision,
manage, and upgrade the Kubernetes control plane's configuration,
compute, and storage.

[Kubernetes](https://kubernetes.io) is an open standard for running
containers across a variety of public and private cloud environments.
Most public cloud vendors now offer an EKS-like managed offering,
including [Azure (AKS)]({{< ref "/docs/reference/tutorials/kubernetes/tutorial-aks" >}}),
[Google Cloud (GKE)]({{< ref "/docs/reference/tutorials/kubernetes/tutorial-gke" >}}),
and [Digital Ocean]({{< ref "/docs/reference/pkg/nodejs/pulumi/digitalocean#KubernetesCluster" >}}),
and the availability of on-premises private cloud configurations enables
hybrid cloud for large organizations. Kubernetes in inherently more
complicated to operate than the equivalent ECS solutions mentioned
earlier, because it requires becoming an expert in Kubernetes, which
requires more specialization in its tools and management practices. But
the potential payoff is larger for organizations wanting to go "all in"
on cloud native technologies to facilitate either multi-cloud or hybrid
computing -- challenges most large enterprises are facing today.

In the EKS case, as with ECS, we continue using standard Dockerfiles,
however we use the Kubernetes object model to configure and run
workloads. Instead of task definitions, you use
[Kubernetes objects like Namespaces, Pods, Deployments, and Services](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/).
This full API is available to specify in code using Pulumi, like so:

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

Like the ECS example earlier, this spins up 2 load balanced instances of
the NGINX web server.

You will find that the entirety of Kubernetes is more feature rich and
offers more control over scheduling and scaling your workloads, but with
that richness also comes added complexity that will increase training,
and time to ramp up, in addition to ongoing maintenance costs. To learn
more about Pulumi's support for Kubernetes, [go here]({{< relref "pulumi-a-better-way-to-kubernetes" >}}).

## Private ECR Container Registries

In all of these cases, [Amazon Elastic Container Registry (ECR)]({{< ref "/docs/reference/crosswalk/aws/ecr" >}})
lets you publish
Docker container images to a privately hosted repository inside your AWS
account. The benefit of this is that images are stored within your AWS
account, where access is governed by IAM and, where they are stored
closer to your workloads (maximizing push/pull efficiency). This is an
alternative approach to, say, publishing images to the Docker Hub which
entails a different authentication and pushing and pulling images over
the Internet, where performance can be an issue.

## Next Steps

Pulumi Crosswalk for AWS supports three main options for running
containers in AWS -- ECS Fargate, ECS with EC2 instances, and EKS --
each of which integrates deeply with other AWS services like IAM, ELB,
and CloudWatch. It's possible to use any of these services without
Pulumi, but there are [many benefits to Pulumi's infrastructure as code](https://www.pulumi.com/why-pulumi/).

In short, to get your containers up on AWS, in an easy yet
production-ready way, [get started for free with Pulumi for AWS today]({{< ref "/docs/quickstart/aws" >}})!

After getting started, here are some additional resources to go deeper
on specific topics:

-   [Getting Started with ECS]({{< ref "/docs/reference/crosswalk/aws/ecs" >}})
-   [Getting Started with EKS]({{< ref "/docs/reference/crosswalk/aws/eks" >}})
-   [Getting Started with ECR]({{< ref "/docs/reference/crosswalk/aws/ecr" >}})
    -   [Using ECR from ECS Fargate or EC2]({{< ref "/docs/reference/crosswalk/aws/ecs#building-and-publishing-docker-images-automatically" >}})
    -   [Using ECR from EKS]({{< ref "/docs/reference/crosswalk/aws/eks#using-an-ecr-container-image-from-an-eks-kubernetes-deployment" >}})
    -   [Building and Publishing Docker Images to a Private Amazon ECR Repository]({{< relref "building-and-publishing-docker-images-to-a-private-amazon-ecr-repository" >}})

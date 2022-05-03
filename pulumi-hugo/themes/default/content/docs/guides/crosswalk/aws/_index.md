---
title: "Pulumi Crosswalk for AWS"
meta_desc: Pulumi Crosswalk for AWS supports a simplified approach to defining and deploying cloud infrastructure.
linktitle: Crosswalk for AWS
menu:
  userguides:
    identifier: crosswalk-aws
    weight: 4

aliases: ["/docs/reference/crosswalk/aws/"]
---

<a href="{{< relref "./" >}}">
    <img src="/images/docs/reference/crosswalk/aws/logo.svg" align="right" width="280" style="margin: 0 0 32px 16px;">
</a>

Pulumi Crosswalk for AWS is a collection of libraries that use automatic well-architected best practices to make common infrastructure-as-code tasks in AWS easier and more secure.

<img src="/images/docs/reference/crosswalk/aws/arch.png">

## Overview

Pulumi Crosswalk for AWS supports "day one" tasks, such as creating your initial container-based workloads using
[Amazon Elastic Container Service (ECS)]({{< relref "ecs" >}})---including Fargate or [Kubernetes (EKS)](
{{< relref "eks" >}})---and creating serverless workloads using [Amazon API Gateway]({{< relref "api-gateway" >}}) and [AWS Lambda]({{< relref "lambda" >}}). Secure and cost-conscious defaults are chosen so that simple programs automatically use best practices for the underlying infrastructure, enabling better productivity with confidence.

Pulumi Crosswalk for AWS also supports "day two and beyond" tasks, such as scaling your workload, securing and
integrating it with your existing infrastructure, or going to production in multiple complex environments. This includes [Amazon Virtual Private Cloud (VPC)]({{< relref "vpc" >}}) for network isolation, [AWS Auto Scaling](
{{< relref "autoscaling" >}}) for dynamic scaling, and [AWS Identity and Access Management (IAM)]({{< relref "iam" >}}) for
securing your infrastructure.

For example, this program builds and publishes a Dockerized application to a private [Elastic Container Registry (ECR)](
{{< relref "ecr" >}}), spins up an ECS Fargate cluster, and runs a scalable, load balanced service, all in
response to a single `pulumi up` command line invocation:

{{< chooser language "typescript,python,csharp" / >}}

{{% choosable language typescript %}}

```typescript
import * as awsx from "@pulumi/awsx";
import * as aws from "@pulumi/aws";

// Create a repository.
const repo = new awsx.ecr.Repository("my-repo");

// Build an image from the "./app" directory (relative to our project and containing Dockerfile),
// and publish it to our ECR repository provisioned above.
const image = new awsx.ecr.Image("image", {
    repositoryUrl: repo.url,
    path: "./app",
})

// Create an ECS Cluster
const cluster = new aws.ecs.Cluster("default-cluster");

// Create a load balancer on port 80 and spin up two instances of Nginx.
const lb = new awsx.lb.ApplicationLoadBalancer("nginx-lb");

const service = new awsx.ecs.FargateService("my-service", {
    cluster: cluster.arn,
    taskDefinitionArgs: {
        container: {
            image: image.imageUri,
            cpu: 512,
            memory: 128,
            essential: true,
            portMappings: [
                {
                    containerPort: 80,
                    targetGroup: lb.defaultTargetGroup,
                },
            ],
        },
    },
});

// Export the load balancer's address so that it's easy to access.
export const url = lb.loadBalancer.dnsName;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_aws as aws
import pulumi_awsx as awsx

repo = awsx.ecr.Repository("my-repo");

image = awsx.ecr.Image("image",
                       repository_url=repo.url,
                       path="./app")

cluster = aws.ecs.Cluster("default-cluster")

lb = awsx.lb.ApplicationLoadBalancer("nginx-lb")

service = awsx.ecs.FargateService("service",
                                  cluster=cluster.arn,
                                  task_definition_args=awsx.ecs.FargateServiceTaskDefinitionArgs(
                                      containers={
                                          "nginx": awsx.ecs.TaskDefinitionContainerDefinitionArgs(
                                              image=image.image_uri,
                                              memory=128,
                                              port_mappings=[awsx.ecs.TaskDefinitionPortMappingArgs(
                                                  container_port=80,
                                                  target_group=lb.default_target_group,
                                              )]
                                          )
                                      }
                                  ))

pulumi.export("url", lb.load_balancer.dns_name)
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using System.Threading.Tasks;
using Pulumi;
using Pulumi.Awsx.Ecs.Inputs;
using Aws = Pulumi.Aws;
using Ecr = Pulumi.Awsx.Ecr;
using Ecs = Pulumi.Awsx.Ecs;
using Lb = Pulumi.Awsx.Lb;

class MyStack : Stack
{
    public MyStack()
    {
        var repo = new Ecr.Repository("my-repo");

        var image = new Ecr.Image("image", new Ecr.ImageArgs
        {
            RepositoryUrl = repo.Url,
            Path = "./app",
        });

        var cluster = new Aws.Ecs.Cluster("demo-cluster");

        var lb = new Lb.ApplicationLoadBalancer("nginx-lb");

        var service = new Ecs.FargateService("my-service", new Ecs.FargateServiceArgs
        {
            Cluster = cluster.Arn,
            TaskDefinitionArgs = new FargateServiceTaskDefinitionArgs
            {
                Container = new TaskDefinitionContainerDefinitionArgs
                {
                    Memory = 128,
                    Cpu = 512,
                    Image = image.ImageUri,
                    Essential = true,
                    PortMappings = new TaskDefinitionPortMappingArgs
                    {
                        ContainerPort = 80,
                        TargetGroup = lb.DefaultTargetGroup,
                    }
                }
            }
        });
    }
}

class Program
{
    static Task<int> Main(string[] args) => Deployment.RunAsync<MyStack>();
}
```

{{% /choosable %}}

This example uses the default VPC and reasonable security defaults, but supports easy customization of all aspects.

## Getting Started

To get started with Pulumi Crosswalk for AWS, [download and install Pulumi]({{< relref "/docs/get-started/install" >}}), and [configure it to work with your AWS account]({{< relref "/registry/packages/aws/installation-configuration" >}}). Afterwards,
[try the Getting Started tutorial]({{< relref "/registry/packages/aws/how-to-guides/ecs-fargate" >}}) or select one of the
relevant User Guides to get started:

### Containers

* [Elastic Container Service (ECS)]({{< relref "ecs" >}})
* [Elastic Kubernetes Service (EKS)]({{< relref "eks" >}})
* [Elastic Container Registry (ECR)]({{< relref "ecr" >}})

### Serverless

* [Lambda]({{< relref "lambda" >}})
* [API Gateway]({{< relref "api-gateway" >}})

### Monitoring

* [CloudWatch]({{< relref "cloudwatch" >}})

### Core Infrastructure

* [Auto Scaling]({{< relref "autoscaling" >}})
* [Elastic Load Balancing (ELB)]({{< relref "elb" >}})
* [Identity and Access Management (IAM)]({{< relref "iam" >}})
* [Virtual Private Cloud (VPC)]({{< relref "vpc" >}})

### Continuous Deployment

* [Using Pulumi from AWS Code Services]({{< relref "/docs/guides/continuous-delivery/aws-code-services" >}})

### Other AWS Services

Pulumi supports the entirety of the AWS platform. If your favorite service isn't listed above, check out:

* [AWS Index of Services]({{< relref "aws-index-of-services" >}})

## Frequently Asked Questions (FAQ)

### What Clouds Does Pulumi Crosswalk Support?

Pulumi Crosswalk supports AWS only at the moment. Support for additional clouds is on the roadmap
([Azure](https://github.com/pulumi/pulumi-azure/issues/277), [GCP](https://github.com/pulumi/pulumi-gcp/issues/165),
and [Kubernetes](https://github.com/pulumi/pulumi-kubernetes/issues/589)).

### What Languages are Supported?

Pulumi Crosswalk for AWS is available for all supported Pulumi languages.

### What Packages Define Pulumi Crosswalk for AWS?

Because Pulumi Crosswalk for AWS is a broader "brand" for our framework spanning multiple packages, there isn't
a single package that contains everything. The [`@pulumi/aws`]({{< relref "/registry/packages/aws/api-docs" >}}),
[`@pulumi/awsx`]({{< relref "/docs/reference/pkg/nodejs/pulumi/awsx" >}}), and
[`@pulumi/eks`]({{< relref "/docs/reference/pkg/nodejs/pulumi/eks" >}}) packages each has an important role to play.

### Is Pulumi Crosswalk for AWS Free to Use?

Yes, Pulumi Crosswalk for AWS is completely open source and free to use, along with the Individual Edition of Pulumi.
[Pulumi's commercial offerings]({{< relref "/pricing" >}}) already fully support Pulumi Crosswalk for AWS.

If you would like to contribute to the packages, please see the relevant repo on GitHub: [`pulumi/pulumi-aws`](
https://github.com/pulumi/pulumi-aws), [`pulumi/pulumi-awsx`](https://github.com/pulumi/pulumi-awsx), or
[`pulumi/eks`](https://github.com/pulumi/pulumi-eks). Issues and Pull Requests are welcome!

### If I'm an Existing User, What Has Changed?

The primary change is new functionality added to the above packages, and the availability of these User Guides.
Pulumi Crosswalk for AWS continues to work with the standard Pulumi CLI and Pulumi Service. If you already use the free Individual
Edition, or paid Team or Enterprise Edition, you can continue to do so now with Pulumi Crosswalk for AWS functionality.

### Upgrading from an old version of Pulumi Crosswalk for AWS?

Previous versions of `@pulumi/awsx` were TypeScript-only. The functionality has changed from these TypeScript-only versions.
We have taken the opportunity to move the existing TypeScript-only functionality into a `classic` namespace. To create a
VPC using the old TypeScript version of Crosswalk for AWS, the following code would work:

```typescript
import * as awsx from "@pulumi/awsx/classic";

const vpc = new awsx.ec2.Vpc("classic-vpc", {});
```

Any resource that you use from the existing library can continue to be used from that `classic` namespace. All of the classic
functionality is available in that namesoace.

### Is Support or Training Available for Pulumi Crosswalk for AWS?

Yes! Please fill out [this form]({{< relref "/contact.md" >}}) and a Pulumi team member will be in touch.

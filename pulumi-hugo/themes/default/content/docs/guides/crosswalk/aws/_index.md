---
title: "Crosswalk for AWS Guides"
meta_desc: Pulumi Crosswalk for AWS supports a simplified approach to defining and deploying cloud infrastructure.
linktitle: Crosswalk for AWS
menu:
  userguides:
    identifier: crosswalk-aws
    weight: 4

aliases: ["/docs/reference/crosswalk/aws/"]
---
<a href="./">
    <img src="/images/docs/reference/crosswalk/aws/logo.svg" align="right" width="280" style="margin: 0 0 32px 16px;">
</a>

Pulumi Crosswalk for AWS is a collection of libraries that use automatic well-architected best practices to make common infrastructure-as-code tasks in AWS easier and more secure.

<img src="/images/docs/reference/crosswalk/aws/arch.png">

## Overview

Pulumi Crosswalk for AWS supports "day one" tasks, such as creating your initial container-based workloads using
[Amazon Elastic Container Service (ECS)](/docs/guides/crosswalk/aws/ecs)---including Fargate or [Kubernetes (EKS)](
eks)---and creating serverless workloads using [Amazon API Gateway](/docs/guides/crosswalk/aws/api-gateway/) and [AWS Lambda](/docs/guides/crosswalk/aws/lambda/). Secure and cost-conscious defaults are chosen so that simple programs automatically use best practices for the underlying infrastructure, enabling better productivity with confidence.

Pulumi Crosswalk for AWS also supports "day two and beyond" tasks, such as scaling your workload, securing and
integrating it with your existing infrastructure, or going to production in multiple complex environments. This includes [Amazon Virtual Private Cloud (VPC)](/docs/guides/crosswalk/aws/vpc) for network isolation, [AWS Auto Scaling](
autoscaling) for dynamic scaling, and [AWS Identity and Access Management (IAM)](/docs/guides/crosswalk/aws/iam) for
securing your infrastructure.

For example, this program builds and publishes a Dockerized application to a private [Elastic Container Registry (ECR)](
ecr), spins up an ECS Fargate cluster, and runs a scalable, load balanced service, all in
response to a single `pulumi up` command line invocation:

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language "javascript,typescript" %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import * as awsx from "@pulumi/awsx";

const repository = new awsx.ecr.Repository("repository", {});
const image = new awsx.ecr.Image("image", {
    repositoryUrl: repository.url,
    path: "./app",
});
const cluster = new aws.ecs.Cluster("cluster", {});
const lb = new awsx.lb.ApplicationLoadBalancer("lb", {});
const service = new awsx.ecs.FargateService("service", {
    cluster: cluster.arn,
    assignPublicIp: true,
    taskDefinitionArgs: {
        container: {
            image: image.imageUri,
            cpu: 512,
            memory: 128,
            essential: true,
            portMappings: [{
                targetGroup: lb.defaultTargetGroup,
            }],
        },
    },
});
export const url = lb.loadBalancer.dnsName;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_aws as aws
import pulumi_awsx as awsx

repository = awsx.ecr.Repository("repository")
image = awsx.ecr.Image("image",
    repository_url=repository.url,
    path="./app")
cluster = aws.ecs.Cluster("cluster")
lb = awsx.lb.ApplicationLoadBalancer("lb")
service = awsx.ecs.FargateService("service",
    cluster=cluster.arn,
    assign_public_ip=True,
    task_definition_args=awsx.ecs.FargateServiceTaskDefinitionArgs(
        container=awsx.ecs.TaskDefinitionContainerDefinitionArgs(
            image=image.image_uri,
            cpu=512,
            memory=128,
            essential=True,
            port_mappings=[awsx.ecs.TaskDefinitionPortMappingArgs(
                target_group=lb.default_target_group,
            )],
        ),
    ))
pulumi.export("url", lb.load_balancer.dns_name)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v5/go/aws/ecs"
	"github.com/pulumi/pulumi-aws/sdk/v5/go/aws/lb"
	"github.com/pulumi/pulumi-awsx/sdk/go/awsx/ecr"
	"github.com/pulumi/pulumi-awsx/sdk/go/awsx/ecs"
	"github.com/pulumi/pulumi-awsx/sdk/go/awsx/lb"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
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
		cluster, err := ecs.NewCluster(ctx, "cluster", nil)
		if err != nil {
			return err
		}
		lb, err := lb.NewApplicationLoadBalancer(ctx, "lb", nil)
		if err != nil {
			return err
		}
		_, err = ecs.NewFargateService(ctx, "service", &ecs.FargateServiceArgs{
			Cluster:        cluster.Arn,
			AssignPublicIp: pulumi.Bool(true),
			TaskDefinitionArgs: &ecs.FargateServiceTaskDefinitionArgs{
				Container: &ecs.TaskDefinitionContainerDefinitionArgs{
					Image:     image.ImageUri,
					Cpu:       pulumi.Int(512),
					Memory:    pulumi.Int(128),
					Essential: pulumi.Bool(true),
					PortMappings: []ecs.TaskDefinitionPortMappingArgs{
						&ecs.TaskDefinitionPortMappingArgs{
							TargetGroup: lb.DefaultTargetGroup,
						},
					},
				},
			},
		})
		if err != nil {
			return err
		}
		ctx.Export("url", lb.LoadBalancer.ApplyT(func(loadBalancer *lb.LoadBalancer) (string, error) {
			return loadBalancer.DnsName, nil
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
using Aws = Pulumi.Aws;
using Awsx = Pulumi.Awsx;

return await Deployment.RunAsync(() =>
{
    var repository = new Awsx.Ecr.Repository("repository");

    var image = new Awsx.Ecr.Image("image", new()
    {
        RepositoryUrl = repository.Url,
        Path = "./app",
    });

    var cluster = new Aws.Ecs.Cluster("cluster");

    var lb = new Awsx.Lb.ApplicationLoadBalancer("lb");

    var service = new Awsx.Ecs.FargateService("service", new()
    {
        Cluster = cluster.Arn,
        AssignPublicIp = true,
        TaskDefinitionArgs = new Awsx.Ecs.Inputs.FargateServiceTaskDefinitionArgs
        {
            Container = new Awsx.Ecs.Inputs.TaskDefinitionContainerDefinitionArgs
            {
                Image = image.ImageUri,
                Cpu = 512,
                Memory = 128,
                Essential = true,
                PortMappings = new[]
                {
                    new Awsx.Ecs.Inputs.TaskDefinitionPortMappingArgs
                    {
                        TargetGroup = lb.DefaultTargetGroup,
                    },
                },
            },
        },
    });

    return new Dictionary<string, object?>
    {
        ["url"] = lb.LoadBalancer.Apply(loadBalancer => loadBalancer.DnsName),
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
import com.pulumi.awsx.ecr.Repository;
import com.pulumi.awsx.ecr.Image;
import com.pulumi.awsx.ecr.ImageArgs;
import com.pulumi.aws.ecs.Cluster;
import com.pulumi.awsx.lb.ApplicationLoadBalancer;
import com.pulumi.awsx.ecs.FargateService;
import com.pulumi.awsx.ecs.FargateServiceArgs;
import com.pulumi.awsx.ecs.inputs.FargateServiceTaskDefinitionArgs;
import com.pulumi.awsx.ecs.inputs.TaskDefinitionContainerDefinitionArgs;
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
        var repository = new Repository("repository");

        var image = new Image("image", ImageArgs.builder()
            .repositoryUrl(repository.url())
            .path("./app")
            .build());

        var cluster = new Cluster("cluster");

        var lb = new ApplicationLoadBalancer("lb");

        var service = new FargateService("service", FargateServiceArgs.builder()
            .cluster(cluster.arn())
            .assignPublicIp(true)
            .taskDefinitionArgs(FargateServiceTaskDefinitionArgs.builder()
                .container(TaskDefinitionContainerDefinitionArgs.builder()
                    .image(image.imageUri())
                    .cpu(512)
                    .memory(128)
                    .essential(true)
                    .portMappings(TaskDefinitionPortMappingArgs.builder()
                        .targetGroup(lb.defaultTargetGroup())
                        .build())
                    .build())
                .build())
            .build());

        ctx.export("url", lb.loadBalancer().applyValue(loadBalancer -> loadBalancer.dnsName()));
    }
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
name: scratch-yaml
description: A Pulumi YAML program to deploy a serverless application on AWS
runtime: yaml
resources:
  repository:
    type: awsx:ecr:Repository
  image:
    type: awsx:ecr:Image
    properties:
      repositoryUrl: ${repository.url}
      path: "./app"
  cluster:
    type: aws:ecs:Cluster
  lb:
    type: awsx:lb:ApplicationLoadBalancer
  service:
    type: awsx:ecs:FargateService
    properties:
      cluster: ${cluster.arn}
      assignPublicIp: true
      taskDefinitionArgs:
        container:
          image: ${image.imageUri}
          cpu: 512
          memory: 128
          essential: true
          portMappings:
            - targetGroup: ${lb.defaultTargetGroup}
outputs:
  url: ${lb.loadBalancer.dnsName}
```

{{% /choosable %}}

This example uses the default VPC and reasonable security defaults, but supports easy customization of all aspects.

## Code Example Deep Dive

Watch this video to dive into an Amazon ECS and Fargate code example that conceptually illustrates the benefits of using Crosswalk libraries versus authoring code from scratch with the [AWS classic provider](/registry/packages/aws/).

{{< youtube "gi9ZoZwzHAM?rel=0" >}}

## Getting Started

To get started with Pulumi Crosswalk for AWS, [download and install Pulumi](/docs/get-started/install/), and [configure it to work with your AWS account](/registry/packages/aws/installation-configuration/). Afterwards,
[try the Getting Started tutorial](/registry/packages/aws/how-to-guides/ecs-fargate/) or select one of the
relevant User Guides to get started:

### Containers

* [Elastic Container Service (ECS)](ecs)
* [Elastic Kubernetes Service (EKS)](eks)
* [Elastic Container Registry (ECR)](ecr)

### Serverless

* [Lambda](lambda/)
* [API Gateway](api-gateway/)

### Monitoring

* [CloudWatch](cloudwatch/)

### Core Infrastructure

* [Auto Scaling](autoscaling/)
* [Elastic Load Balancing (ELB)](elb)
* [Identity and Access Management (IAM)](iam)
* [Virtual Private Cloud (VPC)](vpc)

### Continuous Deployment

* [Using Pulumi from AWS Code Services](/docs/guides/continuous-delivery/aws-code-services/)

### Other AWS Services

Pulumi supports the entirety of the AWS platform. If your favorite service isn't listed above, check out:

* [AWS Index of Services](aws-index-of-services/)

## Frequently Asked Questions (FAQ)

### What Clouds Does Pulumi Crosswalk Support?

Pulumi Crosswalk supports AWS only at the moment. Support for additional clouds is on the roadmap
([Azure](https://github.com/pulumi/pulumi-azure/issues/277), [GCP](https://github.com/pulumi/pulumi-gcp/issues/165),
and [Kubernetes](https://github.com/pulumi/pulumi-kubernetes/issues/589)).

### What Languages are Supported?

Pulumi Crosswalk for AWS is available for all supported Pulumi languages.

### What Packages Define Pulumi Crosswalk for AWS?

Because Pulumi Crosswalk for AWS is a broader "brand" for our framework spanning multiple packages, there isn't
a single package that contains everything. The [`@pulumi/aws`](/registry/packages/aws/api-docs),
[`@pulumi/awsx`](/registry/packages/awsx/api-docs/), [`@pulumi/aws-apigateway`](/registry/packages/aws-apigateway/api-docs/) and
[`@pulumi/eks`](/registry/packages/eks/api-docs/) packages each has an important role to play.

### Is Pulumi Crosswalk for AWS Free to Use?

Yes, Pulumi Crosswalk for AWS is completely open source and free to use, along with the Individual Edition of Pulumi.
[Pulumi's commercial offerings](/pricing) already fully support Pulumi Crosswalk for AWS.

If you would like to contribute to the packages, please see the relevant repo on GitHub: [`pulumi/pulumi-aws`](
https://github.com/pulumi/pulumi-aws), [`pulumi/pulumi-awsx`](https://github.com/pulumi/pulumi-awsx) [`pulumi/pulumi-aws-apigateway`](https://github.com/pulumi/pulumi-aws-apigateway/), or
[`pulumi/eks`](https://github.com/pulumi/pulumi-eks). Issues and Pull Requests are welcome!

### If I'm an Existing User, What Has Changed?

The primary change is new functionality added to the above packages, and the availability of these User Guides.
Pulumi Crosswalk for AWS continues to work with the standard Pulumi CLI and Pulumi Cloud. If you already use the free Individual
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

Yes! Please fill out [this form](/contact/) and a Pulumi team member will be in touch.

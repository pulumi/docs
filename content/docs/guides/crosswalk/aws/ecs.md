---
title_tag: "Using AWS Elastic Container Service (ECS) | Crosswalk"
title: Using AWS Elastic Container Service (ECS)
meta_desc: Pulumi Crosswalk for AWS ECS simplifies deploying containerized applications into ECS and managing all of the
            associated resources.
linktitle: Elastic Container Service (ECS)
menu:
  userguides:
    parent: crosswalk-aws
    weight: 5

aliases: ["/docs/reference/crosswalk/aws/ecs/"]
---

<a href="./">
    <img src="/images/docs/reference/crosswalk/aws/logo.svg" align="right" width="280" style="margin: 0 0 32px 16px;">
</a>

[Amazon Elastic Container Service (Amazon ECS)](https://aws.amazon.com/ecs) is a scalable, high-performance container
orchestration service that supports Docker containers and allows you to easily run and scale containerized applications
on AWS. ECS eliminates the need for you to install and operate your own container orchestration software, manage and
scale a cluster of virtual machines, or schedule containers on those virtual machines.

## Overview

Pulumi Crosswalk for AWS ECS simplifies deploying containerized applications into ECS and managing all of the
associated resources. This includes simple support for load-balanced container services and one-off tasks, in addition
to managing the clusters and associated scaling, network, and security policies. This includes ECS Fargate---the
simplest option, alleviating the need to manage the cluster's servers themselves---in addition to ECS classic---
providing full control over the underlying EC2 machine resources that power your cluster.

> An alternative to ECS is Amazon's Elastic Kubernetes Service (EKS). Similar to ECS, EKS lets you operate
> containerized applications in a cluster. EKS tends to be more complex to provision and manage, but has
> the added advantage of using the industry standard container orchestrator, Kubernetes, and therefore can help
> with portability between clouds and self-hosted configurations. See
> [Pulumi Crosswalk for AWS EKS](/docs/guides/crosswalk/aws/eks/) for more information about using EKS.

## Creating a Load Balanced ECS Service

To run a Docker container in ECS using default network and cluster settings, use the `awsx.ecs.FargateService`
class. Since we need to access this container over port 80 using a stable address, we will use a load balancer.

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language "javascript,typescript" %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import * as awsx from "@pulumi/awsx";

const cluster = new aws.ecs.Cluster("cluster", {});
const lb = new awsx.lb.ApplicationLoadBalancer("lb", {});
const service = new awsx.ecs.FargateService("service", {
    cluster: cluster.arn,
    assignPublicIp: true,
    desiredCount: 2,
    taskDefinitionArgs: {
        container: {
            image: "nginx:latest",
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

cluster = aws.ecs.Cluster("cluster")
lb = awsx.lb.ApplicationLoadBalancer("lb")
service = awsx.ecs.FargateService("service",
    cluster=cluster.arn,
    assign_public_ip=True,
    desired_count=2,
    task_definition_args=awsx.ecs.FargateServiceTaskDefinitionArgs(
        container=awsx.ecs.TaskDefinitionContainerDefinitionArgs(
            image="nginx:latest",
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
	"github.com/pulumi/pulumi-awsx/sdk/go/awsx/ecs"
	"github.com/pulumi/pulumi-awsx/sdk/go/awsx/lb"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
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
			DesiredCount:   pulumi.Int(2),
			TaskDefinitionArgs: &ecs.FargateServiceTaskDefinitionArgs{
				Container: &ecs.TaskDefinitionContainerDefinitionArgs{
					Image:     pulumi.String("nginx:latest"),
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
    var cluster = new Aws.Ecs.Cluster("cluster");

    var lb = new Awsx.Lb.ApplicationLoadBalancer("lb");

    var service = new Awsx.Ecs.FargateService("service", new()
    {
        Cluster = cluster.Arn,
        AssignPublicIp = true,
        DesiredCount = 2,
        TaskDefinitionArgs = new Awsx.Ecs.Inputs.FargateServiceTaskDefinitionArgs
        {
            Container = new Awsx.Ecs.Inputs.TaskDefinitionContainerDefinitionArgs
            {
                Image = "nginx:latest",
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
        var cluster = new Cluster("cluster");

        var lb = new ApplicationLoadBalancer("lb");

        var service = new FargateService("service", FargateServiceArgs.builder()
            .cluster(cluster.arn())
            .assignPublicIp(true)
            .desiredCount(2)
            .taskDefinitionArgs(FargateServiceTaskDefinitionArgs.builder()
                .container(TaskDefinitionContainerDefinitionArgs.builder()
                    .image("nginx:latest")
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
resources:
  cluster:
    type: aws:ecs:Cluster
  lb:
    type: awsx:lb:ApplicationLoadBalancer
  service:
    type: awsx:ecs:FargateService
    properties:
      cluster: ${cluster.arn}
      assignPublicIp: true
      desiredCount: 2
      taskDefinitionArgs:
        container:
          image: nginx:latest
          cpu: 512
          memory: 128
          essential: true
          portMappings:
            - targetGroup: ${lb.defaultTargetGroup}
outputs:
  url: ${lb.loadBalancer.dnsName}
```

{{% /choosable %}}

After deploying this program, `pulumi stack output url` can be used to access the Url output property. We can then access our  NGINX web server behind our load balancer via curl:

```bash
curl http://$(pulumi stack output url)
```

Giving the following output:

```bash
<!DOCTYPE html>
<html>
<body>
<h1>Welcome to nginx!</h1>
</body>
</html>
```

We have chosen to create an [Elastic Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing) so that we
can access our services over the Internet at a stable address, spread evenly across two instances. Any of the ELB
options described in the [Pulumi Crosswalk for ELB documentation](/docs/guides/crosswalk/aws/elb/) can be used with our ECS service.

Behind the scenes, our program creates the ECS cluster in the default VPC to run the compute. This is something
[we can configure](/docs/guides/crosswalk/aws/eks#configuring-your-eks-clusters-networking) if we want to use a different VPC.

Because we've used [`Fargate`](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html), we don't
need to specify anything about our machine instances. Instead, Fargate will manage that for us automatically based on
the optional `memory` and `cpu` values we request for our containers.

For many scenarios, this is exactly what we want: a simple way of just running containerized applications. While this
approach is simple and hides a lot of complexity, it's often desirable to control more of what is going on.

## Creating an ECS Cluster in a VPC

To create an ECS service inside of a VPC, we will first create or use an existing VPC using any of the techniques
described in [Pulumi Crosswalk for AWS VPC](/docs/guides/crosswalk/aws/vpc/). Then we pass the subnets
from that VPC into the network configuration argument for our cluster:

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language "javascript,typescript" %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import * as awsx from "@pulumi/awsx";

const vpc = new awsx.ec2.Vpc("vpc", {});
const securityGroup = new aws.ec2.SecurityGroup("securityGroup", {
    vpcId: vpc.vpcId,
    egress: [{
        fromPort: 0,
        toPort: 0,
        protocol: "-1",
        cidrBlocks: ["0.0.0.0/0"],
        ipv6CidrBlocks: ["::/0"],
    }],
});
const cluster = new aws.ecs.Cluster("cluster", {});
const service = new awsx.ecs.FargateService("service", {
    cluster: cluster.arn,
    networkConfiguration: {
        subnets: vpc.privateSubnetIds,
        securityGroups: [securityGroup.id],
    },
    desiredCount: 2,
    taskDefinitionArgs: {
        container: {
            image: "nginx:latest",
            cpu: 512,
            memory: 128,
            essential: true,
        },
    },
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_aws as aws
import pulumi_awsx as awsx

vpc = awsx.ec2.Vpc("vpc")
security_group = aws.ec2.SecurityGroup("securityGroup",
    vpc_id=vpc.vpc_id,
    egress=[aws.ec2.SecurityGroupEgressArgs(
        from_port=0,
        to_port=0,
        protocol="-1",
        cidr_blocks=["0.0.0.0/0"],
        ipv6_cidr_blocks=["::/0"],
    )])
cluster = aws.ecs.Cluster("cluster")
service = awsx.ecs.FargateService("service",
    cluster=cluster.arn,
    network_configuration=aws.ecs.ServiceNetworkConfigurationArgs(
        subnets=vpc.private_subnet_ids,
        security_groups=[security_group.id]
    ),
    desired_count=2,
    task_definition_args=awsx.ecs.FargateServiceTaskDefinitionArgs(
        container=awsx.ecs.TaskDefinitionContainerDefinitionArgs(
            image="nginx:latest",
            cpu=512,
            memory=128,
            essential=True,
        ),
    ))
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v5/go/aws/ec2"
	"github.com/pulumi/pulumi-aws/sdk/v5/go/aws/ecs"
	"github.com/pulumi/pulumi-awsx/sdk/go/awsx/ec2"
	"github.com/pulumi/pulumi-awsx/sdk/go/awsx/ecs"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		vpc, err := ec2.NewVpc(ctx, "vpc", nil)
		if err != nil {
			return err
		}
		securityGroup, err := ec2.NewSecurityGroup(ctx, "securityGroup", &ec2.SecurityGroupArgs{
			VpcId: vpc.VpcId,
			Egress: ec2.SecurityGroupEgressArray{
				&ec2.SecurityGroupEgressArgs{
					FromPort: pulumi.Int(0),
					ToPort:   pulumi.Int(0),
					Protocol: pulumi.String("-1"),
					CidrBlocks: pulumi.StringArray{
						pulumi.String("0.0.0.0/0"),
					},
					Ipv6CidrBlocks: pulumi.StringArray{
						pulumi.String("::/0"),
					},
				},
			},
		})
		if err != nil {
			return err
		}
		cluster, err := ecs.NewCluster(ctx, "cluster", nil)
		if err != nil {
			return err
		}
		_, err = ecs.NewFargateService(ctx, "service", &ecs.FargateServiceArgs{
			Cluster: cluster.Arn,
			NetworkConfiguration: &ecs.ServiceNetworkConfigurationArgs{
				Subnets: vpc.PrivateSubnetIds,
				SecurityGroups: pulumi.StringArray{
					securityGroup.ID(),
				},
			},
			DesiredCount: pulumi.Int(2),
			TaskDefinitionArgs: &ecs.FargateServiceTaskDefinitionArgs{
				Container: &ecs.TaskDefinitionContainerDefinitionArgs{
					Image:     pulumi.String("nginx:latest"),
					Cpu:       pulumi.Int(512),
					Memory:    pulumi.Int(128),
					Essential: pulumi.Bool(true),
				},
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
using Pulumi;
using Aws = Pulumi.Aws;
using Awsx = Pulumi.Awsx;

return await Deployment.RunAsync(() =>
{
    var vpc = new Awsx.Ec2.Vpc("vpc");

    var securityGroup = new Aws.Ec2.SecurityGroup("securityGroup", new()
    {
        VpcId = vpc.VpcId,
        Egress = new[]
        {
            new Aws.Ec2.Inputs.SecurityGroupEgressArgs
            {
                FromPort = 0,
                ToPort = 0,
                Protocol = "-1",
                CidrBlocks = new[]
                {
                    "0.0.0.0/0",
                },
                Ipv6CidrBlocks = new[]
                {
                    "::/0",
                },
            },
        },
    });

    var cluster = new Aws.Ecs.Cluster("cluster");

    var service = new Awsx.Ecs.FargateService("service", new()
    {
        Cluster = cluster.Arn,
        NetworkConfiguration = new Aws.Ecs.Inputs.ServiceNetworkConfigurationArgs
        {
            Subnets = vpc.PrivateSubnetIds,
            SecurityGroups = new[]
            {
                securityGroup.Id,
            },
        },
        DesiredCount = 2,
        TaskDefinitionArgs = new Awsx.Ecs.Inputs.FargateServiceTaskDefinitionArgs
        {
            Container = new Awsx.Ecs.Inputs.TaskDefinitionContainerDefinitionArgs
            {
                Image = "nginx:latest",
                Cpu = 512,
                Memory = 128,
                Essential = true,
            },
        },
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
        var cluster = new Cluster("cluster");

        var lb = new ApplicationLoadBalancer("lb");

        var service = new FargateService("service", FargateServiceArgs.builder()
            .cluster(cluster.arn())
            .assignPublicIp(true)
            .desiredCount(2)
            .taskDefinitionArgs(FargateServiceTaskDefinitionArgs.builder()
                .container(TaskDefinitionContainerDefinitionArgs.builder()
                    .image("nginx:latest")
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
resources:
  vpc:
    type: awsx:ec2:Vpc
  securityGroup:
    type: aws:ec2:SecurityGroup
    properties:
      vpcId: ${vpc.vpcId}
      egress:
        - fromPort: 0
          toPort: 0
          protocol: -1
          cidrBlocks:
            - 0.0.0.0/0
          ipv6CidrBlocks:
            - "::/0"
  cluster:
    type: aws:ecs:Cluster
  service:
    type: awsx:ecs:FargateService
    properties:
      cluster: ${cluster.arn}
      networkConfiguration:
        subnets: ${vpc.privateSubnetIds}
        securityGroups:
          - ${securityGroup.id}
      desiredCount: 2
      taskDefinitionArgs:
        container:
          image: nginx:latest
          cpu: 512
          memory: 128
          essential: true
```

{{% /choosable %}}

When using a custom VPC, you will also need to specify your own security groups if you need to allow ingress or egress.

## ECS Tasks, Containers, and Services

We saw example uses above but didn't describe the details of how ECS core concepts work, or are authored in your
application.

To deploy your application to ECS, it must be containerized. This means authoring a `Dockerfile` that specifies
how all of your application's runtime dependencies are built and packaged up. This is then used to create an image
that is used by the ECS runtime to mount and run your code, as services scale out. For more information about container
technology, see [Docker Basics for Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/docker-basics.html).

Given an image, ECS requires that you author a [Task Definition](
https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definitions.html), which specifies what requirements
your Docker application has of the underlying cluster. This includes information about the container(s) to run.
After that, ECS containers may be run as one-off [Tasks](
https://docs.aws.amazon.com/AmazonECS/latest/developerguide/scheduling_tasks.html), or long-lived [Services](
https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html).

For full details of the available component arguments, please refer to the registry API documentation.

## Building and Publishing Docker Images Automatically

Containers with Pulumi Crosswalk for AWS ECS are far more flexible than just accepting a preexisting image URL,
and can even refer to a `Dockerfile` on disk so you do not need to build and publish
it separately ahead of time. This makes it very easy to use private registrations for your ECS workloads.

For example, specifying a `path` will run a `docker build` in that path, push the result up to the ECR repository that specified in the first argument, and then pass
the private ECR repository path to the container:
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

For more information about using ECR, refer to [Pulumi Crosswalk for AWS ECR](/docs/guides/crosswalk/aws/ecr/).

## Additional ECS Resources

* [Amazon Elastic Container Service](https://aws.amazon.com/ecs/)

---
title_tag: "Using AWS Elastic Container Registry (ECR) | Crosswalk"
title: Using AWS Elastic Container Registry (ECR)
meta_desc: Pulumi Crosswalk for AWS ECR makes the provisioning of new ECR repositories as simple as one line of code.
linktitle: Elastic Container Registry (ECR)
menu:
  userguides:
    parent: crosswalk-aws
    weight: 4

aliases: ["/docs/reference/crosswalk/aws/ecr/"]
---

<a href="./">
    <img src="/images/docs/reference/crosswalk/aws/logo.svg" align="right" width="280" style="margin: 0 0 32px 16px;">
</a>

[Amazon Elastic Container Registry (ECR)](https://aws.amazon.com/ecr/) is a managed Docker container registry that
makes it easy to store, manage, and deploy Docker container images. ECR supports private Docker registries with
resource-based permissions using AWS IAM, so specific users and instances can access images. Using ECR simplifies
going from development to production, and eliminates the need to operate your own container repositories or worry
about scaling the underlying infrastructure, while hosting your images in a highly available and scalable architecture.

## Overview

Pulumi Crosswalk for AWS ECR makes the provisioning of new ECR repositories as simple as one line of code,
integrates with Pulumi Crosswalk for AWS [ECS](/docs/guides/crosswalk/aws/ecs/) and [EKS](/docs/guides/crosswalk/aws/eks/) to ease
deployment of new application containers to your ECS, "Fargate", and/or Kubernetes clusters, and even supports
building and deploying Docker images from your developer desktop or CI/CD workflows.

## Provisioning an ECR Repository

Each AWS account automatically has an ECR [_registry_](https://docs.aws.amazon.com/AmazonECR/latest/userguide/Registries.html),
and within each registry, you can create any number of [_repositories_](
https://docs.aws.amazon.com/AmazonECR/latest/userguide/Repositories.html) to actually contain your Docker images.

To create a new ECR repository, allocate an instance of the `awsx.ecr.Repository` class:

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language "javascript,typescript" %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as awsx from "@pulumi/awsx";

const repository = new awsx.ecr.Repository("repository", {});
export const url = repository.url;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_awsx as awsx

repository = awsx.ecr.Repository("repository")
pulumi.export("url", repository.url)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-awsx/sdk/go/awsx/ecr"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		repository, err := ecr.NewRepository(ctx, "repository", nil)
		if err != nil {
			return err
		}
		ctx.Export("url", repository.Url)
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

return await Deployment.RunAsync(() =>
{
    var repository = new Awsx.Ecr.Repository("repository");

    return new Dictionary<string, object?>
    {
        ["url"] = repository.Url,
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

        ctx.export("url", repository.url());
    }
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
resources:
  repository:
    type: awsx:ecr:Repository
outputs:
  url: ${repository.url}
```

{{% /choosable %}}

From there, we can just run `pulumi up` to provision a new repository:

```bash
$ pulumi up
Updating (dev):

     Type                           Name               Status
 +   pulumi:pulumi:Stack            crosswalk-aws-dev  created
 +   ├─ awsx:ecr:Repository         repository         created
 +   │  └─ aws:ecr:Repository       repository         created
 +   └─ aws:ecr:LifecyclePolicy     repository         created

Outputs:
    url: "012345678901.dkr.ecr.us-west-2.amazonaws.com/repository-e2fe830"

Resources:
    + 4 created

Duration: 4s
```

The `url` emitted is what we will use to push and pull images to and from the newly created repository. We can do
so either using the Docker CLI or through infrastructure as code in our Pulumi program.

## Building and Publishing Container Images

Amazon ECR stores [_images_](https://docs.aws.amazon.com/AmazonECR/latest/userguide/images.html) inside of the
repositories you create. You can use the Docker CLI to push and pull images explicitly, using the `build`, `push`,
and `pull` commands, targeting the repository's URL. Alternatively, you can use your Pulumi program to build and
publish container images as part of your Pulumi deployment, and consume them from ECS or EKS directly.

### Building and Publishing Images Manually Using the Docker CLI

All repositories in your account's ECR registry will have a URL of the form
`<aws_account_id>.dkr.ecr.<region>.amazonaws.com/<repo>`, where `<aws_account_id>` is your AWS account ID,
`<region>` is the location for the repository, and `<repo>` is the name given to the repository. In the above example,
the resulting URL is exported and printed to the console.

To build and publish a new Docker image to such a repository, first retrieve your container image in the usual way,
e.g. either using [`docker build`](https://docs.docker.com/engine/reference/commandline/build/) or
[`docker pull`](https://docs.docker.com/engine/reference/commandline/pull/).

The image then needs to be tagged with the URL of the repository you're publishing to. This can be done using
`docker build`'s `-t` argument, while building the image, as in:

```bash
$ docker build -t 012345678901.dkr.ecr.us-west-2.amazonaws.com/my-repo-e2fe830 .
```

Alternatively, this can be done by tagging the image with [`docker tag`](
https://docs.docker.com/engine/reference/commandline/tag/) after building or pulling it. For example, if the image
ID to tag is `e9ae3c220b23`, then we would run the following:

```bash
$ docker tag e9ae3c220b23 012345678901.dkr.ecr.us-west-2.amazonaws.com/my-repo-e2fe830
```

By default, this tag will be tagged as `latest`; if you'd like to tag it using something else, do so as usual:

```bash
$ docker tag e9ae3c220b23 012345678901.dkr.ecr.us-west-2.amazonaws.com/my-repo-e2fe830:v2.0
```

After building and tagging, we then need to authenticate with the ECR registry. Each authentication token covers a
single registry and lasts 12 hours. The AWS CLI provides an easy way to do this:

```bash
$ aws ecr get-login-password | docker login --username AWS --password-stdin 012345678901.dkr.ecr.us-west-2.amazonaws.com
```

For more information on authentication, see [Registry Authentication](
https://docs.aws.amazon.com/AmazonECR/latest/userguide/Registries.html#registry_auth)

Finally, after building, tagging, and logging in, we are ready to push to our repository:

```bash
$ docker push 012345678901.dkr.ecr.us-west-2.amazonaws.com/my-repo-e2fe830
The push refers to repository [012345678901.dkr.ecr.us-west-2.amazonaws.com/my-repo-e2fe830]
8a453b312607: Pushed
e6b5722b9fb4: Pushed
137a99b96f0d: Pushed
d6c6b3975afa: Pushed
36daa25da760: Pushed
be03501d5dd0: Pushed
3f9a4fb2ec3f: Pushed
a464c54f93a9: Pushed
latest: digest: sha256:f2d7dca5c0800e2dce13b655a439f368587b77ad82de11675851be4c9f2cbf91 size: 1999
```

Afterwards, we can then pull the image from the registry by authenticating and pulling from the repository URL.

### Building and Publishing Images Automatically in Code

Instead of using the Docker CLI directly, Pulumi supports building, publishing, and consuming Docker images
entirely from code. This lets you version and deploy container changes easily alongside the supporting infrastructure.

In the following example, creating an `Image` resource will build an image from the "./app" directory (relative to our project and containing Dockerfile), and publish it to our ECR repository provisioned above.

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language "javascript,typescript" %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as awsx from "@pulumi/awsx";

const repository = new awsx.ecr.Repository("repository", {});
const image = new awsx.ecr.Image("image", {
    repositoryUrl: repository.url,
    path: "./app",
});
export const url = repository.url;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_awsx as awsx

repository = awsx.ecr.Repository("repository")
image = awsx.ecr.Image("image",
    repository_url=repository.url,
    path="./app")
pulumi.export("url", repository.url)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-awsx/sdk/go/awsx/ecr"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		repository, err := ecr.NewRepository(ctx, "repository", nil)
		if err != nil {
			return err
		}
		_, err = ecr.NewImage(ctx, "image", &ecr.ImageArgs{
			RepositoryUrl: repository.Url,
			Path:          pulumi.String("./app"),
		})
		if err != nil {
			return err
		}
		ctx.Export("url", repository.Url)
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

return await Deployment.RunAsync(() =>
{
    var repository = new Awsx.Ecr.Repository("repository");

    var image = new Awsx.Ecr.Image("image", new()
    {
        RepositoryUrl = repository.Url,
        Path = "./app",
    });

    return new Dictionary<string, object?>
    {
        ["url"] = repository.Url,
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

        ctx.export("url", repository.url());
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
outputs:
  url: ${repository.url}
```

{{% /choosable %}}

As we run `pulumi up`, we will see Docker build output in the Pulumi CLI display. If there is an error, it'll
be printed in the diagnostics section, but otherwise the resulting image name is printed:

```bash
$ pulumi up
Updating (dev):

     Type                           Name               Status
 +   pulumi:pulumi:Stack            crosswalk-aws-dev  created
 +   └─ awsx:ecr:Repository         my-repo            created
 +      ├─ aws:ecr:Repository       my-repo            created
 +      └─ aws:ecr:LifecyclePolicy  my-repo            created

Outputs:
    image: "012345678901.dkr.ecr.us-west-2.amazonaws.com/my-repo-e2fe830:latest"

Resources:
    + 4 created

Duration: 13s
```

This image URL can then be used anywhere you'd normally use a Docker image name. For example, we can run it:

```bash
$ docker run -p 80:80 012345678901.dkr.ecr.us-west-2.amazonaws.com/my-repo-e2fe830:latest
```

As we will see below, this can also be consumed from your container orchestrator, to run the container as a service.

### Deleting Images

If you are done using an image, you can delete it from your repository. This can be done by [defining a lifecycle
policy](#managing-container-image-lifecycles-using-policies) or manually using the AWS CLI. For more information on
how to manually delete an image, see the ECR documentation on [Deleting an Image](
https://docs.aws.amazon.com/AmazonECR/latest/userguide/delete_image.html).

## Using a Private Repository from Your Container Orchestrator

To use your ECR images with Amazon ECS and EKS, use the full repository name as the image name. As seen above,
this is of the form `<aws_account_id>.dkr.ecr.<region>.amazonaws.com/<repo>[:<tag>]`, where the `<tag>` is optional (it
defaults to `latest`). The container instances require IAM permissions which are typically enabled by default.

### Consuming a Private Repository from ECS

To use your private repository from an ECS task definition, reference it like so:

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

For information about ECS, refer to the [Pulumi Crosswalk for AWS ECS documentation](/docs/guides/crosswalk/aws/ecs/). For
information about consuming ECR images from ECS services specifically, see
[Using Amazon ECR Images with Amazon ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/ECR_on_ECS.html).

### Consuming a Private Repository from EKS

To use your private repository from a Kubernetes service, such as one using EKS, reference it like so:

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language "javascript,typescript" %}}

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
package generated_program;

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

For information about EKS, refer to the [Pulumi Crosswalk for AWS EKS documentation](/docs/guides/crosswalk/aws/eks/).

### IAM Permissions Required to use ECR

For the above examples to work, the container instances powering your ECS or EKS cluster need proper IAM
policy permissions to access your Amazon ECR registry. The following example defines such an IAM policy:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ecr:BatchCheckLayerAvailability",
                "ecr:BatchGetImage",
                "ecr:GetDownloadUrlForLayer",
                "ecr:GetAuthorizationToken"
            ],
            "Resource": "*"
        }
    ]
}
```

See the [Pulumi Crosswalk for AWS IAM documentation](/docs/guides/crosswalk/aws/iam/) for instructions on how to manage
such policies.

## Managing Container Image Lifecycles using Policies

[ECR lifecycle policies](https://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html) allow
you to specify the lifecycle management of images in a repository. A lifecycle policy is a set of one or more rules,
where each rule defines an action for Amazon ECR. The actions apply to images that contain tags prefixed with the
given strings. This allows the automation of cleaning up unused images, for example expiring images based on age or
count. You should expect that after creating a lifecycle policy the affected images are expired within 24 hours.

Pulumi Crosswalk for AWS ECR module makes it easy to configure a repository's lifecycle policy, using the
`lifeCyclePolicyArgs` property on the `Repository` class's constructor. Using this property, there are two main ways
to control how an image is purged from the repository:

1. Once a maximum number of images has been reached (`maximumNumberOfImages`).
2. Once an image reaches a maximum allowed age (`maximumAgeLimit`).

### Lifecycle Policy Rules

For more details, refer to [Amazon ECR Lifecycle Policies](
https://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html), however we will now examine
a number of examples to demonstrate how lifecycle policies are applied.

## Additional ECR Resources

For more information about Amazon ECR, see the following:

* [Amazon Elastic Container Registry homepage](https://aws.amazon.com/ecr/)

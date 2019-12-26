---
title: "AWS Elastic Container Service (ECS)"
meta_desc: Pulumi Crosswalk for AWS ECS simplifies deploying containerized applications into ECS and managing all of the
           associated resources.
linktitle: Elastic Container Service (ECS)
menu:
  userguides:
    parent: crosswalk-aws
    weight: 5

aliases: ["/docs/reference/crosswalk/aws/ecs/"]
---

<a href="{{< relref "./" >}}">
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
> [Pulumi Crosswalk for AWS EKS]({{< relref "eks" >}}) for more information about using EKS.

## Creating a Load Balanced ECS Service

To run a Docker container in ECS using default network and cluster settings, use the `awsx.ecs.FargateService`
class. Since we need to access this container over port 80 using a stable address, we will use a load balancer:

```typescript
import * as awsx from "@pulumi/awsx";

// Create a load balancer on port 80 and spin up two instances of Nginx.
const lb = new awsx.lb.ApplicationListener("nginx", { port: 80 });
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

After deploying this program, we can access our two  NGINX web servers behind our load balancer via curl:

```bash
$ curl http://$(pulumi stack output url)
```

`$(pulumi stack output url)` evaluates to the load balancer's URL.

### **Output**

```
<!DOCTYPE html>
<html>
<body>
<h1>Welcome to nginx!</h1>
</body>
</html>
```

We have chosen to create an [Elastic Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing) so that we
can access our services over the Internet at a stable address, spread evenly across two instances. Any of the ELB
options described in the [Pulumi Crosswalk for ELB documentation]({{< relref "elb" >}}) can be used with our ECS service.

Behind the scenes, our program also creates an ECS cluster in the default VPC to run the compute. This is something
[we can configure](#creating-an-ecs-cluster-in-a-vpc) if we want to use a different VPC.

Because we've used [`Fargate`](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html), we don't
need to specify anything about our machine instances. Instead, Fargate will manage that for us automatically based on
the optional `memory` and `cpu` values we request for our containers.

For many scenarios, this is exactly what we want: a simple way of just running containerized applications. While this
approach is simple and hides a lot of complexity, it's often desirable to control more of what is going on.

## Explicitly Creating ECS Clusters for EC2 or Fargate

The `awsx.ecs.Cluster` class creates a new ECS cluster for Tasks and Services to run within. If you don't specify
a cluster explicitly, then a default one will be created that is configured to use your region's default VPC.

There are a few reasons to want to create a cluster explicitly: The first is to isolate the compute running in
different clusters from one another. Another is to place your cluster in a VPC so that it is isolated at the
networking level. If you want to schedule non-Fargate Tasks and Services, you will need to create a
cluster explicitly, since you will need to define an Auto Scaling Group that controls the EC2 instances powering it.

To use an explicit cluster, create an instance and pass it as the `cluster` property for the
`awsx.ecs.FargateService` or `awsx.ecs.EC2Service` constructors:

```typescript
import * as awsx from "@pulumi/awsx";

// Create an ECS cluster explicitly, and give it a name tag.
const cluster = new awsx.ecs.Cluster("custom", {
    tags: {
        "Name": "my-custom-ecs-cluster",
    },
});

// Deploy a Service into this new cluster.
const nginx = new awsx.ecs.FargateService("nginx", {
    cluster,
    // ... as before ...
});
```

In this example, we simply specified the tags for our cluster. We will see other possibilities in the following examples.

## Creating an ECS Cluster in a VPC

To create an ECS cluster inside of a VPC, we will first create or use an existing VPC using any of the techniques
described in [Pulumi Crosswalk for AWS VPC]({{< relref "vpc" >}}). Then we simply pass that
as the `vpc` argument for our cluster's constructor:

```typescript
import * as awsx from "@pulumi/awsx";

const vpc = new awsx.ec2.Vpc("vpc", { ... });
const cluster = new awsx.ecs.Cluster("custom", { vpc });

const nginx = new awsx.ecs.FargateService("nginx", {
    cluster,
    // ... as before ...
});
```

By default, the cluster will be given a security group permitting all egress from the cluster, on any TCP port,
and ingress from any address on port 22 and targeting any of the exposed load balancer endpoints in your cluster.
If you wish to override these defaults, pass the `securityGroupIds` property to the constructor.

## Creating an Auto Scaling Group for ECS Cluster Instances

Using Fargate is easy, because we don't have to worry about the EC2 instances powering our cluster. In the case
of wanting more control over the instances and their configuration, we can create an
[Auto Scaling Group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/AutoScalingGroup.html) explicitly, and
the cluster will then use that to run all compute scheduled inside our cluster. This is required to use `EC2Service`.

```typescript
import * as awsx from "@pulumi/awsx";

const cluster = new awsx.ecs.Cluster("custom");

const asg = cluster.createAutoScalingGroup("custom", {
    templateParameters: { minSize: 5 },
    launchConfigurationArgs: { instanceType: "t2.medium" },
});
```

Because we're manually managing our cluster's compute, we are also responsible for ensuring our cluster has enough
capacity to meet our workload's demands. It is typically not desirable to use a fixed quantity of servers. Instead,
refer to [Automatic Scaling with Amazon ECS](
https://aws.amazon.com/blogs/compute/automatic-scaling-with-amazon-ecs/) for best practices on setting up auto-scaling
for your ECS workloads. Remember, Fargate handles all of this for you behind the scenes, but with less control.

## Using an Existing ECS Cluster

If you already have an ECS cluster that you'd like to use, and would like to define Tasks and Services to run there, you can supply the `cluster` argument to the constructor:

```typescript
import * as awsx from "@pulumi/awsx";

// Fetch an existing cluster.
const cluster = new awsx.ecs.Cluster("custom", {
    cluster: aws.ecs.Cluster.get("existing_cluster_id"),
});

// Deploy a Service into the existing cluster.
const nginx = new awsx.ecs.FargateService("nginx", {
    cluster,
    // ... as before ...
});
```

Notice that we are using a method from a different package, [`aws.ecs.Cluster.get`](/docs/reference/pkg/nodejs/pulumi/aws/ecs/#Cluster-get), to look up our existing cluster by its ID and then creating an `awsx.ecs.Cluster` out of it. The former is the raw resource description, while the latter is the object type required to work with the Pulumi Crosswalk for AWS ECS APIs.

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

### ECS Task Definitions

A task definition is required to run Docker containers in Amazon ECS. We saw above that each Service takes a
`taskDefinitionArgs` object. Some of the parameters you can specify this task definition include:

* `image`: The Docker image to use with each container in your task.
* `cpu` and `memory`: How much CPU and memory to use with each task or each container within a task.
* `networkMode`: The Docker networking mode to use for the containers (`none`, `bridge`, `awsvpc`, or `host`).
* `logGroup`: The logging configuration to use for your tasks (by default, a new group with 1 day retention).
* `volumes`: Any data volumes that should be used with the containers in the task.
* `executionRole`: The IAM role that your tasks should assume while running.

Of course, the most important part of a task definition is the `containers` map, which specifies one or many
containers to run as part of your task.

### ECS Container Definitions

A TaskDefinition's [`containers` property](
https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html#container_definitions)
specifies the Docker configuration for one or more container instances that are launched by the task.

The simplest way to specify a container to run is to provide a string to the `image` parameter of the container
definition. This string is either the name of an image on [Docker Hub](https://hub.docker.com/), an [ECR Repository](
https://docs.aws.amazon.com/AmazonECR/latest/userguide/Repositories.html), or any valid Docker repository URL.

For example, this example simply uses the `nginx` image from the Docker Hub:

```typescript
import * as awsx from "@pulumi/awsx";

const listener = new awsx.lb.NetworkListener("listener", { port: 80 });
const task = new awsx.ecs.FargateTaskDefinition("task", {
    containers: {
        nginx: {
            image: "nginx",
            memory: 128,
            portMappings: [ listener ],
        },
    },
});
```

This has the effect of running a single container within our task that runs the Nginx web server.

### Services

ECS allows you to run and maintain a specified number of instances of a task definition simultaneously in a cluster.
This is called a Service. If any of your tasks should fail or stop for any reason, ECS launches another instance of
your task definition to replace it and maintain the desired count of tasks using your chosen scheduling strategy.

Although we have seen simple examples of Service definitions above, there are many additional capabilities.

This includes control of the scheduling of your service:

* `desiredCount`: The number of instances of the task definition to place and keep running. Defaults to 1. Do
  not specify if using the `DAEMON` scheduling strategy.

* `orderedPlacementStrategies`: Service level strategy rules that are taken into consideration during task placement.
  List from top to bottom in order of precedence. The maximum number of strategies is 5.

* `placementConstraints`: Rules that are taken into consideration during task placement. Maximum number of 10.

* `schedulingStrategy`: The scheduling strategy to use for the service. The valid values are `REPLICA` and `DAEMON`.
  Defaults to `REPLICA`. Note that Fargate tasks do not support the `DAEMON` scheduling strategy.

* `waitForSteadyState`: Wait for the service to reach a steady state (like [`aws ecs wait services-stable`](
  https://docs.aws.amazon.com/cli/latest/reference/ecs/wait/services-stable.html)) before considering a deployment
  complete. Defaults to `true`.

In addition to control of the health checking of your service:

* `deploymentMaximumPercent`: The upper limit (as a percentage of the service's `desiredCount`) of the number of running
  tasks that can be running in a service during a deployment. Not valid when using the `DAEMON` scheduling strategy.

* `deploymentMinimumHealthyPercent`: The lower limit (as a percentage of the service's `desiredCount`) of the number of
  running tasks that must remain running and healthy in a service during a deployment.

* `healthCheckGracePeriodSecond`: Seconds to ignore failing load balancer health checks on newly instantiated tasks to
  prevent premature shutdown, up to 7200. Only valid for services configured to use load balancers.

In addition to security and networking configuration:

* `iamRole`: ARN of the IAM role that allows Amazon ECS to make calls to your load balancer on your behalf. This
  parameter is required if you are using a load balancer with your service, but only if your task definition does not
  use the `awsvpc` network mode. If using `awsvpc` network mode, do not specify this role. If your account has already
  created the Amazon ECS service-linked role, that role is used by default for your service unless you specify a role

* `networkConfiguration`: The network configuration for the service. This parameter is required for task definitions
  that use the `awsvpc` network mode to receive their own Elastic Network Interface, and it is not supported for other
  network modes.

For additional information about each of these settings, please [refer to the AWS documentation](
https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service_definition_parameters.html).

## Building and Publishing Docker Images Automatically

Containers with Pulumi Crosswalk for AWS ECS are far more flexible than just accepting a preexisting image URL,
and can even refer to a `Dockerfile` on disk so you do not need to build and publish
it separately ahead of time. This makes it very easy to use private registrations for your ECS workloads.

For example, [`fromPath`](/docs/reference/pkg/nodejs/pulumi/awsx/ecs/#Image-fromPath") will run a `docker build` in that path, push the result up to the ECR repository that specified in the first argument, and then pass
the private ECR repostory path to the container:

```typescript
const task = new awsx.ecs.FargateTaskDefinition("task", {
    containers: {
        nginx: {
            image: awsx.ecs.Image.fromPath("<ecr-repository-name>", "/path/to/Dockerfile/"),
            // ...
        },
    },
});
```

For more control over how the Docker image is built and published, you can use [`fromDockerBuild`](/docs/reference/pkg/nodejs/pulumi/awsx/ecs/#Image-fromDockerBuild). This allows you
to control the build context, whether to cache multi-stage builds, and so on:

```typescript
const task = new awsx.ecs.FargateTaskDefinition("task", {
    containers: {
        nginx: {
            image: awsx.ecs.Image.fromDockerBuild({
                context: "./app",
                dockerfile: "./app/Dockerfile-multistage",
                cacheFrom: { stages: [ "build" ] },
            }),
            // ...
        },
    },
});
```

Finally, you can create a container image from a callback function. This allows you to author the same code that
runs in the container within your Pulumi application directly, much like [magic functions for Lambda]({{< relref "lambda" >}}):

```typescript
const listener =
    new awsx.lb.NetworkTargetGroup("custom", { port: 8080 })
               .createListener("custom", { port: 80 });

const service = new awsx.ecs.EC2Service("custom", {
    cluster,
    desiredCount: 2,
    taskDefinitionArgs: {
        containers: {
            webserver: {
                memory: 128,
                portMappings: [ listener ],
                image: awsx.ecs.Image.fromFunction(() => {
                    const rand = Math.random();
                    const http = require("http");
                    http.createServer((req: any, res: any) => {
                        res.end(`Hello, world! (from ${rand})`);
                    }).listen(8080);
                }),
            },
        },
    },
});
```

This example runs an anonymous web server inside of an image built and published automatically to ECR.

For more information about using ECR, refer to [Pulumi Crosswalk for AWS ECR]({{< relref "ecr" >}}).

## Running Fire and Forget Tasks

An ECS TaskDefinition can be used to define a Service, or it can be run on demand in a "fire and forget" manner---from within a Lambda callback for example. This can be done by calling the `run` method on the Task instance. This
`run` call must be supplied a cluster to run in.

For example, continuing from before:

```ts
import * as aws from "@pulumi/aws";
import * as awsx from "@pulumi/awsx";

const cluster = new awsx.ecs.Cluster("my-cluster");

const helloTask = new awsx.ecs.FargateTaskDefinition("hello-world", {
    container: {
        image: "hello-world",
        memory: 20,
    },
});

const api = new awsx.apigateway.API("hello-world-api", {
    routes: [{
        path: "/hello",
        method: "GET",
        eventHandler: async (req) => {
            // Anytime someone hits the /hello endpoint, schedule our task.
            const result = await helloTask.run({ cluster });
            return { statusCode: 200, body: "OK" };
        },
    }],
});
```

The calls to `run` must specify which `cluster` to run the task in, and may control other aspects of scheduling.

## Additional ECS Resources

* [Amazon Elastic Container Service](https://aws.amazon.com/ecs/)

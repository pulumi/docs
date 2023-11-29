---
title_tag: "Using AWS Elastic Container Service (ECS) | Crosswalk"
title: ECS
h1: AWS Elastic Container Service (ECS)
meta_desc: Pulumi Crosswalk for AWS ECS simplifies deploying containerized applications into ECS and managing all of the
            associated resources.
meta_image: /images/docs/meta-images/docs-clouds-aws-meta-image.png
menu:
  clouds:
    parent: aws-guides
    identifier: aws-guides-ecs
    weight: 5

aliases:
- /docs/reference/crosswalk/aws/ecs/
- /docs/guides/crosswalk/aws/ecs/
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
> [Pulumi Crosswalk for AWS EKS](/docs/clouds/aws/guides/eks/) for more information about using EKS.

## Creating a Load Balanced ECS Service

To run a Docker container in ECS using default network and cluster settings, use the `awsx.ecs.FargateService`
class. Since we need to access this container over port 80 using a stable address, we will use a load balancer.

{{< example-program path="awsx-load-balanced-fargate-nginx" >}}

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
options described in the [Pulumi Crosswalk for ELB documentation](/docs/clouds/aws/guides/elb/) can be used with our ECS service.

Behind the scenes, our program creates the ECS cluster in the default VPC to run the compute. This is something
[we can configure](/docs/clouds/aws/guides/eks#configuring-your-eks-clusters-networking) if we want to use a different VPC.

Because we've used [`Fargate`](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html), we don't
need to specify anything about our machine instances. Instead, Fargate will manage that for us automatically based on
the optional `memory` and `cpu` values we request for our containers.

For many scenarios, this is exactly what we want: a simple way of just running containerized applications. While this
approach is simple and hides a lot of complexity, it's often desirable to control more of what is going on.

## Creating an ECS Cluster in a VPC

To create an ECS service inside of a VPC, we will first create or use an existing VPC using any of the techniques
described in [Pulumi Crosswalk for AWS VPC](/docs/clouds/aws/guides/vpc/). Then we pass the subnets
from that VPC into the network configuration argument for our cluster:

{{< example-program path="awsx-vpc-fargate-service" >}}

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

{{< example-program path="awsx-load-balanced-fargate-ecr" >}}

For more information about using ECR, refer to [Pulumi Crosswalk for AWS ECR](/docs/clouds/aws/guides/ecr/).

## Additional ECS Resources

* [Amazon Elastic Container Service](https://aws.amazon.com/ecs/)

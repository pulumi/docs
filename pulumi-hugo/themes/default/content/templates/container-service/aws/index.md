---
title: Container Service on AWS
layout: template
meta_desc: The Container Service template makes it easy to deploy a container service on AWS with Pulumi and Amazon Elastic Container Service (ECS).
meta_image: meta.png
card_desc: Deploy a container service on AWS with Pulumi and Amazon ECS.
template:
  prefix: container-aws
  dirname: my-container-service
  languages:
    - typescript
    - python
    - go
    - csharp
    - yaml
cloud:
  name: Amazon Web Services
  slug: aws
---

The Container Service template creates an infrastructure as code project in your favorite language that deploys a container service to AWS. You can then use the container service to build your own containerized application. The architecture includes [Amazon Elastic Container Service (ECS)]({{< relref "/registry/packages/aws/api-docs/ecs/cluster" >}}) for cluster management, [AWS Fargate]({{< relref "/registry/packages/awsx/api-docs/ecs/fargateservice" >}}) to run the cluster on serverless compute, and an [Application Load Balancer]({{< relref "/registry/packages/awsx/api-docs/lb" >}}) that serves the container endpoint to the internet. It also uses an [Amazon Elastic Container Repository (ECR)]({{< relref "/registry/packages/awsx/api-docs/ecr/repository" >}}) that stores the container image. The template generates a complete Pulumi program that provisions the cloud resources and installs Nginx in a container, providing you with a working project out of the box that you can customize easily and extend to suit your needs.

![An architecture diagram of the Pulumi AWS Container Service template](./architecture.png)

## Using this template

To use this template to deploy an ECS cluster that's running your container service, make sure you've [installed Pulumi]({{< relref "/docs/get-started/install" >}}) and [configured your AWS credentials]({{< relref "/registry/packages/aws/installation-configuration#credentials" >}}), then create a new [project]({{< relref "/docs/intro/concepts/project" >}}) using the template in your language of choice:

{{< templates/pulumi-new >}}

Follow the prompts to complete the new-project wizard. When it's done, you'll have a complete Pulumi project that's ready to deploy and configured with the most common settings. Feel free to inspect the code in {{< langfile >}} for a closer look.

## Deploying the project

The template requires no additional configuration. Once the new project is created, you can deploy it immediately with [`pulumi up`]({{< relref "/docs/reference/cli/pulumi_up" >}}):

```bash
$ pulumi up
```

When the deployment completes, Pulumi exports the following [stack output]({{< relref "/docs/intro/concepts/stack#outputs" >}}) values:

url
: The HTTP URL for the container's endpoint.

Output values like these are useful in many ways, most commonly as inputs for other stacks or related cloud resources. The computed `url`, for example, can be used from the command line to open the newly deployed container service in your favorite web browser:

```bash
$ open $(pulumi stack output url)
```

## Customizing the project

Projects created with the Container Service template expose the following [configuration]({{< relref "/docs/intro/concepts/config" >}}) settings:

container_port
: Specifies the port mapping for the container. Defaults to port 80.

cpu
: Specifies the amount of CPU to use with each task or each container within a task. Defaults to 512.

memory
: Specifies the amount of memory to use with each task or each container within a task. Defaults to 128.

image
: Specifies the location of the Dockerfile used to build the container image that is run. Defaults to the Dockerfile in the `app` folder.

All of these settings are optional and may be adjusted either by editing the stack configuration file directly (by default, `Pulumi.dev.yaml`) or by changing their values with [`pulumi config set`]({{< relref "/docs/reference/cli/pulumi_config_set" >}}) as shown below.

### Using your own container image

If you already have a container image you'd like to build your container service with, you can do so either by replacing the Dockerfile in the `app` folder or by configuring the stack to point to another folder on your computer with the `image` setting:

```bash
$ pulumi config set path ../my-existing-image/build
$ pulumi up
```

## Tidying up

You can cleanly destroy the stack and all of its infrastructure with [`pulumi destroy`]({{< relref "/docs/reference/cli/pulumi_destroy" >}}):

```bash
$ pulumi destroy
```

## Learn more

Congratulations! You're now well on your way to managing a production-grade container service on AWS with Pulumi --- and there's lots more you can do from here:

* Discover more architecture templates in [Templates &rarr;]({{< relref "/templates" >}})
* Dive into the API docs for the [AWS]({{< relref "/registry/packages/aws" >}}) and [AWSx (Crosswalk)]({{< relref "/registry/packages/awsx" >}}) packages
* Expand your understanding of how Pulumi works in [Learn Pulumi &rarr;]({{< relref "/learn" >}})
* Read up on the latest new features [in the Pulumi Blog &rarr;](/blog/tag/containers)

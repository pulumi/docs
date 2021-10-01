---
title: "Pulumi container images now available on Amazon ECR Public"
date: "2020-12-01"
meta_desc: "Pulumi container images now available on Amazon ECR Public"
meta_image: "pulumi-images-ecr.png"
authors: ["paul-stack"]
tags: ["aws", "containers", "ecr"]
---

At re:Invent, the AWS team unveiled the new Amazon Elastic Container Registry Public (Amazon ECR Public), creating a new
option for users in publishing and pulling public container images. Pulumi fully supports Amazon ECR Public in two ways:

1. Official Pulumi container images are available today on Amazon ECR Public.
2. Pulumi is the easiest way to package and publish your container images, and we’ll support publishing your container
   images to Amazon ECR Public very soon.

<!--more-->

If you want to learn more about Pulumi and building resources in AWS, join one of our [upcoming workshops](https://www.pulumi.com/events-workshops/#upcoming).

Pulumi publishes official container images for running Pulumi along with the desired Pulumi programming language runtimes.
These containers are used directly by developers as the foundation for process automation, such as GitHub Actions; in custom
container environments with Pulumi’s Automation API; and in Kubernetes-based solutions, like the Pulumi Kubernetes Operator.
These images are publicly available via [Docker Hub](https://hub.docker.com/r/pulumi) and will continue to be available there.

With the unveiling of Amazon ECR Public, we want to make sure Pulumi’s official container images are always available to
ensure that our users can ultimately choose the right container image that suits their needs. Going forward, Pulumi’s
official container images will be available on Amazon ECR Public.

We've published our Pulumi container images in this new repository, and we plan to publish to both the Docker Hub and Amazon
ECR Public repositories for all new Pulumi releases. You can browse Pulumi images in the Amazon ECR gallery here:
[https://gallery.ecr.aws/?searchTerm=pulumi](https://gallery.ecr.aws/?searchTerm=pulumi).

## Try it out!

Here’s how easy it is to grab the latest Pulumi container images from the Amazon ECR Public repository:

```bash
$ docker pull public.ecr.aws/pulumi/pulumi:latest
```

To grab the latest language runtime specific containers, run the following commands:

Python:

```bash
$ docker pull public.ecr.aws/pulumi/pulumi-python:latest
```

Go:

```bash
$ docker pull public.ecr.aws/pulumi/pulumi-go:latest
```

TypeScript / JavaScript:

```bash
$ docker pull public.ecr.aws/pulumi/pulumi-nodejs:latest
```

DotNet:

```bash
$ docker pull public.ecr.aws/pulumi/pulumi-dotnet:latest
```

Finally, you can grab the latest official image for the Pulumi Kubernetes Operator with this command:

```bash
$ docker pull public.ecr.aws/pulumi/pulumi-kubernetes-operator:latest
```

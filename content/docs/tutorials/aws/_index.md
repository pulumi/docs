---
title: "AWS Tutorials"
meta_desc: A collection of tutorials that highlight complete end-to-end scenarios when
           using the Amazon Web Services (AWS) platform.
linktitle: "AWS"
menu:
  userguides:
    parent: tutorials
    identifier: tutorials-aws

aliases: ["/docs/reference/tutorials/aws/"]
---

The following tutorials highlight the AWS platform using complete end-to-end scenarios.

> If this is your first time getting started with Pulumi for AWS, try the
> easy <a href="{{< relref "/docs/get-started/aws" >}}">Get Started guide</a> first.
> For a more in-depth information about Pulumi's support for specific AWS services, see the
> [Pulumi AWS User Guide]({{< relref "/docs/guides/crosswalk/aws" >}}).
>
> If you are looking to use Kubernetes on AWS, see [the EKS tutorial]({{< relref "../kubernetes/eks" >}}).

## Featured Tutorials

<div class="md:flex flex-row mt-6 mb-6">
    <div class="w-1/2 border-solid border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4">
            <i class="fas fa-server pr-2"></i>
            <a href="{{< relref "ec2-webserver" >}}" style="color: #4387c7">
                EC2 Virtual Machine
            </a>
        </h3>
        <p>
            Provision a Linux web server using an Amazon EC2 virtual machine.
        </p>
    </div>
    <div class="w-1/2 border-solid ml-4 border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4">
            <i class="fas fa-boxes pr-2"></i>
            <a href="{{< relref "ecs-fargate" >}}" style="color: #4387c7">
                ECS Fargate Containers
            </a>
        </h3>
        <p>
            Build and deploy a containerized application to a private
            Amazon ECR registry, and provision a load balanced ECS "Fargate"
            service.
        </p>
    </div>
</div>

<div class="md:flex flex-row mt-6 mb-6">
    <div class="w-1/2 border-solid border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4">
            <i class="fas fa-bolt pr-2"></i>
            <a href="{{< relref "rest-api" >}}" style="color: #4387c7">
                API Gateway and Lambda
            </a>
        </h3>
        <p>
            Create a serverless application using Amazon API Gateway and
            Lambda with automatic SSL and on-demand scaling.
        </p>
    </div>
    <div class="w-1/2 border-solid ml-4 border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4">
            <i class="fas fa-globe pr-2"></i>
            <a href="{{< relref "s3-website" >}}" style="color: #4387c7">
                S3 Static Website
            </a>
        </h3>
        <p>
            Deploy and serve a static website publicly on the Internet using AWS S3.
        </p>
    </div>
</div>

## Other Examples and Tutorials

{{< chooser language "javascript,typescript,python" / >}}
{{< tutorials-index-aws >}}

If you'd like to see a new tutorial, please [request one](
https://github.com/pulumi/docs/issues/new?title=New%20AWS%20Tutorial%20Request).
Pull requests are also welcome!

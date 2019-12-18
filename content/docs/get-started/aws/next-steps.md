---
title: Next Steps | AWS
h1: Next Steps
linktitle: Next Steps
meta_desc: This page provides a list of tutorials that take a deeper dive into
            AWS cloud resources.
weight: 11
no_on_this_page: true
menu:
  getstarted:
    parent: aws
    identifier: aws-next-steps

aliases: ["/docs/quickstart/aws/next-steps/"]
---

We've seen how to quickly get started using AWS with Pulumi.

From here, you can dive deeper with additional AWS tutorials:

* [Containers on ECS "Fargate"]({{< relref "/docs/tutorials/aws/ecs-fargate" >}}): Deploy containers to Amazon
* [EC2 Linux WebServer VM]({{< relref "/docs/tutorials/aws/ec2-webserver.md" >}}): Create an EC2 Linux Web Server virtual machine
* [Serverless REST API Gateways using Lambda]({{< relref "/docs/tutorials/aws/rest-api" >}}): Create simple RESTful web server using AWS Lambdas
* [Serve a Static Website from S3]({{< relref "/docs/tutorials/aws/s3-website" >}}): Serve a static website out of content in an S3 bucket
* [Serverless + Containers + Infrastructure]({{< relref "/docs/tutorials/aws/video-thumbnailer" >}}): Deploy a complete  application using a combination of buckets, serverless functions and containers.

In addition to the tutorials, several interesting examples are available complete with instructions:

* [Ruby on Rails in EC2](https://github.com/pulumi/examples/tree/master/aws-ts-ruby-on-rails): Run a Ruby on Rails
    WebServer using EC2 instances
* [SQS-Triggered Lambdas](https://github.com/pulumi/examples/tree/master/aws-js-sqs-slack): Post to Slack using a Lambda
    anytime a SQS message arrives
* [Static Website in CloudFront and S3](https://github.com/pulumi/examples/tree/master/aws-ts-static-website): Create a
    static website serving content out of S3, fronted by a CloudFront CDN
* [Provision an Elastic Kubernetes Service Cluster](https://github.com/pulumi/examples/tree/master/aws-ts-eks): Stand up
    a managed EKS cluster

## Introducing Pulumi Crosswalk for AWS

<a href="{{< relref "/docs/guides/crosswalk/aws" >}}">
    <img src="/images/docs/reference/crosswalk/aws/logo.svg" width="150" align="right" style="margin-left: 16px">
</a>

Use Pulumi Crosswalk for AWS to easily use the best of what AWS has to offer, with
well-architected best practices, for the entire AWS cloud. Go to production
with containers, Kubernetes, and serverless applications.

<a href="{{< relref "/docs/guides/crosswalk/aws" >}}">Get Started with Crosswalk for AWS Now</a>

{{< get-started-stepper >}}

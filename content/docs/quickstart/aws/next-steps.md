---
title: Next Steps
weight: 11
menu:
  quickstart:
    parent: aws
    identifier: aws-next-steps
---

We've seen how to quickly get started using AWS with Pulumi.

From here, you can dive deeper with additional AWS tutorials:

* [Containers on ECS "Fargate"]({{< relref "/docs/reference/tutorials/aws/tutorial-service.md" >}}): Deploy containers to Amazon
* [EC2 Linux WebServer VM]({{< relref "/docs/reference/tutorials/aws/tutorial-ec2-webserver.md" >}}): Create an EC2 Linux Web Server virtual machine
* [Serverless REST API Gateways using Lambda]({{< relref "/docs/reference/tutorials/aws/tutorial-rest-api.md" >}}): Create simple RESTful web server using AWS Lambdas
* [Serve a Static Website from S3]({{< relref "/docs/reference/tutorials/aws/tutorial-s3-website.md" >}}): Serve a static website out of content in an S3 bucket
* [Serverless + Containers + Infrastructure]({{< relref "/docs/reference/tutorials/aws/tutorial-thumbnailer.md" >}}): Deploy a complete  application using a combination of buckets, serverless functions and containers.

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

<a href="{{< relref "/docs/reference/crosswalk/aws" >}}">
    <img src="/images/docs/reference/crosswalk/aws/logo.svg" width="150" align="right" style="margin-left: 16px">
</a>

Use Pulumi Crosswalk for AWS to easily use the best of what AWS has to offer, with
well-architected best practices, for the entire AWS cloud. Go to production
with containers, Kubernetes, and serverless applications.

<a href="{{< relref "/docs/reference/crosswalk/aws" >}}">Get Started with Crosswalk for AWS Now</a>

{{< get-started-stepper >}}

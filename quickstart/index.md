---
title: Getting Started
---

<!-- LINKS: -->
[Pulumi examples repo]: https://github.com/pulumi/examples
<!-- END LINKS: -->

> **Note:** Some sections of 5-part Quickstart are still under development. In the meantime, check out the [Pulumi introduction](../reference/index.html) and the [Pulumi examples repo on GitHub].

Welcome!  We are excited that you want to learn Pulumi.  The Pulumi Quickstart teaches you how to:

1. [Set up your environment and build your first Pulumi program](./part1.html)
2. [Create reusable libraries for infrastructure](./part2.html)
3. Create programs that use containers and serverless functions
4. Deploy application and infrastructure code together using the same tools and workflows
5. Learn more

## Additional Documentation

In addition to the tutorial, you can check out the reference documentation for information:

* [An overall introduction to Pulumi](../reference/index.html)
* [Learn the core concepts used by Pulumi programs](../reference/concepts.html)
* [Using Pulumi to manage AWS Infrastructure](../reference/aws.html)
* [Using Pulumi to create Cloud-Agnostic Serverless and Containers](../reference/cloud.html)
* [Use JavaScript or TypeScript to program the cloud](../reference/javascript.html)
* [Use Python to program the cloud](../reference/python.html)

Much more is available in the table of contents available in [the reference section index](../reference/index.html).

## Code Examples

For code samples, see examples in the [Pulumi examples repo] on GitHub. Below are some highlighted samples.

- [AWS EC2 instance in JavaScript](https://github.com/pulumi/examples/tree/master/aws-js-webserver)
- [AWS EC2 instance in Python](https://github.com/pulumi/examples/tree/master/aws-py-webserver)
- [Azure Virtual Machine in JavaScript](https://github.com/pulumi/examples/tree/master/azure-js-webserver)
- [Kubernetes Nginx in TypeScript](https://github.com/pulumi/examples/tree/master/kubernetes-ts-webserver)
- [URL Shortener](https://github.com/pulumi/examples/tree/master/cloud-ts-url-shortener/). A complete URL shortener web application using high-level `cloud.Table` and `cloud.HttpEndpoint` components.
- [Video Thumbnailer](https://github.com/pulumi/examples/tree/master/cloud-js-thumbnailer/). An end-to-end pipeline for generating keyframe thumbnails from videos uploaded to a bucket using containerized [FFmpeg](https://www.ffmpeg.org/).  
- [Raw AWS Serverless](https://github.com/pulumi/examples/tree/master/aws-ts-serverless-raw). A complete serverless C# application using raw `aws.apigateway.RestAPI`, `aws.lambda.Function` and `aws.dynamodb.Table` resources from `@pulumi/aws`. 

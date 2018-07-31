---
title: Getting Started
---

Welcome to the intro guide to Pulumi. This is the best place to get started using Pulumi to create cloud applications
and infrastructure. Pulumi supports many languages and clouds, leverages package management for easy sharing and reuse,
and is built atop an open source platform for creating and versioning your cloud software safely and in a team setting.

[Install Pulumi](../install) and then choose from one of the following next steps:

* [Take a Tour](../tour): Take a Tour of Pulumi, learning key programming model concepts, one at a time
* [Hello World](aws-hello-world.html): Create a simple HTTP app that uses serverless functions (currently AWS-only)
* [Tutorials](#tutorials): Take 5-minute tutorials for containers, serverless, or infrastructure (currently AWS-only)
* [Examples](#examples): Explore examples across many clouds, languages, and scenarios (including AWS, Azure, GCP, and Kubernetes)

## <a name="tutorials"></a>Tutorials

Each tutorial walks through an end-to-end scenario in 5 minutes:

* [Containers](aws-containers.html): Create a load-balanced, hosted NGINX container service
* [Serverless](aws-rest-api.html): Create a REST API that uses serverless functions and Dynamo DB
* [Infrastructure](aws-ec2.html): Create an EC2-based WebServer and associated infrastructure
* [Everything Together (Colada)](aws-extract-thumbnail.html): Create a video thumbnail app that uses containers, serverless, and infrastructure together

> **Note:** Although Pulumi supports Azure, GCP, Kubernetes, and other cloud providers, these tutorials use AWS. If you
> don't have an AWS account, [create one now](https://aws.amazon.com/free/). Tutorials for other clouds are on their way.

## <a name="examples"></a>Examples

Our [examples repo](https://github.com/pulumi/examples) on GitHub contains examples across many clouds -- AWS, Azure,
GCP, and Kubernetes -- languages -- JavaScript, TypeScript, Python, and Go -- and scenarios -- containers, serverless,
and infrastructure. Each example is self-contained and easily deployable with instructions in its README.

These are good starting points for basic introductions across each cloud provider/scenario:

* **Containers**:
    - [AWS ECS/Fargate](https://github.com/pulumi/examples/tree/master/cloud-js-containers)
    - [Kubernetes Guestbook](https://github.com/pulumi/examples/tree/master/kubernetes-ts-guestbook)
* **Serverless**:
    - [AWS Lambdas](https://github.com/pulumi/examples/tree/master/cloud-js-api)
    - [Google Cloud Functions](https://github.com/pulumi/examples/tree/master/gcp-ts-functions)
    - [Azure Functions](https://github.com/pulumi/examples/tree/master/azure-ts-functions)
* **Infrastructure**:
    - [AWS VM WebServer](https://github.com/pulumi/examples/tree/master/aws-js-webserver)
    - [Azure VM WebServer](https://github.com/pulumi/examples/tree/master/azure-js-webserver)
    - [GCP VM WebServer](https://github.com/pulumi/examples/tree/master/gcp-js-webserver)

For more compete examples, please check out the index in
[the example repo's README](https://github.com/pulumi/examples/blob/master/README.md).

---
title: Tutorials
---

To get started with Pulumi, [configure AWS](../install/aws.html). Then, run the following commands: 

```bash
# Step 1. Install Pulumi
curl -fsSL https://get.pulumi.com | sh

# Step 2. Create a new project
pulumi new hello-aws-javascript

# Step 3. Deploy to the cloud
pulumi update
```

## Featured tutorials

- [Hello World](aws-hello-world.html). A simple single-page app that uses serverless functions.
- [Containers](aws-containers.html). Deploy an NGINX container to production in 5 minutes.
- [Serverless REST API](aws-rest-api.html). In just 20 lines of code, create a REST API that uses serverless functions and Dynamo DB.
- [Provision virtual machines on AWS](aws-ec2.html). Use JavaScript to create repeatable deployments of cloud infrastructure.
- [Create an application with serverless functions and containers](aws-extract-thumbnail.html). Create a full application that extracts a thumbnail from a video, using AWS Lambda and FFmpeg running in a Docker container.

## Featured examples

Check out these examples in the [Pulumi examples repo](https://github.com/pulumi/examples) on GitHub. 

### Containers

- [Voting app with two containers (TypeScript)](https://github.com/pulumi/examples/tree/master/cloud-ts-voting-app). 
A simple voting app that uses Redis for a data store and a Python Flask app for the frontend. 

### Serverless functions

- [URL Shortener (TypeScript)](https://github.com/pulumi/examples/tree/master/cloud-ts-url-shortener/). A complete URL shortener web application using high-level `cloud.Table` and `cloud.API` components.
- [Video Thumbnailer (JavaScript)](https://github.com/pulumi/examples/tree/master/cloud-js-thumbnailer/). An end-to-end pipeline for generating keyframe thumbnails from videos uploaded to a bucket using containerized [FFmpeg](https://www.ffmpeg.org/).  
- [Raw AWS Serverless (TypeScript)](https://github.com/pulumi/examples/tree/master/aws-ts-serverless-raw). A complete serverless application using raw `aws.apigateway.RestAPI`, `aws.lambda.Function` and `aws.dynamodb.Table` resources from `@pulumi/aws`. 

### Infrastructure

- [AWS EC2 instance (Python)](https://github.com/pulumi/examples/tree/master/aws-py-webserver)
- [Azure Virtual Machine (JavaScript)](https://github.com/pulumi/examples/tree/master/azure-js-webserver)
- [Static website on AWS S3 (JavaScript)](https://github.com/pulumi/examples/tree/master/aws-js-s3-folder)

### Kubernetes 

- [Kubernetes Guestbook (TypeScript)](https://github.com/pulumi/examples/tree/master/kubernetes-ts-guestbook). A version of the Kubernetes Guestbook app using Pulumi and `@pulumi/kubernetes`.



<!-- LINKS: -->
[Pulumi examples repo]: https://github.com/pulumi/examples
<!-- END LINKS: -->


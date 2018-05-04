---
title: Getting Started
---

<!-- LINKS: -->
[Pulumi examples repo]: https://github.com/pulumi/examples
<!-- END LINKS: -->

Pulumi is a tool and service that makes it easier to build modern cloud applications on AWS, Azure, GCP, and Kubernetes. Instead of using a configuration language, you use JavaScript or Python to define your desired cloud resources. 

Resources are declared with syntax like `new aws.ec2.Instance` in JavaScript or `ec2.Instance(...)` in Python. Pulumi is based on the concept of _immutable infrastructure_. Unlike Boto scripts that mutate infrastructure when they are run, Pulumi runs your program to determine the desired set of resources. Then, Pulumi makes only the minimal required changes to your infrastructure, without disrupting existing resources.

## 5-minute quickstarts

- [Create EC2 instances on AWS](./aws-ec2.html)
- [Host a static site on S3](./aws-s3-website.html)
- [Create a serverless REST API](./aws-rest-api.html)
- Provision containers on AWS (coming soon!)

## Code Examples

For code samples, see examples in the [Pulumi examples repo] on GitHub. Below are some highlighted samples. If you don't have access to the GitHub repo, please email [support@pulumi.com](mailto:support@pulumi.com) to get access, or download the [Pulumi examples zipfile](/examples/pulumi-examples.zip).

**Virtual machines**

- [AWS EC2 instance (JavaScript)](https://github.com/pulumi/examples/tree/master/aws-js-webserver)
- [AWS EC2 instance (Python)](https://github.com/pulumi/examples/tree/master/aws-py-webserver)
- [Azure Virtual Machine (JavaScript)](https://github.com/pulumi/examples/tree/master/azure-js-webserver)

**Containers**

- [Voting app with two containers (TypeScript)](https://github.com/pulumi/examples/tree/master/cloud-ts-voting-app). 
A simple voting app that uses Redis for a data store and a Python Flask app for the frontend. 

**Kubernetes** 

- [Kubernetes Guestbook (TypeScript)](https://github.com/pulumi/examples/tree/master/kubernetes-ts-guestbook). A version of the Kubernetes Guestbook app using Pulumi and `@pulumi/kubernetes`.

**Serverless functions**

- [URL Shortener](https://github.com/pulumi/examples/tree/master/cloud-ts-url-shortener/). A complete URL shortener web application using high-level `cloud.Table` and `cloud.HttpEndpoint` components.
- [Video Thumbnailer](https://github.com/pulumi/examples/tree/master/cloud-js-thumbnailer/). An end-to-end pipeline for generating keyframe thumbnails from videos uploaded to a bucket using containerized [FFmpeg](https://www.ffmpeg.org/).  
- [Raw AWS Serverless](https://github.com/pulumi/examples/tree/master/aws-ts-serverless-raw). A complete serverless application using raw `aws.apigateway.RestAPI`, `aws.lambda.Function` and `aws.dynamodb.Table` resources from `@pulumi/aws`. 



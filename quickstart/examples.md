---
title: "Example Code"
---

We have a number of examples in the [Pulumi examples repo](https://github.com/pulumi/examples) on GitHub. Below are some highlighted samples. If you don't have access to the GitHub repo, please email [support@pulumi.com](mailto:support@pulumi.com) to get access, or download the [Pulumi examples zipfile](/examples/pulumi-examples.zip).

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

- [URL Shortener (TypeScript)](https://github.com/pulumi/examples/tree/master/cloud-ts-url-shortener/). A complete URL shortener web application using high-level `cloud.Table` and `cloud.HttpEndpoint` components.
- [Video Thumbnailer (JavaScript)](https://github.com/pulumi/examples/tree/master/cloud-js-thumbnailer/). An end-to-end pipeline for generating keyframe thumbnails from videos uploaded to a bucket using containerized [FFmpeg](https://www.ffmpeg.org/).  
- [Raw AWS Serverless (TypeScript)](https://github.com/pulumi/examples/tree/master/aws-ts-serverless-raw). A complete serverless application using raw `aws.apigateway.RestAPI`, `aws.lambda.Function` and `aws.dynamodb.Table` resources from `@pulumi/aws`. 



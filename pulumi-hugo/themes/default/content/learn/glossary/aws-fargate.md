---
title: Fargate
meta_desc: A serverless compute product from AWS, designed for use with containerized workloads.
layout: glossary/single
---

## Definition

[AWS Fargate](https://aws.amazon.com/fargate/) is a serverless compute platform, allowing you to run your application without the need to directly provision and manage EC2 instances. Unlike [AWS Lambda](/learn/glossary/aws-lambda), which is designed to execute code directly, Fargate works alongside [AWS Elastic Container Service](/learn/glossary/aws-ecs) (ECS) or [Elastic Kubernetes Service](/learn/glossary/aws-eks) (EKS) to run containerized applications.

An application running on Fargate consists of multiple components. The overarching component is called a cluster, and it includes a grouping of tasks and services that make up your application. The task definition describes the parameters for your application, such as which containers to run, what operating system should be used, and the ports the application will use. A task is an instance of this definition running inside of your cluster, either by itself or as part of a service. The service component is what maintains the scheduling of your tasks, bringing up as many instances of that task as you defined and restarting them if one goes down.

### Use Cases

The low operational overhead involved in using Fargate, as well as the ease of splitting up components into isolated task definitions, makes it a great tool for applications built as groupings of microservices that require more complexity than AWS Lambda can support.

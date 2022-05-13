---
title: Elastic Container Service
meta_desc: A managed container orchestration tool on AWS, allowing for the deployment and automated management of containerized applications.
layout: glossary/single
---

## Description

[AWS Elastic Container Service](https://aws.amazon.com/ecs/) (ECS) is a managed container orchestration tool. Containers and the parameters necessary to run your application are described in a task definition. That task definition is then used to instantiate a task either by itself, or as part of a service that handles the automated maintenance of those tasks for you. Applications running on ECS are deployed either via [Fargate](/learn/glossary/aws-fargate), a serverless compute platform for containerized applications, or via EC2.

### Use Cases

The ideal use case for ECS is dependent on how you deploy the application. If you have an application built of many small containerized microservices, require batch processing, or have small workloads with occasional spikes of activity, use Fargate. If you need to directly manage your own infrastructure, or have a very busy application that will require consistently high usage of CPU or memory, use EC2.

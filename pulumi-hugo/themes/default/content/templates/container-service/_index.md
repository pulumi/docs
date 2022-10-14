---
title: Container Service Templates
layout: overview
description: Pulumi program templates are the fastest way to deploy container services on AWS, Azure, or Google Cloud Platform. Templates come with predefined infrastructure as code so you can get started instantly.
meta_desc: Pulumi program templates that make it easy to deploy container services on AWS, Azure, or Google Cloud Platform.
meta_image: meta.png
weight: 1
---

### What are containers?

[Containers](/containers) are lightweight virtualized operating system environments in which developers can package and run an application and its dependencies as isolated runtime environments. The benefits of containers include better scalability, portability, and fault isolation. Docker is most commonly used to create container images. Containers are great for scenarios such as microservices, batch jobs, and migrating a legacy application. In the cloud, containers are typically run using container services that manage the container orchestration, cluster management, and compute for you.

**On AWS,** these are the main ways to run containers:
|                                         |                                                                                                                                                       |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Amazon Elastic Container Service (ECS)  | Fully managed container orchestration service created by AWS. Deploy containers to EC2 instances you manage or serverless instances from AWS Fargate. |
| Amazon Elastic Kubernetes Service (EKS) | Fully managed Kubernetes service. Deploy containers to EC2 instances you manage or serverless instances from AWS Fargate.                             |
| AWS Fargate                             | Serverless compute engine for containers that you use with ECS and EKS. Deploys and manages EC2 instances for you when you’re running containers.     |
| AWS AppRunner                           | Fully managed container service that runs your container images without you needing to know how to deploy and manage the underlying infrastructure.   |

### Building and deploying container services on AWS, Azure, and Google Cloud

[Infrastructure as code](/what-is/what-is-infrastructure-as-code) is an efficient and repeatable way of building container services with programming languages and deploying them to your preferred cloud, such as [AWS](/aws), [Azure](/azure), or [Google Cloud Platform](/gcp).

Pulumi’s open source, infrastructure as code SDK lets you build and deploy container services with TypeScript/JavaScript, Python, Go, Java, .NET, and YAML. The main benefits include:

* **Programming Languages:** Define infrastructure as code in your favorite language instead of domain-specific languages or clicking through cloud consoles.

* **Container Ecosystem Support:** Orchestrate every component (container registries, images, clusters, tasks, etc.) with code.

* **Fast, Easy Deployment:** Quickly deploy a container service with a CLI or from a CI/CD workflow.

* **Rapid Development:** Author, version, test, and release infrastructure changes just like software.

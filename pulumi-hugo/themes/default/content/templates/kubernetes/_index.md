---
title: "Kubernetes Templates"
layout: overview
description: Pulumi program templates are the fastest way to deploy Kubernetes clusters and their associated infrastructure on AWS, Azure, or Google Cloud Platform. Templates come with predefined infrastructure as code so you can get started instantly.
meta_desc: Pulumi program templates that make it easy to deploy Kubernetes on AWS, Azure, or Google Cloud Platform.

# Be sure to replace this image. Figma source file:
# https://www.figma.com/file/lGrSpwbGGmbixEuewMbtkh/Template-Architecture-Diagrams?node-id=15%3A196
meta_image: meta.png

# Adjust this value to ensure the new template sorts as you'd like it to sort in the list.
weight: 99
---

### What is Kubernetes?

[Kubernetes (k8s)](/kubernetes) is an open source container management and orchestration project. It enables infrastructure engineers and platform teams to deploy and run container services at scale with a control plane that schedules, deploys, and scales containers throughout their lifecycle using a desired state model. The benefits of using k8s include its portability across multiple environments and clouds, high scalability, and extensibility via an ecosystem of extensions and plugins.

**On [AWS](/aws/),** you can use Kubernetes with Amazon Elastic Kubernetes Service (EKS).

**On [Azure](/azure/),** you can use Kubernetes with Azure Kubernetes Service (AKS).

**On [Google Cloud Platform](/gcp/),** you can use Kubernetes with Google Kubernetes Engine (GKE).

### Building and deploying Kubernetes clusters on AWS, Azure, and Google Cloud

[Infrastructure as code](/what-is/what-is-infrastructure-as-code/) is an efficient and repeatable way of building Kubernetes clusters and their infrastructure with programming languages and deploying them to your preferred cloud.

Pulumi’s open source, infrastructure as code SDK lets you build and deploy Kubernetes and cloud infrastructure with TypeScript/JavaScript, Python, Go, Java, .NET, and YAML. The main benefits include:

* **Programming Languages:** Define infrastructure as code in your favorite language instead of domain-specific languages or clicking through cloud consoles.

* **Cloud Native Ecosystem Support:** Use Helm charts and native Kubernetes API objects, including integrated Kustomize support, to deploy workloads to your Kubernetes cluster.

* **Fast, Easy Deployment:** Quickly deploy your Kubernetes cluster and associated infrastructure with the CLI, with a [GitOps workflow](/docs/guides/continuous-delivery/pulumi-kubernetes-operator/), or from a CI/CD workflow.

* **Rapid Development:** Author, version, test, and release cluster and infrastructure changes just like software.

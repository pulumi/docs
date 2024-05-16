---
title_tag: Templates for Deploying Kubernetes Clusters
title: "Kubernetes Cluster Templates"
layout: overview
description: Pulumi program templates are the fastest way to deploy Kubernetes clusters and their associated infrastructure on AWS, Azure, or Google Cloud Platform. Templates come with predefined infrastructure as code so you can get started instantly.
meta_desc: Easily deploy Kubernetes clusters and their associated infrastructure on AWS, Azure, or Google Cloud Platform with Pulumi K8s templates.
meta_image: meta.png
weight: 98
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

* **Fast, Easy Deployment:** Quickly deploy your Kubernetes cluster and associated infrastructure with the CLI, with a [GitOps workflow](/docs/using-pulumi/continuous-delivery/pulumi-kubernetes-operator/), or from a CI/CD workflow.

* **Rapid Development:** Author, version, test, and release cluster and infrastructure changes just like software.

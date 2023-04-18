---
title: Kubernetes Getting Started
h1: Get Started with Kubernetes
meta_desc: This page provides an overview and guide on how to get started with Kubernetes.
linktitle: Kubernetes
weight: 1
menu:
  getstarted:
    identifier: kubernetes
    weight: 2

aliases: ["/docs/quickstart/kubernetes/"]
---

Pulumi's Cloud Native SDK makes it easy to target any Kubernetes environment to
provision a cluster, configure and deploy applications, and update them as
required.

Pulumi supports programming against Kubernetes---Minikube, on-premises and
cloud-hosted custom Kubernetes clusters, and the managed services from Google
(GKE), Azure (AKS), and Amazon (EKS). The Pulumi Kubernetes provider
packages and CLI help you accomplish all these within minutes.

For a quick example of how Pulumi deploys infrastructure on Kubernetes, this tutorial takes you through the following steps to easily deploy an [NGINX](https://www.nginx.com/) web server:

1. Setting up and configuring Pulumi to access your Kubernetes cluster.
1. Creating a new Pulumi project.
1. Deploying NGINX on Kubernetes.
1. Creating a service to access the NGINX deployment.
1. Cleaning up your deployment by destroying the resources you've provisioned.

{{< get-started-stepper >}}

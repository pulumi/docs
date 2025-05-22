---
title_tag: Get Started with Kubernetes
meta_desc: This page provides an overview and guide on how to get started with Kubernetes.
title: Get started
h1: Get Started with Kubernetes
menu:
    iac:
        name: Kubernetes
        parent: iac-get-started
        weight: 4
    clouds:
        identifier: kubernetes-get-started
        parent: kube
        weight: 4
aliases:
    - /docs/quickstart/kubernetes/
    - /docs/get-started/kubernetes/
    - /docs/clouds/kubernetes/get-started/
    - /docs/iac/get-started/kubernetes/
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

Before you begin, watch this overview of how to deploy Kubernetes infrastructure with Pulumi:

<div class="rounded-md shadow border border-gray-300 w-3/4 mx-auto my-4" style="position: relative; padding-bottom: 40.25%; height: 0; overflow: hidden;">
    <iframe
        src="//www.youtube.com/embed/2P8JLgAc5QI?rel=0"
        style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border:0;"
        allowfullscreen=""
        title="Getting Started with Kubernetes and Pulumi: Deploy Amazon EKS in 5 minutes">
    </iframe>
</div>

{{< get-started-stepper >}}

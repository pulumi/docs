---
title: Next Steps | Kubernetes
h1: Next Steps
linktitle: Next Steps
meta_desc: This page provides a list of tutorials that take a deeper dive into Kubernetes
           across all major cloud providers.
weight: 11
menu:
  getstarted:
    parent: kubernetes
    identifier: kubernetes-next-steps

aliases: ["/docs/quickstart/kubernetes/next-steps/"]
---

We've seen how to quickly get started using Kubernetes with Pulumi.

From here, you can dive deeper with additional tutorials:

## Clusters

The following tutorials are focused on creating managed Kubernetes clusters
across the major cloud providers.

- [AWS EKS - Hello World!]({{< relref "/docs/tutorials/kubernetes/eks" >}})
- [Azure AKS - Hello World!]({{< relref "/docs/tutorials/kubernetes/aks" >}})
- [Google Cloud GKE - Hello World!]({{< relref "/docs/tutorials/kubernetes/gke" >}})

## Workloads

The following tutorials are focused on deploying app workloads to running Kubernetes clusters, managed or self-managed.

1. [Hello, World!]({{< relref "/docs/tutorials/kubernetes/exposed-deployment" >}})
2. [Deploying the WordPress Helm Chart]({{< relref "/docs/tutorials/kubernetes/wordpress-chart" >}})
3. [Guestbook App with Redis and Nginx]({{< relref "/docs/tutorials/kubernetes/guestbook" >}})
4. [Graceful App Rollout]({{< relref "/docs/tutorials/kubernetes/configmap-rollout" >}})
5. [Gating rollout on Prometheus checks]({{< relref "/docs/tutorials/kubernetes/p8s-rollout" >}})
6. [Run a Stateless App Deployment]({{< relref "/docs/tutorials/kubernetes/stateless-app" >}})

{{< get-started-stepper >}}

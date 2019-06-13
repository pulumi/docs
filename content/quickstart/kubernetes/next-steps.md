---
title: Next Steps
weight: 11
menu:
  quickstart:
    parent: kubernetes
    identifier: kubernetes-next-steps
---

We've seen how to quickly get started using Kubernetes with Pulumi.

From here, you can dive deeper with additional tutorials:

## Clusters

The following tutorials are focused on creating managed Kubernetes clusters
across the major cloud providers.

- [AWS EKS - Hello World!]({{< relref "/reference/tutorials/kubernetes/tutorial-eks" >}})
- [Azure AKS - Hello World!]({{< relref "/reference/tutorials/kubernetes/tutorial-aks" >}})
- [Google Cloud GKE - Hello World!]({{< relref "/reference/tutorials/kubernetes/tutorial-gke" >}})

## Workloads

The following tutorials are focused on deploying app workloads to running Kubernetes clusters, managed or self-managed.

1. [Hello, World!]({{< relref "/reference/tutorials/kubernetes/tutorial-exposed-deployment" >}})
2. [Deploying the WordPress Helm Chart]({{< relref "/reference/tutorials/kubernetes/tutorial-wordpress-chart" >}})
3. [Guestbook App with Redis and Nginx]({{< relref "/reference/tutorials/kubernetes/tutorial-guestbook" >}})
4. [Graceful App Rollout]({{< relref "/reference/tutorials/kubernetes/tutorial-configmap-rollout" >}})
5. [Gating rollout on Prometheus checks]({{< relref "/reference/tutorials/kubernetes/tutorial-p8s-rollout" >}})
6. [Run a Stateless App Deployment]({{< relref "/reference/tutorials/kubernetes/tutorial-stateless-app" >}})

{{< get-started-stepper >}}

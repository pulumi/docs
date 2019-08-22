---
title: "Kubernetes"
menu:
  userguides:
    parent: tutorials
    weight: 4

aliases: ["/docs/reference/tutorials/kubernetes/"]
---

{{< get-started-note >}}

Additionally, there are several tutorials available to follow:

## Clusters

The following tutorials are focused on creating managed Kubernetes clusters
across the major cloud providers.

- [AWS EKS - Hello World!]({{< relref "/docs/tutorials/kubernetes/eks" >}})
- [Google Cloud GKE - Hello World!]({{< relref "/docs/tutorials/kubernetes/gke" >}})
- [Azure AKS - Hello World!]({{< relref "/docs/tutorials/kubernetes/aks" >}})

## Workloads

The following tutorials are focused on deploying app workloads to running Kubernetes clusters, managed or self-managed.

1. [Hello, World!]({{< relref "/docs/tutorials/kubernetes/exposed-deployment" >}})
2. [Deploying the WordPress Helm Chart]({{< relref "/docs/tutorials/kubernetes/wordpress-chart" >}})
3. [Guestbook App with Redis and Nginx]({{< relref "/docs/tutorials/kubernetes/guestbook" >}})
4. [Graceful App Rollout]({{< relref "/docs/tutorials/kubernetes/configmap-rollout.md" >}})
5. [Gating rollout on Prometheus checks]({{< relref "/docs/tutorials/kubernetes/p8s-rollout" >}})
6. [Run a Stateless App Deployment]({{< relref "/docs/tutorials/kubernetes/stateless-app" >}})
7. [EKS - Migrating Node Groups with Zero Downtime]({{< relref "/docs/tutorials/kubernetes/eks-migrate-nodegroups" >}})

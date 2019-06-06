---
title: Introduction
menu:
  quickstart:
    parent: kubernetes
    identifier: kubernetes-using-pulumi
    weight: 1
---

## Using Pulumi

Pulumi can be used with Kubernetes in many ways. Users can:

-   Provision a managed Kubernetes cluster on a cloud provider.
-   Provision the IaaS resources for a self-managed Kubernetes cluster.
-   Create Kubernetes API resources and deploy app workloads to any existing Kubernetes cluster (managed or
    self-managed) with only a `kubeconfig` required.

If you have already provisioned a Kubernetes cluster and have set up `kubectl`
to connect to it, the Pulumi CLI should "just work" transparently out of the box
after importing the [`pulumi/kubernetes`][pulumi-k8s] package into your program.

Pulumi supports any Kubernetes version that is currently supported by 
Kubernetes [upstream][upstream].

## Why Pulumi?

In addition to being compatible with all existing Kubernetes workflows, Pulumi provides several
advantages:

-   **Drop-in replacement for kubectl or Helm.** For workload orchestration and deployments to a running cluster, Pulumi is used instead of the typical Kubernetes deployment tools. See
    the [FAQ][faq] for more detail.
-   **Proactive reports of errors if resource initialization fails.** If Pulumi understands why a
    resource failed to become healthy, it will tell you at provisioning time -- no more guesswork
    with `kubectl get`.
-   **Drift detection.** Pulumi's strong diffing features mean that it is easy to detect when a
    resource is out of sync with the spec in version control.
-   **Precise lifecycle tracking.** Pulumi's planning phase tells you explicitly which resources
    will be deleted. No more accidentally destroying resources with `kubectl apply --prune`.
-   **End-to-end planning.** Unlike `kubectl diff`, Pulumi's planning features will show you how a
    change ripples through the app. For example, which `Pods` will change when we update a
    `ConfigMap`.
-   **Strong integration with managed Kubernetes offerings.** Pulumi exposes SDKs for major cloud
    providers, so it is easy to provision a managed Kubernetes cluster (_e.g._, [Elastic Kubernetes
    Service (EKS)][eks] on AWS), and in the same page of code, deploy Kubernetes resources into that
    cluster.
-   **Powerful integration with public cloud resources.** Because Pulumi exposes an SDK for major
    cloud providers, we will see that it takes an order of magnitude fewer lines of code to
    reference a managed database (_e.g._, [Aurora][aurora] on AWS) vs. other infrastructure-as-code
    solutions.
-   **And more!**

Check out [Pulumi: A Better Way to Kubernetes][better-way-to-k8s] for details!

[upstream]: https://kubernetes.io/docs/reference/
[eks]: https://aws.amazon.com/eks/
[faq]: {{< relref "/quickstart/kubernetes/faq" >}}
[gcp]: {{< relref "/quickstart/gcp" >}}
[kubeconfig]: https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/
[gke-tutorial]: {{< relref "/tutorial-gke" >}}
[eks-tutorial]: {{< relref "/tutorial-eks" >}}
[aks-tutorial]: {{< relref "/tutorial-azure-kubernetes-service" >}}
[eks]: https://aws.amazon.com/eks/
[aurora]: https://aws.amazon.com/rds/aurora/
[pulumi-k8s]: https://github.com/pulumi/pulumi-kubernetes
[better-way-to-k8s]: https://blog.pulumi.com/pulumi-a-better-way-to-kubernetes

---
title: Kubernetes Introduction
meta_desc: This page provides an introduction to Kubernetes and how Pulumi can help provision and manage
           Kubernetes resources.
aliases: ["/docs/reference/clouds/kubernetes/introduction/"]
---

## Using Pulumi

Pulumi can be used with Kubernetes in many ways. Users can:

- Provision a managed Kubernetes cluster on a cloud provider.
- Provision the IaaS resources for a self-managed Kubernetes cluster.
- Create Kubernetes API resources and deploy app workloads to any existing Kubernetes cluster (managed or
    self-managed) with only a `kubeconfig` required.

If you have already provisioned a Kubernetes cluster and have set up `kubectl`
to connect to it, the Pulumi CLI should "just work" transparently out of the box
after importing the [`pulumi/kubernetes`][pulumi-k8s] package into your program.

Pulumi supports any Kubernetes version that is currently supported by
Kubernetes [upstream][upstream].

## Why Pulumi?

In addition to being compatible with all existing Kubernetes workflows, Pulumi provides several
advantages:

- **A great complement to kubectl.** `kubectl` is the standard for cluster operations in Kubernetes. However, `kubectl` is user-driven in certain uses (e.g. `get`, `describe`), and server-driven in others (e.g. `apply`). Pulumi excels at workload orchestration, API resource lifecycle management, and [cluster management][cluster-management] by providing rich diffs and deterministic Infrastructure-as-Code primitives. Pulumi takes the guesswork out of updates with comprehensive previews of planned changes, and controlled rollouts that use a [create-before-replace][create-before-replace] / blue-green deployment strategy. See the Kubernetes [FAQ][faq], and the Pulumi [Programming Model][programming-model] for more detail.
- **Proactive reports of errors if resource initialization fails.** If Pulumi understands why a
    resource failed to become healthy, it will tell you at provisioning time -- no more guesswork
    with `kubectl get`.
- **Drift detection.** Pulumi's strong diffing features mean that it is easy to detect when a
    resource is out of sync with the spec in version control.
- **Precise lifecycle tracking.** Pulumi's planning phase tells you explicitly which resources
    will be deleted. No more accidentally destroying resources with `kubectl apply --prune`.
- **End-to-end planning.** Unlike `kubectl diff`, Pulumi's planning features will show you how a
    change ripples through the app. For example, which `Pods` will change when we update a
    `ConfigMap`.
- **Strong integration with managed Kubernetes offerings.** Pulumi exposes SDKs for major cloud
    providers, so it is easy to provision a managed Kubernetes cluster (_e.g._, [Elastic Kubernetes
    Service (EKS)][eks] on AWS), and in the same page of code, deploy Kubernetes resources into that
    cluster.
- **Powerful integration with public cloud resources.** Because Pulumi exposes an SDK for major
    cloud providers, we will see that it takes an order of magnitude fewer lines of code to
    reference a managed database (_e.g._, [Aurora][aurora] on AWS) vs. other infrastructure-as-code
    solutions.
- **And more!**

Check out [Pulumi: A Better Way to Kubernetes][better-way-to-k8s] for details!

<!-- markdownlint-disable url -->
[upstream]: https://kubernetes.io/docs/reference/
[eks]: https://aws.amazon.com/eks/
[faq]: {{< relref "/docs/intro/cloud-providers/kubernetes/faq" >}}
[gcp]: {{< relref "/docs/get-started/gcp" >}}
[kubeconfig]: https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/
[gke-tutorial]: {{< relref "/docs/tutorials/kubernetes/gke" >}}
[eks-tutorial]: {{< relref "/docs/tutorials/kubernetes/eks" >}}
[aks-tutorial]: {{< relref "/docs/tutorials/kubernetes/aks" >}}
[eks]: https://aws.amazon.com/eks/
[aurora]: https://aws.amazon.com/rds/aurora/
[pulumi-k8s]: https://github.com/pulumi/pulumi-kubernetes
[better-way-to-k8s]: {{< relref "pulumi-a-better-way-to-kubernetes" >}}
[create-before-replace]: {{< relref "/docs/intro/concepts/resources#autonaming" >}}
[programming-model]: {{< relref "/docs/intro/concepts" >}}
[cluster-management]: {{< relref "/docs/tutorials/kubernetes#clusters" >}}
<!-- markdownlint-enable url -->

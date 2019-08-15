---
title: Kubernetes
menu:
  intro:
    parent: clouds-and-languages
    identifier: clouds-kubernetes
---

<img src="/logos/tech/k8s.svg" align="right" class="h-16 px-8 pb-4">

[Kubernetes][k8s] is an open source project for running and managing containerized applications
on a cluster of machines.

[Pulumi]({{< relref "/docs/quickstart" >}}) is an infrastructure-as-code tool that exposes the Kubernetes resource API as an
SDK, alongside other SDKs which span common cloud native utilities, cloud
provider IaaS offerings, and their catalog of services - managed Kubernetes included.

<center><img src="/images/docs/quickstart/kubernetes/cake.svg" width="670"></center>

The various SDK's allow Kubernetes users to leverage Pulumi for novel forms of cluster
management, and deployment of app workloads to clusters. Users of
Kubernetes and Pulumi can:

-  Instantiate IaaS resources and managed services from any cloud.
-  Provision managed Kubernetes clusters from the major cloud providers.
-  Provision self-managed (open source) Kubernetes clusters on top of raw IaaS resources or on-prem virtualization providers.
-  Create and orchestrate Kubernetes API resources for app workloads, in the programming language of their choice.
-  Manage real code instead of YAML, JSON, DSL's, or tar archives of templates.
-  Apply standard software development practices to Kubernetes applications, including the use of functions, classes, loops, conditionals, etc.
-  Increase productivity using the power of dev tools such as IDE auto-completion, type &
   error checking, linting, refactoring, and testing frameworks to validate Kubernetes clusters, app workloads, or both.

## Getting Started

The quickest way to get started with Kubernetes is to follow the [Get Started]({{< relref "/docs/quickstart/kubernetes" >}}) guide.

## Library Packages

#### For Cluster Management

The following SDKs are available to work with IaaS resources, and managed or self-managed Kubernetes clusters:

-   AWS: [`pulumi/aws`](https://github.com/pulumi/aws), [`pulumi/awsx`](https://github.com/pulumi/pulumi-awsx), [`pulumi/eks`](https://github.com/pulumi/eks)
-   GCP: [`pulumi/gcp`](https://github.com/pulumi/gcp)
-   Azure: [`pulumi/azure`](https://github.com/pulumi/pulumi-azure)

#### For Workload Management

The [`pulumi/kubernetes`](https://github.com/pulumi/pulumi-kubernetes) SDK is available to work with, and deploy app workloads to running Kubernetes clusters:

-   JavaScript/TypeScript: [npm](https://www.npmjs.com/package/@pulumi/kubernetes)
-   Python: [PyPI](https://pypi.org/project/pulumi-kubernetes/)
-   Go: Planned

## Menu

- [Introduction]({{< relref "introduction.md" >}})
- [Setup]({{< relref "setup.md" >}})
- [FAQ]({{< relref "faq.md" >}})
- [Tutorials]({{< relref "/docs/reference/tutorials/kubernetes/_index.md" >}})

[k8s]: https://kubernetes.io

---
title: Kubernetes Overview
meta_desc: This page provides an overview of how Pulumi works with Kubernetes.
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-kubernetes
    weight: 1

aliases: ["/docs/reference/clouds/kubernetes/"]
---

<img src="/logos/tech/k8s.svg" align="right" class="h-16 px-8 pb-4">

[Kubernetes][k8s] is an open source project for running and managing containerized applications
on a cluster of machines.

[Pulumi]({{< relref "/docs/get-started" >}}) is an infrastructure-as-code tool that exposes the Kubernetes resource API as an
SDK, alongside other SDKs which span common cloud native utilities, cloud
provider IaaS offerings, and their catalog of services - managed Kubernetes included.

<a href="/images/docs/quickstart/kubernetes/cake.svg">
<img src="/images/docs/quickstart/kubernetes/cake.svg">
</a>

## Use Cases

The various SDKs allow Kubernetes users to leverage Pulumi for novel forms of cluster
management, and deployment of app workloads to clusters. Users of
Kubernetes and Pulumi can:

- Instantiate IaaS resources and managed services from any cloud.
- Provision managed Kubernetes clusters from the major cloud providers.
- Provision self-managed (open source) Kubernetes clusters on top of raw IaaS resources or on-prem virtualization providers.
- Create and orchestrate Kubernetes API resources for app workloads, in the programming language of their choice.
- Manage real code instead of YAML, JSON, DSL's, or tar archives of templates.
- Apply standard software development practices to Kubernetes applications, including the use of functions, classes, loops, conditionals, etc.
- Increase productivity using the power of dev tools such as IDE auto-completion, type &
   error checking, linting, refactoring, and testing frameworks to validate Kubernetes clusters, app workloads, or both.

## Getting Started

The quickest way to get started with Kubernetes is to follow the [Get Started]({{< relref "/docs/get-started/kubernetes" >}}) guide.

## Library Packages

### For Cluster Management

The following SDKs are available to work with IaaS resources, and managed or self-managed Kubernetes clusters.

The packages are available in Node.js (Javascript and Typescript), Python, Go, and .NET.

- AWS: [`pulumi/aws`](https://github.com/pulumi/aws)
- Azure: [`pulumi/azure`](https://github.com/pulumi/pulumi-azure)
- DigitalOcean: [`pulumi/digitalocean`](https://github.com/pulumi/pulumi-digitalocean)
- GCP: [`pulumi/gcp`](https://github.com/pulumi/gcp)

#### Extension Packages

- [`pulumi/awsx`](https://github.com/pulumi/pulumi-awsx) - AWS Extensions
- [`pulumi/eks`](https://github.com/pulumi/eks) - Manage EKS clusters

### For Workload Management

The [`pulumi/kubernetes`](https://github.com/pulumi/pulumi-kubernetes) SDK is available to work with, and deploy app workloads to running Kubernetes clusters:

- JavaScript/TypeScript: [npm](https://www.npmjs.com/package/@pulumi/kubernetes)
- Python: [PyPI](https://pypi.org/project/pulumi-kubernetes/)
- Go:
  - Import package: `github.com/pulumi/pulumi-kubernetes/sdk/v2/go/kubernetes`
  - [GitHub](https://github.com/pulumi/pulumi-kubernetes/tree/master/sdk/go/kubernetes)
- .NET: [`Pulumi.Kubernetes`](https://www.nuget.org/packages/Pulumi.Kubernetes)

#### Extension Packages

- [`pulumi/kx`](https://github.com/pulumi/eks) - Kubernetes Workload Extensions

[k8s]: https://kubernetes.io

## Crosswalk for Kubernetes

<a href="{{< relref "./" >}}">
    <img src="/images/docs/reference/crosswalk/kubernetes/crosswalk-for-k8s.svg" align="right" width="280" style="margin: 0 0 32px 16px;">
</a>

[Pulumi Crosswalk for Kubernetes][crosswalk-k8s] is a collection of industry standard
best-practices for managing Kubernetes, and its infrastructure in production.

[Get started][crosswalk-control-plane] by deploying stacks of infrastructure architected to enable teams
to run and manage Kubernetes in production.

[crosswalk-control-plane]: {{< relref "/docs/guides/crosswalk/kubernetes/control-plane" >}}
[crosswalk-k8s]: {{< relref "/docs/guides/crosswalk/kubernetes" >}}
[prod-arch-for-teams]: {{< relref "/docs/guides/crosswalk/kubernetes" >}}

## Pulumi Kubernetes Operator

<a href="{{< relref "./" >}}">
    <img src="/logos/tech/ci-cd/kubernetes.png" align="right" width="150" style="margin: 0 0 32px 16px;">
</a>

The [Pulumi Kubernetes Operator][k8s-operator] is an [extension pattern][k8s-ext-pattern] that
enables Kuberentes users to create a `Stack` as a first-class API
resource, and use the `StackController` to drive the updates of the Stack until
success.

Deploying [Pulumi Stacks][stack] in Kubernetes provides the capability to build
out CI/CD and automation systems into your clusters, creating native support to manage your infrastructure alonside your Kubernetes workloads.

[Get started][k8s-operator-cicd] with the Pulumi Kubernetes Operator in your CI/CD pipelines.

[k8s-operator]: https://github.com/pulumi/pulumi-kubernetes-operator
[k8s-ext-pattern]: https://kubernetes.io/docs/concepts/extend-kubernetes/operator/
[stack]: {{< relref "/docs/intro/concepts/stack" >}}
[k8s-operator-cicd]: {{< relref "/docs/guides/continuous-delivery/pulumi-kubernetes-operator" >}}

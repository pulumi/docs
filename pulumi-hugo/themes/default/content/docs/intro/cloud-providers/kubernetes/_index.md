---
title: Kubernetes
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

## Pulumi Kubernetes Provider

The Kubernetes provider for Pulumi can be used to provision any resources available in the Kubernetes API.  The Kubernetes provider must be configured with a `kubeconfig` or other credentials to connect to a taret Kubernetes cluster.

See the [full API documentation]({{< relref "/docs/reference/pkg/kubernetes" >}}) for complete details of the available Kubernetes provider APIs.

### Setup

The Kubernetes provider supports several options for providing access to a Kubernetes cluster.  See the [Kubernetes setup page]({{< relref "/docs/intro/cloud-providers/kubernetes/setup" >}}) for details.

### Getting Started

The quickest way to get started with Kubernetes is to follow the [Get Started]({{< relref "/docs/get-started/kubernetes" >}}) guide.

Additional Kubernetes tutorials are available covering:

- [Clusters]({{< relref "/docs/tutorials/kubernetes#clusters" >}}) on AWS, Azure and GCP
- [Workloads]({{< relref "/docs/tutorials/kubernetes#workloads" >}}) including Guestbook, Helm Charts, Stateless Apps, and more
- [Day Two Tasks]({{< relref "/docs/tutorials/kubernetes#day-two-tasks" >}}) including gated deployments and zero downtime upgrades
- And [many more]({{< relref "/docs/tutorials/kubernetes#other-examples-and-tutorials" >}}) examples and tutorials

### Libraries

The following packages are available in package managers:

- JavaScript/TypeScript: [`@pulumi/kubernetes`](https://www.npmjs.com/package/@pulumi/kubernetes)
- Python: [`pulumi-kubernetes`](https://pypi.org/project/pulumi-kubernetes/)
- Go: [`github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes`](https://github.com/pulumi/pulumi-kubernetes)
- .NET: [`Pulumi.Kubernetes`](https://www.nuget.org/packages/Pulumi.Kubernetes)

The Kubernetes provider is open source and available in the [pulumi/pulumi-kubernetes](https://github.com/pulumi/pulumi-kubernetes) repo.

### Configuration

The Kubernetes provider accepts the following configuration settings.  These can be provided to the default Kubernetes provider via `pulumi config set kubernetes:<option>`, or passed to the constructor of `new kubernetes.Provider` to construct a specific instance of the Kubernetes provider.

- `cluster`: (Optional) If present, the name of the kubeconfig cluster to use.
- `context`: (Optional) If present, the name of the kubeconfig context to use.
- `enableDryRun`: (Optional) BETA FEATURE - If present and set to true, enable server-side diff calculations. This feature is in developer preview, and is disabled by default. This config can be specified in the following ways, using this precedence: (1) this `enableDryRun` parameter or (2) the `PULUMI_K8S_ENABLE_DRY_RUN` environment variable.
- `kubeconfig`: (Optional) The contents of a kubeconfig file. If this is set, this config will be used instead of `$KUBECONFIG`.
- `namespace`: (Optional) The contents of a kubeconfig file. If this is set, this config will be used instead of `$KUBECONFIG`.
- `renderYamlToDirectory`: (Optional) BETA FEATURE - If present, render resource manifests to this directory. In this mode, resources will not be created on a Kubernetes cluster, but the rendered manifests will be kept in sync with changes to the Pulumi program. This feature is in developer preview, and is disabled by default. Note that some computed Outputs such as status fields will not be populated since the resources are not created on a Kubernetes cluster. These Output values will remain undefined,
and may result in an error if they are referenced by other resources. Also note that any secret values
used in these resources will be rendered in plain text to the resulting YAML.
- `suppressDeprecationWarnings`: (Optional) If present and set to true, suppress `apiVersion` deprecation warnings from the CLI. This config can be specified in the following ways, using this precedence: (1) this `suppressDeprecationWarnings` parameter or (2) the `PULUMI_K8S_SUPPRESS_DEPRECATION_WARNINGS` environment variable.

### Annotations

A few Pulumi-specific annotations can be applied to Kubernetes resources managed by Pulumi to control aspects of how Pulumi deploys and manages the Kubernetes resource:

- `pulumi.com/skipAwait`: Disables Pulumi's default await logic that waits for a Kubernetes resource to become "ready" before marking the resource as having created or updated succesfully.
- `pulumi.com/timeoutSeconds`: Specifies the number of seconds that the Pulumi Kubernetes provider will wait for the resource to become "ready".

In addition, the Pulumi provider may write the following annotations onto resources it manages:

- `pulumi.com/autonamed`: Indicates that the Pulumi Kubernetes provider decided to autoname the resource (instead of using an explicitly provided `metadata.name`).

## Additional Pulumi Packages for Kubernetes Users

### For Cluster Management

The following SDKs are available to work with IaaS resources, and managed or self-managed Kubernetes clusters.

The packages are available in Node.js (Javascript and Typescript), Python, Go, and .NET.

- AWS: [`pulumi/aws`](https://github.com/pulumi/aws)
- Azure: [`pulumi/azure-native`](https://github.com/pulumi/pulumi-azure-native)
- DigitalOcean: [`pulumi/digitalocean`](https://github.com/pulumi/pulumi-digitalocean)
- Google Cloud: [`pulumi/gcp`](https://github.com/pulumi/gcp)

#### Extension Packages

- [`pulumi/awsx`](https://github.com/pulumi/pulumi-awsx) - AWS Extensions
- [`pulumi/eks`](https://github.com/pulumi/eks) - Manage EKS clusters

### For Workload Management

The [`pulumi/kubernetes`](https://github.com/pulumi/pulumi-kubernetes) SDK is available to work with, and deploy app workloads to running Kubernetes clusters:

- JavaScript/TypeScript: [npm](https://www.npmjs.com/package/@pulumi/kubernetes)
- Python: [PyPI](https://pypi.org/project/pulumi-kubernetes/)
- Go:
  - Import package: `github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes`
  - [GitHub](https://github.com/pulumi/pulumi-kubernetes/tree/master/sdk/go/kubernetes)
- .NET: [`Pulumi.Kubernetes`](https://www.nuget.org/packages/Pulumi.Kubernetes)

#### Extension Packages

- [`pulumi/kx`](https://github.com/pulumi/pulumi-kubernetesx) - Kubernetes Workload Extensions

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
out CI/CD and automation systems into your clusters, creating native support to manage your infrastructure alongside your Kubernetes workloads.

[Get started][k8s-operator-cicd] with the Pulumi Kubernetes Operator in your [continuous delivery][pulumi-cd] pipelines.

[k8s-operator]: https://github.com/pulumi/pulumi-kubernetes-operator
[k8s-ext-pattern]: https://kubernetes.io/docs/concepts/extend-kubernetes/operator/
[stack]: {{< relref "/docs/intro/concepts/stack" >}}
[k8s-operator-cicd]: {{< relref "/docs/guides/continuous-delivery/pulumi-kubernetes-operator" >}}
[pulumi-cd]: {{< relref "/docs/guides/continuous-delivery" >}}

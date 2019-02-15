---
title: Kubernetes
redirect_from: /reference/kubernetes.html
---

<img src="/images/quickstart/k8s-purple.png" align="right">

[Kubernetes][k8s] is an open source platform for running containerized applications on a cluster of
machines. Applications are managed through a RESTful API that exposes mechanisms to deploy, scale,
and introspect on resources in the cluster.

Pulumi is an infrastructure-as-code tool that exposes a Kubernetes SDK that allows users to write
Kubernetes applications in the language of their choice, such as JavaScript and Python. It is
designed to fit in anywhere you already use Kubernetes:

-   **API-compatible with Kubernetes** -- users do not have to learn a new API to write Kubernetes
    applications with Pulumi. (See the [Kubernetes][api-reference] and
    [Pulumi](/reference/pkg/nodejs/@pulumi/kubernetes/index.html) API documentation for more
    details.)
-   **Compatible with Kubernetes YAML and Helm Charts.** For example:
    ```typescript
    import * as k8s as "@pulumi/kubernetes";
    new k8s.yaml.ConfigFile("app.yaml");
    ```
-   **Drop-in replacement for `kubectl apply`.** Anywhere you have a [kubeconfig file][kubeconfig],
    you can use Pulumi.

The remainder of this document will demonstrate how to use Pulumi for Kubernetes development, as
illustrated through a series of use cases and tutorials.

> **Note:** Pulumi supports any Kubernetes version that is currently supported by Kubernetes
> upstream. Typically a Kubernetes minor release is supported by upstream for a 9 month window, with
> all supported versions being listed in [the reference docs][reference]. If you have a more
> specific version requirement, please contact us.

## Why Pulumi?

In addition to being compatible with all existing Kubernetes workflows, Pulumi provides several
advantages over bare `kubectl`. In the course of these tutorials, we will see:

-   **Proactive reports of errors if resource initialization fails.** If Pulumi understands why a
    resource failed to become healthy, it will tell you at provisioning time -- no more guesswork
    with `kubectl get`.
-   **Drift detection.** Pulumi's strong diffing features mean that it is easy to detect when a
    resource is out of sync with the spec in version control.
-   **Precise lifecycle tracking.** Pulumi's planning phase tells you explicitly which resources
    will be deleted. No more accidentally destroying resources with `kubectl apply --prune`.
-   **End-to-end planning.** Unlike `kubectl diff`, Pulumi's planning features will show you how a
    change ripples through the app. For example, which `Pod`s will change when we update a
    `ConfigMap`.
-   **Strong integration with managed Kubernetes offerings.** Pulumi exposes SDKs for major cloud
    providers, so it is easy to provision a managed Kubernetes cluster (_e.g._, [Elastic Kubernetes
    Service (EKS)][eks] on AWS), and in the same page of code, deploy Kubernetes resources to that
    cluster.
-   **Powerful integration with public cloud resources.** Because Pulumi exposes an SDK for major
    cloud providers, we will see that it takes an order of magnitude fewer lines of code to
    reference a managed database (_e.g._, [Aurora][aurora] on AWS) vs. other infrastructure-as-code
    solutions.
-   **And more!**

## Using Pulumi

Kubernetes applications can be deployed in one of two ways. We will split tutorials along these
lines:

-   **Using an existing cluster and [kubeconfig file][kubeconfig].** Pulumi works anywhere `kubectl`
    works -- it uses the official Kubernetes Go client under the hood.
-   **Using a Kubernetes cluster manged by Pulumi.** Pulumi makes it easy to provision a managed
    Kubernetes cluster (_e.g._, Google Kubernetes Engine via the Pulumi [Google Cloud Platform][gcp]
    SDK), and then to provision Kubernetes resources onto that cluster, all in the same code.

### Prerequisites

-   Install [Node.js][nodejs] version 6 or later.
-   Install a package manager for Node.js, such as [npm] or [Yarn].
-   Follow the directions [here][install] to install the Pulumi CLI.

<!-- By default, Pulumi uses the same configuration as `kubectl`, so if you're already connected to a cluster, Pulumi will
"just work." For more details, including this initial setup, please see the [Kubernetes setup page](./setup.html). -->

### Using an existing cluster

It is possible to use the Pulumi Kubernetes SDK entirely by itself, using a pre-provisioned cluster.
These tutorials focus on this scenario. You will need:

-   An existing Kubernetes cluster
-   A [kubeconfig][kubeconfig] file in an appropriate location.

Any cluster that is reachable from `kubectl` should work. If you do not have both of these things,
you can obtain them by following [this guide](https://pulumi.io/quickstart/kubernetes/setup.html).

The tutorials are:

-   **[New to Pulumi]** [Getting started with Pulumi.](./tutorial-configmap-rollout.html) This
    application shows the basics of managing a Kubernetes application with Pulumi. We will see how
    Pulumi's diffing and planning features makes it easy to understand the blast radius of a change.
    We will also see how Pulumi proactively presents information about resources that fail to
    initialize during a rollout.
-   **[New to Pulumi]** ["Adopting" a Helm Chart](./tutorial-wordpress-chart.html).
    This tutorial deploys a simple Helm Chart on a Kubernetes cluster.

### Using a cluster provisioned by Pulumi

It is also possible to provision a managed Kubernetes cluster (_e.g._, [EKS][eks] on AWS), and then
provision a Kubernetes application on top of the managed cluster. These examples apply to various
clouds, so there is not a common "Prerequisites" section, except what you've already done to set up
Pulumi.

-   **[Advanced Pulumi user]** [Standing up an AKS cluster, Mongo-flavored CosmosDB, and a Helm
    Chart that uses it for persistent data storage.](./tutorial-p8s-rollout.html) This tutorial is
    similar in flavor to the lifecycle tutorial, except rollouts are staged, gated on Prometheus
    health checks. This allows us to roll out to a small canary ring, check Prometheus metrics, and
    then roll out to a larger prod ring only when that succeeds.

## Kubernetes the Prod Way

[Kubernetes the Prod Way](/quickstart/k8s-the-prod-way/index.html) is a tutorial aimed at users
looking for guidance on how to set up a Kubernetes cluster for production workloads, including
identity, managed infrastructure (_e.g._, databases, Kubernetes clusters).

## Examples

You can find additional examples Kubernetes examples in [the Pulumi examples
repo](https://github.com/pulumi/examples).

<!-- -   **[New to Kubernetes & Pulumi]** [Getting started with Kubernetes.](./tutorial-guestbook.html)
    This tutorial deploys a Pulumi-native adaptation of the canonical [Kubernetes Guestbook
    example][guestbook]. Kubernetes and exposing it to the Internet with a `Service`. In addition to
    very simple Kubernetes resource types, this example shows off several unique features of Pulumi,
    including diffing and incremental errors when deployment fails. -->

## Libraries

The following packages are available in package managers:

-   JavaScript/TypeScript: [npm](https://www.npmjs.com/package/@pulumi/kubernetes)
-   Python: [PyPI](https://pypi.org/project/pulumi-kubernetes/)

Support will eventually expand to Go as well.

## FAQ

You can find a list of frequently-asked questions [here](./faq.html).

[api-reference]: https://kubernetes.io/docs/reference/
[k8s]: https://kubernetes.io/
[wp]: https://github.com/pulumi/examples/tree/master/kubernetes-ts-helm-wordpress
[kubeconfig]: https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/
[aws]: https://pulumi.io/quickstart/aws/index.html
[azure]: https://pulumi.io/quickstart/azure/index.html
[gcp]: https://pulumi.io/quickstart/gcp/index.html
[eks]: https://aws.amazon.com/eks/
[install]: https://pulumi.io/quickstart/install.html
[nodejs]: https://nodejs.org/en/
[npm]: https://www.npmjs.com/get-npm
[yarn]: https://yarnpkg.com/en/docs/install
[aurora]: https://aws.amazon.com/rds/aurora/
[guestbook]: https://github.com/pulumi/examples/tree/master/kubernetes-ts-guestbook

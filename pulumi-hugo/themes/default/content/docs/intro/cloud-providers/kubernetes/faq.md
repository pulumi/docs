---
title: Kubernetes FAQ
meta_desc: This page provides Frequently Asked Questions about Kubernetes and Pulumi.
aliases: ["/docs/reference/clouds/kubernetes/faq/"]
---

## Does Pulumi create and manage Kubernetes clusters, or deploy workloads to running clusters?

Pulumi handles both cases, and we highly encourage you to try them together!
Pulumi's SDKs handle the various layers of infrastucture needed
to define, provision, and operate Kubernetes clusters (managed or self-managed), their underlying
dependencies, and the app workloads intended to run in-cluster.

## Is the Pulumi Kubernetes API compatible with Kubernetes resource API?

The SDK API is 100% compatible with Kubernetes resource API, and is schematically
identical to what Kubernetes users expect.

In fact, Pulumi's Kubernetes SDK are manufactured by automatically wrapping our library functionality around
the Kubernetes resource [OpenAPI spec][openapi] as soon as a new version is released!
Ultimately, this means that Pulumi users do not have to learn a new
Kubernetes API model, nor wait long to work with the latest versions available. See the [Kubernetes][api-reference] and
[Pulumi]({{< relref "/docs/reference/pkg/kubernetes" >}}) API documentation for more
details.

Notably, Pulumi also supports alpha and beta APIs.

## Does Pulumi work with my kubeconfig file?

**Yes!** Pulumi uses the official Kubernetes [client-go] library to interact
with the Kubernetes cluster. It will work pretty much anywhere `kubectl` works.

## How does Pulumi compare to kubectl?

Pulumi is intended to be a drop-in replacement for `kubectl`. Though `kubectl` and
Pulumi differ, functionally speaking, Pulumi works with
the Kubernetes API Server to accomplish the same deployment goals as
`kubectl`. Pulumi, like `kubectl`, can be used with any cluster as long as you have a [kubeconfig
file][kubeconfig].

Most users use Pulumi to manage Kubernetes resources, but still use `kubectl`'s rich commands for
examining cluster state (_e.g._, `describe`, `explain`, `get`, and so on).

The differences between the two are:

* The Pulumi CLI presents information-rich status updates, clearly showing progress as resources
   come online or fail within the cluster. `kubectl` users must manually
   retreive these updates from the cluster with repeated calls.

* Pulumi allows you to preview the effects
   a change will have on your resource configuration.

* Pulumi provides full lifecycle management (creation, deletion, replacement) of resources. If we must change an immutable
   field in an API object, `pulumi preview` alerts the user the object must be replaced.

* The primary interface to `kubectl` is YAML. Pulumi exposes a rich, multi-language SDK to create
   API resources, and additionally supports execution of Kubernetes YAML manifests and Helm charts.

* `kubectl` has a set of commands specifically meant to make it easy to understand what's happening
   in the cluster. Pulumi _only_ does API resource management.

* Pulumi has a notion of resource initialization completion, allowing resources be configured using
   values from the live object. For example, a `Deployment` might boot a database, then parse the
   connection string, then put that in a secret, then reference that secret in a `Pod`. As of
   Kubernetes v1.12, `kubectl` can also wait for resource initialization, though it only supports
   applying all resource configuration at one time.

* Pulumi makes it easy to deploy the same app workload multiple times with default [auto-naming]({{< relref "/docs/intro/concepts/programming-model#autonaming" >}}).

## How does Pulumi compare to Helm?

Helm v2 allows users to easily install pre-packaged application *charts* into a Kubernetes
cluster. Charts are parameterized by some number of values, which users can fill in to customize
their application.

* By default, Helm 2 Charts are managed by an in-cluster API server, called Tiller.
   This makes many things (_e.g._, RBAC) harder, because the API server is run
   with a single `ServiceAccount`, which typically has global read/write access to the cluster.

   Pulumi requires no server-side component.

* The Pulumi CLI presents information-rich status updates, clearly showing progress as resources
   come online.

* Pulumi allows you to preview the effects
   a change will have on your resource configuration.

* Pulumi provides full lifecycle management (creation, deletion, replacement) of resources. If we must change an immutable field in
   an API object, `pulumi preview` alerts the user the object must be replaced.

* Helm 2 parameterizes YAML templates using Go templates, a textual replacement engine. Go templates
   are not guaranteed to generate syntactically-correct YAML. Pulumi exposes a rich, multi-language
   SDK, with strong typing to catch errors, and a pre-deployment validation step to catch errors
   before you run the program.

## Can I use my existing YAML manifests and Helm Charts?

Pulumi has integration support for Kubernetes YAML manifests and Helm Charts. This
support allows users to jumpstart their Pulumi experience by
easily integrating existing Kubernetes workloads with new Pulumi
code.

### Examples

#### YAML Manifest:

```typescript
import * as k8s as "@pulumi/kubernetes";

const myapp = new k8s.yaml.ConfigFile("app", {file: "app.yaml"});
```

#### Helm Chart:

```typescript
import * as k8s as "@pulumi/kubernetes";

// Deploy a version of the stable/wordpress chart.
const wordpress = new k8s.helm.v2.Chart("wpdev", {
    repo: "stable",
    version: "2.1.3",
    chart: "wordpress"
});
```

See the [pulumi/examples][examples] repo for more details.

## Does the Pulumi Service see my credentials in the kubeconfig file?

No. Only the `pulumi` CLI tool running locally in the user's client can read the kubeconfig file or execute
resource operations on the cluster.

The service is used to coordinate multiple user updates, so they don't update the
same resources concurrently, and stores the state history of your deployments.

If you ask Pulumi to boot up a cluster (_e.g._, as our [EKS example][eks] shows), then it is
possible to retrieve a kubeconfig file _for that cluster only_. In this case, the kubeconfig file is
stored as part of the state history of rollouts -- but they are considered opaque state by the
Pulumi service. The service **never** uses these values for any reason whatsoever.

Additionally, the contents of the kubeconfig files are not sensitive for managed clusters
on the major cloud providers, as they defer authentication to their local CLIs.

## Does the Pulumi Service see my cloud provider credentials?

No. The `pulumi` CLI tool runs locally in the user's client. This allows
Pulumi to transparently rely on the underlying cloud provider's CLI and authentication
mechanisms. The service does not read, use, depend on, or store any credentials.

## Can I use Pulumi without the pulumi.com service?

Yes. The service performs several functions that are useful, such as coordinating so that
multiple users don't simultaneously update the same resources, state
checkpointing & management, webhooks, secrets management, and team auth, RBAC,
and policies.

If you do not need these features, then you can have Pulumi store the state file somewhere
else (_e.g._, in a local file, or in object storage). See documentation for [`pulumi login`][login] and [pulumi #2455](https://github.com/pulumi/pulumi/pull/2455).

<!-- markdownlint-disable url -->
[kubeconfig]: https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/
[client-go]: https://github.com/kubernetes/client-go
[login]: {{< relref "/docs/reference/cli/pulumi_login" >}}
[eks]: https://github.com/pulumi/examples/tree/master/aws-ts-eks
[api-reference]: https://kubernetes.io/docs/reference/
[openapi]: https://github.com/kubernetes/kubernetes/tree/master/api/openapi-spec
[examples]: https://github.com/pulumi/examples
<!-- markdownlint-enable url -->

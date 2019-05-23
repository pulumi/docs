---
title: Kubernetes FAQ
---

## Does Pulumi work with my [kubeconfig file][kubeconfig]?

**Yes!** Pulumi uses the official [Kubernetes Go client library][client-go]. It
will work pretty much anywhere `kubectl` works.

## Does Pulumi support the entire Kubernetes API?

**Yes!** The Pulumi SDK is generated from the Kubernetes OpenAPI spec, so anything that exists in
the Kubernetes API can be used from Pulumi. Notably, Pulumi supports even alpha and beta APIs.

## Can I use Pulumi without the pulumi.com service?

**Yes!** The service performs several functions that are useful, such as coordinating so that
multiple users don't simultaneously update the same resources.

If you don't want or need these things, then you can ask Pulumi to store the state file somewhere
else (_e.g._, in a local file). See documentation for [`pulumi login`][login].

## Does the Pulumi service use credentials in my [kubeconfig file][kubeconfig] to deploy my app?

**Never!** The `pulumi` CLI tool acts exactly like `kubectl` -- it reads the local kubeconfig file,
authenticates with the cluster, and runs some set of resource operations locally. If you set
`pulumi` up to talk to the service, it will maintain a deployment history and coordinate to make
sure that multiple users don't update the same resources simultaneously.

In general, it's safe to think of the `pulumi` CLI roughly as a replacement for the `kubectl`.
Wherever you would run `kubectl` to deploy your app (_e.g._, CI/CD), you'd run `pulumi` instead.

See also the relevant entry in the general [Pulumi FAQ](/reference/faq.html).

## Does the Pulumi service ever _see_ the cluster credentials in my [kubeconfig file][kubeconfig]?

**Never, unless you ask it to.** Only the `pulumi` CLI tool will read the kubeconfig file or execute
resource operations on the cluster. The service coordinates multiple users so they don't update the
same resources concurrently, and stores the state history of your deployments.

If you ask Pulumi to boot up a cluster (_e.g._, as our [EKS example][eks] shows), then it is
possible to retrieve a kubeconfig file _for that cluster_. In this case, the kubeconfig file is
stored as part of the state history of rollouts -- but they are considered opaque state by the
Pulumi service. The service **never** uses these values for any reason whatsoever.

## How does Pulumi relate to `kubectl`?

Most users use Pulumi to manage Kubernetes resources, but still use `kubectl`'s rich commands for
examining cluster state (_e.g._, `describe`, `explain`, `get`, and so on).

The differences in resource management are:

* Pulumi and `kubectl` both use the official [Kubernetes Go client library][client-go] to talk to do
  things like load the [kubeconfig file][kubeconfig], authenticate to the cluster, and talk to the
  API server.
* The Pulumi CLI presents information-rich status updates, giving a notion of progress as resources
  come online. `kubectl` does not.
* Pulumi has a strong notion of a "plan" -- running `pulumi preview` allows you to see what effect
  a change will have on your resource configuration. `kubectl` does not.
* Explicit notions of creation, deletion, and replacement. If we must change an immutable field in
  an API object, `pulumi preview` alerts the user the object must be replaced. `kubectl` does not.
* Pulumi exposes `pulumi preview --diff`, allowing you to see how a resource has specifically
  changed. (This will be coming in future releases of `kubectl`.)
* The primary interface to `kubectl` is YAML. Pulumi exposes a rich, multi-language SDK, and
  additionally supports raw Kubernetes YAML with the `yaml` namespace in the root of the Kubernetes
  package.
* `kubectl` has a set of commands specifically meant to make it easy to understand what's happening
  in the cluster. Pulumi _only_ does resource management.
* Pulumi has a notion of resource initialization completion, allowing resources be configured using
  values from the live object. For example, a deployment might boot a database, then parse the
  connection string, then put that in a secret, then reference that secret in a `Pod`. As of
  Kubernetes v1.12, `kubectl` can also wait for resource initialization, though it only supports
  applying all resource configuration at one time.
* The ability to deploy the same application multiple times due to autonaming.

## How does Pulumi relate to `helm`?

Helm v2 allows users to easily install a pre-packaged application ("Chart") into a Kubernetes
cluster. Charts are parameterized by some number of values, which users can fill in to customize
their application.

* Helm 2 Charts are managed by an in-cluster API server, called Tiller, rather than the official
  Kubernetes API server. This makes many things (_e.g._, RBAC) harder, because the API server is run
  with a single `ServiceAccount`, which typically has global read/write access to the cluster.

  Pulumi requires no server-side component. Just like `kubectl`, it uses the official [Kubernetes go
  client library][client-go] to talk directly to the API server. It's appropriate to drop Pulumi in
  anywhere you already use `kubectl`.
* The Pulumi CLI presents information-rich status updates, giving a notion of progress as resources
  come online. Helm 2 does not.
* Pulumi has a strong notion of a "plan" -- running `pulumi preview` allows you to see what effect
  a change will have on your resource configuration. Helm 2 does not.
* Explicit notions of creation, deletion, and replacement. If we must change an immutable field in
  an API object, `pulumi preview` alerts the user the object must be replaced. Helm 2 does not.
* Pulumi exposes `pulumi preview --diff`, allowing you to see how a resource has specifically
  changed. Helm 2 does not.
* Pulumi and Helm 2 both use the official [Kubernetes Go client library][client-go] to talk to the
  Kubernetes API server.
* Helm 2 parameterizes YAML templates using Go templates, a textual replacement engine. Go templates
  are not guaranteed to generate syntactically-correct YAML. Pulumi exposes a rich, multi-language
  SDK, with strong typing to catch errors, and a pre-deployment validation step to catch errors
  before you run the program.


[kubeconfig]: https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/
[client-go]: https://github.com/kubernetes/client-go
[login]: https://pulumi.io/reference/cli/pulumi_login.html
[eks]: https://github.com/pulumi/examples/tree/master/aws-ts-eks

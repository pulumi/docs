---
title: Setup
redirect_from: /install/kubernetes.html
---

<!-- LINKS -->
[Pulumi Kubernetes provider]: ./index.html
[Kubernetes Go client library]: https://github.com/kubernetes/client-go
[kubeconfig file]: https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/
[GKE]: https://cloud.google.com/kubernetes-engine/docs/tutorials/
[EKS]: https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html
[AKS]: https://docs.microsoft.com/en-us/azure/aks/
[Heptio AWS quickstart]: https://aws.amazon.com/quickstart/architecture/heptio-kubernetes/

The [Pulumi Kubernetes provider] authenticates and connects to a Kubernetes cluster using a local [kubeconfig file]. This logic is implemented using the official [Kubernetes Go client library], so Pulumi's behavior is identical to `kubectl`. If you have already provisioned a Kubernetes cluster and set up `kubectl` to connect to it, the Pulumi CLI should "just work."

## Pre-requisites

If you're not yet set up, you'll need to do two things:

1.  Provision a Kubernetes cluster. There are several popular guides for each of the major public clouds:
    * For **AWS**, there is [EKS](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html) and the [Heptio quickstart](https://aws.amazon.com/quickstart/architecture/heptio-kubernetes/).
    * For **Azure**, there is [AKS](https://docs.microsoft.com/en-us/azure/aks/).
    * For **GCP**, there is [GKE](https://cloud.google.com/kubernetes-engine/docs/tutorials/).
1.  Download `kubectl`, the Kubernetes CLI. There is an extensive tutorial available [in the Kubernetes docs](https://kubernetes.io/docs/tasks/tools/install-kubectl/). If you're using [Homebrew](https://brew.sh/) on macOS, you can install the community-managed `kubectl` formula via `brew install kubectl`.

## Configuration

By default, `kubectl` and Pulumi will both look for a kubeconfig file in:

* `$KUBECONFIG`, the environment variable
* `~/.kube/config`, in the current user's home directory

If the kubeconfig file is not in either of these locations, Pulumi will not find it, and it will
fail to authenticate against the cluster.

> Pulumi never sends your Kubernetes authentication secrets or credentials to the Pulumi service. Because the Pulumi client uses the Kubernetes Go client to connect to the cluster and execute operations on your behalf, your credentials are only ever stored where you left them (typically in the local kubeconfig file, `~/.ssh`, and so on).

The kubeconfig file defines some number of _contexts_. Each context is a name that is associated
with a _cluster_, _namespace_, and a "_user_" (a local-only name that's associated with a credential
that allows access to the cluster).

To create a context, for example, you can run the `kubectl set-context` command as follows:

```shell
$ kubectl config \
    set-context my-context \
    --cluster=my-cluster \
    --user=my-user
```

If you have done this and are using the default context file, you will be able to set the
configuration variable `kubernetes:context` to the given context name:

```shell
$ pulumi stack init new-kube-stack
$ pulumi config set kubernetes:context my-context
```

If you don't want to need to select a context everywhere, you can always make it the default:

```shell
$ kubectl config \
    use-context my-context
```

> **Note:** Depending on a default context is a bad idea if you're going to share your stack with
> others; it makes your stack dependent on ambient information not known to Pulumi, an anti-pattern
> that leads to unrepeatable deployments.

Additionally, the Kubernetes provider accepts the following configuration settings. These can be
provided to the default Kubernetes provider via `pulumi config set kubernetes:<option>`, or passed
to the constructor of `new kubernetes.Provider` to construct a specific instance of the Kubernetes provider.

* `kubeconfig`: (Optional) The kubeconfig file to use for all resource operations.
* `context`: (Optional) Override the context to use. This works with both kubeconfig files that are
  taken from the system, and those that are supplied with the `kubeconfig` configuration variable.
* `cluster`: (Optional) Override the cluster to use. This works with both kubeconfig files that are
  taken from the system, and those that are supplied with the `kubeconfig` configuration variable.
* `namespace`: (Optional) Override the namespace to use. This works with both kubeconfig files that
  are taken from the system, and those that are supplied with the `kubeconfig` configuration
  variable.

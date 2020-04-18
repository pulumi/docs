---
title: Kubernetes Setup
meta_desc: This page provides an overview on how to seup the Kubernetes Provider for Pulumi.
aliases: ["/docs/reference/clouds/kubernetes/setup/"]
---

<!-- markdownlint-disable url -->
[pulumi-kubernetes-provider]: {{< relref "./" >}}
[client-go]: https://github.com/kubernetes/client-go
[gke-tutorial]: {{< relref "/docs/tutorials/kubernetes/gke" >}}
[eks-tutorial]: {{< relref "/docs/tutorials/kubernetes/eks" >}}
[aks-tutorial]: {{< relref "/docs/tutorials/kubernetes/aks" >}}
[Heptio AWS quickstart]: https://aws.amazon.com/quickstart/architecture/heptio-kubernetes/
[provider-args]: {{< relref "/docs/reference/pkg/kubernetes/provider" >}}
[provider-kubeconfig]: {{< relref "/docs/reference/pkg/kubernetes/provider#inputs" >}}
[kubeconfig]: https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/
[install]: {{< relref "/docs/get-started/install" >}}
[nodejs]: https://nodejs.org/en/
[npm]: https://www.npmjs.com/get-npm
[yarn]: https://yarnpkg.com/en/docs/install
<!-- markdownlint-enable url -->

Your Pulumi program is required to import the [pulumi/kubernetes][pulumi-kubernetes-provider] provider package to allow the Pulumi CLI to authenticate and interact with a running Kubernetes cluster.

By default, Pulumi will use a local [kubeconfig] if available, or one can be passed as a [provider argument][provider-kubeconfig] in the request.

With the `kubeconfig` available, Pulumi communicates with the API Server using the official Kubernetes [client-go] library, just like `kubectl` does.

## Pre-Requisites

If you do not have a cluster set up and running yet, you'll need to do the
following steps.

1. Follow the directions [here][install] to install the Pulumi CLI.
1. Install a package manager for your Pulumi program language runtime, such as [npm] or [Yarn] for [Node.js][nodejs], or PyPI for Python.
1. Provision a Kubernetes cluster. For a new managed Kubernetes cluster, check out the [cluster guides.]({{< relref "/docs/tutorials/kubernetes#clusters" >}})
1. Download [`kubectl`](https://kubernetes.io/docs/tasks/tools/install-kubectl/) and verify the cluster is up and running.

## Steps

By default, Pulumi will look for a kubeconfig file in the following locations,
just like `kubectl`:

* The environment variable: `$KUBECONFIG`,
* Or in current user's default kubeconfig directory: `~/.kube/config`

If the kubeconfig file is not in either of these locations, Pulumi will **not** find it, and it will
fail to authenticate against the cluster. Set one of these locations to a valid kubeconfig file, if you have not done so
already.

Once the cluster is accessible, setup is complete and you can proceed to the
desired tutorials.

> Note: Pulumi **never** sends **any** authentication secrets or credentials to the Pulumi service. See the [FAQ]({{< relref "faq#does-the-pulumi-service-see-my-credentials-in-the-kubeconfig-file">}}) for more detail.

## Misc.

### Kubernetes Configuration

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
configuration variable `kubernetes:context` in the Pulumi config system to the given context name:

```shell
$ pulumi stack init new-kube-stack
$ pulumi config set kubernetes:context my-context
```

If you don't want to select a context, you can always make it the default:

```shell
$ kubectl config \
    use-context my-context
```

> **Note:** Depending on a default context is a bad idea if you're going to share your stack with
> others; it makes your stack dependent on ambient information not known to Pulumi, an anti-pattern
> that leads to unrepeatable deployments.

Additionally, the Kubernetes provider accepts many [configuration settings][provider-args].

These can be provided to the default Kubernetes provider via `pulumi config set kubernetes:<option>`, or passed
to the constructor of a `new kubernetes.Provider` to construct a specific instance of the Kubernetes provider for your requests.

#### Pulumi Dashboard Resource Links

Each Kubernetes resource managed by Pulumi will have a link in the corresponding [Pulumi Console](https://app.pulumi.com")
to view the resource in the cluster. These links are local, and require the client run `kubectl proxy` beforehand to access the resource.

To learn more about `kubectl proxy` check out the [reference docs](https://kubernetes.io/docs/tasks/access-kubernetes-api/http-proxy-access-api/).

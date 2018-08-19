---
title: "Kubernetes"
---

The Kubernetes provider for Pulumi can be used to provision any of the resources specified by the
Kubernetes API (_e.g._, [v1.10](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.10/). The
Kubernetes provider uses the official Kubernetes Go client under the hood, and will automatically
configure itself if a [kubeconfig
file](https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/)
file is present.

See the [full API documentation](./pkg/nodejs/@pulumi/kubernetes/index.html) for complete details of
the available Kubernetes provider APIs.

> **Note:** The Pulumi provider currently supports Kubernetes 1.5+.  If you have a specific version
> requirement and are unsure of whether we currently support it, or are certain we don't and need us
> to begin doing so, please contact us.

## Example

```typescript
import * as k8s from "@pulumi/kubernetes";

// Create an nginx pod
let nginxcontainer = new k8s.core.v1.Pod("nginx", {
    spec: {
        containers: [{
            image: "nginx:1.7.9", name: "nginx", ports: [{ containerPort: 80 }]
        }]
    }
});
```

You can find additional examples Kubernetes examples in [the Pulumi examples
repo](https://github.com/pulumi/examples). If you are new to Pulumi, it may be easiest to look at
them in this order:

1. Getting your feet wet [deploying a container to Kubernetes and exposing it to the Internet with a
   `Service`](https://github.com/pulumi/examples/tree/master/kubernetes-ts-exposed-deployment). This
   example shows off several unique features of Pulumi, including diffing and incremental errors
   when deployment fails.
1. ["Adopting" a Helm
   Chart](https://github.com/pulumi/examples/tree/master/kubernetes-ts-helm-wordpress). This example
   additionally demonstrates the rich status updates Pulumi offers, allowing you to reliably and
   reproducibly deploy code, even if it isn't yours.
1. [The canonical Kubernetes Guestbook
   example](https://github.com/pulumi/examples/tree/master/kubernetes-ts-guestbook). You can see the
   original example [here](https://github.com/pulumi/examples/tree/master/kubernetes-ts-guestbook)
   for comparison.
1. [Triggering a new deployment when changing the data in a
   `ConfigMap`](https://github.com/pulumi/examples/tree/master/kubernetes-ts-configmap-rollout).
   This example shows how Pulumi will safely allow you to update containers to use new configuration
   data in a way that is natural to the user.

## Libraries

The following pacakges are available in pacakge managers:

* JavaScript/TypeScript: https://www.npmjs.com/package/@pulumi/kubernetes

Support will eventually expand to Python and Go as well.

## Authentication and Configuration

Pulumi authenticates and connects to a Kubernetes cluster using a local [kubeconfig
file](https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/).
In this way, its behavior is identical to `kubectl`, so if you have already provisioned a Kubernetes
cluster and set up `kubectl` to connect to it, the Pulumi CLI should "just work."

By default, `kubectl` and Pulumi will both look for a kubeconfig file in:

* `$KUBECONFIG`, the environment variable
* `~/.kube/config`, in the current user's home directory

If the kubeconfig file is not in either of these locations, Pulumi will not find it, and it will
fail to authenticate against the cluster.

The kubeconfig file defines some number of _contexts_. Each context is a name that is associated
with a _cluster_, _namespace_, and a "_user_" (a local-only name that's associated with a credential
that allows access to the cluster).

To create a context, for example, you can run the `kubectl set-context` command as follows:

```
$ kubectl config \
    set-context my-context \
    --cluster=my-cluster \
    --user=my-user
```

If you have done this and are using the default context file, you will be able to set the
configuration variable `kubernetes:context` to the given context name:

```
$ pulumi stack init new-kube-stack
$ pulumi config set kubernetes:context my-context
```

If you don't want to need to select a context everywhere, you can always make it the default:

```
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

---
title: Kubernetes
redirect_from: /reference/kubernetes.html
---

<img src="/images/quickstart/k8s-purple.png" align="right">

The Kubernetes provider for Pulumi can be used to provision any of the resources specified by the
Kubernetes API (_e.g._, [v1.10](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.10/). The
Kubernetes provider uses the official Kubernetes Go client under the hood, and will automatically
configure itself if a [kubeconfig
file](https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/)
file is present.

See the [full API documentation](/reference/pkg/nodejs/@pulumi/kubernetes/index.html) for complete details of
the available Kubernetes provider APIs.

> **Note:** The Pulumi provider currently supports Kubernetes 1.5+.  If you have a specific version
> requirement and are unsure of whether we currently support it, or are certain we don't and need us
> to begin doing so, please contact us.

## Setup

By default, Pulumi uses the same configuration as `kubectl`, so if you're already connected to a cluster, Pulumi will
"just work." For more details, including this initial setup, please see the [Kubernetes setup page](./setup.html).

## Tutorials

The easiest way to start with Kubernetes is to follow one of the tutorials:

* [Run a Stateless App Deployment](./tutorial-stateless-app.html): Deploy a simple stateless Nginx web server backed
    by a Docker container
* [Create a Guestbook App with Redis and Nginx](./tutorial-guestbook.html): Create multi-tier web application using
    Redis and Nginx, and powered by Docker containers

There are additional examples available complete with step-by-step instructions. If you are new to Pulumi, it may be
easiest to look at them in this order:

* Getting your feet wet [deploying a container to Kubernetes and exposing it to the Internet with a
    `Service`](https://github.com/pulumi/examples/tree/master/kubernetes-ts-exposed-deployment). This
    example shows off several unique features of Pulumi, including diffing and incremental errors
    when deployment fails.
* ["Adopting" a Helm
   Chart](https://github.com/pulumi/examples/tree/master/kubernetes-ts-helm-wordpress). This example
   additionally demonstrates the rich status updates Pulumi offers, allowing you to reliably and
   reproducibly deploy code, even if it isn't yours.
* [The canonical Kubernetes Guestbook
   example](https://github.com/pulumi/examples/tree/master/kubernetes-ts-guestbook). You can see the
   original example [here](https://github.com/pulumi/examples/tree/master/kubernetes-ts-guestbook)
   for comparison.
* [Triggering a new deployment when changing the data in a
   `ConfigMap`](https://github.com/pulumi/examples/tree/master/kubernetes-ts-configmap-rollout).
   This example shows how Pulumi will safely allow you to update containers to use new configuration
   data in a way that is natural to the user.

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

You can find additional examples Kubernetes examples in [the Pulumi examples repo](https://github.com/pulumi/examples). 

## Libraries

The following pacakges are available in pacakge managers:

* JavaScript/TypeScript: https://www.npmjs.com/package/@pulumi/kubernetes

Support will eventually expand to Python and Go as well.

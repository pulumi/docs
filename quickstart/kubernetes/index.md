---
title: Kubernetes
redirect_from: /reference/kubernetes.html
---

<img src="/images/quickstart/k8s-purple.png" align="right">

The Kubernetes provider for Pulumi can be used to provision any of the resources specified by the
Kubernetes API (_e.g._, [v1.10](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.10/)). The
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

* Getting your feet wet [deploying a container to Kubernetes and exposing it to the Internet with a
    `Service`](./tutorial-exposed-deployment.html). This example shows off several unique features of
    Pulumi, including diffing and incremental errors when deployment fails.
* ["Adopting" a Helm Chart](./tutorial-wordpress-chart.html). This example additionally demonstrates
   the rich status updates Pulumi offers, allowing you to reliably and reproducibly deploy code,
   even if it isn't yours.
* [The canonical Kubernetes Guestbook example](./tutorial-guestbook.html). You can see the original
   example [here](https://github.com/pulumi/examples/tree/master/kubernetes-ts-guestbook) for
   comparison.
* [Triggering a new deployment when changing the data in a
   `ConfigMap`](./tutorial-configmap-rollout.html).
   This example shows how Pulumi will safely allow you to update containers to use new configuration
   data in a way that is natural to the user.
* [Staged rollout gated on Prometheus health checks](./tutorial-p8s-rollout.html). This example
  shows how we can roll out to a small canary ring, check Prometheus metrics, and then roll out to a
  larger prod ring only when that succeeds.
* [Run a Stateless App Deployment](./tutorial-stateless-app.html): Deploy a simple stateless Nginx web server backed
    by a Docker container

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

The following packages are available in package managers:

* JavaScript/TypeScript: https://www.npmjs.com/package/@pulumi/kubernetes

Support will eventually expand to Python and Go as well.

## FAQ

You can find a list of frequently-asked questions [here](./faq.html).

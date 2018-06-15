---
title: "Kubernetes"
---

Pulumi supports managing Kubernetes resources using your language of choice.  This lets you express the same set of
concepts you'd normally write in your declarative YAML file, except that you'll also get the ability to

* **Abstract** away common patterns by using familiar programming language constructs;
* **Share and reuse** packages, either within your own app, inside your organization, or with the community;
* **Diff and deploy resource state** with full auditability around who updated what, when, and why;
* **Manage cloud provider resources** alongside your Kubernetes abstractions, with a single consistent toolchain.

Everything you already know about Pulumi applies to managing Kubernetes resources, and the below guide will help get
you up and running with the Kubernetes provider.

> **Note:** The Pulumi provider currently supports Kubernetes 1.5+.  If you have a specific version requirement and are
> unsure of whether we currently support it, or are certain we don't and need us to begin doing so, please contact us.

## Packages

Kubernetes resources are defined in the following locations:

* Source repo: [pulumi/pulumi-kubernetes](https://github.com/pulumi/pulumi-kubernetes)
* NPM package for JavaScript and/or TypeScript: [@pulumi/kubernetes](https://www.npmjs.com/package/@pulumi/kubernetes)
* Package documentation: [@pulumi/kubernetes](pkg/nodejs/@pulumi/kubernetes)

To use a Kubernetes package, you simply add it to your project's package management file, as usual.

### JavaScript and TypeScript

If you're using JavaScript and/or TypeScript, add your dependency to `package.json`:

```json
{
    "dependencies": {
        "@pulumi/kubernetes": "^0.14.0"
    }
}
```

Install the package using `npm install` or `yarn install`.  This will download the latest version, and also install
the associated Pulumi resource provider plugin.

### Go

The Pulumi Kubernetes provider **currently does not support Go.** We are planning to support it eventually. To track
this work, see issue [#59](https://github.com/pulumi/pulumi-kubernetes/issues/59)

### Python

The Pulumi Kubernetes provider **currently does not support Go.** We are planning to support it eventually. To track
this work, see issue [#70](https://github.com/pulumi/pulumi-kubernetes/issues/70)

## Examples

Here is a minimal example of a program that runs a single-container Nginx pod:

```typescript
import * as k8s from "@pulumi/kubernetes";

// Create an nginx pod
let nginxcontainer = new k8s.core.v1.Pod("nginx", {
    metadata: {
        name: "nginx",
        labels: {
            app: "nginx",
        },
    },
    spec: {
        containers: [{
            image: "nginx:1.7.9",
            name: "nginx",
            ports: [{
                containerPort: 80,
            }],
        }],
    },
});
```

Of course, most real applications would not be this simple.  There are several more comprehensive examples of
Kubernetes programs available in the [Pulumi examples repo](https://github.com/pulumi/examples).  For example, we
ported [the infamous Kubernetes Guestbook
example](https://github.com/pulumi/examples/tree/master/kubernetes-ts-guestbook) to Pulumi, and it demonstrates
composing many interesting resource types into a single application.

## Configuration

Pulumi authenticates and connects to a Kubernetes cluster using a local
[kubeconfig file](https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/). In
this way, its behavior is identical to `kubectl`, so if you have already provisioned a Kubernetes cluster and set up
`kubectl` to connect to it, the Pulumi CLI should "just work."

By default, `kubectl` and Pulumi will both look for a kubeconfig file in:

* `$KUBECONFIG`, the environment variable
* `~/.kube/config`, in the current user's home directory

If the kubeconfig file is not in either of these locations, Pulumi will not find it, and it will fail to authenticate
against the cluster.

The kubeconfig file defines some number of _contexts_. Each context is a name that is associated with a _cluster_,
_namespace_, and a "_user_" (a local-only name that's associated with a credential that allows access to the cluster).

To create a context, for example, you can run the `kubectl set-context` command as follows:

```
$ kubectl config \
    set-context my-context \
    --cluster=my-cluster \
    --user=my-user
```

If you have done this and are using the default context file, you will be able to set the configuration variable
`kubernetes:configContext` to the given context name:

```
$ pulumi stack init new-kube-stack
$ pulumi config set kubernetes:configContext my-context
```

If you don't want to need to select a context everywhere, you can always make it the default:

```
$ kubectl config \
    use-context my-context
```

> **Note:** Depending on a default context is a bad idea if you're going to share your stack with others; it makes your
> stack dependent on ambient information not known to Pulumi, an anti-pattern that leads to unrepeatable deployments.

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
* PyPI package for Python: `pulumi_kubernetes`
* NPM package for JavaScript and/or TypeScript: [@pulumi/kubernetes](https://www.npmjs.com/package/@pulumi/kubernetes)
* Package documentation: [@pulumi/kubernetes](pkg/nodejs/@pulumi/kubernetes)

To use a Kubernetes package, you simply add it to your project's package management file, as usual.

### Python

If you're using Python, add your dependency to `requirements.txt`:

```
pulumi_kubernetes>=0.11.0
```

Install the package using `pip install -r requirements.txt`.  This will download the latest version, and also install
the associated Pulumi resource provider plugin.

> **Note:** While Pulumi is in Private Beta, be sure to [configure your Pip client](./python.html#pypi-packages)
> to correctly download packages from Pulumi's private PyPI proxy server.  This is a temporary requirement.

### JavaScript and TypeScript

If you're using JavaScript and/or TypeScript, add your dependency to `package.json`:

```json
{
    "dependencies": {
        "@pulumi/kubernetes": "^0.11.0"
    }
}
```

Install the package using `npm install` or `yarn install`.  This will download the latest version, and also install
the associated Pulumi resource provider plugin.

## Examples

Here is a minimal example of a program that runs a single-container Nginx pod:

```python
import pulumi_kubernetes as k8s

c = k8s.Pod('nginx',
    metadata={
        'name': 'nginx',
        'labels': {
            'app': 'nginx',
        },
    },
    spec={
        'containers': [{
            'image': 'nginx:1.7.9',
            'name': 'nginx',
            'ports': [{ 'container_port': 80 }],
        }],
    },
)
```

Of course, most real applications would not be this simple.  There are several more comprehensive examples of
Kubernetes programs available in the [Pulumi examples repo](https://github.com/pulumi/examples).  For example, we
ported [the infamous Kubernetes Guestbook
example](https://github.com/pulumi/examples/tree/master/kubernetes-ts-guestbook) to Pulumi, and it demonstrates
composing many interesting resource types into a single application.

## Configuration

Before deploying a program to a real cluster, you will need to configure your Pulumi program to communicate and
authenticate with the target Kubernetes master node.  This can be done in one of two ways.

> **Note:** If you're running a cluster locally, such as with [Minikube](
> https://github.com/kubernetes/minikube), it's likely that performing a deployment will "just work" because of the
> default configuration settings.  If you get an error, however:
>
> ```
> Post http://localhost/api/v1/namespaces/default/pods: dial tcp [::1]:80: getsockopt: connection refused
> ```
>
> This means you either haven't started your cluster, or need to configure an endpoint explicitly (see below).

### Host and Credentials

The easiest approach is to define a host plus credentials to use for contacting your Kubernetes cluster.

This includes the following settings:

* `kubernetes:host`: The host URI of the Kubernetes master node.  If unspecified, the `KUBE_HOST` environment
  variable is consulted, and the default is `https://localhost` if not overridden anywhere.

The following HTTP basic authentication options are available:

* `kubernetes:username`: The username used for HTTP basic authentication when communicating with the Kubernetes
  master node.  If unspecified, the `KUBE_USER` environment variable is consulted.

* `kubernetes:password`: The password used for HTTP basic authentication when communicating with the Kubernetes
  master node.  If unspecified, the `KUBE_PASSWORD` environment variable is consulted.

The following TLS certificate authentication options available:

* `kubernetes:clientCertificate`: A PEM-encoded client certificate for TLS authentication.  This may alternatively
  be specified using the `KUBE_CLIENT_CERT_DATA` environment variable.

* `kubernetes:clientKey`: A PEM-encoded client certificate key for TLS authentication.  This may alternatively
  be specified using the `KUBE_CLIENT_KEY_DATA` environment variable.

* `kubernetes:clusterCaCertificate`: PEM-encoded root certificate bundles, alternatively specified using the
  `KUBE_CLUSTER_CA_CERT_DATA` environment variable.

* `kubernetes:insecure`: If true, TLS certificate verification will be skipped.  This defaults to `false`, and
  can also be set via the `KUBE_INSECURE` environment variable.

For example, here are a sequence of CLI invocations that will fully configure access to a cluster:

```
$ pulumi stack init new-kube-stack
$ pulumi config set kubernetes:host https://104.197.5.247
$ pulumi config set kubernetes:username x
$ pulumi config set kubernetes:password y
$ cat ~/.kube/client-cert.pem | pulumi config set kubernetes:clientCertificate
$ cat ~/.kube/client-key.pem | pulumi config set kubernetes:clientKey
$ cat ~/.kube/client-ca-cert.pem | pulumi config set kubernetes:clientCaCertificate
```

This approach is easy, and requires less up-front configuration, but it does mean you might need to duplicate more
configuration state across your stacks when you are deploying many stacks to the same target cluster.  Kubernetes has
support for pre-defined "contexts", which encapsulate this information, although you should be careful if you go down
this path not to make Pulumi dependent on your machine settings for deployment configuration.

### Context Objects

The easiest way to configure access is to define a context using Kubernetes' support for configuring `kubectl`
access to multiple clusters.  See [this
document](https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/) for
comprehensive instructions on how to do so.  This will allow you to not only give a name to your context, but also
associate it with a cluster, namespace, and user, for authentication and tagging purposes.

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

If you've elected to store your configuration somewhere other than the default location, you can point Pulumi to
it by setting the `kubernetes:configPath` variable.

Note that you can override the default cluster or user by using the `kubernetes:configContextCluster` and/or
`kubernetes:configContextAuthInfo` variables.  If they aren't specified, the settings from the context are used.

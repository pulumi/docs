---
title_tag: Configure access | Kubernetes
title: Configure access
h1: "Get started with Pulumi and Kubernetes"
meta_desc: This page provides an overview on how to get started with Pulumi when starting a Kubernetes project.
weight: 3
menu:
    iac:
        name: Configure access
        parent: kubernetes-get-started
        weight: 3
        identifier: kubernetes-get-started.configure
aliases:
    - /docs/quickstart/kubernetes/configure/
    - /docs/get-started/kubernetes/configure/
    - /docs/clouds/kubernetes/get-started/configure/
---

## Configure access to Kubernetes

Pulumi's CLI needs access to a Kubernetes cluster to manage cloud resources.

You must have access to a Kubernetes cluster—either a local cluster (such as <a href="https://minikube.sigs.k8s.io/" target="_blank">Minikube</a>, <a href="https://kind.sigs.k8s.io/" target="_blank">kind</a>, or <a href="https://docs.docker.com/desktop/kubernetes/" target="_blank">Docker Desktop</a>) or a cloud-managed cluster (such as <a href="https://cloud.google.com/kubernetes-engine" target="_blank">GKE</a>, <a href="https://azure.microsoft.com/en-us/products/kubernetes-service" target="_blank">AKS</a>, or <a href="https://aws.amazon.com/eks/" target="_blank">EKS</a>).

You also need <a href="https://kubernetes.io/docs/tasks/tools/" target="_blank">kubectl</a> installed and configured to access your cluster.

### Testing access

To test that your Kubernetes cluster access is configured properly, run:

{{% choosable os "linux,macos" %}}

```bash
$ kubectl cluster-info
```

{{% /choosable %}}

{{% choosable os "windows" %}}

```powershell
> kubectl cluster-info
```

{{% /choosable %}}

If your cluster's control plane and services are printed, your configuration is correct. If not, read on:

```
Kubernetes control plane is running at https://127.0.0.1:6443
CoreDNS is running at https://127.0.0.1:6443/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy
```

You can also verify you have access to cluster resources:

{{% choosable os "linux,macos" %}}

```bash
$ kubectl get nodes
$ kubectl auth can-i get pods
```

{{% /choosable %}}

{{% choosable os "windows" %}}

```powershell
> kubectl get nodes
> kubectl auth can-i get pods
```

{{% /choosable %}}

### How Pulumi accesses your cluster

Pulumi uses the same kubeconfig file that kubectl uses (typically `~/.kube/config`). If you can run `kubectl get nodes`, Pulumi will work automatically.

You can verify which context Pulumi will use:

{{% choosable os "linux,macos" %}}

```bash
$ kubectl config current-context
```

{{% /choosable %}}

{{% choosable os "windows" %}}

```powershell
> kubectl config current-context
```

{{% /choosable %}}

### Alternative approaches

If you need to use a specific kubeconfig file or context, you can set:

{{% choosable os "linux,macos" %}}

```bash
$ export KUBECONFIG="$HOME/path/to/kubeconfig"
```

{{% /choosable %}}

{{% choosable os windows %}}

```powershell
> $env:KUBECONFIG = "C:\path\to\kubeconfig"
```

{{% /choosable %}}

Or specify the context in your Pulumi stack configuration:

{{% choosable os "linux,macos" %}}

```bash
$ pulumi config set kubernetes:context my-cluster-context
```

{{% /choosable %}}

{{% choosable os "windows" %}}

```powershell
> pulumi config set kubernetes:context my-cluster-context
```

{{% /choosable %}}

For detailed information on Pulumi's use of Kubernetes credentials, see [Kubernetes Setup](/registry/packages/kubernetes/installation-configuration/).

{{< get-started-stepper >}}

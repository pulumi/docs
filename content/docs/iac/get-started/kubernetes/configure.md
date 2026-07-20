---
title_tag: Configure access | Kubernetes
title: Configure access to Kubernetes
linkTitle: Configure access
h1: "Configure access to Kubernetes"
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

The Pulumi CLI needs access to a Kubernetes cluster to manage resources. For this tutorial, you'll need a cluster — a local one such as <a href="https://minikube.sigs.k8s.io/" target="_blank">minikube</a>, <a href="https://kind.sigs.k8s.io/" target="_blank">kind</a>, or <a href="https://docs.docker.com/desktop/kubernetes/" target="_blank">Docker Desktop</a>, or a cloud-managed one such as <a href="https://cloud.google.com/kubernetes-engine" target="_blank">GKE</a>, <a href="https://azure.microsoft.com/en-us/products/kubernetes-service" target="_blank">AKS</a>, or <a href="https://aws.amazon.com/eks/" target="_blank">EKS</a> — plus <a href="https://kubernetes.io/docs/tasks/tools/" target="_blank">kubectl</a> installed and configured to reach it.

Pulumi uses the same kubeconfig that kubectl does, so if you can reach your cluster with kubectl, Pulumi works automatically. Test it directly:

```bash
$ kubectl cluster-info

Kubernetes control plane is running at https://127.0.0.1:6443
CoreDNS is running at https://127.0.0.1:6443/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy
```

If your cluster's control plane and services are printed, you're configured correctly. You can also confirm you have access to cluster resources and check which context Pulumi will use:

```bash
$ kubectl get nodes
$ kubectl auth can-i get pods
$ kubectl config current-context
```

To use a specific kubeconfig file or context, set the `KUBECONFIG` environment variable, or set the `kubernetes:context` value on your stack once you've created one:

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

For additional configuration options, see [Kubernetes Setup](/registry/packages/kubernetes/installation-configuration/).

{{< get-started-stepper >}}

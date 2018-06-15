---
title: "Configure Pulumi for Kubernetes"
---

<!-- LINKS -->
[Pulumi Kubernetes provider]: ../reference/kubernetes.html
[Kubernetes Go client library]: https://github.com/kubernetes/client-go
[kubeconfig file]: https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/
[GKE]: https://cloud.google.com/kubernetes-engine/docs/tutorials/
[EKS]: https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html
[AKS]: https://docs.microsoft.com/en-us/azure/aks/
[Heptio AWS quickstart]: https://aws.amazon.com/quickstart/architecture/heptio-kubernetes/

The [Pulumi Kubernetes provider] authenticates and connects to a Kubernetes cluster using a local [kubeconfig file]. This logic is implemented using the official [Kubernetes Go client library], so Pulumi's behavior is identical to `kubectl`. If you have already provisioned a Kubernetes cluster and set up `kubectl` to connect to it, the Pulumi CLI should "just work."

> Pulumi never sends your Kubernetes authentication secrets or credentials to the Pulumi service. Because the Pulumi client uses the Kubernetes Go client to connect to the cluster and execute operations on your behalf, your credentials are only ever stored where you left them (typically in the local kubeconfig file, `~/.ssh`, and so on).

If you're not yet set up, you'll need to do two things:

1.  Provision a Kubernetes cluster. There are several popular guides for each of the major public clouds:
    * For **AWS**, there is [EKS](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html) and the [Heptio quickstart](https://aws.amazon.com/quickstart/architecture/heptio-kubernetes/).
    * For **Azure**, there is [AKS](https://docs.microsoft.com/en-us/azure/aks/).
    * For **GCP**, there is [GKE](https://cloud.google.com/kubernetes-engine/docs/tutorials/).
1.  Download `kubectl`, the Kubernetes CLI. There is an extensive tutorial available [in the Kubernetes docs](https://kubernetes.io/docs/tasks/tools/install-kubectl/). If you're using [Homebrew](https://brew.sh/) on macOS, you can install the community-managed kubectl formula via `brew install kubectl`.

---
title_tag: "Kubernetes Guides"
meta_desc: Production-ready Kubernetes guides for teams. Work together to deliver Kubernetes to AWS, Azure, Google Cloud, or private.
title: Guides
h1: Pulumi & Kubernetes guides
meta_image: /images/docs/meta-images/docs-clouds-kubernetes-meta-image.png
menu:
  iac:
    name: Guides
    parent: kubernetes-clouds
    identifier: kubernetes-clouds-guides
    weight: 30
aliases:
- /docs/guides/k8s-the-prod-way/app
- /docs/guides/k8s-the-prod-way/architecture
- /docs/guides/crosswalk/kubernetes/
- /docs/clouds/kubernetes/guides/
---

These guides cover production-ready Kubernetes for teams. Work together to deliver Kubernetes to any cloud — AWS, Azure, Google Cloud, or private.

If you are just getting started with Pulumi and Kubernetes, the [Get Started][k8s-get-started] guide is a better place to start.

## Playbooks for Kubernetes

Manage production-ready infrastructure leveraging hosted
Kubernetes offerings such as [Amazon Elastic Kubernetes Service (EKS)][eks], [Azure
Kubernetes Service (AKS)][aks], or [Google Kubernetes Engine (GKE)][gke].

Discover solutions to the hardest Kubernetes problems to avoid mitigating
pitfalls around infrastructure, security, governance, reliability, and
maintainability of the cluster, its workloads, and underlying resources.

[Get started][k8s-playbooks] with the playbooks to manage Kubernetes in production with your team.

## Pulumi Kubernetes Operator

<a href="./">
    <img src="/logos/tech/ci-cd/kubernetes.png" align="right" width="150" style="margin: 0 0 32px 16px;">
</a>

The [Pulumi Kubernetes Operator][k8s-operator] is an [extension pattern][k8s-ext-pattern] that
enables Kubernetes users to create a `Stack` as a first-class API
resource, and use the `StackController` to drive the updates of the Stack until
success.

Deploying [Pulumi Stacks][stack] in Kubernetes provides the capability to build
out CI/CD and automation systems into your clusters, creating native support to manage your infrastructure alongside your Kubernetes workloads.

[Get started][k8s-operator-cicd] with the Pulumi Kubernetes Operator in your [continuous delivery][pulumi-cd] pipelines.

[k8s-operator]: https://github.com/pulumi/pulumi-kubernetes-operator
[k8s-ext-pattern]: https://kubernetes.io/docs/concepts/extend-kubernetes/operator/
[stack]: /docs/concepts/stack/
[k8s-operator-cicd]: /docs/using-pulumi/continuous-delivery/pulumi-kubernetes-operator/

<!-- markdownlint-disable url -->
[k8s-playbooks]: /docs/clouds/kubernetes/guides/playbooks/
[k8s-get-started]: /docs/iac/get-started/kubernetes/
[eks]: https://aws.amazon.com/eks/
[aks]: https://azure.microsoft.com/en-us/services/kubernetes-service/
[gke]: https://cloud.google.com/kubernetes-engine/
[pulumi-k8s]: https://github.com/pulumi/pulumi-kubernetes
[pulumi-cd]: /docs/using-pulumi/continuous-delivery/
<!-- markdownlint-enable url -->

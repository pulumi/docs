---
title: "Pulumi Crosswalk for Kubernetes - Azure"
linktitle: Azure
menu:
  userguides:
    parent: crosswalk-kubernetes
    identifier: crosswalk-kubernetes-azure

aliases: ["/docs/guides/crosswalk/kubernetes/azure"]
---

The following [Pulumi stacks]({{< relref
"/docs/intro/concepts/organizing-stacks-projects.md" >}}) partition the set of
responsibilities and functionality necessary to manage a Kubernetes cluster and
its infrastructure, as detailed in [Production Architecture for Teams][prod-arch-for-teams].

The full code for **Crosswalk for Kubernetes - Azure** is on [GitHub][gh-repo].

## Cloud Stacks

  1. (Coming Soon) [Identity]({{< relref "01-cloud-stacks/01-identity.md" >}}): Manage authentication for the cluster.
  1. (Coming Soon) [Managed Infrastructure]({{< relref "01-cloud-stacks/02-networking.md" >}}): Setup managed infrastructure, such as networking, storage, and other cloud services.

## Kubernetes Stacks
  1. (In Progress) [Kubernetes Cluster]({{< relref "02-kubernetes-stacks/01-cluster-configuration.md" >}}): Manage the control plane, worker nodes, RBAC, and defaults.
  1. (Coming Soon) [Cluster Services]({{< relref "02-kubernetes-stacks/02-cluster-services.md" >}}): Manage cluster-scoped services, such as logging and monitoring.
  1. (Coming Soon) [App Services]({{< relref "02-kubernetes-stacks/03-app-services.md" >}}): Manage application-scoped services, such as DNS and ingress management. 
  1. (Coming Soon) [Apps]({{< relref "02-kubernetes-stacks/04-apps.md" >}}): Manage applications and workloads.  

[gh-repo]: https://github.com/metral/kubernetes-the-prod-way/tree/metral/crosswalk/azure
[prod-arch-for-teams]: /docs/guides/crosswalk/kubernetes/introduction/01-architecture/

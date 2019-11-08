---
title: "Pulumi Crosswalk for Kubernetes"
linktitle: Crosswalk for Kubernetes
menu:
  userguides:
    parent: guides
    identifier: crosswalk-kubernetes
---

Pulumi Crosswalk for Kubernetes is a collection of industry-standard
best-practices, and tasks for managing Kubernetes and its infrastructure in production.

This guide is for provisioning and configuring production-grade Kubernetes
clusters, and deploying workloads into the clusters.

If you are just getting started with Pulumi and Kubernetes, the [Get Started][k8s-get-started] guide is a better place to start.

## Overview

The primary steps to follow include how to:

  * [Create the Control Plane][crosswalk-control-plane]
  * [Create the Worker Nodes][crosswalk-worker-nodes]
  * [Try out the Cluster][crosswalk-try-out-the-cluster]
  * [Update the Worker Nodes][crosswalk-update-worker-nodes]
  * [Configure Cluster Defaults][crosswalk-configure-defaults]
  * [Configure Access Control][crosswalk-configure-access]
  * [Deploy Cluster Services][crosswalk-cluster-svcs]
  * [Deploy App Services][crosswalk-app-svcs]
  * [Deploy Apps][crosswalk-apps]

## Production Architecture for Teams

Infrastructure misconfiguration accounts for the most significant subset of serious
production outages in major systems. Many of these failure modes are preventable.

The primary objective of this reference architecture is to create sensible
defaults that reduce the likelihood of these errors. Modern infrastructure as
code tools, such as Pulumi, are effective means of accomplishing
this goal.

These tools allow engineering teams to share specifications for what their
infrastructure should look like and allow teams to reliably provision and manage
infrastructure. Changes to infrastructure can be audited as part of
code review, and they allow teams to detect drift.

This architecture is meant to show how these tools can be used within a team
to employ and understand:

* **Security:** Who has access to what, and how are things ensured?
* **Governance:** How do we ensure the blast radius of changes is as small as possible?
* **Engineering:**  How do we automate this with CI/CD?

## Production Infrastructure as Code

At the heart of this architecture is a simple idea: that we should separate resources into
loosely-coupled, independently-manageable sets, based on risk and functionality.

<center><img src="/images/docs/quickstart/kubernetes/cake.svg" width="670"></center>

We suggest splitting infrastructure up into (roughly) six [Pulumi
stacks]({{< relref "/docs/intro/concepts/organizing-stacks-projects" >}}) of resources.

### 1. Identity

Identities and role definitions for organizations and CI/CD are required before anyone can provision
anything. This is a requirement for every production Kubernetes deployment.

By isolating resources into loosely-coupled stacks, we
have the opportunity to grant minimal permissions based on the [principle of least
privilege][least-privileged].

The identity stack typically contains:

* Identities and roles for the team e.g. [AWS IAM][aws-iam], [GCP IAM][gcp-iam], [Azure AD][azure-ad].

    For example, the databases team typically gets only administrative permissions for the datastores, while an app team might only get cluster developer permissions.
* Service Accounts for bots and CI/CD.

    While IAM roles and Active Directory accounts describe identity of users,
    service accounts grant an identity for workloads, e.g. Storage
    CI/CD.

### 2. Managed Infrastructure

Provisioning shared, managed infrastructure is required to configure the
cluster.

At a minimum, this typically includes networking infrastructure,
and can often include storage backends along with other cloud services such as
VMs, registries, data pipelines, and data warehouses.

### 3. Kubernetes Cluster

Configure and provision the Kubernetes cluster with the desired settings and defaults.

Typically this also involves provisioning Kubernetes cluster infrastructure
with [API resources][k8s-api-resources] such as `Namespaces`, `Roles` , `RoleBindings`, and `Quotas`.

Using a managed Kubernetes cluster on [EKS][eks], [GKE][gke], or [AKS][aks] is
the easiest recommended way to get started with deploying a cluster.

### 4. Cluster Services

With a running, vanilla cluster you should install any Kubernetes cluster-scoped
services that will be shared by a subset or all cluster users.

At a minimum, services include centralized cluster and app-based logging, and often
include monitoring, policies, and service meshes.

### 5. App Services

Configure any Kubernetes app-scoped services that will be shared
by a subset or all users with deployment permissions.

App services tend to include managed datastores (e.g. [RDS][aws-rds],
[Cloud SQL][cloud-sql], and [CosmosDB][cosmos-db]), ingress controllers,
DNS managers, TLS certificate managers, and app pipelines.

### 6. Apps

Deploy applications and workloads into the cluster.

## Frequently Asked Questions (FAQ)

* TODO

[aws-iam]: https://aws.amazon.com/iam/
[gcp-iam]: https://cloud.google.com/iam/
[azure-ad]: https://azure.microsoft.com/en-us/services/active-directory/
[eks]: https://aws.amazon.com/eks/
[gke]: https://cloud.google.com/kubernetes-engine/
[aks]: https://docs.microsoft.com/en-us/azure/aks/
[aws-rds]: https://aws.amazon.com/rds
[cloud-sql]: https://cloud.google.com/sql/
[cosmos-db]: https://azure.microsoft.com/en-us/services/cosmos-db/
[k8s-get-started]: {{< relref "/docs/get-started/kubernetes" >}}
[k8s-api-resources]: https://kubernetes.io/docs/reference/kubernetes-api/
[aws-sqs]: https://aws.amazon.com/sqs/
[crosswalk-control-plane]: {{< relref "/docs/guides/crosswalk/kubernetes/control-plane" >}}
[crosswalk-worker-nodes]: {{< relref "/docs/guides/crosswalk/kubernetes/worker-nodes" >}}
[crosswalk-try-out-the-cluster]: {{< relref "/docs/guides/crosswalk/kubernetes/try-out-the-cluster" >}}
[crosswalk-configure-defaults]: {{< relref "/docs/guides/crosswalk/kubernetes/configure-defaults" >}}
[crosswalk-configure-access]: {{< relref "/docs/guides/crosswalk/kubernetes/configure-access-control" >}}
[crosswalk-cluster-svcs]: {{< relref "/docs/guides/crosswalk/kubernetes/cluster-services" >}}
[crosswalk-app-svcs]: {{< relref "/docs/guides/crosswalk/kubernetes/app-services" >}}
[crosswalk-apps]: {{< relref "/docs/guides/crosswalk/kubernetes/apps" >}}
[crosswalk-update-worker-nodes]: {{< relref "/docs/guides/crosswalk/kubernetes/update-worker-nodes" >}}
[least-privileged]: https://en.wikipedia.org/wiki/Principle_of_least_privilege

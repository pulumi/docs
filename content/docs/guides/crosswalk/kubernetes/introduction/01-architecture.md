---
title: Production Architecture for Teams

aliases: ["/docs/guides/crosswalk/kubernetes/architecture/"]
---

Infrastructure misconfiguration accounts for the most significant subset of serious
production outages in major systems. Some [reasonable estimates][post-mortems] put the fraction in
the range of 40-50%.

Many of these failure modes are trivially preventable. The primary objective of this reference
architecture is to create sensible defaults that make many of these issues either impossible, or
dramatically less likely.

**Modern Infrastructure-as-Code tools, such as Pulumi, are effective means of accomplishing
this goal.**

These tools allow engineering teams to share specifications for what their
infrastructure should look like. These specifications can be executed, allowing teams to
reliably provision and manage infastructure. Changes to infrastructure can be audited as part of
code review. And they allow teams to detect drift.

But even the most powerful tools don't solve problems -- teams do. And doing
so requires the organizational discipline to use such tools effectively.

This architecture is meant to show how infrastructure-as-code tools can be used in a team setting.
It is meant to answer questions like:

* **Security:** Who has access to what, and how are things ensured?
* **Governance:** How do we ensure the blast radius of changes is as small as possible?
* **Engineering:**  How do we automate this with CI/CD?

## Production Infrastructure-as-Code

At the heart of this architecture is a simple idea: that we should **separate resources into
loosely-coupled, independently-managable sets, based on risk and functionality.**

There are many benefits to this approach:

* **Faster release velocity.** Modern infrastructure-as-code tools can
  take tens of minutes to generate large plans of resources. Splitting up configuration into well-scoped modules
  is always more time-efficient.
* **Tractable plans.** It is markedly easier to notice that you're destroying your primary datastore
  in a 30-line plan than a 900-line plan.
* **Users get permissions they need rather than global admin permissions.**
* **Limited blast radius.** Separating (e.g.) app and storage configration means that the app team
  can't accidentally destroy the primary datastore.
* **Independently managable.** For example, the identity stack (containing, e.g., GCP IAM) can
  expose roles and credentials; the permissions of a specific role can be changed without making
  changes to (say) the application layer.

We advocate splitting infrastructure up into (roughly) 6 stacks of resources. As we will see, this is
particularly easy with Pulumi, as the notion of a [Pulumi
stack]({{< relref "/docs/intro/concepts/organizing-stacks-projects.md" >}}) was specifically designed for
this use case.

<center><img src="/images/docs/quickstart/kubernetes/cake.svg" width="670"></center>

## 1. Identity

Identities and role definitions for organizations and CI/CD are required before anyone can provision
anything. This is a requirement for every production Kubernetes deployment.

One side-effect of isolating resources into loosely-coupled stacks is that we
have the opportunity to grant **minimal permissions** based on need. (See also
[principle of least
privilege](https://en.m.wikipedia.org/wiki/Principleofleastprivilege)).

Typically the identity stack looks like:

1. **AWS/Azure/GCP identities and roles for the team.** (e.g., [AWS IAM][aws-iam], [GCP
   IAM][gcp-iam], [Azure AD][azure-ad].) For example, the databases team typically gets only
   administrative permissions for the datastores, while an app team might only get cluster
   developer permissions.
1. **AWS/Azure/GCP service accounts for CI/CD.** While IAM roles and Active Directory accounts
   describe identity of users, service accounts grant an identity for workloads, e.g. Storage
   CI/CD. The identity stack provisions these as well, with similarly minimal permissions. For
   example, the storage infrastructure service account may only have administrative permissions in its given namespace.

## 2. Managed Infrastructure

Provisioning shared, managed infrastructure is required to configure the
cluster. At minimum, this typically this includes networking infrastructure,
and can often include a managed datastore (e.g., [Aurora][aurora],
[Cloud SQL][cloud-sql], [CosmosDB][cosmos-db]) along with other cloud services such as VMs, registries, data pipelines, and data warehouses.

## 3. Kubernetes Cluster 

Provision the managed Kubernetes cluster on [EKS][eks], [GKE][gke], or [AKS][aks],
and configure it with the desired settings and defaults.

Typically this also involves provisioning Kubernetes cluster infrastructure
such as `Namespaces`, `Roles` , `RoleBindings`, `Quotas` etc.

## 4. Cluster Services

With a running, vanilla cluster you should install any Kubernetes cluster-scoped
services that will be shared by a subset or all cluster users.

At a minimum, services include centralized cluster and app-based logging, and often
include monitoring, policies, registries, and service meshes.

## 5. App Services

Configure any Kubernetes app-scoped services that will be shared
by a subset or all users with deployment permissions.

At a minimum, app services include ingress controllers, and often include DNS and TLS
certificate managers, and app pipelines.

## 6. Apps

Deploy applications and workloads into the cluster.

[post-mortems]: https://danluu.com/postmortem-lessons/

[aws-iam]: https://aws.amazon.com/iam/
[gcp-iam]: https://cloud.google.com/iam/
[azure-ad]: https://azure.microsoft.com/en-us/services/active-directory/

[eks]: https://aws.amazon.com/eks/
[gke]: https://cloud.google.com/kubernetes-engine/
[aks]: https://docs.microsoft.com/en-us/azure/aks/

[aurora]: https://aws.amazon.com/rds/aurora/
[cloud-sql]: https://cloud.google.com/sql/
[cosmos-db]: https://azure.microsoft.com/en-us/services/cosmos-db/

---
title: A Prod-First Architecture for Kubernetes _Teams_
---

Infrastructure mis-configuration probably accounts for the most significant subset of serious
production outages in major systems. Some [reasonable estimates][post-mortems] put the fraction in
the range of 40-50%.

Many of these failure modes are trivially preventable. The primary objective of this reference
architecture is to create sensible defaults that make many of these issues either impossible, or
dramatically less likely.

Our most effective tools in accomplishing this is to **separate resources into loosely-coupled,
independently-managable sets, based on _risk_ and _functionality_.**

There are many benefits to this approach:

* **Faster release velocity.** Modern infrastructure-as-code tools (_e.g._, Pulumi, Terraform) can
  take tens of minutes to generate large plans. Splitting up configuration into well-scoped modules
  is _always_ more time-efficient.
* **Tractable plans.** It is markedly easier to notice that you're destroying your primary datastore
  in a 30-line plan than a 900-line plan.
* **Users get permissions they _need_ rather than global admin permissions.**
* **Limited blast radius.** Separating (_e.g._) app and storage configration means that the app team
  can't accidentally destroy the primary datastore.
* **Independently managable.** For example, the identity stack (containing, _e.g._, GCP IAM) can
  expose roles and credentials; the permissions of a specific role can be changed without making
  changes to (say) the application layer.

And so on.

We advocate splitting infrastructure up into (roughly) 3 sets of resources. As we will see, this is
particularly easy with Pulumi, as the notion of a [Pulumi
stack](https://pulumi.io/reference/organizing-stacks-projects.html) was specifically designed for
this use case.

An explanation of the 3 stacks follows the diagram. In the next section, we begin to provision and
configure each of these stacks.

<img src="/images/k8s-the-prod-way/kube-arch.png">

## 1. Identity

Identities and role definitions for organizations and CI/CD are required before anyone can provision
anything. This is a requirement for every production Kubernetes deployment.

One side-effect of isolating resources into loosely-coupled stacks is that we
have the opportunity to grant **minimal permissions** based on need. (See also
[principle of least
privilege](https://en.m.wikipedia.org/wiki/Principle_of_least_privilege)).

Typically the identity stack looks something like this:

1. **AWS/Azure/GCP identities and roles for the team.** (_e.g._, [AWS IAM][aws-iam], [GCP
   IAM][gcp-iam], [Azure AD][azure-ad].) For example, the databases team typically gets _only_
   administrative permissions for the datastores, while an app team might _only_ get cluster
   developer permissions on for (_e.g._) GKE.
1. **AWS/Azure/GCP service accounts for CI/CD.** While IAM roles and Active Directory accounts
   describe identity of users, service accounts grant an identity for _workloads_, _e.g._, "Storage
   CI/CD." The identity stack provisions these as well, with similarly minimal permissions. For
   example, the storage infrastructure service account has _only_ administrative permissions, _etc_.

## 2. Shared, managed infrastructure (_e.g._, compute, networking, storage)

The next step is to provision all shared, managed infrastructure. At minimum, this typically this
includes networking infrastructure and a managed Kubernetes platform (_e.g._, [EKS][eks],
[GKE][gke], [AKS][aks]), and frequently also involves a managed datastore (_e.g._, [Aurora][aurora],
[Cloud SQL][cloud-sql], [CosmosDB][cosmos-db]).

Typically this also involves provisioning Kubernetes cluster infrastructure -- things like
`Namespace`s, `ClusterRoleBinding`s, and so on.

In (1), we provisioned a service account with admin permissions to each of the managed
infrastructure offerings we wish to use. This is used in CI/CD. Typically all changes to shared,
managed infrastructure are executed by this service account.

## 3. Applications

Finally, using the service account with Kubernetes developer permissions provisioned in (1), and
credentials to shared, managed infrastructure provisioned in (2) (_e.g._, kubeconfig files, database
credentials, and so on), we can provision applications.



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

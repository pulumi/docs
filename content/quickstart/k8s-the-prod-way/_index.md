---
title: Kubernetes the Prod Way
---

**Kubernetes the Prod Way** is a tutorial, reference architecture, and collection of prod-first code
examples that demonstrate industry best-practices for **using Kubernetes** in contexts where an
**organization of people** must ship **production applications.**

For example: in an organization, we typically expect identity (_e.g._, [AWS IAM][aws-iam], [GCP
IAM][gcp-iam], [Azure AD][azure-ad]), compute (_e.g._, [EKS][eks], [GKE][gke], [AKS][aks]), storage
(_e.g._, [Aurora][aurora], [Cloud SQL][cloud-sql], [CosmosDB][cosmos-db]), and networking to be
provisioned and "owned" by separate people, and perhaps separate teams. But, when an app team
deploys a service, we expect all of these components to work seamlessly together.

**Kubernetes the Prod Way** will show you, using batteries-included examples, how to **provision**
and **use** these technologies together in a way that maintains high release velocity, without
sacrificing security, governance, or stability.

Examples are provided for each of: **AWS, GCP, and Azure.** In the future, we will also provide
examples for common on-prem technology, such as VMWare vSphere.

## Target Audience

This tutorial is aimed at people who are planning to support production applications running on
Kubernetes, particularly those looking for concrete guidance on how to set up infrastructure so that
teams can operate quickly, effectively, and safely.

## Contents

The labs in Kubernetes the Prod Way are built using [Pulumi][pulumi], a tool that allows you to
provision and configure cloud infrastructure, including [Amazon Web Services][aws] (AWS), [Microsoft
Azure][azure], [Google Cloud Platform][gcp] (GCP), and Kubernetes.

With that said, nearly all of the lessons learned could be applied using other tools as well, and
there is very little that is specific to Pulumi.

Kubernetes the Prod Way is organized as a series of labs. These labs cover everything from
bootstrapping IAM roles, to provisioning compute, storage, and networking, to deploying applications
on top of Kubernetes.

* [Prerequisites]({{< relref "prerequisites.md" >}})
* [A Production Architecture for _Teams_]({{< relref "architecture.md" >}})
* [Lab 1: Bootstrapping Identity]({{< relref "identity.md" >}})
* [Lab 2: Provisioning Environments]({{< relref "infrastructure.md" >}})
* [Lab 3: Provisioning Applications]({{< relref "app.md" >}})
* Lab 4: Setting Up CI/CD
* Lab 5: Configuring Standard Kubernetes Infrastructure (coming soon!)
* Lab 6: Testing your infrastructure (coming soon!)


[aws-iam]: https://aws.amazon.com/iam/
[gcp-iam]: https://cloud.google.com/iam/
[azure-ad]: https://azure.microsoft.com/en-us/services/active-directory/

[eks]: https://aws.amazon.com/eks/
[gke]: https://cloud.google.com/kubernetes-engine/
[aks]: https://docs.microsoft.com/en-us/azure/aks/

[aurora]: https://aws.amazon.com/rds/aurora/
[cloud-sql]: https://cloud.google.com/sql/
[cosmos-db]: https://azure.microsoft.com/en-us/services/cosmos-db/

[pulumi]: https://www.pulumi.com/

[aws]: https://aws.amazon.com/
[azure]: https://azure.microsoft.com/en-us/
[gcp]: https://cloud.google.com/

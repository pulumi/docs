---
title: "Introducing Crosswalk for Kubernetes"
date: "2019-11-19"
meta_desc: "Introduction to Crosswalk for Kubernetes by Pulumi. A collection of best practices for Kubernetes in code."
meta_image: ""
authors: ["sophia-parafina"]
tags: ["Kubernetes","Crosswalk"]
---

Running Kubernetes in production can be challenging. However, there are common patterns of usage informed by best practices that we can use to successfully run applications on Kubernetes in production. Pulumi has collected these common patterns into tasks. Crosswalk for Kubernetes is a set of tasks to configure, deploy, and manage Kubernetes in production.

Tasks are segmented by operations and belong to one of the six stacks outlined above. The Pulumi code for each stack is available and linked at the top of each task.

Together, the docs and stack code provide a reference architecture to operate and use Kubernetes in production across a team using industry best-practices.

At the core of this architecture is a simple idea: that we should separate resources into loosely-coupled, independently-manageable sets, based on risk and functionality.

## Crosswalk 

We suggest splitting infrastructure up into (roughly) six Pulumi stacks of resources.

1. Identity
Identities and role definitions for organizations and CI/CD are required before anyone can provision anything. This is a requirement for every production Kubernetes deployment.

By isolating resources into loosely-coupled stacks, we can grant minimal permissions based on the principle of least privilege.

The identity stack typically contains:

Identities and roles for the team e.g. AWS IAM, GCP IAM, Azure AD.

For example, the database team typically gets only administrative permissions for the datastores, while an app team might only get cluster developer permissions.

Service Accounts for bots and CI/CD.

While IAM roles and Active Directory accounts describe identity of users, service accounts grant an identity for workloads, e.g. Storage CI/CD.

2. Managed Infrastructure
Provisioning shared, managed infrastructure is required to configure the cluster.

At a minimum, this typically includes networking infrastructure, and can often include storage backends along with other cloud services such as VMs, registries, data pipelines, and data warehouses.

3. Kubernetes Cluster
Configuring and provision the Kubernetes cluster with the desired settings and defaults.

This also typically involves provisioning the Kubernetes cluster infrastructure with API resources such as Namespaces, Roles , RoleBindings, and Quotas.

Using a managed Kubernetes cluster on EKS, GKE, or AKS is the easiest recommended way to get started with deploying a cluster.

4. Cluster Services
With a running, vanilla cluster you can install any Kubernetes cluster-scoped services that will be shared by a subset or all cluster users.

At a minimum, services that should be installed include centralized cluster and app-based logging, and often include monitoring, policies, and service meshes.

5. App Services
Configure any Kubernetes app-scoped services that will be shared by a subset or all users with deployment permissions.

App services tend to include managed datastores (e.g. RDS, Cloud SQL, and CosmosDB), ingress controllers, DNS managers, TLS certificate managers, and app pipelines.

6. Apps
Deploy applications and workloads into the cluster.
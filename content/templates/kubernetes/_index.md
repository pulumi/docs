---
title_tag: Templates for Deploying Kubernetes Clusters
title: "Kubernetes Cluster Templates"
layout: overview
schema_type: faq
description: Pulumi templates for Kubernetes clusters and supporting infrastructure on AWS, Azure, and Google Cloud, in your language of choice.
meta_desc: Deploy Kubernetes clusters and supporting infrastructure on AWS, Azure, or Google Cloud with Pulumi Kubernetes templates.
meta_image: meta.png
weight: 98
---

## About these templates

### What is Kubernetes?

[Kubernetes](/kubernetes) is an open-source container orchestration platform. It runs a control plane that schedules, deploys, and scales containerized workloads across a cluster of machines using a declarative, desired-state model. Kubernetes is portable across clouds, scales horizontally, and supports a large ecosystem of extensions through Helm charts and Custom Resource Definitions.

### Which managed Kubernetes service should I use on each cloud?

Each major cloud offers a managed control plane so you don't have to operate Kubernetes yourself:

- **AWS**: [Amazon EKS](/registry/packages/eks/api-docs/cluster/) — runs your workloads on either EC2 nodes you manage or [AWS Fargate](/registry/packages/awsx/api-docs/ecs/fargateservice/) serverless capacity.
- **Azure**: [Azure Kubernetes Service (AKS)](/registry/packages/azure-native/api-docs/containerservice/managedcluster) — integrates with Azure Active Directory and Azure Monitor.
- **Google Cloud**: [Google Kubernetes Engine (GKE)](/registry/packages/gcp/api-docs/container/cluster) — integrates tightly with the rest of Google Cloud and supports Autopilot for fully managed nodes.

### How do I deploy a Kubernetes cluster with Pulumi?

Use one of the Kubernetes Cluster templates above to scaffold a Pulumi project that provisions a managed cluster and the surrounding infrastructure (VPC, subnets, IAM, node pools). Each template deploys end to end with `pulumi new` followed by `pulumi up` and exports a `kubeconfig` you can use immediately with `kubectl`.

### How do I deploy applications onto an existing cluster?

Once your cluster is running, the [Kubernetes Application templates](/templates/kubernetes-application/) give you a starting point for deploying workloads — either a [Helm chart](/templates/kubernetes-application/helm-chart/) or a [Kubernetes Deployment + Service](/templates/kubernetes-application/web-application/) — using the same language as your cluster's infrastructure code.

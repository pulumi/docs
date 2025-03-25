---
title: "Pulumi's Latest Kubernetes Updates from KubeCon North America"
allow_long_title: true
date: 2024-11-12T08:00:00-00:00
draft: false
meta_desc: Inspired by KubeCon North America 2024, this post presents a collection
  of recent Kubernetes-focused updates to Pulumi software
meta_image: meta.png
authors:
  - gavin-johnson
tags:
  - kubecon
  - kubernetes
  - conferences
aliases:
  - /blog/kubecon-2024-launches
search:
  keywords:
    - north
    - kubernetes
    - '2024'
    - america
    - kubecon
    - updates
    - presents
---

Pulumi is excited to be at KubeCon North America this week, the premier event for all things Kubernetes and cloud-native. KubeCon is the gathering place for developers, enterprises, and cloud native experts to meet and further the education and advancement of Kubernetes and cloud native computing. At Pulumi, we are strongly committed to Kubernetes and continue to support the ecosystem with infrastructure management solutions that empower teams to automate, secure, and manage Kubernetes at scale.

## Come See Us at KubeCon

Stop by the Pulumi KubeCon booth R1 this week to chat with experts on the Pulumi team. If you can't make it to KubeCon, [join our workshop](https://www.pulumi.com/resources/pulumi-kubernetes-better-together/) on November 18, 2024, to see how easy it is to manage Kubernetes with Pulumi.


## Recent Pulumi Kubernetes Updates

We've launched several new and improved capabilities recently to serve Kubernetes users and to make it easier than ever to automate, secure, manage, and scale clusters and workloads.

### Pulumi Kubernetes Operator 2.0

The **Pulumi Kubernetes Operator** automates the deployment and management of infrastructure by running Pulumi programs directly in Kubernetes clusters, enabling teams to manage cloud resources alongside Kubernetes-native resources. The **Pulumi Kubernetes Operator 2.0** is a significant upgrade that introduces dedicated "workspace" pods for each Stack resource, effectively isolating each stack’s compute and memory resources, improving the isolation of secrets, and opening up new customization options. The operator now scales horizontally, enhancing performance and enabling teams to manage complex Kubernetes setups with greater reliability.

[Read more about the Pulumi Kubernetes Operator 2.0](https://www.pulumi.com/blog/pulumi-kubernetes-operator-2-0/)


### Pulumi ESC Secrets in Kubernetes with the External Secrets Operator

**Pulumi ESC integrates with the External Secrets Operator (ESO)** to securely access secrets from Pulumi ESC in Kubernetes. This enables a secure, automated way to manage and use secrets from Pulumi ESC across Kubernetes clusters, reducing the need for manual secrets maintenance and potential security risks from the local storage of secrets in manifest files.

[Read more about using Pulumi ESC secrets in Kubernetes with the External Secrets Operator](https://www.pulumi.com/blog/cloud-native-secret-management-with-pulumi-esc-and-external-secrets-operator/)


### Pulumi EKS Provider Version 3.0.0

The **Pulumi EKS Provider Version 3.0.0** simplifies Amazon Elastic Kubernetes Service (EKS) cluster management with improvements in flexibility and security and the introduction of new features to enhance the Kubernetes experience on AWS. This update allows users to more easily customize networking, scaling, and security configurations for EKS clusters, streamlining deployment and management workflows.

[Read more about the Pulumi EKS Provider Version 3.0.0](https://www.pulumi.com/blog/eks-v3-release/)


### Kubernetes-Native Support for Customer-Managed Pulumi Deployments Agents

**Kubernetes-native support for customer-managed Pulumi Deployments agents** allows organizations to host Pulumi Deployments agents within their Kubernetes environments enhancing the flexibility and control they have over their infrastructure deployments. Kubernetes-native support offers greater flexibility, scalability, and security for self-hosted Pulumi Deployments agents.

[Read more about Kubernetes-native support for customer-managed Pulumi Deployments agents](https://www.pulumi.com/blog/customer-managed-agents-kubernetes/)


### Improved Kubernetes await Logic in the Pulumi Kubernetes Provider

**Improved Kubernetes await logic in the Pulumi Kubernetes provider** enables more reliable handling of resource dependencies and synchronization when managing Kubernetes resources. This update makes it easier to ensure that resources are created or updated in the correct order, improving the overall predictability and stability of Kubernetes deployments.

[Read more about improved Kubernetes await logic in the Pulumi Kubernetes provider](https://www.pulumi.com/blog/improved-kubernetes-await-logic/)


### Helm Chart v4 Resource in the Pulumi Kubernetes Provider

The **Helm Chart v4 resource in the Pulumi Kubernetes provider** introduces several new capabilities for users managing Helm charts. It allows for more sophisticated chart management, including enhanced support for dependencies between charts, applying transformations to chart resources, and the ability to handle Kubernetes namespaces more flexibly​.

[Read more about the Helm Chart v4 resource in the Pulumi Kubernetes provider](https://www.pulumi.com/blog/kubernetes-chart-v4/)


### Revamped crd2pulumi

**[crd2pulumi](https://github.com/pulumi/crd2pulumi)** is a CLI tool that generates strongly-typed Pulumi resources from Kubernetes CustomResourceDefinitions (CRDs), enabling better IDE support, type safety, and autocompletion for managing complex CRDs​. It was revamped to enhance its handling of CRDs with multiple versions, refine the structure of its generated code, and offer more flexible output paths for smoother integration into Pulumi programs.

[Learn about the crd2pulumi and its recent updates](https://github.com/pulumi/crd2pulumi/pull/143)

---
title: "Amazon EKS Hybrid Nodes: Bridging Cloud and On-Premises"
date: 2024-12-01T15:06:25-05:00
draft: false
meta_desc: "Manage Amazon EKS Hybrid Nodes with Pulumi: Use AWS's control plane while
  running workloads on-premises or at the edge."
meta_image: meta.png
authors:
  - josh-kodroff
tags:
  - aws
  - kubernetes
search:
  keywords:
    - EKS
    - AWS
    - Hybrid Nodes
    - Infrastructure Management
    - Kubernetes Environments
---

AWS has introduced a new feature for Amazon Elastic Kubernetes Service (EKS): [Amazon EKS Hybrid Nodes](https://aws.amazon.com/eks/hybrid-nodes/?trk=f4bc0305-3e3d-470e-bbb5-02917c6bc4c6&sc_channel=el). This addition to the Amazon EKS Hybrid/Edge portfolio allows organizations to maintain their Kubernetes control plane in AWS while running workloads on-premises or at the edge. This hybrid approach offers the best of both worlds - AWS's reliable and scalable control plane management combined with the flexibility to run workloads wherever they make the most sense for your business.

Amazon EKS Hybrid Nodes are particularly valuable for organizations that need to keep certain workloads on-premises due to data sovereignty requirements, latency concerns, or existing infrastructure investments. By extending EKS to support on-premises workloads, AWS is addressing a critical need in the enterprise market, especially for industries like manufacturing, telecommunications, and healthcare that often require local data processing.

Pulumi's strategic partnership with AWS has always focused on making cloud infrastructure easier to manage through modern infrastructure as code. As an EKS Service Ready Partner, Pulumi provides first-class support for AWS services, including EKS. This partnership ensures that as AWS releases new features like EKS Hybrid Nodes, Pulumi users can quickly adopt and integrate them into their infrastructure management workflows.
Managing Hybrid Environments with Pulumi

Pulumi's infrastructure as code platform is perfectly positioned to help organizations manage their hybrid EKS environments. Using Pulumi, teams can define and manage both their [EKS clusters](/registry/packages/eks/) and [Kubernetes](/registry/packages/kubernetes/) resources using their favorite programming languages, bringing software engineering practices to infrastructure management. This includes managing Hybrid Node configurations, networking setup, and security policies across both cloud and on-premises environments.

Pulumi's Environments Secrets and Config (ESC) adds another layer of capability to Hybrid Node deployments. Operators can securely manage OIDC IAM credentials, kubeconfig files and other sensitive credentials through ESC, ensuring secure access to EKS clusters regardless of where the workloads run. Furthermore, pods running on Hybrid Nodes can consume ESC secrets through Pulumi ESC’s integration with the [Kubernetes External Secrets Operator](/docs/esc/integrations/kubernetes/external-secrets-operator/), maintaining a consistent secrets management approach across your entire hybrid infrastructure.

Pulumi’s solutions for EKS Anywhere are automatically validated across a variety of EKS deployment models (including cloud, VMWare, Nutanix, and bare metal) via [AWS’ Conformitron framework](https://aws.amazon.com/blogs/containers/conformitron-validate-third-party-software-with-amazon-eks-and-amazon-eks-anywhere/). The framework makes it simple for AWS partners to test their offerings across common customer environments without having to provision these environments themselves.

## Automation and Operations

Organizations can leverage Pulumi's CI/CD capabilities within their Hybrid Node environment. [Pulumi Deployments](/docs/pulumi-cloud/deployments/) or the [Pulumi Kubernetes Operator](/docs/iac/packages-and-automation/continuous-delivery/pulumi-kubernetes-operator/) can run directly on Hybrid Nodes, enabling automated infrastructure management from within your on-premises environment. This approach allows for consistent infrastructure automation while respecting network boundaries and security requirements.

## Summary

The combination of EKS Hybrid Nodes and Pulumi's infrastructure as code platform provides organizations with a powerful solution for managing hybrid Kubernetes environments. As this feature continues to evolve, Pulumi will provide comprehensive support for deploying and managing Hybrid Node configurations, making it easier for teams to adopt and maintain hybrid architectures while modernizing their application workloads.

Stay tuned for upcoming Pulumi examples for managing EKS Hybrid Nodes, which will enable you to manage your hybrid Kubernetes infrastructure using your preferred programming language, complete with type safety, testing capabilities, and modern development practices.

If you’d like to learn more about how you can harness the power of EKS with Pulumi, check out [the latest version of our EKS package](/blog/eks-v3-release/) or [join us for our AWS Immersion Day workshop following re:Invent 2024](/events/aws-immersion-day-platform-engineering/).

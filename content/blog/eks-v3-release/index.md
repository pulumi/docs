---
title: "Pulumi EKS Provider Version 3.0.0"
date: 2024-10-17T17:32:03+02:00
draft: false
meta_desc: "Release of the next version of the Pulumi Provider for AWS EKS"
meta_image: meta.png
authors:
  - florian-stadler
tags:
  - aws
  - eks
  - release
search:
  keywords:
    - EKS
    - AWS
    - Amazon Linux
    - Managed Addons
---

The latest major release of the Pulumi EKS Provider is available now!

This release delivers significant improvements in flexibility, security and introduces new features to enhance your Kubernetes experience on AWS.
AWS recently announced the deprecation of two features used by default in Pulumi EKS: the aws-auth ConfigMap and the AL2 operating system. Pulumi EKS v3 addresses these deprecations, enhances the maintainability of the provider, and aligns it with EKS best practices.

<!--more-->

Here are a few links to help you get started if you are new to Pulumi:

- [EKS Setup & Installation](https://www.pulumi.com/registry/packages/eks/installation-configuration/) - Instructions on installing and configuring the Pulumi EKS provider
- [EKS How-to Guides](https://www.pulumi.com/registry/packages/kubernetes/how-to-guides/eks/) - Learn how to use the EKS provider to provision and manage Kubernetes clusters on AWS
- [Pulumi AI](https://www.pulumi.com/ai) - Ask Pulumi AI to help you create a new EKS project

## Key Highlights of EKS V3

1. **Support for Amazon Linux 2023 (AL2023) and Bottlerocket Operating Systems**: Enhanced operating system options for node groups, allowing you to choose the OS that best fits your workloads and compliance needs. This addresses the upcoming deprecation of Amazon Linux 2 (AL2).

2. **Access Entries for IAM Integration**: Enables replacement of the deprecated aws-auth ConfigMap with Access Entries for managing Kubernetes authentication.

3. **EKS Managed Addons**: Simplified management of `vpc-cni`, `coredns`, and `kube-proxy` as EKS managed addons.

4. **EKS Security Groups for Pods and Network Policies**: Enhanced network security and control within EKS clusters.

## New Features and Improvements

### Support for Amazon Linux 2023 and Bottlerocket

We have expanded the operating system options for node groups in EKS v3 to address the upcoming deprecation of Amazon Linux 2 (AL2). You can now choose between Amazon Linux 2 (deprecated), Amazon Linux 2023 and Bottlerocket for your EKS nodes. This flexibility allows you to select the OS that best fits your workloads, security requirements, and compliance needs, while ensuring you are using a supported and actively maintained operating system. We've introduced a new `operatingSystem` property for node groups to facilitate this choice.

### Access Entries for IAM Integration

AWS has introduced [Access Entries](https://docs.aws.amazon.com/eks/latest/userguide/access-entries.html) as a new method for granting IAM principals access to Kubernetes resources. This approach relies solely on AWS resources for managing Kubernetes auth, replacing the deprecated `aws-auth` ConfigMap. You can now leverage Access Entries by setting the `authenticationMode` to `API` in your cluster configuration.

### EKS Managed Addons

The EKS cluster components `vpc-cni`, `coredns`, and `kube-proxy` are now configured as EKS managed addons. This change simplifies management, especially for clusters with private API endpoints, and ensures that these critical components stay up to date automatically. Additionally it removes the dependency on `kubectl`, allowing pulumi-native management of clusters.

### Cluster Autoscaler Integration

Pulumi EKS v3 introduces better support for the Kubernetes Cluster Autoscaler. A new `ignoreScalingChanges` parameter for node groups allows Pulumi to ignore external scaling changes, facilitating seamless integration with dynamic scaling solutions.

### EKS Security Groups for Pods and Network Policies

We've added support for EKS security groups for pods ([example](https://github.com/pulumi/pulumi-eks/tree/master/examples/pod-security-groups)) and EKS Network Policies ([example](https://github.com/pulumi/pulumi-eks/tree/master/examples/network-policies)), providing more granular control over pod-to-pod and pod-to-external network communication within your EKS clusters.

## Migration Guide

To help you transition smoothly, we've prepared a migration guide with these key steps:

1. Update node groups to use AL2023 or explicitly configure AL2 if needed.
2. Replace the deprecated `NodeGroup` component with `NodeGroupV2`.
3. Update your code to handle new output types for certain properties.
4. Review and update your use of default security groups, which can now be disabled.

Please refer to our [EKS v3 Migration Documentation](https://www.pulumi.com/registry/packages/eks/how-to-guides/v3-migration/) for a detailed guide.

## Conclusion

Pulumi EKS v3 represents a significant step forward in managing Kubernetes clusters on AWS, empowering you to build and manage more robust and efficient EKS clusters.

We encourage all users to upgrade to this latest version to take advantage of these improvements and ensure your EKS deployments remain secure and up-to-date.

For more information on getting started with Pulumi EKS v3, check out our [documentation](https://www.pulumi.com/registry/packages/eks/) or join our [community Slack](https://slack.pulumi.com/) for support and discussions.

Happy clustering with Pulumi EKS v3!

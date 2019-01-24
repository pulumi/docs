---
title: Node.js Packages
---

The Pulumi SDK package is used for accessing the core programming model around resources, configuration, etc. directly:

* [Pulumi SDK `@pulumi/pulumi`](@pulumi/pulumi)

### Cloud Providers

Each cloud vendor has a dedicated package for deploying resources to it:

* [Amazon Web Services (`@pulumi/aws`)](@pulumi/aws)
* [Microsoft Azure (`@pulumi/azure`)](@pulumi/azure)
* [Google Cloud Platform (`@pulumi/gcp`)](@pulumi/gcp)
* [Kubernetes (`@pulumi/kubernetes`)](@pulumi/kubernetes)
* [OpenStack (`@pulumi/openstack`)](@pulumi/openstack)
* [vSphere (`@pulumi/vsphere`)](@pulumi/vsphere)

### Cloud-Agnostic Packages

Pulumi offers highly productive, cloud-agnostic packages, for container and serverless oriented programming.  The
`@pulumi/cloud` package provides common abstractions, while the individual implementation packages supply the
cloud-specific behavior, in addition to extensions for accessing more cloud-specific controls:

* [Pulumi Cloud Framework (`@pulumi/cloud`)](@pulumi/cloud)
* [Pulumi Cloud Framework on AWS (`@pulumi/cloud-aws`)](@pulumi/cloud-aws)
* [Pulumi Cloud Framework on Azure (`@pulumi/cloud-azure`)](@pulumi/cloud-azure)

### Helper Libraries

These libraries help with common cloud programming patterns and practices:

* [AWS Infrastructure Components (`@pulumi/aws-infra`)](@pulumi/aws-infra): common AWS networking and
  infrastructure patterns
* [AWS EKS Cluster (`@pulumi/eks`)](@pulumi/eks): simple creation and management of AWS EKS clusters
* [Azure Serverless Components (`@pulumi/azure-serverless`)](@pulumi/azure-serverless): components for writing
  serverless applications on Azure

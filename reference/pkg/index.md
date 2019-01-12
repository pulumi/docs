---
title: API Reference
---

{% include mini-toc.html %}

All Pulumi libraries are distributed in your chosen language's package manager, even those packages that define
cloud resource definitions. That means NPM for Node.js and PyPI for Python, for instance. There is a dedicated
package for each cloud that includes access to its full capabilities, including containers, serverless functions,
infrastructure, data services, and more.

In addition to the cloud packages, Pulumi offers many convenience libraries that make common tasks easier, like
setting up a network, creating a Kubernetes cluster, and building and publishing containers to private registries.

These packages can be mixed to enable multi-cloud and a spectrum of control to productivity:

![Pulumi Library Architecture](/images/reference/pkg-arch-layers.png)

Below you will find a list of current packages in each language with links to their full documentation.

## Pulumi SDK

The Pulumi SDK package is used for accessing the core programming model around resources, configuration, etc. directly:

* [Pulumi SDK `@pulumi/pulumi`](nodejs/@pulumi/pulumi)

## Cloud Providers

Each cloud vendor has a dedicated package for deploying resources to it:

* [Amazon Web Services (`@pulumi/aws`)](nodejs/@pulumi/aws)
* [Microsoft Azure (`@pulumi/azure`)](nodejs/@pulumi/azure)
* [Google Cloud Platform (`@pulumi/gcp`)](nodejs/@pulumi/gcp)
* [Kubernetes (`@pulumi/kubernetes`)](nodejs/@pulumi/kubernetes)
* [OpenStack (`@pulumi/openstack`)](nodejs/@pulumi/openstack)
* [vSphere (`@pulumi/vsphere`)](nodejs/@pulumi/vsphere)

## Multi-Cloud Packages

Pulumi offers highly productive, cloud-agnostic packages, for container and serverless oriented programming.  The
`@pulumi/cloud` package provides common abstractions, while the individual implementation packages supply the
cloud-specific behavior, in addition to extensions for accessing more cloud-specific controls:

* [Pulumi Cloud Framework (`@pulumi/cloud`)](nodejs/@pulumi/cloud)
* [Pulumi Cloud Framework on AWS (`@pulumi/cloud-aws`)](nodejs/@pulumi/cloud-aws)
* [Pulumi Cloud Framework on Azure (`@pulumi/cloud-azure`)](nodejs/@pulumi/cloud-azure)

## Helper Libraries

These libraries help with common cloud programming patterns and practices:

* [AWS Infrastructure Components (`@pulumi/aws-infra`)](nodejs/@pulumi/aws-infra): common AWS networking and
  infrastructure patterns
* [AWS EKS Cluster (`@pulumi/eks`)](nodejs/@pulumi/eks): simple creation and management of AWS EKS clusters
* [Azure Serverless Components (`@pulumi/azure-serverless`)](nodejs/@pulumi/azure-serverless): components for writing
  serverless applications on Azure

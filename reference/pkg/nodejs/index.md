---
title: Node.js Packages
---



### General Purpose Packages

The Pulumi SDK package is used for accessing the core programming model around resources, configuration, etc. 
directly. Additional general purpose packages can be used across all cloud platforms:

* [Pulumi SDK `@pulumi/pulumi`](@pulumi/pulumi)
* [Docker (`@pulumi/docker`)](@pulumi/docker)
* [Random (`@pulumi/random`)](@pulumi/random)

### Cloud Providers

Each cloud vendor has a dedicated package for deploying resources to it:

* [Amazon Web Services (`@pulumi/aws`)](@pulumi/aws)
    * [AWS Extensions (`@pulumi/awsx`)](@pulumi/awsx): simpler interfaces for common AWS patterns
    * [AWS EKS Cluster (`@pulumi/eks`)](@pulumi/eks): simpler interface for working with AWS EKS
* [Microsoft Azure (`@pulumi/azure`)](@pulumi/azure)
    * [Azure Serverless Components (`@pulumi/azure-serverless`)](@pulumi/azure-serverless): simpler interfaces for
    serverless applications on Azure
* [Google Cloud Platform (`@pulumi/gcp`)](@pulumi/gcp)
* [Kubernetes (`@pulumi/kubernetes`)](@pulumi/kubernetes)
* [OpenStack (`@pulumi/openstack`)](@pulumi/openstack)
* [vSphere (`@pulumi/vsphere`)](@pulumi/vsphere)
* [Packet (`@pulumi/packet`)](@pulumi/packet)
* [F5 BigIP (`@pulumi/ftbigip`)](@pulumi/f5bigip)

### Cloud-Agnostic Packages

Pulumi offers a highly productive, cloud-agnostic package for container and serverless oriented programming in the
`@pulumi/cloud` package which currently allows writing applications once and deploying to either AWS or Azure.

* [Pulumi Cloud Framework (`@pulumi/cloud`)](@pulumi/cloud)

---
title: Node.js Packages
menu:
  reference:
    parent: api
    identifier: node
    name: Node.js
---

### General Purpose Packages

The Pulumi SDK package is used for accessing the core programming model around resources, configuration, etc. 
directly. Additional general purpose packages can be used across all cloud platforms:

* [Pulumi SDK `@pulumi/pulumi`]({{< relref "pulumi/pulumi" >}})
* [Docker (`@pulumi/docker`)]({{< relref "pulumi/docker" >}})
* [Random (`@pulumi/random`)]({{< relref "pulumi/random" >}})

### Cloud Providers

Each cloud vendor has a dedicated package for deploying resources to it:

* [Amazon Web Services (`@pulumi/aws`)]({{< relref "pulumi/aws" >}})
    * [AWS Extensions (`@pulumi/awsx`)]({{< relref "pulumi/awsx" >}}): simpler interfaces for common AWS patterns
    * [AWS EKS Cluster (`@pulumi/eks`)]({{< relref "pulumi/eks" >}}): simpler interface for working with AWS EKS
* [Microsoft Azure (`@pulumi/azure`)]({{< relref "pulumi/azure" >}})
    * [Azure Active Directory (`@pulumi/azuread`)]({{< relref "pulumi/azuread" >}})
* [Google Cloud Platform (`@pulumi/gcp`)]({{< relref "pulumi/gcp" >}})
* [Kubernetes (`@pulumi/kubernetes`)]({{< relref "pulumi/kubernetes" >}})
* [OpenStack (`@pulumi/openstack`)]({{< relref "pulumi/openstack" >}})
* [vSphere (`@pulumi/vsphere`)]({{< relref "pulumi/vsphere" >}})
* [Packet (`@pulumi/packet`)]({{< relref "pulumi/packet" >}})
* [F5 BigIP (`@pulumi/f5bigip`)]({{< relref "pulumi/f5bigip" >}})
* [Cloudflare (`@pulumi/cloudflare`)]({{< relref "pulumi/cloudflare" >}})

### Cloud-Agnostic Packages

Pulumi offers a highly productive, cloud-agnostic package for container and serverless oriented programming in the
`@pulumi/cloud` package which currently allows writing applications once and deploying to either AWS or Azure.

* [Pulumi Cloud Framework (`@pulumi/cloud`)]({{< relref "pulumi/cloud" >}})

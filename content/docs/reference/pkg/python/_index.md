---
title: Python Packages
menu:
  reference:
    parent: api
    identifier: python
    name: Python
---

### General Purpose Packages

The Pulumi SDK package is used for accessing the core programming model around resources, configuration, etc. 
directly. Additional general purpose packages can be used across all cloud platforms:

* [Pulumi SDK (`pulumi`)](pulumi)
* [Random (`pulumi_random`)](pulumi_random)

### Cloud Providers

Each cloud vendor has a dedicated package for deploying resources to it:

* [Amazon Web Services (`pulumi_aws`)](pulumi_aws)
* [Microsoft Azure (`pulumi_azure`)](pulumi_azure)
* [Google Cloud Platform (`pulumi_gcp`)](pulumi_gcp)
* [Kubernetes (`pulumi_kubernetes`)](pulumi_kubernetes)
* [OpenStack (`pulumi_openstack`)](pulumi_openstack)
* [vSphere (`pulumi_vsphere`)](pulumi_vsphere)
* [Packet (`pulumi_packet`)](pulumi_packet)
* [F5 BigIP (`pulumi_f5bigip`)](pulumi_f5bigip)
* [Cloudflare (`pulumi_cloudflare`)](pulumi_cloudflare)
* [DigitalOcean (`pulumi_digitalocean`)](pulumi_digitalocean)
* [GitLab (`pulumi_gitlab`)](pulumi_gitlab)

### Cloud-Agnostic Packages

Coming soon!

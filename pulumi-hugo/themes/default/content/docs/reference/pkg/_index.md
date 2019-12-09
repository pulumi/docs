---
title: API Reference
linktitle: API
menu:
  reference:
    name: API Reference
    weight: 2
---

Pulumi offers APIs for working with a wide variety of cloud platforms, as well
as higher-level APIs that make it easier to deliver cloud applications and
infrastructure.

These APIs are available as packages in your chosen language's package manager
---npm for TypeScript/JavaScript and PyPI for Python. There is a dedicated package for
each cloud that includes access to its full capabilities. In addition, Pulumi
offers many convenience packages that make common tasks easier, like setting
up a network, creating a Kubernetes cluster, and building and publishing containers
to private registries.

### Choose Your Language

{{< langchoose nogo >}}

### General Purpose Packages

The Pulumi SDK package is used for accessing the core programming model around resources, configuration, and other components
directly. Additional general purpose packages can be used across all cloud platforms:

{{% lang nodejs %}}
* [**Pulumi SDK** (`@pulumi/pulumi`)]({{< relref "nodejs/pulumi/pulumi" >}})
* [**Docker** (`@pulumi/docker`)]({{< relref "nodejs/pulumi/docker" >}})
* [**Policy** (`@pulumi/policy`) <span class="badge badge-preview">PREVIEW</span>]({{< relref "nodejs/pulumi/policy" >}})
* [**Random** (`@pulumi/random`)]({{< relref "nodejs/pulumi/random" >}})
{{% /lang %}}

{{% lang python %}}
* [**Pulumi SDK** (`pulumi`)]({{< relref "python/pulumi" >}})
* [**Docker** (`pulumi_docker`)]({{< relref "python/pulumi_docker" >}})
* [**Random** (`pulumi_random`)]({{< relref "python/pulumi_random" >}})
{{% /lang %}}

### Cloud Providers

Each cloud vendor has a dedicated package for deploying resources to it:

{{% lang nodejs %}}
* [**AWS** (`@pulumi/aws`)]({{< relref "nodejs/pulumi/aws" >}})
    * [**AWS Extensions** (`@pulumi/awsx`)]({{< relref "nodejs/pulumi/awsx" >}}) - simpler interfaces for common AWS patterns
    * [**AWS EKS Cluster** (`@pulumi/eks`)]({{< relref "nodejs/pulumi/eks" >}}) - simpler interface for working with AWS EKS
* [**Azure** (`@pulumi/azure`)]({{< relref "nodejs/pulumi/azure" >}})
    * [**Azure Active Directory** (`@pulumi/azuread`)]({{< relref "nodejs/pulumi/azuread" >}})
* [**Google Cloud** (`@pulumi/gcp`)]({{< relref "nodejs/pulumi/gcp" >}})
* [**Kubernetes** (`@pulumi/kubernetes`)]({{< relref "nodejs/pulumi/kubernetes" >}})
    * [**Kubernetes Extensions** (`@pulumi/kubernetesx`) <span class="badge badge-preview">PREVIEW</span>]({{< relref "nodejs/pulumi/kubernetesx" >}}) - simpler interface for working with Kubernetes

* [**Aiven** (`@pulumi/aiven`)]({{< relref "nodejs/pulumi/aiven" >}})
* [**CloudAMQP** (`@pulumi/cloudamqp`)]({{< relref "nodejs/pulumi/cloudamqp" >}})
* [**Cloudflare** (`@pulumi/cloudflare`)]({{< relref "nodejs/pulumi/cloudflare" >}})
* [**HashiCorp Consul** (`@pulumi/consul`)]({{< relref "nodejs/pulumi/consul" >}})
* [**Datadog** (`@pulumi/datadog`)]({{< relref "nodejs/pulumi/datadog" >}})
* [**DigitalOcean** (`@pulumi/digitalocean`)]({{< relref "nodejs/pulumi/digitalocean" >}})
* [**DNSimple** (`@pulumi/dnsimple`)]({{< relref "nodejs/pulumi/dnsimple" >}})
* [**Fastly** (`@pulumi/fastly`)]({{< relref "nodejs/pulumi/fastly" >}})
* [**F5 BigIP** (`@pulumi/f5bigip`)]({{< relref "nodejs/pulumi/f5bigip" >}})
* [**GitLab** (`@pulumi/gitlab`)]({{< relref "nodejs/pulumi/gitlab" >}})
* [**Kafka** (`@pulumi/kafka`)]({{< relref "nodejs/pulumi/kafka" >}})
* [**Linode** (`@pulumi/linode`)]({{< relref "nodejs/pulumi/linode" >}})
* [**MySQL** (`@pulumi/mysql`)]({{< relref "nodejs/pulumi/mysql" >}})
* [**New Relic** (`@pulumi/newrelic`)]({{< relref "nodejs/pulumi/newrelic" >}})
* [**Okta** (`@pulumi/okta`)]({{< relref "nodejs/pulumi/okta" >}})
* [**OpenStack** (`@pulumi/openstack`)]({{< relref "nodejs/pulumi/openstack" >}})
* [**Packet** (`@pulumi/packet`)]({{< relref "nodejs/pulumi/packet" >}})
* [**PostgreSQL** (`@pulumi/postgresql`)]({{< relref "nodejs/pulumi/postgresql" >}})
* [**SignalFX** (`@pulumi/signalfx`)]({{< relref "nodejs/pulumi/signalfx" >}})
* [**Terraform** (`@pulumi/terraform`)]({{< relref "nodejs/pulumi/terraform" >}})
* [**TLS** (`@pulumi/tls`)]({{< relref "nodejs/pulumi/tls" >}})
* [**Hashicorp Vault** (`@pulumi/vault`)]({{< relref "nodejs/pulumi/vault" >}})
* [**vSphere** (`@pulumi/vsphere`)]({{< relref "nodejs/pulumi/vsphere" >}})
{{% /lang %}}

{{% lang python %}}
* [**AWS** (`pulumi_aws`)]({{< relref "python/pulumi_aws" >}})
* [**Azure** (`pulumi_azure`)]({{< relref "python/pulumi_azure" >}})
    * [**Azure Active Directory** (`pulumi_azuread`)]({{< relref "python/pulumi_azuread" >}})
* [**Google Cloud** (`pulumi_gcp`)]({{< relref "python/pulumi_gcp" >}})
* [**Kubernetes** (`pulumi_kubernetes`)]({{< relref "python/pulumi_kubernetes" >}})

* [**Aiven** (`pulumi_aiven`)]({{< relref "python/pulumi_aiven" >}})
* [**CloudAMQP** (`pulumi_cloudamqp`)]({{< relref "python/pulumi_cloudamqp" >}})
* [**Cloudflare** (`pulumi_cloudflare`)]({{< relref "python/pulumi_cloudflare" >}})
* [**HashiCorp Consul** (`pulumi_consul`)]({{< relref "python/pulumi_consul" >}})
* [**Datadog** (`pulumi_datadog`)]({{< relref "python/pulumi_datadog" >}})
* [**DigitalOcean** (`pulumi_digitalocean`)]({{< relref "python/pulumi_digitalocean" >}})
* [**DNSimple** (`pulumi_dnsimple`)]({{< relref "python/pulumi_dnsimple" >}})
* [**Fastly** (`pulumi_fastly`)]({{< relref "python/pulumi_fastly" >}})
* [**F5 BigIP** (`pulumi_f5bigip`)]({{< relref "python/pulumi_f5bigip" >}})
* [**GitLab** (`pulumi_gitlab`)]({{< relref "python/pulumi_gitlab" >}})
* [**Kafka** (`pulumi_kafka`)]({{< relref "python/pulumi_kafka" >}})
* [**Linode** (`pulumi_linode`)]({{< relref "python/pulumi_linode" >}})
* [**MySQL** (`pulumi_mysql`)]({{< relref "python/pulumi_mysql" >}})
* [**New Relic** (`pulumi_newrelic`)]({{< relref "python/pulumi_newrelic" >}})
* [**Okta** (`pulumi_okta`)]({{< relref "python/pulumi_okta" >}})
* [**OpenStack** (`pulumi_openstack`)]({{< relref "python/pulumi_openstack" >}})
* [**Packet** (`pulumi_packet`)]({{< relref "python/pulumi_packet" >}})
* [**PostgreSQL** (`pulumi_postgresql`)]({{< relref "python/pulumi_postgresql" >}})
* [**SignalFX** (`pulumi_signalfx`)]({{< relref "python/pulumi_signalfx" >}})
* [**Terraform** (`pulumi_terraform`)]({{< relref "python/pulumi_terraform" >}})
* [**TLS** (`pulumi_tls`)]({{< relref "python/pulumi_tls" >}})
* [**Hashicorp Vault** (`pulumi_vault`)]({{< relref "python/pulumi_vault" >}})
* [**vSphere** (`pulumi_vsphere`)]({{< relref "python/pulumi_vsphere" >}})
{{% /lang %}}

### Cloud-Agnostic Packages

{{% lang nodejs %}}
Pulumi offers a highly productive, cloud-agnostic package for container and serverless programming in the
`@pulumi/cloud` package which currently allows writing applications once and deploying to either AWS or Azure.

* [**Pulumi Cloud Framework** (`@pulumi/cloud`) <span class="badge badge-preview">PREVIEW</span>]({{< relref "nodejs/pulumi/cloud" >}})
{{% /lang %}}

{{% lang python %}}
Coming soon!
{{% /lang %}}

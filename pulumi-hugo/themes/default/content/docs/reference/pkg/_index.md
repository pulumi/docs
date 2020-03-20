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

{{< langchoose csharp >}}

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

{{% lang go %}}
* [**Pulumi SDK** (`pulumi`)](https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi)
* [**Random** (`random`)](https://pkg.go.dev/github.com/pulumi/pulumi-random/sdk/go/random)
{{% /lang %}}

{{% lang csharp %}}
* [**Pulumi SDK** (`pulumi`)](/docs/reference/pkg/dotnet/Pulumi/Pulumi.html)
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
* [**Alibaba Cloud** (`@pulumi/alicloud`)]({{< relref "nodejs/pulumi/alicloud" >}})
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
* [**Keycloak** (`@pulumi/keycloak`)]({{< relref "nodejs/pulumi/keycloak" >}})
* [**Linode** (`@pulumi/linode`)]({{< relref "nodejs/pulumi/linode" >}})
* [**Mailgun** (`@pulumi/mailgun`)]({{< relref "nodejs/pulumi/mailgun" >}})
* [**MySQL** (`@pulumi/mysql`)]({{< relref "nodejs/pulumi/mysql" >}})
* [**New Relic** (`@pulumi/newrelic`)]({{< relref "nodejs/pulumi/newrelic" >}})
* [**Okta** (`@pulumi/okta`)]({{< relref "nodejs/pulumi/okta" >}})
* [**OpenStack** (`@pulumi/openstack`)]({{< relref "nodejs/pulumi/openstack" >}})
* [**Packet** (`@pulumi/packet`)]({{< relref "nodejs/pulumi/packet" >}})
* [**PostgreSQL** (`@pulumi/postgresql`)]({{< relref "nodejs/pulumi/postgresql" >}})
* [**RabbitMQ** (`@pulumi/rabbitmq`)]({{< relref "nodejs/pulumi/rabbitmq" >}})
* [**Rancher2** (`@pulumi/rancher2`)]({{< relref "nodejs/pulumi/rancher2" >}})
* [**SignalFX** (`@pulumi/signalfx`)]({{< relref "nodejs/pulumi/signalfx" >}})
* [**SpotInst** (`@pulumi/spotinst`)]({{< relref "nodejs/pulumi/spotinst" >}})
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
* [**Alibaba Cloud** (`pulumi_alicloud`)]({{< relref "python/pulumi_alicloud" >}})
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
* [**Keycloak** (`pulumi_keycloak`)]({{< relref "python/pulumi_keycloak" >}})
* [**Linode** (`pulumi_linode`)]({{< relref "python/pulumi_linode" >}})
* [**Mailgun** (`pulumi_mailgun`)]({{< relref "python/pulumi_mailgun" >}})
* [**MySQL** (`pulumi_mysql`)]({{< relref "python/pulumi_mysql" >}})
* [**New Relic** (`pulumi_newrelic`)]({{< relref "python/pulumi_newrelic" >}})
* [**Okta** (`pulumi_okta`)]({{< relref "python/pulumi_okta" >}})
* [**OpenStack** (`pulumi_openstack`)]({{< relref "python/pulumi_openstack" >}})
* [**Packet** (`pulumi_packet`)]({{< relref "python/pulumi_packet" >}})
* [**PostgreSQL** (`pulumi_postgresql`)]({{< relref "python/pulumi_postgresql" >}})
* [**RabbitMQ** (`pulumi_rabbitmq`)]({{< relref "python/pulumi_rabbitmq" >}})
* [**Rancher2** (`pulumi_rancher2`)]({{< relref "python/pulumi_rancher2" >}})
* [**SignalFX** (`pulumi_signalfx`)]({{< relref "python/pulumi_signalfx" >}})
* [**SpotInst** (`pulumi_spotinst`)]({{< relref "python/pulumi_spotinst" >}})
* [**Terraform** (`pulumi_terraform`)]({{< relref "python/pulumi_terraform" >}})
* [**TLS** (`pulumi_tls`)]({{< relref "python/pulumi_tls" >}})
* [**Hashicorp Vault** (`pulumi_vault`)]({{< relref "python/pulumi_vault" >}})
* [**vSphere** (`pulumi_vsphere`)]({{< relref "python/pulumi_vsphere" >}})
{{% /lang %}}

{{% lang go %}}
* [**AWS** (`aws`)](https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws)
* [**Azure** (`azure`)](https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure)
    * [**Azure Active Directory** (`pulumi_azuread`)](https://pkg.go.dev/github.com/pulumi/pulumi-azuread/sdk/go/azuread)
* [**Google Cloud** (`gcp`)](https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp)
* **Kubernetes** (`kubernetes`): Coming soon!
* [**Aiven** (`aiven`)](https://pkg.go.dev/github.com/pulumi/pulumi-aiven/sdk/go/aiven)
* [**Alibaba Cloud** (`alicloud`)](https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud)
* [**CloudAMQP** (`cloudamqp`)](https://pkg.go.dev/github.com/pulumi/pulumi-cloudamqp/sdk/go/cloudamqp)
* [**Cloudflare** (`cloudflare`)](https://pkg.go.dev/github.com/pulumi/pulumi-cloudflare/sdk/go/cloudflare)
* [**HashiCorp Consul** (`consul`)](https://pkg.go.dev/github.com/pulumi/pulumi-consul/sdk/go/consul)
* [**Datadog** (`datadog`)](https://pkg.go.dev/github.com/pulumi/pulumi-datadog/sdk/go/datadog)
* [**DigitalOcean** (`digitalocean`)](https://pkg.go.dev/github.com/pulumi/pulumi-digitalocean/sdk/go/digitalocean)
* [**DNSimple** (`dnsimple`)](https://pkg.go.dev/github.com/pulumi/pulumi-dnsimple/sdk/go/dnsimple)
* [**Fastly** (`fastly`)](https://pkg.go.dev/github.com/pulumi/pulumi-fastly/sdk/go/fastly)
* [**F5 BigIP** (`f5bigip`)](https://pkg.go.dev/github.com/pulumi/pulumi-f5bigip/sdk/go/f5bigip)
* [**GitLab** (`gitlab`)](https://pkg.go.dev/github.com/pulumi/pulumi-gitlab/sdk/go/gitlab)
* [**Kafka** (`kafka`)](https://pkg.go.dev/github.com/pulumi/pulumi-kafka/sdk/go/kafka)
* [**Keycloak** (`keycloak`)](https://pkg.go.dev/github.com/pulumi/pulumi-keycloak/sdk/go/keycloak)
* [**Linode** (`linode`)](https://pkg.go.dev/github.com/pulumi/pulumi-linode/sdk/go/linode)
* [**Mailgun** (`mailgun`)](https://pkg.go.dev/github.com/pulumi/pulumi-mailgun/sdk/go/mailgun)
* [**MySQL** (`mysql`)](https://pkg.go.dev/github.com/pulumi/pulumi-mysql/sdk/go/mysql)
* [**New Relic** (`newrelic`)](https://pkg.go.dev/github.com/pulumi/pulumi-newrelic/sdk/go/newrelic)
* [**Okta** (`okta`)](https://pkg.go.dev/github.com/pulumi/pulumi-okta/sdk/go/okta)
* [**OpenStack** (`openstack`)](https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack)
* [**Packet** (`packet`)](https://pkg.go.dev/github.com/pulumi/pulumi-packet/sdk/go/packet)
* [**PostgreSQL** (`postgresql`)](https://pkg.go.dev/github.com/pulumi/pulumi-postgresql/sdk/go/postgresql)
* **RabbitMQ** (`rabbitmq`): Coming soon!
* [**Rancher2** (`rancher2`)](https://pkg.go.dev/github.com/pulumi/pulumi-rancher2/sdk/go/rancher2)
* [**SignalFX** (`signalfx`)](https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx)
* [**SpotInst** (`spotinst`)](https://pkg.go.dev/github.com/pulumi/pulumi-spotinst/sdk/go/spotinst)
* **Terraform** (`terraform`): Coming soon!
* [**TLS** (`tls`)](https://pkg.go.dev/github.com/pulumi/pulumi-tls/sdk/go/tls)
* [**Hashicorp Vault** (`vault`)](https://pkg.go.dev/github.com/pulumi/pulumi-vault/sdk/go/vault)
* [**vSphere** (`vsphere`)](https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/go/vsphere)
{{% /lang %}}

{{% lang csharp %}}
* [**AWS** (`Pulumi.Aws`)](/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.html)
* [**Microsoft Azure** (`Pulumi.Azure`)](/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.html)
* [**Google Cloud** (`Pulumi.Gcp`)](/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.html)
* [**Kubernetes** (`Pulumi.Kubernetes`)](/docs/reference/pkg/dotnet/Pulumi.Kubernetes/Pulumi.Kubernetes.html)
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

{{% lang go %}}
Coming soon!
{{% /lang %}}

{{% lang csharp %}}
Coming soon!
{{% /lang %}}

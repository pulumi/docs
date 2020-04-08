---
title: API Reference
linktitle: API
menu:
  reference:
    name: API Reference
    weight: 2
---

Pulumi offers APIs for working with a wide variety of cloud platforms, as well as
higher-level APIs that make it easier to deliver cloud applications and infrastructure.

These APIs are available as packages in your chosen language's package manager --- npm for
TypeScript/JavaScript, PyPI for Python, and the like. There is a dedicated package for
each cloud that includes access to its full capabilities. In addition, Pulumi offers many
convenience packages that make common tasks easier, like setting up a network, creating a
Kubernetes cluster, and building and publishing containers to private registries.

## Resources by Cloud Provider

Reference documentation and examples for major cloud providers.

<div class="tiles">
    <a class="tile flex-1 p-8" href="{{< relref "/docs/reference/pkg/aws" >}}">
        <img class="h-10 mx-auto" src="/logos/tech/aws.svg" alt="AWS">
    </a>
    <a class="tile flex-1 p-8 md:mx-4 my-4 md:my-0" href="{{< relref "/docs/reference/pkg/azure" >}}">
        <img class="h-10 mx-auto" src="/logos/tech/azure.svg" alt="Azure">
    </a>
    <a class="tile flex-1 p-8" href="{{< relref "/docs/reference/pkg/gcp" >}}">
        <img class="h-10 mx-auto" src="/logos/tech/gcp.svg" alt="Google Cloud">
    </a>
</div>

<hr class="mt-12 mb-8 border-b border-gray-200">

## All Packages by Language

Detailed documentation for general-purpose and cloud-provider packages, organized by language.

{{% chooser language "javascript,typescript,python,go,csharp" / %}}

### General Purpose Packages

The Pulumi SDK package is used for accessing the core programming model around resources,
configuration, and other components directly. Additional general-purpose packages can be
used across all cloud platforms:

{{% choosable language "javascript,typescript" %}}
* [**Pulumi SDK** (`@pulumi/pulumi`)]({{< relref "nodejs/pulumi/pulumi" >}})
* [**Docker** (`@pulumi/docker`)]({{< relref "nodejs/pulumi/docker" >}})
* [**Policy** (`@pulumi/policy`) <span class="badge badge-preview">PREVIEW</span>]({{< relref "nodejs/pulumi/policy" >}})
* [**Random** (`@pulumi/random`)]({{< relref "nodejs/pulumi/random" >}})
{{% /choosable %}}

{{% choosable language python %}}
* [**Pulumi SDK** (`pulumi`)]({{< relref "python/pulumi" >}})
* [**Docker** (`pulumi_docker`)]({{< relref "python/pulumi_docker" >}})
* [**Random** (`pulumi_random`)]({{< relref "python/pulumi_random" >}})
{{% /choosable %}}

{{% choosable language go %}}
* [**Pulumi SDK** (`pulumi`)](https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi)
* [**Random** (`random`)](https://pkg.go.dev/github.com/pulumi/pulumi-random/sdk/go/random)
{{% /choosable %}}

{{% choosable language csharp %}}
* [**Pulumi SDK** (`Pulumi`)](/docs/reference/pkg/dotnet/Pulumi/Pulumi.html)
* [**Docker** (`Pulumi.Docker`)](/docs/reference/pkg/dotnet/Pulumi.Docker/Pulumi.Docker.html)
* [**Random** (`Pulumi.Random`)](/docs/reference/pkg/dotnet/Pulumi.Random/Pulumi.Random.html)
{{% /choosable %}}

### Cloud Provider Packages

Each cloud vendor has a dedicated package for deploying resources to it:

{{% choosable language "javascript,typescript" %}}
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
{{% /choosable %}}

{{% choosable language python %}}
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
{{% /choosable %}}

{{% choosable language go %}}
* [**AWS** (`aws`)](https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws)
* [**Azure** (`azure`)](https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v2/go/azure)
    * [**Azure Active Directory** (`pulumi_azuread`)](https://pkg.go.dev/github.com/pulumi/pulumi-azuread/sdk/go/azuread)
* [**Google Cloud** (`gcp`)](https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v2/go/gcp)
* [**Kubernetes** (`kubernetes`)](https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes)
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
{{% /choosable %}}

{{% choosable language csharp %}}
* [**AWS** (`Pulumi.Aws`)](/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.html)
* [**Microsoft Azure** (`Pulumi.Azure`)](/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.html)
* [**Google Cloud** (`Pulumi.Gcp`)](/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.html)
* [**Kubernetes** (`Pulumi.Kubernetes`)](/docs/reference/pkg/dotnet/Pulumi.Kubernetes/Pulumi.Kubernetes.html)

* [**Aiven** (`Pulumi.Aiven`)](/docs/reference/pkg/dotnet/Pulumi.Aiven/Pulumi.Aiven.html)
* [**Alibaba Cloud** (`Pulumi.AliCloud`)](/docs/reference/pkg/dotnet/Pulumi.AliCloud/Pulumi.AliCloud.html)
* [**CloudAMQP** (`Pulumi.CloudAmqp`)](/docs/reference/pkg/dotnet/Pulumi.CloudAmqp/Pulumi.CloudAmqp.html)
* [**Cloudflare** (`Pulumi.Cloudflare`)](/docs/reference/pkg/dotnet/Pulumi.Cloudflare/Pulumi.Cloudflare.html)
* [**HashiCorp Consul** (`Pulumi.Consul`)](/docs/reference/pkg/dotnet/Pulumi.Consul/Pulumi.Consul.html)
* [**Datadog** (`Pulumi.Datadog`)](/docs/reference/pkg/dotnet/Pulumi.Datadog/Pulumi.Datadog.html)
* [**DigitalOcean** (`Pulumi.DigitalOcean`)](/docs/reference/pkg/dotnet/Pulumi.DigitalOcean/Pulumi.DigitalOcean.html)
* [**DNSimple** (`Pulumi.DNSimple`)](/docs/reference/pkg/dotnet/Pulumi.DNSimple/Pulumi.DNSimple.html)
* [**Fastly** (`Pulumi.Fastly`)](/docs/reference/pkg/dotnet/Pulumi.Fastly/Pulumi.Fastly.html)
* [**F5 BigIP** (`Pulumi.F5BigIP`)](/docs/reference/pkg/dotnet/Pulumi.F5BigIP/Pulumi.F5BigIP.html)
* [**GitLab** (`Pulumi.GitLab`)](/docs/reference/pkg/dotnet/Pulumi.GitLab/Pulumi.GitLab.html)
* [**Kafka** (`Pulumi.Kafka`)](/docs/reference/pkg/dotnet/Pulumi.Kafka/Pulumi.Kafka.html)
* [**Keycloak** (`Pulumi.Keycloak`)](/docs/reference/pkg/dotnet/Pulumi.Keycloak/Pulumi.Keycloak.html)
* [**Linode** (`Pulumi.Linode`)](/docs/reference/pkg/dotnet/Pulumi.Linode/Pulumi.Linode.html)
* [**Mailgun** (`Pulumi.Mailgun`)](/docs/reference/pkg/dotnet/Pulumi.Mailgun/Pulumi.Mailgun.html)
* [**MySQL** (`Pulumi.MySql`)](/docs/reference/pkg/dotnet/Pulumi.MySql/Pulumi.MySql.html)
* [**New Relic** (`Pulumi.NewRelic`)](/docs/reference/pkg/dotnet/Pulumi.NewRelic/Pulumi.NewRelic.html)
* [**Okta** (`Pulumi.Okta`)](/docs/reference/pkg/dotnet/Pulumi.Okta/Pulumi.Okta.html)
* [**OpenStack** (`Pulumi.OpenStack`)](/docs/reference/pkg/dotnet/Pulumi.OpenStack/Pulumi.OpenStack.html)
* [**Packet** (`Pulumi.Packet`)](/docs/reference/pkg/dotnet/Pulumi.Packet/Pulumi.Packet.html)
* [**PostgreSQL** (`Pulumi.PostgreSql`)](/docs/reference/pkg/dotnet/Pulumi.PostgreSql/Pulumi.PostgreSql.html)
* [**RabbitMQ** (`Pulumi.RabbitMQ`)](/docs/reference/pkg/dotnet/Pulumi.RabbitMQ/Pulumi.RabbitMQ.html)
* [**Rancher2** (`Pulumi.Rancher2`)](/docs/reference/pkg/dotnet/Pulumi.Rancher2/Pulumi.Rancher2.html)
* [**SignalFX** (`Pulumi.SignalFX`)](/docs/reference/pkg/dotnet/Pulumi.SignalFX/Pulumi.SignalFX.html)
* [**SpotInst** (`Pulumi.SpotInst`)](/docs/reference/pkg/dotnet/Pulumi.SpotInst/Pulumi.SpotInst.html)
* [**Terraform** (`Pulumi.Terraform`)](/docs/reference/pkg/dotnet/Pulumi.Terraform/Pulumi.Terraform.html)
* [**TLS** (`Pulumi.Tls`)](/docs/reference/pkg/dotnet/Pulumi.Tls/Pulumi.Tls.html)
* [**Hashicorp Vault** (`Pulumi.Vault`)](/docs/reference/pkg/dotnet/Pulumi.Vault/Pulumi.Vault.html)
* [**vSphere** (`Pulumi.VSphere`)](/docs/reference/pkg/dotnet/Pulumi.VSphere/Pulumi.VSphere.html)
{{% /choosable %}}

### Cloud-Agnostic Packages

{{% choosable language "javascript,typescript" %}}
Pulumi offers a highly productive, cloud-agnostic package for container and serverless
programming in the `@pulumi/cloud` package which currently allows writing applications
once and deploying to either AWS or Azure.

* [**Pulumi Cloud Framework** (`@pulumi/cloud`) <span class="badge badge-preview">PREVIEW</span>]({{< relref "nodejs/pulumi/cloud" >}})
{{% /choosable %}}

{{% choosable language "python,go,csharp" %}}
Coming soon!
{{% /choosable %}}

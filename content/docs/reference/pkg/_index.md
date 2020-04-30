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
    <a class="tile flex-1 p-8" href="{{< prelref "/docs/reference/pkg/aws" >}}">
        <img class="h-10 mx-auto" src="/logos/tech/aws.svg" alt="AWS">
    </a>
    <a class="tile flex-1 p-8 md:mx-4 my-4 md:my-0" href="{{< prelref "/docs/reference/pkg/azure" >}}">
        <img class="h-10 mx-auto" src="/logos/tech/azure.svg" alt="Azure">
    </a>
    <a class="tile flex-1 p-8" href="{{< prelref "/docs/reference/pkg/gcp" >}}">
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
* [**Pulumi SDK** (`@pulumi/pulumi`)]({{< prelref "nodejs/pulumi/pulumi" >}})
* [**Docker** (`@pulumi/docker`)]({{< prelref "nodejs/pulumi/docker" >}})
* [**Policy** (`@pulumi/policy`)]({{< prelref "nodejs/pulumi/policy" >}})
* [**Random** (`@pulumi/random`)]({{< prelref "nodejs/pulumi/random" >}})
{{% /choosable %}}

{{% choosable language python %}}
* [**Pulumi SDK** (`pulumi`)]({{< prelref "python/pulumi" >}})
* [**Docker** (`pulumi_docker`)]({{< prelref "python/pulumi_docker" >}})
* [**Policy** (`pulumi_policy`) <span class="badge badge-preview">PREVIEW</span>]({{< prelref "python/pulumi_policy" >}})
* [**Random** (`pulumi_random`)]({{< prelref "python/pulumi_random" >}})
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
* [**AWS** (`@pulumi/aws`)]({{< prelref "nodejs/pulumi/aws" >}})
    * [**AWS Extensions** (`@pulumi/awsx`)]({{< prelref "nodejs/pulumi/awsx" >}}) - simpler interfaces for common AWS patterns
    * [**AWS EKS Cluster** (`@pulumi/eks`)]({{< prelref "nodejs/pulumi/eks" >}}) - simpler interface for working with AWS EKS
* [**Azure** (`@pulumi/azure`)]({{< prelref "nodejs/pulumi/azure" >}})
    * [**Azure Active Directory** (`@pulumi/azuread`)]({{< prelref "nodejs/pulumi/azuread" >}})
* [**Google Cloud** (`@pulumi/gcp`)]({{< prelref "nodejs/pulumi/gcp" >}})
* [**Kubernetes** (`@pulumi/kubernetes`)]({{< prelref "nodejs/pulumi/kubernetes" >}})
    * [**Kubernetes Extensions** (`@pulumi/kubernetesx`) <span class="badge badge-preview">PREVIEW</span>]({{< prelref "nodejs/pulumi/kubernetesx" >}}) - simpler interface for working with Kubernetes

* [**Aiven** (`@pulumi/aiven`)]({{< prelref "nodejs/pulumi/aiven" >}})
* [**Alibaba Cloud** (`@pulumi/alicloud`)]({{< prelref "nodejs/pulumi/alicloud" >}})
* [**CloudAMQP** (`@pulumi/cloudamqp`)]({{< prelref "nodejs/pulumi/cloudamqp" >}})
* [**Cloudflare** (`@pulumi/cloudflare`)]({{< prelref "nodejs/pulumi/cloudflare" >}})
* [**HashiCorp Consul** (`@pulumi/consul`)]({{< prelref "nodejs/pulumi/consul" >}})
* [**Datadog** (`@pulumi/datadog`)]({{< prelref "nodejs/pulumi/datadog" >}})
* [**DigitalOcean** (`@pulumi/digitalocean`)]({{< prelref "nodejs/pulumi/digitalocean" >}})
* [**DNSimple** (`@pulumi/dnsimple`)]({{< prelref "nodejs/pulumi/dnsimple" >}})
* [**Fastly** (`@pulumi/fastly`)]({{< prelref "nodejs/pulumi/fastly" >}})
* [**F5 BigIP** (`@pulumi/f5bigip`)]({{< prelref "nodejs/pulumi/f5bigip" >}})
* [**GitHub** (`@pulumi/github`)]({{< prelref "nodejs/pulumi/github" >}})
* [**GitLab** (`@pulumi/gitlab`)]({{< prelref "nodejs/pulumi/gitlab" >}})
* [**Kafka** (`@pulumi/kafka`)]({{< prelref "nodejs/pulumi/kafka" >}})
* [**Keycloak** (`@pulumi/keycloak`)]({{< prelref "nodejs/pulumi/keycloak" >}})
* [**Linode** (`@pulumi/linode`)]({{< prelref "nodejs/pulumi/linode" >}})
* [**Mailgun** (`@pulumi/mailgun`)]({{< prelref "nodejs/pulumi/mailgun" >}})
* [**MongoDB Atlas** (`@pulumi/mongodbatlas`)]({{< prelref "nodejs/pulumi/mongodbatlas" >}})
* [**MySQL** (`@pulumi/mysql`)]({{< prelref "nodejs/pulumi/mysql" >}})
* [**New Relic** (`@pulumi/newrelic`)]({{< prelref "nodejs/pulumi/newrelic" >}})
* [**Okta** (`@pulumi/okta`)]({{< prelref "nodejs/pulumi/okta" >}})
* [**OpenStack** (`@pulumi/openstack`)]({{< prelref "nodejs/pulumi/openstack" >}})
* [**Packet** (`@pulumi/packet`)]({{< prelref "nodejs/pulumi/packet" >}})
* [**PostgreSQL** (`@pulumi/postgresql`)]({{< prelref "nodejs/pulumi/postgresql" >}})
* [**RabbitMQ** (`@pulumi/rabbitmq`)]({{< prelref "nodejs/pulumi/rabbitmq" >}})
* [**Rancher2** (`@pulumi/rancher2`)]({{< prelref "nodejs/pulumi/rancher2" >}})
* [**SignalFX** (`@pulumi/signalfx`)]({{< prelref "nodejs/pulumi/signalfx" >}})
* [**SpotInst** (`@pulumi/spotinst`)]({{< prelref "nodejs/pulumi/spotinst" >}})
* [**Terraform** (`@pulumi/terraform`)]({{< prelref "nodejs/pulumi/terraform" >}})
* [**TLS** (`@pulumi/tls`)]({{< prelref "nodejs/pulumi/tls" >}})
* [**Hashicorp Vault** (`@pulumi/vault`)]({{< prelref "nodejs/pulumi/vault" >}})
* [**vSphere** (`@pulumi/vsphere`)]({{< prelref "nodejs/pulumi/vsphere" >}})
{{% /choosable %}}

{{% choosable language python %}}
* [**AWS** (`pulumi_aws`)]({{< prelref "python/pulumi_aws" >}})
* [**Azure** (`pulumi_azure`)]({{< prelref "python/pulumi_azure" >}})
    * [**Azure Active Directory** (`pulumi_azuread`)]({{< prelref "python/pulumi_azuread" >}})
* [**Google Cloud** (`pulumi_gcp`)]({{< prelref "python/pulumi_gcp" >}})
* [**Kubernetes** (`pulumi_kubernetes`)]({{< prelref "python/pulumi_kubernetes" >}})

* [**Aiven** (`pulumi_aiven`)]({{< prelref "python/pulumi_aiven" >}})
* [**Alibaba Cloud** (`pulumi_alicloud`)]({{< prelref "python/pulumi_alicloud" >}})
* [**CloudAMQP** (`pulumi_cloudamqp`)]({{< prelref "python/pulumi_cloudamqp" >}})
* [**Cloudflare** (`pulumi_cloudflare`)]({{< prelref "python/pulumi_cloudflare" >}})
* [**HashiCorp Consul** (`pulumi_consul`)]({{< prelref "python/pulumi_consul" >}})
* [**Datadog** (`pulumi_datadog`)]({{< prelref "python/pulumi_datadog" >}})
* [**DigitalOcean** (`pulumi_digitalocean`)]({{< prelref "python/pulumi_digitalocean" >}})
* [**DNSimple** (`pulumi_dnsimple`)]({{< prelref "python/pulumi_dnsimple" >}})
* [**Fastly** (`pulumi_fastly`)]({{< prelref "python/pulumi_fastly" >}})
* [**F5 BigIP** (`pulumi_f5bigip`)]({{< prelref "python/pulumi_f5bigip" >}})
* [**GitHub** (`pulumi_github`)]({{< prelref "python/pulumi_github" >}})
* [**GitLab** (`pulumi_gitlab`)]({{< prelref "python/pulumi_gitlab" >}})
* [**Kafka** (`pulumi_kafka`)]({{< prelref "python/pulumi_kafka" >}})
* [**Keycloak** (`pulumi_keycloak`)]({{< prelref "python/pulumi_keycloak" >}})
* [**Linode** (`pulumi_linode`)]({{< prelref "python/pulumi_linode" >}})
* [**Mailgun** (`pulumi_mailgun`)]({{< prelref "python/pulumi_mailgun" >}})
* [**MongoDB Atlas** (`pulumi_mongodbatlas`)]({{< prelref "python/pulumi_mongodbatlas" >}})
* [**MySQL** (`pulumi_mysql`)]({{< prelref "python/pulumi_mysql" >}})
* [**New Relic** (`pulumi_newrelic`)]({{< prelref "python/pulumi_newrelic" >}})
* [**Okta** (`pulumi_okta`)]({{< prelref "python/pulumi_okta" >}})
* [**OpenStack** (`pulumi_openstack`)]({{< prelref "python/pulumi_openstack" >}})
* [**Packet** (`pulumi_packet`)]({{< prelref "python/pulumi_packet" >}})
* [**PostgreSQL** (`pulumi_postgresql`)]({{< prelref "python/pulumi_postgresql" >}})
* [**RabbitMQ** (`pulumi_rabbitmq`)]({{< prelref "python/pulumi_rabbitmq" >}})
* [**Rancher2** (`pulumi_rancher2`)]({{< prelref "python/pulumi_rancher2" >}})
* [**SignalFX** (`pulumi_signalfx`)]({{< prelref "python/pulumi_signalfx" >}})
* [**SpotInst** (`pulumi_spotinst`)]({{< prelref "python/pulumi_spotinst" >}})
* [**Terraform** (`pulumi_terraform`)]({{< prelref "python/pulumi_terraform" >}})
* [**TLS** (`pulumi_tls`)]({{< prelref "python/pulumi_tls" >}})
* [**Hashicorp Vault** (`pulumi_vault`)]({{< prelref "python/pulumi_vault" >}})
* [**vSphere** (`pulumi_vsphere`)]({{< prelref "python/pulumi_vsphere" >}})
{{% /choosable %}}

{{% choosable language go %}}
* [**AWS** (`aws`)](https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/v2/go/aws)
* [**Azure** (`azure`)](https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure)
    * [**Azure Active Directory** (`pulumi_azuread`)](https://pkg.go.dev/github.com/pulumi/pulumi-azuread/sdk/v2/go/azuread)
* [**Google Cloud** (`gcp`)](https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp)
* [**Kubernetes** (`kubernetes`)](https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/v2/go/kubernetes)
* [**Aiven** (`aiven`)](https://pkg.go.dev/github.com/pulumi/pulumi-aiven/sdk/v2/go/aiven)
* [**Alibaba Cloud** (`alicloud`)](https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/v2/go/alicloud)
* [**CloudAMQP** (`cloudamqp`)](https://pkg.go.dev/github.com/pulumi/pulumi-cloudamqp/sdk/v2/go/cloudamqp)
* [**Cloudflare** (`cloudflare`)](https://pkg.go.dev/github.com/pulumi/pulumi-cloudflare/sdk/v2/go/cloudflare)
* [**HashiCorp Consul** (`consul`)](https://pkg.go.dev/github.com/pulumi/pulumi-consul/sdk/v2/go/consul)
* [**Datadog** (`datadog`)](https://pkg.go.dev/github.com/pulumi/pulumi-datadog/sdk/v2/go/datadog)
* [**DigitalOcean** (`digitalocean`)](https://pkg.go.dev/github.com/pulumi/pulumi-digitalocean/sdk/v2/go/digitalocean)
* [**DNSimple** (`dnsimple`)](https://pkg.go.dev/github.com/pulumi/pulumi-dnsimple/sdk/v2/go/dnsimple)
* [**Fastly** (`fastly`)](https://pkg.go.dev/github.com/pulumi/pulumi-fastly/sdk/v2/go/fastly)
* [**F5 BigIP** (`f5bigip`)](https://pkg.go.dev/github.com/pulumi/pulumi-f5bigip/sdk/v2/go/f5bigip)
* [**GitHub** (`github`)](https://pkg.go.dev/github.com/pulumi/pulumi-github/sdk/go/github)
* [**GitLab** (`gitlab`)](https://pkg.go.dev/github.com/pulumi/pulumi-gitlab/sdk/v2/go/gitlab)
* [**Kafka** (`kafka`)](https://pkg.go.dev/github.com/pulumi/pulumi-kafka/sdk/v2/go/kafka)
* [**Keycloak** (`keycloak`)](https://pkg.go.dev/github.com/pulumi/pulumi-keycloak/sdk/v2/go/keycloak)
* [**Linode** (`linode`)](https://pkg.go.dev/github.com/pulumi/pulumi-linode/sdk/v2/go/linode)
* [**Mailgun** (`mailgun`)](https://pkg.go.dev/github.com/pulumi/pulumi-mailgun/sdk/v2/go/mailgun)
* [**MongoDB Atlas** (`mongodbatlas`)](https://pkg.go.dev/github.com/pulumi/pulumi-mongodbatlas/sdk/go/mongodbatlas)
* [**MySQL** (`mysql`)](https://pkg.go.dev/github.com/pulumi/pulumi-mysql/sdk/v2/go/mysql)
* [**New Relic** (`newrelic`)](https://pkg.go.dev/github.com/pulumi/pulumi-newrelic/sdk/v2/go/newrelic)
* [**Okta** (`okta`)](https://pkg.go.dev/github.com/pulumi/pulumi-okta/sdk/v2/go/okta)
* [**OpenStack** (`openstack`)](https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/v2/go/openstack)
* [**Packet** (`packet`)](https://pkg.go.dev/github.com/pulumi/pulumi-packet/sdk/v2/go/packet)
* [**PostgreSQL** (`postgresql`)](https://pkg.go.dev/github.com/pulumi/pulumi-postgresql/sdk/v2/go/postgresql)
* [**RabbitMQ** (`rabbitmq`)](https://pkg.go.dev/github.com/pulumi/pulumi-rabbitmq/sdk/v2/go/rabbitmq)
* [**Rancher2** (`rancher2`)](https://pkg.go.dev/github.com/pulumi/pulumi-rancher2/sdk/v2/go/rancher2)
* [**SignalFX** (`signalfx`)](https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/v2/go/signalfx)
* [**SpotInst** (`spotinst`)](https://pkg.go.dev/github.com/pulumi/pulumi-spotinst/sdk/v2/go/spotinst)
* **Terraform** (`terraform`): Coming soon!
* [**TLS** (`tls`)](https://pkg.go.dev/github.com/pulumi/pulumi-tls/sdk/v2/go/tls)
* [**Hashicorp Vault** (`vault`)](https://pkg.go.dev/github.com/pulumi/pulumi-vault/sdk/v2/go/vault)
* [**vSphere** (`vsphere`)](https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/v2/go/vsphere)
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
* [**Terraform** (`Pulumi.Terraform`)](/docs/reference/pkg/dotnet/Pulumi.Terraform/Pulumi.Terraform.State.html)
* [**TLS** (`Pulumi.Tls`)](/docs/reference/pkg/dotnet/Pulumi.Tls/Pulumi.Tls.html)
* [**Hashicorp Vault** (`Pulumi.Vault`)](/docs/reference/pkg/dotnet/Pulumi.Vault/Pulumi.Vault.html)
* [**vSphere** (`Pulumi.VSphere`)](/docs/reference/pkg/dotnet/Pulumi.VSphere/Pulumi.VSphere.html)
{{% /choosable %}}

### Cloud-Agnostic Packages

{{% choosable language "javascript,typescript" %}}
Pulumi offers a highly productive, cloud-agnostic package for container and serverless
programming in the `@pulumi/cloud` package which currently allows writing applications
once and deploying to either AWS or Azure.

* [**Pulumi Cloud Framework** (`@pulumi/cloud`) <span class="badge badge-preview">PREVIEW</span>]({{< prelref "nodejs/pulumi/cloud" >}})
{{% /choosable %}}

{{% choosable language "python,go,csharp" %}}
Coming soon!
{{% /choosable %}}

---
title: API Reference
linktitle: API
meta_desc: Documentation and examples for working with cloud providers and other services.
menu:
  reference:
    name: API Reference
    weight: 2
---

Pulumi offers APIs for working with a wide variety of cloud platforms, as well as
higher-level APIs that make it easier to deliver cloud applications and infrastructure.

## Resource Documentation

[Resource]({{< relref "/docs/intro/concepts/programming-model#resource-providers" >}})-level
documentation and examples for cloud providers and other services. Whether you're looking
for details about how to work with a particular resource or just browsing around to
explore what's possible, you've come to the right place.

### Core Providers

{{< resource-providers "aws,azure-native,gcp,kubernetes" >}}

### Cloud Providers

{{< resource-providers "digitalocean,linode,vsphere,fastly,equinix-metal,openstack,alicloud,cloudamqp,hcloud,civo,yandex" >}}

### Infrastructure

{{< resource-providers "aiven,auth0,azuread,azuredevops,consul,docker,kafka,keycloak,kong,mailgun,okta,pagerduty,rabbitmq,rancher2,spotinst,splunk,vault,venafi,opsgenie,rke,confluent" >}}

### Database

{{< resource-providers "mysql,postgresql,mongodbatlas" >}}

### Monitoring

{{< resource-providers "datadog,newrelic,signalfx,wavefront,sumologic" >}}

### Network

{{< resource-providers "cloudflare,dnsimple,f5bigip,ns1,akamai" >}}

### Version Control

{{< resource-providers "github,gitlab" >}}

### Utilities

{{< resource-providers "random,tls,cloudinit,libvirt" false >}}

### Classic Providers

{{< resource-providers "azure" >}}

### Preview Providers

{{< resource-providers "google-native" >}}


## Package Documentation

SDK reference documentation, organized by language.

{{% chooser language "javascript,typescript,python,go,csharp" / %}}

### Standard Packages

{{% choosable language "javascript,typescript" %}}
<dl class="tabular">
    <dt>Pulumi SDK</dt>
    <dd><a href="{{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi" >}}">@pulumi/pulumi</a></dd>
    <dt>Pulumi Policy</dt>
    <dd><a href="{{< relref "/docs/reference/pkg/nodejs/pulumi/policy" >}}">@pulumi/policy</a></dd>
    <dt>Pulumi Terraform</dt>
    <dd><a href="{{< relref "/docs/reference/pkg/nodejs/pulumi/terraform" >}}">@pulumi/terraform</a></dd>
</dl>
{{% /choosable %}}

{{% choosable language python %}}
<dl class="tabular">
    <dt>Pulumi SDK</dt>
    <dd><a href="{{< relref "/docs/reference/pkg/python/pulumi" >}}">pulumi</a></dd>
    <dt>Pulumi Policy</dt>
    <dd><a href="{{< relref "/docs/reference/pkg/python/pulumi_policy" >}}">pulumi_policy</a></dd>
    <dt>Pulumi Terraform</dt>
    <dd><a href="{{< relref "/docs/reference/pkg/python/pulumi_terraform" >}}">pulumi_terraform</a></dd>
</dl>
{{% /choosable %}}

{{% choosable language go %}}
<dl class="tabular">
    <dt>Pulumi SDK</dt>
    <dd><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi">pulumi</a></dd>
</dl>
{{% /choosable %}}

{{% choosable language csharp %}}
<dl class="tabular">
    <dt>Pulumi SDK</dt>
    <dd><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.html">Pulumi</a></dd>
    <dt>Pulumi FSharp SDK</dt>
    <dd><a href="/docs/reference/pkg/dotnet/Pulumi.FSharp/Pulumi.FSharp.html">Pulumi.FSharp</a></dd>
    <dt>Pulumi Automation API</dt>
    <dd><a href="/docs/reference/pkg/dotnet/Pulumi.Automation/Pulumi.Automation.html">Pulumi.Automation</a></dd>
</dl>
{{% /choosable %}}

### Extension Packages

{{% choosable language "javascript,typescript" %}}
<dl class="tabular">
    <dt>AWS Extensions</dt>
    <dd>
        <a href="{{< relref "/docs/reference/pkg/nodejs/pulumi/awsx" >}}">@pulumi/awsx</a>
        <p>Simpler interfaces encapsulating common AWS patterns.</p>
    </dd>
    <dt>AWS EKS Cluster</dt>
    <dd>
        <a href="{{< relref "/docs/reference/pkg/eks" >}}">@pulumi/eks</a>
        <p>Simpler interfaces for working with AWS EKS.</p>
    </dd>
    <dt>Kubernetes Extensions</dt>
    <dd>
        <a href="{{< relref "/docs/reference/pkg/nodejs/pulumi/kubernetesx" >}}">@pulumi/kubernetesx</a>
        <span class="ml-2 badge badge-preview">Preview</span>
        <p>Simpler interfaces for working with Kubernetes.</p>
    </dd>
</dl>
{{% /choosable %}}

{{% choosable language python %}}
<dl class="tabular">
    <dt>AWS EKS Cluster</dt>
    <dd>
        <a href="{{< relref "/docs/reference/pkg/eks" >}}">pulumi_eks</a>
        <p>Simpler interfaces for working with AWS EKS.</p>
    </dd>
</dl>
{{% /choosable %}}

{{% choosable language go %}}
<dl class="tabular">
    <dt>AWS EKS Cluster</dt>
    <dd>
        <a href="{{< relref "/docs/reference/pkg/eks" >}}">eks</a>
        <p>Simpler interfaces for working with AWS EKS.</p>
    </dd>
</dl>
{{% /choosable %}}

{{% choosable language csharp %}}
<dl class="tabular">
    <dt>AWS EKS Cluster</dt>
    <dd>
        <a href="{{< relref "/docs/reference/pkg/eks" >}}">Pulumi.Eks</a>
        <p>Simpler interfaces for working with AWS EKS.</p>
    </dd>
</dl>
{{% /choosable %}}

{{% choosable language "javascript,typescript" %}}

### Cloud-Agnostic Packages

<dl class="tabular">
    <dt>Pulumi Cloud Framework</dt>
    <dd>
        <a href="{{< relref "/docs/reference/pkg/nodejs/pulumi/cloud" >}}">@pulumi/cloud</a>
        <span class="ml-2 badge badge-preview">PREVIEW</span>
        <p>A highly productive, cloud-agnostic package for container and serverless programming.</p>
    </dd>
</dl>

{{% /choosable %}}

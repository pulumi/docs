---
title: Pulumi vs. Terraform
meta_desc: This page gives an overview about the major differences between Terraform and Pulumi.
linktitle: Terraform
menu:
  intro:
    parent: vs
    weight: 1

aliases: ["/docs/reference/vs/terraform/"]
---

Pulumi is like Terraform, in that you create, deploy, and manage infrastructure as code on any cloud. Unlike
Terraform, however, you will use familiar general purpose languages and tools to do so. Like Terraform, Pulumi is
[open source on GitHub](https://github.com/pulumi/pulumi) and is [free to use]({{< relref "/docs/get-started" >}}).

## Summary

In Terraform, you write programs in a custom domain-specific-language (DSL) called HashiCorp Configuration Language
(HCL), and the Terraform engine takes care of provisioning and updating resources. With Pulumi, you use general
purpose languages to express desired state, and Pulumi's engine similarly gives you diffs and a way to robustly update
your infrastructure. Both Terraform and Pulumi support many cloud providers, including AWS, Azure, and Google Cloud,
plus other services like CloudFlare, Digital Ocean, and more. Thanks to integration with Terraform providers, Pulumi
is able to support a superset of the providers that Terraform currently offers.

## Major Differences

The major differences between Terraform and Pulumi are as follows:

1. Terraform requires that you and your team learn a new custom language, the HCL DSL. In contrast, Pulumi lets you use
   languages you already know and love, like JavaScript, TypeScript, Python, and Go.

2. Because of the use of real languages, you get familiar constructs like for loops, functions, and classes. This
   significantly improves the ability to cut down on boilerplate and enforce best practices. Instead of creating
   a new ecosystem of modules and sharing, Pulumi lets you leverage existing package management tools and techniques.

3. Terraform, by default, requires that you manage concurrency and state manually, by way of its "state files." Pulumi,
   in contrast, uses the free app.pulumi.com service to eliminate these concerns. This makes getting started with
   Pulumi, and operationalizing it in a team setting, much easier. For advanced use cases, [it is possible to use
   Pulumi without the service]({{< relref "/docs/troubleshooting/faq#can-i-use-pulumi-without-depending-on-pulumicom" >}}),
   which works a lot more like Terraform, but it is harder to do and opt-in. Pulumi errs on the side of ease-of-use.

4. Pulumi has deep support for cloud native technologies, like Kubernetes, and supports advanced deployment
   scenarios that cannot be expressed with Terraform. This includes Prometheus-based canaries, automatic Envoy
   sidecar injection, and more. Pulumi is a proud member of the Cloud Native Computing Foundation (CNCF).

For some concrete examples of these differences, please see our article, [From Terraform to Infrastructure as Software](
{{< relref "from-terraform-to-infrastructure-as-software" >}}).

## Using Terraform Providers

Pulumi is able to adapt [any Terraform Provider](https://github.com/terraform-providers) for use with Pulumi, enabling
management of any infrastructure supported by the Terraform Providers ecosystem using Pulumi programs.

Indeed, some of Pulumi's most interesting providers have been created this way, delivering access to robust,
tried-and-true infrastructure management.  The Terraform Providers ecosystem is mature and healthy, and enjoys
contributions from many cloud and infrastructure leaders across the industry, ourselves included.

Most Pulumi users don't need to know about this detail, however we are proud to be building on the work of others,
and contributing our own open source back to this vibrant ecosystem, and thought you should know.

In the event you'd like to add new providers, or understand how this integration works, please check out the
[Pulumi Terraform bridge repo](https://github.com/pulumi/pulumi-terraform).  This bridge is fully open source and
makes it easy to create new Pulumi providers out of existing Terraform Providers.

## Converting From Terraform

Pulumi offers a tool, [`tf2pulumi`](https://github.com/pulumi/tf2pulumi), that converts Terraform HCL to Pulumi. It is
open source on GitHub, and works for most projects we have come across; if you run into a snag, Issues and Pull
Requests are welcome! [Download and use it now.](https://github.com/pulumi/tf2pulumi)

## Using Pulumi and Terraform Side-by-Side

Pulumi supports
[consuming local or remote Terraform state](
{{< relref "using-terraform-remote-state-with-pulumi" >}})
from your Pulumi programs. This helps with
incremental adoption, whereby you continue managing a subset of your infrastructure with Terraform, while you
incrementally move to Pulumi.

For instance, say you would like to keep your VPC and low level network definitions written in Terraform so as to
avoid any disruption, or maybe because some of the team would like to stay on Terraform for now. Using the
state reference support described above, you can author higher level infrastructure in Pulumi that consumes the
Terraform-provisioned VPC information (like the VPC ID, Subnet IDs, etc), making co-existence easy to automate.

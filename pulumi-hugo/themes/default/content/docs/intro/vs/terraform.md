---
title: Pulumi vs. Terraform
meta_desc: Pulumi is like Terraform—create, deploy, and manage infrastructure as code on any cloud. But unlike Terraform you can use familiar languages and tools.
linktitle: Terraform
menu:
  intro:
    parent: vs
    weight: 1

aliases: ["/docs/reference/vs/terraform/"]
---

Terraform and Pulumi hold a lot of similarities, but they differ in a few key ways. This page helps provide a rundown of the differences. First, Pulumi is like Terraform, in that you create, deploy, and manage [infrastructure as code]({{< relref "/what-is/what-is-infrastructure-as-code" >}}) on any cloud. But where
Terraform requires the use of a custom programming language, Pulumi allows you to use familiar general purpose languages and tools to accomplish the same goals. Like Terraform, Pulumi is
[open source on GitHub](https://github.com/pulumi/pulumi) and is [free to use]({{< relref "/docs/get-started" >}}).

Both Terraform and Pulumi support many cloud providers, including AWS, Azure, and Google Cloud,
plus other services like CloudFlare, Digital Ocean, and more. Thanks to integration with Terraform providers, Pulumi
is able to support a superset of the providers that Terraform currently offers.

Here is a summary of the key differences between Pulumi and Terraform:

| **Component** | **Pulumi** | **Terraform** |
| :--- | :--- | :--- |
| [Language Support]({{< relref "#languagesupport" >}}) | Python, TypeScript, JavaScript, Go, C#, F# | Hashicorp Configuration Language (HCL) |
| [State Management]({{< relref "#statemanagement" >}}) | Managed through Pulumi Service by default, self-managed options available | Self-managed by default, managed SaaS offering available |
| [Provider Support]({{< relref "#providersupport" >}}) | Native cloud providers with 100% same-day resource coverage plus Terraform-based providers for additional coverage | Support across multiple IaaS, SaaS, and PaaS providers |
| [OSS License]({{< relref "#license" >}}) | Apache License 2.0 | Mozilla Public License 2.0 |

If you have Terraform HCL that you would like to convert to Pulumi, see [Converting Terraform HCL to Pulumi]({{< relref "/docs/guides/adopting/from_terraform#converting-terraform-hcl-to-pulumi" >}}) in our Adopting Pulumi user guide.

The following sections go into further detail on the differences between Pulumi and Terraform.

## Language Support {#languagesupport}

Terraform requires that you and your team write programs in a custom domain-specific-language (DSL) called HashiCorp Configuration Language
(HCL). In contrast, Pulumi lets you use programming languages like Python, Go, JavaScript, TypeScript, and C#. Because of the use of familiar languages, you get familiar constructs like for loops, functions, and classes. This significantly improves the ability to cut down on boilerplate and enforce best practices. Instead of creating
a new ecosystem of modules and sharing, Pulumi lets you leverage existing package management tools and techniques.

For more information on the languages that Pulumi supports, see [Languages]({{< relref "/docs/intro/languages" >}}).

## State Management {#statemanagement}

The Terraform engine takes care of provisioning and updating resources. With Pulumi, you use general
purpose languages to express desired state, and Pulumi's engine similarly gives you diffs and a way to robustly update
your infrastructure.

By default, Terraform requires that you manage concurrency and state manually, by way of its "state files." Pulumi,
in contrast, uses the free [Pulumi Service](https://app.pulumi.com) to eliminate these concerns. This makes getting started with
Pulumi, and operationalizing it in a team setting, much easier. For advanced use cases, it is possible to use
[Pulumi without the service]({{< relref "/docs/troubleshooting/faq#can-i-use-pulumi-without-depending-on-pulumicom" >}}),
which works a lot more like Terraform, but it requires you to manage state and concurrency issues. Pulumi errs on the side of ease-of-use.

For more information on how Pulumi manages state or how to use different backends, see [State and Backends]({{< relref "/docs/intro/concepts/state" >}}).

## Provider Support {#providersupport}

Pulumi has deep support for cloud native technologies, like Kubernetes, and supports advanced deployment
scenarios that cannot be expressed with Terraform. This includes Prometheus-based canaries, automatic Envoy
sidecar injection, and more. Pulumi is a proud member of the Cloud Native Computing Foundation (CNCF).

### Using Terraform Providers

Pulumi is able to adapt [any Terraform Provider](https://github.com/terraform-providers) for use with Pulumi, enabling
management of any infrastructure supported by the Terraform Providers ecosystem using Pulumi programs.

Indeed, some of Pulumi's most interesting providers have been created this way, delivering access to robust,
tried-and-true infrastructure management.  The Terraform Providers ecosystem is mature and healthy, and enjoys
contributions from many cloud and infrastructure leaders across the industry, ourselves included.

Most Pulumi users don't need to know about this detail, however we are proud to be building on the work of others,
and contributing our own open source back to this vibrant ecosystem, and thought you should know.

In the event you'd like to add new providers, or understand how this integration works, check out the
[Pulumi Terraform bridge repo](https://github.com/pulumi/pulumi-terraform-bridge).  This bridge is fully open source and
makes it easy to create new Pulumi providers out of existing Terraform Providers.

### Converting From Terraform

Pulumi offers a tool, [tf2pulumi](https://github.com/pulumi/tf2pulumi), that converts Terraform HashiCorp Configuration Language to Pulumi. It is
open source on GitHub, and works for most projects we have come across; if you run into a snag, Issues and Pull
Requests are welcome!

To learn more, see [Converting Terraform HCL to Pulumi]({{< relref "/docs/guides/adopting/from_terraform#converting-terraform-hcl-to-pulumi" >}}) in our Adopting Pulumi user guide.

For an example on how to do this conversion, see our article, [From Terraform to Infrastructure as Software](
{{< relref "from-terraform-to-infrastructure-as-software" >}}).

### Using Pulumi and Terraform Side-by-Side

Pulumi supports [consuming local or remote Terraform state]({{< relref "using-terraform-remote-state-with-pulumi" >}}) from your Pulumi programs. This helps with
incremental adoption, whereby you continue managing a subset of your infrastructure with Terraform, while you incrementally move to Pulumi.

For example, maybe you would like to keep your VPC and low-level network definitions written in Terraform so as to
avoid any disruption, or maybe because some of the team would like to stay on Terraform for now and make a shift in the future. Using the
state reference support described previously, you can author higher-level infrastructure in Pulumi that consumes the
Terraform-provisioned VPC information (such as the VPC ID, Subnet IDs, etc.), making the co-existence of Pulumi and Terraform easy to automate.

To learn more, see [Referencing Terraform State]({{< relref "/docs/guides/adopting/from_terraform#referencing-terraform-state" >}}) in our Adopting Pulumi user guide.

## OSS License {#license}

Terraform uses the weak copyleft [Mozilla Public License 2.0](https://github.com/hashicorp/terraform/blob/main/LICENSE). Conversely, Pulumi open-source projects use the permissive and business-friendly [Apache License 2.0](https://github.com/pulumi/pulumi/blob/master/LICENSE). This includes the core [Pulumi repo](https://github.com/pulumi/pulumi), all of the open-source Pulumi resource providers (such as the [Azure Native provider](https://github.com/pulumi/pulumi-azure-native)), conversion utilities like [tf2pulumi](https://github.com/pulumi/tf2pulumi), and other useful projects.

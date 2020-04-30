---
title: "Adopting Pulumi"
meta_desc: Migrate from an existing infrastructure management solution to Pulumi.
menu:
  userguides:
    identifier: adopting
    weight: 2
---

If you've fallen in love with Pulumi, it might not be obvious how to adopt it. For brand new projects, it's easy: simply start writing your infrastructure as code using Pulumi from the start. But what if you already have infrastructure stood up? And perhaps even actively serving a critical business need? In these cases, you may wonder, is it even possible to adopt Pulumi, without downtime or a major disturbance to your existing infrastructure? The answer is **yes**!

This user guide offers a tour of tried-and-true tools and techniques that can be used to migrate any infrastructure to Pulumi, regardless of how that infrastructure was originally provisioned, including using any of the tools [described here]({{< prelref "/docs/intro/vs" >}}). These techniques range from coexisting with this infrastructure &mdash; either temporarily or permanently &mdash; as well as adopting infrastructure and/or converting existing infrastructure as code projects.

Below we will review some basic concepts, but feel free to jump straight to a specific guide:

* [**Importing Infrastructure**]({{< prelref "import" >}}): for any cloud, no matter how it's provisioned
* [**From Terraform**]({{< prelref "from_terraform" >}}): coexist with existing workspaces or convert your HCL
* [**From AWS CloudFormation**]({{< prelref "from_aws" >}}): coexist with, deploy, or convert your templates and stacks
* [**From Azure Resource Manager (ARM)**]({{< prelref "from_azure" >}}): coexist with, deploy, or convert your templates and deployments
* [**From Kubernetes YAML or Helm**]({{< prelref "from_kubernetes" >}}): coexist with, deploy, or convert your configuration

## Concepts

The three basic concepts for how to adopt Pulumi and deal with existing infrastructure are _coexistence_, _importing_, and _conversion_. In short, coexistence lets you provision new infrastructure alongside existing infrastructure, importing lets you adopt control of existing infrastructure into a new Pulumi program, and conversion converts existing infrastructure as code to Pulumi.

Support for these techniques differs based on how your existing infrastructure was provisioned:

|                    | [Coexistence](#coexistence) | [Importing](#importing-infrastructure) | [Conversion](#conversion) |
|--------------------|:-------:|:------:|:-------:|
| [Terraform]({{< prelref "from_terraform" >}}) | ✅      | ✅     | ✅      |
| [AWS CloudFormation]({{< prelref "from_aws" >}}) | ✅      | ✅     |         |
| [Azure ARM]({{< prelref "from_azure" >}})          | ✅      | ✅     |         |
| [Kubernetes YAML]({{< prelref "from_kubernetes" >}})    | ✅      | ✅     |         |
| Other              | ✅      | ✅     |         |

### Coexistence

Let's say you already have infrastructure provisioned by an existing tool, such as Terraform, AWS CloudFormation, or Azure Resource Manager (ARM) templates, but don't want to convert it right now. This could be for any number of reasons:

* Maybe you aren't ready to take on that effort yet and want to focus on new infrastructure.
* Perhaps that infrastructure is managed by a different team who will keep using their own tool.
* Or it could be that this infrastructure is slated to be retired after your current project anyway.

In these cases, new infrastructure can coexist with old infrastructure in two ways, letting you keep your existing infrastructure as-is while building new infrastructure under Pulumi's management. The following techniques can be used:

* [**Resource Getters**]({{< prelref "/docs/intro/concepts/programming-model#resource-get" >}}) available on every resource let you read all the details for a resource from the cloud provider based just on its ID.

* [**Stack References**]({{< prelref "/docs/intro/concepts/organizing-stacks-projects#inter-stack-dependencies" >}}) let you reference outputs of another Pulumi stack for use as inputs to a stack, which is very useful for [organizing projects and stacks]({{< prelref "/docs/intro/concepts/organizing-stacks-projects" >}}).

* **External State References** let you reference outputs from a non-Pulumi stack for use as inputs to a Pulumi stack. Many infrastructure as code tools have the notion of "outputs," which are simply values exported for easy consumption. This might be VPC IDs, auto-assigned IP addresses, and so on. Examples include [Terraform state files and workspaces]({{< prelref "from_terraform" >}}), [AWS CloudFormation stacks]({{< prelref "from_aws" >}}), and [Azure Resource Manager (ARM) deployments]({{< prelref "from_azure" >}}).

Together, these make it easy to reference existing infrastructure regardless of how it was provisioned, without Pulumi taking over control of its ongoing management.

### Importing Infrastructure

Pulumi can adopt existing infrastructure so that, going forward, it is under the control of Pulumi. This is called _importing_, and it is a great way to adopt Pulumi fully without needing to perturb or recreate existing infrastructure.

In the above coexistence scenarios, Pulumi simply _reads_ your existing infrastructure, but won't assume control of managing it. As such, Pulumi will never modify or delete infrastructure that is still managed outside of Pulumi. In the case of importing infrastructure, on the other hand, that won't be true. After the import process, all resources are entirely managed by Pulumi.

Furthermore, Pulumi doesn't care where the infrastructure originally came from. You could have manually provisioned it in your cloud's console UI, from the CLI, using Terraform, your cloud's built-in templating mechanism, and so on. In all cases, after the import process, you'll be left with a working Pulumi program, and all subequent infrastructure updates can be made with Pulumi. You can then retire the old way of managing your infrastructure. This works even if you've lost the original scripts or templates that created the infrastructure.

To learn more about how to import resources in this manner, please [refer to this guide on resource adoption]({{< prelref "import" >}}).

### Conversion

The final approach is to convert an existing infrastructure as code program to Pulumi. This preserves existing program structure &mdash; which may be important if you carefully designed your existing infrastructure as code layout in terms of names, modules, and configurability. This can be difficult if not impossible to reverse-engineer automatically during the import process.

Conversion takes care of the static program structure and will automatically generate a new, fully-functional Pulumi program that matches the source infrastructure as code program. This is usually still combined with importing so that you not only get a new program that provisions the right infrastructure, but also adopt existing infrastructure under the management of Pulumi too.

The primary conversion tool available right now is `tf2pulumi` which converts any Terraform HCL to Pulumi code. [Learn more about how to use it here.]({{< prelref "from_terraform#converting-terraform-hcl-to-pulumi" >}}).

---
title: "Adopting Pulumi"
meta_desc: Migrate from an existing infrastructure management solution to Pulumi.
menu:
  userguides:
    identifier: adopting
    weight: 2
---

If you've fallen in love with Pulumi, it might not be obvious how to adopt it. For brand new projects, it's easy: simply start writing your infrastructure as code using Pulumi from the start. But what if you already have infrastructure stood up? And perhaps even actively serving a critical business need? In these cases, you may wonder, is it even possible to adopt Pulumi, without downtime or a major disturbance to your existing infrastructure? The answer is **yes**!

This user guide offers a tour of tried-and-true tools and techniques that can be used to migrate any infrastructure to Pulumi, regardless of how that infrastructure was originally provisioned, including using any of the tools [described here]({{< relref "/docs/intro/vs" >}}). These techniques range from coexisting with this infrastructure &mdash; either temporarily or permanently &mdash; as well as adopting infrastructure and/or converting existing infrastructure as code projects.

Below we will review some basic concepts, but feel free to jump straight to a specific guide:

* [**Importing Infrastructure**]({{< relref "import" >}}): for any cloud, no matter how it's provisioned
* [**From Terraform**]({{< relref "terraform" >}}): coexist with existing workspaces or convert your HCL
* [**From AWS CloudFormation**]({{< relref "aws" >}}): coexist with, deploy, or convert your templates and stacks
* [**From Azure Resource Manager (ARM)**]({{< relref "azure" >}}): coexist with, deploy, or convert your templates and deployments
* [**From Kubernetes or Helm YAML**]({{< relref "kubernetes" >}}): coexist with, deploy, or convert your configuration

## Concepts

The three basic concepts for how to adopt Pulumi and deal with existing infrastructure are _coexistence_, _importing_, and _conversion_. In short, coexistence lets you provision new infrastructure alongside existing infrastructure, importing lets you adopt control of existing infrastructure into a new Pulumi program, and conversion converts existing infrastructure as code to Pulumi.

Support for these techniques differs based on how your existing infrastructure was provisioned:

|                    | [Coexistence](#coexistence) | [Importing](#importing-infrastructure) | [Conversion](#conversion) |
|--------------------|:-------:|:------:|:-------:|
| Terraform          | ✅      | ✅     | ✅      |
| AWS CloudFormation | ✅      | ✅     |         |
| Azure ARM          | ✅      | ✅     |         |
| Kubernetes YAML    | ✅      | ✅     |         |
| Other              | ✅      | ✅     |         |


### Coexistence

Let's say you already have infrastructure provisioned by an existing tool, such as Terraform, AWS CloudFormation, or Azure Resource Manager (ARM) templates, but don't want to convert it right now. This could be for any number of reasons:

* Maybe you aren't ready to take on that effort yet and want to focus on new infrastructure.
* Perhaps that infrastructure is managed by a different team who will keep using their own tool.
* Or it could be that this infrastructure is slated to be retired after your current project anyway.

 In these cases, new infrastructure can coexist with old infrastructure in two ways, letting you keep your existing infrastructure as-is while building new infrastructure under Pulumi's management.

#### Resource Getters

Every resource type in Pulumi has a "gettter." This allows you to look up an existing resource using its ID for purposes of reading state from it. This gives you back a fully populated Pulumi resource object whose properties can be used to initialize other resources that themselves are under Pulumi's control. For more details, [read the programming model documentation]({{< relref "/docs/intro/concepts/programming-model#resource-get" >}}).

#### Referencing Stack Outputs

Many infrastructure as code tools have the notion of "outputs," which are simply values exported for easy consumption. This might be VPC IDs, auto-assigned IP addresses, and so on. Examples of this include Terraform workspaces, AWS CloudFormation stacks, and ARM templates. In your Pulumi program, you can reference these outputs by name, much like Pulumi's [built-in "stack reference" concept]({{< relref "/docs/intro/concepts/organizing-stacks-projects#inter-stack-dependencies" >}}) which can be used for Pulumi-to-Pulumi dependencies. For details on specifics, refer to the technology-specific guide above.

### Importing Infrastructure

Pulumi can adopt existing infrastructure so that, going forward, it is under the control of Pulumi. This is called _importing_, and it is a great way to adopt Pulumi fully without needing to perturb or recreate existing infrastructure.

In the above coexistence scenarios, Pulumi simply _reads_ your existing infrastructure, but won't assume control of managing it. As such, Pulumi will never modify or delete infrastructure that is still managed outside of Pulumi. In the case of importing infrastructure, on the other hand, that won't be true. After the import process, all resources are entirely managed by Pulumi.

Furthermore, Pulumi doesn't care where the infrastructure originally came from. You could have manually provisioned it in your cloud's console UI, from the CLI, using Terraform, your cloud's built-in templating mechanism, and so on. In all cases, after the import process, you'll be left with a working Pulumi program, and all subequent infrastructure updates can be made with Pulumi. You can then retire the old way of managing your infrastructure. This works even if you've lost the original scripts or templates that created the infrastructure.

### Conversion

The final approach is to convert an existing infrastructure as code program to Pulumi. This preserves existing program structure &mdash; which may be important if you carefully designed your existing infrastructure as code layout in terms of names, modules, and configurability. This can be difficult if not impossible to reverse-engineer automatically during the import process.

Conversion takes care of the static program structure and will automatically generate a new, fully-functional Pulumi program that matches the source infrastructure as code program. This is usually still combined with importing so that you not only get a new program that provisions the right infrastructure, but also adopt existing infrastructure under the management of Pulumi too.

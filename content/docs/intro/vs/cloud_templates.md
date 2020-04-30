---
title: Pulumi vs. AWS CloudFormation and Other Templates
meta_desc: This page gives an overview of the major differences between Pulumi and Cloud Templates such as AWS CloudFormation.
linktitle: Cloud Templates
menu:
  intro:
    parent: vs
    weight: 2

aliases: ["/docs/reference/vs/cloud_templates/"]
---

All major cloud providers offer their own form of infrastructure-as-"code" solution, typically by way of JSON or
YAML-based templating solutions. This includes AWS CloudFormation and Azure Resource Manager (ARM) templates.

These markup-based configuration files are often uploaded to a hosted service in the target cloud, where a hosted
service will then process the files to create, update, or delete resources as necessary.

Pulumi offers a multi-cloud alternative to more restrictive infrastructure-as-code template solutions, like AWS CloudFormation. Pulumi allows you to streamline processes by managing resources from different platforms all in one place, using real code, in your favorite language.

Pulumi lets you use your favorite languages, instead of bespoke templating solutions such as CloudFormation. These
typically use syntaxes that are awkward, hard to learn, and even harder to remember. Pulumi programs are just real
code. Thanks to basic things like functions and classes, we've seen 25,000 line CloudFormation templates shrink to
just a few hundred lines of code. This approach also leads to far less copy and pasting between projects because you can share packages.

Pulumi is also multi-cloud. So, you only need to learn one programming model, tool, and workflow. In fact, you can
easily manage resources from different clouds, easing what would otherwise require manual orchestration. For example

* Use Azure ML, but AWS for VM, container, and/or serverless compute
* Provision a GKE Kubernetes cluster and then deploy Kubernetes apps to it
* Provision Let's Encrypt SSL certificates, Cloudflare DNS, and AWS compute resources

Pulumi also offers a first class CLI experience. The cloud solutions don't let you preview deployment diffs on
your client machine before submitting them, and generally haven't focused on a great CLI experience like Pulumi has,
because they are so service-oriented and closed source.

There are many community-led projects which allow you to write code in a real language and then emit the
configuration templates as a sort of "compilation" step. These offer nice syntactic sugar on top of the raw
templates, but the underlying model leaks through and carries forward all of the other abovementioned shortcomings.

Finally, Pulumi is [open source](https://github.com/pulumi/pulumi) and community-driven. All of the other cloud systems — such as Azure Resource Manager or AWS CloudFormation — are proprietary closed source, lead to lock-in, and lack the ability for the community to contribute to them.

To learn more about adopting Pulumi, please refer to the [AWS CloudFormation]({{< prelref "/docs/guides/adopting/from_aws" >}}) or [Azure Resource Manager (ARM)]({{< prelref "/docs/guides/adopting/from_azure" >}}) migration guides.

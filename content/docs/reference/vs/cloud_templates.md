---
title: Pulumi vs. Cloud Templates (AWS CloudFormation, etc.)
menu:
  reference:
    parent: vs
    name: Cloud Templates
    weight: 2
---

All major cloud providers offer their own form of infrastructure-as-"code" solution, typically by way of JSON or
YAML-based templating solutions. This includes AWS CloudFormation and Azure Resource Manager (ARM) templates.

These markup-based configuration files are often uploaded to a hosted service in the target cloud, where a hosted
service will then process the files to create, update, or delete resources as necessary.

Pulumi's model shares a lot with these systems. Although Pulumi programs are written in imperative, familiar languages,
they are ultimately evaluated to produce a similar set of create, update, or delete operations for your cloud resources.

This is where Pulumi begins to diverge from these other solutions, however.

Pulumi lets you use your favorite languages, instead of bespoke templating solutions. These typically use syntaxes that
are awkward, hard to learn, and even harder to remember. Pulumi programs are just real code. Thanks to basic things
like functions and classes, we've seen 25,000 line CloudFormation templates shrink to just a few hundred lines of code.
This approach also leads to far less copy and pasting between projects because you can share packages.

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

Finally, Pulumi is [open source](https://github.com/pulumi/pulumi) and community-driven. All of the cloud systems are
proprietary closed source, lead to lock-in, and lack the ability for the community to contribute to them.

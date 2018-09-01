---
title: Pulumi vs. Cloud Templates (AWS CloudFormation, etc)
---

All major cloud providers offer their own form of infrastructure-as-"code" by way of JSON or YAML-based templating
solutions. This includes

* AWS CloudFormation
* Azure Resource Manager
* Google Deployment Manager

These configuration files are often uploaded to a hosted service in the target cloud, where it will then process the
files to create, update, or delete resources as needed.

Pulumi's model shares a lot with these systems. Although Pulumi programs are written in imperative, familiar languages,
they are ultimately evaluated to produce a similar set of create, update, or delete operations for your cloud resources.

This is where Pulumi begins to diverge from these other solutions, however.

Pulumi lets you use your favorite languages. Instead of bespoke templating solutions, often tacked on to a markup
in an awkward and hard-to-learn and -remember way, Pulumi programs use real code. Thanks to simple things like
functions and classes, we have seen 25,000 line CloudFormation templates shrink to just a few 100 lines of code.
This approach also leads to far less copy and pasting between projects, because you can share packages.

Pulumi is also multi-cloud. So, you only need to learn one programming model, tool, and workflow. In fact, you can
easily manage resources from different clouds, easing what would otherwise require manual orchestration. For example

* Use Azure ML, but AWS for VM, container, and/or serverless compute
* Provision a GKE Kubernetes cluster and then deploy Kubernetes apps to it
* Provision Let's Encrypt SSL certificates, Cloudflare DNS, and AWS compute resources

Pulumi also offers a much stronger CLI experience. The cloud solutions don't let you preview deployment diffs on
your client machine before submitting them, and generally haven't focused on a great CLI experience like Pulumi has.

There are also many community-led projects which allow you to write code in a real language and then emit the
configuration templates as a sort of "compilation" step. These offer nice syntactic sugar on top of the raw
templates, but the underlying model leaks through and carries forward all of the other abovementioned shortcomings.

Finally, Pulumi is open source and community-driven. All of the cloud systems are proprietary and worsen the
lock-in situation, in addition to lacking the ability to contribute extensions to the heart of the system.

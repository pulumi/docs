---
title: Pulumi vs. Cloud Templates
meta_desc: An index of the differences between Pulumi and cloud templating solutions like AWS CloudFormation and Microsoft Azure Resource Manager (ARM).
linktitle: Cloud Templates
menu:
    intro:
        parent: vs
        identifier: templates
        weight: 2
aliases:
    - /docs/reference/vs/cloud_templates/
    - /docs/intro/vs/cloud_templates/
---

Several cloud providers offer their own form of infrastructure-as-code, typically by way of JSON- or YAML-based templating solutions. Examples include AWS CloudFormation for Amazon Web Services and Azure Resource Manager (ARM) for Microsoft Azure. Template files containing cloud resource configurations are usually uploaded to a hosted service in the target cloud, which then processes the files to create create, update, or delete cloud infrastructure resources as necessary.

While these template-based solutions are often easy to get started with, they can be cumbersome in practice and hard to maintain at scale, and they generally only apply to a single cloud provider. Pulumi takes a different approach that allows you use general-purpose programming languages like TypeScript, Python, C#, and Go to manage your infrastructure, and do target any cloud using a consistent programming model. For example, with Pulumi, you can:

* Use Azure Machine Learning in combination with AWS EC2, Amazon ECS, and AWS Lambda
* Provision GKE Kubernetes clusters and deploy Kubernetes apps into them
* Combine Let's Encrypt SSL certificates, Cloudflare DNS configuration, and AWS compute resources, all in the same program

Unlike many of these provider-specific services, Pulumi is [open source](https://github.com/pulumi/pulumi) and community-driven. To learn more about how Pulumi compares to some of these services in detail, see the following comparison docs:

* [Pulumi vs. AWS CloudFormation]({{< relref "/docs/intro/vs/cloud-templates/cloudformation" >}})

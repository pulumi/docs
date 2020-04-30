---
title: Pulumi vs. Other Solutions
meta_desc: This page gives an overivew of the major differences between Pulumi and
           infrastructure as code solutions.
linktitle: Pulumi vs. Other
menu:
  intro:
    identifier: vs
    weight: 6

aliases: ["/docs/reference/vs/"]
---

Pulumi is a cloud-native infrastructure as code project. It lets you provision and manage resources across many clouds---AWS, Azure, Google Cloud, Kubernetes, OpenStack---using your favorite language. It works great for a wide range of
cloud infrastructures and applications, including containers, virtual machines, databases, cloud services, and serverless.

Because of this broad array of supported scenarios, there are many tools that overlap with Pulumi's capabilities. Many
of these are complementary and can be used together, whereas some are "either or" decisions.

Here are several useful comparisons that will help you understand Pulumi's place in the cloud tooling ecosystem:

* [Hashicorp Terraform]({{< prelref "terraform" >}})
* [Cloud Templates (AWS CloudFormation, Azure RM, etc.)]({{< prelref "cloud_templates" >}})
* [AWS CDK and Troposphere]({{< prelref "cloud_template_transpilers" >}})
* [Cloud SDKs (AWS Boto, etc.)]({{< prelref "cloud_sdks" >}})
* [Serverless Framework]({{< prelref "serverless" >}})
* [Kubernetes YAML and DSLs]({{< prelref "k8s_yaml_dsls" >}})
* [Chef, Puppet, Ansible, Salt, etc.]({{< prelref "chef_puppet_etc" >}})
* [Custom Solutions]({{< prelref "custom" >}})

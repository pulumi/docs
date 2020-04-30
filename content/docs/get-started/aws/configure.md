---
title: Configure | AWS
h1: Configure
linktitle: Configure
meta_desc: This page provides an overview of how to configure an AWS project.
weight: 4
menu:
  getstarted:
    parent: aws
    identifier: aws-configure

aliases: ["/docs/quickstart/aws/configure/"]
---

<!-- TODO inline a streamlined version of configuring the cloud here. -->

<a href="{{< prelref "/docs/intro/cloud-providers/aws/setup" >}}" target="_blank">Configure AWS</a> so the Pulumi CLI can connect to AWS. If you have previously configured the <a href="https://aws.amazon.com/cli/" target="_blank">AWS CLI</a>, `aws`, Pulumi will respect and use your configuration settings.

If you have multiple AWS profiles set up, specify a different profile using one of the following ways:

* Set `AWS_PROFILE`as an <a href="{{< prelref "/docs/intro/cloud-providers/aws/setup#environment-variables" >}}" target="_blank">environment variable</a>, or
* After creating your project in the next step, run `pulumi config set aws:profile <profilename>`. See <a href="{{< prelref "/docs/intro/cloud-providers/aws#configuration" >}}" target="_blank">AWS Configuration</a> for more configuration options.

Next, we'll create a new project.

{{< get-started-stepper >}}

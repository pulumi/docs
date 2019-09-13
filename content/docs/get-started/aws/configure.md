---
title: Configure AWS
weight: 4
menu:
  getstarted:
    parent: aws
    identifier: aws-configure

aliases: ["/docs/quickstart/aws/configure/"]
---

<!-- TODO inline a streamlined version of configuring the cloud here. -->

<a href="{{< relref "/docs/intro/cloud-providers/aws/setup" >}}" target="_blank">Configure AWS</a> so the Pulumi CLI can connect to AWS.

If you have previously configured the <a href="https://aws.amazon.com/cli/" target="_blank">AWS CLI</a>, `aws`, Pulumi will respect and use your configuration settings.

If you have multiple AWS profiles set up, specify a different profile using one of the following ways:

* Set `AWS_PROFILE`as an <a href="{{< relref "/docs/intro/cloud-providers/aws/setup#environment-variables" >}}" target="_blank">environment variable</a>, or
* Run `pulumi config set aws:profile <profilename>`. See <a href="{{< relref "/docs/intro/cloud-providers/aws#configuration" >}}" target="_blank">AWS Configuration</a> for more configuration options.

> If this is your first time running `pulumi new` or most other `pulumi` commands, you will be prompted to log in to the [Pulumi service](https://app.pulumi.com). The [Pulumi CLI]({{< relref "/docs/reference/cli" >}}) works in tandem with the Pulumi service in order to deliver a reliable experience. It is free for individual use, with [additional features available for teams](https://www.pulumi.com/pricing/). Hitting `ENTER` at the prompt opens up a web browser allowing you to either sign in or sign up.

Next, we'll create a new project.

{{< get-started-stepper >}}

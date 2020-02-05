---
title: Configure | Alibaba Cloud
h1: Configure
linktitle: Configure
meta_desc: This page provides an overview of how to configure an Alibaba Cloud project.
weight: 4
menu:
  getstarted:
    parent: alicloud
    identifier: alicloud-configure

---

<!-- TODO inline a streamlined version of configuring the cloud here. -->

<a href="{{< relref "/docs/intro/cloud-providers/alicloud/setup" >}}" target="_blank">Configure Alibaba Cloud</a> so the Pulumi  
CLI can connect to Alibaba Cloud. If you have previously configured the <a href="https://github.com/aliyun/aliyun-cli" target="_blank">Alibaba Cloud CLI</a>
, `aliyun`, Pulumi will respect and use your configuration settings.

If you have multiple Alibaba Cloud profiles set up, specify a different profile using one of the following ways:

* Set `ALICLOUD_PROFILE`as an <a href="{{< relref "/docs/intro/cloud-providers/alicloud/setup#environment-variables" >}}" target="_blank">environment variable</a>, or
* After creating your project in the next step, run `pulumi config set alicloud:profile <profilename>`. See <a href="{{< relref "/docs/intro/cloud-providers/alicloud#configuration" >}}" target="_blank">Alibaba Cloud Configuration</a> for more configuration options.

Next, we'll create a new project.

{{< get-started-stepper >}}

---
title: Configure | Kubernetes
linktitle: Configure
meta_desc: This page provides an overview of how to configure a Kubernetes project.
weight: 4
menu:
  getstarted:
    parent: kubernetes
    identifier: kubernetes-configure

aliases: ["/docs/quickstart/kubernetes/configure/"]
---

<!-- TODO inline a streamlined version of configuring the cloud here. -->

<a href="{{< relref "/docs/intro/cloud-providers/kubernetes/setup.md" >}}" target="_blank">Configure Kubernetes</a> so the Pulumi CLI can connect to a Kubernetes cluster. If you have previously configured the <a href="https://kubernetes.io/docs/reference/kubectl/overview/" target="_blank">kubectl CLI</a>, `kubectl`, Pulumi will respect and use your configuration settings.

Next, we'll create a new project.

{{< get-started-stepper >}}

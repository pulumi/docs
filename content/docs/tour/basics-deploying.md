---
title: Deploying code
menu:
  tour:
    parent: tour
    weight: 3
---

After creating your Pulumi program, you will want to deploy it.

Deploying your program will create, update, or delete the associated cloud resources needed to run it.

The first time you spin up [a stack]({{< relref "programs-stacks.md" >}}) -- an isolated instance of your Pulumi program -- all of
these resources will be created for the first time.  Each stack has its own
[configuration]({{< relref "programs-configuring.md" >}}) and [resources]({{< relref "programs-resources.md" >}}).

From that point onward, any edits to your program result in the minimal incremental changes to your resources.

> Before deploying, you will need to configure your machine to access your cloud provider of choice.  In general, Pulumi
> just uses standard client configuration.  Please see the following instructions for details:
> [AWS]({{< relref "/docs/reference/clouds/aws/setup.md" >}}), [Azure]({{< relref "/docs/reference/clouds/azure/setup.md" >}}), [Google Cloud]({{< relref "/docs/reference/clouds/gcp/setup.md" >}}),
> [OpenStack]({{< relref "/docs/reference/clouds/openstack/setup.md" >}}), or [Kubernetes]({{< relref "/docs/reference/clouds/kubernetes/setup.md" >}}).

***

Next, let's preview a deployment before actually performing it.

<div class="tour-nav">
    <a class="tour-button enabled" href="{{< relref "basics-projects.md" >}}" title="Resources">◀</a>
    <span class="tour-index"><strong>4</strong>/8</span>
    <a class="tour-button enabled" href="{{< relref "basics-previewing.md" >}}" title="Previewing">▶</a>
</div>

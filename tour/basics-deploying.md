---
title: Deploying code
---

After creating your Pulumi program, you will want to deploy it.

Deploying your program will create, update, or delete the associated cloud resources needed to run it.

The first time you spin up [a stack](./programs-stacks.html) -- an isolated instance of your Pulumi program -- all of
these resources will be created for the first time.  Each stack has its own
[configuration](./programs-configuring.html) and [resources](./programs-resources.html).

From that point onward, any edits to your program result in the minimal incremental changes to your resources.

> Before deploying, you will need to configure your machine to access your cloud provider of choice.  In general, Pulumi
> just uses standard client configuration.  Please see the following instructions for details: [AWS](/install/aws.html),
> [Azure](/install/azure.html), [Google Cloud](/install/gcp.html), [OpenStack](/install/openstack.html), or [Kubernetes](/install/kubernetes.html).

***

Next, let's preview a deployment before actually performing it.

<div class="tour-nav">
    <a class="tour-button enabled" href="basics-projects.html" title="Resources">◀</a>
    <span class="tour-index"><strong>4</strong>/8</span>
    <a class="tour-button enabled" href="basics-previewing.html" title="Previewing">▶</a>
</div>

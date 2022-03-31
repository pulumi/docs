---
title: Six Things You Might Not Know About the Pulumi Service
date: 2022-01-24
meta_desc: |
    In this post, we'll highlight a number of the lesser-known features of the Pulumi Service that make it even easier to manage your infrastructure with Pulumi.
summary: |
    As a reader of this blog, you've probably heard of the Pulumi Service, the default state-management backend of the Pulumi CLI, and if that's the case, there's a good chance you've also heard of many of its key features. But did you know we're adding new features to the Service all the time---some of which are incredibly easy to miss? In this post, we'll highlight a few of those lesser-known features that we think make it even easier to manage your infrastructure with Pulumi.
meta_image: meta.png
authors:
    - chris-smith
    - christian-nunciato
    - laura-santamaria
tags:
    - pulumi-news
    - features
    - cloud engineering
    - policy-as-code
    - pulumi-service
    - infrastructure as code
    - pulumi-enterprise
    - continuous-delivery
---

As a reader of this blog, you've probably heard of the [Pulumi Service]({{< relref "/product/pulumi-service" >}}), the default state-management [backend]({{< relref "/docs/intro/concepts/state" >}}) of the Pulumi CLI. If that's the case, there's also a good chance you've heard of a number of the Service's key features, like helping you organize your [projects and stacks]({{< relref "/docs/intro/pulumi-service/projects-and-stacks" >}}), collaborate with others with the help of [organizations]({{< relref "/docs/intro/pulumi-service/organizations" >}}), or handle sensitive data securely with built-in support for [encrypted secrets](https://www.pulumi.com/docs/intro/concepts/secrets/).

What you might not know, though, is that we're adding new features to the Pulumi Service all the time, and that some of these features can  be fairly easy to miss. So in this post, we'll highlight a handful of the features you might _not_ be aware of, and that we think make it even easier to manage your infrastructure with Pulumi.

Let’s get started!

## Feature 1: Stack Tags

The first thing we'll cover is the [Pulumi stack tags]({{< relref "/docs/intro/concepts/stack#stack-tags" >}}) feature. Stack tags are key/value pairs that are associated with your Pulumi stack. You can use them for any number of purposes, from keeping things organized to even flagging whether or not it's okay for a script to reclaim the stack's resources.

While you can create, edit, and remove stack tags using the Pulumi CLI (see [`pulumi stack tag`]({{< relref "/docs/reference/cli/pulumi_stack_tag" >}})), you can also do so in the Pulumi Console:

![Adding and removing stack tags in the Service ](https://user-images.githubusercontent.com/274700/150612443-b0b187e1-6329-42ca-816f-01de1bc5d4ff.gif)

Once set, you can quickly filter stacks on your organization’s Projects tab as well.

![Filtering stacks by tag name](https://user-images.githubusercontent.com/274700/150613454-1554b763-2e8b-42e9-80ce-e629048bb1b9.png)

## Feature 2: Link Updates to your CI/CD pipeline

Another helpful thing the Pulumi Service can do is link the Pulumi stack update to the CI/CD job or run that was used to perform it, as well as to the specific source commit:

![The stack update header, showing links to GitHub source commit](https://user-images.githubusercontent.com/274700/150612892-f8e84597-2ce2-4687-8acc-236a57f6c6a4.png)

When Pulumi updates a stack, it will store some information about the local machine state, such the current git SHA if the stack resides in a `git` repository. It is with this data that the Pulumi Service links to relevant services where possible.

If you're curious to know all of the information Pulumi has for a stack update, you can navigate to the Environment tab for that update:

![The Environment tab of a stack update](https://user-images.githubusercontent.com/274700/150613104-510c755f-180e-4f0c-a2cb-e9f9816649e6.png)

## Feature 3: Custom Update Messages

One of the most useful pieces of additional data stored with each update is the `message` property. By default, Pulumi will use whatever the latest `git` commit message is. But did you know you can customize that message from the command line?

By passing the `--message` (or `-m`) flag to `pulumi up`, you can provide a custom update message, which can help explain the context for why you made a particular infrastructure change:

```bash
$ pulumi up --message "Release the hounds\!"
```

![An update in the Service with a custom message](https://user-images.githubusercontent.com/274700/150614494-b1c6aef1-aed0-4de5-a815-f4f8ddcef48a.png)

## Feature 4: Viewing Resource Changes

Another thing you might have missed is that the Pulumi Service supports multiple views for a stack update's logs.

The standard view mimics the Pulumi CLI's output. However, you can switch to the _Diff_ or _Diagnostic_ views, too.

The Diff view displays all of the properties of modified resources, along with their previous/updated values. This can be helpful when trying to understand exactly what happened for a stack update.

![The diff view, showing resource-property changes](https://user-images.githubusercontent.com/274700/150618931-5881cc70-36ab-4e46-b01c-53c13b8edfa1.png)

The _Diagnostic view_ just outputs so-called “diagnostic” messages from the Pulumi update. Most commonly, this is where you will see the output of things like calls to JavaScript’s `console.log(...)` or Python’s `print(...)` functions. It'll also include the output of dependent tools, like the output when building Docker containers.

![The diagnostic view, showing the output of a Docker image build](https://user-images.githubusercontent.com/274700/150619125-8067b1c6-843d-4f52-999c-69f8e184870e.png)

## Feature 5: Stack Resource Visualization

Another cool feature of the Pulumi Service is being able to visualize a stack’s resources and their relationships to one another. This is a really important feature!

One of the advantages of using an infrastructure as code tool like Pulumi is that you aren’t just creating a flat list of resources. Instead, by the virtue of how the code and resource graph is structured, you are building a graph of resources.

This means that Pulumi has a semantic understanding of not only _what_ resources are in your stack but also how they relate to one another.

If you navigate to a stack’s Resources tab, by default you see them listed in a table. You can filter this list by resource type, or by providing a custom filter:

![Filtering the resources list with a string matching the resource type (e.g., "bucket")](https://user-images.githubusercontent.com/274700/150619318-9d452d1f-dc30-4907-af6a-9941c4c5fa68.png)

However, in order to see the expanded resource graph, click the Graph View button. This will switch to rendering the resources as an interactive graph.

![All resources in a stack, rendered as a graph](https://user-images.githubusercontent.com/274700/150619812-e32419b9-db31-489f-b132-df59b4da2c9f.png)

Notice here that the resources that are part of a [_component_](https://www.pulumi.com/docs/intro/concepts/resources/#components) are grouped together. Also, you can double click on those nodes in the graph to expand or collapse them!

## Feature 6: Drilling into Resource Properties

But you don’t need to just settle for a "top-level view" of your resources. You can click on any specific resource on the Resources tab, and see all of the properties of that resource.

![The Resource details view, showing all properties of a TargetGroup resource](https://user-images.githubusercontent.com/274700/150619959-7025d772-14e5-45a7-b660-78a1fc8d769b.png)

This allows you to see all of the properties that Pulumi is tracking for that resource. It will also show you any relationships to other resources in the same stack.

The Pulumi Service also links you to the resource’s cloud provider’s console where possible, so you can see even more details.

![Linking directly to an ECS Cluster resource in the AWS Console](https://user-images.githubusercontent.com/274700/150620181-be3e7a09-3630-4898-89fa-7c7b775e1d35.png)

{{% notes %}}
Is your resource missing a link to the cloud provider console? With new services being launched from the myriad providers Pulumi supports every day, it’s hard to keep up. So if you would like us to add cloud provider links, please file an issue over in the [pulumi/console-requests](https://github.com/pulumi/console-requests/) GitHub repository so we can update our database.
{{% /notes %}}

There are plenty of other features to check out in the [Pulumi Service]({{< relref "/product/pulumi-service" >}}), and we have exciting improvements on the way! As always, feel free to stop by the [Pulumi Community Slack](https://slack.pulumi.com) to learn more, ask questions, or share anything cool you’re up to!

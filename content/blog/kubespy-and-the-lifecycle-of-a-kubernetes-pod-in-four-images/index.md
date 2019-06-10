---
title: "TODO Port frontmatter"
authors: ["chris-smith"]
tags: ["todo"]
date: "2017-01-01"
draft: true
description: "TODO: Put in a reasonable summary"
---


*This post is **part 1** in a series.*
======================================

One of the most popular features of the recent [v0.15.2
release](https://blog.pulumi.com/cloud-native-infrastructure-with-kubernetes-and-pulumi)
of Pulumi is fine-grained status updates for Kubernetes resources. On
the CLI they look like this:

![status-rich](https://blog.pulumi.com/hs-fs/hubfs/Blog/status-rich.gif?width=600&name=status-rich.gif){width="600"
sizes="(max-width: 600px) 100vw, 600px"
srcset="https://blog.pulumi.com/hs-fs/hubfs/Blog/status-rich.gif?width=300&name=status-rich.gif 300w, https://blog.pulumi.com/hs-fs/hubfs/Blog/status-rich.gif?width=600&name=status-rich.gif 600w, https://blog.pulumi.com/hs-fs/hubfs/Blog/status-rich.gif?width=900&name=status-rich.gif 900w, https://blog.pulumi.com/hs-fs/hubfs/Blog/status-rich.gif?width=1200&name=status-rich.gif 1200w, https://blog.pulumi.com/hs-fs/hubfs/Blog/status-rich.gif?width=1500&name=status-rich.gif 1500w, https://blog.pulumi.com/hs-fs/hubfs/Blog/status-rich.gif?width=1800&name=status-rich.gif 1800w"}


But wait --- how does this work exactly? What is *actually happening*
when you deploy a `Pod` to a cluster? How does a `Service` go from
uninitialized, to being allocated a public IP address? How often is my
`Deployment`'s status changing?

To answer these questions and others like them, today we're releasing
**a small tool, [`kubespy`](https://github.com/pulumi/kubespy),**
purpose-built to help you answer questions like this, by displaying the
changes made to a Kubernetes object in real time. For example, in the
following gif, we're running `kubespy status v1 Pod nginx` to watch the
changes to a `Pod`'s status as it is booted up.

We will spend the rest of this short post using `kubespy` to take a
closer look at what happens to a `Pod` when it's deployed to the
cluster.

![status](https://blog.pulumi.com/hs-fs/hubfs/Blog/status.gif?width=600&name=status.gif){width="600"
sizes="(max-width: 600px) 100vw, 600px"
srcset="https://blog.pulumi.com/hs-fs/hubfs/Blog/status.gif?width=300&name=status.gif 300w, https://blog.pulumi.com/hs-fs/hubfs/Blog/status.gif?width=600&name=status.gif 600w, https://blog.pulumi.com/hs-fs/hubfs/Blog/status.gif?width=900&name=status.gif 900w, https://blog.pulumi.com/hs-fs/hubfs/Blog/status.gif?width=1200&name=status.gif 1200w, https://blog.pulumi.com/hs-fs/hubfs/Blog/status.gif?width=1500&name=status.gif 1500w, https://blog.pulumi.com/hs-fs/hubfs/Blog/status.gif?width=1800&name=status.gif 1800w"}

What happens when you boot up a Pod?
-------------------------------------------------------------------------------

`kubespy` comes with a [simple
example](https://github.com/pulumi/kubespy/tree/master/examples/trivial-pulumi-example)
that deploys nginx using a naked `Pod`. (The example works with both the
Pulumi CLI and `kubectl`, but we hope you'll give Pulumi a shot!)

The essential gist is that `kubespy` will sit and watch for the example
`Pod` to be created or changed; once you deploy the `Pod` (either
`pulumi up` or `kubectl apply`), you will see something like the gif
above.

If you do this yourself, you will see that there are 4 updates reported
by `kubespy`, each of which individually gives us a fairly clear picture
of what Kubernetes is doing internally to try to run the `Pod`:

**First: Acknowledging the `Pod` definition is written to etcd.** The
API server receives the `Pod` definition and begins trying to schedule
it.

![1-created](https://blog.pulumi.com/hs-fs/hubfs/Blog/1-created.png?width=600&name=1-created.png){width="600"
sizes="(max-width: 600px) 100vw, 600px"
srcset="https://blog.pulumi.com/hs-fs/hubfs/Blog/1-created.png?width=300&name=1-created.png 300w, https://blog.pulumi.com/hs-fs/hubfs/Blog/1-created.png?width=600&name=1-created.png 600w, https://blog.pulumi.com/hs-fs/hubfs/Blog/1-created.png?width=900&name=1-created.png 900w, https://blog.pulumi.com/hs-fs/hubfs/Blog/1-created.png?width=1200&name=1-created.png 1200w, https://blog.pulumi.com/hs-fs/hubfs/Blog/1-created.png?width=1500&name=1-created.png 1500w, https://blog.pulumi.com/hs-fs/hubfs/Blog/1-created.png?width=1800&name=1-created.png 1800w"}**Second:
Scheduling the `Pod`.** The scheduler successfully schedules the `Pod`
to run on a node.

![2-scheduled](https://blog.pulumi.com/hs-fs/hubfs/Blog/2-scheduled.png?width=600&name=2-scheduled.png){width="600"
sizes="(max-width: 600px) 100vw, 600px"
srcset="https://blog.pulumi.com/hs-fs/hubfs/Blog/2-scheduled.png?width=300&name=2-scheduled.png 300w, https://blog.pulumi.com/hs-fs/hubfs/Blog/2-scheduled.png?width=600&name=2-scheduled.png 600w, https://blog.pulumi.com/hs-fs/hubfs/Blog/2-scheduled.png?width=900&name=2-scheduled.png 900w, https://blog.pulumi.com/hs-fs/hubfs/Blog/2-scheduled.png?width=1200&name=2-scheduled.png 1200w, https://blog.pulumi.com/hs-fs/hubfs/Blog/2-scheduled.png?width=1500&name=2-scheduled.png 1500w, https://blog.pulumi.com/hs-fs/hubfs/Blog/2-scheduled.png?width=1800&name=2-scheduled.png 1800w"}**Third:
Creating the `Pod`.** The kubelet running on the node receives the `Pod`
definition and begins "creating" the `Pod`. This involves pulling the
container image, adding volume mounts, *etc*. At the end of all of this,
it will attempt to run the container.

![3-creating](https://blog.pulumi.com/hs-fs/hubfs/Blog/3-creating.png?width=600&name=3-creating.png){width="600"
sizes="(max-width: 600px) 100vw, 600px"
srcset="https://blog.pulumi.com/hs-fs/hubfs/Blog/3-creating.png?width=300&name=3-creating.png 300w, https://blog.pulumi.com/hs-fs/hubfs/Blog/3-creating.png?width=600&name=3-creating.png 600w, https://blog.pulumi.com/hs-fs/hubfs/Blog/3-creating.png?width=900&name=3-creating.png 900w, https://blog.pulumi.com/hs-fs/hubfs/Blog/3-creating.png?width=1200&name=3-creating.png 1200w, https://blog.pulumi.com/hs-fs/hubfs/Blog/3-creating.png?width=1500&name=3-creating.png 1500w, https://blog.pulumi.com/hs-fs/hubfs/Blog/3-creating.png?width=1800&name=3-creating.png 1800w"}**Fourth:
Marking the `Pod` as `Running`.** The kubelet has now resolved the image
tag to a specific SHA, pulled it to the node, has successfully applied
the required configuration, and has successfully started the `nginx`
container. In this case, the `Pod` contains only one container to run,
and once it's initialized, the whole `Pod` gets marked running.

![4-running](https://blog.pulumi.com/hs-fs/hubfs/Blog/4-running.png?width=600&name=4-running.png){width="600"
sizes="(max-width: 600px) 100vw, 600px"
srcset="https://blog.pulumi.com/hs-fs/hubfs/Blog/4-running.png?width=300&name=4-running.png 300w, https://blog.pulumi.com/hs-fs/hubfs/Blog/4-running.png?width=600&name=4-running.png 600w, https://blog.pulumi.com/hs-fs/hubfs/Blog/4-running.png?width=900&name=4-running.png 900w, https://blog.pulumi.com/hs-fs/hubfs/Blog/4-running.png?width=1200&name=4-running.png 1200w, https://blog.pulumi.com/hs-fs/hubfs/Blog/4-running.png?width=1500&name=4-running.png 1500w, https://blog.pulumi.com/hs-fs/hubfs/Blog/4-running.png?width=1800&name=4-running.png 1800w"}

### Exercises:

1.  Try inducing an error and see what `kubespy` outputs! Make the image
    tag nonsense, add a volume that doesn't exist, and so on.
2.  Try booting up a service! See what `kubespy` displays under various
    configurations!  

Conclusions, and the subtleties of the Pod API.
----------------------------------------------------------------------------------------------------

This post shows a fairly basic, happy-path use of `Pods`, and shows that
we can `kubespy status` to see exactly what our containers are up to.

But wait --- what does `Running` mean, precisely? If a `Pod` is
`Running`, does that mean it's healthy? If a `Pod` has multiple
containers, and one crashes, does it still get marked `Running`? Are
there any other settings that can change when a `Pod` is marked
`Running`?

Unfortunately, though the `Pod` is the atomic compute abstraction of
Kubernetes (or perhaps *because* of this), the answer to these questions
turns out to be fairly subtle. But, because `Pod`s are so important, we
should endeavor to answer them anyway!

In the next post, we will `kubespy` to observe some of the subtleties of
the `Pod` lifecycle, and especially the effect of `restartPolicy` on the
semantics of the `Pod` object. We will also talk about some of the best
practices we've accumulated, and describe how we solved the problem of
repeatable `Pod` deployments in Pulumi.

**If you enjoyed this post, or are curious to see how this lifecycle is
baked into the Pulumi CLI, please [give us a
shot](https://www.pulumi.com/kubernetes/)! We'd love to have your
feedback.**


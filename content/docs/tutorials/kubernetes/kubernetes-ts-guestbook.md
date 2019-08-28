---
title: "Kubernetes Guestbook (Two Ways)"
---

<a href="https://app.pulumi.com/new?template=https://github.com/pulumi/examples/tree/master/kubernetes-ts-guestbook" target="_blank">
    <img src="https://get.pulumi.com/new/button.svg" alt="Deploy" style="float: right; padding: 8px; margin-top: -65px; margin-right: 8px">
</a>

<p class="mb-4">
    <a class="btn btn-secondary" href="https://github.com/pulumi/examples/tree/master/kubernetes-ts-guestbook" target="_blank"><i class="fab fa-github pr-2"></i> VIEW CODE</a>
</p>


A port of the standard [Kubernetes Guestbook](https://kubernetes.io/docs/tutorials/stateless-application/guestbook/)
to Pulumi. This example shows you how to build and deploy a simple, multi-tier web application using Kubernetes and
Docker, and consists of three components:

* A single-instance Redis master to store guestbook entries
* Multiple replicated Redis instances to serve reads
* Multiple web frontend instances

There is an [interactive Tutorial available](https://www.pulumi.com/docs/reference/tutorials/kubernetes/tutorial-guestbook/) for
this example. If this is your first time using Pulumi for Kubernetes, we recommend starting there.

In this directory, you will find two variants of the Guestbook:

1. [simple/](./simple) is a straight port of the original YAML.
2. [components](./components) demonstrates benefits of using a real language, namely eliminating boilerplate through
   the use of real component abstractions.

Both examples provision the exact same Kubernetes Guestbook application, but showcase different aspects of Pulumi.


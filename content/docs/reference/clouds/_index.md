---
title: Supported Clouds
menu:
  reference:
    identifier: clouds
    weight: 4
---

Pulumi supports many clouds using the same languages, CLI, and deployment workflow.

To quickly get started with Pulumi see the [Get Started]({{< relref "/docs/quickstart" >}}) guide.

* [AWS]({{< relref "./aws" >}})
* [Azure]({{< relref "./azure" >}})
* [Google Cloud]({{< relref "./gcp" >}})
* [Kubernetes]({{< relref "./kubernetes" >}})
* [Open Stack]({{< relref "./openstack" >}})

If your cloud isn't listed, it is possible we have it on [GitHub](https://github.com/pulumi) and/or in
[our Examples](https://github.com/pulumi/examples). Please [contact us]({{< relref "troubleshooting.md" >}}) to inquire and let us know.

## Languages

Pulumi is a multi-language runtime. Your choice of language does not affect which clouds may be
targeted -- each language is just as capable as the other and supports the entire surface area of resources available.

* [Node.js]({{< relref "javascript.md" >}}) - JavaScript, TypeScript, or any other Node.js compatible language
* [Python 3]({{< relref "python.md" >}}) - Python 3.6 or greater
* Go - statically compiled Go binaries (*documentation coming soon*)

If your favorite language isn't listed, it may be on its way soon. (It is, in fact, possible
[to add your own language]({{< relref "../faq.md/#how-can-i-add-support-for-my-favorite-cloud" >}}).)
In either case, please [contact us]({{< relref "troubleshooting.md" >}}) to inquire and let us know what you're looking for.

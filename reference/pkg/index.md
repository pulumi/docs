---
title: API Reference
---

{% include mini-toc.html %}

All Pulumi libraries are distributed in your chosen language's package manager, even those packages that define
cloud resource definitions. That means NPM for Node.js and PyPI for Python, for instance. There is a dedicated
package for each cloud that includes access to its full capabilities, including containers, serverless functions,
infrastructure, data services, and more.

In addition to the cloud packages, Pulumi offers many convenience libraries that make common tasks easier, like
setting up a network, creating a Kubernetes cluster, and building and publishing containers to private registries.

These packages can be mixed to enable multi-cloud and a spectrum of control to productivity:

![Pulumi Library Architecture](/images/reference/pkg-arch-layers.png)

You can read further documentation specific to each language here:
* [JavaScript/TypeScript](nodejs)
* [Python](python)
* Go (coming soon!)

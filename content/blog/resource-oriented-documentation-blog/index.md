---
title: "Resource Oriented Documentation"
date: 2020-04-02T11:34:07-05:00
meta_desc: "Pulumi documentation features a resource-oriented format presented as a single page per resource for easier reading, discovery, and navigation."
meta_image: docs.png
authors:
    - luke-hoban
tags:
    - documentation
---

We know that resource documentation is one of the most important areas of the Pulumi docs site for most Pulumi users, and we've heard the feedback that there is room to improve on these resource docs! Yesterday, we took a major step in rolling out a brand new approach to resource docs for Pulumi.

<!--more-->

## A New Format

These new docs are resource-oriented instead of API-oriented and are presented as a single page per resource for easier reading, discovery, and navigation.  They also support switching on different Pulumi languages inline.  API docs for each language are still available and are deep-linked into from these resource docs.  But in general, we expect to lead with these resource-oriented docs throughout our content as canonical, language-agnostic reference for each Pulumi resource.

We've rolled out these new docs so far for AWS, Azure, and GCP, with the rest of the providers on their way soon.  We continue to work on many more improvements in addition to these new docs, so expect to continue to see improvements over the coming days and weeks.  (Before you ask - Kubernetes docs are coming next!)

{{< figure src="image.png" caption="Now Python, GO and C# users can (easily) see what all the fuss is about." >}}


We'd love your feedback on the new docs either in #docs, in GitHub, or via the <i class="fas fa-thumbs-up"></i> / <i class="fas fa-thumbs-down"></i> buttons on the site.

Here are a few pointers:

- An example resource, [SQS](https://www.pulumi.com/docs/reference/pkg/aws/sqs/queue/)
- [AWS package](https://www.pulumi.com/docs/reference/pkg/aws/)
- [Azure package](https://www.pulumi.com/docs/reference/pkg/azure/)
- [GCP package](https://www.pulumi.com/docs/reference/pkg/gcp/)
- [Root API reference](https://www.pulumi.com/docs/reference/pkg/)

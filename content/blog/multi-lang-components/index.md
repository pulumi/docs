---
title: "Write once, use anywhere with multi-language components"
date: 2021-02-09
draft: false
meta_desc: Multi-language Pulumi components can be used from all supported languages - Python, Go, .NET, and TypeScript.
meta_image: meta.png
authors:
    - levi-blackstone
tags:
    - eks
    - .net
    - python
    - go
    - typescript
---

Today we're excited to announce support for one of our most highly-requested features: multi-language components! Our
first multi-language component is the popular [EKS package], which was previously only available for TypeScript. With the
[v0.22.0 release], teams can [manage EKS clusters] in their language of choice (Python, .NET, Go, and TypeScript).

<!--more-->

Pulumi's support for many familiar programming languages means that your organization is free to choose which supported
language works best for each team. It's already possible to collaborate across languages by using separate Pulumi projects
and referring to them using [Stack References]. Multi-language components take this one step further towards the vision of
"write once, use anywhere". Component authors broaden their reach across languages, and users benefit from the work
of a much larger community.

Multi-language component support allows component authors to project their API into all Pulumi-supported languages
idiomatically and without requiring knowledge of all of these languages. First-class authoring support for multi-language
components is in the works.

Check out our recent Modern Infrastructure Wednesday video to see this feature in action!

{{< youtube "gxLyAr0lUg0?rel=0" >}}

<!-- markdownlint-disable url -->
[EKS package]: {{< relref "/docs/reference/pkg/eks" >}}
[v0.22.0 release]: https://github.com/pulumi/pulumi-eks/releases/tag/v0.22.0
[manage EKS clusters]: {{< relref "/blog/easily-create-and-manage-aws-eks-kubernetes-clusters-with-pulumi" >}}
[Stack References]: {{< relref "/docs/intro/concepts/organizing-stacks-projects#inter-stack-dependencies" >}}
<!-- markdownlint-enable url -->

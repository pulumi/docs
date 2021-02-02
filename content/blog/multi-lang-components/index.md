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

Pulumi's infrastructure as code tooling combines the programming languages and tools you already know with the full power of cloud
infrastructure. But, until now, some of that Pulumi components for that cloud infrastructure, like our popular [EKS package], were
only available in a subset of the languages supported by Pulumi.

Now, with multi-language components, anyone can author a Pulumi component once, in the language they prefer, and make it available
across all Pulumi languages. To celebrate, we've taken that [EKS package]–previously only available for TypeScript–
and brought it to all four Pulumi languages: TypeScript, Python, .NET, and Go. Now, regardless of the language you choose, you can
[manage EKS clusters] with Pulumi, starting with the [v0.22.0 release of the EKS package]. Check out our Modern Infrastructure
Wednesday video to see it in action:

{{< youtube "gxLyAr0lUg0?rel=0" >}}

<!--more-->

EKS in all languages is just the start of the multi-language components story. Multi-language components enable all organizations to choose 
the right programming language, or languages, for each team and each product. Your infrastructure or platform teams will be able to
write components in Go and share them with a webapp team using TypeScript, or write in .NET and share with a machine learning team
using Python, or any other combination that suits your business. Similarly, any member of the worldwide Pulumi community can author
a component in the language they're most comfortable with and share it with all Pulumi users.

The next step in the story is a seamless authoring experience that enables component creators to write, build, and publish components, all
without needing detailed knowledge of the various Pulumi languages. We're excited for you to try it soon - check back here for updates!

<!-- markdownlint-disable url -->
[EKS package]: {{< relref "/docs/reference/pkg/eks" >}}
[v0.22.0 release of the EKS package]: https://github.com/pulumi/pulumi-eks/releases/tag/v0.22.0
[manage EKS clusters]: {{< relref "/blog/easily-create-and-manage-aws-eks-kubernetes-clusters-with-pulumi" >}}
<!-- markdownlint-enable url -->

---
title: "Use Amazon Elastic Kubernetes Service (EKS) in any Pulumi language"
date: 2021-02-04
draft: false
meta_desc: The pulumi-eks package is now available in all Pulumi languages&#58; Python, Go, .NET, and TypeScript.
meta_image: multi-lang.png
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
infrastructure. Until now, some Pulumi components for cloud infrastructure, like our popular [EKS package], were
only available in a subset of the languages supported by Pulumi.

Now, you can use the [EKS package]–previously only available for TypeScript–in all four Pulumi languages: TypeScript, Python, .NET,
and Go. Regardless of the language you choose, you can [manage EKS clusters] with Pulumi, starting with the [v0.22.0 release of the
EKS package]. Check out our Modern Infrastructure Wednesday video to see it in action:

{{< youtube "gxLyAr0lUg0?rel=0" >}}

<!--more-->

EKS in all languages is made possible by our ongoing work to enable "multi-language components". With multi-language components,
a developer can author a Pulumi component in their preferred language and then publish it for all Pulumi languages—without needing
detailed knowledge of the other Pulumi languages.

EKS in all languages is just the start of this story. Multi-language components will enable all organizations to choose
the right programming language, or languages, for each team and each product. Your infrastructure or platform teams will be able to
write components in Go and share them with a webapp team using TypeScript, or write in .NET and share with a machine learning team
using Python or any other combination that suits your business. Similarly, any member of the worldwide Pulumi community will be able to
author a component in the language they're most comfortable with and share it with all Pulumi users.

The next step in the story is a seamless authoring experience that enables component creators to write, build, and publish components
without detailed knowledge of the various Pulumi languages. We're excited for you to try it soon - check back here for updates!

<!-- markdownlint-disable url -->
[EKS package]: {{< relref "/docs/reference/pkg/eks" >}}
[v0.22.0 release of the EKS package]: https://github.com/pulumi/pulumi-eks/releases/tag/v0.22.0
[manage EKS clusters]: {{< relref "/blog/easily-create-and-manage-aws-eks-kubernetes-clusters-with-pulumi" >}}
<!-- markdownlint-enable url -->
